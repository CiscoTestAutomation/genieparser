import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_ap import ShowApLedBrightnessLevelSummary


# ====================================================
# Unit test for 'show ap led-brightness-level summary'
# ====================================================
class TestShowApLedBrightnessLevelSummary(unittest.TestCase):
    """Unit test for 'show ap led-brightness-level summary'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
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
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
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
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
