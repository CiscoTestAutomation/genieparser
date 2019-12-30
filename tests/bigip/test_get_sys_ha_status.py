# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_ha_status
from genie.libs.parser.bigip.get_sys_ha_status import SysHastatus

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/ha-status'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:ha-status:ha-statusstats",
            "selfLink": "https://localhost/mgmt/tm/sys/ha-status?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:%25snmpd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "restart"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "daemon-heartbeat"},
                            "key": {"description": "%snmpd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:bigd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "restart"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "daemon-heartbeat"},
                            "key": {"description": "bigd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:cbrd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "restart"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "daemon-heartbeat"},
                            "key": {"description": "cbrd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:gtmd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "go-offline-restart"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "daemon-heartbeat"},
                            "key": {"description": "gtmd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:keymgmtd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "restart"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "daemon-heartbeat"},
                            "key": {"description": "keymgmtd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:mcpd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "restart"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "daemon-heartbeat"},
                            "key": {"description": "mcpd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:scriptd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "restart"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "daemon-heartbeat"},
                            "key": {"description": "scriptd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:sod": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "restart-all"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "daemon-heartbeat"},
                            "key": {"description": "sod"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:tmm": {
                    "nestedStats": {
                        "entries": {
                            "action": {
                                "description": "go-offline-downlinks-restart"
                            },
                            "failure": {"description": "no"},
                            "haFeature": {"description": "daemon-heartbeat"},
                            "key": {"description": "tmm"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:tmm1": {
                    "nestedStats": {
                        "entries": {
                            "action": {
                                "description": "go-offline-downlinks-restart"
                            },
                            "failure": {"description": "no"},
                            "haFeature": {"description": "daemon-heartbeat"},
                            "key": {"description": "tmm1"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:tmrouted": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "restart"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "daemon-heartbeat"},
                            "key": {"description": "tmrouted"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:vxland": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "restart"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "daemon-heartbeat"},
                            "key": {"description": "vxland"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:wccpd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "restart"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "daemon-heartbeat"},
                            "key": {"description": "wccpd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:dataplane-inoperable:chmand": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "go-offline"},
                            "failure": {"description": "no"},
                            "haFeature": {
                                "description": "dataplane-inoperable"
                            },
                            "key": {"description": "chmand"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:forced-offline:sod": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "none"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "forced-offline"},
                            "key": {"description": "sod"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:license-exceeded:mcpd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "go-offline-downlinks"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "license-exceeded"},
                            "key": {"description": "mcpd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:license-invalid:mcpd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "go-offline-downlinks"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "license-invalid"},
                            "key": {"description": "mcpd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:overdog-ctrl:watchdog": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "none"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "overdog-ctrl"},
                            "key": {"description": "watchdog"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:proc-run:bigd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "go-offline-downlinks"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "proc-run"},
                            "key": {"description": "bigd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:proc-run:gtmd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "go-offline"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "proc-run"},
                            "key": {"description": "gtmd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:proc-run:mcpd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "go-offline-downlinks"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "proc-run"},
                            "key": {"description": "mcpd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:proc-run:named": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "go-offline-downlinks"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "proc-run"},
                            "key": {"description": "named"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:proc-run:tmm": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "go-offline-downlinks"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "proc-run"},
                            "key": {"description": "tmm"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:proc-run:tmrouted": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "failover"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "proc-run"},
                            "key": {"description": "tmrouted"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:provisioning-failed:provisioning": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "go-offline-downlinks"},
                            "failure": {"description": "no"},
                            "haFeature": {
                                "description": "provisioning-failed"
                            },
                            "key": {"description": "provisioning"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:ready-for-world:tmm": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "none"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "ready-for-world"},
                            "key": {"description": "tmm"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:ready-for-world:tmm1": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "none"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "ready-for-world"},
                            "key": {"description": "tmm1"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:reboot-request:sod": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "reboot"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "reboot-request"},
                            "key": {"description": "sod"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:software-update:lind": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "reboot"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "software-update"},
                            "key": {"description": "lind"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:switchboard-failsafe:lacpd": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "go-offline-restart-tm"},
                            "failure": {"description": "no"},
                            "haFeature": {
                                "description": "switchboard-failsafe"
                            },
                            "key": {"description": "lacpd"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/ha-status/:tmm-detect-fail:tmm": {
                    "nestedStats": {
                        "entries": {
                            "action": {"description": "failover"},
                            "failure": {"description": "no"},
                            "haFeature": {"description": "tmm-detect-fail"},
                            "key": {"description": "tmm"},
                        }
                    }
                },
            },
        }


class test_get_sys_ha_status(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:%25snmpd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "restart"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "daemon-heartbeat"},
                        "key": {"description": "%snmpd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:bigd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "restart"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "daemon-heartbeat"},
                        "key": {"description": "bigd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:cbrd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "restart"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "daemon-heartbeat"},
                        "key": {"description": "cbrd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:gtmd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "go-offline-restart"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "daemon-heartbeat"},
                        "key": {"description": "gtmd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:keymgmtd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "restart"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "daemon-heartbeat"},
                        "key": {"description": "keymgmtd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:mcpd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "restart"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "daemon-heartbeat"},
                        "key": {"description": "mcpd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:scriptd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "restart"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "daemon-heartbeat"},
                        "key": {"description": "scriptd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:sod": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "restart-all"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "daemon-heartbeat"},
                        "key": {"description": "sod"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:tmm": {
                "nestedStats": {
                    "entries": {
                        "action": {
                            "description": "go-offline-downlinks-restart"
                        },
                        "failure": {"description": "no"},
                        "haFeature": {"description": "daemon-heartbeat"},
                        "key": {"description": "tmm"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:tmm1": {
                "nestedStats": {
                    "entries": {
                        "action": {
                            "description": "go-offline-downlinks-restart"
                        },
                        "failure": {"description": "no"},
                        "haFeature": {"description": "daemon-heartbeat"},
                        "key": {"description": "tmm1"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:tmrouted": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "restart"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "daemon-heartbeat"},
                        "key": {"description": "tmrouted"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:vxland": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "restart"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "daemon-heartbeat"},
                        "key": {"description": "vxland"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:daemon-heartbeat:wccpd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "restart"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "daemon-heartbeat"},
                        "key": {"description": "wccpd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:dataplane-inoperable:chmand": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "go-offline"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "dataplane-inoperable"},
                        "key": {"description": "chmand"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:forced-offline:sod": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "none"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "forced-offline"},
                        "key": {"description": "sod"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:license-exceeded:mcpd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "go-offline-downlinks"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "license-exceeded"},
                        "key": {"description": "mcpd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:license-invalid:mcpd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "go-offline-downlinks"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "license-invalid"},
                        "key": {"description": "mcpd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:overdog-ctrl:watchdog": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "none"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "overdog-ctrl"},
                        "key": {"description": "watchdog"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:proc-run:bigd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "go-offline-downlinks"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "proc-run"},
                        "key": {"description": "bigd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:proc-run:gtmd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "go-offline"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "proc-run"},
                        "key": {"description": "gtmd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:proc-run:mcpd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "go-offline-downlinks"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "proc-run"},
                        "key": {"description": "mcpd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:proc-run:named": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "go-offline-downlinks"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "proc-run"},
                        "key": {"description": "named"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:proc-run:tmm": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "go-offline-downlinks"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "proc-run"},
                        "key": {"description": "tmm"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:proc-run:tmrouted": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "failover"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "proc-run"},
                        "key": {"description": "tmrouted"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:provisioning-failed:provisioning": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "go-offline-downlinks"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "provisioning-failed"},
                        "key": {"description": "provisioning"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:ready-for-world:tmm": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "none"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "ready-for-world"},
                        "key": {"description": "tmm"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:ready-for-world:tmm1": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "none"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "ready-for-world"},
                        "key": {"description": "tmm1"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:reboot-request:sod": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "reboot"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "reboot-request"},
                        "key": {"description": "sod"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:software-update:lind": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "reboot"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "software-update"},
                        "key": {"description": "lind"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:switchboard-failsafe:lacpd": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "go-offline-restart-tm"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "switchboard-failsafe"},
                        "key": {"description": "lacpd"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/ha-status/:tmm-detect-fail:tmm": {
                "nestedStats": {
                    "entries": {
                        "action": {"description": "failover"},
                        "failure": {"description": "no"},
                        "haFeature": {"description": "tmm-detect-fail"},
                        "key": {"description": "tmm"},
                    }
                }
            },
        },
        "kind": "tm:sys:ha-status:ha-statusstats",
        "selfLink": "https://localhost/mgmt/tm/sys/ha-status?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysHastatus(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysHastatus(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
