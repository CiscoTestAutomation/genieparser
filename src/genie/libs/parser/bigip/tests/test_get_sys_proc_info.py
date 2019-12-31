# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_proc_info
from genie.libs.parser.bigip.get_sys_proc_info import SysProcinfo

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/proc-info'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:proc-info:proc-infocollectionstats",
            "selfLink": "https://localhost/mgmt/tm/sys/proc-info?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/proc-info/acpid": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/acpid?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1491},
                            "procName": {"description": "acpid"},
                            "rss": {"value": 417792},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 4468736},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/agetty": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/agetty?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3968},
                            "procName": {"description": "agetty"},
                            "rss": {"value": 720896},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 112709632},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/alertd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/alertd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 1},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4076},
                            "procName": {"description": "alertd"},
                            "rss": {"value": 8040448},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 1},
                            "vsize": {"value": 37986304},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ata_sff": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ata_sff?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 214},
                            "procName": {"description": "ata_sff"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/audit_forwarder": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/audit_forwarder?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 12437},
                            "procName": {"description": "audit_forwarder"},
                            "rss": {"value": 23527424},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 42450944},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/auditd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/auditd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1451},
                            "procName": {"description": "auditd"},
                            "rss": {"value": 909312},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 57954304},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/bash": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/bash?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 11276},
                            "procName": {"description": "bash"},
                            "rss": {"value": 1392640},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 120291328},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/big3d": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/big3d?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6982},
                            "procName": {"description": "big3d"},
                            "rss": {"value": 1441792},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 9531392},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/bigd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/bigd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 5985},
                            "procName": {"description": "bigd"},
                            "rss": {"value": 24707072},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 58867712},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/bioset": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/bioset?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 328},
                            "procName": {"description": "bioset"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/cbrd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/cbrd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4793},
                            "procName": {"description": "cbrd"},
                            "rss": {"value": 22028288},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 57978880},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/chmand": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/chmand?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 7404},
                            "procName": {"description": "chmand"},
                            "rss": {"value": 32055296},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 168353792},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/crond": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/crond?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3059},
                            "procName": {"description": "crond"},
                            "rss": {"value": 1114112},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 129314816},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/crypto": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/crypto?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 34},
                            "procName": {"description": "crypto"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/csyncd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/csyncd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4075},
                            "procName": {"description": "csyncd"},
                            "rss": {"value": 31768576},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 41467904},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/dbus-daemon": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/dbus-daemon?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1483},
                            "procName": {"description": "dbus-daemon"},
                            "rss": {"value": 1687552},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 62091264},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/deferwq": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/deferwq?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 66},
                            "procName": {"description": "deferwq"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/devmgmtd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/devmgmtd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6343},
                            "procName": {"description": "devmgmtd"},
                            "rss": {"value": 25640960},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 38453248},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/dynconfd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/dynconfd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 7407},
                            "procName": {"description": "dynconfd"},
                            "rss": {"value": 18882560},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 98295808},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/errdefsd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/errdefsd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4338},
                            "procName": {"description": "errdefsd"},
                            "rss": {"value": 6799360},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 102580224},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/eventd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/eventd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6981},
                            "procName": {"description": "eventd"},
                            "rss": {"value": 24473600},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 53141504},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/evrouted": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/evrouted?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4790},
                            "procName": {"description": "evrouted"},
                            "rss": {"value": 24981504},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 32747520},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ext4-rsv-conver": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ext4-rsv-conver?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1420},
                            "procName": {"description": "ext4-rsv-conver"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/f5-rest-node": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/f5-rest-node?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6673},
                            "procName": {"description": "f5-rest-node"},
                            "rss": {"value": 51097600},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 1284382720},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/fsnotify_mark": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/fsnotify_mark?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 33},
                            "procName": {"description": "fsnotify_mark"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/gtmd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/gtmd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "gtm"},
                            "pid": {"value": 6336},
                            "procName": {"description": "gtmd"},
                            "rss": {"value": 9117696},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 125489152},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/httpd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/httpd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 1},
                            "cpuUsage_5mins": {"value": 1},
                            "cpuUsageRecent": {"value": 2},
                            "modules": {"description": "ui"},
                            "pid": {"value": 11337},
                            "procName": {"description": "httpd"},
                            "rss": {"value": 10199040},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 1},
                            "vsize": {"value": 121319424},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/iControlPortal.": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/iControlPortal.?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 3936},
                            "procName": {"description": "iControlPortal."},
                            "rss": {"value": 61763584},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 306618368},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ib-comp-wq": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ib-comp-wq?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1633},
                            "procName": {"description": "ib-comp-wq"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ib_mcast": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ib_mcast?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1634},
                            "procName": {"description": "ib_mcast"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ib_nl_sa_wq": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ib_nl_sa_wq?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1635},
                            "procName": {"description": "ib_nl_sa_wq"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/icr_eventd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/icr_eventd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 7780},
                            "procName": {"description": "icr_eventd"},
                            "rss": {"value": 24915968},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 43819008},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/icrd_child": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/icrd_child?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 2},
                            "cpuUsage_5mins": {"value": 1},
                            "cpuUsageRecent": {"value": 5},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 9974},
                            "procName": {"description": "icrd_child"},
                            "rss": {"value": 106045440},
                            "systemUsage_1min": {"value": 1},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 2},
                            "vsize": {"value": 401657856},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/increase_entrop": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/increase_entrop?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1531},
                            "procName": {"description": "increase_entrop"},
                            "rss": {"value": 126976},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 8646656},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ipoib_flush": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ipoib_flush?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1707},
                            "procName": {"description": "ipoib_flush"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/iprepd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/iprepd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ltm"},
                            "pid": {"value": 6676},
                            "procName": {"description": "iprepd"},
                            "rss": {"value": 24903680},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 32817152},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ipv6_addrconf": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ipv6_addrconf?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 46},
                            "procName": {"description": "ipv6_addrconf"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/irqbalance": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/irqbalance?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1480},
                            "procName": {"description": "irqbalance"},
                            "rss": {"value": 1024000},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 22155264},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/java": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/java?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 5},
                            "cpuUsage_5mins": {"value": 14},
                            "cpuUsageRecent": {"value": 10},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 5978},
                            "procName": {"description": "java"},
                            "rss": {"value": 259293184},
                            "systemUsage_1min": {"value": 2},
                            "systemUsage_5mins": {"value": 7},
                            "systemUsageRecent": {"value": 5},
                            "vsize": {"value": 454184960},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-1-8": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-1-8?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1403},
                            "procName": {"description": "jbd2/dm-1-8"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-3-8": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-3-8?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1419},
                            "procName": {"description": "jbd2/dm-3-8"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-5-8": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-5-8?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 359},
                            "procName": {"description": "jbd2/dm-5-8"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-6-8": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-6-8?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 382},
                            "procName": {"description": "jbd2/dm-6-8"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-7-8": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-7-8?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1398},
                            "procName": {"description": "jbd2/dm-7-8"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-8-8": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-8-8?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1395},
                            "procName": {"description": "jbd2/dm-8-8"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jitterentropy-r": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jitterentropy-r?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 1},
                            "cpuUsage_5mins": {"value": 1},
                            "cpuUsageRecent": {"value": 1},
                            "modules": {"description": " "},
                            "pid": {"value": 1424},
                            "procName": {"description": "jitterentropy-r"},
                            "rss": {"value": 528384},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 1},
                            "vsize": {"value": 4440064},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kauditd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kauditd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 98},
                            "procName": {"description": "kauditd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kblockd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kblockd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 23},
                            "procName": {"description": "kblockd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kdevtmpfs": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kdevtmpfs?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 17},
                            "procName": {"description": "kdevtmpfs"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kdmflush": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kdmflush?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 325},
                            "procName": {"description": "kdmflush"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/keymgmtd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/keymgmtd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6347},
                            "procName": {"description": "keymgmtd"},
                            "rss": {"value": 26259456},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 134991872},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/khungtaskd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/khungtaskd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 19},
                            "procName": {"description": "khungtaskd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kintegrityd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kintegrityd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 21},
                            "procName": {"description": "kintegrityd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kjournald": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kjournald?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1412},
                            "procName": {"description": "kjournald"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kmpath_rdacd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kmpath_rdacd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 44},
                            "procName": {"description": "kmpath_rdacd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kpsmoused": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kpsmoused?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 45},
                            "procName": {"description": "kpsmoused"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ksmd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ksmd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 32},
                            "procName": {"description": "ksmd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ksoftirqd~0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ksoftirqd~0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3},
                            "procName": {"description": "ksoftirqd/0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ksoftirqd~1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ksoftirqd~1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 13},
                            "procName": {"description": "ksoftirqd/1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kswapd0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kswapd0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 31},
                            "procName": {"description": "kswapd0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kthreadd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kthreadd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 2},
                            "procName": {"description": "kthreadd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kthrotld": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kthrotld?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 42},
                            "procName": {"description": "kthrotld"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~0:0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~0:0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 21252},
                            "procName": {"description": "kworker/0:0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~0:0H": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~0:0H?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 5},
                            "procName": {"description": "kworker/0:0H"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~0:1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~0:1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 13469},
                            "procName": {"description": "kworker/0:1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~0:1H": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~0:1H?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3192},
                            "procName": {"description": "kworker/0:1H"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~0:2": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~0:2?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 12651},
                            "procName": {"description": "kworker/0:2"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~0:3": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~0:3?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 25342},
                            "procName": {"description": "kworker/0:3"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~1:0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~1:0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 18261},
                            "procName": {"description": "kworker/1:0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~1:0H": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~1:0H?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 15},
                            "procName": {"description": "kworker/1:0H"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~1:1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~1:1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 13210},
                            "procName": {"description": "kworker/1:1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~1:1H": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~1:1H?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 2108},
                            "procName": {"description": "kworker/1:1H"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~1:2": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~1:2?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 24324},
                            "procName": {"description": "kworker/1:2"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~1:3": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~1:3?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 27344},
                            "procName": {"description": "kworker/1:3"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~u4:0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~u4:0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 24248},
                            "procName": {"description": "kworker/u4:0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~u4:1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~u4:1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 11303},
                            "procName": {"description": "kworker/u4:1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~u4:3": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~u4:3?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 15388},
                            "procName": {"description": "kworker/u4:3"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/lacpd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/lacpd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 5974},
                            "procName": {"description": "lacpd"},
                            "rss": {"value": 32919552},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 32948224},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/lind": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/lind?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4789},
                            "procName": {"description": "lind"},
                            "rss": {"value": 22274048},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 29831168},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/logger": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/logger?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 3925},
                            "procName": {"description": "logger"},
                            "rss": {"value": 761856},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 6619136},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/login": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/login?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3966},
                            "procName": {"description": "login"},
                            "rss": {"value": 3899392},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 124059648},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/logstatd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/logstatd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 7403},
                            "procName": {"description": "logstatd"},
                            "rss": {"value": 24719360},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 129613824},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/lvmetad": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/lvmetad?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 439},
                            "procName": {"description": "lvmetad"},
                            "rss": {"value": 897024},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 208973824},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mcpd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mcpd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 3},
                            "cpuUsage_5mins": {"value": 1},
                            "cpuUsageRecent": {"value": 8},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4791},
                            "procName": {"description": "mcpd"},
                            "rss": {"value": 98238464},
                            "systemUsage_1min": {"value": 1},
                            "systemUsage_5mins": {"value": 1},
                            "systemUsageRecent": {"value": 4},
                            "vsize": {"value": 223965184},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mcpq": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mcpq?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ui"},
                            "pid": {"value": 3933},
                            "procName": {"description": "mcpq"},
                            "rss": {"value": 14176256},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 63414272},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/md": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/md?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 24},
                            "procName": {"description": "md"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/merged": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/merged?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4329},
                            "procName": {"description": "merged"},
                            "rss": {"value": 16146432},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 103100416},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mgmt_acld": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mgmt_acld?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 7409},
                            "procName": {"description": "mgmt_acld"},
                            "rss": {"value": 24735744},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 166834176},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/migration~0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/migration~0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 7},
                            "procName": {"description": "migration/0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/migration~1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/migration~1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 12},
                            "procName": {"description": "migration/1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mlx4": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mlx4?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1625},
                            "procName": {"description": "mlx4"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mlx4_ib": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mlx4_ib?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1637},
                            "procName": {"description": "mlx4_ib"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mlx4_ib_mcg": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mlx4_ib_mcg?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1638},
                            "procName": {"description": "mlx4_ib_mcg"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mpt~0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mpt~0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 218},
                            "procName": {"description": "mpt/0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mpt_poll_0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mpt_poll_0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 215},
                            "procName": {"description": "mpt_poll_0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/named": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/named?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 10605},
                            "procName": {"description": "named"},
                            "rss": {"value": 52920320},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 92078080},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/netns": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/netns?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 18},
                            "procName": {"description": "netns"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/nfit": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/nfit?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 516},
                            "procName": {"description": "nfit"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ntlmconnpool": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ntlmconnpool?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6345},
                            "procName": {"description": "ntlmconnpool"},
                            "rss": {"value": 999424},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 6164480},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ntpd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ntpd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3664},
                            "procName": {"description": "ntpd"},
                            "rss": {"value": 1216512},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 50196480},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/overdog": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/overdog?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 3147},
                            "procName": {"description": "overdog"},
                            "rss": {"value": 89669632},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 90861568},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/pccd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/pccd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 4078},
                            "procName": {"description": "pccd"},
                            "rss": {"value": 24129536},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 130392064},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/promptstatusd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/promptstatusd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 3058},
                            "procName": {"description": "promptstatusd"},
                            "rss": {"value": 15966208},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 86048768},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/racoon": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/racoon?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ltm"},
                            "pid": {"value": 10049},
                            "procName": {"description": "racoon"},
                            "rss": {"value": 888832},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 13733888},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rcu_bh": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rcu_bh?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 8},
                            "procName": {"description": "rcu_bh"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rcu_sched": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rcu_sched?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 9},
                            "procName": {"description": "rcu_sched"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rdma_cm": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rdma_cm?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1717},
                            "procName": {"description": "rdma_cm"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rm": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rm?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 9694},
                            "procName": {"description": "rm"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rrdshim": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rrdshim?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 9872},
                            "procName": {"description": "rrdshim"},
                            "rss": {"value": 2039808},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 11100160},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rrdstats": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rrdstats?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ui"},
                            "pid": {"value": 3934},
                            "procName": {"description": "rrdstats"},
                            "rss": {"value": 962560},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 4419584},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rtstats": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rtstats?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ui"},
                            "pid": {"value": 3935},
                            "procName": {"description": "rtstats"},
                            "rss": {"value": 720896},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 4157440},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/runsm1_named": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/runsm1_named?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6348},
                            "procName": {"description": "runsm1_named"},
                            "rss": {"value": 3039232},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 25669632},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/runsv": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/runsv?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 7775},
                            "procName": {"description": "runsv"},
                            "rss": {"value": 208896},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 2179072},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/runsvdir": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/runsvdir?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3937},
                            "procName": {"description": "runsvdir"},
                            "rss": {"value": 380928},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 2330624},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scriptd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scriptd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 7405},
                            "procName": {"description": "scriptd"},
                            "rss": {"value": 84062208},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 288526336},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scsi_eh_0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scsi_eh_0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 221},
                            "procName": {"description": "scsi_eh_0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scsi_eh_1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scsi_eh_1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 223},
                            "procName": {"description": "scsi_eh_1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scsi_eh_2": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scsi_eh_2?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 226},
                            "procName": {"description": "scsi_eh_2"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scsi_tmf_0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scsi_tmf_0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 222},
                            "procName": {"description": "scsi_tmf_0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scsi_tmf_1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scsi_tmf_1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 225},
                            "procName": {"description": "scsi_tmf_1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scsi_tmf_2": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scsi_tmf_2?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 227},
                            "procName": {"description": "scsi_tmf_2"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/sflow_agent": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/sflow_agent?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ltm"},
                            "pid": {"value": 4074},
                            "procName": {"description": "sflow_agent"},
                            "rss": {"value": 24735744},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 153120768},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/snmpd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/snmpd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 5279},
                            "procName": {"description": "snmpd"},
                            "rss": {"value": 27762688},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 138039296},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/sod": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/sod?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 5648},
                            "procName": {"description": "sod"},
                            "rss": {"value": 82157568},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 83337216},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/sshd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/sshd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3624},
                            "procName": {"description": "sshd"},
                            "rss": {"value": 1060864},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 129302528},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/statsd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/statsd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6346},
                            "procName": {"description": "statsd"},
                            "rss": {"value": 23855104},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 48545792},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/su": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/su?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 6341},
                            "procName": {"description": "su"},
                            "rss": {"value": 3440640},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 118616064},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/syscalld": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/syscalld?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 7779},
                            "procName": {"description": "syscalld"},
                            "rss": {"value": 22446080},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 29843456},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/syslog-ng": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/syslog-ng?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 1},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 2},
                            "modules": {"description": " "},
                            "pid": {"value": 2321},
                            "procName": {"description": "syslog-ng"},
                            "rss": {"value": 6995968},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 1},
                            "vsize": {"value": 260685824},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/systemctl": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/systemctl?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 8489},
                            "procName": {"description": "systemctl"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/systemd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/systemd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1},
                            "procName": {"description": "systemd"},
                            "rss": {"value": 5017600},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 84172800},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/systemd-journal": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/systemd-journal?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 1},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 2},
                            "modules": {"description": " "},
                            "pid": {"value": 416},
                            "procName": {"description": "systemd-journal"},
                            "rss": {"value": 4915200},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 1},
                            "vsize": {"value": 35504128},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/systemd-logind": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/systemd-logind?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3060},
                            "procName": {"description": "systemd-logind"},
                            "rss": {"value": 1556480},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 25714688},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/systemd-udevd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/systemd-udevd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 448},
                            "procName": {"description": "systemd-udevd"},
                            "rss": {"value": 1196032},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 48214016},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/tamd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/tamd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ltm"},
                            "pid": {"value": 4799},
                            "procName": {"description": "tamd"},
                            "rss": {"value": 4419584},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 38977536},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/tmipsecd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/tmipsecd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ltm"},
                            "pid": {"value": 7402},
                            "procName": {"description": "tmipsecd"},
                            "rss": {"value": 24731648},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 54099968},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/tmm.0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/tmm.0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 15},
                            "cpuUsage_5mins": {"value": 14},
                            "cpuUsageRecent": {"value": 14},
                            "modules": {"description": "tmm"},
                            "pid": {"value": 9762},
                            "procName": {"description": "tmm.0"},
                            "rss": {"value": 117272576},
                            "systemUsage_1min": {"value": 7},
                            "systemUsage_5mins": {"value": 7},
                            "systemUsageRecent": {"value": 7},
                            "vsize": {"value": 2515959808},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/tmm.start": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/tmm.start?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 6979},
                            "procName": {"description": "tmm.start"},
                            "rss": {"value": 606208},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 4435968},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/tmrouted": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/tmrouted?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6666},
                            "procName": {"description": "tmrouted"},
                            "rss": {"value": 7020544},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 61726720},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/tmsh": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/tmsh?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 11302},
                            "procName": {"description": "tmsh"},
                            "rss": {"value": 88043520},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 312111104},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/vmtoolsd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/vmtoolsd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1476},
                            "procName": {"description": "vmtoolsd"},
                            "rss": {"value": 2310144},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 274087936},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/vxland": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/vxland?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ltm"},
                            "pid": {"value": 5269},
                            "procName": {"description": "vxland"},
                            "rss": {"value": 22552576},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 33849344},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/watchdog~0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/watchdog~0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 10},
                            "procName": {"description": "watchdog/0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/watchdog~1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/watchdog~1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 11},
                            "procName": {"description": "watchdog/1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/wccpd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/wccpd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 6668},
                            "procName": {"description": "wccpd"},
                            "rss": {"value": 5165056},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 29282304},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/writeback": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/writeback?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 20},
                            "procName": {"description": "writeback"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/zrd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/zrd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "gtm"},
                            "pid": {"value": 5645},
                            "procName": {"description": "zrd"},
                            "rss": {"value": 4988928},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 36515840},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/zxfrd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/zxfrd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6677},
                            "procName": {"description": "zxfrd"},
                            "rss": {"value": 6373376},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 72843264},
                        },
                    }
                },
            },
        }


class test_get_sys_proc_info(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:proc-info:proc-infocollectionstats",
            "selfLink": "https://localhost/mgmt/tm/sys/proc-info?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/proc-info/acpid": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/acpid?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1491},
                            "procName": {"description": "acpid"},
                            "rss": {"value": 417792},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 4468736},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/agetty": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/agetty?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3968},
                            "procName": {"description": "agetty"},
                            "rss": {"value": 720896},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 112709632},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/alertd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/alertd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 1},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4076},
                            "procName": {"description": "alertd"},
                            "rss": {"value": 8040448},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 1},
                            "vsize": {"value": 37986304},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ata_sff": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ata_sff?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 214},
                            "procName": {"description": "ata_sff"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/audit_forwarder": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/audit_forwarder?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 12437},
                            "procName": {"description": "audit_forwarder"},
                            "rss": {"value": 23527424},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 42450944},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/auditd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/auditd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1451},
                            "procName": {"description": "auditd"},
                            "rss": {"value": 909312},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 57954304},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/bash": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/bash?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 11276},
                            "procName": {"description": "bash"},
                            "rss": {"value": 1392640},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 120291328},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/big3d": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/big3d?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6982},
                            "procName": {"description": "big3d"},
                            "rss": {"value": 1441792},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 9531392},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/bigd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/bigd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 5985},
                            "procName": {"description": "bigd"},
                            "rss": {"value": 24707072},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 58867712},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/bioset": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/bioset?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 328},
                            "procName": {"description": "bioset"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/cbrd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/cbrd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4793},
                            "procName": {"description": "cbrd"},
                            "rss": {"value": 22028288},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 57978880},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/chmand": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/chmand?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 7404},
                            "procName": {"description": "chmand"},
                            "rss": {"value": 32055296},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 168353792},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/crond": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/crond?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3059},
                            "procName": {"description": "crond"},
                            "rss": {"value": 1114112},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 129314816},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/crypto": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/crypto?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 34},
                            "procName": {"description": "crypto"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/csyncd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/csyncd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4075},
                            "procName": {"description": "csyncd"},
                            "rss": {"value": 31768576},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 41467904},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/dbus-daemon": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/dbus-daemon?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1483},
                            "procName": {"description": "dbus-daemon"},
                            "rss": {"value": 1687552},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 62091264},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/deferwq": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/deferwq?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 66},
                            "procName": {"description": "deferwq"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/devmgmtd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/devmgmtd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6343},
                            "procName": {"description": "devmgmtd"},
                            "rss": {"value": 25640960},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 38453248},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/dynconfd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/dynconfd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 7407},
                            "procName": {"description": "dynconfd"},
                            "rss": {"value": 18882560},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 98295808},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/errdefsd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/errdefsd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4338},
                            "procName": {"description": "errdefsd"},
                            "rss": {"value": 6799360},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 102580224},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/eventd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/eventd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6981},
                            "procName": {"description": "eventd"},
                            "rss": {"value": 24473600},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 53141504},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/evrouted": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/evrouted?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4790},
                            "procName": {"description": "evrouted"},
                            "rss": {"value": 24981504},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 32747520},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ext4-rsv-conver": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ext4-rsv-conver?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1420},
                            "procName": {"description": "ext4-rsv-conver"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/f5-rest-node": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/f5-rest-node?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6673},
                            "procName": {"description": "f5-rest-node"},
                            "rss": {"value": 51097600},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 1284382720},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/fsnotify_mark": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/fsnotify_mark?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 33},
                            "procName": {"description": "fsnotify_mark"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/gtmd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/gtmd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "gtm"},
                            "pid": {"value": 6336},
                            "procName": {"description": "gtmd"},
                            "rss": {"value": 9117696},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 125489152},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/httpd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/httpd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 1},
                            "cpuUsage_5mins": {"value": 1},
                            "cpuUsageRecent": {"value": 2},
                            "modules": {"description": "ui"},
                            "pid": {"value": 11337},
                            "procName": {"description": "httpd"},
                            "rss": {"value": 10199040},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 1},
                            "vsize": {"value": 121319424},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/iControlPortal.": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/iControlPortal.?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 3936},
                            "procName": {"description": "iControlPortal."},
                            "rss": {"value": 61763584},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 306618368},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ib-comp-wq": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ib-comp-wq?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1633},
                            "procName": {"description": "ib-comp-wq"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ib_mcast": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ib_mcast?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1634},
                            "procName": {"description": "ib_mcast"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ib_nl_sa_wq": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ib_nl_sa_wq?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1635},
                            "procName": {"description": "ib_nl_sa_wq"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/icr_eventd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/icr_eventd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 7780},
                            "procName": {"description": "icr_eventd"},
                            "rss": {"value": 24915968},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 43819008},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/icrd_child": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/icrd_child?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 2},
                            "cpuUsage_5mins": {"value": 1},
                            "cpuUsageRecent": {"value": 5},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 9974},
                            "procName": {"description": "icrd_child"},
                            "rss": {"value": 106045440},
                            "systemUsage_1min": {"value": 1},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 2},
                            "vsize": {"value": 401657856},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/increase_entrop": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/increase_entrop?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1531},
                            "procName": {"description": "increase_entrop"},
                            "rss": {"value": 126976},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 8646656},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ipoib_flush": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ipoib_flush?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1707},
                            "procName": {"description": "ipoib_flush"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/iprepd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/iprepd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ltm"},
                            "pid": {"value": 6676},
                            "procName": {"description": "iprepd"},
                            "rss": {"value": 24903680},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 32817152},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ipv6_addrconf": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ipv6_addrconf?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 46},
                            "procName": {"description": "ipv6_addrconf"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/irqbalance": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/irqbalance?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1480},
                            "procName": {"description": "irqbalance"},
                            "rss": {"value": 1024000},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 22155264},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/java": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/java?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 5},
                            "cpuUsage_5mins": {"value": 14},
                            "cpuUsageRecent": {"value": 10},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 5978},
                            "procName": {"description": "java"},
                            "rss": {"value": 259293184},
                            "systemUsage_1min": {"value": 2},
                            "systemUsage_5mins": {"value": 7},
                            "systemUsageRecent": {"value": 5},
                            "vsize": {"value": 454184960},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-1-8": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-1-8?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1403},
                            "procName": {"description": "jbd2/dm-1-8"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-3-8": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-3-8?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1419},
                            "procName": {"description": "jbd2/dm-3-8"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-5-8": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-5-8?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 359},
                            "procName": {"description": "jbd2/dm-5-8"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-6-8": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-6-8?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 382},
                            "procName": {"description": "jbd2/dm-6-8"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-7-8": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-7-8?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1398},
                            "procName": {"description": "jbd2/dm-7-8"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-8-8": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jbd2~dm-8-8?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1395},
                            "procName": {"description": "jbd2/dm-8-8"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/jitterentropy-r": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/jitterentropy-r?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 1},
                            "cpuUsage_5mins": {"value": 1},
                            "cpuUsageRecent": {"value": 1},
                            "modules": {"description": " "},
                            "pid": {"value": 1424},
                            "procName": {"description": "jitterentropy-r"},
                            "rss": {"value": 528384},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 1},
                            "vsize": {"value": 4440064},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kauditd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kauditd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 98},
                            "procName": {"description": "kauditd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kblockd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kblockd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 23},
                            "procName": {"description": "kblockd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kdevtmpfs": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kdevtmpfs?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 17},
                            "procName": {"description": "kdevtmpfs"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kdmflush": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kdmflush?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 325},
                            "procName": {"description": "kdmflush"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/keymgmtd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/keymgmtd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6347},
                            "procName": {"description": "keymgmtd"},
                            "rss": {"value": 26259456},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 134991872},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/khungtaskd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/khungtaskd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 19},
                            "procName": {"description": "khungtaskd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kintegrityd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kintegrityd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 21},
                            "procName": {"description": "kintegrityd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kjournald": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kjournald?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1412},
                            "procName": {"description": "kjournald"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kmpath_rdacd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kmpath_rdacd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 44},
                            "procName": {"description": "kmpath_rdacd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kpsmoused": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kpsmoused?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 45},
                            "procName": {"description": "kpsmoused"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ksmd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ksmd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 32},
                            "procName": {"description": "ksmd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ksoftirqd~0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ksoftirqd~0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3},
                            "procName": {"description": "ksoftirqd/0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ksoftirqd~1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ksoftirqd~1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 13},
                            "procName": {"description": "ksoftirqd/1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kswapd0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kswapd0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 31},
                            "procName": {"description": "kswapd0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kthreadd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kthreadd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 2},
                            "procName": {"description": "kthreadd"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kthrotld": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kthrotld?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 42},
                            "procName": {"description": "kthrotld"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~0:0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~0:0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 21252},
                            "procName": {"description": "kworker/0:0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~0:0H": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~0:0H?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 5},
                            "procName": {"description": "kworker/0:0H"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~0:1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~0:1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 13469},
                            "procName": {"description": "kworker/0:1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~0:1H": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~0:1H?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3192},
                            "procName": {"description": "kworker/0:1H"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~0:2": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~0:2?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 12651},
                            "procName": {"description": "kworker/0:2"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~0:3": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~0:3?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 25342},
                            "procName": {"description": "kworker/0:3"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~1:0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~1:0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 18261},
                            "procName": {"description": "kworker/1:0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~1:0H": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~1:0H?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 15},
                            "procName": {"description": "kworker/1:0H"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~1:1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~1:1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 13210},
                            "procName": {"description": "kworker/1:1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~1:1H": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~1:1H?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 2108},
                            "procName": {"description": "kworker/1:1H"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~1:2": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~1:2?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 24324},
                            "procName": {"description": "kworker/1:2"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~1:3": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~1:3?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 27344},
                            "procName": {"description": "kworker/1:3"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~u4:0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~u4:0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 24248},
                            "procName": {"description": "kworker/u4:0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~u4:1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~u4:1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 11303},
                            "procName": {"description": "kworker/u4:1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/kworker~u4:3": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/kworker~u4:3?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 15388},
                            "procName": {"description": "kworker/u4:3"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/lacpd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/lacpd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 5974},
                            "procName": {"description": "lacpd"},
                            "rss": {"value": 32919552},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 32948224},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/lind": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/lind?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4789},
                            "procName": {"description": "lind"},
                            "rss": {"value": 22274048},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 29831168},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/logger": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/logger?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 3925},
                            "procName": {"description": "logger"},
                            "rss": {"value": 761856},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 6619136},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/login": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/login?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3966},
                            "procName": {"description": "login"},
                            "rss": {"value": 3899392},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 124059648},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/logstatd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/logstatd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 7403},
                            "procName": {"description": "logstatd"},
                            "rss": {"value": 24719360},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 129613824},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/lvmetad": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/lvmetad?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 439},
                            "procName": {"description": "lvmetad"},
                            "rss": {"value": 897024},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 208973824},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mcpd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mcpd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 3},
                            "cpuUsage_5mins": {"value": 1},
                            "cpuUsageRecent": {"value": 8},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4791},
                            "procName": {"description": "mcpd"},
                            "rss": {"value": 98238464},
                            "systemUsage_1min": {"value": 1},
                            "systemUsage_5mins": {"value": 1},
                            "systemUsageRecent": {"value": 4},
                            "vsize": {"value": 223965184},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mcpq": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mcpq?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ui"},
                            "pid": {"value": 3933},
                            "procName": {"description": "mcpq"},
                            "rss": {"value": 14176256},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 63414272},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/md": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/md?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 24},
                            "procName": {"description": "md"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/merged": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/merged?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 4329},
                            "procName": {"description": "merged"},
                            "rss": {"value": 16146432},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 103100416},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mgmt_acld": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mgmt_acld?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 7409},
                            "procName": {"description": "mgmt_acld"},
                            "rss": {"value": 24735744},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 166834176},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/migration~0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/migration~0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 7},
                            "procName": {"description": "migration/0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/migration~1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/migration~1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 12},
                            "procName": {"description": "migration/1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mlx4": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mlx4?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1625},
                            "procName": {"description": "mlx4"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mlx4_ib": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mlx4_ib?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1637},
                            "procName": {"description": "mlx4_ib"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mlx4_ib_mcg": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mlx4_ib_mcg?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1638},
                            "procName": {"description": "mlx4_ib_mcg"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mpt~0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mpt~0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 218},
                            "procName": {"description": "mpt/0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/mpt_poll_0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/mpt_poll_0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 215},
                            "procName": {"description": "mpt_poll_0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/named": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/named?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 10605},
                            "procName": {"description": "named"},
                            "rss": {"value": 52920320},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 92078080},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/netns": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/netns?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 18},
                            "procName": {"description": "netns"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/nfit": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/nfit?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 516},
                            "procName": {"description": "nfit"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ntlmconnpool": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ntlmconnpool?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6345},
                            "procName": {"description": "ntlmconnpool"},
                            "rss": {"value": 999424},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 6164480},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/ntpd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/ntpd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3664},
                            "procName": {"description": "ntpd"},
                            "rss": {"value": 1216512},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 50196480},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/overdog": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/overdog?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 3147},
                            "procName": {"description": "overdog"},
                            "rss": {"value": 89669632},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 90861568},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/pccd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/pccd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 4078},
                            "procName": {"description": "pccd"},
                            "rss": {"value": 24129536},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 130392064},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/promptstatusd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/promptstatusd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 3058},
                            "procName": {"description": "promptstatusd"},
                            "rss": {"value": 15966208},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 86048768},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/racoon": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/racoon?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ltm"},
                            "pid": {"value": 10049},
                            "procName": {"description": "racoon"},
                            "rss": {"value": 888832},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 13733888},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rcu_bh": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rcu_bh?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 8},
                            "procName": {"description": "rcu_bh"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rcu_sched": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rcu_sched?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 9},
                            "procName": {"description": "rcu_sched"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rdma_cm": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rdma_cm?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1717},
                            "procName": {"description": "rdma_cm"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rm": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rm?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 9694},
                            "procName": {"description": "rm"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rrdshim": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rrdshim?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 9872},
                            "procName": {"description": "rrdshim"},
                            "rss": {"value": 2039808},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 11100160},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rrdstats": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rrdstats?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ui"},
                            "pid": {"value": 3934},
                            "procName": {"description": "rrdstats"},
                            "rss": {"value": 962560},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 4419584},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/rtstats": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/rtstats?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ui"},
                            "pid": {"value": 3935},
                            "procName": {"description": "rtstats"},
                            "rss": {"value": 720896},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 4157440},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/runsm1_named": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/runsm1_named?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6348},
                            "procName": {"description": "runsm1_named"},
                            "rss": {"value": 3039232},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 25669632},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/runsv": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/runsv?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 7775},
                            "procName": {"description": "runsv"},
                            "rss": {"value": 208896},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 2179072},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/runsvdir": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/runsvdir?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3937},
                            "procName": {"description": "runsvdir"},
                            "rss": {"value": 380928},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 2330624},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scriptd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scriptd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 7405},
                            "procName": {"description": "scriptd"},
                            "rss": {"value": 84062208},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 288526336},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scsi_eh_0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scsi_eh_0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 221},
                            "procName": {"description": "scsi_eh_0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scsi_eh_1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scsi_eh_1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 223},
                            "procName": {"description": "scsi_eh_1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scsi_eh_2": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scsi_eh_2?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 226},
                            "procName": {"description": "scsi_eh_2"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scsi_tmf_0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scsi_tmf_0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 222},
                            "procName": {"description": "scsi_tmf_0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scsi_tmf_1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scsi_tmf_1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 225},
                            "procName": {"description": "scsi_tmf_1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/scsi_tmf_2": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/scsi_tmf_2?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 227},
                            "procName": {"description": "scsi_tmf_2"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/sflow_agent": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/sflow_agent?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ltm"},
                            "pid": {"value": 4074},
                            "procName": {"description": "sflow_agent"},
                            "rss": {"value": 24735744},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 153120768},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/snmpd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/snmpd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 5279},
                            "procName": {"description": "snmpd"},
                            "rss": {"value": 27762688},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 138039296},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/sod": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/sod?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 5648},
                            "procName": {"description": "sod"},
                            "rss": {"value": 82157568},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 83337216},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/sshd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/sshd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3624},
                            "procName": {"description": "sshd"},
                            "rss": {"value": 1060864},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 129302528},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/statsd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/statsd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6346},
                            "procName": {"description": "statsd"},
                            "rss": {"value": 23855104},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 48545792},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/su": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/su?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 6341},
                            "procName": {"description": "su"},
                            "rss": {"value": 3440640},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 118616064},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/syscalld": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/syscalld?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 7779},
                            "procName": {"description": "syscalld"},
                            "rss": {"value": 22446080},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 29843456},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/syslog-ng": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/syslog-ng?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 1},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 2},
                            "modules": {"description": " "},
                            "pid": {"value": 2321},
                            "procName": {"description": "syslog-ng"},
                            "rss": {"value": 6995968},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 1},
                            "vsize": {"value": 260685824},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/systemctl": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/systemctl?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 8489},
                            "procName": {"description": "systemctl"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/systemd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/systemd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1},
                            "procName": {"description": "systemd"},
                            "rss": {"value": 5017600},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 84172800},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/systemd-journal": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/systemd-journal?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 1},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 2},
                            "modules": {"description": " "},
                            "pid": {"value": 416},
                            "procName": {"description": "systemd-journal"},
                            "rss": {"value": 4915200},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 1},
                            "vsize": {"value": 35504128},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/systemd-logind": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/systemd-logind?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 3060},
                            "procName": {"description": "systemd-logind"},
                            "rss": {"value": 1556480},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 25714688},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/systemd-udevd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/systemd-udevd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 448},
                            "procName": {"description": "systemd-udevd"},
                            "rss": {"value": 1196032},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 48214016},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/tamd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/tamd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ltm"},
                            "pid": {"value": 4799},
                            "procName": {"description": "tamd"},
                            "rss": {"value": 4419584},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 38977536},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/tmipsecd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/tmipsecd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ltm"},
                            "pid": {"value": 7402},
                            "procName": {"description": "tmipsecd"},
                            "rss": {"value": 24731648},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 54099968},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/tmm.0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/tmm.0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 15},
                            "cpuUsage_5mins": {"value": 14},
                            "cpuUsageRecent": {"value": 14},
                            "modules": {"description": "tmm"},
                            "pid": {"value": 9762},
                            "procName": {"description": "tmm.0"},
                            "rss": {"value": 117272576},
                            "systemUsage_1min": {"value": 7},
                            "systemUsage_5mins": {"value": 7},
                            "systemUsageRecent": {"value": 7},
                            "vsize": {"value": 2515959808},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/tmm.start": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/tmm.start?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 6979},
                            "procName": {"description": "tmm.start"},
                            "rss": {"value": 606208},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 4435968},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/tmrouted": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/tmrouted?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6666},
                            "procName": {"description": "tmrouted"},
                            "rss": {"value": 7020544},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 61726720},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/tmsh": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/tmsh?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 11302},
                            "procName": {"description": "tmsh"},
                            "rss": {"value": 88043520},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 312111104},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/vmtoolsd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/vmtoolsd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 1476},
                            "procName": {"description": "vmtoolsd"},
                            "rss": {"value": 2310144},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 274087936},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/vxland": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/vxland?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "ltm"},
                            "pid": {"value": 5269},
                            "procName": {"description": "vxland"},
                            "rss": {"value": 22552576},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 33849344},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/watchdog~0": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/watchdog~0?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 10},
                            "procName": {"description": "watchdog/0"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/watchdog~1": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/watchdog~1?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 11},
                            "procName": {"description": "watchdog/1"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/wccpd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/wccpd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 6668},
                            "procName": {"description": "wccpd"},
                            "rss": {"value": 5165056},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 29282304},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/writeback": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/writeback?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": " "},
                            "pid": {"value": 20},
                            "procName": {"description": "writeback"},
                            "rss": {"value": 0},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 0},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/zrd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/zrd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "gtm"},
                            "pid": {"value": 5645},
                            "procName": {"description": "zrd"},
                            "rss": {"value": 4988928},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 36515840},
                        },
                    }
                },
                "https://localhost/mgmt/tm/sys/proc-info/zxfrd": {
                    "nestedStats": {
                        "kind": "tm:sys:proc-info:proc-infostats",
                        "selfLink": "https://localhost/mgmt/tm/sys/proc-info/zxfrd?ver=14.1.2.1",
                        "entries": {
                            "bladeNum": {"value": 0},
                            "cpuUsage_1min": {"value": 0},
                            "cpuUsage_5mins": {"value": 0},
                            "cpuUsageRecent": {"value": 0},
                            "modules": {"description": "mgmt"},
                            "pid": {"value": 6677},
                            "procName": {"description": "zxfrd"},
                            "rss": {"value": 6373376},
                            "systemUsage_1min": {"value": 0},
                            "systemUsage_5mins": {"value": 0},
                            "systemUsageRecent": {"value": 0},
                            "vsize": {"value": 72843264},
                        },
                    }
                },
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysProcinfo(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysProcinfo(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
