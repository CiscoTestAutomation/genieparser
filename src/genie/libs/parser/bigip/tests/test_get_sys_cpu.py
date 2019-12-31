# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_cpu
from genie.libs.parser.bigip.get_sys_cpu import SysCpu

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/cpu'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:cpu:cpucollectionstats",
            "selfLink": "https://localhost/mgmt/tm/sys/cpu?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/cpu/0": {
                    "nestedStats": {
                        "kind": "tm:sys:cpu:cpustats",
                        "selfLink": "https://localhost/mgmt/tm/sys/cpu/0?ver=14.1.2.1",
                        "entries": {
                            "https://localhost/mgmt/tm/sys/cpu/0/cpuInfo": {
                                "nestedStats": {
                                    "entries": {
                                        "https://localhost/mgmt/tm/sys/cpu/0/cpuInfo/0": {
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
                                                        "value": 72
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
                                                        "value": 26
                                                    },
                                                    "fiveSecAvgSoftirq": {
                                                        "value": 1
                                                    },
                                                    "fiveSecAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgSystem": {
                                                        "value": 6
                                                    },
                                                    "fiveSecAvgUser": {
                                                        "value": 19
                                                    },
                                                    "idle": {"value": 404881},
                                                    "iowait": {"value": 619},
                                                    "irq": {"value": 0},
                                                    "niced": {"value": 830},
                                                    "oneMinAvgIdle": {
                                                        "value": 82
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
                                                        "value": 10
                                                    },
                                                    "softirq": {"value": 767},
                                                    "stolen": {"value": 0},
                                                    "system": {"value": 23423},
                                                    "user": {"value": 47470},
                                                }
                                            }
                                        },
                                        "https://localhost/mgmt/tm/sys/cpu/0/cpuInfo/1": {
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
                                                        "value": 66
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
                                                        "value": 32
                                                    },
                                                    "fiveSecAvgSoftirq": {
                                                        "value": 1
                                                    },
                                                    "fiveSecAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgSystem": {
                                                        "value": 7
                                                    },
                                                    "fiveSecAvgUser": {
                                                        "value": 24
                                                    },
                                                    "idle": {"value": 407060},
                                                    "iowait": {"value": 831},
                                                    "irq": {"value": 0},
                                                    "niced": {"value": 616},
                                                    "oneMinAvgIdle": {
                                                        "value": 82
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
                                                        "value": 10
                                                    },
                                                    "softirq": {"value": 1268},
                                                    "stolen": {"value": 0},
                                                    "system": {"value": 22513},
                                                    "user": {"value": 45663},
                                                }
                                            }
                                        },
                                    }
                                }
                            },
                            "hostId": {"description": "0"},
                        },
                    }
                }
            },
        }


class test_get_sys_cpu(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:cpu:cpucollectionstats",
            "selfLink": "https://localhost/mgmt/tm/sys/cpu?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/cpu/0": {
                    "nestedStats": {
                        "kind": "tm:sys:cpu:cpustats",
                        "selfLink": "https://localhost/mgmt/tm/sys/cpu/0?ver=14.1.2.1",
                        "entries": {
                            "https://localhost/mgmt/tm/sys/cpu/0/cpuInfo": {
                                "nestedStats": {
                                    "entries": {
                                        "https://localhost/mgmt/tm/sys/cpu/0/cpuInfo/0": {
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
                                                        "value": 72
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
                                                        "value": 26
                                                    },
                                                    "fiveSecAvgSoftirq": {
                                                        "value": 1
                                                    },
                                                    "fiveSecAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgSystem": {
                                                        "value": 6
                                                    },
                                                    "fiveSecAvgUser": {
                                                        "value": 19
                                                    },
                                                    "idle": {"value": 404881},
                                                    "iowait": {"value": 619},
                                                    "irq": {"value": 0},
                                                    "niced": {"value": 830},
                                                    "oneMinAvgIdle": {
                                                        "value": 82
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
                                                        "value": 10
                                                    },
                                                    "softirq": {"value": 767},
                                                    "stolen": {"value": 0},
                                                    "system": {"value": 23423},
                                                    "user": {"value": 47470},
                                                }
                                            }
                                        },
                                        "https://localhost/mgmt/tm/sys/cpu/0/cpuInfo/1": {
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
                                                        "value": 66
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
                                                        "value": 32
                                                    },
                                                    "fiveSecAvgSoftirq": {
                                                        "value": 1
                                                    },
                                                    "fiveSecAvgStolen": {
                                                        "value": 0
                                                    },
                                                    "fiveSecAvgSystem": {
                                                        "value": 7
                                                    },
                                                    "fiveSecAvgUser": {
                                                        "value": 24
                                                    },
                                                    "idle": {"value": 407060},
                                                    "iowait": {"value": 831},
                                                    "irq": {"value": 0},
                                                    "niced": {"value": 616},
                                                    "oneMinAvgIdle": {
                                                        "value": 82
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
                                                        "value": 10
                                                    },
                                                    "softirq": {"value": 1268},
                                                    "stolen": {"value": 0},
                                                    "system": {"value": 22513},
                                                    "user": {"value": 45663},
                                                }
                                            }
                                        },
                                    }
                                }
                            },
                            "hostId": {"description": "0"},
                        },
                    }
                }
            },
        }


    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysCpu(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysCpu(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
