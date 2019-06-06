import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.asa.show_interface import ShowInterfaceSummary, \
												 ShowInterfaceIpBrief, \
												 ShowInterfaceDetail

# =============================================
# Parser for 'show interface summary'
# =============================================
class test_show_interface_summary(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'Vlan1000': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod100',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.100.251',
                'subnet': '255.255.255.0'
            }
        }
    }

    golden_output = {'execute.return_value': '''
		Interface Vlan1000 "pod100", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.100.251, subnet mask 255.255.255.0
	'''}

    golden_parsed_output_2 = {
        'interfaces': {
            'Vlan300': {
                'interface_state': True,
                'config_status': True,
                'name': 'devadmin-out',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '10.10.10.4',
                'subnet': '255.255.255.0',

            },
            'Vlan400': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod100-in',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '10.110.10.230',
                'subnet': '255.255.255.0'
            },
            'Vlan700': {
                'interface_state': True,
                'config_status': False,
                'config_issue': 'nameif',
                'name': '',
                'oper_status': 'up',
                'protocol_status': 'up',
            },
            'Vlan900': {
                'interface_state': True,
                'config_status': True,
                'name': 'adminNAT',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.0.4',
                'subnet': '255.255.255.0'
            },
            'Vlan901': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod1',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.1.251',
                'subnet': '255.255.255.0'
            },
            'Vlan902': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod2',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.2.251',
                'subnet': '255.255.255.0'
            },
            'Vlan903': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod3',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.3.251',
                'subnet': '255.255.255.0'
            },
            'Vlan904': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod4',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.4.251',
                'subnet': '255.255.255.0'
            },
            'Vlan905': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod5',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.5.251',
                'subnet': '255.255.255.0'
            },
            'Vlan906': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod6',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.6.251',
                'subnet': '255.255.255.0'
            },
            'Vlan907': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod7',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.7.251',
                'subnet': '255.255.255.0'
            },
            'Vlan908': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod8',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.8.251',
                'subnet': '255.255.255.0'
            },
            'Vlan909': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod9',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.9.251',
                'subnet': '255.255.255.0'
            },
            'Vlan1178': {
                'interface_state': False,
                'config_status': True,
                'name': 'pod249',
                'oper_status': 'down',
                'protocol_status': 'down',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.249.251',
                'subnet': '255.255.255.0'
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
		Interface Vlan300 "devadmin-out", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 10.10.10.4, subnet mask 255.255.255.0
		Interface Vlan400 "pod100-in", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 10.110.10.230, subnet mask 255.255.255.0
		Interface Vlan700 "", is up, line protocol is up
			Available but not configured via nameif
		Interface Vlan900 "adminNAT", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.0.4, subnet mask 255.255.255.0
		Interface Vlan901 "pod1", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.1.251, subnet mask 255.255.255.0
		Interface Vlan902 "pod2", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.2.251, subnet mask 255.255.255.0
		Interface Vlan903 "pod3", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.3.251, subnet mask 255.255.255.0
		Interface Vlan904 "pod4", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.4.251, subnet mask 255.255.255.0
		Interface Vlan905 "pod5", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.5.251, subnet mask 255.255.255.0
		Interface Vlan906 "pod6", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.6.251, subnet mask 255.255.255.0
		Interface Vlan907 "pod7", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.7.251, subnet mask 255.255.255.0
		Interface Vlan908 "pod8", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.8.251, subnet mask 255.255.255.0
		Interface Vlan909 "pod9", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.9.251, subnet mask 255.255.255.0
		Interface Vlan1178 "pod249", is down, line protocol is down
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.249.251, subnet mask 255.255.255.0
	'''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfaceSummary(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfaceSummary(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        interface_obj = ShowInterfaceSummary(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

# =============================================
# Parser for 'show interface ip brief'
# =============================================
class test_show_interface_ip_brief(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'Vlan1000': {
                'ip_address': '172.16.100.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            }
        }
    }

    golden_output = {'execute.return_value': '''
		Vlan1000  172.16.100.251  YES CONFIG up up
	'''}

    golden_parsed_output_2 = {
        'interfaces': {
            'Vlan1160': {
                'ip_address': '172.16.232.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1161': {
                'ip_address': '172.16.233.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1162': {
                'ip_address': '10.10.2.4',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1163': {
                'ip_address': '172.16.234.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1164': {
                'ip_address': '172.16.235.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1165': {
                'ip_address': '172.16.236.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1166': {
                'ip_address': '172.16.237.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1167': {
                'ip_address': '172.16.238.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1168': {
                'ip_address': '172.16.239.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1169': {
                'ip_address': '172.16.240.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1170': {
                'ip_address': '172.16.241.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1171': {
                'ip_address': '172.16.242.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1172': {
                'ip_address': '172.16.243.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1173': {
                'ip_address': '172.16.244.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1174': {
                'ip_address': '172.16.245.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1175': {
                'ip_address': '172.16.246.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1176': {
                'ip_address': '172.16.247.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1177': {
                'ip_address': '172.16.248.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan1178': {
                'ip_address': '172.16.249.251',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'down',
                'protocol_status': 'down'
            },
            'Vlan300': {
                'ip_address': '10.10.10.4',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan400': {
                'ip_address': '10.110.10.230',
                'check': 'YES',
                'method': 'CONFIG',
                'oper_status': 'up',
                'protocol_status': 'up'
            },
            'Vlan700': {
                'ip_address': 'unassigned',
                'check': 'YES',
                'method': 'unset',
                'oper_status': 'up',
                'protocol_status': 'up'
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
		Vlan1160                   172.16.232.251  YES CONFIG up                    up
		Vlan1161                   172.16.233.251  YES CONFIG up                    up
		Vlan1162                   10.10.2.4       YES CONFIG up                    up
		Vlan1163                   172.16.234.251  YES CONFIG up                    up
		Vlan1164                   172.16.235.251  YES CONFIG up                    up
		Vlan1165                   172.16.236.251  YES CONFIG up                    up
		Vlan1166                   172.16.237.251  YES CONFIG up                    up
		Vlan1167                   172.16.238.251  YES CONFIG up                    up
		Vlan1168                   172.16.239.251  YES CONFIG up                    up
		Vlan1169                   172.16.240.251  YES CONFIG up                    up
		Vlan1170                   172.16.241.251  YES CONFIG up                    up
		Vlan1171                   172.16.242.251  YES CONFIG up                    up
		Vlan1172                   172.16.243.251  YES CONFIG up                    up
		Vlan1173                   172.16.244.251  YES CONFIG up                    up
		Vlan1174                   172.16.245.251  YES CONFIG up                    up
		Vlan1175                   172.16.246.251  YES CONFIG up                    up
		Vlan1176                   172.16.247.251  YES CONFIG up                    up
		Vlan1177                   172.16.248.251  YES CONFIG up                    up
		Vlan1178                   172.16.249.251  YES CONFIG down                  down
		Vlan300                    10.10.10.4      YES CONFIG up                    up
		Vlan400                    10.110.10.230   YES CONFIG up                    up
		Vlan700                    unassigned      YES unset  up                    up
	'''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfaceIpBrief(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfaceIpBrief(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        interface_obj = ShowInterfaceIpBrief(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

# =============================================
# Parser for 'show interface detail'
# =============================================
class test_show_interface_detail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'Vlan1177': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod248',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.248.251',
                'subnet': '255.255.255.0',
                'traffic_input_packets': 16863445,
                'traffic_input_bytes': 10312133394,
                'traffic_output_packets': 10475426,
                'traffic_output_bytes': 5376026271,
                'traffic_dropped_packets': 2551519,
                'interface_number': 756,
                'vlan_config': True,
                'vlan_state': 'UP'
            }
        }
    }

    golden_output = {'execute.return_value': '''
		Interface Vlan1177 "pod248", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.248.251, subnet mask 255.255.255.0
		  Traffic Statistics for "pod248":
			16863445 packets input, 10312133394 bytes
			10475426 packets output, 5376026271 bytes
			2551519 packets dropped
		  Control Point Interface States:
			Interface number is 756
			Interface config status is active
			Interface state is active
		  Control Point Vlan1177 States:
			Interface vlan config status is active
			Interface vlan state is UP
	'''}

    golden_parsed_output_2 = {
        'interfaces': {
            'Vlan1178': {
                'interface_state': False,
                'config_status': True,
                'name': 'pod249',
                'oper_status': 'down',
                'protocol_status': 'down',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.249.251',
                'subnet': '255.255.255.0',
                'traffic_input_packets': 0,
                'traffic_input_bytes': 0,
                'traffic_output_packets': 0,
                'traffic_output_bytes': 0,
                'traffic_dropped_packets': 0,
                'interface_number': 757,
                'vlan_config': False,
                'vlan_state': 'DOWN'
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
		Interface Vlan1178 "pod249", is down, line protocol is down
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.249.251, subnet mask 255.255.255.0
		  Traffic Statistics for "pod249":
			0 packets input, 0 bytes
			0 packets output, 0 bytes
			0 packets dropped
		  Control Point Interface States:
			Interface number is 757
			Interface config status is active
			Interface state is not active
		  Control Point Vlan1178 States:
			Interface vlan config status is not active
			Interface vlan state is DOWN (down in system space)
	'''}

    golden_parsed_output_3 = {
        'interfaces': {
            'Vlan300': {
                'interface_state': True,
                'config_status': True,
                'name': 'devadmin-out',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '10.10.10.4',
                'subnet': '255.255.255.0',
                'traffic_input_packets': 889007666,
                'traffic_input_bytes': 785740327549,
                'traffic_output_packets': 621453837,
                'traffic_output_bytes': 428046938178,
                'traffic_dropped_packets': 2988535,
                'interface_number': 5,
                'vlan_config': True,
                'vlan_state': 'UP'
            },
            'Vlan400': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod100-in',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '10.110.10.230',
                'subnet': '255.255.255.0',
                'traffic_input_packets': 1286035,
                'traffic_input_bytes': 100030768,
                'traffic_output_packets': 1,
                'traffic_output_bytes': 28,
                'traffic_dropped_packets': 1285569,
                'interface_number': 105,
                'vlan_config': True,
                'vlan_state': 'UP'
            },
            'Vlan700': {
                'interface_state': True,
                'config_status': False,
                'name': '',
                'oper_status': 'up',
                'protocol_status': 'up',
                'config_issue': 'nameif'
            },
            'Vlan900': {
                'interface_state': True,
                'config_status': True,
                'name': 'adminNAT',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.0.4',
                'subnet': '255.255.255.0',
                'traffic_input_packets': 1212307,
                'traffic_input_bytes': 96880666,
                'traffic_output_packets': 1,
                'traffic_output_bytes': 28,
                'traffic_dropped_packets': 1212268,
                'interface_number': 507,
                'vlan_config': True,
                'vlan_state': 'UP'
            },
            'Vlan901': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod1',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.1.251',
                'subnet': '255.255.255.0',
                'traffic_input_packets': 7299914,
                'traffic_input_bytes': 6411442725,
                'traffic_output_packets': 2862092,
                'traffic_output_bytes': 118819269,
                'traffic_dropped_packets': 1288374,
                'interface_number': 508,
                'vlan_config': True,
                'vlan_state': 'UP'
            },
             'Vlan1178': {
                'interface_state': False,
                'config_status': True,
                'name': 'pod249',
                'oper_status': 'down',
                'protocol_status': 'down',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.249.251',
                'subnet': '255.255.255.0',
                'traffic_input_packets': 0,
                'traffic_input_bytes': 0,
                'traffic_output_packets': 0,
                'traffic_output_bytes': 0,
                'traffic_dropped_packets': 0,
                'interface_number': 757,
                'vlan_config': False,
                'vlan_state': 'DOWN'
            }
        }
    }

    golden_output_3 = {'execute.return_value': '''
		Interface Vlan300 "devadmin-out", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 10.10.10.4, subnet mask 255.255.255.0
		  Traffic Statistics for "devadmin-out":
			889007666 packets input, 785740327549 bytes
			621453837 packets output, 428046938178 bytes
			2988535 packets dropped
		  Control Point Interface States:
			Interface number is 5
			Interface config status is active
			Interface state is active
		  Control Point Vlan300 States:
			Interface vlan config status is active
			Interface vlan state is UP
		Interface Vlan400 "pod100-in", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 10.110.10.230, subnet mask 255.255.255.0
		  Traffic Statistics for "pod100-in":
			1286035 packets input, 100030768 bytes
			1 packets output, 28 bytes
			1285569 packets dropped
		  Control Point Interface States:
			Interface number is 105
			Interface config status is active
			Interface state is active
		  Control Point Vlan400 States:
			Interface vlan config status is active
			Interface vlan state is UP
		Interface Vlan700 "", is up, line protocol is up
			Available but not configured via nameif
		Interface Vlan900 "adminNAT", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.0.4, subnet mask 255.255.255.0
		  Traffic Statistics for "adminNAT":
			1212307 packets input, 96880666 bytes
			1 packets output, 28 bytes
			1212268 packets dropped
		  Control Point Interface States:
			Interface number is 507
			Interface config status is active
			Interface state is active
		  Control Point Vlan900 States:
			Interface vlan config status is active
			Interface vlan state is UP
		Interface Vlan901 "pod1", is up, line protocol is up
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.1.251, subnet mask 255.255.255.0
		  Traffic Statistics for "pod1":
			7299914 packets input, 6411442725 bytes
			2862092 packets output, 118819269 bytes
			1288374 packets dropped
		  Control Point Interface States:
			Interface number is 508
			Interface config status is active
			Interface state is active
		  Control Point Vlan901 States:
			Interface vlan config status is active
			Interface vlan state is UP
		Interface Vlan1178 "pod249", is down, line protocol is down
			MAC address 286f.7fb1.032c, MTU 1500
			IP address 172.16.249.251, subnet mask 255.255.255.0
		  Traffic Statistics for "pod249":
			0 packets input, 0 bytes
			0 packets output, 0 bytes
			0 packets dropped
		  Control Point Interface States:
			Interface number is 757
			Interface config status is active
			Interface state is not active
		  Control Point Vlan1178 States:
			Interface vlan config status is not active
			Interface vlan state is DOWN (down in system space)
	'''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfaceDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfaceDetail(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        interface_obj = ShowInterfaceDetail(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        interface_obj = ShowInterfaceDetail(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

if __name__ == '__main__':
    unittest.main()