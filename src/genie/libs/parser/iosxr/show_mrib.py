''' show_mrib.py

IOSXR parsers for the following show commands:
    * 'show mrib vrf <WORD> <WORD> route'
    * 'show mrib vrf <WORD> <WORD> route summary'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use

# ==============================================
# Parser for 'show mrib vrf <WORD> <WORD> route'
# ==============================================

class ShowMribVrfRouteSchema(MetaParser):

    """Schema for show mrib vrf <vrf> <address-family> route"""

    schema = {
        'vrf':
            {Any():
                {'address_family':
                    {Any():
                        {'multicast_group':
                            {Any():
                                {'source_address':
                                    {Any():
                                        {'uptime': str,
                                        Optional('flags'): str,
                                        Optional('rpf_nbr'): str,
                                        Optional('mvpn_tid'): str,
                                        Optional('mvpn_remote_tid'): str,
                                        Optional('mvpn_payload'): str,
                                        Optional('mdt_ifh'): str,
                                        Optional('mt_slot'): str,
                                        Optional('incoming_interface_list'):
                                            {Any():
                                                {'uptime': str,
                                                'flags': str,
                                                Optional('rpf_nbr'): str,
                                                },
                                            },
                                        Optional('outgoing_interface_list'):
                                            {Any():
                                                {'uptime': str,
                                                'flags': str,
                                                Optional('location'): str,
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

class ShowMribVrfRoute(ShowMribVrfRouteSchema):
    """
    Parser for show mrib vrf <vrf> <address-family> route
    For checking any output with the parser, below mandatory keys have to be in cli command.
    - vrf
    - af
    """
    cli_command = 'show mrib vrf {vrf} {af} route'
    exclude = ['uptime']

    def cli(self, vrf='default', af='ipv4',output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(vrf=vrf, af=af))
        else:
            out = output

        # Init vars
        parsed_dict = {}
        rpf_nbr = ''

        for line in out.splitlines():
            line = line.rstrip()

            # (192.168.0.12,227.1.1.1) RPF nbr: 192.168.0.12 Flags: RPF ME MH
            # (*,ff00::/8)
            # (2001:db8:1:0:1:1:1:2,ff15::1:1)
            p1 = re.compile(r'^\s*\((?P<source_address>(\S+))\,'
                             '(?P<multicast_group>(\S+))\)'
                             '(?: *RPF +nbr: +(?P<rpf_nbr>(\S+)))?'
                             '(?: *Flags: +(?P<flags>[a-zA-Z\s]+))?$')
            m = p1.match(line)
            if m:
                # Get values
                source_address = m.groupdict()['source_address']
                multicast_group = m.groupdict()['multicast_group']
                rpf_nbr = m.groupdict()['rpf_nbr']
                flags = m.groupdict()['flags']
                # Init dict
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf] = {}
                if 'address_family' not in parsed_dict['vrf'][vrf]:
                    parsed_dict['vrf'][vrf]['address_family'] = {}
                if af not in parsed_dict['vrf'][vrf]['address_family']:
                    parsed_dict['vrf'][vrf]['address_family'][af] = {}
                if 'multicast_group' not in parsed_dict['vrf'][vrf]\
                        ['address_family'][af]:
                    parsed_dict['vrf'][vrf]['address_family'][af]\
                        ['multicast_group'] = {}
                if multicast_group not in parsed_dict['vrf'][vrf]\
                        ['address_family'][af]['multicast_group']:
                    parsed_dict['vrf'][vrf]['address_family'][af]\
                        ['multicast_group'][multicast_group] = {}
                if 'source_address' not in parsed_dict['vrf'][vrf]\
                        ['address_family'][af]['multicast_group']\
                        [multicast_group]:
                    parsed_dict['vrf'][vrf]['address_family'][af]\
                        ['multicast_group'][multicast_group]\
                        ['source_address'] = {}
                if source_address not in parsed_dict['vrf'][vrf]\
                        ['address_family'][af]['multicast_group']\
                        [multicast_group]['source_address']:
                    parsed_dict['vrf'][vrf]['address_family'][af]\
                        ['multicast_group'][multicast_group]\
                        ['source_address'][source_address] = {}
                sub_dict = parsed_dict['vrf'][vrf]['address_family'][af]\
                    ['multicast_group'][multicast_group]\
                    ['source_address'][source_address]
                # Set values
                if rpf_nbr:
                    sub_dict['rpf_nbr'] = rpf_nbr
                if flags:
                    sub_dict['flags'] = flags
                continue

            # RPF nbr: 2001:db8:b901:0:150:150:150:150 Flags: L C RPF P
            p2 = re.compile(r'^\s*RPF +nbr: +(?P<rpf_nbr>(\S+))'
                             ' +Flags: (?P<flags>[a-zA-Z\s]+)$')
            m = p2.match(line)
            if m:
                rpf_nbr = m.groupdict()['rpf_nbr']
                sub_dict['rpf_nbr'] = rpf_nbr
                sub_dict['flags'] = m.groupdict()['flags']
                continue

            # Flags: D P
            p3 = re.compile(r'^\s*Flags: (?P<flags>[a-zA-Z\s]+)$')
            m = p3.match(line)
            if m:
                sub_dict['flags'] = m.groupdict()['flags']
                continue

            # Up: 00:00:54
            p4 = re.compile(r'^\s*Up: +(?P<uptime>(\S+))$')
            m = p4.match(line)
            if m:
                sub_dict['uptime'] = m.groupdict()['uptime']
                continue

            # MT Slot: 0/2/CPU0
            p5 = re.compile(r'^\s*MT +Slot: +(?P<mt_slot>(\S+))$')
            m = p5.match(line)
            if m:
                sub_dict['mt_slot'] = m.groupdict()['mt_slot']
                continue

            # MVPN TID: 0xe000001f
            p6 = re.compile(r'^\s*MVPN +TID: +(?P<mvpn_tid>(\S+))$')
            m = p6.match(line)
            if m:
                sub_dict['mvpn_tid'] = m.groupdict()['mvpn_tid']
                continue

            # MVPN Remote TID: 0x0
            p7 = re.compile(r'^\s*MVPN +Remote +TID:'
                             ' +(?P<mvpn_remote_tid>(\S+))$')
            m = p7.match(line)
            if m:
                sub_dict['mvpn_remote_tid'] = m.groupdict()['mvpn_remote_tid']
                continue

            # MVPN Payload: IPv4
            p8 = re.compile(r'^\s*MVPN +Payload: +(?P<mvpn_payload>(\S+))$')
            m = p8.match(line)
            if m:
                sub_dict['mvpn_payload'] = \
                    str(m.groupdict()['mvpn_payload']).lower()
                continue

            # MDT IFH: 0x803380
            p9 = re.compile(r'^\s*MDT +IFH: +(?P<mdt_ifh>(\S+))$')
            m = p9.match(line)
            if m:
                sub_dict['mdt_ifh'] = m.groupdict()['mdt_ifh']
                continue

            # Incoming Interface List
            p10 = re.compile(r'^\s*Incoming Interface List$')
            m = p10.match(line)
            if m:
                intf_list_type = 'incoming_interface_list'
                if intf_list_type not in sub_dict:
                    sub_dict[intf_list_type] = {}
                    continue

            # Outgoing Interface List
            p11 = re.compile(r'^\s*Outgoing Interface List$')
            m = p11.match(line)
            if m:
                intf_list_type = 'outgoing_interface_list'
                if intf_list_type not in sub_dict:
                    sub_dict[intf_list_type] = {}
                    continue

            # Loopback0 Flags: F A, Up: 00:00:54
            # GigabitEthernet0/1/0/1 Flags: NS, Up: 00:00:01
            # Decaps6tunnel0 Flags: NS DI, Up: 00:04:40
            # mdtvpn1 Flags: F NS MI MT MA, Up: 00:02:53
            # Bundle-Ether1.100 (0/12/CPU0) Flags: F NS, Up: 5d22h
            p12 = re.compile(r'^\s*(?P<interface>(\S+))'
                              '( *\((?P<location>[\S\s]+)\))?'
                              ' +Flags: +(?P<flags>[a-zA-Z\s]+), +Up:'
                              ' +(?P<uptime>(\S+))$')
            m = p12.match(line)
            if m:
                # Get values
                interface = m.groupdict()['interface']
                flags = m.groupdict()['flags']
                uptime = m.groupdict()['uptime']
                location = m.groupdict()['location']
                if interface not in sub_dict[intf_list_type]:
                    sub_dict[intf_list_type][interface] = {}
                if flags:
                    sub_dict[intf_list_type][interface]['flags'] = flags
                if uptime:
                    sub_dict[intf_list_type][interface]['uptime'] = uptime
                if location:
                    sub_dict[intf_list_type][interface]['location'] = location
                if intf_list_type == 'incoming_interface_list' and rpf_nbr:
                    sub_dict[intf_list_type][interface]['rpf_nbr'] = rpf_nbr
                    continue

        return parsed_dict

# ======================================================
# Parser for 'show mrib vrf <WORD> <WORD> route summary'
# ======================================================

class ShowMribVrfRouteSummarySchema(MetaParser):

    """Schema for show mrib vrf <vrf> <address-family> route summary"""

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'no_group_ranges': int,
                        'no_g_routes': int,
                        'no_s_g_routes': int,
                        'no_route_x_interfaces': int,
                        'total_no_interfaces': int,
                    }
                }
            },
        },
    }

class ShowMribVrfRouteSummary(ShowMribVrfRouteSummarySchema):
    """
    Parser for show mrib vrf <vrf> <address-family> route summary
    For checking any output with the parser, below mandatory keys have to be in cli command.
    - vrf
    - af (optional)
    """
    cli_command = [
                    'show mrib route summary',
                    'show mrib vrf {vrf} route summary',
                    'show mrib vrf {vrf} ipv4 route summary',
                    'show mrib vrf {vrf} ipv6 route summary',
                ]

    def cli(self, vrf='', af='',output=None):
        if output is None:
            if vrf:
                if af == 'ipv4':
                    out = self.device.execute(self.cli_command[2].format(vrf=vrf))
                elif af == 'ipv6':
                    out = self.device.execute(self.cli_command[3].format(vrf=vrf))
                else:
                    out = self.device.execute(self.cli_command[1].format(vrf=vrf))
                    af = 'ipv4'
            else:
                out = self.device.execute(self.cli_command[0])
                af = 'ipv4'
        else:
            out = output

        # Init vars
        parsed_dict = {}
        vrf = ''

        for line in out.splitlines():
            line = line.rstrip()

            # MRIB Route Summary for VRF default
            p1 = re.compile(r'^\s*MRIB +Route +Summary +for +VRF +(?P<vrf>(\S+))\s*$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                parsed_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family', {}).setdefault(af, {})
                continue

            # No. of group ranges = 5
            p2 = re.compile(r'^\s*No\. +of +group +ranges +=\s+(?P<no_group_ranges>[0-9]+)\s*$')
            m = p2.match(line)
            if m:
                parsed_dict['vrf'][vrf]['address_family'][af]['no_group_ranges'] = int(m.groupdict()['no_group_ranges'])
                continue

            # No. of (*,G) routes = 1
            p3 = re.compile(r'^\s*No\. +of +\(\*,G\) +routes +=\s+(?P<no_g_routes>[0-9]+)\s*$')
            m = p3.match(line)
            if m:
                parsed_dict['vrf'][vrf]['address_family'][af]['no_g_routes'] = int(m.groupdict()['no_g_routes'])
                continue

            # No. of (S,G) routes = 0
            p4 = re.compile(r'^\s*No\. +of +\(S,G\) +routes +=\s+(?P<no_s_g_routes>[0-9]+)\s*$')
            m = p4.match(line)
            if m:
                parsed_dict['vrf'][vrf]['address_family'][af]['no_s_g_routes'] = int(m.groupdict()['no_s_g_routes'])
                continue

            # No. of Route x Interfaces (RxI) = 0
            p5 = re.compile(r'^\s*No\. +of +Route +x +Interfaces +\(RxI\) +=\s+(?P<no_route_x_interfaces>[0-9]+)\s*$')
            m = p5.match(line)
            if m:
                parsed_dict['vrf'][vrf]['address_family'][af]['no_route_x_interfaces'] = int(m.groupdict()['no_route_x_interfaces'])
                continue

            # Total No. of Interfaces in all routes = 1
            p6 = re.compile(r'^\s*Total +No\. +of +Interfaces +in +all +routes +=\s+(?P<total_no_interfaces>[0-9]+)\s*$')
            m = p6.match(line)
            if m:
                parsed_dict['vrf'][vrf]['address_family'][af]['total_no_interfaces'] = int(m.groupdict()['total_no_interfaces'])
                continue

        return parsed_dict


# ==========================================================================
# Schema for 'show mrib evpn bucket-db'
# ==========================================================================
class ShowMribEvpnBucketDbSchema(MetaParser):
    """ Schema for show mrib evpn bucket-db. """

    schema = {
        'bucket_id':
            {int:
                {'if_handle': str,
                 'if_name': str,
                 'delete_in_progress': str,
                 'state': str,
                 'uptime': str
                 },
             },
    }


# ==========================================================================
# Parser for 'show mrib evpn bucket-db'
# ==========================================================================
class ShowMribEvpnBucketDb(ShowMribEvpnBucketDbSchema):
    """
    Parser for show mrib evpn bucket-db.

    Parameters
    ----------
    device : Router
        Device to be parsed.

    Returns
    -------
    parsed_dict : dict
        Contains the CLI output parsed into a dictionary.

    Examples
    --------
    >>> show_mrib_evpn_bucket_db(uut1)

    {'bucket_id':
        {0:
            {'if_handle': '0x2007ae0',
             'if_name': 'Bundle-Ether1',
             'delete_in_progress': 'N',
             'state': 'Forward',
             'uptime': '02:24:24'
            },
        1:
            {'if_handle': '0x2007ae0',
             'if_name': 'Bundle-Ether1',
             'delete_in_progress': 'N',
             'state': 'Blocked',
             'uptime': '02:24:24'
            },
        2: ...
        }
    }

    """

    cli_command = ["show mrib evpn bucket-db"]

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        parsed_dict = {}

        # IFName   IFHandle   BucketID    State    Uptime    Delete In Progress
        p1 = re.compile(r"IFName +IFHandle +BucketID +State +Uptime +Delete +In +Progress")

        # Bundle-Ether1   0x400b920   0   Forward   01:56:04   N
        p2 = re.compile(r"(?P<if_name>\S+) +(?P<if_handle>0x[a-fA-F\d]+) +"
                        r"(?P<bucket_id>\d+) +(?P<state>\S+) +"
                        r"(?P<uptime>[\d:dhm]+) +(?P<delete_in_progress>\S+)")

        for line in out.splitlines():
            line = line.strip()

            m1 = p1.match(line)
            if m1:
                parsed_dict.setdefault('bucket_id', {})
                continue

            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                bucket_id = int(group['bucket_id'])
                bucket_dict = parsed_dict['bucket_id'].setdefault(bucket_id, {})
                bucket_dict['if_handle'] = group['if_handle']
                bucket_dict['if_name'] = group['if_name']
                bucket_dict['delete_in_progress'] = group['delete_in_progress']
                bucket_dict['state'] = group['state']
                bucket_dict['uptime'] = group['uptime']
                continue

        return parsed_dict
