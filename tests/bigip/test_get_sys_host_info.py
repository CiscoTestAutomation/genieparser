# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_host_info
from genie.libs.parser.bigip.get_sys_host_info import SysHostinfo

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/host-info'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:host-info:host-infostats",
            "selfLink": "https://localhost/mgmt/tm/sys/host-info?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/host-info/0": {
                    "nestedStats": {
                        "entries": {
                            "activeCpuCount": {"value": 2},
                            "cpuCount": {"value": 2},
                            "https://localhost/mgmt/tm/sys/hostInfo/0/cpuInfo": {
                                "nestedStats": {
                                    "entries": {
                                        "https://localhost/mgmt/tm/sys/hostInfo/0/cpuInfo/0": {
                                            "nestedStats": {
                                                "entries": {
                                                    "cpuId": {"value": 0},
                                                    "fiveMinAvgIdle": {
                                                        "value": 74
                                                    },
                                                    "fiveMinAvgIowait": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgIrq": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgNiced": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgSoftirq": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgSystem": {
                                                        "value": 5
                                                    },
                                                    "fiveMinAvgUser": {
                                                        "value": 19
                                                    },
                                                    "fiveSecAvgIdle": {
                                                        "value": 54
                                                    },
                                                    "fiveSecAvgIowait": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgIrq": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgNiced": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgRatio": {
                                                        "value": 44
                                                    },
                                                    "fiveSecAvgSoftirq": {
                                                        "value": 1
                                                    },
                                                    "fiveSecAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgSystem": {
                                                        "value": 11
                                                    },
                                                    "fiveSecAvgUser": {
                                                        "value": 33
                                                    },
                                                    "idle": {"value": 404326},
                                                    "iowait": {"value": 611},
                                                    "irq": {"value": 0},
                                                    "niced": {"value": 830},
                                                    "oneMinAvgIdle": {
                                                        "value": 85
                                                    },
                                                    "oneMinAvgIowait": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgIrq": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgNiced": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgSoftirq": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgSystem": {
                                                        "value": 5
                                                    },
                                                    "oneMinAvgUser": {
                                                        "value": 8
                                                    },
                                                    "softirq": {"value": 762},
                                                    "stolen": {"value": 0},
                                                    "system": {"value": 23367},
                                                    "user": {"value": 47308},
                                                }
                                            }
                                        },
                                        "https://localhost/mgmt/tm/sys/hostInfo/0/cpuInfo/1": {
                                            "nestedStats": {
                                                "entries": {
                                                    "cpuId": {"value": 1},
                                                    "fiveMinAvgIdle": {
                                                        "value": 76
                                                    },
                                                    "fiveMinAvgIowait": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgIrq": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgNiced": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgSoftirq": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgSystem": {
                                                        "value": 5
                                                    },
                                                    "fiveMinAvgUser": {
                                                        "value": 16
                                                    },
                                                    "fiveSecAvgIdle": {
                                                        "value": 58
                                                    },
                                                    "fiveSecAvgIowait": {
                                                        "value": 1
                                                    },
                                                    "fiveSecAvgIrq": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgNiced": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgRatio": {
                                                        "value": 39
                                                    },
                                                    "fiveSecAvgSoftirq": {
                                                        "value": 2
                                                    },
                                                    "fiveSecAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgSystem": {
                                                        "value": 10
                                                    },
                                                    "fiveSecAvgUser": {
                                                        "value": 28
                                                    },
                                                    "idle": {"value": 406528},
                                                    "iowait": {"value": 830},
                                                    "irq": {"value": 0},
                                                    "niced": {"value": 615},
                                                    "oneMinAvgIdle": {
                                                        "value": 85
                                                    },
                                                    "oneMinAvgIowait": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgIrq": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgNiced": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgSoftirq": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgSystem": {
                                                        "value": 5
                                                    },
                                                    "oneMinAvgUser": {
                                                        "value": 7
                                                    },
                                                    "softirq": {"value": 1260},
                                                    "stolen": {"value": 0},
                                                    "system": {"value": 22454},
                                                    "user": {"value": 45471},
                                                }
                                            }
                                        },
                                    }
                                }
                            },
                            "hostId": {"description": "0"},
                            "memoryTotal": {"value": 4145995776},
                            "memoryUsed": {"value": 1900032768},
                        }
                    }
                }
            },
        }


class test_get_sys_host_info(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:host-info:host-infostats",
            "selfLink": "https://localhost/mgmt/tm/sys/host-info?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/host-info/0": {
                    "nestedStats": {
                        "entries": {
                            "activeCpuCount": {"value": 2},
                            "cpuCount": {"value": 2},
                            "https://localhost/mgmt/tm/sys/hostInfo/0/cpuInfo": {
                                "nestedStats": {
                                    "entries": {
                                        "https://localhost/mgmt/tm/sys/hostInfo/0/cpuInfo/0": {
                                            "nestedStats": {
                                                "entries": {
                                                    "cpuId": {"value": 0},
                                                    "fiveMinAvgIdle": {
                                                        "value": 74
                                                    },
                                                    "fiveMinAvgIowait": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgIrq": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgNiced": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgSoftirq": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgSystem": {
                                                        "value": 5
                                                    },
                                                    "fiveMinAvgUser": {
                                                        "value": 19
                                                    },
                                                    "fiveSecAvgIdle": {
                                                        "value": 54
                                                    },
                                                    "fiveSecAvgIowait": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgIrq": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgNiced": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgRatio": {
                                                        "value": 44
                                                    },
                                                    "fiveSecAvgSoftirq": {
                                                        "value": 1
                                                    },
                                                    "fiveSecAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgSystem": {
                                                        "value": 11
                                                    },
                                                    "fiveSecAvgUser": {
                                                        "value": 33
                                                    },
                                                    "idle": {"value": 404326},
                                                    "iowait": {"value": 611},
                                                    "irq": {"value": 0},
                                                    "niced": {"value": 830},
                                                    "oneMinAvgIdle": {
                                                        "value": 85
                                                    },
                                                    "oneMinAvgIowait": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgIrq": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgNiced": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgSoftirq": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgSystem": {
                                                        "value": 5
                                                    },
                                                    "oneMinAvgUser": {
                                                        "value": 8
                                                    },
                                                    "softirq": {"value": 762},
                                                    "stolen": {"value": 0},
                                                    "system": {"value": 23367},
                                                    "user": {"value": 47308},
                                                }
                                            }
                                        },
                                        "https://localhost/mgmt/tm/sys/hostInfo/0/cpuInfo/1": {
                                            "nestedStats": {
                                                "entries": {
                                                    "cpuId": {"value": 1},
                                                    "fiveMinAvgIdle": {
                                                        "value": 76
                                                    },
                                                    "fiveMinAvgIowait": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgIrq": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgNiced": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgSoftirq": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "fiveMinAvgSystem": {
                                                        "value": 5
                                                    },
                                                    "fiveMinAvgUser": {
                                                        "value": 16
                                                    },
                                                    "fiveSecAvgIdle": {
                                                        "value": 58
                                                    },
                                                    "fiveSecAvgIowait": {
                                                        "value": 1
                                                    },
                                                    "fiveSecAvgIrq": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgNiced": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgRatio": {
                                                        "value": 39
                                                    },
                                                    "fiveSecAvgSoftirq": {
                                                        "value": 2
                                                    },
                                                    "fiveSecAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgSystem": {
                                                        "value": 10
                                                    },
                                                    "fiveSecAvgUser": {
                                                        "value": 28
                                                    },
                                                    "idle": {"value": 406528},
                                                    "iowait": {"value": 830},
                                                    "irq": {"value": 0},
                                                    "niced": {"value": 615},
                                                    "oneMinAvgIdle": {
                                                        "value": 85
                                                    },
                                                    "oneMinAvgIowait": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgIrq": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgNiced": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgSoftirq": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "oneMinAvgSystem": {
                                                        "value": 5
                                                    },
                                                    "oneMinAvgUser": {
                                                        "value": 7
                                                    },
                                                    "softirq": {"value": 1260},
                                                    "stolen": {"value": 0},
                                                    "system": {"value": 22454},
                                                    "user": {"value": 45471},
                                                }
                                            }
                                        },
                                    }
                                }
                            },
                            "hostId": {"description": "0"},
                            "memoryTotal": {"value": 4145995776},
                            "memoryUsed": {"value": 1900032768},
                        }
                    }
                }
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysHostinfo(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysHostinfo(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
