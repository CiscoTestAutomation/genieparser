# Import the Python mock functionality
import unittest
from unittest.mock import Mock

# pyATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_device_tracking
from genie.libs.parser.iosxe.show_device_tracking import ShowDeviceTrackingDatabase

# =================================
# Unit test for 'show_device_tracking'
# =================================
class test_show_device_tracking(unittest.TestCase):

    '''Unit test for "show_device_tracking"'''

    empty_output = {'execute.return_value': ''}

    # Specify the expected result for the parsed output
    golden_parsed_output1 = {
        "binding_table_count": 10,
        "dynamic_entry_count": 0,
        "binding_table_limit": 200000,
        "device": {
            1: {
                "dev_code": "L",
                "network_layer_address": "10.22.66.10",
                "link_layer_address": "7081.05ff.eb40",
                "interface": "Vl230",
                "vlan_id": 230,
                "pref_level_code": 100,
                "age": "10194mn",
                "state": "REACHABLE"
            },
            2: {
                "dev_code": "L",
                "network_layer_address": "10.22.28.10",
                "link_layer_address": "7081.05ff.eb40",
                "interface": "Vl238",
                "vlan_id": 238,
                "pref_level_code": 100,
                "age": "10255mn",
                "state": "REACHABLE"
            },
            3: {
                "dev_code": "L",
                "network_layer_address": "10.22.24.10",
                "link_layer_address": "7081.05ff.eb40",
                "interface": "Vl236",
                "vlan_id": 236,
                "pref_level_code": 100,
                "age": "10330mn",
                "state": "REACHABLE"
            },
            4: {
                "dev_code": "L",
                "network_layer_address": "10.22.20.10",
                "link_layer_address": "7081.05ff.eb40",
                "interface": "Vl234",
                "vlan_id": 234,
                "pref_level_code": 100,
                "age": "10329mn",
                "state": "REACHABLE"
            },
            5: {
                "dev_code": "L",
                "network_layer_address": "10.22.16.10",
                "link_layer_address": "7081.05ff.eb40",
                "interface": "Vl232",
                "vlan_id": 232,
                "pref_level_code": 100,
                "age": "10330mn",
                "state": "REACHABLE"
            },
            6: {
                "dev_code": "L",
                "network_layer_address": "10.22.12.10",
                "link_layer_address": "7081.05ff.eb40",
                "interface": "Vl228",
                "vlan_id": 228,
                "pref_level_code": 100,
                "age": "10330mn",
                "state": "REACHABLE"
            },
            7: {
                "dev_code": "L",
                "network_layer_address": "10.22.8.10",
                "link_layer_address": "7081.05ff.eb40",
                "interface": "Vl226",
                "vlan_id": 226,
                "pref_level_code": 100,
                "age": "10329mn",
                "state": "REACHABLE"
            },
            8: {
                "dev_code": "L",
                "network_layer_address": "10.22.4.10",
                "link_layer_address": "7081.05ff.eb40",
                "interface": "Vl224",
                "vlan_id": 224,
                "pref_level_code": 100,
                "age": "10329mn",
                "state": "REACHABLE"
            },
            9: {
                "dev_code": "L",
                "network_layer_address": "10.22.0.10",
                "link_layer_address": "7081.05ff.eb40",
                "interface": "Vl222",
                "vlan_id": 222,
                "pref_level_code": 100,
                "age": "10329mn",
                "state": "REACHABLE"
            },
            10: {
                "dev_code": "L",
                "network_layer_address": "10.10.68.10",
                "link_layer_address": "7081.05ff.eb40",
                "interface": "Vl243",
                "vlan_id": 243,
                "pref_level_code": 100,
                "age": "10330mn",
                "state": "REACHABLE"
            },
            11:{
                "dev_code": "DH4",
                "network_layer_address": "10.160.43.197",
                "link_layer_address": "94d4.69ff.e606",
                "interface": "Te8/0/37",
                "vlan_id": 1023,
                "pref_level_code": 25,
                "age": "116s",
                "state": "REACHABLE",
                "time_left": "191 s try 0(557967 s)"
            }
        }
    }

    # Specify the expected unparsed output
    golden_output1 = {'execute.return_value': '''
        Binding Table has 10 entries, 0 dynamic (limit 200000)
        Codes: L - Local, S - Static, ND - Neighbor Discovery, ARP - Address Resolution Protocol, DH4 - IPv4 DHCP, DH6 - IPv6 DHCP, PKT - Other Packet, API - API created
        Preflevel flags (prlvl):
        0001:MAC and LLA match     0002:Orig trunk            0004:Orig access           
        0008:Orig trusted trunk    0010:Orig trusted access   0020:DHCP assigned         
        0040:Cga authenticated     0080:Cert authenticated    0100:Statically assigned   


            Network Layer Address                   Link Layer Address Interface  vlan  prlvl age    state     Time left        
        L   10.22.66.10                            7081.05ff.eb40     Vl230      230   0100  10194mn REACHABLE                 
        L   10.22.28.10                            7081.05ff.eb40     Vl238      238   0100  10255mn REACHABLE                 
        L   10.22.24.10                            7081.05ff.eb40     Vl236      236   0100  10330mn REACHABLE                 
        L   10.22.20.10                            7081.05ff.eb40     Vl234      234   0100  10329mn REACHABLE                 
        L   10.22.16.10                            7081.05ff.eb40     Vl232      232   0100  10330mn REACHABLE                 
        L   10.22.12.10                            7081.05ff.eb40     Vl228      228   0100  10330mn REACHABLE                 
        L   10.22.8.10                             7081.05ff.eb40     Vl226      226   0100  10329mn REACHABLE                 
        L   10.22.4.10                             7081.05ff.eb40     Vl224      224   0100  10329mn REACHABLE                 
        L   10.22.0.10                             7081.05ff.eb40     Vl222      222   0100  10329mn REACHABLE                 
        L   10.10.68.10                            7081.05ff.eb40     Vl243      243   0100  10330mn REACHABLE
        DH4 10.160.43.197                          94d4.69ff.e606  Te8/0/37      1023  0025  116s    REACHABLE  191 s try 0(557967 s)   
    '''}

    def test_show_device_tracking_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowDeviceTrackingDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_show_device_tracking_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowDeviceTrackingDatabase(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()