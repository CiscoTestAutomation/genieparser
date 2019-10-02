import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.ios.cat6k.show_platform import ShowModule


class test_show_module(unittest.TestCase):
    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "slot": {
            "1": {
                "rp": {
                    "card_type": "Catalyst 6000 supervisor 2 (Active)",
                    "fw_ver": "6.1(3)",
                    "hw_ver": "3.9",
                    "mac_address_from": "0001.6416.0342",
                    "mac_address_to": "0001.6416.0343",
                    "model": "WS-X6K-S2U-MSFC2",
                    "ports": 2,
                    "serial_number": "SAD0628035C",
                    "status": "Ok",
                    "subslot": {
                        "WS-F6K-MSFC2": {
                            "hw_ver": "2.5",
                            "model": "WS-F6K-MSFC2",
                            "serial_number": "SAD062803TX",
                            "status": "Ok",
                        },
                        "WS-F6K-PFC2": {
                            "hw_ver": "3.2",
                            "model": "WS-F6K-PFC2",
                            "serial_number": "SAD062802AV",
                            "status": "Ok",
                        },
                    },
                    "sw_ver": "7.5(0.6)HUB9",
                }
            },
            "2": {
                "rp": {
                    "card_type": "Supervisor-Other",
                    "fw_ver": "Unknown",
                    "hw_ver": "0.0",
                    "mac_address_from": "0000.0000.0000",
                    "mac_address_to": "0000.0000.0000",
                    "model": "unknown",
                    "ports": 0,
                    "serial_number": "unknown",
                    "status": "Unknown",
                    "sw_ver": "Unknown",
                }
            },
            "3": {
                "lc": {
                    "card_type": "Pure SFM-mode 16 port 1000mb GBIC",
                    "fw_ver": "12.1(5r)E1",
                    "hw_ver": "1.3",
                    "mac_address_from": "0005.7485.9518",
                    "mac_address_to": "0005.7485.9527",
                    "model": "WS-X6816-GBIC",
                    "ports": 16,
                    "serial_number": "SAL061218K3",
                    "status": "Ok",
                    "subslot": {
                        "WS-F6K-DFC": {
                            "hw_ver": "2.1",
                            "model": "WS-F6K-DFC",
                            "serial_number": "SAL06121A19",
                            "status": "Ok",
                        }
                    },
                    "sw_ver": "12.1(13)E3",
                }
            },
            "4": {
                "lc": {
                    "card_type": "Pure SFM-mode 16 port 1000mb GBIC",
                    "fw_ver": "12.1(5r)E1",
                    "hw_ver": "1.3",
                    "mac_address_from": "0005.7485.9548",
                    "mac_address_to": "0005.7485.9557",
                    "model": "WS-X6816-GBIC",
                    "ports": 16,
                    "serial_number": "SAL061218K8",
                    "status": "Ok",
                    "subslot": {
                        "WS-F6K-DFC": {
                            "hw_ver": "2.1",
                            "model": "WS-F6K-DFC",
                            "serial_number": "SAL06121A46",
                            "status": "Ok",
                        }
                    },
                    "sw_ver": "12.1(13)E3",
                }
            },
            "5": {
                "other": {
                    "card_type": "Switching Fabric Module-136 (Active)",
                    "fw_ver": "6.1(3)",
                    "hw_ver": "1.2",
                    "mac_address_from": "0001.0002.0003",
                    "mac_address_to": "0001.0002.0003",
                    "model": "WS-X6500-SFM2",
                    "ports": 0,
                    "serial_number": "SAD061701YC",
                    "status": "Ok",
                    "sw_ver": "7.5(0.6)HUB9",
                }
            },
            "6": {
                "lc": {
                    "card_type": "1 port 10-Gigabit Ethernet Module",
                    "fw_ver": "6.3(1)",
                    "hw_ver": "1.0",
                    "mac_address_from": "0002.7ec2.95f2",
                    "mac_address_to": "0002.7ec2.95f2",
                    "model": "WS-X6502-10GE",
                    "ports": 1,
                    "serial_number": "SAD062003CM",
                    "status": "Ok",
                    "subslot": {
                        "WS-F6K-DFC": {
                            "hw_ver": "2.3",
                            "model": "WS-F6K-DFC",
                            "serial_number": "SAL06261R0A",
                            "status": "Ok",
                        },
                        "WS-G6488": {
                            "hw_ver": "1.1",
                            "model": "WS-G6488",
                            "serial_number": "SAD062201BN",
                            "status": "Ok",
                        },
                    },
                    "sw_ver": "7.5(0.6)HUB9",
                }
            },
        }
    }

    golden_output_1 = {
        "execute.return_value": """
        Mod Ports Card Type                              Model              Serial No.
        --- ----- -------------------------------------- ------------------ -----------
          1    2  Catalyst 6000 supervisor 2 (Active)    WS-X6K-S2U-MSFC2   SAD0628035C
          2    0  Supervisor-Other                       unknown            unknown
          3   16  Pure SFM-mode 16 port 1000mb GBIC      WS-X6816-GBIC      SAL061218K3
          4   16  Pure SFM-mode 16 port 1000mb GBIC      WS-X6816-GBIC      SAL061218K8
          5    0  Switching Fabric Module-136 (Active)   WS-X6500-SFM2      SAD061701YC
          6    1  1 port 10-Gigabit Ethernet Module      WS-X6502-10GE      SAD062003CM

        Mod MAC addresses                       Hw    Fw           Sw           Status
        --- ---------------------------------- ------ ------------ ------------ -------
          1  0001.6416.0342 to 0001.6416.0343   3.9   6.1(3)       7.5(0.6)HUB9 Ok      
          2  0000.0000.0000 to 0000.0000.0000   0.0   Unknown      Unknown      Unknown 
          3  0005.7485.9518 to 0005.7485.9527   1.3   12.1(5r)E1   12.1(13)E3,  Ok      
          4  0005.7485.9548 to 0005.7485.9557   1.3   12.1(5r)E1   12.1(13)E3,  Ok      
          5  0001.0002.0003 to 0001.0002.0003   1.2   6.1(3)       7.5(0.6)HUB9 Ok      
          6  0002.7ec2.95f2 to 0002.7ec2.95f2   1.0   6.3(1)       7.5(0.6)HUB9 Ok      

        Mod Sub-Module                  Model           Serial           Hw     Status 
        --- --------------------------- --------------- --------------- ------- -------
          1 Policy Feature Card 2       WS-F6K-PFC2     SAD062802AV      3.2    Ok     
          1 Cat6k MSFC 2 daughterboard  WS-F6K-MSFC2    SAD062803TX      2.5    Ok     
          3 Distributed Forwarding Card WS-F6K-DFC      SAL06121A19      2.1    Ok     
          4 Distributed Forwarding Card WS-F6K-DFC      SAL06121A46      2.1    Ok     
          6 Distributed Forwarding Card WS-F6K-DFC      SAL06261R0A      2.3    Ok     
          6 10GBASE-LR Serial 1310nm lo WS-G6488        SAD062201BN      1.1    Ok
    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowModule(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_module_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowModule(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == "__main__":
    unittest.main()
