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
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '172.16.100.251': { 
                        'ip': '172.16.100.251'
                    },
                },
                'subnet': '255.255.255.0'
            }
        }
    }

    golden_output = {'execute.return_value': '''
		DevNet-asa-sm-1/admin# show interface summary
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
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '10.10.10.4': { 
                        'ip': '10.10.10.4'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan400': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod100-in',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '10.110.10.230': { 
                        'ip': '10.110.10.230'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan700': {
                'interface_state': True,
                'config_status': False,
                'config_issue': 'nameif',
                'name': '',
                'link_status': 'up',
                'line_protocol': 'up',
            },
            'Vlan900': {
                'interface_state': True,
                'config_status': True,
                'name': 'adminNAT',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '172.16.0.4': { 
                        'ip': '172.16.0.4'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan901': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod1',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '172.16.1.251': { 
                        'ip': '172.16.1.251'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan902': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod2',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '172.16.2.251': { 
                        'ip': '172.16.2.251'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan903': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod3',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '172.16.3.251': { 
                        'ip': '172.16.3.251'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan904': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod4',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '172.16.4.251': { 
                        'ip': '172.16.4.251'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan905': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod5',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '172.16.5.251': { 
                        'ip': '172.16.5.251'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan906': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod6',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '172.16.6.251': { 
                        'ip': '172.16.6.251'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan907': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod7',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '172.16.7.251': { 
                        'ip': '172.16.7.251'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan908': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod8',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '172.16.8.251': { 
                        'ip': '172.16.8.251'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan909': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod9',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '172.16.9.251': { 
                        'ip': '172.16.9.251'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan1178': {
                'interface_state': False,
                'config_status': True,
                'name': 'pod249',
                'link_status': 'down',
                'line_protocol': 'down',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
				'ipv4': {
                    '172.16.249.251': { 
                        'ip': '172.16.249.251'
                    },
                },
                'subnet': '255.255.255.0'
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
    	DevNet-asa-sm-1/admin# show interface summary
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
				'ipv4': {
                    '172.16.100.251': { 
                        'ip': '172.16.100.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            }
        }
    }

    golden_output = {'execute.return_value': '''
		DevNet-asa-sm-1/admin# show interface ip brief
		Interface                  IP-Address      OK? Method Status                Protocol
		Vlan1000                   172.16.100.251  YES CONFIG up                    up
	'''}

    golden_parsed_output_2 = {
        'interfaces': {
            'Vlan1160': {
				'ipv4': {
                    '172.16.232.251': { 
                        'ip': '172.16.232.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1161': {
				'ipv4': {
                    '172.16.233.251': { 
                        'ip': '172.16.233.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1162': {
				'ipv4': {
                    '10.10.2.4': { 
                        'ip': '10.10.2.4'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1163': {
				'ipv4': {
                    '172.16.234.251': { 
                        'ip': '172.16.234.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1164': {
				'ipv4': {
                    '172.16.235.251': { 
                        'ip': '172.16.235.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1165': {
				'ipv4': {
                    '172.16.236.251': { 
                        'ip': '172.16.236.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1166': {
				'ipv4': {
                    '172.16.237.251': { 
                        'ip': '172.16.237.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1167': {
				'ipv4': {
                    '172.16.238.251': { 
                        'ip': '172.16.238.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1168': {
				'ipv4': {
                    '172.16.239.251': { 
                        'ip': '172.16.239.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1169': {
				'ipv4': {
                    '172.16.240.251': { 
                        'ip': '172.16.240.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1170': {
				'ipv4': {
                    '172.16.241.251': { 
                        'ip': '172.16.241.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1171': {
				'ipv4': {
                    '172.16.242.251': { 
                        'ip': '172.16.242.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1172': {
				'ipv4': {
                    '172.16.243.251': { 
                        'ip': '172.16.243.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1173': {
				'ipv4': {
                    '172.16.244.251': { 
                        'ip': '172.16.244.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1174': {
				'ipv4': {
                    '172.16.245.251': { 
                        'ip': '172.16.245.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1175': {
				'ipv4': {
                    '172.16.246.251': { 
                        'ip': '172.16.246.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1176': {
				'ipv4': {
                    '172.16.247.251': { 
                        'ip': '172.16.247.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1177': {
				'ipv4': {
                    '172.16.248.251': { 
                        'ip': '172.16.248.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan1178': {
				'ipv4': {
                    '172.16.249.251': { 
                        'ip': '172.16.249.251'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'down',
                'line_protocol': 'down'
            },
            'Vlan300': {
				'ipv4': {
                    '10.10.10.4': { 
                        'ip': '10.10.10.4'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan400': {
				'ipv4': {
                    '10.110.10.230': { 
                        'ip': '10.110.10.230'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan700': {
				'ipv4': {
                    'unnumbered': { 
                        'unnumbered_intf_ref': 'unassigned'
                    },
                },
                'check': 'YES',
                'method': 'unset',
                'link_status': 'up',
                'line_protocol': 'up'
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
    	DevNet-asa-sm-1/admin# show interface ip brief
		Interface                  IP-Address      OK? Method Status                Protocol
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
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ipv4': {
                    '172.16.248.251': { 
                        'ip': '172.16.248.251'
                    },
                },
                'subnet': '255.255.255.0',
                'traffic_statistics': {
                    'packets_input': 16863445,
                    'bytes_input': 10312133394,
                    'packets_output': 10475426,
                    'bytes_output': 5376026271,
                    'packets_dropped': 2551519
                },
                'control_point_states': {
                    'interface': {
                        'interface_number': 756,
                        'interface_config_status': 'active',
                        'interface_state': 'active'
                    },
                    'Vlan1177':{
                        'interface_vlan_config_status': 'active',
                        'interface_vlan_state': 'UP'
                    },
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
    	DevNet-asa-sm-1/admin# show interface detail
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
                'link_status': 'down',
                'line_protocol': 'down',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ipv4': {
                    '172.16.249.251': { 
                        'ip': '172.16.249.251'
                    },
                },
                'subnet': '255.255.255.0',
                'traffic_statistics': {
                    'packets_input': 0,
                    'bytes_input': 0,
                    'packets_output': 0,
                    'bytes_output': 0,
                    'packets_dropped': 0
                },
                'control_point_states': {
                    'interface': {
                        'interface_number': 757,
                        'interface_config_status': 'active',
                        'interface_state': 'not active'
                    },
                    'Vlan1178':{
                        'interface_vlan_config_status': 'not active',
                        'interface_vlan_state': 'DOWN'
                    },
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
    	DevNet-asa-sm-1/admin# show interface detail
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
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ipv4': {
                    '10.10.10.4': { 
                        'ip': '10.10.10.4'
                    },
                },
                'subnet': '255.255.255.0',
                'traffic_statistics': {
	                'packets_input': 889007666,
	                'bytes_input': 785740327549,
	                'packets_output': 621453837,
	                'bytes_output': 428046938178,
	                'packets_dropped': 2988535
                },
                'control_point_states': {
                    'interface': {
                        'interface_number': 5,
                        'interface_config_status': 'active',
                        'interface_state': 'active'
                    },
                    'Vlan300':{
                        'interface_vlan_config_status': 'active',
                        'interface_vlan_state': 'UP'
                    },
                }
            },
            'Vlan400': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod100-in',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ipv4': {
                    '10.110.10.230': { 
                        'ip': '10.110.10.230'
                    },
                },
                'subnet': '255.255.255.0',
                'traffic_statistics': {
	                'packets_input': 1286035,
	                'bytes_input': 100030768,
	                'packets_output': 1,
	                'bytes_output': 28,
	                'packets_dropped': 1285569
                },
                'control_point_states': {
                    'interface': {
                        'interface_number': 105,
                        'interface_config_status': 'active',
                        'interface_state': 'active'
                    },
                    'Vlan400':{
                        'interface_vlan_config_status': 'active',
                        'interface_vlan_state': 'UP'
                    },
                }
            },
            'Vlan700': {
                'interface_state': True,
                'config_status': False,
                'name': '',
                'link_status': 'up',
                'line_protocol': 'up',
                'config_issue': 'nameif'
            },
            'Vlan900': {
                'interface_state': True,
                'config_status': True,
                'name': 'adminNAT',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ipv4': {
                    '172.16.0.4': { 
                        'ip': '172.16.0.4'
                    },
                },
                'subnet': '255.255.255.0',
                'traffic_statistics': {
	                'packets_input': 1212307,
	                'bytes_input': 96880666,
	                'packets_output': 1,
	                'bytes_output': 28,
	                'packets_dropped': 1212268
                },
                'control_point_states': {
                    'interface': {
                        'interface_number': 507,
                        'interface_config_status': 'active',
                        'interface_state': 'active'
                    },
                    'Vlan900':{
                        'interface_vlan_config_status': 'active',
                        'interface_vlan_state': 'UP'
                    },
                }
            },
            'Vlan901': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod1',
                'link_status': 'up',
                'line_protocol': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ipv4': {
                    '172.16.1.251': { 
                        'ip': '172.16.1.251'
                    },
                },
                'subnet': '255.255.255.0',
                'traffic_statistics': {
	                'packets_input': 7299914,
	                'bytes_input': 6411442725,
	                'packets_output': 2862092,
	                'bytes_output': 118819269,
	                'packets_dropped': 1288374
                },
                'control_point_states': {
                    'interface': {
                        'interface_number': 508,
                        'interface_config_status': 'active',
                        'interface_state': 'active'
                    },
                    'Vlan901':{
                        'interface_vlan_config_status': 'active',
                        'interface_vlan_state': 'UP'
                    },
                }
            },
            'Vlan1178': {
                'interface_state': False,
                'config_status': True,
                'name': 'pod249',
                'link_status': 'down',
                'line_protocol': 'down',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ipv4': {
                    '172.16.249.251': { 
                        'ip': '172.16.249.251'
                    },
                },
                'subnet': '255.255.255.0',
                'traffic_statistics': {
	                'packets_input': 0,
	                'bytes_input': 0,
	                'packets_output': 0,
	                'bytes_output': 0,
	                'packets_dropped': 0
                },
                'control_point_states': {
                    'interface': {
                        'interface_number': 757,
                        'interface_config_status': 'active',
                        'interface_state': 'not active'
                    },
                    'Vlan1178':{
		                'interface_vlan_config_status': 'not active',
		                'interface_vlan_state': 'DOWN'
                    },
                }
            }
        }
    }

    golden_output_3 = {'execute.return_value': '''
    	DevNet-asa-sm-1/admin# show interface detail
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