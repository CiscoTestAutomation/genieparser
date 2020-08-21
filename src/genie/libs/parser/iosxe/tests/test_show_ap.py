import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_ap import ShowApSummary


# ===============================
# Unit test for 'show ap summary'
# ===============================
class TestShowApSummary(unittest.TestCase):
    """Unit test for 'show ap summary'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
        "ap_summary": {
            "ap_neighbor_count": 149,
            "a121-cap22": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.9b28",
                "radio_mac": "2c57.4119.a060",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.106",
                "state": "Registered"
            },
            "a132-cap15": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2244",
                "radio_mac": "2c57.4120.d2a0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.146",
                "state": "Registered"
            },
            "a112-cap11": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.22d0",
                "radio_mac": "2c57.4120.d700",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.160",
                "state": "Registered"
            },
            "a112-cap10": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2420",
                "radio_mac": "2c57.4120.b180",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.102",
                "state": "Registered"
            },
            "a112-cap17": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2434",
                "radio_mac": "2c57.4120.b220",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.203",
                "state": "Registered"
            },
            "a112-cap14": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2438",
                "radio_mac": "2c57.4120.b240",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.202",
                "state": "Registered"
            },
            "a122-cap09": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2450",
                "radio_mac": "2c57.4120.b300",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.133",
                "state": "Registered"
            },
            "a131-cap43": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2454",
                "radio_mac": "2c57.4120.b320",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.93",
                "state": "Registered"
            },
            "a122-cap08": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2458",
                "radio_mac": "2c57.4120.b340",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.166",
                "state": "Registered"
            },
            "a122-cap05": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2464",
                "radio_mac": "2c57.4120.b3a0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.117",
                "state": "Registered"
            },
            "a112-cap02": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2478",
                "radio_mac": "2c57.4120.b440",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.152",
                "state": "Registered"
            },
            "a112-cap08": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.247c",
                "radio_mac": "2c57.4120.b460",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.200",
                "state": "Registered"
            },
            "a112-cap21": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2488",
                "radio_mac": "2c57.4120.b4c0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.199",
                "state": "Registered"
            },
            "a121-cap40": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2490",
                "radio_mac": "2c57.4120.b500",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.123",
                "state": "Registered"
            },
            "a121-cap28": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24a0",
                "radio_mac": "2c57.4120.b580",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.152",
                "state": "Registered"
            },
            "a112-cap22": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24b4",
                "radio_mac": "2c57.4120.b620",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.191",
                "state": "Registered"
            },
            "a122-cap13": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24b8",
                "radio_mac": "2c57.4120.b640",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.169",
                "state": "Registered"
            },
            "a121-cap30": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24bc",
                "radio_mac": "2c57.4120.b660",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.107",
                "state": "Registered"
            },
            "a111-cap29": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24c4",
                "radio_mac": "2c57.4120.b6a0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.139",
                "state": "Registered"
            }
        }
    }


    golden_output1 = {'execute.return_value': '''
Number of APs: 149

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a121-cap22                       2      9130AXI   a4b2.3291.9b28  2c57.4119.a060  Fab A  UK          10.6.33.106                               Registered    
a132-cap15                       2      9130AXI   a4b2.3291.2244  2c57.4120.d2a0  Fab A  UK          10.6.32.146                               Registered    
a111-cap27                       2      9130AXI   a4b2.3291.225c  2c57.4120.d360  Fab A  UK          10.6.32.118.                              Registered    
a112-cap11                       2      9130AXI   a4b2.3291.22d0  2c57.4120.d700  Fab A  UK          10.6.33.160                               Registered    
a112-cap10                       2      9130AXI   a4b2.3291.2420  2c57.4120.b180  Fab A  UK          10.6.33.102                               Registered    
a112-cap17                       2      9130AXI   a4b2.3291.2434  2c57.4120.b220  Fab A  UK          10.6.32.203                               Registered    
a112-cap14                       2      9130AXI   a4b2.3291.2438  2c57.4120.b240  Fab A  UK          10.6.32.202                               Registered    
a122-cap09                       2      9130AXI   a4b2.3291.2450  2c57.4120.b300  Fab A  UK          10.6.33.133                               Registered    
a131-cap43                       2      9130AXI   a4b2.3291.2454  2c57.4120.b320  Fab A  UK          10.6.33.93                                Registered    
a122-cap08                       2      9130AXI   a4b2.3291.2458  2c57.4120.b340  Fab A  UK          10.6.32.166                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a122-cap05                       2      9130AXI   a4b2.3291.2464  2c57.4120.b3a0  Fab A  UK          10.6.33.117                               Registered    
a112-cap02                       2      9130AXI   a4b2.3291.2478  2c57.4120.b440  Fab A  UK          10.6.33.152                               Registered    
a112-cap08                       2      9130AXI   a4b2.3291.247c  2c57.4120.b460  Fab A  UK          10.6.32.200                               Registered    
a112-cap21                       2      9130AXI   a4b2.3291.2488  2c57.4120.b4c0  Fab A  UK          10.6.32.199                               Registered    
a121-cap40                       2      9130AXI   a4b2.3291.2490  2c57.4120.b500  Fab A  UK          10.6.33.123                               Registered    
a121-cap28                       2      9130AXI   a4b2.3291.24a0  2c57.4120.b580  Fab A  UK          10.6.32.152                               Registered    
a112-cap22                       2      9130AXI   a4b2.3291.24b4  2c57.4120.b620  Fab A  UK          10.6.32.191                               Registered    
a122-cap13                       2      9130AXI   a4b2.3291.24b8  2c57.4120.b640  Fab A  UK          10.6.32.169                               Registered    
a121-cap30                       2      9130AXI   a4b2.3291.24bc  2c57.4120.b660  Fab A  UK          10.6.33.107                               Registered    
a111-cap29                       2      9130AXI   a4b2.3291.24c4  2c57.4120.b6a0  Fab A  UK          10.6.33.139                               Registered    

    '''}

    def test_show_ap_summary_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowApSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ap_summary_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowApSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
