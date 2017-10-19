''' showversion.py

Example parser class

'''
import xmltodict
import re

from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional, Or, And, \
                                         Default, Use

try:
    from ats import tcl
    from ats.tcl.keyedlist import KeyedList

    def OrKeyedList(default):
        return Or(default, KeyedList({}))

except ImportError:
    def OrKeyedList(default):
        return default

def regexp(expression):
    def match(value):
        if re.match(expression,value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                              %(value,expression))
    return match

def _merge_dict(a, b, path=None):
    '''merges b into a for as many level as there is'''
    # Dict to use to return
    ret = a
    if path is None:
        path = []
    for key in b:
        if key in ret:
            if isinstance(ret[key], dict) and isinstance(b[key], dict):
                _merge_dict(ret[key], b[key], path + [str(key)])
            elif ret[key] == b[key]:
                # same leaf value so do nothing
                pass
            else:
                # Any other case
                raise Exception('{key} cannot be merged as it already '
                                'exists with type '
                                '{ty}.'.format(key=key, ty=type(ret[key])))
        else:
            ret[key] = b[key]
    return ret

class ShowIpOspfSchema(MetaParser):

    schema = {'process_id':
                {Any():
                    {'vrf':
                        {Any():
                            {Optional('id'): str,
                             Optional('num_of_areas'): str,
                             Optional('num_of_normal_areas'): str,
                             Optional('num_of_stub_areas'): str,
                             Optional('num_of_nssa_areas'): str,
                             Optional('ospf_rtr_type'): str,
                             Optional('reference_bandwidth'): str,
                             Optional('area'):
                                 {Optional(regexp('(.*)')):
                                     {Optional('loopback_interfaces'): OrKeyedList(str),
                                      Optional('interfaces_in_this_area'): OrKeyedList(str),
                                      Optional('default_cost'): str,
                                      Optional('active_interfaces'): OrKeyedList(str)},
                                 },
                            }
                        },
                    }
                },
             }

class ShowIpOspf(ShowIpOspfSchema, MetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).


    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        # result = tcl.q.caas.abstract(device=self.device.handle,
        #                              exec='show ip ospf')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')
        cmd = 'show ip ospf'.format()
        out = self.device.execute(cmd)
        ospf_dict = {}
        entry = None
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Routing +Process +\"ospf +(?P<process_id>[0-9]+)\" +with +ID +(?P<router_id>[0-9\.]+)$')
            m = p1.match(line)
            if m:
                if 'process_id' not in ospf_dict:
                    ospf_dict['process_id'] = {}
                pid = m.groupdict()['process_id']
                ospf_dict['process_id'][pid] = {}
                rid = m.groupdict()['router_id']
                vrf = 'default'
                continue

            p2 = re.compile(r'^\s*Connected +to +(?P<type>[a-zA-Z ]+), +VRF +(?P<vrf>.*)$')
            m = p2.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                if 'vrf' not in ospf_dict['process_id'][pid]:
                    ospf_dict['process_id'][pid]['vrf'] = {}
                if vrf not in ospf_dict['process_id'][pid]['vrf']:
                    ospf_dict['process_id'][pid]['vrf'][vrf] = {}
                ospf_dict['process_id'][pid]['vrf'][vrf] = {}
                continue

            p3 = re.compile(r'^\s*It is an (?P<ospf_rtr_type>.*)$')
            m = p3.match(line)
            if m:
                if 'vrf' not in ospf_dict['process_id'][pid]:
                    ospf_dict['process_id'][pid]['vrf'] = {}
                if vrf not in ospf_dict['process_id'][pid]['vrf']:
                    ospf_dict['process_id'][pid]['vrf'][vrf] = {}

                ospf_dict['process_id'][pid]['vrf'][vrf]['ospf_rtr_type'] = m.groupdict()['ospf_rtr_type']
                continue

            p4 = re.compile(r'^\s*Number +of +areas +in +this +router +is (?P<num_of_areas>[0-9]+). '
                         r'(?P<num_of_normal_areas>[0-9]+) normal (?P<num_of_stub_areas>[0-9]+) '
                         r'stub (?P<num_of_nssa_areas>[0-9]+) nssa')
            m = p4.match(line)
            if m:
                if 'vrf' not in ospf_dict['process_id'][pid]:
                    ospf_dict['process_id'][pid]['vrf'] = {}
                if vrf not in ospf_dict['process_id'][pid]['vrf']:
                    ospf_dict['process_id'][pid]['vrf'][vrf] = {}

                ospf_dict['process_id'][pid]['vrf'][vrf]['id'] = rid
                ospf_dict['process_id'][pid]['vrf'][vrf]['num_of_areas'] = m.groupdict()['num_of_areas']
                ospf_dict['process_id'][pid]['vrf'][vrf]['num_of_normal_areas'] = m.groupdict()['num_of_normal_areas']
                ospf_dict['process_id'][pid]['vrf'][vrf]['num_of_stub_areas'] = m.groupdict()['num_of_stub_areas']
                ospf_dict['process_id'][pid]['vrf'][vrf]['num_of_nssa_areas'] = m.groupdict()['num_of_nssa_areas']
                continue

            p5 = re.compile(r'^\s*Reference +bandwidth +unit +is (?P<reference_bandwidth>[0-9a-zA-Z ]+)$')
            m = p5.match(line)
            if m:
                ospf_dict['process_id'][pid]['vrf'][vrf]['reference_bandwidth'] = m.groupdict()['reference_bandwidth']
                continue

            p6 = re.compile(r'^\s+Area +(?P<area>BACKBONE\(0\)|[0-9]|[0-9\.]+)')
            m = p6.match(line)
            if m:
                area = m.groupdict()['area']
                if 'area' not in ospf_dict['process_id'][pid]['vrf'][vrf]:
                    ospf_dict['process_id'][pid]['vrf'][vrf]['area'] = {}
                if area not in ospf_dict['process_id'][pid]['vrf'][vrf]['area']:
                    ospf_dict['process_id'][pid]['vrf'][vrf]['area'][area] = {}
                continue

            p7 = re.compile(r'\s+Number +of +interfaces +in +this +area +is +(?P<interfaces_in_this_area>\d+) '
                         r'+\((?P<loopback_interfaces>\d+) +loopback\)$')
            m = p7.match(line)
            if m:
                ospf_dict['process_id'][pid]['vrf'][vrf]['area'][area]['interfaces_in_this_area'] = m.groupdict()['interfaces_in_this_area']
                ospf_dict['process_id'][pid]['vrf'][vrf]['area'][area]['loopback_interfaces'] = m.groupdict()['loopback_interfaces']
                continue

            p8 = re.compile(r'\s+Number +of +interfaces +in +this +area +is +(?P<interfaces_in_this_area>\d+) '
                         r'+\((?P<passive_interfaces>\d+) + passive\)$')
            m = p8.match(line)
            if m:
                ospf_dict['process_id'][pid]['vrf'][vrf]['area'][area]['interfaces_in_this_area'] = m.groupdict()['interfaces_in_this_area']
                ospf_dict['process_id'][pid]['vrf'][vrf]['area'][area]['passive_interfaces'] = m.groupdict()['passive_interfaces']
                continue
            p9 = re.compile(r'\s+Number +of +interfaces +in +this +area +is +(?P<interfaces_in_this_area>\d+)$')
            m = p9.match(line)
            if m:
                ospf_dict['process_id'][pid]['vrf'][vrf]['area'][area]['interfaces_in_this_area'] = m.groupdict()['interfaces_in_this_area']
                continue
        return ospf_dict

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ip ospf | xml')
        result = tcl.cast_any(output[1])

        return result

    def yang(self):
        ''' parsing mechanism: yang

        Function yang() defines the yang type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''

        ret = {}
        cmd = '''<native><router><ospf/></router></native>'''
        output = self.device.get(('subtree', cmd))

        for data in output.data:
            for native in data:
                for ospf in native:
                    process_id = None
                    nsr = None
                    vrf = 'default'
                    ref = None
                    router_id = None
                    id_value = 0
                    default_cost = None
                    process_id = None
                    areas = {}
                    for value in ospf:
                        # Remove the namespace
                        text = value.tag[value.tag.find('}')+1:]
                        if text == 'id':
                            process_id = value.text
                            continue
                        if text == 'nsr':
                            nsr = value.text
                            continue
                        if text == 'vrf':
                            vrf = value.text
                            continue
                        if text == 'auto-cost':
                            for auto in value:
                                text = auto.tag[auto.tag.find('}')+1:]
                                if text == 'reference-bandwidth':
                                    ref = auto.text
                            continue
                        if text == 'router-id':
                            router_id = value.text
                            continue

                        # Can have multiple area in one ospf
                        if text == 'area':
                            id_value = 0
                            default_cost = None
                            for area in value:
                                text = area.tag[area.tag.find('}')+1:]
                                if text == 'id':
                                    id_value = area.text
                                if text == 'default-cost':
                                    default_cost = area.text
                            areas[id_value] = {}
                            areas[id_value]['default_cost'] = default_cost


                    # Let's build it now
                    if 'process_id' not in ret:
                        ret['process_id'] = {}
                    ret['process_id'][process_id] = {}
                    ret['process_id'][process_id]['vrf'] = {}
                    ret['process_id'][process_id]['vrf'][vrf] = {}
                    if router_id is not None:
                        ret['process_id'][process_id]['vrf'][vrf]['id'] = router_id
                    if areas != {}:
                        ret['process_id'][process_id]['vrf'][vrf]['area'] = areas
                    if ref is not None:
                        ret['process_id'][process_id]['vrf'][vrf]['reference_bandwidth'] = ref
                    if nsr is not None:
                        ret['process_id'][process_id]['vrf'][vrf]['nsr'] = nsr

        return ret

    def yang_cli(self):
        cli_output = self.cli()
        yang_output = self.yang()
        merged_output = _merge_dict(yang_output,cli_output)
        return merged_output

class ShowIpOspfNeighborDetailSchema(MetaParser):
    schema = {Optional('intf_list'): list,
              'intf':
                {Any():
                     {'neighbor': str,
                      'interface_address': str,
                      Optional('interface_id'): str,
                      'area': str,
                      'state': str,
                      'state_changes': str,
                      'neigh_priority': str,
                      'dr': str,
                      'bdr':str,
                      'uptime':str}
                },
            }

class ShowIpOspfNeighborDetail(ShowIpOspfNeighborDetailSchema, MetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).


    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show ip ospf neighbor detail'.format()
        out = self.device.execute(cmd)
        intf_list = []
        ospf_neigh_dict = {}
        entry = None
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Neighbor\s+(?P<neighbor>\S+),\s*interface\s+address\s+(?P<interface_address>\S+)(,)?(\s)?'
                             '(interface-id +(?P<interface_id>\w+))?$')
            m = p1.match(line)
            if m:
                interface_address = m.groupdict()['interface_address']
                neighbor = m.groupdict()['neighbor']
                interface_id = m.groupdict()['interface_id']

            p2 = re.compile(r'^\s*In\s+the\s+area\s+(?P<area>\S+)\s+via\s+interface\s+(?P<interface>\S+)$')
            m = p2.match(line)
            if m:
                if 'intf' not in ospf_neigh_dict:
                    ospf_neigh_dict['intf'] = {}
                intf = m.groupdict()['interface']
                intf_list.append(intf)
                ospf_neigh_dict['intf'][intf] = {}
                ospf_neigh_dict['intf'][intf]['area'] = m.groupdict()['area']
                ospf_neigh_dict['intf'][intf]['interface_address'] = interface_address
                ospf_neigh_dict['intf'][intf]['neighbor'] = neighbor
                if interface_id and 'unknwon' not in interface_id:
                    ospf_neigh_dict['intf'][intf]['interface_id'] = interface_id
                continue

            # Neighbor priority is 0, State is 2WAY, 2 state changes
            p3 = re.compile(r'^ *Neighbor +priority +is +(?P<neigh_pri>[0-9]+), '
                            r'State +is +(?P<state>\w+), '
                            r'+(?P<state_changes>\d+) +state +changes$')
            m = p3.match(line)
            if m:
                ospf_neigh_dict['intf'][intf]['neigh_priority'] = m.groupdict()['neigh_pri']
                ospf_neigh_dict['intf'][intf]['state'] = m.groupdict()['state']
                ospf_neigh_dict['intf'][intf]['state_changes'] = m.groupdict()['state_changes']
                continue

            p4 = re.compile(r'^\s*DR\s+is\s+(?P<dr>\S+)\s+BDR\s+is\s+(?P<bdr>\S+)$')
            m = p4.match(line)
            if m:
                ospf_neigh_dict['intf'][intf]['dr'] = m.groupdict()['dr']
                ospf_neigh_dict['intf'][intf]['bdr'] = m.groupdict()['bdr']
                continue

            p5 = re.compile(r'^\s*Neighbor\s+is\s+up\s+for\s+(?P<uptime>\S+)$')
            m = p5.match(line)
            if m:
                ospf_neigh_dict['intf'][intf]['uptime'] = m.groupdict()['uptime']
                continue


        if intf_list:
            ospf_neigh_dict['intf_list'] = intf_list

        return ospf_neigh_dict

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ip ospf neighbor detail | xml')
        result = tcl.cast_any(output[1])

        return result

class ShowIpOspfInterfaceSchema(MetaParser):
    schema = {Optional('intfs_all'): OrKeyedList(list),
              Optional('intfs_up'): OrKeyedList(list),
              Optional('intfs_down'): OrKeyedList(list),
              'intf':
                {Any():
                     {'intf_state': str,
                      Optional('prot_state'): OrKeyedList(str),
                      'addr': str,
                      'mask': str,
                      'area': str,
                      'pid': str,
                      'rid': str,
                      'ntype': str,
                      'cost': str,
                      Optional('hello_timer'): str,
                      Optional('dead_timer'): str,
                      Optional('retransmit_timer'): str,
                      Optional('wait_timer'): str,
                      Optional('tdelay'): OrKeyedList(str),
                      Optional('ospf_state'): OrKeyedList(str),
                      Optional('pri'): OrKeyedList(str)}
                },
            }


class ShowIpOspfInterface(ShowIpOspfInterfaceSchema,MetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).


    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show ip ospf interface'.format()
        out = self.device.execute(cmd)
        intfs_all = []
        intfs_up = []
        intfs_down = []
        ospf_intf_dict = {}
        entry = None
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*(?P<intf>\S+) +is +(?P<intf_state>[a-zA-Z]+), *line +protocol +is +(?P<prot_state>[a-zA-Z0-9\-]+)?(\s)?([a-z\(\)]+)?$')
            m = p1.match(line)

            if m:
                intf = m.groupdict()['intf']
                if 'intf' not in ospf_intf_dict:
                    ospf_intf_dict['intf'] = {}
                if intf not in ospf_intf_dict['intf']:
                    ospf_intf_dict['intf'][intf] = {}
                intf_state = m.groupdict()['intf_state']
                ospf_intf_dict['intf'][intf]['intf_state'] = intf_state
                prot_state = m.groupdict()['prot_state']
                ospf_intf_dict['intf'][intf]['prot_state'] = prot_state
                intfs_all.append(intf)
                if intf_state == 'up' and prot_state == 'up':
                    intfs_up.append(intf)
                else:
                    intfs_down.append(intf)
                continue

            p1_2 = re.compile(r'^\s*(?P<intf>\S+)\s+is\s+administratively\s+(?P<intf_state>up|down),\s*line\s+protocol\s+is\s+(?P<prot_state>up|down)$')
            m = p1_2.match(line)

            if m:
                intf = m.groupdict()['intf']
                if 'intf' not in ospf_intf_dict:
                    ospf_intf_dict['intf'] = {}
                if intf not in ospf_intf_dict['intf']:
                    ospf_intf_dict['intf'][intf] = {}
                intf_state = m.groupdict()['intf_state']
                ospf_intf_dict['intf'][intf]['intf_state'] = intf_state
                prot_state = m.groupdict()['prot_state']
                ospf_intf_dict['intf'][intf]['prot_state'] = prot_state
                intfs_all.append(intf)
                if intf_state == 'up' and prot_state == 'up':
                    intfs_up.append(intf)
                else:
                    intfs_down.append(intf)

            p2 = re.compile(r'^\s*Internet +Address +(?P<ip_addr>[0-9\.]+)/(?P<mask>[0-9]+), +(Interface ID (?P<intf_id>[0-9]+))?(, )?Area +(?P<area>[0-9]+)')
            m = p2.match(line)
            if m:
                addr = m.groupdict()['ip_addr']
                ospf_intf_dict['intf'][intf]['addr'] = addr
                mask = m.groupdict()['mask']
                ospf_intf_dict['intf'][intf]['mask'] = mask
                area = m.groupdict()['area']
                ospf_intf_dict['intf'][intf]['area'] = area
                continue

            p3 = re.compile(r'^\s*Process\s+ID\s+(?P<pid>[^,]+),\s*Router\s+ID\s+(?P<rid>[^,]+),'
                            r'\s*Network\s+Type\s+(?P<ntype>[^,]+),\s*Cost:\s+(?P<cost>\S+)')
            m = p3.match(line)
            if m:
                pid = m.groupdict()['pid']
                ospf_intf_dict['intf'][intf]['pid'] = pid
                rid = m.groupdict()['rid']
                ospf_intf_dict['intf'][intf]['rid'] = rid
                ntype = m.groupdict()['ntype']
                ospf_intf_dict['intf'][intf]['ntype'] = ntype
                cost = m.groupdict()['cost']
                ospf_intf_dict['intf'][intf]['cost'] = cost
                continue

            p3 = re.compile(r'^\s*Transmit\s+Delay\s+is\s+(?P<tdelay>[^,]+),'
                            r'\s*State\s+(?P<ospf_state>[^,]+),\s*Priority\s+(?P<pri>[^,]+)')
            m = p3.match(line)
            if m:
                if 'intf' not in ospf_intf_dict:
                    ospf_intf_dict['intf'] = {}

                tdelay = m.groupdict()['tdelay']
                ospf_intf_dict['intf'][intf]['tdelay'] = tdelay
                ospf_state = m.groupdict()['ospf_state']
                ospf_intf_dict['intf'][intf]['ospf_state'] = ospf_state
                pri = m.groupdict()['pri']
                ospf_intf_dict['intf'][intf]['pri'] = pri
                continue

            p4 = re.compile(r'^\s*Timer +intervals +configured, +Hello +(?P<hello_timer>[0-9]+), '
                            r'+Dead +(?P<dead_timer>[0-9]+), '
                            r'+Wait +(?P<wait_timer>[0-9]+), '
                            r'+Retransmit +(?P<retransmit_timer>[0-9]+)')
            m = p4.match(line)
            if m:
                if 'intf' not in ospf_intf_dict:
                    ospf_intf_dict['intf'] = {}

                hello_timer = m.groupdict()['hello_timer']
                ospf_intf_dict['intf'][intf]['hello_timer'] = hello_timer
                dead_timer = m.groupdict()['dead_timer']
                ospf_intf_dict['intf'][intf]['dead_timer'] = dead_timer
                wait_timer = m.groupdict()['wait_timer']
                ospf_intf_dict['intf'][intf]['wait_timer'] = wait_timer
                retransmit_timer = m.groupdict()['retransmit_timer']
                ospf_intf_dict['intf'][intf]['retransmit_timer'] = retransmit_timer
                continue
        ospf_intf_dict['intfs_all'] = sorted(intfs_all)
        ospf_intf_dict['intfs_up'] = sorted(intfs_up)
        ospf_intf_dict['intfs_down'] = sorted(intfs_down)
        return ospf_intf_dict


    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ip ospf interface | xml')
        result = tcl.cast_any(output[1])

        return result

class ShowIpOspfDatabaseSchema(MetaParser):

    schema = {'process_id':
                  {Any():
                       {'router_id': str,
						Optional('area'):
							{Optional(Any()):
								{Any():
									{'ls_id':
										{Any():
											{'advrouter':
												{Any():
													{'age': str,
													 'seq': str,
													 'cksum': str,
													 Optional('lnkcnt'): str},
												}
											},
										},
									},
								},
							},
                        },
                   }
              }

class ShowIpOspfDatabase(ShowIpOspfDatabaseSchema, MetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).


    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show ip ospf database'.format()
        out = self.device.execute(cmd)
        ospf_db_dict = {}
        lsa_type = {}

        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*(?P<key>[a-zA-Z0-9]+) +Router +with +ID '
                            r'\((?P<router_id>[0-9\.]+)\) '
                            r'\(Process ID (?P<process_id>[0-9]+)\)')
            m = p1.match(line)
            if m:
                router_id = m.groupdict()['router_id']
                process_id = m.groupdict()['process_id']
                if 'process_id' not in ospf_db_dict:
                    ospf_db_dict['process_id'] = {}
                if process_id not in ospf_db_dict['process_id']:
                    ospf_db_dict['process_id'][process_id] = {}
                ospf_db_dict['process_id'][process_id]['router_id'] = router_id
                continue

            p2 = re.compile(r'^\s*Router +Link +States +\(Area +(?P<area>[0-9]+)\)')
            m = p2.match(line)
            if m:
                area = m.groupdict()['area']
                if 'area' not in ospf_db_dict['process_id'][process_id]:
                    ospf_db_dict['process_id'][process_id]['area'] = {}
                if area not in ospf_db_dict['process_id'][process_id]['area']:
                    ospf_db_dict['process_id'][process_id]['area'][area] = {}
                if 'router_link' not in ospf_db_dict['process_id'][process_id]['area'][area]:
                    ospf_db_dict['process_id'][process_id]['area'][area]['router_link'] = {}
                lsa_type = ospf_db_dict['process_id'][process_id]['area'][area]['router_link']
                continue

            p3 = re.compile(r'^\s*Net +Link +States +\(Area +(?P<area>[0-9]+)\)')
            m = p3.match(line)
            if m:
                area = m.groupdict()['area']
                if 'area' not in ospf_db_dict['process_id'][process_id]:
                    ospf_db_dict['process_id'][process_id]['area'] = {}
                if area not in ospf_db_dict['process_id'][process_id]['area']:
                    ospf_db_dict['process_id'][process_id]['area'][area] = {}
                if 'network_link' not in ospf_db_dict['process_id'][process_id]['area'][area]:
                    ospf_db_dict['process_id'][process_id]['area'][area]['network_link'] = {}
                lsa_type = ospf_db_dict['process_id'][process_id]['area'][area]['network_link']
                continue

            p4 = re.compile(r'^\s*Summary +Network +Link +States +\(Area +(?P<area>[0-9]+)\)')
            m = p4.match(line)
            if m:
                area = m.groupdict()['area']
                if 'area' not in ospf_db_dict['process_id'][process_id]:
                    ospf_db_dict['process_id'][process_id]['area'] = {}
                if area not in ospf_db_dict['process_id'][process_id]['area']:
                    ospf_db_dict['process_id'][process_id]['area'][area] = {}
                if 'summary_network_link' not in ospf_db_dict['process_id'][process_id]['area'][area]:
                    ospf_db_dict['process_id'][process_id]['area'][area]['summary_network_link'] = {}
                lsa_type = ospf_db_dict['process_id'][process_id]['area'][area]['summary_network_link']
                continue

            p5 = re.compile(r'^\s*Opaque +Area +Link +States +\(Area +(?P<area>[0-9]+)\)')
            m = p5.match(line)
            if m:
                area = m.groupdict()['area']
                if 'area' not in ospf_db_dict['process_id'][process_id]:
                    ospf_db_dict['process_id'][process_id]['area'] = {}
                if area not in ospf_db_dict['process_id'][process_id]['area']:
                    ospf_db_dict['process_id'][process_id]['area'][area] = {}
                if 'opaque_area_link' not in ospf_db_dict['process_id'][process_id]['area'][area]:
                    ospf_db_dict['process_id'][process_id]['area'][area]['opaque_area_link'] = {}
                lsa_type = ospf_db_dict['process_id'][process_id]['area'][area]['opaque_area_link']
                continue
            if lsa_type is not {}:
                p6 = re.compile(r'\s*(?P<ls_id>[0-9\.]+) +(?P<advrouter>[0-9\.]+) '
                                r'+(?P<age>\d+) +(?P<seq>0[xX][0-9a-fA-F]+) '
                                r'+(?P<cksum>0[xX][0-9a-fA-F]+) +(?P<lnkcnt>\d+)')
                m = p6.match(line)
                if m:
                    ls_id = m.groupdict()['ls_id']
                    advrouter = m.groupdict()['advrouter']
                    age = m.groupdict()['age']
                    seq = m.groupdict()['seq']
                    cksum = m.groupdict()['cksum']
                    lnkcnt = m.groupdict()['lnkcnt']
                    if 'ls_id' not in lsa_type:
                        lsa_type['ls_id'] = {}
                    if ls_id not in lsa_type['ls_id']:
                        lsa_type['ls_id'][ls_id] = {}
                    if 'advrouter' not in lsa_type['ls_id'][ls_id]:
                        lsa_type['ls_id'][ls_id]['advrouter'] = {}
                    if advrouter not in lsa_type['ls_id'][ls_id]['advrouter']:
                        lsa_type['ls_id'][ls_id]['advrouter'][advrouter] = {}
                    lsa_type['ls_id'][ls_id]['advrouter'][advrouter]['age'] = age
                    lsa_type['ls_id'][ls_id]['advrouter'][advrouter]['seq'] = seq
                    lsa_type['ls_id'][ls_id]['advrouter'][advrouter]['cksum'] = cksum
                    lsa_type['ls_id'][ls_id]['advrouter'][advrouter]['lnkcnt'] = lnkcnt
                    continue

                p7 = re.compile(r'\s*(?P<ls_id>[0-9\.]+) +(?P<advrouter>[0-9\.]+) '
                                r'+(?P<age>\d+) +(?P<seq>0[xX][0-9a-fA-F]+) '
                                r'+(?P<cksum>0[xX][0-9a-fA-F]+)')
                m = p7.match(line)
                if m:
                    ls_id = m.groupdict()['ls_id']
                    advrouter = m.groupdict()['advrouter']
                    age = m.groupdict()['age']
                    seq = m.groupdict()['seq']
                    cksum = m.groupdict()['cksum']
                    if 'ls_id' not in lsa_type:
                        lsa_type['ls_id'] = {}
                    if ls_id not in lsa_type['ls_id']:
                        lsa_type['ls_id'][ls_id] = {}
                    if 'advrouter' not in lsa_type['ls_id'][ls_id]:
                        lsa_type['ls_id'][ls_id]['advrouter'] = {}
                    if advrouter not in lsa_type['ls_id'][ls_id]['advrouter']:
                        lsa_type['ls_id'][ls_id]['advrouter'][advrouter] = {}
                    lsa_type['ls_id'][ls_id]['advrouter'][advrouter]['age'] = age
                    lsa_type['ls_id'][ls_id]['advrouter'][advrouter]['seq'] = seq
                    lsa_type['ls_id'][ls_id]['advrouter'][advrouter]['cksum'] = cksum
                    continue

        return ospf_db_dict

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ip ospf database | xml')
        result = tcl.cast_any(output[1])

        return result
