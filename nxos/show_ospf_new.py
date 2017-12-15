''' show_ospf.py

NXOS parsers for the following show commands:
    * show ip ospf interface
    * show ip ospf interface vrf <WORD>
    * show ip ospf neighbors detail
    * show ip ospf neighbors detail vrf <WORD>
    * show ip ospf database external detail
    * show ip ospf database external detail vrf <WORD>
    * show ip ospf database network detail
    * show ip ospf database network detail vrf <WORD>
    * show ip ospf database summary detail
    * show ip ospf database summary detail vrf <WORD>
    * show ip ospf database router detail
    * show ip ospf database router detail vrf <WORD>

    * show ip ospf
    * show ip ospf vrf <WORD>
    * show ip ospf mpls ldp interface 
    * show ip ospf mpls ldp interface vrf <WORD>
    * show ip ospf sham-links
    * show ip ospf sham-links vrf <WORD>
    * show ip ospf virtual-links
    * show ip ospf virtual-links vrf <WORD>
'''

# Python
import re

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional
from parser.utils.common import Common


# ================================================
# Schema for 'show ip ospf interface [vrf <WORD>]'
# ================================================
class ShowIpOspfInterfaceSchema(MetaParser):

    ''' Schema for "show ip ospf interface [vrf <WORD>]" '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas': 
                                    {Any(): 
                                        {'interfaces': 
                                            {Any(): 
                                                {'name': str,
                                                'bfd': 
                                                    {'enable': bool},
                                                'enable': bool,
                                                'line_protocol': str,
                                                'ip_address': str,
                                                'state': str,
                                                'interface_type': str,
                                                'cost': int,
                                                'index': int,
                                                'if_cfg': bool,
                                                Optional('transmit_delay'): int,
                                                Optional('passive'): bool,
                                                Optional('priority'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('hello_timer'): str,
                                                Optional('statistics'): 
                                                    {'link_scope_lsa_count': int,
                                                    'link_scope_lsa_cksum_sum': int,
                                                    Optional('total_neighbors'): int,
                                                    Optional('num_nbrs_flooding'): int,
                                                    Optional('num_nbrs_adjacent'): int},
                                                Optional('authentication'):
                                                    {Optional('auth_trailer_key_chain'):
                                                        {Optional('key_chain'): str},
                                                    Optional('auth_trailer_key'):
                                                        {Optional('key'): str,
                                                        Optional('crypto_algorithm'): str},
                                                    },
                                                },
                                            },
                                        Optional('sham_links'): 
                                            {Any(): 
                                                {'name': str,
                                                'bfd': 
                                                    {'enable': bool},
                                                'enable': bool,
                                                'line_protocol': str,
                                                'ip_address': str,
                                                'state': str,
                                                'interface_type': str,
                                                'cost': int,
                                                'index': int,
                                                'if_cfg': bool,
                                                Optional('transmit_delay'): int,
                                                Optional('passive'): bool,
                                                Optional('priority'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('hello_timer'): str,
                                                Optional('statistics'): 
                                                    {'link_scope_lsa_count': int,
                                                    'link_scope_lsa_cksum_sum': int,
                                                    Optional('total_neighbors'): int,
                                                    Optional('num_nbrs_flooding'): int,
                                                    Optional('num_nbrs_adjacent'): int},
                                                Optional('authentication'):
                                                    {Optional('auth_trailer_key_chain'):
                                                        {Optional('key_chain'): str},
                                                    Optional('auth_trailer_key'):
                                                        {Optional('key'): str,
                                                        Optional('crypto_algorithm'): str},
                                                    },
                                                },
                                            },
                                        Optional('virtual_links'): 
                                            {Any(): 
                                                {'name': str,
                                                'bfd': 
                                                    {'enable': bool},
                                                'enable': bool,
                                                'line_protocol': str,
                                                'ip_address': str,
                                                'state': str,
                                                'interface_type': str,
                                                'cost': int,
                                                'index': int,
                                                'if_cfg': bool,
                                                Optional('transmit_delay'): int,
                                                Optional('passive'): bool,
                                                Optional('priority'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('wait_interval'): int,
                                                Optional('hello_timer'): str,
                                                Optional('statistics'): 
                                                    {'link_scope_lsa_count': int,
                                                    'link_scope_lsa_cksum_sum': int,
                                                    Optional('total_neighbors'): int,
                                                    Optional('num_nbrs_flooding'): int,
                                                    Optional('num_nbrs_adjacent'): int},
                                                Optional('authentication'):
                                                    {Optional('auth_trailer_key_chain'):
                                                        {Optional('key_chain'): str},
                                                    Optional('auth_trailer_key'):
                                                        {Optional('key'): str,
                                                        Optional('crypto_algorithm'): str},
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
            },
        }


# ================================================
# Parser for 'show ip ospf interface [vrf <WORD>]'
# ================================================
class ShowIpOspfInterface(ShowIpOspfInterfaceSchema):

    ''' Parser for "show ip ospf interface [vrf <WORD>]" '''

    def cli(self, vrf=''):
        
        # Build command
        cmd = 'show ip ospf interface'
        if vrf:
            cmd += ' vrf {}'.format(vrf)

        # Execute command on device
        out = self.device.execute(cmd)
        
        # Init vars
        ret_dict = {}
        af = 'ipv4'

        # Mapping dict
        bool_dict = {'up': True, 'down': False}

        for line in out.splitlines():
            line = line.strip()

            # Ethernet2/2 is up, line protocol is up
            p1 = re.compile(r'^(?P<intf>(\S+)) +is +(?P<enable>(up|down)),'
                             ' +line +protocol +is'
                             ' +(?P<line_protocol>(up|down))$')
            m = p1.match(line)
            if m:
                # intf name
                interface = intf_name = str(m.groupdict()['intf'])
                # enable
                enable = str(m.groupdict()['enable'])
                # line_protocol
                line_protocol = str(m.groupdict()['line_protocol'])

                # Determine if 'interface' or 'sham_link' or 'virtual_link'
                if re.search('SL', interface):
                    pattern = '(?P<link>\w+)-(?P<area_id>[\w\.\:]+)-(?P<local>[\w\.\:]+)-(?P<remote>[\w\.\:]+)'
                    n = re.match(pattern, interface)
                    link = str(n.groupdict()['link'])
                    area_id = str(n.groupdict()['area_id'])
                    local = str(n.groupdict()['local'])
                    remote = str(n.groupdict()['remote'])
                    # Set values for dict
                    intf_type = 'sham_links'
                    intf_name = local + ' ' + remote
                elif re.search('VL', interface):
                    pattern = '(?P<link>\w+)-(?P<area_id>[\w\.\:]+)-(?P<router_id>[\w\.\:]+)'
                    n = re.match(pattern, interface)
                    link = str(n.groupdict()['link'])
                    area_id = str(n.groupdict()['area_id'])
                    router_id = str(n.groupdict()['router_id'])
                    # Set values for dict
                    intf_type = 'virtual_links'
                    intf_name = area_id + ' ' + router_id
                else:
                    # Set values for dict
                    intf_type = 'interfaces'
                    intf_name = interface

                continue
            
            # IP address 10.2.3.2/24
            p2_1 = re.compile(r'^IP +address +(?P<ip_address>(\S+))$')
            m = p2_1.match(line)
            if m:
                ip_address = str(m.groupdict()['ip_address'])
                continue

            # Unnumbered interface using IP address of loopback1 (22.22.22.22)
            p2_2 = re.compile(r'^Unnumbered +interface +using +IP +address +of'
                               ' +(?P<interface>(\S+))'
                               ' +\((?P<ip_address>(\S+))\)$')
            m = p2_2.match(line)
            if m:
                ip_address = str(m.groupdict()['ip_address'])
                continue

            # Process ID 1 VRF default, area 0.0.0.0
            p3 = re.compile(r'^Process +ID +(?P<pid>(\d+)) +VRF'
                             ' +(?P<vrf>(\S+)), +area +(?P<area>(\S+))$')
            m = p3.match(line)
            if m:
                instance = int(m.groupdict()['pid'])
                vrf = str(m.groupdict()['vrf'])
                area = str(m.groupdict()['area'])
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
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if intf_type not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type] = {}
                if intf_name not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][intf_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name] = {}
                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]\
                            [intf_type][intf_name]
                sub_dict['bfd'] = {}
                sub_dict['bfd']['enable'] = False

                # Set all other values
                try:
                    sub_dict['name'] = interface
                    sub_dict['enable'] = bool_dict[enable]
                    sub_dict['line_protocol'] = line_protocol
                    sub_dict['ip_address'] = ip_address
                    sub_dict['if_cfg'] = False
                except:
                    pass
                    continue

            # Enabled by interface configuration
            p4 = re.compile(r'^Enabled +by +interface +configuration$')
            m = p4.match(line)
            if m:
                sub_dict['if_cfg'] = True
                continue

            # State BDR, Network type BROADCAST, cost 1
            p5 = re.compile(r'^State +(?P<state>(\S+)), +Network +type '
                             '(?P<intf_type>(\S+)), +cost +(?P<cost>(\d+))$')
            m = p5.match(line)
            if m:
                sub_dict['state'] = str(m.groupdict()['state']).lower()
                sub_dict['interface_type'] = \
                    str(m.groupdict()['intf_type']).lower()
                sub_dict['cost'] = int(m.groupdict()['cost'])
                continue

            # Index 3, Transmit delay 1 sec, Router Priority 1
            p6_1 = re.compile(r'^Index +(?P<index>(\d+))(?:, +Transmit +delay'
                               ' +(?P<transmit_delay>(\d+)) +sec)?(?:, +Router'
                               ' +Priority +(?P<priority>(\d+)))?$')
            m = p6_1.match(line)
            if m:
                sub_dict['index'] = int(m.groupdict()['index'])
                if m.groupdict()['transmit_delay']:
                    sub_dict['transmit_delay'] = \
                        int(m.groupdict()['transmit_delay'])
                    sub_dict['passive'] = False
                if m.groupdict()['priority']:
                    sub_dict['priority'] = int(m.groupdict()['priority'])
                continue

            # Index 2, Passive interface
            p6_2 = re.compile(r'^Index +(?P<index>(\d+)), +Passive +interface$')
            m = p6_2.match(line)
            if m:
                sub_dict['index'] = int(m.groupdict()['index'])
                sub_dict['passive'] = True
                continue

            # Designated Router ID: 3.3.3.3, address: 10.2.3.3
            p7_1 = re.compile(r'^(D|d)esignated +(R|r)outer +(ID|Id):'
                               ' (?P<router_id>(\S+)), +address:'
                               ' +(?P<ip_addr>(\S+))$')
            m = p7_1.match(line)
            if m:
                sub_dict['dr_router_id'] = str(m.groupdict()['router_id'])
                sub_dict['dr_ip_addr'] = str(m.groupdict()['ip_addr'])
                continue

            # Backup Designated Router ID: 2.2.2.2, address: 10.2.3.2
            p7_2 = re.compile(r'^(B|b)ackup +(D|d)esignated +(R|r)outer'
                               ' +(ID|Id): +(?P<router_id>(\S+)), +address:'
                               ' +(?P<ip_addr>(\S+))$')
            m = p7_2.match(line)
            if m:
                sub_dict['bdr_router_id'] = str(m.groupdict()['router_id'])
                sub_dict['bdr_ip_addr'] = str(m.groupdict()['ip_addr'])
                continue

            # 1 Neighbors, flooding to 1, adjacent with 1
            p8 = re.compile(r'^(?P<num_neighbors>(\d+)) +Neighbors, +flooding'
                             ' +to +(?P<flooding>(\d+)), +adjacent +with'
                             ' +(?P<adjacent>(\d+))$')
            m = p8.match(line)
            if m:
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}
                sub_dict['statistics']['total_neighbors'] = \
                    int(m.groupdict()['num_neighbors'])
                sub_dict['statistics']['num_nbrs_flooding'] = \
                    int(m.groupdict()['flooding'])
                sub_dict['statistics']['num_nbrs_adjacent'] = \
                    int(m.groupdict()['adjacent'])
                continue

            # Timer intervals: Hello 10, Dead 40, Wait 40, Retransmit 5
            p9 = re.compile(r'^Timer +intervals: +Hello +(?P<hello>(\d+)),'
                             ' +Dead +(?P<dead>(\d+)), +Wait +(?P<wait>(\d+)),'
                             ' +Retransmit +(?P<retransmit>(\d+))$')
            m = p9.match(line)
            if m:
                sub_dict['hello_interval'] = int(m.groupdict()['hello'])
                sub_dict['dead_interval'] = int(m.groupdict()['dead'])
                sub_dict['retransmit_interval'] = \
                    int(m.groupdict()['retransmit'])
                sub_dict['wait_interval'] = int(m.groupdict()['wait'])
                continue

            # Hello timer due in 00:00:02
            p10 = re.compile(r'^Hello +timer +due +in +(?P<hello>(\S+))$')
            m = p10.match(line)
            if m:
                sub_dict['hello_timer'] = str(m.groupdict()['hello'])
                continue

            # Simple authentication
            # Simple authentication, using keychain test (ready)
            # Simple authentication, using keychain test (not ready)
            p11_1 = re.compile(r'^Simple +authentication(?:, +using +keychain'
                                ' +(?P<keychain>(\S+))'
                                ' +\((not +ready|ready)\))?$')
            m = p11_1.match(line)
            if m:
                if 'authentication' not in sub_dict:
                    sub_dict['authentication'] = {}
                if 'auth_trailer_key' not in sub_dict['authentication']:
                    sub_dict['authentication']['auth_trailer_key'] = {}
                    sub_dict['authentication']['auth_trailer_key']\
                        ['crypto_algorithm'] = 'Simple'
                # Set keychain
                if m.groupdict()['keychain']:
                    if 'auth_trailer_key_chain' not in sub_dict['authentication']:
                        sub_dict['authentication']['auth_trailer_key_chain'] = {}
                        sub_dict['authentication']['auth_trailer_key_chain']\
                            ['key_chain'] = str(m.groupdict()['keychain'])
                    continue

            # Message-digest authentication, using default key id 0
            p11_2 = re.compile(r'^Message-digest +authentication, +using'
                                ' +default key id +(?P<key>(\S+))$')
            m = p11_2.match(line)
            if m:
                if 'authentication' not in sub_dict:
                    sub_dict['authentication'] = {}
                if 'auth_trailer_key' not in sub_dict['authentication']:
                    sub_dict['authentication']['auth_trailer_key'] = {}
                    sub_dict['authentication']['auth_trailer_key']\
                        ['crypto_algorithm'] = 'Message-digest'
                if 'auth_trailer_key_chain' not in sub_dict['authentication']:
                    sub_dict['authentication']['auth_trailer_key_chain'] = {}
                    sub_dict['authentication']['auth_trailer_key_chain']\
                        ['key'] = str(m.groupdict()['key'])
                    continue

            # Number of opaque link LSAs: 0, checksum sum 0
            p12 = re.compile(r'^Number +of +opaque +link +LSAs:'
                              ' +(?P<count>(\d+)), +checksum +sum'
                              ' +(?P<checksum>(\d+))$')
            m = p12.match(line)
            if m:
                count = int(m.groupdict()['count'])
                checksum = int(m.groupdict()['checksum'])
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}
                sub_dict['statistics']['link_scope_lsa_count'] = \
                    int(m.groupdict()['count'])
                sub_dict['statistics']['link_scope_lsa_cksum_sum'] = \
                    int(m.groupdict()['checksum'])
                continue

            # BFD is enabled
            p13 = re.compile(r'^BFD +is +enabled$')
            m = p13.match(line)
            if m:
                sub_dict['bfd']['enable'] = True

        return ret_dict


# =======================================================
# Schema for 'show ip ospf neighbors detail [vrf <WORD>]'
# =======================================================
class ShowIpOspfNeighborDetailSchema(MetaParser):

    ''' Schema for "show ip ospf neighbors detail [vrf <WORD>]" '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas': 
                                    {Any(): 
                                        {'interfaces': 
                                            {Any(): 
                                                {'neighbors':
                                                     {Any(): 
                                                        {'neighbor_router_id': str,
                                                        'address': str,
                                                        'state': str,
                                                        'last_state_change': str,
                                                        Optional('priority'): int,
                                                        Optional('dr_ip_addr'): str,
                                                        Optional('bdr_ip_addr'): str,
                                                        Optional('dr_router_id'): str,
                                                        Optional('bdr_router_id'): str,
                                                        'hello_options': str,
                                                        'dbd_options': str,
                                                        'last_non_hello_packet_received': str,
                                                        'dead_timer': str,
                                                        Optional('statistics'): {
                                                            Optional('nbr_event_count'): int,
                                                            },
                                                        },
                                                     },
                                                },
                                            },
                                        Optional('virtual_links'): 
                                            {Any(): 
                                                {'neighbors':
                                                     {Any(): 
                                                        {'neighbor_router_id': str,
                                                        'address': str,
                                                        'state': str,
                                                        'last_state_change': str,
                                                        Optional('priority'): int,
                                                        Optional('dr_ip_addr'): str,
                                                        Optional('bdr_ip_addr'): str,
                                                        Optional('dr_router_id'): str,
                                                        Optional('bdr_router_id'): str,
                                                        'hello_options': str,
                                                        'dbd_options': str,
                                                        'last_non_hello_packet_received': str,
                                                        'dead_timer': str,
                                                        Optional('statistics'): {
                                                            Optional('nbr_event_count'): int,
                                                            },
                                                        },
                                                     },
                                                },
                                            },
                                        Optional('sham_links'):
                                            {Any(): 
                                                {'neighbors':
                                                     {Any(): 
                                                        {'neighbor_router_id': str,
                                                        'address': str,
                                                        'state': str,
                                                        'last_state_change': str,
                                                        Optional('priority'): int,
                                                        Optional('dr_ip_addr'): str,
                                                        Optional('bdr_ip_addr'): str,
                                                        Optional('dr_router_id'): str,
                                                        Optional('bdr_router_id'): str,
                                                        'hello_options': str,
                                                        'dbd_options': str,
                                                        'last_non_hello_packet_received': str,
                                                        'dead_timer': str,
                                                        Optional('statistics'): {
                                                            Optional('nbr_event_count'): int,
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
                    },
                },
            },
        }


# =======================================================
# Parser for 'show ip ospf neighbors detail [vrf <WORD>]'
# =======================================================
class ShowIpOspfNeighborDetail(ShowIpOspfNeighborDetailSchema):

    ''' Parser for "show ip ospf neighbors detail [vrf <WORD>]" '''

    def cli(self, vrf=''):
        
        # Build command
        cmd = 'show ip ospf neighbors detail'
        if vrf:
            cmd += ' vrf {}'.format(vrf)

        # Execute command on device
        out = self.device.execute(cmd)
        
        # Init vars
        ret_dict = {}
        af = 'ipv4'

        for line in out.splitlines():
            line = line.strip()

            # Neighbor 3.3.3.3, interface address 10.2.3.3
            p1 = re.compile(r'^Neighbor +(?P<neighbor_router_id>(\S+)),'
                             ' +interface +address +(?P<address>(\S+))$')
            m = p1.match(line)
            if m:
                neighbor = str(m.groupdict()['neighbor_router_id'])
                address = str(m.groupdict()['address'])
                continue

            # Process ID 1 VRF default, in area 0.0.0.0 via interface Ethernet2/2
            # Process ID 1 VRF VRF1, in area 0.0.0.1 via interface SL1-0.0.0.0-22.22.22.22-11.11.11.11
            # Process ID 1 VRF default, in area 0.0.0.0 via interface VL1-0.0.0.1-4.4.4.4
            p2 = re.compile(r'^Process +ID +(?P<instance>(\S+)) +VRF'
                             ' +(?P<vrf>(\S+)), +in +area +(?P<area>(\S+))'
                             ' +via +interface +(?P<interface>(\S+))$')
            m = p2.match(line)
            if m:
                instance = str(m.groupdict()['instance'])
                vrf = str(m.groupdict()['vrf'])
                area = str(m.groupdict()['area'])
                interface = str(m.groupdict()['interface'])

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
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}

                # Determine if 'interface' or 'sham_link' or 'virtual_link'
                if re.search('SL', interface):
                    pattern = '(?P<link>\w+)-(?P<area_id>[\w\.\:]+)-(?P<local>[\w\.\:]+)-(?P<remote>[\w\.\:]+)'
                    n = re.match(pattern, interface)
                    link = str(n.groupdict()['link'])
                    area_id = str(n.groupdict()['area_id'])
                    local = str(n.groupdict()['local'])
                    remote = str(n.groupdict()['remote'])
                    # Set values for dict
                    intf_type = 'sham_links'
                    intf_name = local + ' ' + remote

                elif re.search('VL', interface):
                    pattern = '(?P<link>\w+)-(?P<area_id>[\w\.\:]+)-(?P<router_id>[\w\.\:]+)'
                    n = re.match(pattern, interface)
                    link = str(n.groupdict()['link'])
                    area_id = str(n.groupdict()['area_id'])
                    router_id = str(n.groupdict()['router_id'])
                    # Set values for dict
                    intf_type = 'virtual_links'
                    intf_name = area_id + ' ' + router_id
                else:
                    # Set values for dict
                    intf_type = 'interfaces'
                    intf_name = interface

                # Set interface/sham_link/virtual_link dict
                if intf_type not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type] = {}
                if intf_name not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area][intf_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name] = {}
                if 'neighbors' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]\
                        [intf_type][intf_name]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name]\
                        ['neighbors'] = {}
                if neighbor not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]\
                        [intf_type][intf_name]['neighbors']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area][intf_type][intf_name]\
                        ['neighbors'][neighbor] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]\
                            [intf_type][intf_name]['neighbors'][neighbor]

                # Set previously parsed keys
                sub_dict['neighbor_router_id'] = neighbor
                sub_dict['address'] = address
                continue

            # State is FULL, 5 state changes, last change 08:38:40
            p3 = re.compile(r'^State +is +(?P<state>(\S+)),'
                             ' +(?P<changes>(\d+)) +state +changes,'
                             ' +last +change +(?P<last>(\S+))$')
            m = p3.match(line)
            if m:
                sub_dict['state'] = str(m.groupdict()['state']).lower()
                sub_dict['last_state_change'] = str(m.groupdict()['last'])
                if 'statistics' not in sub_dict:
                    sub_dict['statistics'] = {}
                    sub_dict['statistics']['nbr_event_count'] = int(m.groupdict()['changes'])
                    continue

            # Neighbor priority is 1
            p4 = re.compile(r'^Neighbor +priority +is +(?P<priority>(\S+))$')
            m = p4.match(line)
            if m:
                sub_dict['priority'] = int(m.groupdict()['priority'])
                continue

            # DR is 10.2.3.3 BDR is 10.2.3.2
            p5 = re.compile(r'^DR +is +(?P<dr_ip>(\S+)) +BDR +is'
                             ' +(?P<bdr_ip>(\S+))$')
            m = p5.match(line)
            if m:
                sub_dict['dr_ip_addr'] = str(m.groupdict()['dr_ip'])
                sub_dict['bdr_ip_addr'] = str(m.groupdict()['bdr_ip'])
                continue

            # Hello options 0x12, dbd options 0x52
            p6 = re.compile(r'^Hello +options +(?P<hello_options>(\S+)),'
                             ' +dbd +options +(?P<dbd_options>(\S+))$')
            m = p6.match(line)
            if m:
                sub_dict['hello_options'] = str(m.groupdict()['hello_options'])
                sub_dict['dbd_options']= str(m.groupdict()['dbd_options'])
                continue

            # Last non-hello packet received never
            p7 = re.compile(r'^Last +non-hello +packet +received'
                             ' +(?P<non_hello>(\S+))$')
            m = p7.match(line)
            if m:
                sub_dict['last_non_hello_packet_received'] = \
                    str(m.groupdict()['non_hello'])
                continue

            # Dead timer due in 00:00:39
            p8 = re.compile(r'^Dead +timer +due +in +(?P<dead_timer>(\S+))$')
            m = p8.match(line)
            if m:
                sub_dict['dead_timer'] = str(m.groupdict()['dead_timer'])
                continue

        return ret_dict


# ===================================================================
# Super parser for 'show ip ospf database <WORD> detail [vrf <WORD>]'
# ===================================================================
class ShowIpOspfDatabaseDetailParser(MetaParser):

    ''' Parser for "show ip ospf database <WORD> detail [vrf <WORD>]" '''

    def cli(self, cmd, db_type):

        assert db_type in ['external', 'network', 'summary', 'router',
                           'opaque']

        # Execute command on device
        out = self.device.execute(cmd)
        
        # Init vars
        ret_dict = {}
        af = 'ipv4'
        mt_id = 0

        # Router
        # Network Link
        # Summary Network
        # Opaque Area
        # Type-5 AS External
        lsa_type_mapping = {
            'router': 1,
            'network': 2,
            'summary': 3,
            'external': 5,
            'opaque': 10,
            }

        for line in out.splitlines():
            line = line.strip()

            # OSPF Router with ID (2.2.2.2) (Process ID 1 VRF default)
            # OSPF Router with ID (22.22.22.22) (Process ID 1 VRF VRF1)
            p1 = re.compile(r'^OSPF +Router +with +ID +\((?P<router_id>(\S+))\)'
                             ' +\(Process +ID +(?P<instance>(\d+))'
                             ' +VRF +(?P<vrf>(\S+))\)$')
            m = p1.match(line)
            if m:
                router_id = str(m.groupdict()['router_id'])
                instance = str(m.groupdict()['instance'])
                vrf = str(m.groupdict()['vrf'])
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

            # Type-5 AS External Link States (Area 0.0.0.0)
            # Opaque Area Link States (Area 0.0.0.0)
            # Summary Network Link States (Area 0.0.0.0)
            # Network Link States (Area 0.0.0.0)
            p2 = re.compile(r'^(?P<lsa_type_name>(.*)) +Link +States'
                             '(?: +\(Area +(?P<area>(\S+))\))?$')
            m = p2.match(line)
            if m:
                lsa_type = lsa_type_mapping[db_type]
                
                # Set area
                if m.groupdict()['area']:
                    area = str(m.groupdict()['area'])
                else:
                    area = '0.0.0.0'

                # Create dict structure
                if 'areas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'] = {}
                if area not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area] = {}
                if 'database' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['database'] = {}
                if 'lsa_types' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]['database']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['database']['lsa_types'] = {}
                if lsa_type not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['database']\
                        ['lsa_types']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['database']['lsa_types']\
                        [lsa_type] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]['database']\
                            ['lsa_types'][lsa_type]

                # Set lsa_type
                sub_dict['lsa_type'] = lsa_type
                continue

            # LS age: 1565
            p3 = re.compile(r'^LS +age: +(?P<age>(\d+))$')
            m = p3.match(line)
            if m:
                age = int(m.groupdict()['age'])
                continue

            # Options: 0x20 (No TOS-capability, DC)
            p4 = re.compile(r'^Options: +(?P<option>([a-zA-Z0-9]+))(?:'
                             ' *\((?P<option_desc>(.*))\))?$')
            m = p4.match(line)
            if m:
                option = str(m.groupdict()['option'])
                option_desc = str(m.groupdict()['option_desc'])
                continue

            # LS Type: Type-5 AS-External
            p5 = re.compile(r'^LS +Type: +(?P<lsa_type>(.*))$')
            m = p5.match(line)
            if m:
                lsa_type = lsa_type_mapping[db_type]
                continue

            # Link State ID: 1.1.1.1
            # Link State ID: 44.44.44.44 (Network address)
            # Link State ID: 10.1.2.1 (Designated Router address)
            p5 = re.compile(r'^Link +State +ID: +(?P<lsa_id>(\S+))'
                             '(?: +\(.*\))?$')
            m = p5.match(line)
            if m:
                lsa_id = str(m.groupdict()['lsa_id'])
                continue

            # Advertising Router: 4.4.4.4
            p6 = re.compile(r'^Advertising +Router: +(?P<adv_router>(\S+))$')
            m = p6.match(line)
            if m:
                adv_router = str(m.groupdict()['adv_router'])
                lsa = lsa_id + ' ' + adv_router
                
                # Reset counters for this lsa
                link_tlv_counter = 0
                unknown_tlvs_counter = 0

                # Create schema structure
                if 'lsas' not in sub_dict:
                    sub_dict['lsas'] = {}
                if lsa not in sub_dict['lsas']:
                    sub_dict['lsas'][lsa] = {}
                
                # Set keys under 'lsa'
                sub_dict['lsas'][lsa]['adv_router'] = adv_router
                try:
                    sub_dict['lsas'][lsa]['lsa_id'] = lsa_id
                except:
                    pass

                # Set db_dict
                if 'ospfv2' not in sub_dict['lsas'][lsa]:
                    sub_dict['lsas'][lsa]['ospfv2'] = {}
                if 'body' not in sub_dict['lsas'][lsa]['ospfv2']:
                    sub_dict['lsas'][lsa]['ospfv2']['body'] = {}
                if db_type not in sub_dict['lsas'][lsa]['ospfv2']['body']:
                    sub_dict['lsas'][lsa]['ospfv2']['body'][db_type] = {}
                db_dict = sub_dict['lsas'][lsa]['ospfv2']['body'][db_type]

                # Create 'topologies' sub_dict if 'summary' or 'database'
                if db_type in ['summary', 'external']:
                    if 'topologies' not in db_dict:
                        db_dict['topologies'] = {}
                    if mt_id not in db_dict['topologies']:
                        db_dict['topologies'][mt_id] = {}
                    db_topo_dict = db_dict['topologies'][mt_id]
                    db_topo_dict['mt_id'] = mt_id

                # Set header dict
                if 'header' not in sub_dict['lsas'][lsa]['ospfv2']:
                    sub_dict['lsas'][lsa]['ospfv2']['header'] = {}
                header_dict = sub_dict['lsas'][lsa]['ospfv2']['header']

                try:
                    # Set previously parsed values
                    header_dict['age'] = age
                except:
                    pass
                try:
                    header_dict['option'] = option
                except:
                    pass
                try:
                    header_dict['option_desc'] = option_desc
                except:
                    pass
                try:
                    header_dict['type'] = lsa_type
                except:
                    pass
                try:
                    header_dict['lsa_id'] = lsa_id
                except:
                    pass
                try:
                    header_dict['adv_router'] = adv_router
                except:
                    pass
                try:
                    header_dict['opaque_type'] = opaque_type
                except:
                    pass
                try:
                    header_dict['opaque_id'] = opaque_id
                except:
                    pass

            # LS Seq Number: 0x80000002
            p7 = re.compile(r'^LS +Seq +Number: +(?P<ls_seq_num>(\S+))$')
            m = p7.match(line)
            if m:
                header_dict['seq_num'] = str(m.groupdict()['ls_seq_num'])
                continue

            # Checksum: 0x7d61
            p8 = re.compile(r'^Checksum: +(?P<checksum>(\S+))$')
            m = p8.match(line)
            if m:
                header_dict['checksum'] = str(m.groupdict()['checksum'])
                continue

            # Length: 36
            p9 = re.compile(r'^Length: +(?P<length>(\d+))$')
            m = p9.match(line)
            if m:
                header_dict['length'] = int(m.groupdict()['length'])
                continue

            # Network Mask: /32
            p10 = re.compile(r'^Network +Mask: +\/(?P<net_mask>(\S+))$')
            m = p10.match(line)
            if m:
                db_dict['network_mask'] = '.'.join([str((0xffffffff << (32 - int(m.groupdict()['net_mask'])) >> i) & 0xff) for i in [24, 16, 8, 0]])
                continue

            # Metric Type: 2 (Larger than any link state path)
            p11 = re.compile(r'^Metric +Type: +2 +\(.*\)$')
            m = p11.match(line)
            if m:
                db_topo_dict['flags'] = "E"
                continue

            # TOS: 0
            # TOS: 0 Metric: 1
            p12 = re.compile(r'^TOS:? +(?P<tos>(\d+))'
                              '(?: +Metric: +(?P<metric>(\d+)))?$')
            m = p12.match(line)
            if m:
                if db_type == 'router':
                    tos = int(m.groupdict()['tos'])
                    if m.groupdict()['metric']:
                        metric = int(m.groupdict()['metric'])
                        continue
                else:
                    db_topo_dict['tos'] = int(m.groupdict()['tos'])
                    if m.groupdict()['metric']:
                        db_topo_dict['metric'] = int(m.groupdict()['metric'])
                        continue

            # Metric: 20
            p13 = re.compile(r'^Metric: +(?P<metric>(\d+))$')
            m = p13.match(line)
            if m:
                if db_type == 'router':
                    metric = int(m.groupdict()['metric'])
                    continue
                else: 
                    db_topo_dict['metric'] = int(m.groupdict()['metric'])
                    continue

            # Forward Address: 0.0.0.0
            p14 = re.compile(r'^Forward +Address: +(?P<addr>(\S+))$')
            m = p14.match(line)
            if m:
                db_topo_dict['forwarding_address'] = str(m.groupdict()['addr'])
                continue

            # External Route Tag: 0
            p15 = re.compile(r'^External +Route +Tag: +(?P<tag>(\S+))$')
            m = p15.match(line)
            if m:
                db_topo_dict['external_route_tag'] = str(m.groupdict()['tag'])            
                continue

            # Attached Router: 66.66.66.66
            p16 = re.compile(r'^Attached +Router: +(?P<att_router>(\S+))$')
            m = p16.match(line)
            if m:
                attached_router = str(m.groupdict()['att_router'])
                if 'attached_routers' not in db_dict:
                    db_dict['attached_routers'] = {}
                if attached_router not in db_dict['attached_routers']:
                    db_dict['attached_routers'][attached_router] = {}
                    continue

            # Number of links: 3
            p17 = re.compile(r'^Number +of +links: +(?P<num>(\d+))$')
            m = p17.match(line)
            if m:
                db_dict['num_of_links'] = int(m.groupdict()['num'])
                continue

            # Link connected to: a Stub Network
            p18 = re.compile(r'^Link +connected +to: +a +(?P<type>(.*))$')
            m = p18.match(line)
            if m:
                link_type = str(m.groupdict()['type']).lower()
                continue

            # (Link ID) Network/Subnet Number: 1.1.1.1
            p19_1 = re.compile(r'^\(Link +ID\) +Network\/Subnet +Number:'
                                ' +(?P<link_id>(\S+))$')
            m = p19_1.match(line)
            if m:
                link_id = str(m.groupdict()['link_id'])

                # Create dict structures
                if 'links' not in db_dict:
                    db_dict['links'] = {}
                if link_id not in db_dict['links']:
                    db_dict['links'][link_id] = {}
                db_dict['links'][link_id]['link_id'] = link_id

                # Set previously parsed values
                try:
                    db_dict['links'][link_id]['type'] = link_type
                except:
                    pass
                
                # Create topology dict under link_id
                if 'topologies' not in db_dict['links'][link_id]:
                    db_dict['links'][link_id]['topologies'] = {}
                if mt_id not in db_dict['links'][link_id]['topologies']:
                    db_dict['links'][link_id]['topologies'][mt_id] = {}
                try:
                    # Set previously parsed values
                    db_dict['links'][link_id]['topologies'][mt_id]['mt_id'] = mt_id
                    db_dict['links'][link_id]['topologies'][mt_id]['metric'] = metric
                    db_dict['links'][link_id]['topologies'][mt_id]['tos'] = tos
                    continue
                except:
                    pass

            # (Link ID) Designated Router address: 20.6.7.6
            p19_2 = re.compile(r'^\(Link +ID\) +Designated +Router +address:'
                                ' +(?P<link_id>(\S+))$')
            m = p19_2.match(line)
            if m:
                link_id = str(m.groupdict()['link_id'])

                # Create dict structures
                if 'links' not in db_dict:
                    db_dict['links'] = {}
                if link_id not in db_dict['links']:
                    db_dict['links'][link_id] = {}
                db_dict['links'][link_id]['link_id'] = link_id

                # Set previously parsed values
                try:
                    db_dict['links'][link_id]['type'] = link_type
                except:
                    pass
                
                # Create topology dict under link_id
                if 'topologies' not in db_dict['links'][link_id]:
                    db_dict['links'][link_id]['topologies'] = {}
                if mt_id not in db_dict['links'][link_id]['topologies']:
                    db_dict['links'][link_id]['topologies'][mt_id] = {}
                try:
                    # Set previously parsed values
                    db_dict['links'][link_id]['topologies'][mt_id]['mt_id'] = mt_id
                    db_dict['links'][link_id]['topologies'][mt_id]['metric'] = metric
                    db_dict['links'][link_id]['topologies'][mt_id]['tos'] = tos
                    continue
                except:
                    pass

            # (Link ID) Neighboring Router ID: 22.22.22.22
            p19_3 = re.compile(r'^\(Link +ID\) +Neighboring +Router +ID:'
                                ' +(?P<link_id>(\S+))$')
            m = p19_3.match(line)
            if m:
                link_id = str(m.groupdict()['link_id'])

                # Create dict structures
                if 'links' not in db_dict:
                    db_dict['links'] = {}
                if link_id not in db_dict['links']:
                    db_dict['links'][link_id] = {}
                db_dict['links'][link_id]['link_id'] = link_id

                # Set previously parsed values
                try:
                    db_dict['links'][link_id]['type'] = link_type
                except:
                    pass
                
                # Create topology dict under link_id
                if 'topologies' not in db_dict['links'][link_id]:
                    db_dict['links'][link_id]['topologies'] = {}
                if mt_id not in db_dict['links'][link_id]['topologies']:
                    db_dict['links'][link_id]['topologies'][mt_id] = {}
                try:
                    # Set previously parsed values
                    db_dict['links'][link_id]['topologies'][mt_id]['mt_id'] = mt_id
                    db_dict['links'][link_id]['topologies'][mt_id]['metric'] = metric
                    db_dict['links'][link_id]['topologies'][mt_id]['tos'] = tos
                    continue
                except:
                    pass

            # (Link Data) Network Mask: 255.255.255.255
            p20_1 = re.compile(r'^\(Link +Data\) +Network +Mask:'
                                ' +(?P<link_data>(\S+))$')
            m = p20_1.match(line)
            if m:
                db_dict['links'][link_id]['link_data'] = \
                    str(m.groupdict()['link_data'])
                continue

            # (Link Data) Router Interface address: 20.6.7.6
            p20_2 = re.compile(r'^\(Link +Data\) +Router +Interface +address:'
                                ' +(?P<link_data>(\S+))$')
            m = p20_2.match(line)
            if m:
                db_dict['links'][link_id]['link_data'] = \
                    str(m.groupdict()['link_data'])
                continue

            # Number of TOS metrics: 0
            p21 = re.compile(r'^Number +of +TOS +metrics: +(?P<num>(\d+))$')
            m = p21.match(line)
            if m:
                db_dict['links'][link_id]['num_tos_metrics'] = \
                    int(m.groupdict()['num'])
                continue

            # Opaque Type: 1
            p22 = re.compile(r'^Opaque +Type: +(?P<type>(\d+))$')
            m = p22.match(line)
            if m:
                opaque_type = int(m.groupdict()['type'])
                continue
            
            # Opaque ID: 38
            p23 = re.compile(r'^Opaque +ID: +(?P<id>(\d+))$')
            m = p23.match(line)
            if m:
                opaque_id = int(m.groupdict()['id'])
                continue

            # Fragment number: 0
            p24 = re.compile(r'^Fragment +number: +(?P<num>(\d+))$')
            m = p24.match(line)
            if m:
                header_dict['fragment_number'] = int(m.groupdict()['num'])
                continue

            # MPLS TE router ID : 1.1.1.1
            p25 = re.compile(r'^MPLS +TE +router +ID *: +(?P<mpls>(\S+))$')
            m = p25.match(line)
            if m:
                header_dict['mpls_te_router_id'] = str(m.groupdict()['mpls'])
                continue

            # Number of Links : 0
            p26 = re.compile(r'^Number +of +Links *: +(?P<links>(\d+))$')
            m = p26.match(line)
            if m:
                header_dict['num_links'] = int(m.groupdict()['links'])
                continue

            # Link connected to Broadcast network
            p27 = re.compile(r'^Link +connected +to +(?P<link>(.*))$')
            m = p27.match(line)
            if m:
                link_tlv_counter += 1
                if 'link_tlvs' not in db_dict:
                    db_dict['link_tlvs'] = {}
                if link_tlv_counter not in db_dict['link_tlvs']:
                    db_dict['link_tlvs'][link_tlv_counter] = {}

                # Set link type
                opaque_link = str(m.groupdict()['link'])
                if opaque_link == 'Broadcast network':
                    opaque_link_type = 2
                else:
                    opaque_link_type = 1
                db_dict['link_tlvs'][link_tlv_counter]\
                    ['link_type'] = opaque_link_type
                db_dict['link_tlvs'][link_tlv_counter]\
                    ['link_name'] = opaque_link
                
                # Set remote_if_ipv4_addrs (if needed)
                if opaque_link_type == 2:
                    if 'remote_if_ipv4_addrs' not in db_dict['link_tlvs']\
                            [link_tlv_counter]:
                        db_dict['link_tlvs'][link_tlv_counter]\
                            ['remote_if_ipv4_addrs'] = {}
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['remote_if_ipv4_addrs']['0.0.0.0'] = {}
                continue

            # Link ID : 10.1.4.4
            p28 = re.compile(r'^Link +ID *: +(?P<id>(\S+))$')
            m = p28.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['link_id'] = \
                    str(m.groupdict()['id'])
                continue

            # Interface Address : 10.1.4.1
            p29 = re.compile(r'^Interface +Address *: +(?P<addr>(\S+))$')
            m = p29.match(line)
            if m:
                addr = str(m.groupdict()['addr'])
                if 'local_if_ipv4_addrs' not in db_dict['link_tlvs']\
                        [link_tlv_counter]:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['local_if_ipv4_addrs'] = {}
                if addr not in db_dict['link_tlvs'][link_tlv_counter]\
                        ['local_if_ipv4_addrs']:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['local_if_ipv4_addrs'][addr] = {}
                    continue

            # Admin Metric : 1
            p30 = re.compile(r'^Admin +Metric *: +(?P<te_metric>(\d+))$')
            m = p30.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['te_metric'] = \
                    int(m.groupdict()['te_metric'])
                continue

            # Maximum Bandwidth : 125000000
            p31 = re.compile(r'^Maximum +(B|b)andwidth *:'
                              ' +(?P<max_band>(\d+))$')
            m = p31.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['max_bandwidth'] = \
                    int(m.groupdict()['max_band'])
                continue

            # Maximum reservable bandwidth : 93750000
            p32 = re.compile(r'^Maximum +(R|r)eservable +(B|b)andwidth *:'
                              ' +(?P<max_res_band>(\d+))$')
            m = p32.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]\
                    ['max_reservable_bandwidth'] = \
                    int(m.groupdict()['max_res_band'])
                continue

            # Affinity Bit : 0x0
            p33 = re.compile(r'^Affinity +Bit *: +(?P<admin_group>(\S+))$')
            m = p33.match(line)
            if m:
                db_dict['link_tlvs'][link_tlv_counter]['admin_group'] = \
                    str(m.groupdict()['admin_group'])
                continue

            # Number of Priority : 8
            
            # Priority 0 : 93750000    Priority 1 : 93750000
            p34 = re.compile(r'^Priority +(?P<num1>(\d+)) *:'
                              ' +(?P<band1>(\d+))(?: +Priority +(?P<num2>(\d+))'
                              ' *: +(?P<band2>(\d+)))?$')
            m = p34.match(line)
            if m:
                value1 = str(m.groupdict()['num1']) + ' ' + \
                         str(m.groupdict()['band1'])
                value2 = str(m.groupdict()['num2']) + ' ' + \
                         str(m.groupdict()['band2'])
                if 'unreserved_bandwidths' not in db_dict['link_tlvs']\
                        [link_tlv_counter]:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'] = {}
                if value1 not in db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths']:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value1] = {}
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value1]['priority'] = \
                        int(m.groupdict()['num1'])
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value1]\
                        ['unreserved_bandwidth'] = int(m.groupdict()['band1'])
                if value2 not in db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths']:
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value2] = {}
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value2]['priority'] = \
                            int(m.groupdict()['num2'])
                    db_dict['link_tlvs'][link_tlv_counter]\
                        ['unreserved_bandwidths'][value2]\
                        ['unreserved_bandwidth'] = int(m.groupdict()['band2'])
                    continue

            # Unknown Sub-TLV   :  Type = 32770, Length = 4 Value = 00 00 00 01
            p35 = re.compile(r'^Unknown +Sub-TLV *: +Type += +(?P<type>(\d+)),'
                              ' +Length += +(?P<length>(\d+))'
                              ' +Value += +(?P<value>(.*))$')
            m = p35.match(line)
            if m:
                unknown_tlvs_counter += 1
                if 'unknown_tlvs' not in db_dict['link_tlvs'][link_tlv_counter]:
                    db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs'] = {}
                if unknown_tlvs_counter not in db_dict['link_tlvs']\
                        [link_tlv_counter]['unknown_tlvs']:
                    db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                        [unknown_tlvs_counter] = {}
                db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                    [unknown_tlvs_counter]['type'] = int(m.groupdict()['type'])
                db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                    [unknown_tlvs_counter]['length'] = int(m.groupdict()['length'])
                db_dict['link_tlvs'][link_tlv_counter]['unknown_tlvs']\
                    [unknown_tlvs_counter]['value'] = str(m.groupdict()['value'])
                continue


        return ret_dict


# ===============================================================
# Schema for 'show ip ospf database external detail [vrf <WORD>]'
# ===============================================================
class ShowIpOspfDatabaseExternalDetailSchema(MetaParser):

    ''' Schema for "show ip ospf database external detail [vrf <WORD>]" '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas': 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int},
                                                                'body': 
                                                                    {'external': 
                                                                        {'network_mask': str,
                                                                        'topologies': 
                                                                            {Any(): 
                                                                                {'mt_id': int,
                                                                                'tos': int,
                                                                                'flags': str,
                                                                                'metric': int,
                                                                                'forwarding_address': str,
                                                                                'external_route_tag': str},
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
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ===================================================================
# Super parser for 'show ip ospf database <WORD> detail [vrf <WORD>]'
# ===================================================================
class ShowIpOspfDatabaseExternalDetail(ShowIpOspfDatabaseExternalDetailSchema, ShowIpOspfDatabaseDetailParser):

    ''' Parser for "show ip ospf database external detail [vrf <WORD>]" '''

    def cli(self, vrf=''):
        # excute command to get output
        # Build command
        cmd = 'show ip ospf database external detail'
        if vrf:
            cmd += ' vrf {}'.format(vrf)

        return super().cli(cmd=cmd, db_type='external')


# ==============================================================
# Schema for 'show ip ospf database network detail [vrf <WORD>]'
# ==============================================================
class ShowIpOspfDatabaseNetworkDetailSchema(MetaParser):

    ''' Schema for "show ip ospf database network detail [vrf <WORD>]" '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas': 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int},
                                                                'body': 
                                                                    {'network': 
                                                                        {'network_mask': str,
                                                                        'attached_routers': 
                                                                            {Any(): {},
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
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ===============================================================
# Parser for 'show ip ospf database network detail [vrf <WORD>]'
# ===============================================================
class ShowIpOspfDatabaseNetworkDetail(ShowIpOspfDatabaseNetworkDetailSchema, ShowIpOspfDatabaseDetailParser):

    ''' Parser for "show ip ospf database network detail [vrf <WORD>]" '''

    def cli(self, vrf=''):
        # excute command to get output
        # Build command
        cmd = 'show ip ospf database network detail'
        if vrf:
            cmd += ' vrf {}'.format(vrf)

        return super().cli(cmd=cmd, db_type='network')


# ==============================================================
# Schema for 'show ip ospf database summary detail [vrf <WORD>]'
# ==============================================================
class ShowIpOspfDatabaseSummaryDetailSchema(MetaParser):

    ''' Schema for "show ip ospf database summary detail [vrf <WORD>]" '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas': 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int},
                                                                'body': 
                                                                    {'summary': 
                                                                        {'network_mask': str,
                                                                        'topologies': 
                                                                            {Any(): 
                                                                                {'mt_id': int,
                                                                                'tos': int,
                                                                                'metric': int},
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
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ===============================================================
# Parser for 'show ip ospf database summary detail [vrf <WORD>]'
# ===============================================================
class ShowIpOspfDatabaseSummaryDetail(ShowIpOspfDatabaseSummaryDetailSchema, ShowIpOspfDatabaseDetailParser):

    ''' Parser for "show ip ospf database summary detail [vrf <WORD>]" '''

    def cli(self, vrf=''):
        # excute command to get output
        # Build command
        cmd = 'show ip ospf database summary detail'
        if vrf:
            cmd += ' vrf {}'.format(vrf)

        return super().cli(cmd=cmd, db_type='summary')


# =============================================================
# Schema for 'show ip ospf database router detail [vrf <WORD>]'
# =============================================================
class ShowIpOspfDatabaseRouterDetailSchema(MetaParser):

    ''' Schema for "show ip ospf database router detail [vrf <WORD>]" '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas': 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int},
                                                                'body': 
                                                                    {'router': 
                                                                        {Optional('flags'): str,
                                                                        'num_of_links': int,
                                                                        'links':
                                                                            {Any(): 
                                                                                {'link_id': str,
                                                                                'link_data': str,
                                                                                'type': str,
                                                                                'num_tos_metrics': int,
                                                                                'topologies': 
                                                                                    {Any(): 
                                                                                        {'mt_id': int,
                                                                                        Optional('metric'): int,
                                                                                        Optional('tos'): int},
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


# ==============================================================
# Parser for 'show ip ospf database router detail [vrf <WORD>]'
# ==============================================================
class ShowIpOspfDatabaseRouterDetail(ShowIpOspfDatabaseRouterDetailSchema, ShowIpOspfDatabaseDetailParser):

    ''' Parser for "show ip ospf database router detail [vrf <WORD>]" '''

    def cli(self, vrf=''):
        # excute command to get output
        # Build command
        cmd = 'show ip ospf database router detail'
        if vrf:
            cmd += ' vrf {}'.format(vrf)

        return super().cli(cmd=cmd, db_type='router')


# =============================================================
# Schema for 'show ip ospf database opqaue-area detail [vrf <WORD>]'
# =============================================================
class ShowIpOspfDatabaseOpaqueAreaDetailSchema(MetaParser):

    ''' Schema for "show ip ospf database opaque-area detail [vrf <WORD>]" '''

    schema = {
        'vrf': 
            {Any(): 
                {'address_family': 
                    {Any(): 
                        {'instance': 
                            {Any(): 
                                {'areas': 
                                    {Any(): 
                                        {'database': 
                                            {'lsa_types': 
                                                {Any(): 
                                                    {'lsa_type': int,
                                                    'lsas': 
                                                        {Any(): 
                                                            {'lsa_id': str,
                                                            'adv_router': str,
                                                            'ospfv2': 
                                                                {'header': 
                                                                    {'option': str,
                                                                    'option_desc': str,
                                                                    'lsa_id': str,
                                                                    'age': int,
                                                                    'type': int,
                                                                    'adv_router': str,
                                                                    'seq_num': str,
                                                                    'checksum': str,
                                                                    'length': int,
                                                                    'opaque_type': int,
                                                                    'opaque_id': int,
                                                                    Optional('fragment_number'): int,
                                                                    Optional('mpls_te_router_id'): str,
                                                                    Optional('num_links'): int},
                                                                'body': 
                                                                    {'opaque': 
                                                                        {Optional('link_tlvs'): 
                                                                            {Any(): 
                                                                                {'link_type': int,
                                                                                'link_name': str,
                                                                                'link_id': str,
                                                                                'te_metric': int,
                                                                                'max_bandwidth': int,
                                                                                'max_reservable_bandwidth': int,
                                                                                'admin_group': str,
                                                                                Optional('local_if_ipv4_addrs'): 
                                                                                    {Any(): {}},
                                                                                Optional('remote_if_ipv4_addrs'): 
                                                                                    {Any(): {}},
                                                                                Optional('unreserved_bandwidths'): 
                                                                                    {Any(): 
                                                                                        {'priority': int,
                                                                                        'unreserved_bandwidth': int},
                                                                                    },
                                                                                Optional('unknown_tlvs'): 
                                                                                    {Any(): 
                                                                                        {'type': int,
                                                                                        'length': int,
                                                                                        'value': str},
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


# ==================================================================
# Parser for 'show ip ospf database opaque-area detail [vrf <WORD>]'
# ==================================================================
class ShowIpOspfDatabaseOpaqueAreaDetail(ShowIpOspfDatabaseOpaqueAreaDetailSchema, ShowIpOspfDatabaseDetailParser):

    ''' Parser for "show ip ospf database opaque-area detail [vrf <WORD>]" '''

    def cli(self, vrf=''):
        # excute command to get output
        # Build command
        cmd = 'show ip ospf database opaque-area detail'
        if vrf:
            cmd += ' vrf {}'.format(vrf)

        return super().cli(cmd=cmd, db_type='opaque')
