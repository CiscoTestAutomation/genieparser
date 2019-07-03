# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
											 SchemaMissingKeyError

# Parser
from genie.libs.parser.nxos.show_vpc import ShowVpc


#=========================================================
# Unit test for show vpc
#=========================================================
class test_show_vpc(unittest.TestCase):

	device = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}

	golden_parsed_output = {
		'vpc_domain_id': 1,
        'vpc-peer-status': 'peer adjacency formed ok',
        'vpc-peer-keepalive-status': 'peer is alive',
        'vpc-configuration-consistency-status': 'success',
        'vpc-per-vlan-consistency-status': 'success',
        'vpc-type-2-consistency-status': 'success',
        'vpc-role': 'primary',
        'num-of-vpcs': 1,
        'peer-gateway': 'Enabled',
        'dual-active-excluded-vlans': '-',
        'vpc-graceful-consistency-check-status': 'Enabled',
        'vpc-auto-recovery-status': 'Enabled, timer is off.(timeout = 240s)',
        'vpc-delay-restore-status': 'Timer is off.(timeout = 30s)',
        'vpc-delay-restore-svi-status': 'Timer is off.(timeout = 10s)',
        'operational-l3-peer-router': 'Disabled',
        'peer-link': {
            1: {
                'peer-link-id': 1,
                'peer-link-ifindex': 'Po101',
                'peer-link-port-state': 'up',
                'peer-up-vlan-bitset': '1,100-102,200-202,300-350'
            }
        },
        'vpc': {
            1: {
            	'vpc-id': 1,
                'vpc-ifindex': 'Po1',
                'vpc-port-state': 'up',
                'vpc-consistency': 'success',
                'vpc-consistency-status': 'success',
                'up-vlan-bitset': '1,100-102,200-202'
            }
        }
	}

	golden_output = {'execute.return_value': '''
		R2# show vpc
		Legend:
		                (*) - local vPC is down, forwarding via vPC peer-link

		vPC domain id                     : 1   
		Peer status                       : peer adjacency formed ok      
		vPC keep-alive status             : peer is alive                 
		Configuration consistency status  : success 
		Per-vlan consistency status       : success                       
		Type-2 consistency status         : success 
		vPC role                          : primary                       
		Number of vPCs configured         : 1   
		Peer Gateway                      : Enabled
		Dual-active excluded VLANs        : -
		Graceful Consistency Check        : Enabled
		Auto-recovery status              : Enabled, timer is off.(timeout = 240s)
		Delay-restore status              : Timer is off.(timeout = 30s)
		Delay-restore SVI status          : Timer is off.(timeout = 10s)
		Operational Layer3 Peer-router    : Disabled

		vPC Peer-link status
		---------------------------------------------------------------------
		id    Port   Status Active vlans    
		--    ----   ------ -------------------------------------------------
		1     Po101  up     1,100-102,200-
							202,300-350
		         

		vPC status
		----------------------------------------------------------------------------
		Id    Port          Status Consistency Reason                Active vlans
		--    ------------  ------ ----------- ------                ---------------
		1     Po1           up     success     success               1,100-102,200-     
                                                             		202               		         


		Please check "show vpc consistency-parameters vpc <vpc-num>" for the 
		consistency reason of down vpc and for type-2 consistency reasons for 
		any vpc.
	'''
	}

	golden_parsed_output_2 = {
		'vpc_domain_id': 10,
        'vpc-peer-status': 'peer adjacency formed ok',
        'vpc-peer-keepalive-status': 'peer is alive',
        'vpc-configuration-consistency-status': 'success',
        'vpc-role': 'primary',
        'num-of-vpcs': 1,
        'peer-link': {
            1: {
                'peer-link-id': 1,
                'peer-link-ifindex': 'Po10',
                'peer-link-port-state': 'up',
                'peer-up-vlan-bitset': '1-100'
            }
        },
        'vpc': {
            20: {
            	'vpc-id': 20,
                'vpc-ifindex': 'Po20',
                'vpc-port-state': 'up',
                'vpc-consistency': 'success',
                'vpc-consistency-status': 'success',
                'up-vlan-bitset': '1-100'
            }
        }
	}

	golden_output_2 = {'execute.return_value': '''
		R2# show vpc
		Legend:
		(*) - local vpc is down, forwarding via vPC peer-link
		 
		vPC domain id : 10
		Peer status : peer adjacency formed ok
		vPC keep-alive status : peer is alive
		Configuration consistency status: success
		vPC role : primary
		Number of vPC configured : 1
		 
		vPC Peer-link status
		---------------------------------------------------------------------
		id Port Status Active vlans
		-- ---- ------ --------------------------------------------------
		1 Po10 up 1-100
		 
		vPC status
		----------------------------------------------------------------------
		id Port Status Consistency Reason Active vlans
		-- ---- ------ ----------- -------------------------- ------------
		20 Po20 up success success 1-100
	'''
	}

	golden_parsed_output_3 = {
		'vpc_domain_id': 10,
        'vpc-peer-status': 'peer adjacency formed ok',
        'vpc-peer-keepalive-status': 'peer is alive',
        'vpc-configuration-consistency-status': 'failed',
        'vpc-configuration-consistency-reason': 'vPC type-1 configuration incompatible - STP interface port type inconsistent',
        'vpc-role': 'secondary',
        'num-of-vpcs': 1,
        'peer-link': {
            1: {
                'peer-link-id': 1,
                'peer-link-ifindex': 'Po10',
                'peer-link-port-state': 'up',
                'peer-up-vlan-bitset': '1-100'
            }
        },
        'vpc': {
            20: {
            	'vpc-id': 20,
                'vpc-ifindex': 'Po20',
                'vpc-port-state': 'up',
                'vpc-consistency': 'failed',
                'vpc-consistency-status': 'vPC type-1 configuration',
                'up-vlan-bitset': '-'
            }
        }
	}

	golden_output_3 = {'execute.return_value': '''
		Legend:
		(*) - local vpc is down, forwarding via vPC peer-link

		vPC domain id : 10
		Peer status : peer adjacency formed ok
		vPC keep-alive status : peer is alive
		Configuration consistency status: failed
		Configuration consistency reason: vPC type-1 configuration incompatible - STP interface port type inconsistent
		vPC role : secondary
		Number of vPC configured : 1

		vPC Peer-link status
		---------------------------------------------------------------------
		id Port Status Active vlans
		-- ---- ------ --------------------------------------------------
		1 Po10 up 1-100

		vPC status
		----------------------------------------------------------------------
		id Port Status Consistency Reason Active vlans
		-- ---- ------ ----------- -------------------------- ------------
		20 Po20 up failed vPC type-1 configuration -
		incompatible - STP
		interface port type
		inconsistent
	'''
	}

	golden_parsed_output_4 = {
		'vpc_domain_id': 1,
        'vpc-peer-status': 'peer adjacency formed ok',
        'vpc-peer-keepalive-status': 'peer is alive',
        'vpc-configuration-consistency-status': 'success',
        'vpc-role': 'secondary',
        'num-of-vpcs': 3,
        'track-object': 12,
        'peer-link': {
            1: {
                'peer-link-id': 1,
                'peer-link-ifindex': 'Po10',
                'peer-link-port-state': 'up',
                'peer-up-vlan-bitset': '1-100'
            }
        }
	}

	golden_output_4 = {'execute.return_value': '''
		Legend:
		(*) - local vpc is down, forwarding via vPC peer-link
		 
		vPC domain id : 1
		Peer status : peer adjacency formed ok
		vPC keep-alive status : peer is alive
		Configuration consistency status: success
		vPC role : secondary
		Number of vPC configured : 3
		Track object : 12
		 
		 
		vPC Peer-link status
		---------------------------------------------------------------------
		id Port Status Active vlans
		-- ---- ------ --------------------------------------------------
		1 Po10 up 1-100
	'''
	}

	golden_parsed_output_5 = {
		'vpc_domain_id': 100,
        'vpc-peer-status': 'peer link is down',
        'vpc-peer-keepalive-status': 'peer is alive, but domain IDs do not match',
        'vpc-configuration-consistency-status': 'success',
        'vpc-per-vlan-consistency-status': 'success',
        'vpc-type-2-consistency-status': 'success',
        'vpc-role': 'primary',
        'num-of-vpcs': 1,
        'peer-gateway': 'Disabled',
        'dual-active-excluded-vlans': '-',
        'vpc-graceful-consistency-check-status': 'Enabled',
        'peer-link': {
            1: {
                'peer-link-id': 1,
                'peer-link-ifindex': 'Po100',
                'peer-link-port-state': 'down',
                'peer-up-vlan-bitset': '-'
            }
        },
        'vpc': {
            1: {
            	'vpc-id': 1,
                'vpc-ifindex': 'Po1',
                'vpc-port-state': 'down',
                'vpc-consistency': 'success',
                'vpc-consistency-status': 'success',
                'up-vlan-bitset': '-'
            }
        }
	}

	golden_output_5 = {'execute.return_value': '''
		Legend:
		(*) - local vPC is down, forwarding via vPC peer-link
		 
		vPC domain id : 100
		Peer status : peer link is down
		vPC keep-alive status : peer is alive, but domain IDs do not match
		Configuration consistency status: success
		Per-vlan consistency status : success
		Type-2 consistency status : success
		vPC role : primary
		Number of vPCs configured : 1
		Peer Gateway : Disabled
		Dual-active excluded VLANs : -
		Graceful Consistency Check : Enabled
		 
		vPC Peer-link status
		---------------------------------------------------------------------
		id Port Status Active vlans
		-- ---- ------ --------------------------------------------------
		1 Po100 down -
		 
		vPC status
		----------------------------------------------------------------------------
		id Port Status Consistency Reason Active vlans
		------ ----------- ------ ----------- -------------------------- -----------
		1 Po1 down success success -
	'''
	}

	def test_empty(self):
		self.device = Mock(**self.empty_output)
		obj = ShowVpc(device=self.device)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()

	def test_golden(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowVpc(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden_2(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_2)
		obj = ShowVpc(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output_2)

	def test_golden_3(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_3)
		obj = ShowVpc(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output_3)

	def test_golden_4(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_4)
		obj = ShowVpc(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output_4)

	def test_golden_5(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_5)
		obj = ShowVpc(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output_5)

if __name__ == '__main__':
	unittest.main()