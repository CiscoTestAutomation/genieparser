#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxr.show_spanning_tree import ShowSpanningTreeMst, \
										ShowSpanningTreeMstag, \
										ShowSpanningTreePvrst, \
										ShowSpanningTreePvrsTag, \
										ShowSpanningTreePvsTag

"""
Unit test for 'show spanning-tree mst <mst_id>'
"""
class show_spanning_tree_mst(unittest.TestCase):
	dev = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}
	golden_parsed_output = {
		'mstp': {
		    'test': {
		        'mst_instances': {
		            '0': {
		                'mst_id': '0',
		                'vlan': '1-4094',
		                'cist_root_priority': 32768,
		                'cist_root_address': '0021.1bff.0e05',
		                'cist_root_cost': 2000,
		                'designated_root_priority': 32768,
		                'designated_root_address': 'd867.d9ff.e420',
		                'this_bridge_is': 'the root',
		                'root_cost': 0,
		                'root_max_age': 20,
		                'root_forward_delay': 15,
		                'bridge_priority': 32768,
		                'sys_id_ext': 0,
		                'bridge_address': 'd867.d9ff.e420',
		                'bridge_max_age': 20,
		                'bridge_forward_delay': 15,
		                'bridge_max_hops': 20,
		                'bridge_transmit_hold_count': 6,
		                'interfaces': {
		                    'TenGigabitEthernet0/0/0/16': {
		                        'name': 'TenGigabitEthernet0/0/0/16',
		                        'cost': 2000,
		                        'role': 'ROOT',
		                        'port_priority': 128,
		                        'port_num': 1,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '0021.1bff.0e05',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 1,
		                        },
		                    'TenGigabitEthernet0/0/0/17': {
		                        'name': 'TenGigabitEthernet0/0/0/17',
		                        'cost': 2000,
		                        'role': 'ALT',
		                        'port_priority': 128,
		                        'port_num': 2,
		                        'port_state': 'BLK',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '0021.1bff.0e05',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 2,
		                        },
		                    },
		                },
		            },
		        },
		    },
		}

	golden_output = {'execute.return_value': '''\
	RP/0/RSP0/CPU0:athens#show spanning-tree mst test
	Tue Nov 14 05:54:37.272 EST
	Role:  ROOT=Root, DSGN=Designated, ALT=Alternate, BKP=Backup, MSTR=Master
	State: FWD=Forwarding, LRN=Learning, BLK=Blocked, DLY=Bringup Delayed

	Operating in dot1q mode


	MSTI 0 (CIST):

	  VLANS Mapped: 1-4094

	  CIST Root  Priority    32768
	             Address     0021.1bff.0e05
	             Ext Cost    2000

	  Root ID    Priority    32768
	             Address     d867.d9ff.e420
	             This bridge is the root
	             Int Cost    0
	             Max Age 20 sec, Forward Delay 15 sec


	  Bridge ID  Priority    32768 (priority 32768 sys-id-ext 0)
	             Address     d867.d9ff.e420
	             Max Age 20 sec, Forward Delay 15 sec
	             Max Hops 20, Transmit Hold count  6


	Interface    Port ID           Role State Designated           Port ID
	             Pri.Nbr Cost                 Bridge ID            Pri.Nbr 
	------------ ------- --------- ---- ----- -------------------- -------
	Te0/0/0/16   128.1   2000      ROOT FWD   32768 0021.1bff.0e05 128.1  
	Te0/0/0/17   128.2   2000      ALT  BLK   32768 0021.1bff.0e05 128.2  
	'''}

	golden_parsed_output_2 = {
		'mstp': {
		    'blocked-ports': {
		        'mst_instances': {
		            '0': {
		                'mst_id': '0',
		                'interfaces': {
		                    'GigabitEthernet0/0/4/4': {
		                        'name': 'GigabitEthernet0/0/4/4',
		                        'cost': 200000,
		                        'role': 'ALT',
		                        'port_priority': 128,
		                        'port_num': 196,
		                        'port_state': 'BLK',
		                        'designated_bridge_priority': 4097,
		                        'designated_bridge_address': '0004.9bff.8078',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 195,
		                        },
		                    },
		                },
		            },
		        },
		    },
		}

	golden_output_2 = {'execute.return_value' : '''
	RP/0/RSP0/CPU0:router# show spanning-tree mst blocked-ports
	MSTI 0 (CIST):

	Interface                Port ID                     Designated               Port ID
	Name                     Prio.Nbr Cost   Role State  Cost Bridge ID           Prio.Nbr
	----------------------   -------- ------ ---------   ------------------------ --------
	GigabitEthernet0/0/4/4      128.196  200000 ALT  BLK    0    4097 0004.9bff.8078 128.195

	'''}

	def test_empty(self):
	    self.dev = Mock(**self.empty_output)
	    obj = ShowSpanningTreeMst(device=self.dev)
	    with self.assertRaises(SchemaEmptyParserError):
	        parsed_output = obj.parse(mst='test')

	def test_golden_mst(self):
	    self.dev = Mock(**self.golden_output)
	    obj = ShowSpanningTreeMst(device=self.dev)
	    parsed_output = obj.parse(mst='test')
	    self.assertEqual(parsed_output,self.golden_parsed_output)

	def test_golden_mst_2(self):
	    self.dev = Mock(**self.golden_output_2)
	    obj = ShowSpanningTreeMst(device=self.dev)
	    parsed_output = obj.parse(mst='blocked-ports')
	    self.assertEqual(parsed_output,self.golden_parsed_output_2)

"""
Unit test for 'show spanning-tree mstag <mag_domain>'
"""
class show_spanning_tree_mstag(unittest.TestCase):
	dev = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}
	golden_parsed_output = {
		'mstag': {
		    'risc': {
		        'domain': 'risc',
		        'interfaces': {
		            'Bundle-Ether10.0': {
		                'interface': 'Bundle-Ether10.0',
		                'preempt_delay': False,
		                'name': 'risc',
		                'revision': 1,
		                'max_age': 20,
		                'provider_bridge': False,
		                'bridge_id': '0000.00ff.0002',
		                'port_id': 1,
		                'external_cost': 0,
		                'hello_time': 2,
		                'active': True,
		                'counters': {
		                    'bdpu_sent': 39921,
		                    },
		                },
		            'instances': {
		                '0': {
		                    'instance': 0,
		                    'vlans': '1-2,4-4094',
		                    'priority': 8192,
		                    'port_priority': 128,
		                    'cost': 0,
		                    'root_bridge': '0000.00ff.0001',
		                    'root_priority': 4096,
		                    'counters': {
		                        'topology_changes': 31,
		                        },
		                    },
		                '1': {
		                    'instance': 1,
		                    'vlans': '3',
		                    'priority': 4096,
		                    'port_priority': 128,
		                    'cost': 0,
		                    'root_bridge': '0000.00ff.0002',
		                    'root_priority': 4096,
		                    'counters': {
		                        'topology_changes': 51,
		                        },
		                    },
		                },
		            },
		        },
		    },
		}
	golden_output = {'execute.return_value': '''\
	RP/0/RSP0/CPU0:iamx#show spanning-tree mstag risc
	Fri Apr 22 17:26:52.757 CEST
	Bundle-Ether10.0
	  Pre-empt delay is disabled
	  Name:            risc
	  Revision:        1
	  Max Age:         20
	  Provider Bridge: no
	  Bridge ID:       0000.00ff.0002
	  Port ID:         1
	  External Cost:   0
	  Hello Time:      2
	  Active:          yes
	  BPDUs sent:      39921
	    MSTI 0 (CIST):
	    VLAN IDs:         1-2,4-4094
	    Bridge Priority:  8192
	    Port Priority:    128
	    Cost:             0
	    Root Bridge:      0000.00ff.0001
	    Root Priority:    4096
	    Topology Changes: 31
	  MSTI 1
	    VLAN IDs:         3
	    Bridge Priority:  4096
	    Port Priority:    128
	    Cost:             0
	    Root Bridge:      0000.00ff.0002
	    Root Priority:    4096
	    Topology Changes: 51

	'''}

	golden_output_2 = {'execute.return_value' : '''
	RP/0/RSP0/CPU0:router# show spanning-tree mstag A
	GigabitEthernet0/0/0/1
	  Preempt delay is disabled.
	  Name:            6161:6161:6161
	  Revision:        0
	  Max Age:         20
	  Provider Bridge: no
	  Bridge ID:       6161.61ff.c2c2
	  Port ID:         1
	  External Cost:   0
	  Hello Time:      2
	  Active:          no
	  BPDUs sent:      0
	    MSTI 0 (CIST):
	    VLAN IDs:         1-9,32-39,41-4094
	    Role:             Designated
	    Bridge Priority:  32768
	    Port Priority:    128
	    Cost:             0
	    Root Bridge:      6161.61ff.c2c2
	    Root Priority:    32768
	    Topology Changes: 123
	  MSTI 2
	    VLAN IDs:         10-31
	    Role:             Designated
	    Bridge Priority:  32768
	    Port Priority:    128
	    Cost:             0
	    Root Bridge:      6161.61ff.c2c2
	    Root Priority:    32768
	    Topology Changes: 123
	  MSTI 10
	VLAN IDs:         40
	    Role:             Root (Edge mode)
	    Bridge Priority:  32768
		Port Priority:    128
	    Cost:             200000000
	    Root Bridge:      6161.61ff.c2c2
	    Root Priority:    61440
	    Topology Changes: 0
	'''}

	golden_parsed_output_2 = {
		'mstag': {
		    'A': {
		        'domain': 'A',
		        'interfaces': {
		            'GigabitEthernet0/0/0/1': {
		                'interface': 'GigabitEthernet0/0/0/1',
		                'preempt_delay': False,
		                'name': '6161:6161:6161',
		                'revision': 0,
		                'max_age': 20,
		                'provider_bridge': False,
		                'bridge_id': '6161.61ff.c2c2',
		                'port_id': 1,
		                'external_cost': 0,
		                'hello_time': 2,
		                'active': False,
		                'counters': {
		                    'bdpu_sent': 0,
		                    },
		                },
		            'instances': {
		                '0': {
		                    'instance': 0,
		                    'vlans': '1-9,32-39,41-4094',
		                    'priority': 32768,
		                    'port_priority': 128,
		                    'cost': 0,
		                    'root_bridge': '6161.61ff.c2c2',
		                    'root_priority': 32768,
		                    'counters': {
		                        'topology_changes': 123,
		                        },
		                    },
		                '2': {
		                    'instance': 2,
		                    'vlans': '10-31',
		                    'priority': 32768,
		                    'port_priority': 128,
		                    'cost': 0,
		                    'root_bridge': '6161.61ff.c2c2',
		                    'root_priority': 32768,
		                    'counters': {
		                        'topology_changes': 123,
		                        },
		                    },
		                '10': {
		                    'instance': 10,
		                    'vlans': '40',
		                    'priority': 32768,
		                    'port_priority': 128,
		                    'cost': 200000000,
		                    'root_bridge': '6161.61ff.c2c2',
		                    'root_priority': 61440,
		                    'counters': {
		                        'topology_changes': 0,
		                        },
		                    },
		                },
		            },
		        },
		    },
		}

	def test_empty(self):
	    self.dev = Mock(**self.empty_output)
	    obj = ShowSpanningTreeMstag(device=self.dev)
	    with self.assertRaises(SchemaEmptyParserError):
	        parsed_output = obj.parse(mag_domain='risc')

	def test_golden_mst(self):
	    self.dev = Mock(**self.golden_output)
	    obj = ShowSpanningTreeMstag(device=self.dev)
	    parsed_output = obj.parse(mag_domain='risc')
	    self.assertEqual(parsed_output,self.golden_parsed_output)

	def test_golden_mst_2(self):
	    self.dev = Mock(**self.golden_output_2)
	    obj = ShowSpanningTreeMstag(device=self.dev)
	    parsed_output = obj.parse(mag_domain='A')
	    self.assertEqual(parsed_output,self.golden_parsed_output_2)

"""
Unit test for 'show spanning-tree pvrst <pvst_id>'
"""
class show_spanning_tree_pvrst(unittest.TestCase):
	dev = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}
	golden_parsed_output = {
		'pvst': {
		    'a': {
		        'pvst_id': 'a',
		        'vlans': {
		            2: {
		                'vlan_id': 2,
		                'designated_root_priority': 32768,
		                'designated_root_address': '0021.1bff.d973',
		                'designated_root_max_age': 20,
		                'designated_root_forward_delay': 15,
		                'bridge_priority': 32768,
		                'sys_id_ext': 0,
		                'bridge_address': '8cb6.4fff.6588',
		                'bridge_max_age': 20,
		                'bridge_forward_delay': 15,
		                'bridge_transmit_hold_count': 6,
		                'interface': {
		                    'GigabitEthernet0/7/0/0': {
		                        'name': 'GigabitEthernet0/7/0/0',
		                        'cost': 20000,
		                        'role': 'DSGN',
		                        'port_priority': 128,
		                        'port_num': 1,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '8cb6.4fff.6588',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 1,
		                        },
		                    'GigabitEthernet0/7/0/1': {
		                        'name': 'GigabitEthernet0/7/0/1',
		                        'cost': 20000,
		                        'role': 'DSGN',
		                        'port_priority': 128,
		                        'port_num': 2,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '8cb6.4fff.6588',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 2,
		                        },
		                    'GigabitEthernet0/7/0/10': {
		                        'name': 'GigabitEthernet0/7/0/10',
		                        'cost': 20000,
		                        'role': 'ROOT',
		                        'port_priority': 128,
		                        'port_num': 3,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '0021.1bff.d973',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 3,
		                        },
		                    'GigabitEthernet0/7/0/11': {
		                        'name': 'GigabitEthernet0/7/0/11',
		                        'cost': 20000,
		                        'role': 'ALT',
		                        'port_priority': 128,
		                        'port_num': 4,
		                        'port_state': 'BLK',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '0021.1bff.d973',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 4,
		                        },
		                    },
		                },
		            3: {
		                'vlan_id': 3,
		                'designated_root_priority': 32768,
		                'designated_root_address': '0021.1bff.d973',
		                'designated_root_max_age': 20,
		                'designated_root_forward_delay': 15,
		                'bridge_priority': 32768,
		                'sys_id_ext': 0,
		                'bridge_address': '8cb6.4fff.6588',
		                'bridge_max_age': 20,
		                'bridge_forward_delay': 15,
		                'bridge_transmit_hold_count': 6,
		                'interface': {
		                    'GigabitEthernet0/7/0/0': {
		                        'name': 'GigabitEthernet0/7/0/0',
		                        'cost': 20000,
		                        'role': 'DSGN',
		                        'port_priority': 128,
		                        'port_num': 1,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '8cb6.4fff.6588',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 1,
		                        },
		                    'GigabitEthernet0/7/0/1': {
		                        'name': 'GigabitEthernet0/7/0/1',
		                        'cost': 20000,
		                        'role': 'DSGN',
		                        'port_priority': 128,
		                        'port_num': 2,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '8cb6.4fff.6588',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 2,
		                        },
		                    'GigabitEthernet0/7/0/10': {
		                        'name': 'GigabitEthernet0/7/0/10',
		                        'cost': 20000,
		                        'role': 'ROOT',
		                        'port_priority': 128,
		                        'port_num': 3,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '0021.1bff.d973',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 3,
		                        },
		                    'GigabitEthernet0/7/0/11': {
		                        'name': 'GigabitEthernet0/7/0/11',
		                        'cost': 20000,
		                        'role': 'ALT',
		                        'port_priority': 128,
		                        'port_num': 4,
		                        'port_state': 'BLK',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '0021.1bff.d973',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 4,
		                        },
		                    },
		                },
		            4: {
		                'vlan_id': 4,
		                'designated_root_priority': 32768,
		                'designated_root_address': '0021.1bff.d973',
		                'designated_root_max_age': 20,
		                'designated_root_forward_delay': 15,
		                'bridge_priority': 32768,
		                'sys_id_ext': 0,
		                'bridge_address': '8cb6.4fff.6588',
		                'bridge_max_age': 20,
		                'bridge_forward_delay': 15,
		                'bridge_transmit_hold_count': 6,
		                'interface': {
		                    'GigabitEthernet0/7/0/0': {
		                        'name': 'GigabitEthernet0/7/0/0',
		                        'cost': 20000,
		                        'role': 'DSGN',
		                        'port_priority': 128,
		                        'port_num': 1,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '8cb6.4fff.6588',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 1,
		                        },
		                    'GigabitEthernet0/7/0/1': {
		                        'name': 'GigabitEthernet0/7/0/1',
		                        'cost': 20000,
		                        'role': 'DSGN',
		                        'port_priority': 128,
		                        'port_num': 2,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '8cb6.4fff.6588',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 2,
		                        },
		                    'GigabitEthernet0/7/0/10': {
		                        'name': 'GigabitEthernet0/7/0/10',
		                        'cost': 20000,
		                        'role': 'ROOT',
		                        'port_priority': 128,
		                        'port_num': 3,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '0021.1bff.d973',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 3,
		                        },
		                    'GigabitEthernet0/7/0/11': {
		                        'name': 'GigabitEthernet0/7/0/11',
		                        'cost': 20000,
		                        'role': 'ALT',
		                        'port_priority': 128,
		                        'port_num': 4,
		                        'port_state': 'BLK',
		                        'designated_bridge_priority': 32768,
		                        'designated_bridge_address': '0021.1bff.d973',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 4,
		                        },
		                    },
		                },
		            },
		        },
		    },
		}

	golden_output = {'execute.return_value': '''\
	RP/0/RSP0/CPU0:vkg3#show spanning-tree pvrst a       
	Role:  ROOT=Root, DSGN=Designated, ALT=Alternate, BKP=Backup
	State: FWD=Forwarding, LRN=Learning, BLK=Blocked


	VLAN 2:

	  Root ID    Priority    32768
	             Address     0021.1bff.d973
	             Max Age 20 sec, Forward Delay 15 sec


	  Bridge ID  Priority    32768 (priority 32768 sys-id-ext 0)
	             Address     8cb6.4fff.6588
	             Max Age 20 sec, Forward Delay 15 sec
	             Transmit Hold count   6


	Interface    Port ID           Role State Designated           Port ID
	             Pri.Nbr Cost                 Bridge ID            Pri.Nbr 
	------------ ------- --------- ---- ----- -------------------- -------
	Gi0/7/0/0    128.1   20000     DSGN FWD   32768 8cb6.4fff.6588 128.1
	Gi0/7/0/1    128.2   20000     DSGN FWD   32768 8cb6.4fff.6588 128.2  
	Gi0/7/0/10   128.3   20000     ROOT FWD   32768 0021.1bff.d973 128.3  
	Gi0/7/0/11   128.4   20000     ALT  BLK   32768 0021.1bff.d973 128.4  

	VLAN 3:

	  Root ID    Priority    32768
	             Address     0021.1bff.d973
	             Max Age 20 sec, Forward Delay 15 sec


	  Bridge ID  Priority    32768 (priority 32768 sys-id-ext 0)
	             Address     8cb6.4fff.6588
	             Max Age 20 sec, Forward Delay 15 sec
	             Transmit Hold count  6


	Interface    Port ID           Role State Designated           Port ID
	             Pri.Nbr Cost                 Bridge ID            Pri.Nbr 
	------------ ------- --------- ---- ----- -------------------- -------
	Gi0/7/0/0    128.1   20000     DSGN FWD   32768 8cb6.4fff.6588 128.1  
	Gi0/7/0/1    128.2   20000     DSGN FWD   32768 8cb6.4fff.6588 128.2  
	Gi0/7/0/10   128.3   20000     ROOT FWD   32768 0021.1bff.d973 128.3  
	Gi0/7/0/11   128.4   20000     ALT  BLK   32768 0021.1bff.d973 128.4  

	VLAN 4:

	  Root ID    Priority    32768
	             Address     0021.1bff.d973
	             Max Age 20 sec, Forward Delay 15 sec


	  Bridge ID  Priority    32768 (priority 32768 sys-id-ext 0)
	             Address     8cb6.4fff.6588
	             Max Age 20 sec, Forward Delay 15 sec
	             Transmit Hold count  6


	Interface    Port ID           Role State Designated           Port ID
	             Pri.Nbr Cost                 Bridge ID            Pri.Nbr 
	------------ ------- --------- ---- ----- -------------------- -------
	Gi0/7/0/0    128.1   20000     DSGN FWD   32768 8cb6.4fff.6588 128.1  
	Gi0/7/0/1    128.2   20000     DSGN FWD   32768 8cb6.4fff.6588 128.2  
	Gi0/7/0/10   128.3   20000     ROOT FWD   32768 0021.1bff.d973 128.3  
	Gi0/7/0/11   128.4   20000     ALT  BLK   32768 0021.1bff.d973 128.4

	'''}

	golden_output_2 = {'execute.return_value' : '''
	RP/0/RSP0/CPU0:router# show spanning-tree pvrst MSTP
	Role: ROOT=Root, DSGN=Designated, ALT=Alternate, BKP=Backup
	State: FWD=Forwarding, LRN=Learning, BLK=Blocked


	VLAN 10:

	Root ID Priority 4096
	Address 8cb6.4fff.6588
	This bridge is the root
	Max Age 20 sec, Forward Delay 15 sec


	Bridge ID Priority 4096 (priority 4096 sys-id-ext 0)
	Address 8cb6.4fff.6588
	Max Age 20 sec, Forward Delay 15 sec
	Transmit Hold count 6


	Interface Port ID Role State Designated Port ID
	Pri.Nbr Cost Bridge ID Pri.Nbr
	------------ ------- --------- ---- ----- -------------------- -------
	Gi0/5/0/0 128.1 20000 DSGN FWD 4096 8cb6.4fff.6588 128.1
	Gi0/5/0/2 128.2 20000 DSGN FWD 4096 8cb6.4fff.6588 128.2

	VLAN 20:

	Root ID Priority 8192
	Address c062.6bff.4d2b
	Max Age 20 sec, Forward Delay 15 sec


	Bridge ID Priority 16384 (priority 16384 sys-id-ext 0)
	Address 8cb6.4fff.6588
	Max Age 20 sec, Forward Delay 15 sec
	Transmit Hold count 6


	Interface Port ID Role State Designated Port ID
	Pri.Nbr Cost Bridge ID Pri.Nbr
	------------ ------- --------- ---- ----- -------------------- -------
	Gi0/5/0/0 128.1 20000 ROOT FWD 8192 c062.6bff.4d2b 128.1
	Gi0/5/0/2 128.2 20000 ALT BLK 8192 c062.6bff.4d2b 128.2
	'''}

	golden_parsed_output_2 = {
		'pvst': {
		    'MSTP': {
		        'pvst_id': 'MSTP',
		        'vlans': {
		            10: {
		                'vlan_id': 10,
		                'designated_root_priority': 4096,
		                'designated_root_address': '8cb6.4fff.6588',
		                'designated_root_max_age': 20,
		                'designated_root_forward_delay': 15,
		                'bridge_priority': 4096,
		                'sys_id_ext': 0,
		                'bridge_address': '8cb6.4fff.6588',
		                'bridge_max_age': 20,
		                'bridge_forward_delay': 15,
		                'bridge_transmit_hold_count': 6,
		                'interface': {
		                    'GigabitEthernet0/5/0/0': {
		                        'name': 'GigabitEthernet0/5/0/0',
		                        'cost': 20000,
		                        'role': 'DSGN',
		                        'port_priority': 128,
		                        'port_num': 1,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 4096,
		                        'designated_bridge_address': '8cb6.4fff.6588',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 1,
		                        },
		                    'GigabitEthernet0/5/0/2': {
		                        'name': 'GigabitEthernet0/5/0/2',
		                        'cost': 20000,
		                        'role': 'DSGN',
		                        'port_priority': 128,
		                        'port_num': 2,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 4096,
		                        'designated_bridge_address': '8cb6.4fff.6588',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 2,
		                        },
		                    },
		                },
		            20: {
		                'vlan_id': 20,
		                'designated_root_priority': 8192,
		                'designated_root_address': 'c062.6bff.4d2b',
		                'designated_root_max_age': 20,
		                'designated_root_forward_delay': 15,
		                'bridge_priority': 16384,
		                'sys_id_ext': 0,
		                'bridge_address': '8cb6.4fff.6588',
		                'bridge_max_age': 20,
		                'bridge_forward_delay': 15,
		                'bridge_transmit_hold_count': 6,
		                'interface': {
		                    'GigabitEthernet0/5/0/0': {
		                        'name': 'GigabitEthernet0/5/0/0',
		                        'cost': 20000,
		                        'role': 'ROOT',
		                        'port_priority': 128,
		                        'port_num': 1,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 8192,
		                        'designated_bridge_address': 'c062.6bff.4d2b',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 1,
		                        },
		                    'GigabitEthernet0/5/0/2': {
		                        'name': 'GigabitEthernet0/5/0/2',
		                        'cost': 20000,
		                        'role': 'ALT',
		                        'port_priority': 128,
		                        'port_num': 2,
		                        'port_state': 'BLK',
		                        'designated_bridge_priority': 8192,
		                        'designated_bridge_address': 'c062.6bff.4d2b',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 2,
		                        },
		                    },
		                },
		            },
		        },
		    },
		}

	golden_output_3 = {'execute.return_value' : '''
	RP/0/RSP0/CPU0:router# show spanning-tree pvrst MSTP
	Role: ROOT=Root, DSGN=Designated, ALT=Alternate, BKP=Backup
	State: FWD=Forwarding, LRN=Learning, BLK=Blocked


	VLAN 10:


	Root ID Priority 4096
	Address 8cb6.4fff.6588
	This bridge is the root
	Max Age 20 sec, Forward Delay 15 sec


	Bridge ID Priority 4096 (priority 4096 sys-id-ext 0)
	Address 8cb6.4fff.6588
	Max Age 20 sec, Forward Delay 15 sec
	Transmit Hold count 6


	Interface Port ID Role State Designated Port ID
	Pri.Nbr Cost Bridge ID Pri.Nbr
	------------ ------- --------- ---- ----- -------------------- -------
	Gi0/5/0/0 128.1 20000 DSGN FWD 4096 8cb6.4fff.6588 128.1
	Gi0/5/0/2 128.2 20000 DSGN FWD 4096 8cb6.4fff.6588 128.2

	VLAN 20:

	Root ID Priority 8192
	Address c062.6bff.4d2b
	Max Age 20 sec, Forward Delay 15 sec


	Bridge ID Priority 16384 (priority 16384 sys-id-ext 0)
	Address 8cb6.4fff.6588
	Max Age 20 sec, Forward Delay 15 sec
	Transmit Hold count 6


	Interface Port ID Role State Designated Port ID
	Pri.Nbr Cost Bridge ID Pri.Nbr
	------------ ------- --------- ---- ----- -------------------- -------
	Gi0/5/0/0 128.1 20000 ROOT FWD 8192 c062.6bff.4d2b 128.1
	Gi0/5/0/2 128.2 20000 ALT BLK 8192 c062.6bff.4d2b 128.2
	'''}

	golden_parsed_output_3 = {
		'pvst': {
		    'MSTP': {
		        'pvst_id': 'MSTP',
		        'vlans': {
		            10: {
		                'vlan_id': 10,
		                'designated_root_priority': 4096,
		                'designated_root_address': '8cb6.4fff.6588',
		                'designated_root_max_age': 20,
		                'designated_root_forward_delay': 15,
		                'bridge_priority': 4096,
		                'sys_id_ext': 0,
		                'bridge_address': '8cb6.4fff.6588',
		                'bridge_max_age': 20,
		                'bridge_forward_delay': 15,
		                'bridge_transmit_hold_count': 6,
		                'interface': {
		                    'GigabitEthernet0/5/0/0': {
		                        'name': 'GigabitEthernet0/5/0/0',
		                        'cost': 20000,
		                        'role': 'DSGN',
		                        'port_priority': 128,
		                        'port_num': 1,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 4096,
		                        'designated_bridge_address': '8cb6.4fff.6588',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 1,
		                        },
		                    'GigabitEthernet0/5/0/2': {
		                        'name': 'GigabitEthernet0/5/0/2',
		                        'cost': 20000,
		                        'role': 'DSGN',
		                        'port_priority': 128,
		                        'port_num': 2,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 4096,
		                        'designated_bridge_address': '8cb6.4fff.6588',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 2,
		                        },
		                    },
		                },
		            20: {
		                'vlan_id': 20,
		                'designated_root_priority': 8192,
		                'designated_root_address': 'c062.6bff.4d2b',
		                'designated_root_max_age': 20,
		                'designated_root_forward_delay': 15,
		                'bridge_priority': 16384,
		                'sys_id_ext': 0,
		                'bridge_address': '8cb6.4fff.6588',
		                'bridge_max_age': 20,
		                'bridge_forward_delay': 15,
		                'bridge_transmit_hold_count': 6,
		                'interface': {
		                    'GigabitEthernet0/5/0/0': {
		                        'name': 'GigabitEthernet0/5/0/0',
		                        'cost': 20000,
		                        'role': 'ROOT',
		                        'port_priority': 128,
		                        'port_num': 1,
		                        'port_state': 'FWD',
		                        'designated_bridge_priority': 8192,
		                        'designated_bridge_address': 'c062.6bff.4d2b',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 1,
		                        },
		                    'GigabitEthernet0/5/0/2': {
		                        'name': 'GigabitEthernet0/5/0/2',
		                        'cost': 20000,
		                        'role': 'ALT',
		                        'port_priority': 128,
		                        'port_num': 2,
		                        'port_state': 'BLK',
		                        'designated_bridge_priority': 8192,
		                        'designated_bridge_address': 'c062.6bff.4d2b',
		                        'designated_port_priority': 128,
		                        'designated_port_num': 2,
		                        },
		                    },
		                },
		            },
		        },
		    },
		}

	def test_empty(self):
	    self.dev = Mock(**self.empty_output)
	    obj = ShowSpanningTreePvrst(device=self.dev)
	    with self.assertRaises(SchemaEmptyParserError):
	        parsed_output = obj.parse(pvst_id='a')

	def test_golden_mst(self):
	    self.dev = Mock(**self.golden_output)
	    obj = ShowSpanningTreePvrst(device=self.dev)
	    parsed_output = obj.parse(pvst_id='a')
	    self.assertEqual(parsed_output,self.golden_parsed_output)

	def test_golden_mst_2(self):
	    self.dev = Mock(**self.golden_output_2)
	    obj = ShowSpanningTreePvrst(device=self.dev)
	    parsed_output = obj.parse(pvst_id='MSTP')
	    self.assertEqual(parsed_output,self.golden_parsed_output_2)

	def test_golden_mst_3(self):
	    self.dev = Mock(**self.golden_output_3)
	    obj = ShowSpanningTreePvrst(device=self.dev)
	    parsed_output = obj.parse(pvst_id='MSTP')
	    self.assertEqual(parsed_output,self.golden_parsed_output_3)

"""
Unit test for 'show spanning-tree pvrstag <pvrstag_domain>'
"""
class show_spanning_tree_pvrstag(unittest.TestCase):
	dev = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}
	golden_parsed_output = {
		'pvrstag': {
		    'foo': {
		        'domain': 'foo',
		        'interfaces': {
		            'GigabitEthernet0/0/0/0': {
		                'interface': 'GigabitEthernet0/0/0/0',
		                'vlans': {
		                    '5': {
		                        'preempt_delay': True,
		                        'preempt_delay_state': 'Sending startup BPDU until 13:38:03',
		                        'sub_interface': 'GigabitEthernet0/0/0/0.5',
		                        'sub_interface_state': 'Up',
		                        'max_age': 20,
		                        'root_priority': 0,
		                        'root_bridge': '0000.0000.0000',
		                        'root_cost': 1,
		                        'bridge_priority': 32768,
		                        'bridge_id': '0255.1dff.3c70',
		                        'port_priority': 128,
		                        'port_id': 1,
		                        'hello_time': 2,
		                        'active': True,
		                        'counters': {
		                            'bdpu_sent': 6,
		                            'topology_changes': 0,
		                            },
		                        },
		                    },
		                },
		            'GigabitEthernet0/0/0/1': {
		                'interface': 'GigabitEthernet0/0/0/1',
		                'vlans': {
		                    '5': {
		                        'preempt_delay': True,
		                        'preempt_delay_state': 'Sending standard BPDU',
		                        'sub_interface': 'GigabitEthernet0/0/0/1.5',
		                        'sub_interface_state': 'Up',
		                        'max_age': 20,
		                        'root_priority': 0,
		                        'root_bridge': '0000.0000.0000',
		                        'root_cost': 0,
		                        'bridge_priority': 32768,
		                        'bridge_id': '021a.9eff.5645',
		                        'port_priority': 128,
		                        'port_id': 1,
		                        'hello_time': 2,
		                        'active': True,
		                        'counters': {
		                            'bdpu_sent': 7,
		                            'topology_changes': 0,
		                            },
		                        },
		                    },
		                },
		            },
		        },
		    },
		}
		
	golden_output = {'execute.return_value': '''\
	RP/0/0/CPU0:ios#show spanning-tree pvrstag foo
	Wed Mar 29 12:38:05.528 UTC
	GigabitEthernet0/0/0/0
	  VLAN 5
	    Pre-empt delay is enabled. Sending startup BPDU until 13:38:03
	    Sub-interface:    GigabitEthernet0/0/0/0.5 (Up)
	    Max Age: 20
	    Root Priority:    0
	    Root Bridge: 0000.0000.0000
	    Cost:             1
	    Bridge Priority:  32768
	    Bridge ID:        0255.1dff.3c70
	    Port Priority:    128
	    Port ID           1
	    Hello Time:       2
	    Active:           Yes
	    BPDUs sent:       6
	    Topology Changes: 0

	GigabitEthernet0/0/0/1
	  VLAN 5
	    Pre-empt delay is enabled. Sending standard BPDU
	    Sub-interface:    GigabitEthernet0/0/0/1.5 (Up)
	    Max Age:          20
	    Root Priority:    0
	    Root Bridge:      0000.0000.0000
	    Cost:             0
	    Bridge Priority:  32768
	    Bridge ID:        021a.9eff.5645
	    Port Priority:    128
	    Port ID           1
	    Hello Time:       2
	    Active:           Yes
	    BPDUs sent:       7
	    Topology Changes: 0
	'''}

	def test_empty(self):
	    self.dev = Mock(**self.empty_output)
	    obj = ShowSpanningTreePvrsTag(device=self.dev)
	    with self.assertRaises(SchemaEmptyParserError):
	        parsed_output = obj.parse(pvrstag_domain='foo')

	def test_golden_pvrstag(self):
	    self.dev = Mock(**self.golden_output)
	    obj = ShowSpanningTreePvrsTag(device=self.dev)
	    parsed_output = obj.parse(pvrstag_domain='foo')
	    self.assertEqual(parsed_output,self.golden_parsed_output)

"""
Unit test for 'show spanning-tree pvstag <pvstag_domain>'
"""
class show_spanning_tree_pvstag(unittest.TestCase):
	dev = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}
	golden_parsed_output = {
		'pvstag': {
		    'foo': {
		        'domain': 'foo',
		        'interfaces': {
		            'Bundle-Ether1000': {
		                'interface': 'Bundle-Ether1000',
		                'vlans': {
		                    '2100': {
		                        'preempt_delay': False,
		                        'sub_interface': 'Bundle-Ether1000.2100',
		                        'sub_interface_state': 'Up',
		                        'max_age': 20,
		                        'root_priority': 0,
		                        'root_bridge': '0000.0000.0000',
		                        'root_cost': 0,
		                        'bridge_priority': 32768,
		                        'bridge_id': '6c9c.edff.8d95',
		                        'port_priority': 128,
		                        'port_id': 1,
		                        'hello_time': 2,
		                        'active': True,
		                        'counters': {
		                            'bdpu_sent': 10,
		                            'topology_changes': 0,
		                            },
		                        },
		                    },
		                },
		            },
		        },
		    },
		}

	golden_output = {'execute.return_value': '''\
	RP/0/RSP0/CPU0:SMU-uut#show spanning-tree pvstag foo 
	Bundle-Ether1000
	  VLAN 2100
	    Pre-empt delay is disabled
	    Sub-interface:    Bundle-Ether1000.2100 (Up)
	    Max Age:          20
	    Root Priority:    0
	    Root Bridge:      0000.0000.0000
	    Cost:             0
	    Bridge Priority:  32768
	    Bridge ID:        6c9c.edff.8d95
	    Port Priority:    128
	    Port ID           1
	    Hello Time:       2
	    Active:           Yes
	    BPDUs sent:       10
	    Topology Changes: 0
	'''}

	def test_empty(self):
	    self.dev = Mock(**self.empty_output)
	    obj = ShowSpanningTreePvsTag(device=self.dev)
	    with self.assertRaises(SchemaEmptyParserError):
	        parsed_output = obj.parse(pvstag_domain='foo')

	def test_golden_pvrstag(self):
	    self.dev = Mock(**self.golden_output)
	    obj = ShowSpanningTreePvsTag(device=self.dev)
	    parsed_output = obj.parse(pvstag_domain='foo')
	    self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()