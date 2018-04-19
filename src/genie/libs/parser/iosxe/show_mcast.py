"""show_mcast.py

IOSXE parsers for the following show commands:

    * show ip mroute
    * show ipv6 mroute
    * show ip mroute vrf <vrf_name>
    * show ipv6 mroute vrf <vrf_name>
    * show ip mroute static
    * show ip mroute vrf <vrf_name> static
    * show ip multicast
    * show ip multicast vrf <vrf_name>

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

    def cli(self, cmd='show ip mroute', vrf=''):

        # set vrf infomation
        if vrf:
            cmd += ' vrf {}'.format(vrf)
        else:
            vrf = 'default'

        # excute command to get output
        out = self.device.execute(cmd)

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

            # (*, 239.1.1.1), 00:00:03/stopped, RP 1.1.1.1, flags: SPF
            # (1.1.1.1, 239.1.1.1), 00:00:03/00:02:57, flags: PFT
            # (*, FF07::1), 00:04:45/00:02:47, RP 2001:DB8:6::6, flags:S
            # (2001:DB8:999::99, FF07::1), 00:02:06/00:01:23, flags:SFT
            p2 = re.compile(r'^\((?P<source_address>[\w\:\.\*\/]+),'
                             ' +(?P<multicast_group>[\w\:\.\/]+)\),'
                             ' +(?P<uptime>[\w\:\.]+)\/'
                             '(?P<expires>[\w\:\.]+),'
                             '( +RP +(?P<rendezvous_point>[\w\:\.]+),)?'
                             ' +flags: *(?P<flags>[A-Z]+)$')
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

            # RPF nbr:6:6:6::6
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
            p5 = re.compile(r'^(?P<outgoing_interface>[a-zA-Z0-9\/\.\-]+),'
                             '( +VCD +(?P<vcd>\d+),)?'
                             ' +(?P<state_mode>[\w\/]+),'
                             ' +(?P<uptime>[a-zA-Z0-9\:]+)\/'
                             '(?P<expire>[\w\:]+)'
                             '(, *(?P<flags>\w+))?$')
            m = p5.match(line)
            if m and outgoing:
                outgoing_interface = m.groupdict()['outgoing_interface']
                vcd = m.groupdict()['vcd']
                uptime = m.groupdict()['uptime']
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
    def cli(self, vrf=''):
        return super().cli(cmd='show ipv6 mroute', vrf=vrf)


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

    def cli(self, vrf=''):
        # cli implemetation of parsers
        cmd = 'show ip mroute static' if not vrf else \
              'show ip mroute vrf {} static'.format(vrf)
        vrf = vrf if vrf else 'default'
        out = self.device.execute(cmd)

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
    schema = {'vrf': 
                {Any():
                    {
                    'enable': bool,
                    'multipath': bool,
                    'route_limit': str,
                    'fallback_group_mode': str,
                    'multicast_bound_with_filter_autorp': int,
                    'mo_frr': bool,
                    },
                },
            }

class ShowIpMulticast(ShowIpMulticastSchema):
    """Parser for:
        show ip multicast
        show ip multicast vrf <vrf>
    """
    def cli(self, vrf=''):

        # cli implemetation of parsers
        cmd = 'show ip multicast' if not vrf else \
              'show ip multicast vrf {}'.format(vrf)
        vrf = vrf if vrf else 'default'
        out = self.device.execute(cmd)

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