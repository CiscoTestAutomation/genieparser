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
        'vpc_domain_id': '210',
        'vpc_peer_status': 'peer adjacency formed ok',
        'vpc_peer_keepalive_status': 'peer is alive',
        'vpc_configuration_consistency_status': 'success',
        'vpc_per_vlan_consistency_status': 'success',
        'vpc_type_2_consistency_status': 'success',
        'vpc_role': 'secondary',
        'num_of_vpcs': 13,
        'peer_gateway': 'Enabled',
        'peer_gateway_exculded_vlans': '-',
        'peer_gateway_exculded_bridge_domains': '-',
        'dual_active_excluded_vlans_and_bds': '-',
        'vpc_graceful_consistency_check_status': 'Enabled',
        'vpc_auto_recovery_status': 'Enabled, timer is off.(timeout = 240s)',
        'delay_restore_orphan_ports_status': {
            'timer': 'off',
            'timeout': 0,
        },
        'operational_l3_peer_router': 'Enabled',
        'self_isolation': 'Disabled',
        'peer_link': {
            1: {
                'peer_link_id': 1,
                'peer_link_ifindex': 'Port-channel1',
                'peer_link_port_state': 'up',
                'peer_up_vlan_bitset': '1,8,17,60-62,65,67-68,92-93,110,122-123,126-127,135-137,140-144,153-154,159,191,194,251,256,301-302,304-305,344,401-402,1199',
                'vlan_bds': '-',
            },
        },
        'vpc': {
            4: {
                'vpc_id': 4,
                'vpc_ifindex': 'Port-channel4',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '65,67-68,401-402,1199',
            },
            5: {
                'vpc_id': 5,
                'vpc_ifindex': 'Port-channel5',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '65,67-68,401-402',
            },
            101: {
                'vpc_id': 101,
                'vpc_ifindex': 'Port-channel101',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '17,60-62,65,67,110,122-123,135-137,140-143,153-154,191,194,251,256,305',
            },
            102: {
                'vpc_id': 102,
                'vpc_ifindex': 'Port-channel102',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '17,60-62,65,67,110,122-123,135-137,140-143,154,191,194,251,256,305',
            },
            103: {
                'vpc_id': 103,
                'vpc_ifindex': 'Port-channel103',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '159,256,301-302,304-305,344',
            },
            104: {
                'vpc_id': 104,
                'vpc_ifindex': 'Port-channel104',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '159,301-302,304-305,344',
            },
            105: {
                'vpc_id': 105,
                'vpc_ifindex': 'Port-channel105',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '159,301-302,304-305,344',
            },
            106: {
                'vpc_id': 106,
                'vpc_ifindex': 'Port-channel106',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '17,60-62,67-68,135-137,140-143,153-154,191,194,305,401-402',
            },
            107: {
                'vpc_id': 107,
                'vpc_ifindex': 'Port-channel107',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '17,60-62,67-68,135-137,140-143,153-154,191,194,305,401-402',
            },
            1022: {
                'vpc_id': 1022,
                'vpc_ifindex': 'Port-channel1022',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '1,8,17,60-62,65,67-68,92-93,110,122-123,126-127,135-137,140-144,153-154,159,191,194,251,256,301-302,304-305,344,401-402,1199',
            },
            1023: {
                'vpc_id': 1023,
                'vpc_ifindex': 'Port-channel1023',
                'vpc_port_state': 'down*',
                'vpc_consistency': 'failed',
                'vpc_consistency_status': 'Compatibility check failed for speed',
                'up_vlan_bitset': '-',
            },
            1024: {
                'vpc_id': 1024,
                'vpc_ifindex': 'Port-channel1024',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '1,8,17,60-62,65,67-68,92-93,110,122-123,126-127,135-137,140-144,153-154,159,191,194,251,256,301-302,304-305,344,401-402,1199',
            },
            1025: {
                'vpc_id': 1025,
                'vpc_ifindex': 'Port-channel1025',
                'vpc_port_state': 'up',
                'vpc_consistency': 'success',
                'vpc_consistency_status': 'success',
                'up_vlan_bitset': '1,8,17,60-62,65,67-68,92-93,110,122-123,126-127,135-137,140-144,153-154,159,191,194,251,256,301-302,304-305,344,401-402,1199',
            },
        },
    }
    golden_output_7 = {'execute.return_value': '''
        show vpc
        Legend:
                        (*) - local vPC is down, forwarding via vPC peer-link
        
        vPC domain id                          : 210
        Peer status                            : peer adjacency formed ok
        vPC keep-alive status                  : peer is alive
        Configuration consistency status       : success
        Per-vlan consistency status            : success
        Type-2 consistency status              : success
        vPC role                               : secondary
        Number of vPCs configured              : 13
        Peer Gateway                           : Enabled
        Peer gateway excluded VLANs            : -
        Peer gateway excluded bridge-domains   : -
        Dual-active excluded VLANs and BDs     : -
        Graceful Consistency Check             : Enabled
        Auto-recovery status                   : Enabled, timer is off.(timeout = 240s)
        Delay-restore orphan ports status      : Timer is off.(timeout = 0s)
        Operational Layer3 Peer-router         : Enabled
        Self-isolation                         : Disabled
        
        vPC Peer-link status
        --------------------------------------------------------------------------------
        id   Port   Status Active vlans                   Active BDs
        --   ----   ------ -------------------------------------------------------------
        1    Po1    up     1,8,17,60-62,65,67-68,92-93,11 -
                        0,122-123,126-127,135-137,140-
                        144,153-154,159,191,194,251,25
                        6,301-302,304-305,344,401-402,
                        1199
        
        vPC status
        Id               : 4
        Port           : Po4
        Status         : up
        Consistency    : success
        Reason         : success
        Active Vlans   : 65,67-68,401-402,1199
        Id               : 5
        Port           : Po5
        Status         : up
        Consistency    : success
        Reason         : success
        Active Vlans   : 65,67-68,401-402
        Id               : 101
        Port           : Po101
        Status         : up
        Consistency    : success
        Reason         : success
        Active Vlans   : 17,60-62,65,67,110,122-123,135-137,140-143,153-154,191,194,2
                        51,256,305
        Id               : 102
        Port           : Po102
        Status         : up
        Consistency    : success
        Reason         : success
        Active Vlans   : 17,60-62,65,67,110,122-123,135-137,140-143,154,191,194,251,2
                        56,305
        Id               : 103
        Port           : Po103
        Status         : up
        Consistency    : success
        Reason         : success
        Active Vlans   : 159,256,301-302,304-305,344
        Id               : 104
        Port           : Po104
        Status         : up
        Consistency    : success
        Reason         : success
        Active Vlans   : 159,301-302,304-305,344
        Id               : 105
        Port           : Po105
        Status         : up
        Consistency    : success
        Reason         : success
        Active Vlans   : 159,301-302,304-305,344
        Id               : 106
        Port           : Po106
        Status         : up
        Consistency    : success
        Reason         : success
        Active Vlans   : 17,60-62,67-68,135-137,140-143,153-154,191,194,305,401-402
        Id               : 107
        Port           : Po107
        Status         : up
        Consistency    : success
        Reason         : success
        Active Vlans   : 17,60-62,67-68,135-137,140-143,153-154,191,194,305,401-402
        Id               : 1022
        Port           : Po1022
        Status         : up
        Consistency    : success
        Reason         : success
        Active Vlans   : 1,8,17,60-62,65,67-68,92-93,110,122-123,126-127,135-137,140-
                        144,153-154,159,191,194,251,256,301-302,304-305,344,401-402,
                        1199
        Id               : 1023
        Port           : Po1023
        Status         : down*
        Consistency    : failed
        Reason         : Compatibility check failed for speed
        Active Vlans   : -
        Id               : 1024
        Port           : Po1024
        Status         : up
        Consistency    : success
        Reason         : success
        Active Vlans   : 1,8,17,60-62,65,67-68,92-93,110,122-123,126-127,135-137,140-
                        144,153-154,159,191,194,251,256,301-302,304-305,344,401-402,
                        1199
        Id               : 1025
        Port           : Po1025
        Status         : up
        Consistency    : success
        Reason         : success
        Active Vlans   : 1,8,17,60-62,65,67-68,92-93,110,122-123,126-127,135-137,140-
                        144,153-154,159,191,194,251,256,301-302,304-305,344,401-402,
                        1199

    '''}

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

    def test_golden_6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_6)
        obj = ShowVpc(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_6)
    
    def test_golden_7(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_7)
        obj = ShowVpc(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_7)

if __name__ == '__main__':
    unittest.main()