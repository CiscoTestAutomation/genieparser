''' show_ospf.py

IOS parsers for the following show commands:
    * show ip ospf
    * show ip ospf interface
    * show ip ospf sham-links
    * show ip ospf virtual-links
    * show ip ospf neighbor detail
    * show ip ospf database router
    * show ip ospf database network
    * show ip ospf database summary
    * show ip ospf database external
    * show ip ospf database opaque-area
    * show ip ospf mpls ldp interface
    * show ip ospf mpls traffic-eng link
'''

# Python
import re

from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

from genie.libs.parser.iosxe.show_ospf import  ShowIpOspfInterface as ShowIpOspfInterface_iosxe,\
                                               ShowIpOspfDatabaseRouter as ShowIpOspfDatabaseRouter_iosxe,\
                                               ShowIpOspfDatabaseExternal as ShowIpOspfDatabaseExternal_iosxe,\
                                               ShowIpOspfDatabaseNetwork as ShowIpOspfDatabaseNetwork_iosxe,\
                                               ShowIpOspfDatabaseSummary as ShowIpOspfDatabaseSummary_iosxe,\
                                               ShowIpOspfDatabaseOpaqueArea as ShowIpOspfDatabaseOpaqueArea_iosxe,\
                                               ShowIpOspf as ShowIpOspf_iosxe,\
                                               ShowIpOspfMplsLdpInterface as ShowIpOspfMplsLdpInterface_iosxe,\
                                               ShowIpOspfMplsTrafficEngLink as ShowIpOspfMplsTrafficEngLink_iosxe,\
                                               ShowIpOspfNeighborDetail as ShowIpOspfNeighborDetail_iosxe


class ShowIpOspf(ShowIpOspf_iosxe):

    ''' Parser for "show ip ospf" '''
    pass

class ShowIpOspfInterface(ShowIpOspfInterface_iosxe):

    ''' Parser for "show ip ospf interface" '''
    pass

# ============================================
# Super parser for 'show ip ospf <WORD>-links'
# ============================================
class ShowIpOspfLinksParser(MetaParser):

    ''' Parser for "show ip ospf <WORD>-links" '''

    def cli(self, cmd, link_type,output=None):

        assert link_type in ['virtual_links', 'sham_links']

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        af = 'ipv4'

        # crypo_algorithm dict
        crypto_dict = {'cryptographic': 'md5', 'simple password': 'simple'}

        for line in out.splitlines():
            line = line.strip()

            # Sham Link OSPF_SL0 to address 22.22.22.22 is up
            # Virtual Link OSPF_VL0 to router 4.4.4.4 is up
            p1 = re.compile(r'^(Virtual|Sham) +Link +(?P<interface>(\S+)) +to'
                             ' +(address|router) +(?P<address>(\S+)) +is'
                             ' +(?P<link_state>(up|down))$')
            m = p1.match(line)
            if m:
                address = str(m.groupdict()['address'])
                sl_remote_id = vl_router_id = address
                interface = str(m.groupdict()['interface'])
                link_state = str(m.groupdict()['link_state'])
                instance = None

                # Get link name
                n = re.match('(?P<ignore>\S+)_(?P<name>(S|V)L(\d+))', interface)
                if n:
                    real_link_name = str(n.groupdict()['name'])
                else:
                    real_link_name = interface

                # Get OSPF process ID from 'show ip ospf interface'
                cmd = 'show ip ospf interface | section {}'.format(interface)
                out = self.device.execute(cmd)

                for line in out.splitlines():
                    line = line.rstrip()

                    # Process ID 2, Router ID 11.11.11.11, Network Type SHAM_LINK, Cost: 111
                    p = re.search('Process +ID +(?P<instance>(\S+)), +Router'
                                  ' +(.*)', line)
                    if p:
                        instance = str(p.groupdict()['instance'])
                        break

                # Get VRF information using the ospf instance
                if instance is not None:
                    cmd = 'show running-config | section router ospf {}'.format(instance)
                    out = self.device.execute(cmd)

                    for line in out.splitlines():
                        line = line.rstrip()

                        # Skip the show command line so as to not match
                        if re.search('show', line):
                            continue

                        # router ospf 1
                        # router ospf 2 vrf VRF1
                        p = re.search('router +ospf +(?P<instance>(\S+))'
                                      '(?: +vrf +(?P<vrf>(\S+)))?', line)
                        if p:
                            p_instance = str(p.groupdict()['instance'])
                            if p_instance == instance:
                                if p.groupdict()['vrf']:
                                    vrf = str(p.groupdict()['vrf'])
                                    break
                                else:
                                    vrf = 'default'
                                    break

                # Build dict
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}
                if 'address_family' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['address_family'] = {}
                if af not in ret_dict['vrf'][vrf]['address_family']:
                    ret_dict['vrf'][vrf]['address_family'][af] = {}
                if 'instance' not in ret_dict['vrf'][vrf]['address_family'][af]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance'] = {}
                if instance not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance] = {}
                continue


            # Area 1, source address 33.33.33.33
            # Area 1 source address 11.11.11.11
            p2 = re.compile(r'^Area +(?P<area>(\S+)),? +source +address'
                             ' +(?P<source_address>(\S+))$')
            m = p2.match(line)
            if m:
                area = str(IPAddress(str(m.groupdict()['area'])))
                source_address = str(m.groupdict()['source_address'])

                # Set link_name for sham_link
                link_name = '{} {}'.format(source_address, sl_remote_id)

                # Build dict
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if link_type not in  ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][link_type] = {}
                if link_name not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][link_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][link_type][link_name] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]\
                            [link_type][link_name]

                # Set values
                sub_dict['transit_area_id'] = area
                sub_dict['local_id'] = source_address
                sub_dict['demand_circuit'] = False

                # Set previously parsed values
                try:
                    sub_dict['name'] = real_link_name
                    sub_dict['remote_id'] = sl_remote_id
                    sub_dict['link_state'] = link_state
                except Exception:
                    pass
                continue

            # Run as demand circuit
            p3 = re.compile(r'^Run +as +demand +circuit$')
            m = p3.match(line)
            if m:
                if link_type == 'sham_links':
                    sub_dict['demand_circuit'] = True
                else:
                    demand_circuit = True
                continue

            # DoNotAge LSA not allowed (Number of DCbitless LSA is 7).
            # DoNotAge LSA not allowed (Number of DCbitless LSA is 1). Cost of using 111 State POINT_TO_POINT,
            # DoNotAge LSA allowed. Cost of using 111 State DOWN,
            p4 = re.compile(r'^DoNotAge +LSA +(not )?allowed'
                             '( +\(Number +of +DCbitless +LSA +is +(?P<dcbitless>(\d+))\))?.'
                             '(?: +Cost +of +using +(?P<cost>(\d+)))?'
                             '(?: State +(?P<state>(\S+)))?$')
            m = p4.match(line)
            if m:
                if m.groupdict()['dcbitless']:
                    dcbitless_lsa_count = int(m.groupdict()['dcbitless'])
                    donotage_lsa = 'not allowed'
                else:
                    donotage_lsa = 'allowed'
                if m.groupdict()['cost']:
                    cost = int(m.groupdict()['cost'])
                if m.groupdict()['state']:
                    link_state =  str(m.groupdict()['state']).lower()

                # Set values for sham_links
                if link_type == 'sham_links':
                    if m.groupdict()['dcbitless']:
                        sub_dict['dcbitless_lsa_count'] = dcbitless_lsa_count
                    sub_dict['donotage_lsa'] = donotage_lsa
                    if m.groupdict()['cost']:
                        sub_dict['cost'] = cost
                    if m.groupdict()['state']:
                        sub_dict['state'] = link_state
                    continue

            # Transit area 1
            # Transit area 1, via interface GigabitEthernet0/1
            p5 = re.compile(r'^Transit +area +(?P<area>[\w\.]+),?'
                             '(?: +via +interface +(?P<intf>(\S+)))?$')
            m = p5.match(line)
            if m:
                area = str(IPAddress(str(m.groupdict()['area'])))

                # Set link_name for virtual_link
                link_name = '{} {}'.format(area, vl_router_id)

                # Create dict
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if link_type not in  ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][link_type] = {}
                if link_name not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][link_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][link_type][link_name] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]\
                            [link_type][link_name]

                # Set values
                sub_dict['transit_area_id'] = area
                sub_dict['demand_circuit'] = False
                if m.groupdict()['intf']:
                    sub_dict['interface'] = str(m.groupdict()['intf'])

                # Set previously parsed values
                try:
                    sub_dict['name'] = real_link_name
                except Exception:
                    pass
                try:
                    sub_dict['router_id'] = vl_router_id
                except Exception:
                    pass
                try:
                    sub_dict['dcbitless_lsa_count'] = dcbitless_lsa_count
                except Exception:
                    pass
                try:
                    sub_dict['donotage_lsa'] = donotage_lsa
                except Exception:
                    pass
                try:
                    sub_dict['demand_circuit'] = demand_circuit
                except Exception:
                    pass
                try:
                    sub_dict['link_state'] = link_state
                except Exception:
                    pass
                continue

            # Topology-MTID    Cost    Disabled     Shutdown      Topology Name
            #             0       1          no           no               Base
            p6 = re.compile(r'^(?P<mtid>(\d+)) +(?P<topo_cost>(\d+))'
                             ' +(?P<disabled>(yes|no)) +(?P<shutdown>(yes|no))'
                             ' +(?P<topo_name>(\S+))$')
            m = p6.match(line)
            if m:
                mtid = int(m.groupdict()['mtid'])
                if 'topology' not in sub_dict:
                    sub_dict['topology'] = {}
                if mtid not in sub_dict['topology']:
                    sub_dict['topology'][mtid] = {}
                sub_dict['topology'][mtid]['cost'] = int(m.groupdict()['topo_cost'])
                sub_dict['topology'][mtid]['name'] = str(m.groupdict()['topo_name'])
                if 'yes' in m.groupdict()['disabled']:
                    sub_dict['topology'][mtid]['disabled'] = True
                else:
                    sub_dict['topology'][mtid]['disabled'] = False
                if 'yes' in m.groupdict()['shutdown']:
                    sub_dict['topology'][mtid]['shutdown'] = True
                else:
                    sub_dict['topology'][mtid]['shutdown'] = False
                    continue

            # Transmit Delay is 1 sec, State POINT_TO_POINT,
            p7 = re.compile(r'^Transmit +Delay +is +(?P<transmit_delay>(\d+))'
                             ' +sec, +State +(?P<state>(\S+)),?$')
            m = p7.match(line)
            if m:
                sub_dict['transmit_delay'] = int(m.groupdict()['transmit_delay'])
                state = str(m.groupdict()['state']).lower()
                state = state.replace("_", "-")
                sub_dict['state'] = state
                continue

            # Timer intervals configured, Hello 3, Dead 13, Wait 13, Retransmit 5
            # Timer intervals configured, Hello 4, Dead 16, Wait 16, Retransmit 44
            # Timer intervals configured, Hello 10, Dead 40, Wait 40,
            p8 = re.compile(r'^Timer +intervals +configured,'
                             ' +Hello +(?P<hello>(\d+)),'
                             ' +Dead +(?P<dead>(\d+)),'
                             ' +Wait +(?P<wait>(\d+)),'
                             '(?: +Retransmit +(?P<retransmit>(\d+)))?$')
            m = p8.match(line)
            if m:
                if m.groupdict()['hello']:
                    sub_dict['hello_interval'] = int(m.groupdict()['hello'])
                if m.groupdict()['dead']:
                    sub_dict['dead_interval'] = int(m.groupdict()['dead'])
                if m.groupdict()['wait']:
                    sub_dict['wait_interval'] = int(m.groupdict()['wait'])
                if m.groupdict()['retransmit']:
                    sub_dict['retransmit_interval'] = int(m.groupdict()['retransmit'])
                continue

            # Strict TTL checking enabled, up to 3 hops allowed
            p9 = re.compile(r'^Strict +TTL +checking'
                             ' +(?P<strict_ttl>(enabled|disabled))'
                             '(?:, +up +to +(?P<hops>(\d+)) +hops +allowed)?$')
            m = p9.match(line)
            if m:
                if 'ttl_security' not in sub_dict:
                    sub_dict['ttl_security'] = {}
                if 'enabled' in m.groupdict()['strict_ttl']:
                    sub_dict['ttl_security']['enable'] = True
                else:
                    sub_dict['ttl_security']['enable'] = False
                if m.groupdict()['hops']:
                    sub_dict['ttl_security']['hops'] = int(m.groupdict()['hops'])
                    continue

            # Hello due in 00:00:03:179
            p10 = re.compile(r'^Hello +due +in +(?P<hello_timer>(\S+))$')
            m = p10.match(line)
            if m:
                sub_dict['hello_timer'] = str(m.groupdict()['hello_timer'])
                continue

            # Adjacency State FULL
            p11 = re.compile(r'^Adjacency +State +(?P<adj_state>(\S+))$')
            m = p11.match(line)
            if m:
                sub_dict['adjacency_state'] = str(m.groupdict()['adj_state']).lower()
                continue

            # Index 1/2/2, retransmission queue length 0, number of retransmission 2
            p12 = re.compile(r'^Index +(?P<index>(\S+)), +retransmission +queue'
                              ' +length +(?P<length>(\d+)), +number +of'
                              ' +retransmission +(?P<retrans>(\d+))$')
            m = p12.match(line)
            if m:
                sub_dict['index'] = str(m.groupdict()['index'])
                sub_dict['retrans_qlen'] = int(m.groupdict()['length'])
                sub_dict['total_retransmission'] = int(m.groupdict()['retrans'])
                continue

            # First 0x0(0)/0x0(0)/0x0(0) Next 0x0(0)/0x0(0)/0x0(0)
            p13 = re.compile(r'^First +(?P<first>(\S+)) +Next +(?P<next>(\S+))$')
            m = p13.match(line)
            if m:
                sub_dict['first'] = str(m.groupdict()['first'])
                sub_dict['next'] = str(m.groupdict()['next'])
                continue

            # Last retransmission scan length is 1, maximum is 1
            p14 = re.compile(r'^Last +retransmission +scan +length +is'
                              ' +(?P<len>(\d+)), +maximum +is +(?P<max>(\d+))$')
            m = p14.match(line)
            if m:
                sub_dict['last_retransmission_scan_length'] = \
                    int(m.groupdict()['len'])
                sub_dict['last_retransmission_max_length'] = \
                    int(m.groupdict()['max'])
                continue

            # Last retransmission scan time is 0 msec, maximum is 0 msec
            p15 = re.compile(r'^Last +retransmission +scan +time +is'
                              ' +(?P<time>(\d+)) +msec, +maximum +is'
                              ' +(?P<max>(\d+)) +msec$')
            m = p15.match(line)
            if m:
                sub_dict['last_retransmission_scan_time'] = \
                    int(m.groupdict()['time'])
                sub_dict['last_retransmission_max_scan'] = \
                    int(m.groupdict()['max'])
                continue

        return ret_dict


# ====================================
# Schema for 'show ip ospf sham-links'
# ====================================
class ShowIpOspfShamLinksSchema(MetaParser):

    ''' Schema for 'show ip ospf sham-links' '''

    schema = {
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {'instance':
                            {Any():
                                {'areas':
                                    {Any():
                                        {'sham_links':
                                            {Any():
                                                {'name': str,
                                                'link_state': str,
                                                'local_id': str,
                                                'remote_id': str,
                                                'transit_area_id': str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('transmit_delay'): int,
                                                'cost': int,
                                                'state': str,
                                                Optional('hello_timer'): str,
                                                Optional('demand_circuit'): bool,
                                                Optional('dcbitless_lsa_count'): int,
                                                Optional('donotage_lsa'): str,
                                                Optional('adjacency_state'): str,
                                                Optional('ttl_security'):
                                                    {'enable': bool,
                                                    Optional('hops'): int},
                                                Optional('index'): str,
                                                Optional('first'): str,
                                                Optional('next'): str,
                                                Optional('last_retransmission_max_length'): int,
                                                Optional('last_retransmission_max_scan'): int,
                                                Optional('last_retransmission_scan_length'): int,
                                                Optional('last_retransmission_scan_time'): int,
                                                Optional('total_retransmission'): int,
                                                Optional('retrans_qlen'): int,
                                                Optional('topology'):
                                                    {Any():
                                                        {'cost': int,
                                                        'disabled': bool,
                                                        'shutdown': bool,
                                                        'name': str}},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ====================================
# Parser for 'show ip ospf sham-links'
# ====================================
class ShowIpOspfShamLinks(ShowIpOspfShamLinksSchema, ShowIpOspfLinksParser):

    ''' Parser for 'show ip ospf sham-links' '''
    cli_command = 'show ip ospf sham-links'
    def cli(self,output=None):

        return super().cli(cmd=self.cli_command, link_type='sham_links',output=output)


# =======================================
# Schema for 'show ip ospf virtual-links'
# =======================================
class ShowIpOspfVirtualLinksSchema(MetaParser):

    ''' Schema for 'show ip ospf virtual-links' '''

    schema = {
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {'instance':
                            {Any():
                                {'areas':
                                    {Any():
                                        {'virtual_links':
                                            {Any():
                                                {'name': str,
                                                'link_state': str,
                                                'router_id': str,
                                                'transit_area_id': str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                'transmit_delay': int,
                                                'state': str,
                                                'demand_circuit': bool,
                                                Optional('cost'): int,
                                                Optional('hello_timer'): str,
                                                Optional('interface'): str,
                                                Optional('dcbitless_lsa_count'): int,
                                                Optional('donotage_lsa'): str,
                                                Optional('adjacency_state'): str,
                                                Optional('ttl_security'):
                                                    {'enable': bool,
                                                    Optional('hops'): int},
                                                Optional('index'): str,
                                                Optional('first'): str,
                                                Optional('next'): str,
                                                Optional('last_retransmission_max_length'): int,
                                                Optional('last_retransmission_max_scan'): int,
                                                Optional('last_retransmission_scan_length'): int,
                                                Optional('last_retransmission_scan_time'): int,
                                                Optional('total_retransmission'): int,
                                                Optional('retrans_qlen'): int,
                                                Optional('topology'):
                                                    {Any():
                                                        {'cost': int,
                                                        'disabled': bool,
                                                        'shutdown': bool,
                                                        'name': str}},
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# =======================================
# Parser for 'show ip ospf virtual-links'
# =======================================
class ShowIpOspfVirtualLinks(ShowIpOspfVirtualLinksSchema, ShowIpOspfLinksParser):

    ''' Parser for 'show ip ospf virtual-links' '''

    cli_command = 'show ip ospf virtual-links'
    def cli(self,output=None):

        return super().cli(cmd=self.cli_command, link_type='virtual_links',output=output)


class ShowIpOspfNeighborDetail(ShowIpOspfNeighborDetail_iosxe):

    ''' Parser for "show ip ospf neighbor detail" '''
    pass

class ShowIpOspfDatabaseRouter(ShowIpOspfDatabaseRouter_iosxe):

    ''' Parser for "show ip ospf database router" '''
    pass

class ShowIpOspfDatabaseExternal(ShowIpOspfDatabaseExternal_iosxe):

    ''' Parser for "show ip ospf database external" '''
    pass

class ShowIpOspfDatabaseNetwork(ShowIpOspfDatabaseNetwork_iosxe):

    ''' Parser for "show ip ospf database network" '''
    pass

class ShowIpOspfDatabaseSummary(ShowIpOspfDatabaseSummary_iosxe):

    ''' Parser for "show ip ospf database summary" '''
    pass


class ShowIpOspfDatabaseOpaqueArea(ShowIpOspfDatabaseOpaqueArea_iosxe):

    ''' Parser for "show ip ospf database opaque-area" '''
    pass


class ShowIpOspfMplsLdpInterface(ShowIpOspfMplsLdpInterface_iosxe):

    ''' Parser for "show ip ospf mpls ldp interface" '''
    pass


class ShowIpOspfMplsTrafficEngLink(ShowIpOspfMplsTrafficEngLink_iosxe):

    ''' Parser for "show ip ospf mpls traffic-eng link" '''
    pass
