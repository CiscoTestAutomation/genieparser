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
            'Vlan100': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod10',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            }
        }
    }

    golden_output = {'execute.return_value': '''
		ciscoasa/admin# show interface summary
		Interface Vlan100 "pod10", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
	'''}

    golden_parsed_output_2 = {
        'interfaces': {
        	'Vlan300': {
                'interface_state': True,
                'config_status': True,
                'name': 'admin-out',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan400': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod10-in',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan500': {
                'interface_state': True,
                'config_status': False,
                'config_issue': 'nameif',
                'name': '',
                'link_status': True,
                'line_protocol': True,
            },
            'Vlan600': {
                'interface_state': True,
                'config_status': True,
                'name': 'adminTEST',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan700': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod1',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan902': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod2',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan900': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod3',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan1000': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod4',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan1100': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod5',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan1200': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod6',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan1300': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod7',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan1400': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod8',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan1500': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod9',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            },
            'Vlan1600': {
                'interface_state': False,
                'config_status': True,
                'name': 'pod249',
                'link_status': False,
                'line_protocol': False,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0'
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
    	ciscoasa/admin# show interface summary
		Interface Vlan300 "admin-out", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		Interface Vlan400 "pod10-in", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		Interface Vlan500 "", is up, line protocol is up
			Available but not configured via nameif
		Interface Vlan600 "adminTEST", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		Interface Vlan700 "pod1", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		Interface Vlan902 "pod2", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		Interface Vlan900 "pod3", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		Interface Vlan1000 "pod4", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		Interface Vlan1100 "pod5", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		Interface Vlan1200 "pod6", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		Interface Vlan1300 "pod7", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		Interface Vlan1400 "pod8", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		Interface Vlan1500 "pod9", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		Interface Vlan1600 "pod249", is down, line protocol is down
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
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
            'Control0/0': {
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'GigabitEthernet0/0': {
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'GigabitEthernet0/1': {
				'ipv4': {
                    'unnumbered': { 
                        'unnumbered_intf_ref': 'unassigned'
                    },
                },
                'check': 'YES',
                'method': 'unset admin',
                'link_status': 'down',
                'line_protocol': 'down'
            },
            'GigabitEthernet0/2': {
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'check': 'YES',
                'method': 'manual admin',
                'link_status': 'down',
                'line_protocol': 'down'
            },
            'GigabitEthernet0/3': {
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'check': 'YES',
                'method': 'DHCP admin',
                'link_status': 'down',
                'line_protocol': 'down'
            },
            'Management0/0': {
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up'
            },
            'Vlan150': {
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'up',
                'line_protocol': 'up'
            },
            'Vlan160': {
				'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'check': 'YES',
                'method': 'CONFIG',
                'link_status': 'down',
                'line_protocol': 'down'
            },
            'Vlan170': {
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

    golden_output = {'execute.return_value': '''
		Interface IP-Address OK? Method Status Protocol
		Control0/0 10.10.1.1 YES CONFIG up up
		GigabitEthernet0/0 10.10.1.1 YES CONFIG up up
		GigabitEthernet0/1 unassigned YES unset admin down down
		GigabitEthernet0/2 10.10.1.1 YES manual admin down down
		GigabitEthernet0/3 10.10.1.1 YES DHCP admin down down
		Management0/0 10.10.1.1 YES CONFIG up
		Vlan150                   10.10.1.1  YES CONFIG up                    up
		Vlan160                   10.10.1.1  YES CONFIG down                  down
		Vlan170                    unassigned      YES unset  up                    up
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

# =============================================
# Parser for 'show interface detail'
# =============================================
class test_show_interface_detail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'Vlan5000': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod248',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
                'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
                    },
                },
                'subnet': '255.255.255.0',
                'traffic_statistics': {
                    'packets_input': 34354322,
                    'bytes_input': 32443242111,
                    'packets_output': 92739172,
                    'bytes_output': 4309803982,
                    'packets_dropped': 2551519
                },
                'control_point_states': {
                    'interface': {
                        'interface_number': 899,
                        'interface_config_status': 'active',
                        'interface_state': 'active'
                    },
                    'Vlan5000':{
                        'interface_vlan_config_status': 'active',
                        'interface_vlan_state': 'UP'
                    },
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
    	DevNet-asa-sm-1/admin# show interface detail
		Interface Vlan5000 "pod248", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		  Traffic Statistics for "pod248":
			34354322 packets input, 32443242111 bytes
			92739172 packets output, 4309803982 bytes
			2551519 packets dropped
		  Control Point Interface States:
			Interface number is 899
			Interface config status is active
			Interface state is active
		  Control Point Vlan5000 States:
			Interface vlan config status is active
			Interface vlan state is UP
	'''}

    golden_parsed_output_2 = {
        'interfaces': {
            'Vlan6000': {
                'interface_state': False,
                'config_status': True,
                'name': 'pod555',
                'link_status': False,
                'line_protocol': False,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
                'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
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
                        'interface_number': 612,
                        'interface_config_status': 'active',
                        'interface_state': 'not active'
                    },
                    'Vlan6000':{
                        'interface_vlan_config_status': 'not active',
                        'interface_vlan_state': 'DOWN'
                    },
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
    	DevNet-asa-sm-1/admin# show interface detail
		Interface Vlan6000 "pod555", is down, line protocol is down
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		  Traffic Statistics for "pod555":
			0 packets input, 0 bytes
			0 packets output, 0 bytes
			0 packets dropped
		  Control Point Interface States:
			Interface number is 612
			Interface config status is active
			Interface state is not active
		  Control Point Vlan1600 States:
			Interface vlan config status is not active
			Interface vlan state is DOWN (down in system space)
	'''}

    golden_parsed_output_3 = {
        'interfaces': {
            'Vlan300': {
                'interface_state': True,
                'config_status': True,
                'name': 'admin-out',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
                'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
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
                'name': 'pod10-in',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
                'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
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
            'Vlan500': {
                'interface_state': True,
                'config_status': False,
                'name': '',
                'link_status': True,
                'line_protocol': True,
                'config_issue': 'nameif'
            },
            'Vlan600': {
                'interface_state': True,
                'config_status': True,
                'name': 'adminTEST',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
                'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
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
                    'Vlan600':{
                        'interface_vlan_config_status': 'active',
                        'interface_vlan_state': 'UP'
                    },
                }
            },
            'Vlan700': {
                'interface_state': True,
                'config_status': True,
                'name': 'pod1',
                'link_status': True,
                'line_protocol': True,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
                'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
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
                    'Vlan700':{
                        'interface_vlan_config_status': 'active',
                        'interface_vlan_state': 'UP'
                    },
                }
            },
            'Vlan1600': {
                'interface_state': False,
                'config_status': True,
                'name': 'pod249',
                'link_status': False,
                'line_protocol': False,
                'mac_address': 'aa11.bb22.cc33',
                'mtu': 1500,
                'ipv4': {
                    '10.10.1.1': { 
                        'ip': '10.10.1.1'
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
                    'Vlan1600':{
		                'interface_vlan_config_status': 'not active',
		                'interface_vlan_state': 'DOWN'
                    },
                }
            }
        }
    }

    golden_output_3 = {'execute.return_value': '''
    	ciscoasa/admin# show interface detail
		Interface Vlan300 "admin-out", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		  Traffic Statistics for "admin-out":
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
		Interface Vlan400 "pod10-in", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		  Traffic Statistics for "pod10-in":
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
		Interface Vlan500 "", is up, line protocol is up
			Available but not configured via nameif
		Interface Vlan600 "adminTEST", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		  Traffic Statistics for "adminTEST":
			1212307 packets input, 96880666 bytes
			1 packets output, 28 bytes
			1212268 packets dropped
		  Control Point Interface States:
			Interface number is 507
			Interface config status is active
			Interface state is active
		  Control Point Vlan600 States:
			Interface vlan config status is active
			Interface vlan state is UP
		Interface Vlan700 "pod1", is up, line protocol is up
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		  Traffic Statistics for "pod1":
			7299914 packets input, 6411442725 bytes
			2862092 packets output, 118819269 bytes
			1288374 packets dropped
		  Control Point Interface States:
			Interface number is 508
			Interface config status is active
			Interface state is active
		  Control Point Vlan700 States:
			Interface vlan config status is active
			Interface vlan state is UP
		Interface Vlan1600 "pod249", is down, line protocol is down
			MAC address aa11.bb22.cc33, MTU 1500
			IP address 10.10.1.1, subnet mask 255.255.255.0
		  Traffic Statistics for "pod249":
			0 packets input, 0 bytes
			0 packets output, 0 bytes
			0 packets dropped
		  Control Point Interface States:
			Interface number is 757
			Interface config status is active
			Interface state is not active
		  Control Point Vlan1600 States:
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