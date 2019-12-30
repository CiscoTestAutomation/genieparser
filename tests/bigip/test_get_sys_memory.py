# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_memory
from genie.libs.parser.bigip.get_sys_memory import SysMemory

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/memory'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:memory:memorystats",
            "selfLink": "https://localhost/mgmt/tm/sys/memory?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/memory/memory-host": {
                    "nestedStats": {
                        "entries": {
                            "https://localhost/mgmt/tm/sys/memory/memory-host/0": {
                                "nestedStats": {
                                    "entries": {
                                        "hostId": {"description": "0"},
                                        "memoryFree": {"value": 2245963008},
                                        "memoryTotal": {"value": 4145995776},
                                        "memoryUsed": {"value": 1900032768},
                                        "otherMemoryFree": {
                                            "value": 325689344
                                        },
                                        "otherMemoryTotal": {
                                            "value": 1990123520
                                        },
                                        "otherMemoryUsed": {
                                            "value": 1664434176
                                        },
                                        "swapFree": {"value": 926441472},
                                        "swapTotal": {"value": 1048571904},
                                        "swapUsed": {"value": 122130432},
                                        "tmmMemoryFree": {"value": 1920273664},
                                        "tmmMemoryTotal": {
                                            "value": 2155872256
                                        },
                                        "tmmMemoryUsed": {"value": 235598592},
                                    }
                                }
                            }
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/memory/memory-subsys": {
                    "nestedStats": {
                        "entries": {
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/AAA_IVS_CTX": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "AAA_IVS_CTX"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ADM%20Mitigation": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ADM Mitigation"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ADM%20Statistics": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ADM Statistics"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/APMD%20proxy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "APMD proxy"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Application%20Family%20Name": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2117936},
                                        "maxAllocated": {"value": 2117936},
                                        "tmName": {
                                            "description": "Application Family Name"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Application%20filter": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 417792},
                                        "maxAllocated": {"value": 417792},
                                        "tmName": {
                                            "description": "Application filter"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/BIGTCP%20PKTSEG%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "BIGTCP PKTSEG cache"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Bot%20Defense": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 186064},
                                        "maxAllocated": {"value": 186064},
                                        "tmName": {
                                            "description": "Bot Defense"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Content%20Analysis": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Content Analysis"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Content%20Classification": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 139264},
                                        "maxAllocated": {"value": 139264},
                                        "tmName": {
                                            "description": "Content Classification"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DHCP%20lease%20query%20transaction": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "DHCP lease query transaction"
                                        },
                                        "size": {"value": 2128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DHCPv4%20transaction": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "DHCPv4 transaction"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DHCPv6%20transaction": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "DHCPv6 transaction"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DNS%20DOS%20profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "DNS DOS profile"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DoS%20Layer%207": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 9136},
                                        "maxAllocated": {"value": 9136},
                                        "tmName": {
                                            "description": "DoS Layer 7"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DoS%20Layer%207%20ACY": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "DoS Layer 7 ACY"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DoS%20Network%20Whitelist": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 127664},
                                        "maxAllocated": {"value": 127664},
                                        "tmName": {
                                            "description": "DoS Network Whitelist"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ECM": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3248},
                                        "maxAllocated": {"value": 3248},
                                        "tmName": {"description": "ECM"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/FPS": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 108768},
                                        "maxAllocated": {"value": 108768},
                                        "tmName": {"description": "FPS"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/FPS%20Configuration": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 540096},
                                        "maxAllocated": {"value": 540096},
                                        "tmName": {
                                            "description": "FPS Configuration"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Firewall%20BDoS": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Firewall BDoS"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Firewall%20FQDN": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Firewall FQDN"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Firewall%20NAT": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 10240},
                                        "maxAllocated": {"value": 10240},
                                        "tmName": {
                                            "description": "Firewall NAT"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IKE%20DEVBUF": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "IKE DEVBUF"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IKE%20LIB": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 5536},
                                        "maxAllocated": {"value": 5536},
                                        "tmName": {"description": "IKE LIB"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IKE%20VBUF": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 29312},
                                        "maxAllocated": {"value": 29312},
                                        "tmName": {"description": "IKE VBUF"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IKEV2": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 5250560},
                                        "maxAllocated": {"value": 5250560},
                                        "tmName": {"description": "IKEV2"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IPFIX%20MDS": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "IPFIX MDS"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IPFIX%20Proxy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "IPFIX Proxy"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IPFIX%20iRules": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "IPFIX iRules"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/In-TMM%20monitoring%20activity": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "In-TMM monitoring activity"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/L3%20Rate%20Limit": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "L3 Rate Limit"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/LSN": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 103424},
                                        "maxAllocated": {"value": 103432},
                                        "tmName": {"description": "LSN"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/LTM%20addr%20list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "LTM addr list"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Layer%202%20Opaque": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Layer 2 Opaque"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Log%20Profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4352},
                                        "maxAllocated": {"value": 4352},
                                        "tmName": {
                                            "description": "Log Profile"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/MW_HASH_COOKIE": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "MW_HASH_COOKIE"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/MW_HASH_TOPIC": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2240},
                                        "maxAllocated": {"value": 2240},
                                        "tmName": {
                                            "description": "MW_HASH_TOPIC"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/NETFLOW": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "NETFLOW"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/NIST%20CAVS%20tests": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "NIST CAVS tests"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/NSH": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "NSH"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Netflow%20Protected%20Server": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Netflow Protected Server"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Network%20DoS%20profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Network DoS profile"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/OAuth": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 252104},
                                        "maxAllocated": {"value": 252104},
                                        "tmName": {"description": "OAuth"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/OAuth%20Database": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 112},
                                        "maxAllocated": {"value": 112},
                                        "tmName": {
                                            "description": "OAuth Database"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/PEM%20PSC%20CFINFO": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "PEM PSC CFINFO"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/PEM%20Subscriber%20Context": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "PEM Subscriber Context"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/PSPM%20PSC%20session%20delete%20context": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "PSPM PSC session delete context"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Quality%20Qf%20Experience": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Quality Qf Experience"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/RLE%20bitmap": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "RLE bitmap"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Radius%20AAA": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Radius AAA"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Rate%20shaper%20flow_key%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Rate shaper flow_key cache"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SCRUBBER%20PUBLISHER": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "SCRUBBER PUBLISHER"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SCTP%20buffer": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "SCTP buffer"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SCTP%20chunk": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "SCTP chunk"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SFC": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "SFC"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SIP%20DOS%20profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "SIP DOS profile"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SSL%20Orchestrator": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "SSL Orchestrator"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SSP_SPM_POLICY_CACHE": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "SSP_SPM_POLICY_CACHE"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Shared%20IPTBL": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 528608},
                                        "maxAllocated": {"value": 528608},
                                        "tmName": {
                                            "description": "Shared IPTBL"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP4%20SACK": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "TCP4 SACK"},
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP4%20SACK%20hole": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "TCP4 SACK hole"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP4%20lost%20segment": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "TCP4 lost segment"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP4%20segment": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "TCP4 segment"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP%20SACK": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 640},
                                        "maxAllocated": {"value": 640},
                                        "tmName": {"description": "TCP SACK"},
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP%20SACK%20hole": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "TCP SACK hole"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP%20lost%20segment": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "TCP lost segment"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP%20qdiffsample%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "TCP qdiffsample cache"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP%20segment": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 160},
                                        "tmName": {
                                            "description": "TCP segment"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TMC%20key": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "TMC key"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Tmstat%20internal%20structures": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 953832},
                                        "maxAllocated": {"value": 953832},
                                        "tmName": {
                                            "description": "Tmstat internal structures"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Traffic%20Matching%20Criteria": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 664416},
                                        "maxAllocated": {"value": 664416},
                                        "tmName": {
                                            "description": "Traffic Matching Criteria"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/URL%20Categorization%20Library": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 86176},
                                        "maxAllocated": {"value": 86176},
                                        "tmName": {
                                            "description": "URL Categorization Library"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/URL%20Classification": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 80},
                                        "maxAllocated": {"value": 80},
                                        "tmName": {
                                            "description": "URL Classification"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Unit%20Testing": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Unit Testing"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2369600},
                                        "maxAllocated": {"value": 2369600},
                                        "tmName": {"description": "access"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access2": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 640},
                                        "maxAllocated": {"value": 640},
                                        "tmName": {"description": "access2"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_acp_msg": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_acp_msg"
                                        },
                                        "size": {"value": 64000},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_bwc_items": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_bwc_items"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_log_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 512},
                                        "maxAllocated": {"value": 512},
                                        "tmName": {
                                            "description": "access_log_entries"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_profile_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_profile_entry"
                                        },
                                        "size": {"value": 1280},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_session_batch": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_session_batch"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_session_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_session_data"
                                        },
                                        "size": {"value": 512},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_session_items": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_session_items"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_session_variables": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_session_variables"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_slist_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_slist_entry"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_str_t": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_str_t"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_uri_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_uri_info"
                                        },
                                        "size": {"value": 8248},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_uuid_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_uuid_entries"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_whitelist_uri_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 542720},
                                        "maxAllocated": {"value": 542720},
                                        "tmName": {
                                            "description": "access_whitelist_uri_entries"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acl": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 12512},
                                        "maxAllocated": {"value": 12512},
                                        "tmName": {"description": "acl"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acl%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "acl cache"},
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acl_build_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "acl_build_ctx"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acl_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "acl_entry"},
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acl_hudnode_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "acl_hudnode_data"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acl_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "acl_item"},
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acs_hudnode_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "acs_hudnode_data"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acs_queue_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "acs_queue_data"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/address_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "address_entry"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/api_path_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "api_path_entries"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/api_profile_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 5392},
                                        "maxAllocated": {"value": 5392},
                                        "tmName": {
                                            "description": "api_profile_entries"
                                        },
                                        "size": {"value": 2696},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/api_server_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "api_server_entries"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apiprotection": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 64},
                                        "maxAllocated": {"value": 64},
                                        "tmName": {
                                            "description": "apiprotection"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apm_app_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "apm_app_item"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apm_log_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 262336},
                                        "maxAllocated": {"value": 262336},
                                        "tmName": {
                                            "description": "apm_log_entries"
                                        },
                                        "size": {"value": 65584},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apm_log_profile_access_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "apm_log_profile_access_entries"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apm_log_profile_access_item_ent": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "apm_log_profile_access_item_ent"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apm_resource_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "apm_resource_info"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apm_resource_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "apm_resource_item"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/auth": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1536},
                                        "maxAllocated": {"value": 1536},
                                        "tmName": {"description": "auth"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/auth_domain": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "auth_domain"
                                        },
                                        "size": {"value": 5168},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/avr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 128},
                                        "maxAllocated": {"value": 128},
                                        "tmName": {"description": "avr"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/bbr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "bbr"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/bigip_connection": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 6912},
                                        "maxAllocated": {"value": 13824},
                                        "tmName": {
                                            "description": "bigip_connection"
                                        },
                                        "size": {"value": 768},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/bwc": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1794048},
                                        "maxAllocated": {"value": 1794048},
                                        "tmName": {"description": "bwc"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/bwc_flow_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "bwc_flow_ctx"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/bwc_measure_instance": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "bwc_measure_instance"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/bwc_shaper": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "bwc_shaper"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/cec": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1232},
                                        "maxAllocated": {"value": 1232},
                                        "tmName": {"description": "cec"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/cec_table_item_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "cec_table_item_cache"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/centralized%20management": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 110144},
                                        "maxAllocated": {"value": 110144},
                                        "tmName": {
                                            "description": "centralized management"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/cipher": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 40960},
                                        "maxAllocated": {"value": 40960},
                                        "tmName": {"description": "cipher"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/citrix_client_bundle": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 160},
                                        "maxAllocated": {"value": 160},
                                        "tmName": {
                                            "description": "citrix_client_bundle"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/client_policy_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1792},
                                        "maxAllocated": {"value": 1792},
                                        "tmName": {
                                            "description": "client_policy_entries"
                                        },
                                        "size": {"value": 896},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/clientssl_certkeychain_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 480},
                                        "maxAllocated": {"value": 480},
                                        "tmName": {
                                            "description": "clientssl_certkeychain_list"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/clientssl_ocsp_stapling_paramet": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "clientssl_ocsp_stapling_paramet"
                                        },
                                        "size": {"value": 9272},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/cmp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 192},
                                        "maxAllocated": {"value": 192},
                                        "tmName": {"description": "cmp"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/config_snapshots": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "config_snapshots"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/connector": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "connector"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/connflow": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3072},
                                        "maxAllocated": {"value": 3072},
                                        "tmName": {"description": "connflow"},
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/crl_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "crl_list"},
                                        "size": {"value": 2072},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/crypto%20codec": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 128},
                                        "maxAllocated": {"value": 128},
                                        "tmName": {
                                            "description": "crypto codec"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/crypto_irule_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "crypto_irule_ctx"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/crypto_transport_server_req_cac": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "crypto_transport_server_req_cac"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ctc_req_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ctc_req_cache"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ctc_req_ctx_dh_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ctc_req_ctx_dh_cache"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ctc_req_ctx_ecdh_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ctc_req_ctx_ecdh_cache"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/cubic%20data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "cubic data"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dag": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "dag"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/data%20sync%20lib": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "data sync lib"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dedup": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "dedup"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dedup_xact_op_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dedup_xact_op_ctx"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/deflate": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "deflate"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/devbuf": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2794672},
                                        "maxAllocated": {"value": 2794672},
                                        "tmName": {"description": "devbuf"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dhcp_leasequery_transaction_cac": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dhcp_leasequery_transaction_cac"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dhcp_transaction_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dhcp_transaction_cache"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dht": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 18176},
                                        "maxAllocated": {"value": 18176},
                                        "tmName": {"description": "dht"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dht%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1792},
                                        "maxAllocated": {"value": 1792},
                                        "tmName": {"description": "dht cache"},
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dht_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "dht_entry"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dht_reply_hud_token": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dht_reply_hud_token"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dht_request": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dht_request"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dht_request_local": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dht_request_local"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/diam_msg": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "diam_msg"},
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/diam_retrans": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "diam_retrans"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns64_entry_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dns64_entry_cache"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns%20cache%20resolver": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dns cache resolver"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns%20cache%20resolver%20ub%20ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dns cache resolver ub ctx"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns%20express": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 77184},
                                        "maxAllocated": {"value": 77184},
                                        "tmName": {
                                            "description": "dns express"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns%20security": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 224},
                                        "maxAllocated": {"value": 224},
                                        "tmName": {
                                            "description": "dns security"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns_hw_cfg_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dns_hw_cfg_cache"
                                        },
                                        "size": {"value": 69664},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns_ldns": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "dns_ldns"},
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns_path": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "dns_path"},
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns_persistence": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dns_persistence"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns_qname_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dns_qname_cache"
                                        },
                                        "size": {"value": 1280},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_pkt": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_pkt"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_rrset": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_rrset"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_rrsig": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_rrsig"
                                        },
                                        "size": {"value": 4248},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_sig_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_sig_cache"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_xfr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_xfr"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_xfr_ns_target": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_xfr_ns_target"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_xfr_nsec3": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_xfr_nsec3"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dpi": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 34480},
                                        "maxAllocated": {"value": 34480},
                                        "tmName": {"description": "dpi"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dpi_shared_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dpi_shared_pcb"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/drop_policy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 320},
                                        "maxAllocated": {"value": 320},
                                        "tmName": {
                                            "description": "drop_policy"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dynad": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "dynad"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/errdefs": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 220584},
                                        "maxAllocated": {"value": 220584},
                                        "tmName": {"description": "errdefs"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/evtimer": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 192},
                                        "maxAllocated": {"value": 192},
                                        "tmName": {"description": "evtimer"},
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fad_address_bnode": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 640},
                                        "maxAllocated": {"value": 640},
                                        "tmName": {
                                            "description": "fad_address_bnode"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fad_program_listener_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fad_program_listener_info"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fad_string_map_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fad_string_map_entry"
                                        },
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fad_string_map_hash": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fad_string_map_hash"
                                        },
                                        "size": {"value": 512},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fast_dns_pl_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fast_dns_pl_cache"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/filter": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1124576},
                                        "maxAllocated": {"value": 1124576},
                                        "tmName": {"description": "filter"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/flow%20forwarding": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 6295664},
                                        "maxAllocated": {"value": 6295664},
                                        "tmName": {
                                            "description": "flow forwarding"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/flow%20streams": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "flow streams"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::crypto_req_ctx_rsa": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::crypto_req_ctx_rsa"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::crypto_req_rsa_cipher": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::crypto_req_rsa_cipher"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_alert": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_alert"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_auto_trans": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_auto_trans"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_bait": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_bait"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_bait_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_bait_list"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_custom_alert_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_custom_alert_list"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_custom_alert_raw_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_custom_alert_raw_list"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_decrypt_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_decrypt_data"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_found_custom_alert": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_found_custom_alert"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_found_encrypted_param": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_found_encrypted_param"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_found_inject_tag": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_found_inject_tag"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_global_url": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_global_url"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_global_url_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_global_url_info"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_header_custom_alert": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_header_custom_alert"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_header_custom_alert_li": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_header_custom_alert_li"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_ip_custom_alert": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_ip_custom_alert"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_malware": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_malware"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_malware_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_malware_info"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_malware_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_malware_list"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_mobilesafe": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1280},
                                        "maxAllocated": {"value": 1280},
                                        "tmName": {
                                            "description": "fps::fps_mobilesafe"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_mobilesafe_common": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_mobilesafe_common"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_mobilesafe_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_mobilesafe_data"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_mobilesafe_mitm_domain": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_mobilesafe_mitm_domain"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_mobilesafe_os": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_mobilesafe_os"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_parameter": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1792},
                                        "maxAllocated": {"value": 1792},
                                        "tmName": {
                                            "description": "fps::fps_parameter"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_parameter_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 48},
                                        "maxAllocated": {"value": 48},
                                        "tmName": {
                                            "description": "fps::fps_parameter_list"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_parameter_parser": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_parameter_parser"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_pcb"
                                        },
                                        "size": {"value": 1536},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 384},
                                        "maxAllocated": {"value": 384},
                                        "tmName": {
                                            "description": "fps::fps_profile"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_profile_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 8192},
                                        "maxAllocated": {"value": 8192},
                                        "tmName": {
                                            "description": "fps::fps_profile_info"
                                        },
                                        "size": {"value": 2048},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_rule": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_rule"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_rule_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_rule_list"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_shared_ptr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 240},
                                        "maxAllocated": {"value": 240},
                                        "tmName": {
                                            "description": "fps::fps_shared_ptr"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_str_custom_alert": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_str_custom_alert"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_url": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 640},
                                        "maxAllocated": {"value": 640},
                                        "tmName": {
                                            "description": "fps::fps_url"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_url_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2048},
                                        "maxAllocated": {"value": 2048},
                                        "tmName": {
                                            "description": "fps::fps_url_info"
                                        },
                                        "size": {"value": 1024},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_url_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 48},
                                        "maxAllocated": {"value": 48},
                                        "tmName": {
                                            "description": "fps::fps_url_list"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_user_full_record": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_user_full_record"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_user_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_user_info"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_vcrypt_staging_mode_da": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_vcrypt_staging_mode_da"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fred_cb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "fred_cb"},
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fred_flow_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fred_flow_data"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/gpa": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 33792},
                                        "maxAllocated": {"value": 33792},
                                        "tmName": {"description": "gpa"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/gpa_applications": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 450352},
                                        "maxAllocated": {"value": 450352},
                                        "tmName": {
                                            "description": "gpa_applications"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/gpa_categories": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 19968},
                                        "maxAllocated": {"value": 19968},
                                        "tmName": {
                                            "description": "gpa_categories"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/gpa_classif_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "gpa_classif_pcb"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/gpa_shared_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "gpa_shared_pcb"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/gpa_urlcats": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 33280},
                                        "maxAllocated": {"value": 33280},
                                        "tmName": {
                                            "description": "gpa_urlcats"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ha_context_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ha_context_cache"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ha_cursor_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ha_cursor_cache"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/html%20rule": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 8192},
                                        "maxAllocated": {"value": 8192},
                                        "tmName": {"description": "html rule"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/html_rule": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "html_rule"},
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/html_rule_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "html_rule_list"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/http_ck_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "http_ck_cache"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/http_cookie": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "http_cookie"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/http_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "http_data"},
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/http_persist": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "http_persist"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/hud_message_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "hud_message_ctx"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/hud_oob": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "hud_oob"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ifc": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 13824},
                                        "maxAllocated": {"value": 13824},
                                        "tmName": {"description": "ifc"},
                                        "size": {"value": 768},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ifnet": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 5345744},
                                        "maxAllocated": {"value": 5345744},
                                        "tmName": {"description": "ifnet"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ifvirt_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ifvirt_entry"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ike_crypto_req_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ike_crypto_req_cache"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ike_peer": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ike_peer"},
                                        "size": {"value": 512},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ike_req": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ike_req"},
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/inst_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "inst_entry"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/internal_proxy_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "internal_proxy_list"
                                        },
                                        "size": {"value": 4128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipfix_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipfix_cache"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipfix_conn_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipfix_conn_cache"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipfix_repo_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipfix_repo_cache"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipfix_template_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipfix_template_cache"
                                        },
                                        "size": {"value": 384},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1434512},
                                        "maxAllocated": {"value": 1434512},
                                        "tmName": {"description": "ips"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-insection-profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 293760},
                                        "maxAllocated": {"value": 293760},
                                        "tmName": {
                                            "description": "ips-insection-profile"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-inspection": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 558400},
                                        "maxAllocated": {"value": 558400},
                                        "tmName": {
                                            "description": "ips-inspection"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-profile-status": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 240},
                                        "maxAllocated": {"value": 240},
                                        "tmName": {
                                            "description": "ips-profile-status"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-service": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1200},
                                        "maxAllocated": {"value": 1200},
                                        "tmName": {
                                            "description": "ips-service"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-service-port-profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2688},
                                        "maxAllocated": {"value": 2688},
                                        "tmName": {
                                            "description": "ips-service-port-profile"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-service-profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1664},
                                        "maxAllocated": {"value": 1664},
                                        "tmName": {
                                            "description": "ips-service-profile"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-service-profile-filter": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips-service-profile-filter"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_diameter_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_diameter_pcb_cache_20190917"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_dns_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_dns_pcb_cache_20190917"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_ftp_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_ftp_pcb_cache_20190917"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_imap_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_imap_pcb_cache_20190917"
                                        },
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_mqtt_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_mqtt_pcb_cache_20190917"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_mysql_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_mysql_pcb_cache_20190917"
                                        },
                                        "size": {"value": 768},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_pcb_cache_20190917"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_radius_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_radius_pcb_cache_20190917"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_sip_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_sip_pcb_cache_20190917"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_smtp_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_smtp_pcb_cache_20190917"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_snmp_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_snmp_pcb_cache_20190917"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_tftp_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_tftp_pcb_cache_20190917"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipsec_crypto_req_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipsec_crypto_req_cache"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipsec_enc_auth_ctx_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipsec_enc_auth_ctx_cache"
                                        },
                                        "size": {"value": 616},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipsec_ike_ctx_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipsec_ike_ctx_cache"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipsec_ipcomp_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipsec_ipcomp_cache"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipsec_policy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipsec_policy"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/isess%20rid": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "isess rid"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/isession": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 147712},
                                        "maxAllocated": {"value": 147712},
                                        "tmName": {"description": "isession"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/isession_abort_stat": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "isession_abort_stat"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/isession_virt_compress_stats": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "isession_virt_compress_stats"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/isession_virt_stat": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "isession_virt_stat"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/join_cert_validator_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "join_cert_validator_list"
                                        },
                                        "size": {"value": 3176},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/km_crl_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "km_crl_ctx"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/km_ocsp_concurrent_conn_lim": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "km_ocsp_concurrent_conn_lim"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/km_ocsp_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "km_ocsp_ctx"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/l7%20policy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1594816},
                                        "maxAllocated": {"value": 1594816},
                                        "tmName": {"description": "l7 policy"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/laddr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 7680},
                                        "maxAllocated": {"value": 7680},
                                        "tmName": {"description": "laddr"},
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lasthop": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1152},
                                        "maxAllocated": {"value": 1792},
                                        "tmName": {"description": "lasthop"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/leasepool": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "leasepool"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/leasepool%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "leasepool cache"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/leasepool_mbr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "leasepool_mbr"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/libldns": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 145712},
                                        "maxAllocated": {"value": 145712},
                                        "tmName": {"description": "libldns"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/listener": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2101696},
                                        "maxAllocated": {"value": 2101696},
                                        "tmName": {"description": "listener"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/listener%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 507136},
                                        "maxAllocated": {"value": 517888},
                                        "tmName": {
                                            "description": "listener cache"
                                        },
                                        "size": {"value": 896},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/listener%20key": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2097792},
                                        "maxAllocated": {"value": 2097792},
                                        "tmName": {
                                            "description": "listener key"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/listener%20key%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 181120},
                                        "maxAllocated": {"value": 184960},
                                        "tmName": {
                                            "description": "listener key cache"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/local_route": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "local_route"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/loop_nexthop": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "loop_nexthop"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lsn%20inbound%20bitmap": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "lsn inbound bitmap"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lsn_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "lsn_entry"},
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lsn_inbound_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "lsn_inbound_entry"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lsn_pool": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "lsn_pool"},
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lsn_prefix": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "lsn_prefix"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lw4o6_tbl_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "lw4o6_tbl_entry"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mac_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mac_entry"},
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/malloc": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 36097240},
                                        "maxAllocated": {"value": 36097240},
                                        "tmName": {"description": "malloc"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mblb_assoc%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mblb_assoc cache"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mblb_harness%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mblb_harness cache"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mblb_message%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mblb_message cache"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mblb_swinfo%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mblb_swinfo cache"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mco%20db": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 41943072},
                                        "maxAllocated": {"value": 41943072},
                                        "tmName": {"description": "mco db"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mcp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4251664},
                                        "maxAllocated": {"value": 4251664},
                                        "tmName": {"description": "mcp"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mds_btree_nodes": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3200},
                                        "maxAllocated": {"value": 3200},
                                        "tmName": {
                                            "description": "mds_btree_nodes"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mds_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mds_cache"},
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mds_connset": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mds_connset"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mds_message": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mds_message"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/memcache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 96},
                                        "maxAllocated": {"value": 96},
                                        "tmName": {"description": "memcache"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/memcache%20request%20items": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "memcache request items"
                                        },
                                        "size": {"value": 1792},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/messagerouter": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 336},
                                        "maxAllocated": {"value": 336},
                                        "tmName": {
                                            "description": "messagerouter"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/method": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2928},
                                        "maxAllocated": {"value": 2928},
                                        "tmName": {"description": "method"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mobile%20app%20manager": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mobile app manager"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/monitor%20agent": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 24576},
                                        "maxAllocated": {"value": 24576},
                                        "tmName": {
                                            "description": "monitor agent"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/monitor_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "monitor_ctx"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mpi_request": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mpi_request"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mqtt_message": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mqtt_message"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mqtt_slab": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mqtt_slab"},
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/multicast": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "multicast"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_cookie": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 64},
                                        "maxAllocated": {"value": 64},
                                        "tmName": {"description": "mw_cookie"},
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_kv": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mw_kv"},
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_msg": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mw_msg"},
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_msgbus": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 66048},
                                        "maxAllocated": {"value": 66048},
                                        "tmName": {"description": "mw_msgbus"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_msgp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mw_msgp"},
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_pub": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1152},
                                        "maxAllocated": {"value": 1152},
                                        "tmName": {"description": "mw_pub"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_sub": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 640},
                                        "maxAllocated": {"value": 640},
                                        "tmName": {"description": "mw_sub"},
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_work": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mw_work"},
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/neighbor_advertiser_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 640},
                                        "tmName": {
                                            "description": "neighbor_advertiser_entry"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/neighbor_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 14720},
                                        "maxAllocated": {"value": 14720},
                                        "tmName": {
                                            "description": "neighbor_entry"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/net_ip": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1056},
                                        "maxAllocated": {"value": 1056},
                                        "tmName": {"description": "net_ip"},
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/network%20access": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 144},
                                        "maxAllocated": {"value": 144},
                                        "tmName": {
                                            "description": "network access"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/network%20access%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "network access cache"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/nps%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "nps cache"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_agent_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_agent_item"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_claim_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_claim_entries"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_client_app_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_client_app_entries"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_client_app_scope_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_client_app_scope_entries"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_client_app_scope_item_ent": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_client_app_scope_item_ent"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_crypto_contexts": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_crypto_contexts"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_crypto_key_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_crypto_key_entries"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_db_instance_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 32},
                                        "maxAllocated": {"value": 32},
                                        "tmName": {
                                            "description": "oauth_db_instance_entries"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_jwk_config_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_jwk_config_entries"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_profile_client_app_entrie": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_profile_client_app_entrie"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_profile_client_app_item_e": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_profile_client_app_item_e"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_profile_jwk_config_entrie": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_profile_jwk_config_entrie"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_profile_jwk_config_item_e": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_profile_jwk_config_item_e"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_profile_resource_server_e": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_profile_resource_server_e"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_profile_resource_server_i": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_profile_resource_server_i"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_request_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 14976},
                                        "maxAllocated": {"value": 14976},
                                        "tmName": {
                                            "description": "oauth_request_item"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_resource_server_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_resource_server_entries"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_scope_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_scope_entries"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ocsp_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ocsp_list"},
                                        "size": {"value": 4216},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ocsp_trans_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ocsp_trans_list"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/packet": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 999552},
                                        "maxAllocated": {"value": 999552},
                                        "tmName": {"description": "packet"},
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pcp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 69856},
                                        "maxAllocated": {"value": 69856},
                                        "tmName": {"description": "pcp"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pcp_prefix": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pcp_prefix"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/peer_iclient": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "peer_iclient"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/peer_isession": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "peer_isession"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/peer_route": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "peer_route"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/peer_woc": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "peer_woc"},
                                        "size": {"value": 384},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2188976},
                                        "maxAllocated": {"value": 2188976},
                                        "tmName": {"description": "pem"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem%20format%20script": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem format script"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem%20forwarding%20endpoint": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem forwarding endpoint"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem%20intercept%20endpoint": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem intercept endpoint"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem%20service%20chain%20endpoint": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem service chain endpoint"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem_flow_bwc_handles": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem_flow_bwc_handles"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem_hud_cb_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem_hud_cb_data"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem_tcl_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem_tcl_info"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/persist": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "persist"},
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/persistence": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 448},
                                        "maxAllocated": {"value": 448},
                                        "tmName": {
                                            "description": "persistence"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pfkey_msg_stat": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1280},
                                        "maxAllocated": {"value": 1280},
                                        "tmName": {
                                            "description": "pfkey_msg_stat"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pingaccess": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pingaccess"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/plugin": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 431552},
                                        "maxAllocated": {"value": 431552},
                                        "tmName": {"description": "plugin"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/plugin_message": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "plugin_message"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/policy_nexthop": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "policy_nexthop"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pool": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 71872},
                                        "maxAllocated": {"value": 71872},
                                        "tmName": {"description": "pool"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pool%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 16640},
                                        "maxAllocated": {"value": 16640},
                                        "tmName": {
                                            "description": "pool cache"
                                        },
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/poolmbr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 43008},
                                        "maxAllocated": {"value": 43008},
                                        "tmName": {"description": "poolmbr"},
                                        "size": {"value": 512},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/poolprio": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "poolprio"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/port%20set": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 36096},
                                        "maxAllocated": {"value": 36864},
                                        "tmName": {"description": "port set"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pq": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "pq"},
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/private": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "private"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3142144},
                                        "maxAllocated": {"value": 3142144},
                                        "tmName": {"description": "profile"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1325312},
                                        "maxAllocated": {"value": 1325312},
                                        "tmName": {"description": "proxy"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy%20exclude": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "proxy exclude"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy_common_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 1280},
                                        "tmName": {
                                            "description": "proxy_common_cache"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy_common_pending_msg": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "proxy_common_pending_msg"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy_connect_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "proxy_connect_data"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "proxy_ctx"},
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy_tuple": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "proxy_tuple"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pva": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "pva"},
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/queueing_method": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 256},
                                        "maxAllocated": {"value": 256},
                                        "tmName": {
                                            "description": "queueing_method"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/radius%20server": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4096},
                                        "maxAllocated": {"value": 4096},
                                        "tmName": {
                                            "description": "radius server"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/radius_server": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "radius_server"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ramcache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 140000},
                                        "maxAllocated": {"value": 140000},
                                        "tmName": {"description": "ramcache"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ramcache%20document": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ramcache document"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ramcache%20entity": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ramcache entity"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ramcache%20resource": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ramcache resource"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rate%20shaper": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "rate shaper"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rate%20tracker": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "rate tracker"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rateclass": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "rateclass"},
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rateclass_queue": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "rateclass_queue"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rateshaper": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "rateshaper"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/red_cb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "red_cb"},
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/regex": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "regex"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/remote%20desktop": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "remote desktop"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/resolv": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 768},
                                        "maxAllocated": {"value": 768},
                                        "tmName": {"description": "resolv"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/resolv_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "resolv_cache"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/resolv_query": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "resolv_query"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/response_config_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "response_config_entries"
                                        },
                                        "size": {"value": 384},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/response_config_header_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "response_config_header_entries"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rewrite%20profile%20rules": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 432},
                                        "maxAllocated": {"value": 432},
                                        "tmName": {
                                            "description": "rewrite profile rules"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/router%20advertisement": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "router advertisement"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rt_dom": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "rt_dom"},
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rt_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 7680},
                                        "maxAllocated": {"value": 7680},
                                        "tmName": {"description": "rt_entry"},
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rtm_internal": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "rtm_internal"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rules": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 89648},
                                        "maxAllocated": {"value": 89648},
                                        "tmName": {"description": "rules"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sPVA": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 112},
                                        "maxAllocated": {"value": 112},
                                        "tmName": {"description": "sPVA"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sandbox_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 262368},
                                        "maxAllocated": {"value": 262368},
                                        "tmName": {
                                            "description": "sandbox_entries"
                                        },
                                        "size": {"value": 65592},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sandbox_file_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sandbox_file_entries"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sandbox_profile_access_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sandbox_profile_access_entries"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sandbox_profile_access_item_ent": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sandbox_profile_access_item_ent"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sb_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "sb_cache"},
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sctp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 224},
                                        "maxAllocated": {"value": 224},
                                        "tmName": {"description": "sctp"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sctp_ports_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sctp_ports_cache"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/security%20log%20profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 20624},
                                        "maxAllocated": {"value": 20624},
                                        "tmName": {
                                            "description": "security log profile"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/selfip": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4800},
                                        "maxAllocated": {"value": 4800},
                                        "tmName": {"description": "selfip"},
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/service": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1280},
                                        "maxAllocated": {"value": 1280},
                                        "tmName": {"description": "service"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/service%20policy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "service policy"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/session": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2109568},
                                        "maxAllocated": {"value": 2109568},
                                        "tmName": {"description": "session"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/session%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1408},
                                        "maxAllocated": {"value": 1408},
                                        "tmName": {
                                            "description": "session cache"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/session%20master%20key": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 528},
                                        "maxAllocated": {"value": 528},
                                        "tmName": {
                                            "description": "session master key"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/session%20pdq": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "session pdq"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/session_leasepool_mbr_table": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "session_leasepool_mbr_table"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sfc_errors_stat": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sfc_errors_stat"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/shaper_domain": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 32},
                                        "maxAllocated": {"value": 32},
                                        "tmName": {
                                            "description": "shaper_domain"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/shared_var_context": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "shared_var_context"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sip_dialog": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sip_dialog"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sip_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "sip_entry"},
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sip_header_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sip_header_cache"
                                        },
                                        "size": {"value": 2056},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sip_msg": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "sip_msg"},
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sip_node_ack_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sip_node_ack_cache"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sipmsg": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "sipmsg"},
                                        "size": {"value": 768},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/source%20addr%20translation": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 768},
                                        "maxAllocated": {"value": 768},
                                        "tmName": {
                                            "description": "source addr translation"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_local_hash": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_local_hash"
                                        },
                                        "size": {"value": 1024},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_mult_ip_data_stat": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_mult_ip_data_stat"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_policy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_policy"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_session_create_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_session_create_ctx"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_session_ip_mapping_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_session_ip_mapping_ctx"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_session_timer_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_session_timer_ctx"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_session_update_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_session_update_ctx"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_subs_id_update_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_subs_id_update_ctx"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_towerid_local_hash": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_towerid_local_hash"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4287408},
                                        "maxAllocated": {"value": 4287408},
                                        "tmName": {"description": "ssl"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_basic": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_basic"},
                                        "size": {"value": 752},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_bulk_crypto_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_bulk_crypto_ctx"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_cn": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_cn"},
                                        "size": {"value": 1192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_cn_req": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_cn_req"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_compat": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 312496},
                                        "maxAllocated": {"value": 312496},
                                        "tmName": {
                                            "description": "ssl_compat"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_dht_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_dht_data"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_dht_key": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_dht_key"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_hs": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_hs"},
                                        "size": {"value": 6216},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_hs_m": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_hs_m"},
                                        "size": {"value": 16384},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_keys": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_keys"},
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 112000},
                                        "maxAllocated": {"value": 112000},
                                        "tmName": {
                                            "description": "ssl_profile"
                                        },
                                        "size": {"value": 7000},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_proxy_profile_hash": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_proxy_profile_hash"
                                        },
                                        "size": {"value": 512},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_rd": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_rd"},
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_session": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_session"
                                        },
                                        "size": {"value": 296},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_sni": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_sni"},
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_sni_profile_hash": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_sni_profile_hash"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_sni_profile_hash_cert": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_sni_profile_hash_cert"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4096},
                                        "maxAllocated": {"value": 4096},
                                        "tmName": {"description": "sso"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso::sso_config": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2983360},
                                        "maxAllocated": {"value": 2983360},
                                        "tmName": {
                                            "description": "sso::sso_config"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso::sso_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sso::sso_pcb"
                                        },
                                        "size": {"value": 2080},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso::sso_plugin": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sso::sso_plugin"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso::sso_saml": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sso::sso_saml"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso::xml_parser": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3539248},
                                        "maxAllocated": {"value": 3539248},
                                        "tmName": {
                                            "description": "sso::xml_parser"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso_config": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sso_config"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso_config_jwt_claim_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sso_config_jwt_claim_entries"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso_config_jwt_claim_item_entri": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sso_config_jwt_claim_item_entri"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/streamflow": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "streamflow"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/string%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 499000},
                                        "maxAllocated": {"value": 499000},
                                        "tmName": {
                                            "description": "string cache"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/subscriber_id_cookie_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "subscriber_id_cookie_cache"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sw_crypto_req_ctx_dh_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sw_crypto_req_ctx_dh_cache"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sw_crypto_req_ctx_dsa_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sw_crypto_req_ctx_dsa_cache"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sw_crypto_req_ctx_ecdh_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sw_crypto_req_ctx_ecdh_cache"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sw_crypto_req_ctx_ecdsa_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sw_crypto_req_ctx_ecdsa_cache"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sw_crypto_req_ctx_rsa_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 32},
                                        "maxAllocated": {"value": 32},
                                        "tmName": {
                                            "description": "sw_crypto_req_ctx_rsa_cache"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sw_crypto_req_ctx_sm2_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sw_crypto_req_ctx_sm2_cache"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sweeper": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 12176},
                                        "maxAllocated": {"value": 12176},
                                        "tmName": {"description": "sweeper"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tacacsplus_server": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "tacacsplus_server"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tacplus%20server": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4096},
                                        "maxAllocated": {"value": 4096},
                                        "tmName": {
                                            "description": "tacplus server"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tcl": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 7369984},
                                        "maxAllocated": {"value": 7369984},
                                        "tmName": {"description": "tcl"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tcl_ip_addr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1248},
                                        "maxAllocated": {"value": 1248},
                                        "tmName": {
                                            "description": "tcl_ip_addr"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tclrule_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3584},
                                        "maxAllocated": {"value": 3584},
                                        "tmName": {
                                            "description": "tclrule_pcb"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tclrule_pcb_children": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "tclrule_pcb_children"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/temp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 264976},
                                        "maxAllocated": {"value": 264976},
                                        "tmName": {"description": "temp"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/thread%20stacks": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 17203200},
                                        "maxAllocated": {"value": 17203200},
                                        "tmName": {
                                            "description": "thread stacks"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tm_header_cache_entry_slab": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 768},
                                        "maxAllocated": {"value": 768},
                                        "tmName": {
                                            "description": "tm_header_cache_entry_slab"
                                        },
                                        "size": {"value": 384},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tm_opaque": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 72},
                                        "maxAllocated": {"value": 144},
                                        "tmName": {"description": "tm_opaque"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tm_sys": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 92576},
                                        "maxAllocated": {"value": 92576},
                                        "tmName": {"description": "tm_sys"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tmc%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "tmc cache"},
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tmc%20key%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "tmc key cache"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tmc_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "tmc_entry"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tmjail": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 23104},
                                        "maxAllocated": {"value": 23104},
                                        "tmName": {"description": "tmjail"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/traffic%20class": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "traffic class"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/traffic%20class%20tables": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "traffic class tables"
                                        },
                                        "size": {"value": 896},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/traffic%20managment%20interface": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 24304},
                                        "maxAllocated": {"value": 24304},
                                        "tmName": {
                                            "description": "traffic managment interface"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/traffic_selector": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "traffic_selector"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tsig_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "tsig_ctx"},
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tsig_req_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "tsig_req_ctx"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tunnel_nexthop": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 768},
                                        "maxAllocated": {"value": 768},
                                        "tmName": {
                                            "description": "tunnel_nexthop"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/umem": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 33404928},
                                        "maxAllocated": {"value": 35663032},
                                        "tmName": {"description": "umem"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/umem%20dynamic%20leak%20util": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "umem dynamic leak util"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/url%20filter": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 672032},
                                        "maxAllocated": {"value": 672032},
                                        "tmName": {
                                            "description": "url filter"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/url_filter_log_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 256},
                                        "maxAllocated": {"value": 256},
                                        "tmName": {
                                            "description": "url_filter_log_entries"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/urlc_cloud_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "urlc_cloud_cache"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/vaddr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 7840},
                                        "maxAllocated": {"value": 8064},
                                        "tmName": {"description": "vaddr"},
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/vcmp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3968},
                                        "maxAllocated": {"value": 3968},
                                        "tmName": {"description": "vcmp"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/vpn_na_item_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "vpn_na_item_entries"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/vpn_session_data_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "vpn_session_data_entries"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wa_resource_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wa_resource_item"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::assembly": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4352},
                                        "maxAllocated": {"value": 4352},
                                        "tmName": {
                                            "description": "wam::assembly"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2560},
                                        "maxAllocated": {"value": 2560},
                                        "tmName": {
                                            "description": "wam::cache"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::config": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 168512},
                                        "maxAllocated": {"value": 168512},
                                        "tmName": {
                                            "description": "wam::config"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::css_parser": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::css_parser"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::html_parser": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 52064},
                                        "maxAllocated": {"value": 52064},
                                        "tmName": {
                                            "description": "wam::html_parser"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::js_parser": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::js_parser"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::m3u8_parser": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::m3u8_parser"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::mstor": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::mstor"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::mstor_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::mstor_ctx"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::mstor_object": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::mstor_object"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::mstor_op": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::mstor_op"
                                        },
                                        "size": {"value": 1792},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::mtag": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "wam::mtag"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::normalization": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::normalization"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::plugin": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::plugin"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::roistats_bucket": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::roistats_bucket"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::stats_bucket": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::stats_bucket"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::stdlib": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 7200},
                                        "maxAllocated": {"value": 7200},
                                        "tmName": {
                                            "description": "wam::stdlib"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::uci": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "wam::uci"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_annotation": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_annotation"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_assembler": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_assembler"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_bitset_bits": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_bitset_bits"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_dfa": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_dfa"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_dfa_state": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_dfa_state"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_document": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_document"
                                        },
                                        "size": {"value": 512},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_entity": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_entity"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_evt": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1120},
                                        "maxAllocated": {"value": 1120},
                                        "tmName": {
                                            "description": "wam::wam_evt"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_condition": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_condition"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_expression": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_expression"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_map": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_map"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_operand": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_operand"
                                        },
                                        "size": {"value": 384},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_policy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_policy"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_state": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_state"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_string": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_string"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_transition": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_transition"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_nfa_dfa": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_nfa_dfa"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_resource": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_resource"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_resumption_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_resumption_info"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_sink": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_sink"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_transaction": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_transaction"
                                        },
                                        "size": {"value": 1792},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wash_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wash_pcb"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/web%20application": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 16384},
                                        "maxAllocated": {"value": 16384},
                                        "tmName": {
                                            "description": "web application"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/web_application": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "web_application"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/web_application_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "web_application_item"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/westwood%20data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "westwood data"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/work": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 196608},
                                        "maxAllocated": {"value": 196608},
                                        "tmName": {"description": "work"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/xdata": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 61118464},
                                        "maxAllocated": {"value": 61130752},
                                        "tmName": {"description": "xdata"},
                                        "size": {"value": 2048},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/xfr_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "xfr_ctx"},
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/xhead": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 954976},
                                        "maxAllocated": {"value": 955168},
                                        "tmName": {"description": "xhead"},
                                        "size": {"value": 32},
                                    }
                                }
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/memory/memory-tmm": {
                    "nestedStats": {
                        "entries": {
                            "https://localhost/mgmt/tm/sys/memory/memory-tmm/0.0": {
                                "nestedStats": {
                                    "entries": {
                                        "memoryTotal": {"value": 2155872256},
                                        "memoryUsed": {"value": 235599872},
                                        "tmmId": {"description": "0.0"},
                                    }
                                }
                            }
                        }
                    }
                },
            },
        }


class test_get_sys_memory(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
            "kind": "tm:sys:memory:memorystats",
            "selfLink": "https://localhost/mgmt/tm/sys/memory?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/memory/memory-host": {
                    "nestedStats": {
                        "entries": {
                            "https://localhost/mgmt/tm/sys/memory/memory-host/0": {
                                "nestedStats": {
                                    "entries": {
                                        "hostId": {"description": "0"},
                                        "memoryFree": {"value": 2245963008},
                                        "memoryTotal": {"value": 4145995776},
                                        "memoryUsed": {"value": 1900032768},
                                        "otherMemoryFree": {
                                            "value": 325689344
                                        },
                                        "otherMemoryTotal": {
                                            "value": 1990123520
                                        },
                                        "otherMemoryUsed": {
                                            "value": 1664434176
                                        },
                                        "swapFree": {"value": 926441472},
                                        "swapTotal": {"value": 1048571904},
                                        "swapUsed": {"value": 122130432},
                                        "tmmMemoryFree": {"value": 1920273664},
                                        "tmmMemoryTotal": {
                                            "value": 2155872256
                                        },
                                        "tmmMemoryUsed": {"value": 235598592},
                                    }
                                }
                            }
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/memory/memory-subsys": {
                    "nestedStats": {
                        "entries": {
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/AAA_IVS_CTX": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "AAA_IVS_CTX"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ADM%20Mitigation": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ADM Mitigation"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ADM%20Statistics": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ADM Statistics"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/APMD%20proxy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "APMD proxy"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Application%20Family%20Name": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2117936},
                                        "maxAllocated": {"value": 2117936},
                                        "tmName": {
                                            "description": "Application Family Name"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Application%20filter": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 417792},
                                        "maxAllocated": {"value": 417792},
                                        "tmName": {
                                            "description": "Application filter"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/BIGTCP%20PKTSEG%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "BIGTCP PKTSEG cache"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Bot%20Defense": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 186064},
                                        "maxAllocated": {"value": 186064},
                                        "tmName": {
                                            "description": "Bot Defense"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Content%20Analysis": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Content Analysis"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Content%20Classification": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 139264},
                                        "maxAllocated": {"value": 139264},
                                        "tmName": {
                                            "description": "Content Classification"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DHCP%20lease%20query%20transaction": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "DHCP lease query transaction"
                                        },
                                        "size": {"value": 2128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DHCPv4%20transaction": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "DHCPv4 transaction"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DHCPv6%20transaction": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "DHCPv6 transaction"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DNS%20DOS%20profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "DNS DOS profile"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DoS%20Layer%207": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 9136},
                                        "maxAllocated": {"value": 9136},
                                        "tmName": {
                                            "description": "DoS Layer 7"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DoS%20Layer%207%20ACY": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "DoS Layer 7 ACY"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/DoS%20Network%20Whitelist": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 127664},
                                        "maxAllocated": {"value": 127664},
                                        "tmName": {
                                            "description": "DoS Network Whitelist"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ECM": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3248},
                                        "maxAllocated": {"value": 3248},
                                        "tmName": {"description": "ECM"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/FPS": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 108768},
                                        "maxAllocated": {"value": 108768},
                                        "tmName": {"description": "FPS"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/FPS%20Configuration": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 540096},
                                        "maxAllocated": {"value": 540096},
                                        "tmName": {
                                            "description": "FPS Configuration"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Firewall%20BDoS": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Firewall BDoS"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Firewall%20FQDN": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Firewall FQDN"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Firewall%20NAT": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 10240},
                                        "maxAllocated": {"value": 10240},
                                        "tmName": {
                                            "description": "Firewall NAT"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IKE%20DEVBUF": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "IKE DEVBUF"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IKE%20LIB": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 5536},
                                        "maxAllocated": {"value": 5536},
                                        "tmName": {"description": "IKE LIB"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IKE%20VBUF": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 29312},
                                        "maxAllocated": {"value": 29312},
                                        "tmName": {"description": "IKE VBUF"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IKEV2": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 5250560},
                                        "maxAllocated": {"value": 5250560},
                                        "tmName": {"description": "IKEV2"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IPFIX%20MDS": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "IPFIX MDS"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IPFIX%20Proxy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "IPFIX Proxy"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/IPFIX%20iRules": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "IPFIX iRules"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/In-TMM%20monitoring%20activity": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "In-TMM monitoring activity"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/L3%20Rate%20Limit": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "L3 Rate Limit"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/LSN": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 103424},
                                        "maxAllocated": {"value": 103432},
                                        "tmName": {"description": "LSN"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/LTM%20addr%20list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "LTM addr list"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Layer%202%20Opaque": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Layer 2 Opaque"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Log%20Profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4352},
                                        "maxAllocated": {"value": 4352},
                                        "tmName": {
                                            "description": "Log Profile"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/MW_HASH_COOKIE": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "MW_HASH_COOKIE"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/MW_HASH_TOPIC": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2240},
                                        "maxAllocated": {"value": 2240},
                                        "tmName": {
                                            "description": "MW_HASH_TOPIC"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/NETFLOW": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "NETFLOW"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/NIST%20CAVS%20tests": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "NIST CAVS tests"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/NSH": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "NSH"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Netflow%20Protected%20Server": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Netflow Protected Server"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Network%20DoS%20profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Network DoS profile"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/OAuth": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 252104},
                                        "maxAllocated": {"value": 252104},
                                        "tmName": {"description": "OAuth"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/OAuth%20Database": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 112},
                                        "maxAllocated": {"value": 112},
                                        "tmName": {
                                            "description": "OAuth Database"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/PEM%20PSC%20CFINFO": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "PEM PSC CFINFO"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/PEM%20Subscriber%20Context": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "PEM Subscriber Context"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/PSPM%20PSC%20session%20delete%20context": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "PSPM PSC session delete context"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Quality%20Qf%20Experience": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Quality Qf Experience"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/RLE%20bitmap": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "RLE bitmap"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Radius%20AAA": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Radius AAA"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Rate%20shaper%20flow_key%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Rate shaper flow_key cache"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SCRUBBER%20PUBLISHER": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "SCRUBBER PUBLISHER"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SCTP%20buffer": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "SCTP buffer"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SCTP%20chunk": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "SCTP chunk"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SFC": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "SFC"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SIP%20DOS%20profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "SIP DOS profile"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SSL%20Orchestrator": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "SSL Orchestrator"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/SSP_SPM_POLICY_CACHE": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "SSP_SPM_POLICY_CACHE"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Shared%20IPTBL": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 528608},
                                        "maxAllocated": {"value": 528608},
                                        "tmName": {
                                            "description": "Shared IPTBL"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP4%20SACK": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "TCP4 SACK"},
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP4%20SACK%20hole": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "TCP4 SACK hole"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP4%20lost%20segment": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "TCP4 lost segment"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP4%20segment": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "TCP4 segment"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP%20SACK": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 640},
                                        "maxAllocated": {"value": 640},
                                        "tmName": {"description": "TCP SACK"},
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP%20SACK%20hole": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "TCP SACK hole"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP%20lost%20segment": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "TCP lost segment"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP%20qdiffsample%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "TCP qdiffsample cache"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TCP%20segment": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 160},
                                        "tmName": {
                                            "description": "TCP segment"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/TMC%20key": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "TMC key"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Tmstat%20internal%20structures": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 953832},
                                        "maxAllocated": {"value": 953832},
                                        "tmName": {
                                            "description": "Tmstat internal structures"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Traffic%20Matching%20Criteria": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 664416},
                                        "maxAllocated": {"value": 664416},
                                        "tmName": {
                                            "description": "Traffic Matching Criteria"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/URL%20Categorization%20Library": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 86176},
                                        "maxAllocated": {"value": 86176},
                                        "tmName": {
                                            "description": "URL Categorization Library"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/URL%20Classification": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 80},
                                        "maxAllocated": {"value": 80},
                                        "tmName": {
                                            "description": "URL Classification"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/Unit%20Testing": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "Unit Testing"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2369600},
                                        "maxAllocated": {"value": 2369600},
                                        "tmName": {"description": "access"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access2": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 640},
                                        "maxAllocated": {"value": 640},
                                        "tmName": {"description": "access2"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_acp_msg": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_acp_msg"
                                        },
                                        "size": {"value": 64000},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_bwc_items": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_bwc_items"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_log_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 512},
                                        "maxAllocated": {"value": 512},
                                        "tmName": {
                                            "description": "access_log_entries"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_profile_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_profile_entry"
                                        },
                                        "size": {"value": 1280},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_session_batch": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_session_batch"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_session_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_session_data"
                                        },
                                        "size": {"value": 512},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_session_items": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_session_items"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_session_variables": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_session_variables"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_slist_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_slist_entry"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_str_t": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_str_t"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_uri_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_uri_info"
                                        },
                                        "size": {"value": 8248},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_uuid_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "access_uuid_entries"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/access_whitelist_uri_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 542720},
                                        "maxAllocated": {"value": 542720},
                                        "tmName": {
                                            "description": "access_whitelist_uri_entries"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acl": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 12512},
                                        "maxAllocated": {"value": 12512},
                                        "tmName": {"description": "acl"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acl%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "acl cache"},
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acl_build_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "acl_build_ctx"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acl_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "acl_entry"},
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acl_hudnode_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "acl_hudnode_data"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acl_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "acl_item"},
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acs_hudnode_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "acs_hudnode_data"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/acs_queue_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "acs_queue_data"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/address_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "address_entry"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/api_path_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "api_path_entries"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/api_profile_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 5392},
                                        "maxAllocated": {"value": 5392},
                                        "tmName": {
                                            "description": "api_profile_entries"
                                        },
                                        "size": {"value": 2696},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/api_server_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "api_server_entries"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apiprotection": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 64},
                                        "maxAllocated": {"value": 64},
                                        "tmName": {
                                            "description": "apiprotection"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apm_app_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "apm_app_item"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apm_log_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 262336},
                                        "maxAllocated": {"value": 262336},
                                        "tmName": {
                                            "description": "apm_log_entries"
                                        },
                                        "size": {"value": 65584},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apm_log_profile_access_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "apm_log_profile_access_entries"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apm_log_profile_access_item_ent": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "apm_log_profile_access_item_ent"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apm_resource_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "apm_resource_info"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/apm_resource_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "apm_resource_item"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/auth": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1536},
                                        "maxAllocated": {"value": 1536},
                                        "tmName": {"description": "auth"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/auth_domain": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "auth_domain"
                                        },
                                        "size": {"value": 5168},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/avr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 128},
                                        "maxAllocated": {"value": 128},
                                        "tmName": {"description": "avr"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/bbr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "bbr"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/bigip_connection": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 6912},
                                        "maxAllocated": {"value": 13824},
                                        "tmName": {
                                            "description": "bigip_connection"
                                        },
                                        "size": {"value": 768},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/bwc": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1794048},
                                        "maxAllocated": {"value": 1794048},
                                        "tmName": {"description": "bwc"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/bwc_flow_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "bwc_flow_ctx"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/bwc_measure_instance": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "bwc_measure_instance"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/bwc_shaper": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "bwc_shaper"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/cec": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1232},
                                        "maxAllocated": {"value": 1232},
                                        "tmName": {"description": "cec"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/cec_table_item_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "cec_table_item_cache"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/centralized%20management": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 110144},
                                        "maxAllocated": {"value": 110144},
                                        "tmName": {
                                            "description": "centralized management"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/cipher": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 40960},
                                        "maxAllocated": {"value": 40960},
                                        "tmName": {"description": "cipher"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/citrix_client_bundle": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 160},
                                        "maxAllocated": {"value": 160},
                                        "tmName": {
                                            "description": "citrix_client_bundle"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/client_policy_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1792},
                                        "maxAllocated": {"value": 1792},
                                        "tmName": {
                                            "description": "client_policy_entries"
                                        },
                                        "size": {"value": 896},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/clientssl_certkeychain_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 480},
                                        "maxAllocated": {"value": 480},
                                        "tmName": {
                                            "description": "clientssl_certkeychain_list"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/clientssl_ocsp_stapling_paramet": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "clientssl_ocsp_stapling_paramet"
                                        },
                                        "size": {"value": 9272},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/cmp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 192},
                                        "maxAllocated": {"value": 192},
                                        "tmName": {"description": "cmp"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/config_snapshots": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "config_snapshots"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/connector": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "connector"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/connflow": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3072},
                                        "maxAllocated": {"value": 3072},
                                        "tmName": {"description": "connflow"},
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/crl_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "crl_list"},
                                        "size": {"value": 2072},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/crypto%20codec": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 128},
                                        "maxAllocated": {"value": 128},
                                        "tmName": {
                                            "description": "crypto codec"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/crypto_irule_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "crypto_irule_ctx"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/crypto_transport_server_req_cac": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "crypto_transport_server_req_cac"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ctc_req_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ctc_req_cache"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ctc_req_ctx_dh_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ctc_req_ctx_dh_cache"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ctc_req_ctx_ecdh_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ctc_req_ctx_ecdh_cache"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/cubic%20data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "cubic data"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dag": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "dag"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/data%20sync%20lib": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "data sync lib"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dedup": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "dedup"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dedup_xact_op_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dedup_xact_op_ctx"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/deflate": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "deflate"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/devbuf": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2794672},
                                        "maxAllocated": {"value": 2794672},
                                        "tmName": {"description": "devbuf"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dhcp_leasequery_transaction_cac": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dhcp_leasequery_transaction_cac"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dhcp_transaction_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dhcp_transaction_cache"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dht": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 18176},
                                        "maxAllocated": {"value": 18176},
                                        "tmName": {"description": "dht"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dht%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1792},
                                        "maxAllocated": {"value": 1792},
                                        "tmName": {"description": "dht cache"},
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dht_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "dht_entry"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dht_reply_hud_token": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dht_reply_hud_token"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dht_request": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dht_request"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dht_request_local": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dht_request_local"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/diam_msg": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "diam_msg"},
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/diam_retrans": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "diam_retrans"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns64_entry_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dns64_entry_cache"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns%20cache%20resolver": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dns cache resolver"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns%20cache%20resolver%20ub%20ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dns cache resolver ub ctx"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns%20express": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 77184},
                                        "maxAllocated": {"value": 77184},
                                        "tmName": {
                                            "description": "dns express"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns%20security": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 224},
                                        "maxAllocated": {"value": 224},
                                        "tmName": {
                                            "description": "dns security"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns_hw_cfg_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dns_hw_cfg_cache"
                                        },
                                        "size": {"value": 69664},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns_ldns": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "dns_ldns"},
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns_path": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "dns_path"},
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns_persistence": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dns_persistence"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dns_qname_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dns_qname_cache"
                                        },
                                        "size": {"value": 1280},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_pkt": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_pkt"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_rrset": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_rrset"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_rrsig": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_rrsig"
                                        },
                                        "size": {"value": 4248},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_sig_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_sig_cache"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_xfr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_xfr"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_xfr_ns_target": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_xfr_ns_target"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dnssec_xfr_nsec3": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dnssec_xfr_nsec3"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dpi": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 34480},
                                        "maxAllocated": {"value": 34480},
                                        "tmName": {"description": "dpi"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dpi_shared_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "dpi_shared_pcb"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/drop_policy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 320},
                                        "maxAllocated": {"value": 320},
                                        "tmName": {
                                            "description": "drop_policy"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/dynad": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "dynad"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/errdefs": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 220584},
                                        "maxAllocated": {"value": 220584},
                                        "tmName": {"description": "errdefs"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/evtimer": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 192},
                                        "maxAllocated": {"value": 192},
                                        "tmName": {"description": "evtimer"},
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fad_address_bnode": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 640},
                                        "maxAllocated": {"value": 640},
                                        "tmName": {
                                            "description": "fad_address_bnode"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fad_program_listener_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fad_program_listener_info"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fad_string_map_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fad_string_map_entry"
                                        },
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fad_string_map_hash": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fad_string_map_hash"
                                        },
                                        "size": {"value": 512},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fast_dns_pl_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fast_dns_pl_cache"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/filter": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1124576},
                                        "maxAllocated": {"value": 1124576},
                                        "tmName": {"description": "filter"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/flow%20forwarding": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 6295664},
                                        "maxAllocated": {"value": 6295664},
                                        "tmName": {
                                            "description": "flow forwarding"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/flow%20streams": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "flow streams"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::crypto_req_ctx_rsa": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::crypto_req_ctx_rsa"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::crypto_req_rsa_cipher": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::crypto_req_rsa_cipher"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_alert": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_alert"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_auto_trans": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_auto_trans"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_bait": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_bait"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_bait_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_bait_list"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_custom_alert_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_custom_alert_list"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_custom_alert_raw_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_custom_alert_raw_list"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_decrypt_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_decrypt_data"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_found_custom_alert": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_found_custom_alert"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_found_encrypted_param": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_found_encrypted_param"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_found_inject_tag": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_found_inject_tag"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_global_url": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_global_url"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_global_url_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_global_url_info"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_header_custom_alert": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_header_custom_alert"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_header_custom_alert_li": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_header_custom_alert_li"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_ip_custom_alert": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_ip_custom_alert"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_malware": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_malware"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_malware_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_malware_info"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_malware_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_malware_list"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_mobilesafe": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1280},
                                        "maxAllocated": {"value": 1280},
                                        "tmName": {
                                            "description": "fps::fps_mobilesafe"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_mobilesafe_common": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_mobilesafe_common"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_mobilesafe_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_mobilesafe_data"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_mobilesafe_mitm_domain": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_mobilesafe_mitm_domain"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_mobilesafe_os": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_mobilesafe_os"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_parameter": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1792},
                                        "maxAllocated": {"value": 1792},
                                        "tmName": {
                                            "description": "fps::fps_parameter"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_parameter_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 48},
                                        "maxAllocated": {"value": 48},
                                        "tmName": {
                                            "description": "fps::fps_parameter_list"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_parameter_parser": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_parameter_parser"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_pcb"
                                        },
                                        "size": {"value": 1536},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 384},
                                        "maxAllocated": {"value": 384},
                                        "tmName": {
                                            "description": "fps::fps_profile"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_profile_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 8192},
                                        "maxAllocated": {"value": 8192},
                                        "tmName": {
                                            "description": "fps::fps_profile_info"
                                        },
                                        "size": {"value": 2048},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_rule": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_rule"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_rule_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_rule_list"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_shared_ptr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 240},
                                        "maxAllocated": {"value": 240},
                                        "tmName": {
                                            "description": "fps::fps_shared_ptr"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_str_custom_alert": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_str_custom_alert"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_url": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 640},
                                        "maxAllocated": {"value": 640},
                                        "tmName": {
                                            "description": "fps::fps_url"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_url_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2048},
                                        "maxAllocated": {"value": 2048},
                                        "tmName": {
                                            "description": "fps::fps_url_info"
                                        },
                                        "size": {"value": 1024},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_url_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 48},
                                        "maxAllocated": {"value": 48},
                                        "tmName": {
                                            "description": "fps::fps_url_list"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_user_full_record": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_user_full_record"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_user_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_user_info"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fps::fps_vcrypt_staging_mode_da": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fps::fps_vcrypt_staging_mode_da"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fred_cb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "fred_cb"},
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/fred_flow_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "fred_flow_data"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/gpa": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 33792},
                                        "maxAllocated": {"value": 33792},
                                        "tmName": {"description": "gpa"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/gpa_applications": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 450352},
                                        "maxAllocated": {"value": 450352},
                                        "tmName": {
                                            "description": "gpa_applications"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/gpa_categories": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 19968},
                                        "maxAllocated": {"value": 19968},
                                        "tmName": {
                                            "description": "gpa_categories"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/gpa_classif_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "gpa_classif_pcb"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/gpa_shared_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "gpa_shared_pcb"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/gpa_urlcats": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 33280},
                                        "maxAllocated": {"value": 33280},
                                        "tmName": {
                                            "description": "gpa_urlcats"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ha_context_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ha_context_cache"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ha_cursor_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ha_cursor_cache"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/html%20rule": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 8192},
                                        "maxAllocated": {"value": 8192},
                                        "tmName": {"description": "html rule"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/html_rule": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "html_rule"},
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/html_rule_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "html_rule_list"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/http_ck_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "http_ck_cache"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/http_cookie": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "http_cookie"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/http_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "http_data"},
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/http_persist": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "http_persist"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/hud_message_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "hud_message_ctx"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/hud_oob": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "hud_oob"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ifc": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 13824},
                                        "maxAllocated": {"value": 13824},
                                        "tmName": {"description": "ifc"},
                                        "size": {"value": 768},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ifnet": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 5345744},
                                        "maxAllocated": {"value": 5345744},
                                        "tmName": {"description": "ifnet"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ifvirt_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ifvirt_entry"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ike_crypto_req_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ike_crypto_req_cache"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ike_peer": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ike_peer"},
                                        "size": {"value": 512},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ike_req": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ike_req"},
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/inst_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "inst_entry"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/internal_proxy_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "internal_proxy_list"
                                        },
                                        "size": {"value": 4128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipfix_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipfix_cache"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipfix_conn_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipfix_conn_cache"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipfix_repo_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipfix_repo_cache"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipfix_template_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipfix_template_cache"
                                        },
                                        "size": {"value": 384},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1434512},
                                        "maxAllocated": {"value": 1434512},
                                        "tmName": {"description": "ips"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-insection-profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 293760},
                                        "maxAllocated": {"value": 293760},
                                        "tmName": {
                                            "description": "ips-insection-profile"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-inspection": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 558400},
                                        "maxAllocated": {"value": 558400},
                                        "tmName": {
                                            "description": "ips-inspection"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-profile-status": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 240},
                                        "maxAllocated": {"value": 240},
                                        "tmName": {
                                            "description": "ips-profile-status"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-service": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1200},
                                        "maxAllocated": {"value": 1200},
                                        "tmName": {
                                            "description": "ips-service"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-service-port-profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2688},
                                        "maxAllocated": {"value": 2688},
                                        "tmName": {
                                            "description": "ips-service-port-profile"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-service-profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1664},
                                        "maxAllocated": {"value": 1664},
                                        "tmName": {
                                            "description": "ips-service-profile"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips-service-profile-filter": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips-service-profile-filter"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_diameter_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_diameter_pcb_cache_20190917"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_dns_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_dns_pcb_cache_20190917"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_ftp_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_ftp_pcb_cache_20190917"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_imap_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_imap_pcb_cache_20190917"
                                        },
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_mqtt_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_mqtt_pcb_cache_20190917"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_mysql_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_mysql_pcb_cache_20190917"
                                        },
                                        "size": {"value": 768},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_pcb_cache_20190917"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_radius_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_radius_pcb_cache_20190917"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_sip_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_sip_pcb_cache_20190917"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_smtp_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_smtp_pcb_cache_20190917"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_snmp_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_snmp_pcb_cache_20190917"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ips_tftp_pcb_cache_20190917": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ips_tftp_pcb_cache_20190917"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipsec_crypto_req_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipsec_crypto_req_cache"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipsec_enc_auth_ctx_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipsec_enc_auth_ctx_cache"
                                        },
                                        "size": {"value": 616},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipsec_ike_ctx_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipsec_ike_ctx_cache"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipsec_ipcomp_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipsec_ipcomp_cache"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ipsec_policy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ipsec_policy"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/isess%20rid": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "isess rid"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/isession": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 147712},
                                        "maxAllocated": {"value": 147712},
                                        "tmName": {"description": "isession"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/isession_abort_stat": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "isession_abort_stat"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/isession_virt_compress_stats": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "isession_virt_compress_stats"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/isession_virt_stat": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "isession_virt_stat"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/join_cert_validator_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "join_cert_validator_list"
                                        },
                                        "size": {"value": 3176},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/km_crl_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "km_crl_ctx"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/km_ocsp_concurrent_conn_lim": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "km_ocsp_concurrent_conn_lim"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/km_ocsp_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "km_ocsp_ctx"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/l7%20policy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1594816},
                                        "maxAllocated": {"value": 1594816},
                                        "tmName": {"description": "l7 policy"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/laddr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 7680},
                                        "maxAllocated": {"value": 7680},
                                        "tmName": {"description": "laddr"},
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lasthop": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1152},
                                        "maxAllocated": {"value": 1792},
                                        "tmName": {"description": "lasthop"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/leasepool": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "leasepool"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/leasepool%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "leasepool cache"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/leasepool_mbr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "leasepool_mbr"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/libldns": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 145712},
                                        "maxAllocated": {"value": 145712},
                                        "tmName": {"description": "libldns"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/listener": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2101696},
                                        "maxAllocated": {"value": 2101696},
                                        "tmName": {"description": "listener"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/listener%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 507136},
                                        "maxAllocated": {"value": 517888},
                                        "tmName": {
                                            "description": "listener cache"
                                        },
                                        "size": {"value": 896},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/listener%20key": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2097792},
                                        "maxAllocated": {"value": 2097792},
                                        "tmName": {
                                            "description": "listener key"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/listener%20key%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 181120},
                                        "maxAllocated": {"value": 184960},
                                        "tmName": {
                                            "description": "listener key cache"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/local_route": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "local_route"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/loop_nexthop": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "loop_nexthop"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lsn%20inbound%20bitmap": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "lsn inbound bitmap"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lsn_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "lsn_entry"},
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lsn_inbound_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "lsn_inbound_entry"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lsn_pool": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "lsn_pool"},
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lsn_prefix": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "lsn_prefix"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/lw4o6_tbl_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "lw4o6_tbl_entry"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mac_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mac_entry"},
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/malloc": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 36097240},
                                        "maxAllocated": {"value": 36097240},
                                        "tmName": {"description": "malloc"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mblb_assoc%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mblb_assoc cache"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mblb_harness%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mblb_harness cache"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mblb_message%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mblb_message cache"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mblb_swinfo%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mblb_swinfo cache"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mco%20db": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 41943072},
                                        "maxAllocated": {"value": 41943072},
                                        "tmName": {"description": "mco db"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mcp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4251664},
                                        "maxAllocated": {"value": 4251664},
                                        "tmName": {"description": "mcp"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mds_btree_nodes": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3200},
                                        "maxAllocated": {"value": 3200},
                                        "tmName": {
                                            "description": "mds_btree_nodes"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mds_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mds_cache"},
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mds_connset": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mds_connset"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mds_message": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mds_message"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/memcache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 96},
                                        "maxAllocated": {"value": 96},
                                        "tmName": {"description": "memcache"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/memcache%20request%20items": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "memcache request items"
                                        },
                                        "size": {"value": 1792},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/messagerouter": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 336},
                                        "maxAllocated": {"value": 336},
                                        "tmName": {
                                            "description": "messagerouter"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/method": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2928},
                                        "maxAllocated": {"value": 2928},
                                        "tmName": {"description": "method"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mobile%20app%20manager": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mobile app manager"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/monitor%20agent": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 24576},
                                        "maxAllocated": {"value": 24576},
                                        "tmName": {
                                            "description": "monitor agent"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/monitor_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "monitor_ctx"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mpi_request": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mpi_request"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mqtt_message": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "mqtt_message"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mqtt_slab": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mqtt_slab"},
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/multicast": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "multicast"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_cookie": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 64},
                                        "maxAllocated": {"value": 64},
                                        "tmName": {"description": "mw_cookie"},
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_kv": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mw_kv"},
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_msg": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mw_msg"},
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_msgbus": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 66048},
                                        "maxAllocated": {"value": 66048},
                                        "tmName": {"description": "mw_msgbus"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_msgp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mw_msgp"},
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_pub": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1152},
                                        "maxAllocated": {"value": 1152},
                                        "tmName": {"description": "mw_pub"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_sub": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 640},
                                        "maxAllocated": {"value": 640},
                                        "tmName": {"description": "mw_sub"},
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/mw_work": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "mw_work"},
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/neighbor_advertiser_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 640},
                                        "tmName": {
                                            "description": "neighbor_advertiser_entry"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/neighbor_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 14720},
                                        "maxAllocated": {"value": 14720},
                                        "tmName": {
                                            "description": "neighbor_entry"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/net_ip": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1056},
                                        "maxAllocated": {"value": 1056},
                                        "tmName": {"description": "net_ip"},
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/network%20access": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 144},
                                        "maxAllocated": {"value": 144},
                                        "tmName": {
                                            "description": "network access"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/network%20access%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "network access cache"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/nps%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "nps cache"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_agent_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_agent_item"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_claim_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_claim_entries"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_client_app_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_client_app_entries"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_client_app_scope_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_client_app_scope_entries"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_client_app_scope_item_ent": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_client_app_scope_item_ent"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_crypto_contexts": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_crypto_contexts"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_crypto_key_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_crypto_key_entries"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_db_instance_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 32},
                                        "maxAllocated": {"value": 32},
                                        "tmName": {
                                            "description": "oauth_db_instance_entries"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_jwk_config_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_jwk_config_entries"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_profile_client_app_entrie": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_profile_client_app_entrie"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_profile_client_app_item_e": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_profile_client_app_item_e"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_profile_jwk_config_entrie": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_profile_jwk_config_entrie"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_profile_jwk_config_item_e": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_profile_jwk_config_item_e"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_profile_resource_server_e": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_profile_resource_server_e"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_profile_resource_server_i": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_profile_resource_server_i"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_request_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 14976},
                                        "maxAllocated": {"value": 14976},
                                        "tmName": {
                                            "description": "oauth_request_item"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_resource_server_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_resource_server_entries"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/oauth_scope_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "oauth_scope_entries"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ocsp_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ocsp_list"},
                                        "size": {"value": 4216},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ocsp_trans_list": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ocsp_trans_list"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/packet": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 999552},
                                        "maxAllocated": {"value": 999552},
                                        "tmName": {"description": "packet"},
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pcp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 69856},
                                        "maxAllocated": {"value": 69856},
                                        "tmName": {"description": "pcp"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pcp_prefix": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pcp_prefix"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/peer_iclient": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "peer_iclient"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/peer_isession": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "peer_isession"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/peer_route": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "peer_route"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/peer_woc": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "peer_woc"},
                                        "size": {"value": 384},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2188976},
                                        "maxAllocated": {"value": 2188976},
                                        "tmName": {"description": "pem"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem%20format%20script": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem format script"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem%20forwarding%20endpoint": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem forwarding endpoint"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem%20intercept%20endpoint": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem intercept endpoint"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem%20service%20chain%20endpoint": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem service chain endpoint"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem_flow_bwc_handles": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem_flow_bwc_handles"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem_hud_cb_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem_hud_cb_data"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pem_tcl_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pem_tcl_info"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/persist": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "persist"},
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/persistence": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 448},
                                        "maxAllocated": {"value": 448},
                                        "tmName": {
                                            "description": "persistence"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pfkey_msg_stat": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1280},
                                        "maxAllocated": {"value": 1280},
                                        "tmName": {
                                            "description": "pfkey_msg_stat"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pingaccess": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "pingaccess"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/plugin": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 431552},
                                        "maxAllocated": {"value": 431552},
                                        "tmName": {"description": "plugin"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/plugin_message": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "plugin_message"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/policy_nexthop": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "policy_nexthop"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pool": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 71872},
                                        "maxAllocated": {"value": 71872},
                                        "tmName": {"description": "pool"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pool%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 16640},
                                        "maxAllocated": {"value": 16640},
                                        "tmName": {
                                            "description": "pool cache"
                                        },
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/poolmbr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 43008},
                                        "maxAllocated": {"value": 43008},
                                        "tmName": {"description": "poolmbr"},
                                        "size": {"value": 512},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/poolprio": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "poolprio"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/port%20set": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 36096},
                                        "maxAllocated": {"value": 36864},
                                        "tmName": {"description": "port set"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pq": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "pq"},
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/private": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "private"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3142144},
                                        "maxAllocated": {"value": 3142144},
                                        "tmName": {"description": "profile"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1325312},
                                        "maxAllocated": {"value": 1325312},
                                        "tmName": {"description": "proxy"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy%20exclude": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "proxy exclude"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy_common_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 1280},
                                        "tmName": {
                                            "description": "proxy_common_cache"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy_common_pending_msg": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "proxy_common_pending_msg"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy_connect_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "proxy_connect_data"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "proxy_ctx"},
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/proxy_tuple": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "proxy_tuple"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/pva": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "pva"},
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/queueing_method": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 256},
                                        "maxAllocated": {"value": 256},
                                        "tmName": {
                                            "description": "queueing_method"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/radius%20server": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4096},
                                        "maxAllocated": {"value": 4096},
                                        "tmName": {
                                            "description": "radius server"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/radius_server": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "radius_server"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ramcache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 140000},
                                        "maxAllocated": {"value": 140000},
                                        "tmName": {"description": "ramcache"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ramcache%20document": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ramcache document"
                                        },
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ramcache%20entity": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ramcache entity"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ramcache%20resource": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ramcache resource"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rate%20shaper": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "rate shaper"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rate%20tracker": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "rate tracker"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rateclass": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "rateclass"},
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rateclass_queue": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "rateclass_queue"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rateshaper": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "rateshaper"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/red_cb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "red_cb"},
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/regex": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "regex"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/remote%20desktop": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "remote desktop"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/resolv": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 768},
                                        "maxAllocated": {"value": 768},
                                        "tmName": {"description": "resolv"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/resolv_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "resolv_cache"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/resolv_query": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "resolv_query"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/response_config_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "response_config_entries"
                                        },
                                        "size": {"value": 384},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/response_config_header_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "response_config_header_entries"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rewrite%20profile%20rules": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 432},
                                        "maxAllocated": {"value": 432},
                                        "tmName": {
                                            "description": "rewrite profile rules"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/router%20advertisement": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "router advertisement"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rt_dom": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "rt_dom"},
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rt_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 7680},
                                        "maxAllocated": {"value": 7680},
                                        "tmName": {"description": "rt_entry"},
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rtm_internal": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "rtm_internal"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/rules": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 89648},
                                        "maxAllocated": {"value": 89648},
                                        "tmName": {"description": "rules"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sPVA": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 112},
                                        "maxAllocated": {"value": 112},
                                        "tmName": {"description": "sPVA"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sandbox_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 262368},
                                        "maxAllocated": {"value": 262368},
                                        "tmName": {
                                            "description": "sandbox_entries"
                                        },
                                        "size": {"value": 65592},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sandbox_file_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sandbox_file_entries"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sandbox_profile_access_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sandbox_profile_access_entries"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sandbox_profile_access_item_ent": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sandbox_profile_access_item_ent"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sb_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "sb_cache"},
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sctp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 224},
                                        "maxAllocated": {"value": 224},
                                        "tmName": {"description": "sctp"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sctp_ports_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sctp_ports_cache"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/security%20log%20profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 20624},
                                        "maxAllocated": {"value": 20624},
                                        "tmName": {
                                            "description": "security log profile"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/selfip": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4800},
                                        "maxAllocated": {"value": 4800},
                                        "tmName": {"description": "selfip"},
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/service": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1280},
                                        "maxAllocated": {"value": 1280},
                                        "tmName": {"description": "service"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/service%20policy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "service policy"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/session": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2109568},
                                        "maxAllocated": {"value": 2109568},
                                        "tmName": {"description": "session"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/session%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1408},
                                        "maxAllocated": {"value": 1408},
                                        "tmName": {
                                            "description": "session cache"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/session%20master%20key": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 528},
                                        "maxAllocated": {"value": 528},
                                        "tmName": {
                                            "description": "session master key"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/session%20pdq": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "session pdq"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/session_leasepool_mbr_table": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "session_leasepool_mbr_table"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sfc_errors_stat": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sfc_errors_stat"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/shaper_domain": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 32},
                                        "maxAllocated": {"value": 32},
                                        "tmName": {
                                            "description": "shaper_domain"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/shared_var_context": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "shared_var_context"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sip_dialog": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sip_dialog"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sip_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "sip_entry"},
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sip_header_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sip_header_cache"
                                        },
                                        "size": {"value": 2056},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sip_msg": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "sip_msg"},
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sip_node_ack_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sip_node_ack_cache"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sipmsg": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "sipmsg"},
                                        "size": {"value": 768},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/source%20addr%20translation": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 768},
                                        "maxAllocated": {"value": 768},
                                        "tmName": {
                                            "description": "source addr translation"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_local_hash": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_local_hash"
                                        },
                                        "size": {"value": 1024},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_mult_ip_data_stat": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_mult_ip_data_stat"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_policy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_policy"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_session_create_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_session_create_ctx"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_session_ip_mapping_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_session_ip_mapping_ctx"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_session_timer_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_session_timer_ctx"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_session_update_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_session_update_ctx"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_subs_id_update_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_subs_id_update_ctx"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/spm_towerid_local_hash": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "spm_towerid_local_hash"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4287408},
                                        "maxAllocated": {"value": 4287408},
                                        "tmName": {"description": "ssl"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_basic": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_basic"},
                                        "size": {"value": 752},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_bulk_crypto_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_bulk_crypto_ctx"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_cn": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_cn"},
                                        "size": {"value": 1192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_cn_req": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_cn_req"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_compat": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 312496},
                                        "maxAllocated": {"value": 312496},
                                        "tmName": {
                                            "description": "ssl_compat"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_dht_data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_dht_data"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_dht_key": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_dht_key"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_hs": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_hs"},
                                        "size": {"value": 6216},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_hs_m": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_hs_m"},
                                        "size": {"value": 16384},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_keys": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_keys"},
                                        "size": {"value": 256},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_profile": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 112000},
                                        "maxAllocated": {"value": 112000},
                                        "tmName": {
                                            "description": "ssl_profile"
                                        },
                                        "size": {"value": 7000},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_proxy_profile_hash": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_proxy_profile_hash"
                                        },
                                        "size": {"value": 512},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_rd": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_rd"},
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_session": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_session"
                                        },
                                        "size": {"value": 296},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_sni": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "ssl_sni"},
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_sni_profile_hash": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_sni_profile_hash"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/ssl_sni_profile_hash_cert": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "ssl_sni_profile_hash_cert"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4096},
                                        "maxAllocated": {"value": 4096},
                                        "tmName": {"description": "sso"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso::sso_config": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2983360},
                                        "maxAllocated": {"value": 2983360},
                                        "tmName": {
                                            "description": "sso::sso_config"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso::sso_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sso::sso_pcb"
                                        },
                                        "size": {"value": 2080},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso::sso_plugin": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sso::sso_plugin"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso::sso_saml": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sso::sso_saml"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso::xml_parser": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3539248},
                                        "maxAllocated": {"value": 3539248},
                                        "tmName": {
                                            "description": "sso::xml_parser"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso_config": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sso_config"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso_config_jwt_claim_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sso_config_jwt_claim_entries"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sso_config_jwt_claim_item_entri": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sso_config_jwt_claim_item_entri"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/streamflow": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "streamflow"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/string%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 499000},
                                        "maxAllocated": {"value": 499000},
                                        "tmName": {
                                            "description": "string cache"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/subscriber_id_cookie_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "subscriber_id_cookie_cache"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sw_crypto_req_ctx_dh_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sw_crypto_req_ctx_dh_cache"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sw_crypto_req_ctx_dsa_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sw_crypto_req_ctx_dsa_cache"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sw_crypto_req_ctx_ecdh_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sw_crypto_req_ctx_ecdh_cache"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sw_crypto_req_ctx_ecdsa_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sw_crypto_req_ctx_ecdsa_cache"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sw_crypto_req_ctx_rsa_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 32},
                                        "maxAllocated": {"value": 32},
                                        "tmName": {
                                            "description": "sw_crypto_req_ctx_rsa_cache"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sw_crypto_req_ctx_sm2_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "sw_crypto_req_ctx_sm2_cache"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/sweeper": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 12176},
                                        "maxAllocated": {"value": 12176},
                                        "tmName": {"description": "sweeper"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tacacsplus_server": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "tacacsplus_server"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tacplus%20server": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4096},
                                        "maxAllocated": {"value": 4096},
                                        "tmName": {
                                            "description": "tacplus server"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tcl": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 7369984},
                                        "maxAllocated": {"value": 7369984},
                                        "tmName": {"description": "tcl"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tcl_ip_addr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1248},
                                        "maxAllocated": {"value": 1248},
                                        "tmName": {
                                            "description": "tcl_ip_addr"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tclrule_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3584},
                                        "maxAllocated": {"value": 3584},
                                        "tmName": {
                                            "description": "tclrule_pcb"
                                        },
                                        "size": {"value": 448},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tclrule_pcb_children": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "tclrule_pcb_children"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/temp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 264976},
                                        "maxAllocated": {"value": 264976},
                                        "tmName": {"description": "temp"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/thread%20stacks": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 17203200},
                                        "maxAllocated": {"value": 17203200},
                                        "tmName": {
                                            "description": "thread stacks"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tm_header_cache_entry_slab": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 768},
                                        "maxAllocated": {"value": 768},
                                        "tmName": {
                                            "description": "tm_header_cache_entry_slab"
                                        },
                                        "size": {"value": 384},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tm_opaque": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 72},
                                        "maxAllocated": {"value": 144},
                                        "tmName": {"description": "tm_opaque"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tm_sys": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 92576},
                                        "maxAllocated": {"value": 92576},
                                        "tmName": {"description": "tm_sys"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tmc%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "tmc cache"},
                                        "size": {"value": 640},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tmc%20key%20cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "tmc key cache"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tmc_entry": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "tmc_entry"},
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tmjail": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 23104},
                                        "maxAllocated": {"value": 23104},
                                        "tmName": {"description": "tmjail"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/traffic%20class": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "traffic class"
                                        },
                                        "size": {"value": 96},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/traffic%20class%20tables": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "traffic class tables"
                                        },
                                        "size": {"value": 896},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/traffic%20managment%20interface": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 24304},
                                        "maxAllocated": {"value": 24304},
                                        "tmName": {
                                            "description": "traffic managment interface"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/traffic_selector": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "traffic_selector"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tsig_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "tsig_ctx"},
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tsig_req_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "tsig_req_ctx"
                                        },
                                        "size": {"value": 16},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/tunnel_nexthop": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 768},
                                        "maxAllocated": {"value": 768},
                                        "tmName": {
                                            "description": "tunnel_nexthop"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/umem": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 33404928},
                                        "maxAllocated": {"value": 35663032},
                                        "tmName": {"description": "umem"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/umem%20dynamic%20leak%20util": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "umem dynamic leak util"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/url%20filter": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 672032},
                                        "maxAllocated": {"value": 672032},
                                        "tmName": {
                                            "description": "url filter"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/url_filter_log_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 256},
                                        "maxAllocated": {"value": 256},
                                        "tmName": {
                                            "description": "url_filter_log_entries"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/urlc_cloud_cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "urlc_cloud_cache"
                                        },
                                        "size": {"value": 64},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/vaddr": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 7840},
                                        "maxAllocated": {"value": 8064},
                                        "tmName": {"description": "vaddr"},
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/vcmp": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 3968},
                                        "maxAllocated": {"value": 3968},
                                        "tmName": {"description": "vcmp"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/vpn_na_item_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "vpn_na_item_entries"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/vpn_session_data_entries": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "vpn_session_data_entries"
                                        },
                                        "size": {"value": 8},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wa_resource_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wa_resource_item"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::assembly": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 4352},
                                        "maxAllocated": {"value": 4352},
                                        "tmName": {
                                            "description": "wam::assembly"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::cache": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 2560},
                                        "maxAllocated": {"value": 2560},
                                        "tmName": {
                                            "description": "wam::cache"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::config": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 168512},
                                        "maxAllocated": {"value": 168512},
                                        "tmName": {
                                            "description": "wam::config"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::css_parser": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::css_parser"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::html_parser": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 52064},
                                        "maxAllocated": {"value": 52064},
                                        "tmName": {
                                            "description": "wam::html_parser"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::js_parser": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::js_parser"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::m3u8_parser": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::m3u8_parser"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::mstor": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::mstor"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::mstor_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::mstor_ctx"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::mstor_object": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::mstor_object"
                                        },
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::mstor_op": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::mstor_op"
                                        },
                                        "size": {"value": 1792},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::mtag": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "wam::mtag"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::normalization": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::normalization"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::plugin": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::plugin"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::roistats_bucket": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::roistats_bucket"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::stats_bucket": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::stats_bucket"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::stdlib": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 7200},
                                        "maxAllocated": {"value": 7200},
                                        "tmName": {
                                            "description": "wam::stdlib"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::uci": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "wam::uci"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_annotation": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_annotation"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_assembler": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_assembler"
                                        },
                                        "size": {"value": 128},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_bitset_bits": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_bitset_bits"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_dfa": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_dfa"
                                        },
                                        "size": {"value": 40},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_dfa_state": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_dfa_state"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_document": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_document"
                                        },
                                        "size": {"value": 512},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_entity": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_entity"
                                        },
                                        "size": {"value": 320},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_evt": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 1120},
                                        "maxAllocated": {"value": 1120},
                                        "tmName": {
                                            "description": "wam::wam_evt"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_condition": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_condition"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_expression": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_expression"
                                        },
                                        "size": {"value": 48},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_map": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_map"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_operand": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_operand"
                                        },
                                        "size": {"value": 384},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_policy": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_policy"
                                        },
                                        "size": {"value": 80},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_state": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_state"
                                        },
                                        "size": {"value": 56},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_string": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_string"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_match_transition": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_match_transition"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_nfa_dfa": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_nfa_dfa"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_resource": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_resource"
                                        },
                                        "size": {"value": 192},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_resumption_info": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_resumption_info"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_sink": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_sink"
                                        },
                                        "size": {"value": 32},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wam_transaction": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wam_transaction"
                                        },
                                        "size": {"value": 1792},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/wam::wash_pcb": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "wam::wash_pcb"
                                        },
                                        "size": {"value": 224},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/web%20application": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 16384},
                                        "maxAllocated": {"value": 16384},
                                        "tmName": {
                                            "description": "web application"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/web_application": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "web_application"
                                        },
                                        "size": {"value": 112},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/web_application_item": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "web_application_item"
                                        },
                                        "size": {"value": 24},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/westwood%20data": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {
                                            "description": "westwood data"
                                        },
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/work": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 196608},
                                        "maxAllocated": {"value": 196608},
                                        "tmName": {"description": "work"},
                                        "size": {"value": 1},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/xdata": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 61118464},
                                        "maxAllocated": {"value": 61130752},
                                        "tmName": {"description": "xdata"},
                                        "size": {"value": 2048},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/xfr_ctx": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 0},
                                        "maxAllocated": {"value": 0},
                                        "tmName": {"description": "xfr_ctx"},
                                        "size": {"value": 160},
                                    }
                                }
                            },
                            "https://localhost/mgmt/tm/sys/memory/memory-subsys/xhead": {
                                "nestedStats": {
                                    "entries": {
                                        "allocated": {"value": 954976},
                                        "maxAllocated": {"value": 955168},
                                        "tmName": {"description": "xhead"},
                                        "size": {"value": 32},
                                    }
                                }
                            },
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/memory/memory-tmm": {
                    "nestedStats": {
                        "entries": {
                            "https://localhost/mgmt/tm/sys/memory/memory-tmm/0.0": {
                                "nestedStats": {
                                    "entries": {
                                        "memoryTotal": {"value": 2155872256},
                                        "memoryUsed": {"value": 235599872},
                                        "tmmId": {"description": "0.0"},
                                    }
                                }
                            }
                        }
                    }
                },
            },
        }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysMemory(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysMemory(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
