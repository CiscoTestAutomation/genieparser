import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
<<<<<<< HEAD
from genie.libs.parser.iosxe.show_ap import ShowApRfProfileSummary


# ==========================================
# Unit test for 'show ap rf-profile summary'
# ==========================================
class TestShowApRfProfileSummary(unittest.TestCase):
    """Unit test for 'show ap rf-profile summary'"""
=======
from genie.libs.parser.iosxe.show_ap import ShowApCdpNeighbor


# ====================================
# Unit test for 'show ap cdp neighbor'
# ====================================
class TestShowApCdpNeighbor(unittest.TestCase):
    """Unit test for 'show ap cdp neighbor'"""
>>>>>>> iosxe/show_ap_cdp_neighbor

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
<<<<<<< HEAD
        "rf_profile_summary": {
            "rf_profile_count": 14,
            "rf_profiles": {
                "Custom-RF_a": {
                    "rf_profile_name": "Custom-RF_a",
                    "band": "5 GHz",
                    "description": "Custom-RF_a_Desc",
                    "state": "Up"
                },
                "Custom-RF_b": {
                    "rf_profile_name": "Custom-RF_b",
                    "band": "2.4 GHz",
                    "description": "Custom-RF_b_Desc",
                    "state": "Up"
                },
                "Low_Client_Density_rf_5gh": {
                    "rf_profile_name": "Low_Client_Density_rf_5gh",
                    "band": "5 GHz",
                    "description": "pre configured Low Client Density rf",
                    "state": "Up"
                },
                "High_Client_Density_rf_5gh": {
                    "rf_profile_name": "High_Client_Density_rf_5gh",
                    "band": "5 GHz",
                    "description": "pre configured High Client Density r",
                    "state": "Up"
                },
                "Low-Client-Density-802.11a": {
                    "rf_profile_name": "Low-Client-Density-802.11a",
                    "band": "5 GHz",
                    "description": "",
                    "state": "Up"
                },
                "Low_Client_Density_rf_24gh": {
                    "rf_profile_name": "Low_Client_Density_rf_24gh",
                    "band": "2.4 GHz",
                    "description": "pre configured Low Client Density rf",
                    "state": "Up"
                },
                "High-Client-Density-802.11a": {
                    "rf_profile_name": "High-Client-Density-802.11a",
                    "band": "5 GHz",
                    "description": "",
                    "state": "Up"
                },
                "High_Client_Density_rf_24gh": {
                    "rf_profile_name": "High_Client_Density_rf_24gh",
                    "band": "2.4 GHz",
                    "description": "pre configured High Client Density r",
                    "state": "Up"
                },
                "Low-Client-Density-802.11bg": {
                    "rf_profile_name": "Low-Client-Density-802.11bg",
                    "band": "2.4 GHz",
                    "description": "",
                    "state": "Up"
                },
                "High-Client-Density-802.11bg": {
                    "rf_profile_name": "High-Client-Density-802.11bg",
                    "band": "2.4 GHz",
                    "description": "",
                    "state": "Up"
                },
                "Typical_Client_Density_rf_5gh": {
                    "rf_profile_name": "Typical_Client_Density_rf_5gh",
                    "band": "5 GHz",
                    "description": "pre configured Typical Density rfpro",
                    "state": "Up"
                },
                "Typical-Client-Density-802.11a": {
                    "rf_profile_name": "Typical-Client-Density-802.11a",
                    "band": "5 GHz",
                    "description": "",
                    "state": "Up"
                },
                "Typical_Client_Density_rf_24gh": {
                    "rf_profile_name": "Typical_Client_Density_rf_24gh",
                    "band": "2.4 GHz",
                    "description": "pre configured Typical Client Densit",
                    "state": "Up"
                },
                "Typical-Client-Density-802.11bg": {
                    "rf_profile_name": "Typical-Client-Density-802.11bg",
                    "band": "2.4 GHz",
                    "description": "",
                    "state": "Up"
                }
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
Number of RF-profiles: 14

RF Profile Name                  Band     Description                          State 
------------------------------------------------------------------------------------
Custom-RF_a                      5 GHz    Custom-RF_a_Desc                     Up    
Custom-RF_b                      2.4 GHz  Custom-RF_b_Desc                     Up    
Low_Client_Density_rf_5gh        5 GHz    pre configured Low Client Density rf Up    
High_Client_Density_rf_5gh       5 GHz    pre configured High Client Density r Up    
Low-Client-Density-802.11a       5 GHz                                         Up    
Low_Client_Density_rf_24gh       2.4 GHz  pre configured Low Client Density rf Up    
High-Client-Density-802.11a      5 GHz                                         Up    
High_Client_Density_rf_24gh      2.4 GHz  pre configured High Client Density r Up    
Low-Client-Density-802.11bg      2.4 GHz                                       Up    
High-Client-Density-802.11bg     2.4 GHz                                       Up    
Typical_Client_Density_rf_5gh    5 GHz    pre configured Typical Density rfpro Up    
Typical-Client-Density-802.11a   5 GHz                                         Up    
Typical_Client_Density_rf_24gh   2.4 GHz  pre configured Typical Client Densit Up    
Typical-Client-Density-802.11bg  2.4 GHz                                       Up    

=========================
Number of RF-profiles: 14 
    '''}

    def test_show_ap_rf_profile_summary_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowApRfProfileSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ap_rf_profile_summary_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowApRfProfileSummary(device=self.device)
=======
    "ap_cdp_neighbor_count": 149,
    "ap_name": {
        "0221-cap22": {
            "ap_ip": "10.8.33.106",
            "neighbor_name": "a02-21-sd-sw1.cisco.com",
            "neighbor_port": "TenGigabitEthernet3/0/47",
            "neighbor_ip_count": 1,
            "neighbor_ip_addresses": {
                1: "10.8.32.1"
            }
        },
        "0232-cap15": {
            "ap_ip": "10.8.32.46",
            "neighbor_name": "a02-32-sd-sw1.cisco.com",
            "neighbor_port": "TenGigabitEthernet9/0/47",
            "neighbor_ip_count": 1,
            "neighbor_ip_addresses": {
                1: "10.8.32.1"
            }
        },
        "0211-cap27": {
            "ap_ip": "10.8.32.188",
            "neighbor_name": "a02-11-sd-sw1.cisco.com",
            "neighbor_port": "TenGigabitEthernet4/0/46",
            "neighbor_ip_count": 1,
            "neighbor_ip_addresses": {
                1: "10.8.32.1"
            }
        },
        "0212-cap11": {
            "ap_ip": "10.8.33.160",
            "neighbor_name": "a02-12-sd-sw2.cisco.com",
            "neighbor_port": "TenGigabitEthernet1/0/40",
            "neighbor_ip_count": 1,
            "neighbor_ip_addresses": {
                1: "10.8.32.1"
            }
        },
        "0212-cap10": {
            "ap_ip": "10.8.33.102",
            "neighbor_name": "a02-12-sd-sw1.cisco.com",
            "neighbor_port": "TenGigabitEthernet1/0/43",
            "neighbor_ip_count": 1,
            "neighbor_ip_addresses": {
                1: "10.8.32.1"
            }
        },
        "0212-cap17": {
            "ap_ip": "10.8.32.203",
            "neighbor_name": "a02-12-sd-sw2.cisco.com",
            "neighbor_port": "TenGigabitEthernet1/0/47",
            "neighbor_ip_count": 1,
            "neighbor_ip_addresses": {
                1: "10.8.32.1"
            }
        },
        "0212-ca.4": {
            "ap_ip": "10.8.32.202",
            "neighbor_name": "a02-12-sd-sw1.cisco.com",
            "neighbor_port": "TenGigabitEthernet1/0/48",
            "neighbor_ip_count": 1,
            "neighbor_ip_addresses": {
                1: "10.8.32.1"
            }
        },
        "0222-cap09": {
            "ap_ip": "10.8.33.33",
            "neighbor_name": "a02-22-sd-sw2.cisco.com",
            "neighbor_port": "TenGigabitEthernet8/0/48",
            "neighbor_ip_count": 1,
            "neighbor_ip_addresses": {
                1: "10.8.32.1"
            }
        },
        "0231-cap43": {
            "ap_ip": "10.8.33.93",
            "neighbor_name": "a02-31-sd-sw1.cisco.com",
            "neighbor_port": "TenGigabitEthernet4/0/47",
            "neighbor_ip_count": 1,
            "neighbor_ip_addresses": {
                1: "10.8.32.1"
            }
        },
        "0222-cap08": {
            "ap_ip": "10.8.32.166",
            "neighbor_name": "a02-22-sd-sw2.cisco.com",
            "neighbor_port": "TenGigabitEthernet4/0/47",
            "neighbor_ip_count": 1,
            "neighbor_ip_addresses": {
                1: "10.8.32.1"
            }
        }
    }
}

    golden_output1 = {'execute.return_value': '''
    Number of neighbors: 149

    AP Name                          AP IP                                     Neighbor Name      Neighbor Port
    -------------------------------------------------------------------------------------------------------------
    0221-cap22                   10.8.33.106                              a02-21-sd-sw1.cisco.com TenGigabitEthernet3/0/47  
    
    Neighbor IP Count: 1
    10.8.32.1                      
    0232-cap15                   10.8.32.46                              a02-32-sd-sw1.cisco.com TenGigabitEthernet9/0/47  
    
    Neighbor IP Count: 1
    10.8.32.1                      
    
    0211-cap27                   10.8.32.188                              a02-11-sd-sw1.cisco.com TenGigabitEthernet4/0/46  
    
    Neighbor IP Count: 1
    10.8.32.1                      
    
    0212-cap11                   10.8.33.160                              a02-12-sd-sw2.cisco.com TenGigabitEthernet1/0/40  
    
    Neighbor IP Count: 1
    10.8.32.1                      
    
    0212-cap10                   10.8.33.102                              a02-12-sd-sw1.cisco.com TenGigabitEthernet1/0/43  
    
    Neighbor IP Count: 1
    10.8.32.1                      
    
    0212-cap17                   10.8.32.203                              a02-12-sd-sw2.cisco.com TenGigabitEthernet1/0/47  
    
    Neighbor IP Count: 1
    10.8.32.1                      
    
    0212-ca.4                   10.8.32.202                              a02-12-sd-sw1.cisco.com TenGigabitEthernet1/0/48  
    
    Neighbor IP Count: 1
    10.8.32.1                      
    
    0222-cap09                   10.8.33.33                              a02-22-sd-sw2.cisco.com TenGigabitEthernet8/0/48  
    
    Neighbor IP Count: 1
    10.8.32.1                      
    
    0231-cap43                   10.8.33.93                               a02-31-sd-sw1.cisco.com TenGigabitEthernet4/0/47  
    
    Neighbor IP Count: 1
    10.8.32.1                      
    
    0222-cap08                   10.8.32.166                              a02-22-sd-sw2.cisco.com TenGigabitEthernet4/0/47  
    
    Neighbor IP Count: 1
    10.8.32.1                      
    '''}

    def test_show_ap_cdp_neighbor_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowApCdpNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ap_cdp_neighbor_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowApCdpNeighbor(device=self.device)
>>>>>>> iosxe/show_ap_cdp_neighbor
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
