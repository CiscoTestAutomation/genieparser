"""show_mcast.py

IOSXE parsers for the following show commands:

    * show ip mroute
    * show ipv6 mroute
    * show ip mroute
    * show ip mroute vrf <vrf_name>
    * show ipv6 mroute
    * show ipv6 mroute vrf <vrf_name>
    * show ip mroute static
    * show ip mroute vrf <vrf_name> static
    * show ip multicast
    * show ip multicast vrf <vrf_name>
    * show ip multicast mpls vif

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# =====================================
# Parser for 'show ip mroute'
# Parser for 'show ip mroute vrf xxx'
# Parser for 'show ipv6 mroute'
# Parser for 'show ipv6 mroute vrf xxx'
# =====================================

class ShowIpMrouteSchema(MetaParser):
    """Schema for:
        show ip mroute
        show ip mroute vrf <vrf>
        show ipv6 mroute
        show ipv6 mroute vrf <vrf>"""

    schema = {'vrf':         
                {Any():
                    {'address_family':
                        {Any(): 
                            {Optional('multicast_group'): 
                                {Any(): 
                                    {Optional('source_address'): 
                                        {Any(): 
                                            {Optional('uptime'): str,
                                             Optional('expire'): str,
                                             Optional('flags'): str,
                                             Optional('rp_bit'): bool,
                                             Optional('msdp_learned'): bool,                                             
                                             Optional('rp'): str,
                                             Optional('rpf_nbr'): str,
                                             Optional('rpf_info'): str,
                                             Optional('incoming_interface_list'):
                                                {Any(): 
                                                    {'rpf_nbr': str,
                                                     Optional('rpf_info'): str,
                                                    },
                                                },
                                             Optional('outgoing_interface_list'): 
                                                {Any(): 
                                                    {'uptime': str,
                                                     'expire': str,
                                                     'state_mode': str,
                                                     Optional('flags'): str,
                                                     Optional('vcd'): str,
                                                     Optional('lisp_mcast_source'): str,
                                                     Optional('lisp_mcast_group'): str,
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    }
                },
            }

class ShowIpMroute(ShowIpMrouteSchema):
    """Parser for:
        show ip mroute
        show ip mroute vrf <vrf>"""

    cli_command = ['show ip mroute', 'show ip mroute vrf {vrf}']
    exclude = ['expire', 'uptime', 'outgoing_interface_list', 'flags']


    def cli(self, vrf='',output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial variables
        mroute_dict = {}
        sub_dict = {}
        outgoing = False

        for line in out.splitlines():
            line = line.strip()

            # IP Multicast Routing Table
            # Multicast Routing Table
            p1 = re.compile(r'^(?P<address_family>[\w\W]+)? *[mM]ulticast'
                             ' +[rR]outing +[tT]able$')
            m = p1.match(line)
            if m:
                address_family = m.groupdict()['address_family']
                if address_family:
                    if address_family.strip().lower() == 'ip':
                        address_family = 'ipv4'
                else:
                    address_family = 'ipv6'

                if 'vrf' not in mroute_dict:
                    mroute_dict['vrf'] = {}
                if vrf not in mroute_dict['vrf']:
                    mroute_dict['vrf'][vrf] = {}
                if 'address_family' not in mroute_dict['vrf'][vrf]:
                    mroute_dict['vrf'][vrf]['address_family'] = {}
                if address_family not in mroute_dict['vrf'][vrf]['address_family']:
                    mroute_dict['vrf'][vrf]['address_family'][address_family] = {}
                continue

            # (*, 239.1.1.1), 00:00:03/stopped, RP 10.4.1.1, flags: SPF
            # (10.4.1.1, 239.1.1.1), 00:00:03/00:02:57, flags: PFT
            # (*, FF07::1), 00:04:45/00:02:47, RP 2001:DB8:6::6, flags:S
            # (2001:DB8:999::99, FF07::1), 00:02:06/00:01:23, flags:SFT
            p2 = re.compile(r'^\((?P<source_address>[\w\:\.\*\/]+),'
                             ' +(?P<multicast_group>[\w\:\.\/]+)\),'
                             ' +(?P<uptime>[\w\:\.]+)\/'
                             '(?P<expires>[\w\:\.]+),'
                             '( +RP +(?P<rendezvous_point>[\w\:\.]+),)?'
                             ' +flags: *(?P<flags>[a-zA-Z]+)$')
            m = p2.match(line)
            if m:
                source_address = m.groupdict()['source_address']
                multicast_group = m.groupdict()['multicast_group']

                if 'multicast_group' not in mroute_dict['vrf'][vrf]['address_family'][address_family]:
                    mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'] = {}
                if multicast_group not in mroute_dict['vrf'][vrf]['address_family'][address_family]\
                ['multicast_group']:
                    mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group] = {}
                if 'source_address' not in mroute_dict['vrf'][vrf]['address_family'][address_family]\
                ['multicast_group'][multicast_group]:
                    mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                    ['source_address'] = {}
                if source_address not in mroute_dict['vrf'][vrf]['address_family'][address_family]\
                        ['multicast_group'][multicast_group]['source_address']:
                    mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                        ['source_address'][source_address] = {}

                sub_dict = mroute_dict['vrf'][vrf]['address_family'][address_family]['multicast_group'][multicast_group]\
                        ['source_address'][source_address]

                sub_dict['uptime'] = m.groupdict()['uptime']
                sub_dict['expire'] = m.groupdict()['expires']
                flags = m.groupdict()['flags']
                sub_dict['flags'] = flags
                if "M" in flags:
                    sub_dict['msdp_learned'] = True
                else:
                    sub_dict['msdp_learned'] = False
                if "R" in flags:
                    sub_dict['rp_bit'] = True
                else:
                    sub_dict['rp_bit'] = False

                
                rendezvous_point = m.groupdict()['rendezvous_point']
                if rendezvous_point:
                    sub_dict['rp'] = rendezvous_point

                continue

            # Incoming interface: Null, RPF nbr 224.0.0.0224.0.0.0
            # Incoming interface: Loopback0, RPF nbr 0.0.0.0, Registering
            p3 = re.compile(r'^Incoming +interface:'
                             ' +(?P<incoming_interface>[a-zA-Z0-9\/\-\.]+),'
                             ' +RPF +nbr +(?P<rpf_nbr>[\w\:\.]+)'
                             '(, *(?P<status>\w+))?$')
            m = p3.match(line)
            if m:
                incoming_interface = m.groupdict()['incoming_interface']
                rpf_nbr = m.groupdict()['rpf_nbr']
                rpf_info = m.groupdict()['status']
                
                sub_dict['rpf_nbr'] = rpf_nbr
                if rpf_info:
                    sub_dict['rpf_info'] = rpf_info.lower()

                if incoming_interface.lower() == 'null':
                    sub_dict['rpf_nbr'] = rpf_nbr
                    if rpf_info:
                        sub_dict['rpf_info'] = rpf_info.lower()
                    continue

                if 'incoming_interface_list' not in sub_dict:
                    sub_dict['incoming_interface_list'] = {}
                if incoming_interface not in sub_dict['incoming_interface_list']:
                    sub_dict['incoming_interface_list'][incoming_interface] = {}
                sub_dict['incoming_interface_list'][incoming_interface]['rpf_nbr'] = rpf_nbr
                if rpf_info:
                    sub_dict['incoming_interface_list'][incoming_interface]\
                        ['rpf_info'] = rpf_info.lower()
                continue

            # Incoming interface:Tunnel5
            p3_1 = re.compile(r'^Incoming +interface:'
                             ' *(?P<incoming_interface>[a-zA-Z0-9\/\-\.]+)$')
            m = p3_1.match(line)
            if m:
                incoming_interface = m.groupdict()['incoming_interface']

                if incoming_interface.lower() == 'null':
                    continue

                if 'incoming_interface_list' not in sub_dict:
                    sub_dict['incoming_interface_list'] = {}
                if incoming_interface not in sub_dict['incoming_interface_list']:
                    sub_dict['incoming_interface_list'][incoming_interface] = {}
                continue

            # RPF nbr:2001:db8:90:24::6
            p3_2 = re.compile(r'^RPF +nbr: *(?P<rpf_nbr>[\w\:\.]+)$')
            m = p3_2.match(line)
            if m:
                rpf_nbr = m.groupdict()['rpf_nbr']
                try:
                    sub_dict['rpf_nbr'] = rpf_nbr
                    sub_dict['incoming_interface_list'][incoming_interface]['rpf_nbr'] = rpf_nbr
                except Exception:
                    sub_dict['rpf_nbr'] = rpf_nbr
                continue

            # Outgoing interface list: Null
            # Outgoing interface list:
            p4 =  re.compile(r'^Outgoing +interface +list:'
                              '( *(?P<intf>\w+))?$')
            m = p4.match(line)
            if m:
                intf = m.groupdict()['intf']
                if intf:
                    outgoing = False
                else:
                    outgoing = True
                continue

            # Vlan5, Forward/Dense, 00:03:25/00:00:00, H
            # Vlan5, Forward/Dense, 00:04:35/00:02:30
            # ATM0/0, VCD 14, Forward/Sparse, 00:03:57/00:02:53
            # POS4/0, Forward, 00:02:06/00:03:27
            # LISP0.4100, (172.24.0.3, 232.0.0.199), Forward/Sparse, 00:10:33/stopped
            p5 = re.compile(r'^(?P<outgoing_interface>[a-zA-Z0-9\/\.\-]+),'
                             '( +VCD +(?P<vcd>\d+),)?'
                             '( \(((?P<lisp_mcast_source>[0-9\.,]+), (?P<lisp_mcast_group>[0-9\.,]+)+)\),)?'
                             ' +(?P<state_mode>[\w\/-]+),'
                             ' +(?P<uptime>[a-zA-Z0-9\:]+)\/'
                             '(?P<expire>[\w\:]+)'
                             '(, *(?P<flags>\w+))?$')
            m = p5.match(line)
            if m and outgoing:
                outgoing_interface = m.groupdict()['outgoing_interface']
                vcd = m.groupdict()['vcd']
                uptime = m.groupdict()['uptime']
                lisp_mcast_source = m.groupdict()['lisp_mcast_source']
                lisp_mcast_group = m.groupdict()['lisp_mcast_group']
                state_mode = m.groupdict()['state_mode'].lower()
                expire = m.groupdict()['expire']
                flags = m.groupdict()['flags']

                if 'outgoing_interface_list' not in sub_dict:
                    sub_dict['outgoing_interface_list'] = {}
                if outgoing_interface not in sub_dict['outgoing_interface_list']:
                    sub_dict['outgoing_interface_list'][outgoing_interface] = {}

                sub_dict['outgoing_interface_list'][outgoing_interface]['uptime'] = uptime
                sub_dict['outgoing_interface_list'][outgoing_interface]['expire'] = expire
                sub_dict['outgoing_interface_list'][outgoing_interface]['state_mode'] = state_mode
                if flags:
                    sub_dict['outgoing_interface_list'][outgoing_interface]['flags'] = flags
                if vcd:
                    sub_dict['outgoing_interface_list'][outgoing_interface]['vcd'] = vcd
                if lisp_mcast_source:
                    sub_dict['outgoing_interface_list'][outgoing_interface]['lisp_mcast_source'] = lisp_mcast_source
                if lisp_mcast_group:
                    sub_dict['outgoing_interface_list'][outgoing_interface]['lisp_mcast_group'] = lisp_mcast_group
                continue

        return mroute_dict


# ===========================================
# Parser for 'show ipv6 mroute'
# Parser for 'show ipv6 mroute vrf xxx'
# ===========================================
class ShowIpv6Mroute(ShowIpMroute):
    """Parser for:
       show ipv6 mroute
       show ipv6 mroute vrf <vrf>"""

    cli_command = ['show ipv6 mroute', 'show ipv6 mroute vrf {vrf}']
    exclude = ['expire', 'uptime', 'joins', 'leaves',
               'incoming_interface_list', '(Tunnel.*)']


    def cli(self, vrf='',output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(vrf=vrf, output=out)


# ===========================================
# Parser for 'show ip mroute static'
# Parser for 'show ip mroute vrf xxx static'
# ===========================================

class ShowIpMrouteStaticSchema(MetaParser):
    """Schema for:
        show ip mroute static
        show ip mroute vrf <vrf> static
    """
    schema = {'vrf': 
                {Any():
                    {'mroute':
                        {Any():
                            {'path':
                                {Any():
                                    {'neighbor_address': str,
                                     Optional('admin_distance'): str
                                    }
                                },
                            },
                        },
                    },
                },
            }

class ShowIpMrouteStatic(ShowIpMrouteStaticSchema):
    """Parser for:
            show ip mroute static
            show ip mroute vrf <vrf> static
        """
    cli_command = ['show ip mroute static', 'show ip mroute vrf {vrf} static']

    def cli(self, vrf='',output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output


        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            # Mroute: 172.16.0.0/16, RPF neighbor: 172.30.10.13, distance: 1
            p1 = re.compile(r'^Mroute: +(?P<mroute>[\w\:\.\/]+),'
                             ' RPF +neighbor: +(?P<rpf_nbr>[\w\.\:]+),'
                             ' distance: +(?P<distance>\d+)$')
                              
            m = p1.match(line)
            if m:
                mroute = m.groupdict()['mroute']
                rpf_nbr = m.groupdict()['rpf_nbr']
                distance = m.groupdict()['distance']

                path = rpf_nbr + ' ' + distance

                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                if 'mroute' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['mroute'] = {}
                if mroute not in ret_dict['vrf'][vrf]['mroute']:
                    ret_dict['vrf'][vrf]['mroute'][mroute] = {}

                if 'mroute' not in ret_dict['vrf'][vrf]:
                    ret_dict['vrf'][vrf]['mroute'] = {}
                if mroute not in ret_dict['vrf'][vrf]['mroute']:
                    ret_dict['vrf'][vrf]['mroute'][mroute] = {}
                    
                if 'path' not in ret_dict['vrf'][vrf]['mroute'][mroute]:
                    ret_dict['vrf'][vrf]['mroute'][mroute]['path'] = {}
                if path not in ret_dict['vrf'][vrf]['mroute'][mroute]['path']:
                    ret_dict['vrf'][vrf]['mroute'][mroute]['path'][path] = {}

                ret_dict['vrf'][vrf]['mroute'][mroute]['path'][path]\
                    ['neighbor_address'] = rpf_nbr

                ret_dict['vrf'][vrf]['mroute'][mroute]['path'][path]\
                    ['admin_distance'] = distance

                continue

        return ret_dict


# ===========================================
# Parser for 'show ip multicast'
# Parser for 'show ip multicast vrf xxx'
# ===========================================

class ShowIpMulticastSchema(MetaParser):
    """Schema for:
        show ip multicast
        show ip multicast vrf <vrf>
    """
    schema = {
        'vrf': {
            Any(): {
                'enable': bool,
                'multipath': bool,
                'route_limit': str,
                'fallback_group_mode': str,
                'multicast_bound_with_filter_autorp': int,
                Optional('mo_frr'): bool,
            },
        },
    }

class ShowIpMulticast(ShowIpMulticastSchema):
    """Parser for:
        show ip multicast
        show ip multicast vrf <vrf>
    """
    cli_command = ['show ip multicast', 'show ip multicast vrf {vrf}']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                vrf = 'default'
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Multicast Routing: enabled
            p1 = re.compile(r'^Multicast +Routing: +(?P<status>\w+)$')
                              
            m = p1.match(line)
            if m:
                status = m.groupdict()['status'].lower()
                if 'vrf' not in ret_dict:
                    ret_dict['vrf'] = {}
                if vrf not in ret_dict['vrf']:
                    ret_dict['vrf'][vrf] = {}

                if 'enabled' in status:
                    ret_dict['vrf'][vrf]['enable'] = True
                else:
                    ret_dict['vrf'][vrf]['enable'] = False
                continue

            # Multicast Multipath: enabled
            p2 = re.compile(r'^Multicast +Multipath: +(?P<status>\w+)$')
                              
            m = p2.match(line)
            if m:
                status = m.groupdict()['status'].lower()
                if 'enabled' in status:
                    ret_dict['vrf'][vrf]['multipath'] = True
                else:
                    ret_dict['vrf'][vrf]['multipath'] = False
                continue

            # Multicast Route limit: No limit
            p3 = re.compile(r'^Multicast +Route +limit: +(?P<status>[\w\s]+)$')
                              
            m = p3.match(line)
            if m:
                status = m.groupdict()['status'].lower()
                ret_dict['vrf'][vrf]['route_limit'] = status
                continue

            # Multicast Fallback group mode: Sparse
            p4 = re.compile(r'^Multicast +Fallback +group +mode: +(?P<mode>[\w\s]+)$')
                              
            m = p4.match(line)
            if m:
                mode = m.groupdict()['mode'].lower()
                ret_dict['vrf'][vrf]['fallback_group_mode'] = mode
                continue

            # Number of multicast boundaries configured with filter-autorp option: 0
            p5 = re.compile(r'^Number +of +multicast +boundaries +configured +'
                             'with +filter\-autorp +option: +(?P<num>\d+)$')
                              
            m = p5.match(line)
            if m:
                num = m.groupdict()['num']
                ret_dict['vrf'][vrf]['multicast_bound_with_filter_autorp'] = int(num)
                continue

            # MoFRR: Disabled
            p2 = re.compile(r'^MoFRR: +(?P<status>\w+)$')
                              
            m = p2.match(line)
            if m:
                status = m.groupdict()['status'].lower()
                if 'enabled' in status:
                    ret_dict['vrf'][vrf]['mo_frr'] = True
                else:
                    ret_dict['vrf'][vrf]['mo_frr'] = False
                continue

        return ret_dict

class ShowIpMulticastMplsvifSchema(MetaParser):
    """Schema for:
        show ip multicast mpls vif
    """
    schema = {
        'interfaces': {
            Any(): {
                'next_hop': str,
                'application': str,
                'ref_count': str,
                'table': int,
                'vrf': str,
                'flags': str,
            },
        },
    }

class ShowIpMulticastMplsvif(ShowIpMulticastMplsvifSchema):
    """Parser for:
        show ip multicast mpls vif
    """
    cli_command = 'show ip multicast mpls vif'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        if not out.strip():
            return ret_dict

        ## Lspvif9     0.0.0.0              MDT               N/A       11   (vrf vrf3001) 0x1
        p1=re.compile(r"(?P<interface>[a-zA-Z0-9]+)\s+(?P<next_hop>\d+\.\d+\.\d+\.\d+)\s+"
                    "(?P<application>\S+)\s+(?P<ref_count>\S+)\s+(?P<table>\S+)\s+[a-zA-Z\(]*\s*"
                    "(?P<vrf>[a-z0-9]+)\)*\s+(?P<flags>\S+)")

        for line in out.splitlines():
            line=line.strip()

            ## Lspvif9     0.0.0.0              MDT               N/A       11   (vrf vrf3001) 0x1
            m=p1.match(line)
            if m:
                r=m.groupdict()
                intf_dict=ret_dict.setdefault('interfaces',{}).setdefault(r["interface"],{})
                r.pop('interface')
                for key,value in r.items():
                    intf_dict.update({key:int(value) if value.isdigit() else value})

        return ret_dict

class ShowIpMrouteCountSchema(MetaParser):
    ''' search for
        show ip mroute count
    '''

    schema = {
        'routes': int,
        'bytes_of_memory': int,
        'groups': int,
        'average': float,
        'group_id': {
            Any(): {
                'source_count': int,
                'pkt_forwarded': int,
                'pkt_received': int
            }
        },
    }


class ShowIpMrouteCount(ShowIpMrouteCountSchema):
    ''' Parser for
        show ip mroute count
    '''

    cli_command = 'show ip mroute count'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 1009 routes using 1103272 bytes of memory
        p1 = re.compile(r'(?P<routes>\d+)\s+routes\s+using\s+(?P<bytes_of_memory>\d+)')

        # 1005 groups, 0.00 average sources per group
        p2 = re.compile(r'(?P<groups>\d+)\s+groups,\s(?P<average>[\d\.]+)\s+average')

        # Group: 232.3.6.233, Source count: 0, Packets forwarded: 0, Packets received: 0
        p3 = re.compile(
            r'Group:\s+(?P<group>[\w.]+),\s+Source\scount:\s(?P<source_count>\d+),\s+Packets\sforwarded:\s(?P<pkt_forwarded>\d+),\s+Packets\sreceived:\s(?P<pkt_received>\d+)')

        for line in out.splitlines():
            line = line.strip()

            # 1009 routes using 1103272 bytes of memory
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'routes': int(group['routes'])})
                ret_dict.update({'bytes_of_memory': int(group['bytes_of_memory'])})
                continue

            # 1005 groups, 0.00 average sources per group
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'groups': int(group['groups'])})
                ret_dict.update({'average': float(group['average'])})
                continue

            # Group: 232.3.6.233, Source count: 0, Packets forwarded: 0, Packets received: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                groupid = group['group']
                if 'group_id' not in ret_dict:
                    group_dict = ret_dict.setdefault('group_id', {})
                group_dict[groupid] = {}
                group_dict[groupid]['source_count'] = int(group['source_count'])
                group_dict[groupid]['pkt_forwarded'] = int(group['pkt_forwarded'])
                group_dict[groupid]['pkt_received'] = int(group['pkt_received'])
                continue

        return ret_dict