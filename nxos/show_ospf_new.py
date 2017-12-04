''' show_ospf.py

NXOS parsers for the following show commands:

    * show ip ospf
    * show ip ospf vrf <WORD>
    * show ip ospf mpls ldp interface 
    * show ip ospf mpls ldp interface vrf <WORD>
    * show ip ospf sham-links
    * show ip ospf sham-links vrf <WORD>
    * show ip ospf virtual-links
    * show ip ospf virtual-links vrf <WORD>
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
                                                'bfd': bool,
                                                'enable': bool,
                                                'line_protocol': str,
                                                'ip_address': str,
                                                'state': str,
                                                'interface_type': str,
                                                'cost': int,
                                                'index': int,
                                                Optional('transmit_delay'): int,
                                                Optional('passive'): bool,
                                                Optional('priority'): int,
                                                Optional('dr_router_id'): str,
                                                Optional('dr_ip_addr'): str,
                                                Optional('bdr_router_id'): str,
                                                Optional('bdr_ip_addr'): str,
                                                Optional('total_neighbors'): int,
                                                Optional('num_nbrs_flooding'): int,
                                                Optional('num_nbrs_adjacent'): int,
                                                Optional('hello_interval'): int,
                                                Optional('dead_interval'): int,
                                                Optional('retransmit_interval'): int,
                                                Optional('wait_timer'): int,
                                                Optional('hello_timer'): str,
                                                Optional('opaque_lsa_links'): int,
                                                Optional('checksum'): int,
                                                Optional('authentication'): {
                                                    Optional('auth_trailer_key_chain'): {
                                                        Optional('key_chain'): str},
                                                    Optional('auth_trailer_key'): {
                                                        Optional('key'): str,
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
                if 'interfaces' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'] = {}
                if interface not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['interfaces']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'][interface] = {}
                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]\
                            ['interfaces'][interface]
                sub_dict['bfd'] = False

                # Set all other values
                try:
                    sub_dict['name'] = intf_name
                    sub_dict['enable'] = bool_dict[enable]
                    sub_dict['line_protocol'] = line_protocol
                    sub_dict['ip_address'] = ip_address
                except:
                    pass
                    continue

            # Enabled by interface configuration
            p4 = re.compile(r'^Enabled +by +interface +configuration$')
            m = p4.match(line)
            if m:
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
            p7_1 = re.compile(r'^Designated +Router +ID: (?P<router_id>(\S+)),'
                             ' +address: +(?P<ip_addr>(\S+))$')
            m = p7_1.match(line)
            if m:
                sub_dict['dr_router_id'] = str(m.groupdict()['router_id'])
                sub_dict['dr_ip_addr'] = str(m.groupdict()['ip_addr'])
                continue

            # Backup Designated Router ID: 2.2.2.2, address: 10.2.3.2
            p7_2 = re.compile(r'^Backup +Router +ID: (?P<router_id>(\S+)),'
                             ' +address: +(?P<ip_addr>(\S+))$')
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
                sub_dict['total_neighbors'] = int(m.groupdict()['num_neighbors'])
                sub_dict['num_nbrs_flooding'] = int(m.groupdict()['flooding'])
                sub_dict['num_nbrs_adjacent'] = int(m.groupdict()['adjacent'])
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
                sub_dict['wait_timer'] = int(m.groupdict()['wait'])
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
                              ' +(?P<opaque>(\d+)), +checksum +sum'
                              ' +(?P<checksum>(\d+))$')
            m = p12.match(line)
            if m:
                sub_dict['opaque_lsa_links'] = int(m.groupdict()['opaque'])
                sub_dict['checksum'] = int(m.groupdict()['checksum'])
                continue

            # BFD is enabled
            p13 = re.compile(r'^BFD +is +enabled$')
            m = p13.match(line)
            if m:
                sub_dict['bfd'] = True

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
                                                        'num_state_changes': int,
                                                        'last_state_change': str,
                                                        Optional('neighbor_priority'): int,
                                                        Optional('dr_ip_addr'): str,
                                                        Optional('bdr_ip_addr'): str,
                                                        'hello_options': str,
                                                        'dbd_options': str,
                                                        'last_non_hello_packet_received': str,
                                                        'dead_timer': str,
                                                        Optional('statistics'): {
                                                            Optional('nbr_event_count'): int,
                                                            Optional('nbr_retrans_qlen'): str,
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
                if 'interfaces' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'] = {}
                if interface not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['areas'][area]['interfaces']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'][interface] = {}
                if 'neighbors' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]\
                        ['interfaces'][interface]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'][interface]\
                        ['neighbors'] = {}
                if neighbor not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['areas'][area]\
                        ['interfaces'][interface]['neighbors']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['areas'][area]['interfaces'][interface]\
                        ['neighbors'][neighbor] = {}

                # Set sub_dict
                sub_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['areas'][area]['interfaces']\
                            [interface]['neighbors'][neighbor]

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
                sub_dict['num_state_changes'] = int(m.groupdict()['changes'])
                sub_dict['last_state_change'] = str(m.groupdict()['last'])
                continue

            # Neighbor priority is 1
            p4 = re.compile(r'^Neighbor +priority +is +(?P<priority>(\S+))$')
            m = p4.match(line)
            if m:
                sub_dict['neighbor_priority'] = int(m.groupdict()['priority'])
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

        assert db_type in ['external', 'network', 'summary', 'router', 'opaque-area']

        # Execute command on device
        out = self.device.execute(cmd)
        
        # Init vars
        ret_dict = {}
        af = 'ipv4'

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
            p2 = re.compile(r'^(?P<lsa_type>(.*)) +Link +States'
                             ' +\(Area +(?P<area>(\S+))\)$')
            m = p2.match(line)
            if m:
                lsa_type = str(m.groupdict()['lsa_type'])
                area = str(m.groupdict()['area'])
                continue

            # LS age: 1565
            p3 = re.compile(r'^LS +age: +(?P<lsa_id>(\d+))$')
            m = p3.match(line)
            if m:
                lsa_id = str(m.groupdict()['lsa_id'])
                continue

            # Options: 0x20 (No TOS-capability, DC)
            p4 = re.compile(r'^Options: +(?P<options>(.*))$')
            m = p4.match(line)
            if m:
                options = str(m.groupdict()['options'])
                continue

            # LS Type: Type-5 AS-External
            p5 = re.compile(r'^LS +Type: +(?P<lsa_type>(.*))$')
            m = p5.match(line)
            if m:
                lsa_type = str(m.groupdict()['lsa_type'])
                if 'database' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['database'] = {}
                if 'lsa_types' not in ret_dict['vrf'][vrf]['address_family']\
                        [af]['instance'][instance]['database']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['database']['lsa_types'] = {}
                if lsa_type not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['database']['lsa_types']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['database']['lsa_types'][lsa_type] = {}
                    continue

            # Link State ID: 1.1.1.1
            # Link State ID: 44.44.44.44 (Network address)
            # Link State ID: 10.1.2.1 (Designated Router address)
            p5 = re.compile(r'^Link +State +ID: +(?P<link_state_id>(\S+))'
                             '(?: +\(.*\))?$')
            m = p5.match(line)
            if m:
                link_state_id = str(m.groupdict()['link_state_id'])
                continue

            # Advertising Router: 4.4.4.4
            p6 = re.compile(r'^Advertising +Router: +(?P<adv_router>(\S+))$')
            m = p6.match(line)
            if m:
                adv_router = str(m.groupdict()['adv_router'])
                lsa = lsa_id + ' ' + adv_router
                if 'lsas' not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['database']['lsa_types']\
                        [lsa_type]:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['database']['lsa_types'][lsa_type]\
                        ['lsas'] = {}
                if lsa not in ret_dict['vrf'][vrf]['address_family'][af]\
                        ['instance'][instance]['database']['lsa_types']\
                        [lsa_type]['lsas']:
                    ret_dict['vrf'][vrf]['address_family'][af]['instance']\
                        [instance]['database']['lsa_types'][lsa_type]\
                        ['lsas'][lsa] = {}
                # Set sub_dict
                lsa_dict = ret_dict['vrf'][vrf]['address_family'][af]\
                            ['instance'][instance]['database']['lsa_types']\
                            [lsa_type]['lsas'][lsa]
                # Init dicts
                if 'ospfv2' not in lsa_dict:
                    lsa_dict['ospfv2'] = {}
                if 'body' not in lsa_dict['ospfv2']:
                    lsa_dict['ospfv2']['body'] = {}
                if db_type not in lsa_dict['ospfv2']['body']:
                    lsa_dict['ospfv2']['body'][db_type] = {}
                # Set db_dict
                db_dict = lsa_dict['ospfv2']['body'][db_type]
                try:
                    db_dict['options'] = options
                    db_dict['link_state_id'] = link_state_id
                    continue
                except:
                    pass

            # LS Seq Number: 0x80000002
            p7 = re.compile(r'^LS +Seq +Number: +(?P<ls_seq_num>(\S+))$')
            m = p7.match(line)
            if m:
                db_dict['ls_seq_num'] = str(m.groupdict()['ls_seq_num'])
                continue

            # Checksum: 0x7d61
            p8 = re.compile(r'^Checksum: +(?P<flags>(\S+))$')
            m = p8.match(line)
            if m:
                db_dict['flags'] = str(m.groupdict()['flags'])
                continue

            # Length: 36
            p9 = re.compile(r'^Length: +(?P<length>(\d+))$')
            m = p9.match(line)
            if m:
                db_dict['length'] = int(m.groupdict()['length'])
                continue

            # Network Mask: /32
            p10 = re.compile(r'^Network +Mask: +(?P<net_mask>(\S+))$')
            m = p10.match(line)
            if m:
                db_dict['network_mask'] = str(m.groupdict()['net_mask'])
                continue

            # Metric Type: 2 (Larger than any link state path)
            p11 = re.compile(r'^Metric +Type: +(?P<mt_id>(.*))$')
            m = p11.match(line)
            if m:
                db_dict['mt_id'] = str(m.groupdict()['mt_id'])
                continue

            # TOS: 0
            # TOS: 0 Metric: 1
            p12 = re.compile(r'^TOS:? +(?P<tos>(\d+))(?: +Metric:'
                              ' +(?P<metric>(\d+)))?$')
            m = p12.match(line)
            if m:
                tos = int(m.groupdict()['tos'])
                metric = m.groupdict()['metric']
                if db_type is 'router':
                    continue
                db_dict['tos'] = tos
                if m.groupdict()['metric']:
                    db_dict['metric'] = metric
                    continue

            # Metric: 20
            p13 = re.compile(r'^Metric: +(?P<metric>(\d+))$')
            m = p13.match(line)
            if m:
                db_dict['metric'] = str(m.groupdict()['metric'])
                continue

            # Forward Address: 0.0.0.0
            p14 = re.compile(r'^Forward +Address: +(?P<fwd_addr>(\S+))$')
            m = p14.match(line)
            if m:
                db_dict['forwarding_address'] = str(m.groupdict()['fwd_addr'])
                continue

            # External Route Tag: 0
            p15 = re.compile(r'^External +Route +Tag: +(?P<tag>(\S+))$')
            m = p15.match(line)
            if m:
                db_dict['external_route_tag'] = str(m.groupdict()['tag'])            
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
            p18 = re.compile(r'^Link +connected +to: +a +(?P<link>(.*))$')
            m = p18.match(line)
            if m:
                link = str(m.groupdict()['link']).lower()
                if 'links' not in db_dict:
                    db_dict['links'] = {}
                if link not in db_dict['links']:
                    db_dict['links'][link] = {}
                try:
                    db_dict['links'][link]['tos'] = tos
                    db_dict['links'][link]['metric'] = metric
                    continue
                except:
                    pass
            
            # (Link ID) Network/Subnet Number: 1.1.1.1
            # (Link ID) Designated Router address: 20.6.7.6
            p19 = re.compile(r'^\(Link +ID\) +Network\/Subnet +Number:'
                              ' +(?P<id>(\S+))$')
            m = p19.match(line)
            if m:
                db_dict['links'][link]['link_id'] = str(m.groupdict()['id'])

            # (Link Data) Network Mask: 255.255.255.255
            # (Link Data) Router Interface address: 20.6.7.6
            p20 = re.compile(r'^\(Link +Data\) +Network +Mask:'
                              ' +(?P<data>(\S+))$')
            m = p20.match(line)
            if m:
                db_dict['links'][link]['link_data'] = str(m.groupdict()['data'])

            # Number of TOS metrics: 0
            p21 = re.compile(r'^Number +of +TOS +metrics: +(?P<num>(\d+))$')
            m = p21.match(line)
            if m:
                db_dict['links'][link]['num_tos_metrics'] = \
                    int(m.groupdict()['num'])
                continue
        import pdb ; pdb.set_trace()
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
                                {'database': 
                                    {'lsa_types': 
                                        {Any(): 
                                            {'lsas': 
                                                {Any(): 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'external': 
                                                                {'network_mask': str,
                                                                'mt_id': str,
                                                                'flags': str,
                                                                'metric': str,
                                                                'forwarding_address': str,
                                                                'external_route_tag': str,
                                                                'options': str,
                                                                'link_state_id': str,
                                                                'length': int,
                                                                'tos': int,
                                                                'ls_seq_num': str,
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
                                {'database': 
                                    {'lsa_types': 
                                        {Any(): 
                                            {'lsas': 
                                                {Any(): 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'network': 
                                                                {'network_mask': str,
                                                                'attached_routers': 
                                                                    {Any(): {},
                                                                    },
                                                                'flags': str,
                                                                'options': str,
                                                                'link_state_id': str,
                                                                'length': int,
                                                                'ls_seq_num': str,
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
                                {'database': 
                                    {'lsa_types': 
                                        {Any(): 
                                            {'lsas': 
                                                {Any(): 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'summary': 
                                                                {'network_mask': str,
                                                                'metric': str,
                                                                Optional('mt_id'): str,
                                                                'tos': int,
                                                                'flags': str,
                                                                'options': str,
                                                                'link_state_id': str,
                                                                'length': int,
                                                                'ls_seq_num': str,
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
                                {'database': 
                                    {'lsa_types': 
                                        {Any(): 
                                            {'lsas': 
                                                {Any(): 
                                                    {'ospfv2': 
                                                        {'body': 
                                                            {'router': 
                                                                {'num_of_links': int,
                                                                'flags': str,
                                                                'options': str,
                                                                'link_state_id': str,
                                                                'length': int,
                                                                'ls_seq_num': str,
                                                                'links':
                                                                    {Any(): 
                                                                        {'link_id': str,
                                                                        'link_data': str,
                                                                        'num_tos_metrics': int,
                                                                        'metric': str,
                                                                        'tos': int,
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
