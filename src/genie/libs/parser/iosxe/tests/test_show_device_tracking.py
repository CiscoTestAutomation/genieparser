import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_device_tracking import ShowDeviceTrackingDatabase


# =============================================
# Unit test for 'show device-tracking database'
# =============================================
class TestShowDeviceTrackingDatabase(unittest.TestCase):
    """Unit test for 'show device-tracking database'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
        "binding_table_count": 10,
        "dynamic_entry_count": 0,
        "binding_table_limit": 200000,
        "device": {
            1: {
                "dev_code": "L",
                "network_layer_address": "10.22.66.10",
                "link_layer_address": "7081.0535.b60b",
                "interface": "Vl230",
                "vlan_id": 230,
                "pref_level_code": 100,
                "age": "10194mn",
                "state": "REACHABLE"
            },
            2: {
                "dev_code": "L",
                "network_layer_address": "10.22.28.10",
                "link_layer_address": "7081.0535.b60b",
                "interface": "Vl238",
                "vlan_id": 238,
                "pref_level_code": 100,
                "age": "10255mn",
                "state": "REACHABLE"
            },
            3: {
                "dev_code": "L",
                "network_layer_address": "10.22.24.10",
                "link_layer_address": "7081.0535.b60b",
                "interface": "Vl236",
                "vlan_id": 236,
                "pref_level_code": 100,
                "age": "10330mn",
                "state": "REACHABLE"
            },
            4: {
                "dev_code": "L",
                "network_layer_address": "10.22.20.10",
                "link_layer_address": "7081.0535.b60b",
                "interface": "Vl234",
                "vlan_id": 234,
                "pref_level_code": 100,
                "age": "10329mn",
                "state": "REACHABLE"
            },
            5: {
                "dev_code": "L",
                "network_layer_address": "10.22.16.10",
                "link_layer_address": "7081.0535.b60b",
                "interface": "Vl232",
                "vlan_id": 232,
                "pref_level_code": 100,
                "age": "10330mn",
                "state": "REACHABLE"
            },
            6: {
                "dev_code": "L",
                "network_layer_address": "10.22.12.10",
                "link_layer_address": "7081.0535.b60b",
                "interface": "Vl228",
                "vlan_id": 228,
                "pref_level_code": 100,
                "age": "10330mn",
                "state": "REACHABLE"
            },
            7: {
                "dev_code": "L",
                "network_layer_address": "10.22.8.10",
                "link_layer_address": "7081.0535.b60b",
                "interface": "Vl226",
                "vlan_id": 226,
                "pref_level_code": 100,
                "age": "10329mn",
                "state": "REACHABLE"
            },
            8: {
                "dev_code": "L",
                "network_layer_address": "10.22.4.10",
                "link_layer_address": "7081.0535.b60b",
                "interface": "Vl224",
                "vlan_id": 224,
                "pref_level_code": 100,
                "age": "10329mn",
                "state": "REACHABLE"
            },
            9: {
                "dev_code": "L",
                "network_layer_address": "10.22.0.10",
                "link_layer_address": "7081.0535.b60b",
                "interface": "Vl222",
                "vlan_id": 222,
                "pref_level_code": 100,
                "age": "10329mn",
                "state": "REACHABLE"
            },
            10: {
                "dev_code": "L",
                "network_layer_address": "10.10.68.10",
                "link_layer_address": "7081.0535.b60b",
                "interface": "Vl243",
                "vlan_id": 243,
                "pref_level_code": 100,
                "age": "10330mn",
                "state": "REACHABLE"
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
    Binding Table has 10 entries, 0 dynamic (limit 200000)
    Codes: L - Local, S - Static, ND - Neighbor Discovery, ARP - Address Resolution Protocol, DH4 - IPv4 DHCP, DH6 - IPv6 DHCP, PKT - Other Packet, API - API created
    Preflevel flags (prlvl):
    0001:MAC and LLA match     0002:Orig trunk            0004:Orig access           
    0008:Orig trusted trunk    0010:Orig trusted access   0020:DHCP assigned         
    0040:Cga authenticated     0080:Cert authenticated    0100:Statically assigned   
    
    
        Network Layer Address                   Link Layer Address Interface  vlan  prlvl age    state     Time left        
    L   10.22.66.10                            7081.0535.b60b     Vl230      230   0100  10194mn REACHABLE                 
    L   10.22.28.10                            7081.0535.b60b     Vl238      238   0100  10255mn REACHABLE                 
    L   10.22.24.10                            7081.0535.b60b     Vl236      236   0100  10330mn REACHABLE                 
    L   10.22.20.10                            7081.0535.b60b     Vl234      234   0100  10329mn REACHABLE                 
    L   10.22.16.10                            7081.0535.b60b     Vl232      232   0100  10330mn REACHABLE                 
    L   10.22.12.10                            7081.0535.b60b     Vl228      228   0100  10330mn REACHABLE                 
    L   10.22.8.10                             7081.0535.b60b     Vl226      226   0100  10329mn REACHABLE                 
    L   10.22.4.10                             7081.0535.b60b     Vl224      224   0100  10329mn REACHABLE                 
    L   10.22.0.10                             7081.0535.b60b     Vl222      222   0100  10329mn REACHABLE                 
    L   10.10.68.10                            7081.0535.b60b     Vl243      243   0100  10330mn REACHABLE   
    
    '''}

    def test_show_device_tracking_database_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowDeviceTrackingDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_device_tracking_database_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowDeviceTrackingDatabase(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
