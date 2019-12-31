# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_hardware
from genie.libs.parser.bigip.get_sys_hardware import SysHardware

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/hardware'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:hardware:hardwarestats",
            "selfLink": "https://localhost/mgmt/tm/sys/hardware?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/hardware/chassis-info": {
                    "nestedStats": {
                        "entries": {
                            "https://localhost/mgmt/tm/sys/hardware/chassis-info/0": {
                                "nestedStats": {
                                    "entries": {
                                        "maxMacCount": {"value": 1},
                                        "regKey": {"description": "-"},
                                    }
                                }
                            }
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/hardware/hardware-version": {
                    "nestedStats": {
                        "entries": {
                            "https://localhost/mgmt/tm/sys/hardware/hardware-version/HD1": {
                                "nestedStats": {
                                    "entries": {
                                        "model": {
                                            "description": "VMware Virtual S"
                                        },
                                        "tmName": {"description": "HD1"},
                                        "type": {
                                            "description": "physical-disk"
                                        },
                                        "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/HD1/versions": {
                                            "nestedStats": {
                                                "entries": {
                                                    "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/HD1/versions/0": {
                                                        "nestedStats": {
                                                            "entries": {
                                                                "tmName": {
                                                                    "description": "SerialNumber"
                                                                },
                                                                "version": {
                                                                    "description": "VMware-sda"
                                                                },
                                                            }
                                                        }
                                                    },
                                                    "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/HD1/versions/1": {
                                                        "nestedStats": {
                                                            "entries": {
                                                                "tmName": {
                                                                    "description": "Size"
                                                                },
                                                                "version": {
                                                                    "description": "76.00G"
                                                                },
                                                            }
                                                        }
                                                    },
                                                    "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/HD1/versions/2": {
                                                        "nestedStats": {
                                                            "entries": {
                                                                "tmName": {
                                                                    "description": "Firmware Version"
                                                                },
                                                                "version": {
                                                                    "description": "1.0"
                                                                },
                                                            }
                                                        }
                                                    },
                                                    "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/HD1/versions/3": {
                                                        "nestedStats": {
                                                            "entries": {
                                                                "tmName": {
                                                                    "description": "Media Type"
                                                                },
                                                                "version": {
                                                                    "description": "HDD"
                                                                },
                                                            }
                                                        }
                                                    },
                                                }
                                            }
                                        },
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/hardware/hardware-version/cpus": {
                                "nestedStats": {
                                    "entries": {
                                        "model": {
                                            "description": "Intel(R) Core(TM) i7-4870HQ CPU @ 2.50GHz"
                                        },
                                        "tmName": {"description": "cpus"},
                                        "type": {"description": "base-board"},
                                        "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/cpus/versions": {
                                            "nestedStats": {
                                                "entries": {
                                                    "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/cpus/versions/0": {
                                                        "nestedStats": {
                                                            "entries": {
                                                                "tmName": {
                                                                    "description": "cache size"
                                                                },
                                                                "version": {
                                                                    "description": "6144 KB"
                                                                },
                                                            }
                                                        }
                                                    },
                                                    "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/cpus/versions/1": {
                                                        "nestedStats": {
                                                            "entries": {
                                                                "tmName": {
                                                                    "description": "cores"
                                                                },
                                                                "version": {
                                                                    "description": "2  (physical:2)"
                                                                },
                                                            }
                                                        }
                                                    },
                                                    "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/cpus/versions/2": {
                                                        "nestedStats": {
                                                            "entries": {
                                                                "tmName": {
                                                                    "description": "cpu MHz"
                                                                },
                                                                "version": {
                                                                    "description": "2493.589"
                                                                },
                                                            }
                                                        }
                                                    },
                                                    "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/cpus/versions/3": {
                                                        "nestedStats": {
                                                            "entries": {
                                                                "tmName": {
                                                                    "description": "cpu sockets"
                                                                },
                                                                "version": {
                                                                    "description": "2"
                                                                },
                                                            }
                                                        }
                                                    },
                                                    "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/cpus/versions/4": {
                                                        "nestedStats": {
                                                            "entries": {
                                                                "tmName": {
                                                                    "description": "cpu stepping"
                                                                },
                                                                "version": {
                                                                    "description": "1"
                                                                },
                                                            }
                                                        }
                                                    },
                                                }
                                            }
                                        },
                                    }
                                }
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/hardware/platform": {
                    "nestedStats": {
                        "entries": {
                            "https://localhost/mgmt/tm/sys/hardware/platform/0": {
                                "nestedStats": {
                                    "entries": {
                                        "baseMac": {
                                            "description": "00:0c:29:35:0d:bd"
                                        },
                                        "biosRev": {"description": " "},
                                        "cloudName": {"description": " "},
                                        "hypervisorName": {
                                            "description": "VMware Virtual Platform"
                                        },
                                        "marketingName": {
                                            "description": "BIG-IP Virtual Edition"
                                        },
                                    }
                                }
                            }
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/hardware/system-info": {
                    "nestedStats": {
                        "entries": {
                            "https://localhost/mgmt/tm/sys/hardware/system-info/0": {
                                "nestedStats": {
                                    "entries": {
                                        "bigipChassisSerialNum": {
                                            "description": "564d4d7e-c668-e9dc-2bf3c9350dbd"
                                        },
                                        "hostBoardPartRevNum": {
                                            "description": " "
                                        },
                                        "hostBoardSerialNum": {
                                            "description": " "
                                        },
                                        "platform": {"description": "Z100"},
                                        "project_200LevelBomNum": {
                                            "description": " "
                                        },
                                        "switchBoardPartRevNum": {
                                            "description": " "
                                        },
                                        "switchBoardSerialNum": {
                                            "description": " "
                                        },
                                    }
                                }
                            }
                        }
                    }
                },
            },
        }


class test_get_sys_hardware(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/hardware/chassis-info": {
                "nestedStats": {
                    "entries": {
                        "https://localhost/mgmt/tm/sys/hardware/chassis-info/0": {
                            "nestedStats": {
                                "entries": {
                                    "maxMacCount": {"value": 1},
                                    "regKey": {"description": "-"},
                                }
                            }
                        }
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/hardware/hardware-version": {
                "nestedStats": {
                    "entries": {
                        "https://localhost/mgmt/tm/sys/hardware/hardware-version/HD1": {
                            "nestedStats": {
                                "entries": {
                                    "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/HD1/versions": {
                                        "nestedStats": {
                                            "entries": {
                                                "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/HD1/versions/0": {
                                                    "nestedStats": {
                                                        "entries": {
                                                            "tmName": {
                                                                "description": "SerialNumber"
                                                            },
                                                            "version": {
                                                                "description": "VMware-sda"
                                                            },
                                                        }
                                                    }
                                                },
                                                "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/HD1/versions/1": {
                                                    "nestedStats": {
                                                        "entries": {
                                                            "tmName": {
                                                                "description": "Size"
                                                            },
                                                            "version": {
                                                                "description": "76.00G"
                                                            },
                                                        }
                                                    }
                                                },
                                                "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/HD1/versions/2": {
                                                    "nestedStats": {
                                                        "entries": {
                                                            "tmName": {
                                                                "description": "Firmware "
                                                                "Version"
                                                            },
                                                            "version": {
                                                                "description": "1.0"
                                                            },
                                                        }
                                                    }
                                                },
                                                "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/HD1/versions/3": {
                                                    "nestedStats": {
                                                        "entries": {
                                                            "tmName": {
                                                                "description": "Media "
                                                                "Type"
                                                            },
                                                            "version": {
                                                                "description": "HDD"
                                                            },
                                                        }
                                                    }
                                                },
                                            }
                                        }
                                    },
                                    "model": {
                                        "description": "VMware " "Virtual " "S"
                                    },
                                    "tmName": {"description": "HD1"},
                                    "type": {"description": "physical-disk"},
                                }
                            }
                        },
                        "https://localhost/mgmt/tm/sys/hardware/hardware-version/cpus": {
                            "nestedStats": {
                                "entries": {
                                    "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/cpus/versions": {
                                        "nestedStats": {
                                            "entries": {
                                                "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/cpus/versions/0": {
                                                    "nestedStats": {
                                                        "entries": {
                                                            "tmName": {
                                                                "description": "cache "
                                                                "size"
                                                            },
                                                            "version": {
                                                                "description": "6144 "
                                                                "KB"
                                                            },
                                                        }
                                                    }
                                                },
                                                "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/cpus/versions/1": {
                                                    "nestedStats": {
                                                        "entries": {
                                                            "tmName": {
                                                                "description": "cores"
                                                            },
                                                            "version": {
                                                                "description": "2  "
                                                                "(physical:2)"
                                                            },
                                                        }
                                                    }
                                                },
                                                "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/cpus/versions/2": {
                                                    "nestedStats": {
                                                        "entries": {
                                                            "tmName": {
                                                                "description": "cpu "
                                                                "MHz"
                                                            },
                                                            "version": {
                                                                "description": "2493.589"
                                                            },
                                                        }
                                                    }
                                                },
                                                "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/cpus/versions/3": {
                                                    "nestedStats": {
                                                        "entries": {
                                                            "tmName": {
                                                                "description": "cpu "
                                                                "sockets"
                                                            },
                                                            "version": {
                                                                "description": "2"
                                                            },
                                                        }
                                                    }
                                                },
                                                "https://localhost/mgmt/tm/sys/hardware/hardwareVersion/cpus/versions/4": {
                                                    "nestedStats": {
                                                        "entries": {
                                                            "tmName": {
                                                                "description": "cpu "
                                                                "stepping"
                                                            },
                                                            "version": {
                                                                "description": "1"
                                                            },
                                                        }
                                                    }
                                                },
                                            }
                                        }
                                    },
                                    "model": {
                                        "description": "Intel(R) "
                                        "Core(TM) "
                                        "i7-4870HQ "
                                        "CPU "
                                        "@ "
                                        "2.50GHz"
                                    },
                                    "tmName": {"description": "cpus"},
                                    "type": {"description": "base-board"},
                                }
                            }
                        },
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/hardware/platform": {
                "nestedStats": {
                    "entries": {
                        "https://localhost/mgmt/tm/sys/hardware/platform/0": {
                            "nestedStats": {
                                "entries": {
                                    "baseMac": {
                                        "description": "00:0c:29:35:0d:bd"
                                    },
                                    "biosRev": {"description": " "},
                                    "cloudName": {"description": " "},
                                    "hypervisorName": {
                                        "description": "VMware "
                                        "Virtual "
                                        "Platform"
                                    },
                                    "marketingName": {
                                        "description": "BIG-IP "
                                        "Virtual "
                                        "Edition"
                                    },
                                }
                            }
                        }
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/hardware/system-info": {
                "nestedStats": {
                    "entries": {
                        "https://localhost/mgmt/tm/sys/hardware/system-info/0": {
                            "nestedStats": {
                                "entries": {
                                    "bigipChassisSerialNum": {
                                        "description": "564d4d7e-c668-e9dc-2bf3c9350dbd"
                                    },
                                    "hostBoardPartRevNum": {
                                        "description": " "
                                    },
                                    "hostBoardSerialNum": {"description": " "},
                                    "platform": {"description": "Z100"},
                                    "project_200LevelBomNum": {
                                        "description": " "
                                    },
                                    "switchBoardPartRevNum": {
                                        "description": " "
                                    },
                                    "switchBoardSerialNum": {
                                        "description": " "
                                    },
                                }
                            }
                        }
                    }
                }
            },
        },
        "kind": "tm:sys:hardware:hardwarestats",
        "selfLink": "https://localhost/mgmt/tm/sys/hardware?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysHardware(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysHardware(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
