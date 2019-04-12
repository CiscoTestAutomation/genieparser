#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxr.show_spanning_tree import ShowSpanningTreeMst


class show_spanning_tree_mst(unittest.TestCase):
	dev = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}
	golden_parsed_output = {
		'mst_instances': {
		    '0': {
		        'mst_id': '0',
		        'vlan': '1-4094',
		        'cist_root_priority': 32768,
		        'cist_root_address': '0021.1bfd.1007',
		        'cist_root_cost': 2000,
		        'designated_root_priority': 32768,
		        'designated_root_address': 'd867.d938.ace7',
		        'root_cost': 0,
		        'root_max_age': 20,
		        'root_forward_delay': 15,
		        'bridge_priority': 32768,
		        'sys_id_ext': 0,
		        'bridge_address': 'd867.d938.ace7',
		        'bridge_max_age': 20,
		        'bridge_forward_delay': 15,
		        'bridge_max_hops': 20,
		        'bridge_transmit_hold_count': 6,
		        'interfaces': {
		            'Te0/0/0/16': {
		                'name': 'Te0/0/0/16',
		                'cost': 2000,
		                'role': 'ROOT',
		                'port_priority': 1,
		                'port_num': 128,
		                'port_state': 'FWD',
		                'designated_bridge_priority': 32768,
		                'designated_bridge_address': '0021.1bfd.1007',
		                'designated_port_priority': 1,
		                'designated_port_num': 128,
		                },
		            'Te0/0/0/17': {
		                'name': 'Te0/0/0/17',
		                'cost': 2000,
		                'role': 'ALT',
		                'port_priority': 2,
		                'port_num': 128,
		                'port_state': 'BLK',
		                'designated_bridge_priority': 32768,
		                'designated_bridge_address': '0021.1bfd.1007',
		                'designated_port_priority': 2,
		                'designated_port_num': 128,
		                },
		            },
		        },
		    },
		}
	golden_output = {'execute.return_value': '''\
	Role:  ROOT=Root, DSGN=Designated, ALT=Alternate, BKP=Backup, MSTR=Master
	State: FWD=Forwarding, LRN=Learning, BLK=Blocked, DLY=Bringup Delayed

	Operating in dot1q mode


	MSTI 0 (CIST):

	  VLANS Mapped: 1-4094

	  CIST Root  Priority    32768
	             Address     0021.1bfd.1007
	             Ext Cost    2000

	  Root ID    Priority    32768
	             Address     d867.d938.ace7
	             This bridge is the root
	             Int Cost    0
	             Max Age 20 sec, Forward Delay 15 sec


	  Bridge ID  Priority    32768 (priority 32768 sys-id-ext 0)
	             Address     d867.d938.ace7
	             Max Age 20 sec, Forward Delay 15 sec
	             Max Hops 20, Transmit Hold count  6


	Interface    Port ID           Role State Designated           Port ID
	             Pri.Nbr Cost                 Bridge ID            Pri.Nbr 
	------------ ------- --------- ---- ----- -------------------- -------
	Te0/0/0/16   128.1   2000      ROOT FWD   32768 0021.1bfd.1007 128.1  
	Te0/0/0/17   128.2   2000      ALT  BLK   32768 0021.1bfd.1007 128.2  
	'''}

	def test_empty(self):
	    self.dev = Mock(**self.empty_output)
	    obj = ShowSpanningTreeMst(device=self.dev)
	    with self.assertRaises(SchemaEmptyParserError):
	        parsed_output = obj.parse()

	def test_golden_mst(self):
	    self.dev = Mock(**self.golden_output)
	    obj = ShowSpanningTreeMst(device=self.dev)
	    parsed_output = obj.parse()
	    self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()