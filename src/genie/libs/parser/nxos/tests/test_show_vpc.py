# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.nxos.show_vpc import ShowVpc


#=========================================================
# Unit test for show vpc
#=========================================================
class test_show_vpc(unittest.TestCase):

    empty_output = {'execute.return_value': ''}
    maxDiff = None

    golden_parsed_output = {
        'vpc_domain_id': '1',
        'vpc_peer_status': 'peer adjacency formed ok',
        'vpc_peer_keepalive_status': 'peer is alive',
        'vpc_configuration_consistency_status': 'success',
        'vpc_per_vlan_consistency_status': 'success',
        'vpc_type_2_consistency_status': 'success',
        'vpc_role': 'primary',
        'num_of_vpcs': 1,
        'peer_gateway': 'Enabled',
        'dual_active_excluded_vlans': '-',
        'vpc_graceful_consistency_check_status': 'Enabled',
        'vpc_auto_recovery_status': 'Enabled, timer is off.(timeout = 240s)',
        'vpc_delay_restore_status': 'Timer is off.(timeout = 30s)',
        'vpc_delay_restore_svi_status': 'Timer is off.(timeout = 10s)',
        'operational_l3_peer_router': 'Disabled',
        'peer_link': {
            1: {
                'peer_link_id': 1,
                'peer_link_ifindex': 'Port-channel101',
                'peer_link_port_state': 'up',
                'peer_up_vlan_bitset': '1,100-102,200-202,300-350'
            }
        },
        'vpc': {
            1: {
                'vpc_id': 1,
                'vpc_ifindex': 'Port-channel1',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '1,100-102,200-202'
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

        vPC peer-link status
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
        'vpc_domain_id': '10',
        'vpc_peer_status': 'peer adjacency formed ok',
        'vpc_peer_keepalive_status': 'peer is alive',
        'vpc_configuration_consistency_status': 'success',
        'vpc_role': 'primary',
        'num_of_vpcs': 1,
        'peer_link': {
            1: {
                'peer_link_id': 1,
                'peer_link_ifindex': 'Port-channel10',
                'peer_link_port_state': 'up',
                'peer_up_vlan_bitset': '1-100'
            }
        },
        'vpc': {
            20: {
                'vpc_id': 20,
                'vpc_ifindex': 'Port-channel20',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '1-100'
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
         
        vPC peer-link status
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
        'vpc_domain_id': '10',
        'vpc_peer_status': 'peer adjacency formed ok',
        'vpc_peer_keepalive_status': 'peer is alive',
        'vpc_configuration_consistency_status': 'failed',
        'vpc_configuration_consistency_reason': 'vPC type-1 configuration incompatible - STP interface port type inconsistent',
        'vpc_role': 'secondary',
        'num_of_vpcs': 1,
        'peer_link': {
            1: {
                'peer_link_id': 1,
                'peer_link_ifindex': 'Port-channel10',
                'peer_link_port_state': 'up',
                'peer_up_vlan_bitset': '1-100'
            }
        },
        'vpc': {
            20: {
                'vpc_id': 20,
                'vpc_ifindex': 'Port-channel20',
                'vpc_port_state': 'up',
                'vpc_consistency': 'failed',
                'vpc_consistency_status': 'vPC type-1 configuration',
                'up_vlan_bitset': '-'
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

        vPC peer-link status
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
        'vpc_domain_id': '1',
        'vpc_peer_status': 'peer adjacency formed ok',
        'vpc_peer_keepalive_status': 'peer is alive',
        'vpc_configuration_consistency_status': 'success',
        'vpc_role': 'secondary',
        'num_of_vpcs': 3,
        'track_object': 12,
        'peer_link': {
            1: {
                'peer_link_id': 1,
                'peer_link_ifindex': 'Port-channel10',
                'peer_link_port_state': 'up',
                'peer_up_vlan_bitset': '1-100'
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
         
         
        vPC peer-link status
        ---------------------------------------------------------------------
        id Port Status Active vlans
        -- ---- ------ --------------------------------------------------
        1 Po10 up 1-100
    '''
    }

    golden_parsed_output_5 = {
        'vpc_domain_id': '100',
        'vpc_peer_status': 'peer link is down',
        'vpc_peer_keepalive_status': 'peer is alive, but domain IDs do not match',
        'vpc_configuration_consistency_status': 'success',
        'vpc_per_vlan_consistency_status': 'success',
        'vpc_type_2_consistency_status': 'success',
        'vpc_role': 'primary',
        'num_of_vpcs': 1,
        'peer_gateway': 'Disabled',
        'dual_active_excluded_vlans': '-',
        'vpc_graceful_consistency_check_status': 'Enabled',
        'peer_link': {
            1: {
                'peer_link_id': 1,
                'peer_link_ifindex': 'Port-channel100',
                'peer_link_port_state': 'down',
                'peer_up_vlan_bitset': '-'
            }
        },
        'vpc': {
            1: {
                'vpc_id': 1,
                'vpc_ifindex': 'Port-channel1',
                'vpc_port_state': 'down',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '-'
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
         
        vPC peer-link status
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

    golden_parsed_output_6 = {
        'vpc_domain_id': 'Not configured',
        'vpc_peer_status': 'peer link not configured',
        'vpc_peer_keepalive_status': 'Disabled',
        'vpc_configuration_consistency_status': 'failed',
        'vpc_per_vlan_consistency_status': 'failed',
        'vpc_type_2_consistency_status': 'failed',
        'vpc_role': 'none established',
        'num_of_vpcs': 0,
        'peer_gateway': 'Disabled',
        'dual_active_excluded_vlans': '-',
        'vpc_graceful_consistency_check_status': 'Disabled (due to peer configuration)',
        'vpc_auto_recovery_status': 'Disabled',
        'vpc_delay_restore_status': 'Timer is off.(timeout = 30s)',
        'vpc_delay_restore_svi_status': 'Timer is off.(timeout = 10s)',
        'operational_l3_peer_router': 'Disabled'
    }

    golden_output_6 = {'execute.return_value': '''
        +++ N95_1: executing command 'show vpc' +++
        show vpc
        Legend:
                        (*) - local vPC is down, forwarding via vPC peer-link
        
        vPC domain id                     : Not configured
        Peer status                       : peer link not configured      
        vPC keep-alive status             : Disabled                      
        Configuration consistency status  : failed  
        Per-vlan consistency status       : failed                        
        Configuration inconsistency reason: vPC peer-link does not exist  
        Type-2 consistency status         : failed  
        Type-2 inconsistency reason       : vPC peer-link does not exist  
        vPC role                          : none established              
        Number of vPCs configured         : 0   
        Peer Gateway                      : Disabled
        Dual-active excluded VLANs        : -
        Graceful Consistency Check        : Disabled (due to peer configuration)
        Auto-recovery status              : Disabled
        Delay-restore status              : Timer is off.(timeout = 30s)
        Delay-restore SVI status          : Timer is off.(timeout = 10s)
        Operational Layer3 Peer-router    : Disabled
        N95_1# 
    '''}

    golden_parsed_output_7 = {
        'vpc_domain_id': 'Unknown',
        'vpc_plus_switch_id': 'Unknown',
        'vpc_peer_status': 'peer adjacency formed ok',
        'vpc_peer_keepalive_status': 'peer is alive',
        'vpc_fabricpath_status': 'peer is reachable through fabricpath',
        'vpc_configuration_consistency_status': 'success',
        'vpc_per_vlan_consistency_status': 'success',
        'vpc_type_2_consistency_status': 'success',
        'vpc_role': 'primary',
        'num_of_vpcs': 8,
        'peer_gateway': 'Disabled',
        'dual_active_excluded_vlans': '-',
        'vpc_graceful_consistency_check_status': 'Enabled',
        'vpc_auto_recovery_status': 'Enabled (timeout = 300 seconds)',
        'peer_link': {
            1: {
                'peer_link_id': 1,
                'peer_link_ifindex': 'Port-channel1',
                'peer_link_port_state': 'up',
                'peer_up_vlan_bitset': '1,2,3,4,5,6,7'
            }
        },
        'vpc': {
            11: {
                'vpc_id': 11,
                'vpc_ifindex': 'Port-channel11',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '1,2,3,4,5,6,7,8,9,10,11',
                'vpc_plus_attrib': 'DF: Partial,FP MAC:312.0.0'
            }
        }
    }

    golden_output7 = {'execute.return_value': '''
        Legend:
                        (*) - local vPC is down, forwarding via vPC peer-link
        
        vPC domain id                     : Unknown
        vPC+ switch id                    : Unknown
        Peer status                       : peer adjacency formed ok
        vPC keep-alive status             : peer is alive
        vPC fabricpath status             : peer is reachable through fabricpath
        Configuration consistency status  : success
        Per-vlan consistency status       : success
        Type-2 consistency status         : success
        vPC role                          : primary
        Number of vPCs configured         : 8
        Peer Gateway                      : Disabled
        Dual-active excluded VLANs        : -
        Graceful Consistency Check        : Enabled
        Auto-recovery status              : Enabled (timeout = 300 seconds)
        
        vPC Peer-link status
        ---------------------------------------------------------------------
        id   Port   Status Active vlans
        --   ----   ------ --------------------------------------------------
        1    Po1    up     1,2,3,4,5,6,7
        
        vPC status
        ---------------------------------------------------------------------------
        id     Port        Status Consistency Reason       Active vlans vPC+ Attrib
        --     ----------  ------ ----------- ------       ------------ -----------
        11     Po11        up     success     success      1,2,3,4,5,6, DF: Partial,
                                                           7,8,9,       FP MAC:
                                                           10,11        312.0.0
    '''
    }
    
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVpc(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowVpc(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowVpc(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowVpc(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.device = Mock(**self.golden_output_4)
        obj = ShowVpc(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_golden_5(self):
        self.device = Mock(**self.golden_output_5)
        obj = ShowVpc(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_5)

    def test_golden_6(self):
        self.device = Mock(**self.golden_output_6)
        obj = ShowVpc(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_6)

    def test_golden_7(self):
        self.device = Mock(**self.golden_output7)
        obj = ShowVpc(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_7)
        
if __name__ == '__main__':
    unittest.main()