# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.nxos.show_vdc import ShowVdcResourceDetail


# =====================================
#  Unit test for 'show vdc resource detail'
#  Unit test for 'show vdc resource {resource} detail'
# =====================================
class TestShowVdcResourceDetail(unittest.TestCase):
    '''unit test for
        * show vdc resource detail
        * show vdc resource {resource} detail
    '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "resources": {
            "m4route-mem": {
                "total": 400,
                "total_avail": 342,
                "total_free": 399,
                "total_unused": 57,
                "total_used": 1,
                "vdcs": {
                    "example.cisco.com": {
                        "free": 57,
                        "max": 58,
                        "min": 58,
                        "unused": 57,
                        "used": 1,
                    }
                },
            },
            "m6route-mem": {
                "total": 80,
                "total_avail": 72,
                "total_free": 79,
                "total_unused": 7,
                "total_used": 1,
                "vdcs": {
                    "example.cisco.com": {
                        "free": 7,
                        "max": 8,
                        "min": 8,
                        "unused": 7,
                        "used": 1,
                    }
                },
            },
            "port-channel": {
                "total": 511,
                "total_avail": 509,
                "total_free": 509,
                "total_unused": 0,
                "total_used": 2,
                "vdcs": {
                    "example.cisco.com": {
                        "free": 509,
                        "max": 511,
                        "min": 0,
                        "unused": 0,
                        "used": 2,
                    }
                },
            },
            "u4route-mem": {
                "total": 1536,
                "total_avail": 1288,
                "total_free": 1535,
                "total_unused": 247,
                "total_used": 1,
                "vdcs": {
                    "example.cisco.com": {
                        "free": 247,
                        "max": 248,
                        "min": 248,
                        "unused": 247,
                        "used": 1,
                    }
                },
            },
            "u6route-mem": {
                "total": 640,
                "total_avail": 544,
                "total_free": 639,
                "total_unused": 95,
                "total_used": 1,
                "vdcs": {
                    "example.cisco.com": {
                        "free": 95,
                        "max": 96,
                        "min": 96,
                        "unused": 95,
                        "used": 1,
                    }
                },
            },
            "vlan": {
                "total": 4094,
                "total_avail": 3672,
                "total_free": 3672,
                "total_unused": 0,
                "total_used": 422,
                "vdcs": {
                    "example.cisco.com": {
                        "free": 3672,
                        "max": 4094,
                        "min": 16,
                        "unused": 0,
                        "used": 422,
                    }
                },
            },
            "vni_bd": {
                "total": 4096,
                "total_avail": 0,
                "total_free": 4096,
                "total_unused": 4096,
                "total_used": 0,
                "vdcs": {
                    "example.cisco.com": {
                        "free": 4096,
                        "max": 4096,
                        "min": 4096,
                        "unused": 4096,
                        "used": 0,
                    }
                },
            },
            "vrf": {
                "total": 4096,
                "total_avail": 4094,
                "total_free": 4094,
                "total_unused": 0,
                "total_used": 2,
                "vdcs": {
                    "example.cisco.com": {
                        "free": 4094,
                        "max": 4096,
                        "min": 2,
                        "unused": 0,
                        "used": 2,
                    }
                },
            },
        }
    }

    golden_output = {'execute.return_value': '''
  vlan               422 used     0 unused   3672 free   3672 avail   4094 total
 ------
          Vdc                              Min       Max       Used      Unused    Avail
          ---                              ---       ---       ----      ------    -----
          example.cisco.com                 16        4094      422       0         3672

  vrf                  2 used     0 unused   4094 free   4094 avail   4096 total
 -----
          Vdc                              Min       Max       Used      Unused    Avail
          ---                              ---       ---       ----      ------    -----
          example.cisco.com                 2         4096      2         0         4094

  port-channel         2 used     0 unused    509 free    509 avail    511 total
 --------------
          Vdc                              Min       Max       Used      Unused    Avail
          ---                              ---       ---       ----      ------    -----
          example.cisco.com                 0         511       2         0         509

  u4route-mem          1 used   247 unused   1535 free   1288 avail   1536 total
 -------------
          Vdc                              Min       Max       Used      Unused    Avail
          ---                              ---       ---       ----      ------    -----
          example.cisco.com                 248       248       1         247       247

  u6route-mem          1 used    95 unused    639 free    544 avail    640 total
 -------------
          Vdc                              Min       Max       Used      Unused    Avail
          ---                              ---       ---       ----      ------    -----
          example.cisco.com                 96        96        1         95        95

  m4route-mem          1 used    57 unused    399 free    342 avail    400 total
 -------------
          Vdc                              Min       Max       Used      Unused    Avail
          ---                              ---       ---       ----      ------    -----
          example.cisco.com                 58        58        1         57        57

  m6route-mem          1 used     7 unused     79 free     72 avail     80 total
 -------------
          Vdc                              Min       Max       Used      Unused    Avail
          ---                              ---       ---       ----      ------    -----
          example.cisco.com                 8         8         1         7         7

  vni_bd               0 used  4096 unused   4096 free      0 avail   4096 total
 --------
          Vdc                              Min       Max       Used      Unused    Avail
          ---                              ---       ---       ----      ------    -----
          example.cisco.com                4096      4096      0         4096      4096

        '''}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVdcResourceDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_vdc(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowVdcResourceDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
