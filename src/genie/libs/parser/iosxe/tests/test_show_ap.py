import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
<<<<<<< HEAD
from genie.libs.parser.iosxe.show_ap import ShowApLedBrightnessLevelSummary


# ====================================================
# Unit test for 'show ap led-brightness-level summary'
# ====================================================
class TestShowApLedBrightnessLevelSummary(unittest.TestCase):
    """Unit test for 'show ap led-brightness-level summary'"""
=======
from genie.libs.parser.iosxe.show_ap import ShowApRfProfileSummary


# ==========================================
# Unit test for 'show ap rf-profile summary'
# ==========================================
class TestShowApRfProfileSummary(unittest.TestCase):
    """Unit test for 'show ap rf-profile summary'"""
>>>>>>> master

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
<<<<<<< HEAD
        "ap_name": {
            "b881-cap4": {
                "led_brightness_level": 8
            },
            "b852-cap6": {
                "led_brightness_level": 8
            },
            "b861-cap14": {
                "led_brightness_level": 8
            },
            "b822-cap10": {
                "led_brightness_level": 8
            },
            "b871-cap1": {
                "led_brightness_level": 8
            },
            "b861-cap7": {
                "led_brightness_level": 8
            },
            "b852-cap18": {
                "led_brightness_level": 8
            },
            "b871-cap3": {
                "led_brightness_level": 8
            },
            "b862-cap2": {
                "led_brightness_level": 8
            },
            "b801-cap16": {
                "led_brightness_level": 8
            },
            "b832-cap3": {
                "led_brightness_level": 8
            },
            "b802-cap4": {
                "led_brightness_level": 8
            },
            "b862-cap5": {
                "led_brightness_level": 8
            },
            "b851-cap9": {
                "led_brightness_level": 8
            },
            "b802-cap8": {
                "led_brightness_level": 8
            },
            "b822-cap14": {
                "led_brightness_level": 8
            },
            "b872-cap8": {
                "led_brightness_level": 8
            },
            "b872-cap6": {
                "led_brightness_level": 8
            },
            "b862-cap18": {
                "led_brightness_level": 8
            },
            "b822-cap16": {
                "led_brightness_level": 8
=======
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
>>>>>>> master
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
<<<<<<< HEAD
    AP Name                           LED Brightness level    
    --------------------------------------------------------
    b881-cap4                     8                       
    b852-cap6                     8                       
    b861-cap14                    8                       
    b822-cap10                    8                       
    b871-cap1                     8                       
    b861-cap7                     8                       
    b852-cap18                    8                       
    b871-cap3                     8                       
    b862-cap2                     8                       
    b801-cap16                    8                       
    
    AP Name                           LED Brightness level    
    --------------------------------------------------------
    b832-cap3                     8                       
    b802-cap4                     8                       
    b862-cap5                     8                       
    b851-cap9                     8                       
    b802-cap8                     8                       
    b822-cap14                    8                       
    b872-cap8                     8                       
    b872-cap6                     8                       
    b862-cap18                    8                       
    b822-cap16                    8        
    '''}

    def test_show_ap_led_brightness_level_summary_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowApLedBrightnessLevelSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ap_led_brightness_level_summary_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowApLedBrightnessLevelSummary(device=self.device)
=======
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
>>>>>>> master
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
