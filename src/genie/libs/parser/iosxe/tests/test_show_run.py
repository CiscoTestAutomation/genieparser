#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_run import ShowRunPolicyMap, ShowRunInterface


class TestShowRunPolicyMap(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "policy_map": {
            "L3VPN-0_in": {
                "class": {
                    "HEY_in": {
                        "police": {
                            "cir_bps": "365",
                            "pir_bps": "235",
                            "conformed": "transmit",
                            "exceeded": "drop"
                        }
                    },
                    "OSPF": {
                        "police": {
                            "cir_bps": "543",
                            "pir_bps": "876",
                            "conformed": "transmit",
                            "exceeded": "drop"
                        }
                    },
                    "class-default": {
                        "police": {
                            "cir_bps": "2565",
                            "cir_bc_bytes": "4234",
                            "conformed": "transmit",
                            "exceeded": "drop"
                        },
                        "service_policy": "child"
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        show run policy-map L3VPN-0_in
        Building configuration...

        Current configuration : 56 bytes
        !
        policy-map L3VPN-0_in
        class HEY_in
        police cir 365 pir 235 conform-action transmit  exceed-action drop
        class OSPF
        police cir 543 pir 876 conform-action transmit  exceed-action drop
        class class-default
        police cir 2565 bc 4234 conform-action transmit  exceed-action drop
        service-policy child
        !
        end
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowRunPolicyMap(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(name= 'L3VPN-0_in')

    def test_golden(self):
        self.device1 = Mock(**self.golden_output)
        obj = ShowRunPolicyMap(device=self.device1)
        parsed_output = obj.parse(name= 'L3VPN-0_in')
        self.assertEqual(parsed_output,self.golden_parsed_output)


class TestShowRunInterface(unittest.TestCase):

    maxDiff = None 
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet1/0/13': {
                'authentication_control_direction': 'in',
                'authentication_event_fail_action': 'next-method',
                'authentication_fallback': 'dot1x',
                'authentication_host_mode': 'multi-auth',
                'authentication_order': 'dot1x mab',
                'authentication_periodic': True,
                'authentication_port_control': 'auto',
                'authentication_priority': 'dot1x mab',
                'authentication_timer_inactivity': '65535',
                'authentication_timer_reauthenticate_server': True,
                'authentication_violation': 'restrict',
                'description': 'ISE Controlled Port',
                'dot1x_pae_authenticator': True,
                'dot1x_timeout_quiet_period': '5',
                'dot1x_timeout_server_timeout': '10',
                'dot1x_timeout_tx_period': '5',
                'ip_arp_inspection_limit_rate': '1024',
                'ip_dhcp_snooping_limit_rate': '100',
                'load_interval': '30',
                'mab': True,
                'snmp_trap_link_status': False,
                'snmp_trap_mac_notification_change_added': True,
                'snmp_trap_mac_notification_change_removed': True,
                'spanning_tree_bpduguard': 'enable',
                'spanning_tree_portfast': True,
                'switchport_access_vlan': '70',
                'switchport_mode': 'access',
                'switchport_nonegotiate': 'nonegotiate',
            },
        },
    }
    golden_output = {'execute.return_value': '''\
        #show running-config interface Gi1/0/13
 
        Building configuration...
        
        
        
        Current configuration : 914 bytes
        
        !
        
        interface GigabitEthernet1/0/13
         description ISE Controlled Port
         switchport access vlan 70
         switchport mode access
         switchport nonegotiate
         ip arp inspection limit rate 1024
         load-interval 30
         authentication control-direction in
         authentication event fail action next-method
         authentication host-mode multi-auth
         authentication order dot1x mab
         authentication priority dot1x mab
         authentication port-control auto
         authentication periodic
         authentication timer reauthenticate server
         authentication timer inactivity 65535
         authentication violation restrict
         authentication fallback dot1x
         mab
         snmp trap mac-notification change added
         snmp trap mac-notification change removed
         no snmp trap link-status
         dot1x pae authenticator
         dot1x timeout quiet-period 5
         dot1x timeout server-timeout 10
         dot1x timeout tx-period 5
         spanning-tree portfast
         spanning-tree bpduguard enable
         ip dhcp snooping limit rate 100
        end
    '''}

    golden_parsed_output1 = {
        'interfaces': {
            'GigabitEthernet0': {
                'description': '"Boot lan interface"',
                'ipv4': {
                    'ip': '10.1.21.249',
                    'netmask': '255.255.255.0',
                },
                'negotiation_auto': True,
                'vrf': 'Mgmt-intf',
            },
        },
    }
    golden_output1 = {'execute.return_value': '''\
        #show running-config interface GigabitEthernet0
        Building configuration...

        Current configuration : 150 bytes
        !
        interface GigabitEthernet0
         description "Boot lan interface"
         vrf forwarding Mgmt-intf
         ip address 10.1.21.249 255.255.255.0
         negotiation auto
        end
    '''}

    golden_parsed_output2 = {
        'interfaces': {
            'Port-channel1.100': {
                'encapsulation_dot1q': '201',
                'ipv4': {
                    'ip': '202.0.0.1',
                    'netmask': '255.255.255.0',
                },
                'ipv6': ['2002::1/112'],
                'ipv6_ospf': {
                    '1': {
                        'area': '0',
                    },
                },
            },
        },
    }
    golden_output2 = {'execute.return_value': '''\
        interface Port-channel1.100
         encapsulation dot1Q 201
         ip address 202.0.0.1 255.255.255.0
         ipv6 address 2002::1/112
         ipv6 ospf 1 area 0
        end
    '''}

    golden_parsed_output3 = {
        'interfaces': {
            'GigabitEthernet0/0/3': {
                'ip_ospf': {
                    '2': {
                        'area': '0',
                    },
                },
                'ipv4': {
                    'ip': '99.99.110.1',
                    'netmask': '255.255.255.0',
                },
                'ipv6': ['2003::1/112'],
                'ipv6_ospf': {
                    '1': {
                        'area': '0',
                    },
                },
                'negotiation_auto': True,
            },
        },
    }
    golden_output3 = {'execute.return_value': '''\
        interface GigabitEthernet0/0/3
         ip address 99.99.110.1 255.255.255.0
         ip ospf 2 area 0
         negotiation auto
         ipv6 address 2003::1/112
         ipv6 ospf 1 area 0
        end
    '''}

    golden_parsed_output4 = {
        'interfaces': {
            'GigabitEthernet0/0/0.101': {
                'encapsulation_dot1q': '101',
                'ipv4': {
                    'ip': '201.0.0.1',
                    'netmask': '255.255.255.0',
                },
                'ipv6': ['2001::1/112'],
                'ipv6_enable': True,
                'ipv6_ospfv3': {
                    '1': {
                        'area': '0',
                    },
                },
                'vrf': 'VRF1',
            },
        },
    }
    golden_output4 = {'execute.return_value': '''\
        interface GigabitEthernet0/0/0.101
         encapsulation dot1Q 101
         vrf forwarding VRF1
         ip address 201.0.0.1 255.255.255.0
         ipv6 address 2001::1/112
         ipv6 enable
         ospfv3 1 ipv6 area 0
        end
    '''}

    golden_parsed_output5 = {
        'interfaces': {
            'Loopback1': {
                'ipv4': {
                    'ip': '200.1.0.2',
                    'netmask': '255.255.255.0',
                },
                'ipv6': ['1:1:1::1/64', '2000:1::2/112'],
                'vrf': 'VRF1',
            },
        },
    }
    golden_output5 = {'execute.return_value': '''\
        interface Loopback1
         vrf forwarding VRF1
         ip address 200.1.0.2 255.255.255.0
         ipv6 address 1:1:1::1/64
         ipv6 address 2000:1::2/112
        end
    '''}

    golden_parsed_output6 = {
        'interfaces': {
            'GigabitEthernet0/0/0': {
                'carrier_delay': ['up 60', 'down 60'],
                'ipv6': ['1::1/112'],
                'negotiation_auto': True,
            },
        },
    }
    golden_output6 = {'execute.return_value': '''\
        interface GigabitEthernet0/0/0
         no ip address
         carrier-delay up 60
         carrier-delay down 60
         negotiation auto
         ipv6 address 1::1/112
        end
    '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowRunInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(interface='GigabitEthernet0/0/0')

    def test_golden(self):
        self.device1 = Mock(**self.golden_output)
        obj = ShowRunInterface(device=self.device1)
        parsed_output = obj.parse(interface='Gi1/0/13')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden1(self):
        self.device1 = Mock(**self.golden_output1)
        obj = ShowRunInterface(device=self.device1)
        parsed_output = obj.parse(interface='GigabitEthernet0')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_golden2(self):
        self.device1 = Mock(**self.golden_output2)
        obj = ShowRunInterface(device=self.device1)
        parsed_output = obj.parse(interface='Port-channel1.100')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_golden3(self):
        self.device1 = Mock(**self.golden_output3)
        obj = ShowRunInterface(device=self.device1)
        parsed_output = obj.parse(interface='GigabitEthernet0/0/3')
        self.assertEqual(parsed_output,self.golden_parsed_output3)

    def test_golden4(self):
        self.device1 = Mock(**self.golden_output4)
        obj = ShowRunInterface(device=self.device1)
        parsed_output = obj.parse(interface='GigabitEthernet0/0/0.101')
        self.assertEqual(parsed_output,self.golden_parsed_output4)

    def test_golden5(self):
        self.device1 = Mock(**self.golden_output5)
        obj = ShowRunInterface(device=self.device1)
        parsed_output = obj.parse(interface='Loopback1')
        self.assertEqual(parsed_output,self.golden_parsed_output5)

    def test_golden6(self):
        self.device1 = Mock(**self.golden_output6)
        obj = ShowRunInterface(device=self.device1)
        parsed_output = obj.parse(interface='GigabitEthernet0/0/0')
        self.assertEqual(parsed_output,self.golden_parsed_output6)


if __name__ == '__main__':
    unittest.main()