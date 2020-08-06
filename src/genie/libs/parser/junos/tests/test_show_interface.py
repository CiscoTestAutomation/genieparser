import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import (
    SchemaEmptyParserError,
    SchemaMissingKeyError,
)

from genie.libs.parser.junos.show_interface import (ShowInterfacesTerse,
                                                    ShowInterfacesTerseMatch,
                                                    ShowInterfacesDescriptions,
                                                    ShowInterfaces,
                                                    ShowInterfacesPolicersInterface,
                                                    ShowInterfacesStatistics,
                                                    ShowInterfacesQueue,
                                                    ShowInterfacesExtensive)

#############################################################################
# unitest For show interfaces terse [| match <interface>]
#############################################################################


class test_show_interfaces_terse(unittest.TestCase):
    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_parsed_output = {
        "em1": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
        },
        "em1.0": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
            "protocol": {
                "inet": {
                    "10.0.0.4/8": {"local": "10.0.0.4/8"},
                    "172.16.64.1/2": {"local": "172.16.64.1/2"},
                    "172.16.64.4/2": {"local": "172.16.64.4/2"},
                },
                "inet6": {
                    "fe80::250:56ff:fe82:ba52/64": {
                        "local": "fe80::250:56ff:fe82:ba52/64"
                    },
                    "2001:db8:8d82:0:a::4/64": {"local": "2001:db8:8d82:0:a::4/64"},
                },
                "tnp": {"0x4": {"local": "0x4"}},
            },
        },
        "fxp0": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
        },
        "fxp0.0": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
            "protocol": {"inet": {"172.25.192.114/24": {"local": "172.25.192.114/24"}}},
        },
        "ge-0/0/0": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
        },
        "ge-0/0/0.0": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
            "protocol": {
                "inet": {"10.0.1.1/24": {"local": "10.0.1.1/24"}},
                "multiservice": {},
            },
        },
        "ge-0/0/1": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
        },
        "ge-0/0/1.0": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
            "protocol": {
                "inet": {"10.0.2.1/24": {"local": "10.0.2.1/24"}},
                "multiservice": {},
            },
        },
        "ge-0/0/2": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "down",
            "oper_status": "down",
        },
        "lc-0/0/0": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
        },
        "lc-0/0/0.32769": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
            "protocol": {"vpls": {}},
        },
        "lo0.0": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
            "protocol": {
                "inet": {
                    "10.1.1.1": {"local": "10.1.1.1", "remote": "0/0"},
                    "10.11.11.11": {"local": "10.11.11.11", "remote": "0/0"},
                }
            },
        },
        "lo0.16384": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
            "protocol": {
                "inet": {"127.0.0.1": {"local": "127.0.0.1", "remote": "0/0"}}
            },
        },
        "lo0.16385": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
            "protocol": {"inet": {}},
        },
        "pfe-0/0/0": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
        },
        "pfe-0/0/0.16383": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
            "protocol": {"inet": {}, "inet6": {}},
        },
        "pfh-0/0/0": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
        },
        "pfh-0/0/0.16383": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
            "protocol": {"inet": {}},
        },
        "pfh-0/0/0.16384": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
            "protocol": {"inet": {}},
        },
    }

    golden_output = {
        "execute.return_value": """
        root@junos_vmx1> show interfaces terse
        Interface               Admin Link Proto    Local                 Remote
        ge-0/0/0                up    up
        ge-0/0/0.0              up    up   inet     10.0.1.1/24
                                           multiservice
        lc-0/0/0                up    up
        lc-0/0/0.32769          up    up   vpls
        pfe-0/0/0               up    up
        pfe-0/0/0.16383         up    up   inet
                                           inet6
        pfh-0/0/0               up    up
        pfh-0/0/0.16383         up    up   inet
        pfh-0/0/0.16384         up    up   inet
        ge-0/0/1                up    up
        ge-0/0/1.0              up    up   inet     10.0.2.1/24
                                           multiservice
        ge-0/0/2                up    down
        em1                     up    up
        em1.0                   up    up   inet     10.0.0.4/8
                                                    172.16.64.1/2
                                                    172.16.64.4/2
                                           inet6    fe80::250:56ff:fe82:ba52/64
                                                    2001:db8:8d82:0:a::4/64
                                           tnp      0x4
        fxp0                    up    up
        fxp0.0                  up    up   inet     172.25.192.114/24
        lo0.0                   up    up   inet     10.1.1.1            --> 0/0
                                                    10.11.11.11         --> 0/0
        lo0.16384               up    up   inet     127.0.0.1           --> 0/0
        lo0.16385               up    up   inet
    """
    }

    golden_output_interface = {
        "execute.return_value": """
    root@junos_vmx1 > show interfaces em1.0 terse
    em1.0                   up    up   inet     10.0.0.4/8
                                                    172.16.64.1/2
                                                    172.16.64.4/2
                                           inet6    fe80::250:56ff:fe82:ba52/64
                                                    2001:db8:8d82:0:a::4/64
                                           tnp      0x4
    """
    }

    golden_parsed_output_interface = {
        "em1.0": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
            "protocol": {
                "inet": {
                    "10.0.0.4/8": {"local": "10.0.0.4/8"},
                    "172.16.64.1/2": {"local": "172.16.64.1/2"},
                    "172.16.64.4/2": {"local": "172.16.64.4/2"},
                },
                "inet6": {
                    "fe80::250:56ff:fe82:ba52/64": {
                        "local": "fe80::250:56ff:fe82:ba52/64"
                    },
                    "2001:db8:8d82:0:a::4/64": {"local": "2001:db8:8d82:0:a::4/64"},
                },
                "tnp": {"0x4": {"local": "0x4"}},
            },
        }
    }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfacesTerse(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfacesTerse(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_interface(self):
        self.device = Mock(**self.golden_output_interface)
        interface_obj = ShowInterfacesTerse(device=self.device)
        parsed_output = interface_obj.parse(interface="em1.0")
        self.assertEqual(parsed_output, self.golden_parsed_output_interface)


class test_show_interfaces_terse_match(unittest.TestCase):
    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_parsed_output = {
        "fxp0": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
        },
        "fxp0.0": {
            "admin_state": "up",
            "enabled": True,
            "link_state": "up",
            "oper_status": "up",
            "protocol": {"inet": {"172.25.192.114/24": {"local": "172.25.192.114/24"}}},
        },
    }

    golden_output = {
        "execute.return_value": """
        root@junos_vmx1> show interfaces terse | match fxp0
        fxp0                    up    up
        fxp0.0                  up    up   inet     172.25.192.114/24
    """
    }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfacesTerseMatch(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            interface_obj.parse(interface="fxp0")

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfacesTerseMatch(device=self.device)
        parsed_output = interface_obj.parse(interface="fxp0")
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowInterfacesDescriptions(unittest.TestCase):
    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    maxDiff = None

    golden_parsed_output = {
        "interface-information": {
            "physical-interface": [
                {
                    "admin-status": "up",
                    "description": "none/100G/in/hktGCS002_ge-0/0/0",
                    "name": "ge-0/0/0",
                    "oper-status": "up",
                },
                {
                    "admin-status": "up",
                    "description": "YW7079/9.6G/BB/sjkGDS221-EC11_xe-0/1/5[SJC]_Area8_Cost100",
                    "name": "ge-0/0/1",
                    "oper-status": "up",
                },
                {
                    "admin-status": "up",
                    "description": "ve-hkgasr01_Gi2[DefaultCost1000]",
                    "name": "ge-0/0/2",
                    "oper-status": "up",
                },
            ]
        }
    }

    golden_output = {
        "execute.return_value": """
        show interfaces descriptions
        Interface       Admin Link Description
        ge-0/0/0        up    up   none/100G/in/hktGCS002_ge-0/0/0
        ge-0/0/1        up    up   YW7079/9.6G/BB/sjkGDS221-EC11_xe-0/1/5[SJC]_Area8_Cost100
        ge-0/0/2        up    up   ve-hkgasr01_Gi2[DefaultCost1000]
    """
    }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfacesDescriptions(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfacesDescriptions(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowInterfaces(unittest.TestCase):
    device = Device(name="aDevice")
    maxDiff = None
    empty_output = {"execute.return_value": ""}

    golden_parsed_output = {
        "interface-information": {
            "physical-interface": [
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:ff:56:b6",
                    "description": "none/100G/in/hktGCS002_ge-0/0/0",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:ff:56:b6",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:19 UTC (29w6d 18:56 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-no-redirects": True,
                                        "ifff-sendbcast-pkt-to-re": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-broadcast": "10.189.5.95",
                                        "ifa-destination": "10.189.5.92/30",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "10.189.5.93"
                                    },
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "inet6",
                                    "interface-address": [
                                        {
                                            "ifa-destination": "2001:db8:223c:2c16::/64",
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True,
                                                "ifaf-is-primary": True
                                            },
                                            "ifa-local": "2001:db8:223c:2c16::1"
                                        },
                                        {
                                            "ifa-destination": "fe80::/64",
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True
                                            },
                                            "ifa-local": "fe80::250:56ff:feff:56b6"
                                        }
                                    ],
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "mpls",
                                    "maximum-labels": "3",
                                    "mtu": "1488"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "multiservice",
                                    "mtu": "Unlimited"
                                }
                            ],
                            "encapsulation": "ENET2",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x4004000"
                            },
                            "local-index": "333",
                            "name": "ge-0/0/0.0",
                            "snmp-index": "606",
                            "traffic-statistics": {
                                "input-packets": "133657033",
                                "output-packets": "129243982"
                            }
                        }
                    ],
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/0",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "2952",
                        "input-pps": "5",
                        "output-bps": "3080",
                        "output-pps": "3"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "vpls",
                                    "mtu": "Unlimited"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "329",
                            "logical-interface-bandwidth": "0",
                            "name": "lc-0/0/0.32769",
                            "snmp-index": "520",
                            "traffic-statistics": {
                                "input-packets": "0",
                                "output-packets": "0"
                            }
                        }
                    ],
                    "name": "lc-0/0/0",
                    "speed": "800mbps",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet6",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "330",
                            "logical-interface-bandwidth": "0",
                            "name": "pfe-0/0/0.16383",
                            "snmp-index": "523",
                            "traffic-statistics": {
                                "input-packets": "0",
                                "output-packets": "0"
                            }
                        }
                    ],
                    "name": "pfe-0/0/0",
                    "speed": "800mbps",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "331",
                            "logical-interface-bandwidth": "0",
                            "name": "pfh-0/0/0.16383",
                            "snmp-index": "524",
                            "traffic-statistics": {
                                "input-packets": "0",
                                "output-packets": "0"
                            }
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "inet",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "332",
                            "logical-interface-bandwidth": "0",
                            "name": "pfh-0/0/0.16384",
                            "snmp-index": "525",
                            "traffic-statistics": {
                                "input-packets": "0",
                                "output-packets": "0"
                            }
                        }
                    ],
                    "name": "pfh-0/0/0",
                    "speed": "800mbps",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:ff:37:f9",
                    "description": "YW7079/9.6G/BB/sjkGDS221-EC11_xe-0/1/5[SJC]_Area8_Cost100",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:ff:37:f9",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:19 UTC (29w6d 18:56 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-no-redirects": True,
                                        "ifff-sendbcast-pkt-to-re": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-broadcast": "10.169.14.123",
                                        "ifa-destination": "10.169.14.120/30",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "10.169.14.122"
                                    },
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-name": "inet6",
                                    "interface-address": [
                                        {
                                            "ifa-destination": "2001:db8:eb18:6337::/64",
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True,
                                                "ifaf-is-primary": True
                                            },
                                            "ifa-local": "2001:db8:eb18:6337::2"
                                        },
                                        {
                                            "ifa-destination": "fe80::/64",
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True
                                            },
                                            "ifa-local": "fe80::250:56ff:feff:37f9"
                                        }
                                    ],
                                    "intf-curr-cnt": "2",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-name": "mpls",
                                    "maximum-labels": "3",
                                    "mtu": "1488"
                                },
                                {
                                    "address-family-name": "multiservice",
                                    "mtu": "Unlimited"
                                }
                            ],
                            "encapsulation": "ENET2",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x4004000"
                            },
                            "local-index": "334",
                            "name": "ge-0/0/1.0",
                            "snmp-index": "605",
                            "traffic-statistics": {
                                "input-packets": "376821627",
                                "output-packets": "370477594"
                            }
                        }
                    ],
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/1",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "3696",
                        "input-pps": "6",
                        "output-bps": "7736",
                        "output-pps": "9"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:ff:1e:ba",
                    "description": "ve-hkgasr01_Gi2[DefaultCost1000]",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:ff:1e:ba",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2020-03-05 16:04:34 UTC (2w6d 12:00 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-sendbcast-pkt-to-re": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-broadcast": "10.19.198.27",
                                        "ifa-destination": "10.19.198.24/30",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "10.19.198.25"
                                    },
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-name": "mpls",
                                    "maximum-labels": "3",
                                    "mtu": "1488"
                                },
                                {
                                    "address-family-name": "multiservice",
                                    "mtu": "Unlimited"
                                }
                            ],
                            "encapsulation": "ENET2",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x4004000"
                            },
                            "local-index": "336",
                            "name": "ge-0/0/2.0",
                            "snmp-index": "536",
                            "traffic-statistics": {
                                "input-packets": "210359939",
                                "output-packets": "222589463"
                            }
                        }
                    ],
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/2",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "928",
                        "input-pps": "1",
                        "output-bps": "800",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:ff:93:cb",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:ff:93:cb",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-10-25 08:50:18 UTC (21w5d 19:15 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-sendbcast-pkt-to-re": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-broadcast": "10.55.0.255",
                                        "ifa-destination": "100.0.0/24",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "10.55.0.254"
                                    },
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-name": "multiservice",
                                    "mtu": "Unlimited"
                                }
                            ],
                            "encapsulation": "ENET2",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x4004000"
                            },
                            "local-index": "335",
                            "name": "ge-0/0/3.0",
                            "snmp-index": "537",
                            "traffic-statistics": {
                                "input-packets": "14609",
                                "output-packets": "17416"
                            }
                        }
                    ],
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/3",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:ff:3e:28",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:ff:3e:28",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/4",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:ff:01:1d",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:ff:01:1d",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/5",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:ff:01:1e",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:ff:01:1e",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/6",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:ff:01:1f",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:ff:01:1f",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/7",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:ff:01:20",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:ff:01:20",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/8",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:ff:01:21",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:ff:01:21",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 18:55 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/9",
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-pps": "0",
                        "output-bps": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "2c:6b:f5:ff:01:29",
                    "hardware-physical-address": "2c:6b:f5:ff:01:29",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Ethernet",
                    "link-type": "Full-Duplex",
                    "mtu": "9192",
                    "name": "cbp0",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "name": "demux0",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "name": "dsc",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "00:50:56:ff:e2:c1",
                    "hardware-physical-address": "00:50:56:ff:e2:c1",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "interface-flapped": {
                        "#text": "2019-08-29 09:03:11 UTC (29w6d 19:02 ago)"
                    },
                    "link-level-type": "Ethernet",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": [
                                        {
                                            "ifa-broadcast": "10.255.255.255",
                                            "ifa-destination": "10/8",
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True
                                            },
                                            "ifa-local": "10.0.0.4"
                                        },
                                        {
                                            "ifa-broadcast": "172.16.16.255",
                                            "ifa-destination": "128/2",
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True,
                                                "ifaf-kernel": True,
                                                "ifaf-preferred": True
                                            },
                                            "ifa-local": "172.16.64.1"
                                        },
                                        {
                                            "ifa-broadcast": "172.16.16.255",
                                            "ifa-destination": "128/2",
                                            "ifa-flags": {
                                                "ifaf-is-default": True,
                                                "ifaf-is-primary": True,
                                                "ifaf-primary": True
                                            },
                                            "ifa-local": "172.16.64.4"
                                        }
                                    ],
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "inet6",
                                    "interface-address": [
                                        {
                                            "ifa-destination": "fe80::/64",
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True
                                            },
                                            "ifa-local": "fe80::250:56ff:feff:e2c1"
                                        },
                                        {
                                            "ifa-destination": "2001:db8:8d82::/64",
                                            "ifa-flags": {
                                                "ifaf-is-default": True,
                                                "ifaf-is-preferred": True,
                                                "ifaf-is-primary": True
                                            },
                                            "ifa-local": "0x4"
                                        }
                                    ],
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True,
                                        "ifff-primary": True
                                    },
                                    "address-family-name": "tnp",
                                    "mtu": "1500"
                                }
                            ],
                            "encapsulation": "ENET2",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x4000000"
                            },
                            "local-index": "3",
                            "name": "em1.0",
                            "snmp-index": "24",
                            "traffic-statistics": {
                                "input-packets": "724625563",
                                "output-packets": "793953088"
                            }
                        }
                    ],
                    "mtu": "1514",
                    "name": "em1",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "VxLAN-Tunnel-Endpoint",
                    "link-type": "Full-Duplex",
                    "mtu": "Unlimited",
                    "name": "esi",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "mtu": "Unlimited",
                    "name": "fti0",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "mtu": "Unlimited",
                    "name": "fti1",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "mtu": "Unlimited",
                    "name": "fti2",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "mtu": "Unlimited",
                    "name": "fti3",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "mtu": "Unlimited",
                    "name": "fti4",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "mtu": "Unlimited",
                    "name": "fti5",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "mtu": "Unlimited",
                    "name": "fti6",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Flexible-tunnel-Interface",
                    "link-type": "Full-Duplex",
                    "mtu": "Unlimited",
                    "name": "fti7",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "00:50:56:ff:0a:95",
                    "hardware-physical-address": "00:50:56:ff:0a:95",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "interface-flapped": {
                        "#text": "2019-08-29 09:03:11 UTC (29w6d 19:02 ago)"
                    },
                    "link-level-type": "Ethernet",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True,
                                        "ifff-sendbcast-pkt-to-re": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-broadcast": "10.1.0.255",
                                        "ifa-destination": "1.0.0/24",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "10.1.0.101"
                                    },
                                    "intf-curr-cnt": "2",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                }
                            ],
                            "encapsulation": "ENET2",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x4000000"
                            },
                            "local-index": "4",
                            "name": "fxp0.0",
                            "snmp-index": "13",
                            "traffic-statistics": {
                                "input-packets": "563129",
                                "output-packets": "805208"
                            }
                        }
                    ],
                    "mtu": "1514",
                    "name": "fxp0",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "GRE",
                    "mtu": "Unlimited",
                    "name": "gre",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "IP-over-IP",
                    "mtu": "Unlimited",
                    "name": "ipip",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "2c:6b:f5:ff:08:09",
                    "hardware-physical-address": "2c:6b:f5:ff:08:09",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Ethernet",
                    "link-type": "Full-Duplex",
                    "mtu": "1514",
                    "name": "irb",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "2c:6b:f5:ff:08:d8",
                    "hardware-physical-address": "2c:6b:f5:ff:08:d8",
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Ethernet",
                    "link-type": "Full-Duplex",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-broadcast": "172.16.16.255",
                                        "ifa-destination": "128/2",
                                        "ifa-flags": {
                                            "ifaf-is-default": True,
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True,
                                            "ifaf-primary": True
                                        },
                                        "ifa-local": "172.16.64.127"
                                    },
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1514",
                                    "new-hold-limit": "75000"
                                }
                            ],
                            "encapsulation": "unknown",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x24004000"
                            },
                            "local-index": "325",
                            "logical-interface-bandwidth": "1Gbps",
                            "name": "jsrv.1",
                            "snmp-index": "514",
                            "traffic-statistics": {
                                "input-packets": "0",
                                "output-packets": "0"
                            }
                        }
                    ],
                    "mtu": "1514",
                    "name": "jsrv",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-loopback": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-no-redirects": True,
                                        "ifff-sendbcast-pkt-to-re": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-flags": {
                                            "ifaf-is-default": True,
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "10.189.5.252"
                                    },
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                },
                                {
                                    "address-family-name": "inet6",
                                    "interface-address": {
                                        "ifa-flags": {
                                            "ifaf-is-default": True,
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "127.0.0.1"
                                    },
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "320",
                            "name": "lo0.0",
                            "snmp-index": "16",
                            "traffic-statistics": {
                                "input-packets": "83",
                                "output-packets": "83"
                            }
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-name": "inet",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "322",
                            "name": "lo0.16384",
                            "snmp-index": "21",
                            "traffic-statistics": {
                                "input-packets": "0",
                                "output-packets": "0"
                            }
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-name": "inet",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "321",
                            "name": "lo0.16385",
                            "snmp-index": "22",
                            "traffic-statistics": {
                                "input-packets": "33920495",
                                "output-packets": "33920495"
                            }
                        }
                    ],
                    "name": "lo0",
                    "traffic-statistics": {
                        "input-packets": "33920578",
                        "output-packets": "33920578"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "LSI",
                    "mtu": "Unlimited",
                    "name": "lsi",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "GRE",
                    "mtu": "Unlimited",
                    "name": "mtun",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "PIM-Decapsulator",
                    "mtu": "Unlimited",
                    "name": "pimd",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "PIM-Encapsulator",
                    "mtu": "Unlimited",
                    "name": "pime",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "2c:6b:f5:ff:08:c8",
                    "hardware-physical-address": "2c:6b:f5:ff:08:c8",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Ethernet",
                    "link-type": "Full-Duplex",
                    "mtu": "9192",
                    "name": "pip0",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "link-level-type": "PPPoE",
                    "link-type": "Full-Duplex",
                    "mtu": "1532",
                    "name": "pp0"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Remote-BEB",
                    "link-type": "Full-Duplex",
                    "mtu": "Unlimited",
                    "name": "rbeb",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "Interface-Specific",
                    "mtu": "Unlimited",
                    "name": "tap",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-level-type": "VxLAN-Tunnel-Endpoint",
                    "link-type": "Full-Duplex",
                    "mtu": "Unlimited",
                    "name": "vtep",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-packets": "0",
                        "output-packets": "0"
                    }
                }
            ]
        }
    }

    golden_output = {
        "execute.return_value": """
        show interfaces
        Physical interface: ge-0/0/0, Enabled, Physical link is Up
        Interface index: 148, SNMP ifIndex: 526
        Description: none/100G/in/hktGCS002_ge-0/0/0
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 00:50:56:ff:56:b6, Hardware address: 00:50:56:ff:56:b6
        Last flapped   : 2019-08-29 09:09:19 UTC (29w6d 18:56 ago)
        Input rate     : 2952 bps (5 pps)
        Output rate    : 3080 bps (3 pps)
        Active alarms  : None
        Active defects : None
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/0.0 (Index 333) (SNMP ifIndex 606)
            Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
            Input packets : 133657033
            Output packets: 129243982
            Protocol inet, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: No-Redirects, Sendbcast-pkt-to-re
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 10.189.5.92/30, Local: 10.189.5.93, Broadcast: 10.189.5.95
            Protocol inet6, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Is-Primary
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 2001:db8:223c:2c16::/64, Local: 2001:db8:223c:2c16::1
            Addresses, Flags: Is-Preferred
                Destination: fe80::/64, Local: fe80::250:56ff:feff:56b6
            Protocol mpls, MTU: 1488, Maximum labels: 3
            Flags: Is-Primary
            Protocol multiservice, MTU: Unlimited
            Flags: Is-Primary

        Physical interface: lc-0/0/0, Enabled, Physical link is Up
        Interface index: 145, SNMP ifIndex: 519
        Speed: 800mbps
        Device flags   : Present Running
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Logical interface lc-0/0/0.32769 (Index 329) (SNMP ifIndex 520)
            Flags: Up Encapsulation: ENET2
            Bandwidth: 0
            Input packets : 0
            Output packets: 0
            Protocol vpls, MTU: Unlimited
            Flags: Is-Primary

        Physical interface: pfe-0/0/0, Enabled, Physical link is Up
        Interface index: 147, SNMP ifIndex: 522
        Speed: 800mbps
        Device flags   : Present Running
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Logical interface pfe-0/0/0.16383 (Index 330) (SNMP ifIndex 523)
            Flags: Up SNMP-Traps Encapsulation: ENET2
            Bandwidth: 0
            Input packets : 0
            Output packets: 0
            Protocol inet, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: None
            Protocol inet6, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: None

        Physical interface: pfh-0/0/0, Enabled, Physical link is Up
        Interface index: 146, SNMP ifIndex: 521
        Speed: 800mbps
        Device flags   : Present Running
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Logical interface pfh-0/0/0.16383 (Index 331) (SNMP ifIndex 524)
            Flags: Up SNMP-Traps Encapsulation: ENET2
            Bandwidth: 0
            Input packets : 0
            Output packets: 0
            Protocol inet, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: None

        Logical interface pfh-0/0/0.16384 (Index 332) (SNMP ifIndex 525)
            Flags: Up SNMP-Traps Encapsulation: ENET2
            Bandwidth: 0
            Input packets : 0
            Output packets: 0
            Protocol inet, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Is-Primary

        Physical interface: ge-0/0/1, Enabled, Physical link is Up
        Interface index: 149, SNMP ifIndex: 527
        Description: YW7079/9.6G/BB/sjkGDS221-EC11_xe-0/1/5[SJC]_Area8_Cost100
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 00:50:56:ff:37:f9, Hardware address: 00:50:56:ff:37:f9
        Last flapped   : 2019-08-29 09:09:19 UTC (29w6d 18:56 ago)
        Input rate     : 3696 bps (6 pps)
        Output rate    : 7736 bps (9 pps)
        Active alarms  : None
        Active defects : None
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/1.0 (Index 334) (SNMP ifIndex 605)
            Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
            Input packets : 376821627
            Output packets: 370477594
            Protocol inet, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: No-Redirects, Sendbcast-pkt-to-re
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 10.169.14.120/30, Local: 10.169.14.122, Broadcast: 10.169.14.123
            Protocol inet6, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 2, Curr new hold cnt: 0, NH drop cnt: 0
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 2001:db8:eb18:6337::/64, Local: 2001:db8:eb18:6337::2
            Addresses, Flags: Is-Preferred
                Destination: fe80::/64, Local: fe80::250:56ff:feff:37f9
            Protocol mpls, MTU: 1488, Maximum labels: 3
            Protocol multiservice, MTU: Unlimited

        Physical interface: ge-0/0/2, Enabled, Physical link is Up
        Interface index: 150, SNMP ifIndex: 528
        Description: ve-hkgasr01_Gi2[DefaultCost1000]
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 00:50:56:ff:1e:ba, Hardware address: 00:50:56:ff:1e:ba
        Last flapped   : 2020-03-05 16:04:34 UTC (2w6d 12:00 ago)
        Input rate     : 928 bps (1 pps)
        Output rate    : 800 bps (0 pps)
        Active alarms  : None
        Active defects : None
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/2.0 (Index 336) (SNMP ifIndex 536)
            Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
            Input packets : 210359939
            Output packets: 222589463
            Protocol inet, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Sendbcast-pkt-to-re
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 10.19.198.24/30, Local: 10.19.198.25, Broadcast: 10.19.198.27
            Protocol mpls, MTU: 1488, Maximum labels: 3
            Protocol multiservice, MTU: Unlimited

        Physical interface: ge-0/0/3, Enabled, Physical link is Up
        Interface index: 151, SNMP ifIndex: 529
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 00:50:56:ff:93:cb, Hardware address: 00:50:56:ff:93:cb
        Last flapped   : 2019-10-25 08:50:18 UTC (21w5d 19:15 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : None
        Active defects : None
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/3.0 (Index 335) (SNMP ifIndex 537)
            Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
            Input packets : 14609
            Output packets: 17416
            Protocol inet, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Sendbcast-pkt-to-re
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 100.0.0/24, Local: 10.55.0.254, Broadcast: 10.55.0.255
            Protocol multiservice, MTU: Unlimited

        Physical interface: ge-0/0/4, Enabled, Physical link is Down
        Interface index: 152, SNMP ifIndex: 530
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running Down
        Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 00:50:56:ff:3e:28, Hardware address: 00:50:56:ff:3e:28
        Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 18:55 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : LINK
        Active defects : LINK
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Physical interface: ge-0/0/5, Enabled, Physical link is Down
        Interface index: 153, SNMP ifIndex: 531
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running Down
        Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 2c:6b:f5:ff:01:1d, Hardware address: 2c:6b:f5:ff:01:1d
        Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 18:55 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : LINK
        Active defects : LINK
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Physical interface: ge-0/0/6, Enabled, Physical link is Down
        Interface index: 154, SNMP ifIndex: 532
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running Down
        Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 2c:6b:f5:ff:01:1e, Hardware address: 2c:6b:f5:ff:01:1e
        Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 18:55 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : LINK
        Active defects : LINK
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Physical interface: ge-0/0/7, Enabled, Physical link is Down
        Interface index: 155, SNMP ifIndex: 533
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running Down
        Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 2c:6b:f5:ff:01:1f, Hardware address: 2c:6b:f5:ff:01:1f
        Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 18:55 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : LINK
        Active defects : LINK
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Physical interface: ge-0/0/8, Enabled, Physical link is Down
        Interface index: 156, SNMP ifIndex: 534
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running Down
        Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 2c:6b:f5:ff:01:20, Hardware address: 2c:6b:f5:ff:01:20
        Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 18:55 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : LINK
        Active defects : LINK
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Physical interface: ge-0/0/9, Enabled, Physical link is Down
        Interface index: 157, SNMP ifIndex: 535
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running Down
        Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 2c:6b:f5:ff:01:21, Hardware address: 2c:6b:f5:ff:01:21
        Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 18:55 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Active alarms  : LINK
        Active defects : LINK
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        Interface transmit statistics: Disabled

        Physical interface: cbp0, Enabled, Physical link is Up
        Interface index: 129, SNMP ifIndex: 501
        Type: Ethernet, Link-level type: Ethernet, MTU: 9192
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Current address: 2c:6b:f5:ff:01:29, Hardware address: 2c:6b:f5:ff:01:29
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: demux0, Enabled, Physical link is Up
        Interface index: 128, SNMP ifIndex: 502
        Type: Software-Pseudo, MTU: 9192, Clocking: 1
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: dsc, Enabled, Physical link is Up
        Interface index: 5, SNMP ifIndex: 5
        Type: Software-Pseudo, MTU: Unlimited
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: em1, Enabled, Physical link is Up
        Interface index: 65, SNMP ifIndex: 23
        Type: Ethernet, Link-level type: Ethernet, MTU: 1514
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Current address: 00:50:56:ff:e2:c1, Hardware address: 00:50:56:ff:e2:c1
        Last flapped   : 2019-08-29 09:03:11 UTC (29w6d 19:02 ago)
            Input packets : 0
            Output packets: 0

        Logical interface em1.0 (Index 3) (SNMP ifIndex 24)
            Flags: Up SNMP-Traps 0x4000000 Encapsulation: ENET2
            Input packets : 724625563
            Output packets: 793953088
            Protocol inet, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Is-Primary
            Addresses, Flags: Is-Preferred
                Destination: 10/8, Local: 10.0.0.4, Broadcast: 10.255.255.255
            Addresses, Flags: Preferred Kernel Is-Preferred
                Destination: 128/2, Local: 172.16.64.1, Broadcast: 172.16.16.255
            Addresses, Flags: Primary Is-Default Is-Primary
                Destination: 128/2, Local: 172.16.64.4, Broadcast: 172.16.16.255
            Protocol inet6, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Is-Primary
            Addresses, Flags: Is-Preferred
                Destination: fe80::/64, Local: fe80::250:56ff:feff:e2c1
            Addresses, Flags: Is-Default Is-Preferred Is-Primary
                Destination: 2001:db8:8d82::/64, Local: 2001:db8:8d82::a:0:0:4
            Protocol tnp, MTU: 1500
            Flags: Primary, Is-Primary
            Addresses
                Local: 0x4

        Physical interface: esi, Enabled, Physical link is Up
        Interface index: 134, SNMP ifIndex: 503
        Type: Software-Pseudo, Link-level type: VxLAN-Tunnel-Endpoint, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti0, Enabled, Physical link is Up
        Interface index: 136, SNMP ifIndex: 504
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti1, Enabled, Physical link is Up
        Interface index: 137, SNMP ifIndex: 505
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti2, Enabled, Physical link is Up
        Interface index: 138, SNMP ifIndex: 506
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti3, Enabled, Physical link is Up
        Interface index: 139, SNMP ifIndex: 507
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti4, Enabled, Physical link is Up
        Interface index: 140, SNMP ifIndex: 508
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti5, Enabled, Physical link is Up
        Interface index: 141, SNMP ifIndex: 509
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti6, Enabled, Physical link is Up
        Interface index: 142, SNMP ifIndex: 510
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fti7, Enabled, Physical link is Up
        Interface index: 143, SNMP ifIndex: 511
        Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: fxp0, Enabled, Physical link is Up
        Interface index: 64, SNMP ifIndex: 1
        Type: Ethernet, Link-level type: Ethernet, MTU: 1514
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Current address: 00:50:56:ff:0a:95, Hardware address: 00:50:56:ff:0a:95
        Last flapped   : 2019-08-29 09:03:11 UTC (29w6d 19:02 ago)
            Input packets : 0
            Output packets: 0

        Logical interface fxp0.0 (Index 4) (SNMP ifIndex 13)
            Flags: Up SNMP-Traps 0x4000000 Encapsulation: ENET2
            Input packets : 563129
            Output packets: 805208
            Protocol inet, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 2, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Sendbcast-pkt-to-re, Is-Primary
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 1.0.0/24, Local: 10.1.0.101, Broadcast: 10.1.0.255

        Physical interface: gre, Enabled, Physical link is Up
        Interface index: 10, SNMP ifIndex: 8
        Type: GRE, Link-level type: GRE, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps
            Input packets : 0
            Output packets: 0

        Physical interface: ipip, Enabled, Physical link is Up
        Interface index: 11, SNMP ifIndex: 9
        Type: IPIP, Link-level type: IP-over-IP, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
            Input packets : 0
            Output packets: 0

        Physical interface: irb, Enabled, Physical link is Up
        Interface index: 132, SNMP ifIndex: 512
        Type: Ethernet, Link-level type: Ethernet, MTU: 1514
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Current address: 2c:6b:f5:ff:08:09, Hardware address: 2c:6b:f5:ff:08:09
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: jsrv, Enabled, Physical link is Up
        Interface index: 144, SNMP ifIndex: 513
        Type: Ethernet, Link-level type: Ethernet, MTU: 1514
        Device flags   : Present Running
        Link type      : Full-Duplex
        Link flags     : None
        Current address: 2c:6b:f5:ff:08:d8, Hardware address: 2c:6b:f5:ff:08:d8
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Logical interface jsrv.1 (Index 325) (SNMP ifIndex 514)
            Flags: Up 0x24004000 Encapsulation: unknown
            Bandwidth: 1Gbps
            Routing Instance: None Bridging Domain: None
            Input packets : 0
            Output packets: 0
            Protocol inet, MTU: 1514
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: Is-Primary
            Addresses, Flags: Primary Is-Default Is-Preferred Is-Primary
                Destination: 128/2, Local: 172.16.64.127, Broadcast: 172.16.16.255

        Physical interface: lo0, Enabled, Physical link is Up
        Interface index: 6, SNMP ifIndex: 6
        Type: Loopback, MTU: Unlimited
        Device flags   : Present Running Loopback
        Interface flags: SNMP-Traps
        Link flags     : None
        Last flapped   : Never
            Input packets : 33920578
            Output packets: 33920578

        Logical interface lo0.0 (Index 320) (SNMP ifIndex 16)
            Flags: SNMP-Traps Encapsulation: Unspecified
            Input packets : 83
            Output packets: 83
            Protocol inet, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Flags: No-Redirects, Sendbcast-pkt-to-re
            Addresses, Flags: Is-Default Is-Primary
                Local: 10.189.5.252
            Protocol inet6, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Addresses, Flags: Is-Default Is-Primary
                Local: 2001:db8:223c:ca45::b
                Local: fe80::250:560f:fc8d:7c08

        Logical interface lo0.16384 (Index 322) (SNMP ifIndex 21)
            Flags: SNMP-Traps Encapsulation: Unspecified
            Input packets : 0
            Output packets: 0
            Protocol inet, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Addresses
                Local: 127.0.0.1

        Logical interface lo0.16385 (Index 321) (SNMP ifIndex 22)
            Flags: SNMP-Traps Encapsulation: Unspecified
            Input packets : 33920495
            Output packets: 33920495
            Protocol inet, MTU: Unlimited
            Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0

        Physical interface: lsi, Enabled, Physical link is Up
        Interface index: 4, SNMP ifIndex: 4
        Type: Software-Pseudo, Link-level type: LSI, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: mtun, Enabled, Physical link is Up
        Interface index: 66, SNMP ifIndex: 12
        Type: Multicast-GRE, Link-level type: GRE, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
            Input packets : 0
            Output packets: 0

        Physical interface: pimd, Enabled, Physical link is Up
        Interface index: 26, SNMP ifIndex: 11
        Type: PIMD, Link-level type: PIM-Decapsulator, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
            Input packets : 0
            Output packets: 0

        Physical interface: pime, Enabled, Physical link is Up
        Interface index: 25, SNMP ifIndex: 10
        Type: PIME, Link-level type: PIM-Encapsulator, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
            Input packets : 0
            Output packets: 0

        Physical interface: pip0, Enabled, Physical link is Up
        Interface index: 130, SNMP ifIndex: 515
        Type: Ethernet, Link-level type: Ethernet, MTU: 9192
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Current address: 2c:6b:f5:ff:08:c8, Hardware address: 2c:6b:f5:ff:08:c8
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: pp0, Enabled, Physical link is Up
        Interface index: 131, SNMP ifIndex: 516
        Type: PPPoE, Link-level type: PPPoE, MTU: 1532
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None

        Physical interface: rbeb, Enabled, Physical link is Up
        Interface index: 135, SNMP ifIndex: 517
        Type: Software-Pseudo, Link-level type: Remote-BEB, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: tap, Enabled, Physical link is Up
        Interface index: 12, SNMP ifIndex: 7
        Type: Software-Pseudo, Link-level type: Interface-Specific, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0

        Physical interface: vtep, Enabled, Physical link is Up
        Interface index: 133, SNMP ifIndex: 518
        Type: Software-Pseudo, Link-level type: VxLAN-Tunnel-Endpoint, MTU: Unlimited, Speed: Unlimited
        Device flags   : Present Running
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : Never
            Input packets : 0
            Output packets: 0
    """
    }

    golden_output_2 = {
        "execute.return_value": """
        show interfaces extensive
            Physical interface: ge-0/0/0, Enabled, Physical link is Up
            Interface index: 148, SNMP ifIndex: 526, Generation: 151
            Description: none/100G/in/hktGCS002_ge-0/0/0
            Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
            Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
            Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
            Pad to minimum frame size: Disabled
            Device flags   : Present Running
            Interface flags: SNMP-Traps Internal: 0x4000
            Link flags     : None
            CoS queues     : 8 supported, 8 maximum usable queues
            Hold-times     : Up 2000 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 00:50:56:ff:56:b6, Hardware address: 00:50:56:ff:56:b6
            Last flapped   : 2019-08-29 09:09:19 UTC (29w6d 22:19 ago)
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :          19732539397                 3152 bps
            Output bytes  :          16367814635                 3160 bps
            Input  packets:            133726363                    5 pps
            Output packets:            129306863                    4 pps
            IPv6 transit statistics:
            Input  bytes  :            737203554
            Output bytes  :           1018758352
            Input  packets:              7541948
            Output packets:              6986863
            Label-switched interface (LSI) traffic statistics:
            Input  bytes  :                    0                    0 bps
            Input  packets:                    0                    0 pps
            Dropped traffic statistics due to STP State:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0,
                L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 1, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0,
                MTU errors: 0, Resource errors: 0
            Active alarms  : None
            Active defects : None
            PCS statistics                      Seconds
                Bit errors                             0
                Errored blocks                         0
            Ethernet FEC statistics              Errors
                FEC Corrected Errors                    0
                FEC Uncorrected Errors                  0
                FEC Corrected Errors Rate               0
                FEC Uncorrected Errors Rate             0
            MAC statistics:                      Receive         Transmit
                Total octets                   21604601324      16828244544
                Total packets                    133726919        129183374
                Unicast packets                  133726908        129183361
                Broadcast packets                        0                0
                Multicast packets                        0                0
                CRC/Align errors                         0                0
                FIFO errors                              0                0
                MAC control frames                       0                0
                MAC pause frames                         0                0
                Oversized frames                         0
                Jabber frames                            0
                Fragment frames                          0
                VLAN tagged frames                       0
                Code violations                          0
                Total errors                             0                0
            Filter statistics:
                Input packet count               133726908
                Input packet rejects                   118
                Input DA rejects                        60
                Input SA rejects                         0
                Output packet count                               129183361
                Output packet pad count                                   0
                Output packet error count                                 0
                CAM destination filters: 0, CAM source filters: 0
            Autonegotiation information:
                Negotiation status: Incomplete
            Packet Forwarding Engine configuration:
                Destination slot: 0 (0x00)
            CoS information:
                Direction : Output
                CoS transmit queue               Bandwidth               Buffer Priority   Limit
                                        %            bps     %           usec
                0 best-effort            95      950000000    95              0      low    none
                3 network-control         5       50000000     5              0      low    none
            Interface transmit statistics: Disabled

            Logical interface ge-0/0/0.0 (Index 333) (SNMP ifIndex 606) (Generation 142)
                Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
                Traffic statistics:
                Input  bytes  :          19732539397
                Output bytes  :          15997705213
                Input  packets:            133726363
                Output packets:            129306864
                IPv6 transit statistics:
                Input  bytes  :            737203554
                Output bytes  :           1018758352
                Input  packets:              7541948
                Output packets:              6986863
                Local statistics:
                Input  bytes  :          12676733166
                Output bytes  :          11303933633
                Input  packets:             63558712
                Output packets:             61684919
                Transit statistics:
                Input  bytes  :           7055806231                 3152 bps
                Output bytes  :           4693771580                  816 bps
                Input  packets:             70167651                    5 pps
                Output packets:             67621945                    1 pps
                IPv6 transit statistics:
                Input  bytes  :           737203554                 1856 bps
                Output bytes  :          1018758352                    0 bps
                Input  packets:             7541948                    2 pps
                Output packets:             6986863                    0 pps
                Protocol inet, MTU: 1500
                Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 160, Route table: 0
                Flags: No-Redirects, Sendbcast-pkt-to-re
                Input Filters: catch_all
                Addresses, Flags: Is-Preferred Is-Primary
                    Destination: 10.189.5.92/30, Local: 10.189.5.93, Broadcast: 10.189.5.95, Generation: 146
                Protocol inet6, MTU: 1500
                Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 161, Route table: 0
                Flags: Is-Primary
                Input Filters: v6_catch_all
                Addresses, Flags: Is-Preferred Is-Primary
                    Destination: 2001:db8:223c:2c16::/64, Local: 2001:db8:223c:2c16::1
                Generation: 148
                Addresses, Flags: Is-Preferred
                    Destination: fe80::/64, Local: fe80::250:56ff:feff:56b6
                Protocol mpls, MTU: 1488, Maximum labels: 3, Generation: 150
                Generation: 162, Route table: 0
                Flags: Is-Primary
                Protocol multiservice, MTU: Unlimited, Generation: 163, Route table: 0
                Flags: Is-Primary
                Policer: Input: __default_arp_policer__

            Physical interface: lc-0/0/0, Enabled, Physical link is Up
            Interface index: 145, SNMP ifIndex: 519, Generation: 148
            Type: Unspecified, Link-level type: Unspecified, MTU: 0, Clocking: Unspecified, Speed: 800mbps
            Device flags   : Present Running
            Link type      : Unspecified
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Logical interface lc-0/0/0.32769 (Index 329) (SNMP ifIndex 520) (Generation 138)
                Flags: Up Encapsulation: ENET2
                Bandwidth: 0
                Traffic statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Local statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Transit statistics:
                Input  bytes  :                    0                    0 bps
                Output bytes  :                    0                    0 bps
                Input  packets:                    0                    0 pps
                Output packets:                    0                    0 pps
                Protocol vpls, MTU: Unlimited, Generation: 155, Route table: 1
                Flags: Is-Primary

            Physical interface: pfe-0/0/0, Enabled, Physical link is Up
            Interface index: 147, SNMP ifIndex: 522, Generation: 150
            Type: Unspecified, Link-level type: Unspecified, MTU: 0, Clocking: Unspecified, Speed: 800mbps
            Device flags   : Present Running
            Link type      : Unspecified
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Logical interface pfe-0/0/0.16383 (Index 330) (SNMP ifIndex 523) (Generation 139)
                Flags: Up SNMP-Traps Encapsulation: ENET2
                Bandwidth: 0
                Traffic statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                IPv6 transit statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Local statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Transit statistics:
                Input  bytes  :                    0                    0 bps
                Output bytes  :                    0                    0 bps
                Input  packets:                    0                    0 pps
                Output packets:                    0                    0 pps
                IPv6 transit statistics:
                Input  bytes  :                   0                    0 bps
                Output bytes  :                   0                    0 bps
                Input  packets:                   0                    0 pps
                Output packets:                   0                    0 pps
                Protocol inet, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 156, Route table: 1
                Flags: None
                Protocol inet6, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 157, Route table: 1
                Flags: None

            Physical interface: pfh-0/0/0, Enabled, Physical link is Up
            Interface index: 146, SNMP ifIndex: 521, Generation: 149
            Type: Unspecified, Link-level type: Unspecified, MTU: 0, Clocking: Unspecified, Speed: 800mbps
            Device flags   : Present Running
            Link type      : Unspecified
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Logical interface pfh-0/0/0.16383 (Index 331) (SNMP ifIndex 524) (Generation 140)
                Flags: Up SNMP-Traps Encapsulation: ENET2
                Bandwidth: 0
                Traffic statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Local statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Transit statistics:
                Input  bytes  :                    0                    0 bps
                Output bytes  :                    0                    0 bps
                Input  packets:                    0                    0 pps
                Output packets:                    0                    0 pps
                Protocol inet, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 158, Route table: 1
                Flags: None

            Logical interface pfh-0/0/0.16384 (Index 332) (SNMP ifIndex 525) (Generation 141)
                Flags: Up SNMP-Traps Encapsulation: ENET2
                Bandwidth: 0
                Traffic statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Local statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Transit statistics:
                Input  bytes  :                    0                    0 bps
                Output bytes  :                    0                    0 bps
                Input  packets:                    0                    0 pps
                Output packets:                    0                    0 pps
                Protocol inet, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 159, Route table: 2
                Flags: Is-Primary

            Physical interface: ge-0/0/1, Enabled, Physical link is Up
            Interface index: 149, SNMP ifIndex: 527, Generation: 152
            Description: YW7079/9.6G/BB/sjkGDS221-EC11_xe-0/1/5[SJC]_Area8_Cost100
            Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
            Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
            Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
            Pad to minimum frame size: Disabled
            Device flags   : Present Running
            Interface flags: SNMP-Traps Internal: 0x4000
            Link flags     : None
            CoS queues     : 8 supported, 8 maximum usable queues
            Hold-times     : Up 2000 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 00:50:56:ff:37:f9, Hardware address: 00:50:56:ff:37:f9
            Last flapped   : 2019-08-29 09:09:19 UTC (29w6d 22:19 ago)
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :          34950288700                 5304 bps
            Output bytes  :          42783271407                 8016 bps
            Input  packets:            376916510                    9 pps
            Output packets:            370594612                    9 pps
            IPv6 transit statistics:
            Input  bytes  :           3303092203
            Output bytes  :           3127179954
            Input  packets:             41039648
            Output packets:             41594426
            Label-switched interface (LSI) traffic statistics:
            Input  bytes  :                    0                    0 bps
            Input  packets:                    0                    0 pps
            Dropped traffic statistics due to STP State:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0,
                L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 1, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0,
                MTU errors: 0, Resource errors: 0
            Active alarms  : None
            Active defects : None
            PCS statistics                      Seconds
                Bit errors                             0
                Errored blocks                         0
            Ethernet FEC statistics              Errors
                FEC Corrected Errors                    0
                FEC Uncorrected Errors                  0
                FEC Corrected Errors Rate               0
                FEC Uncorrected Errors Rate             0
            MAC statistics:                      Receive         Transmit
                Total octets                   40247994921      45995779695
                Total packets                    376916517        370414748
                Unicast packets                  376916499        370414722
                Broadcast packets                        0                0
                Multicast packets                        0                0
                CRC/Align errors                         0                0
                FIFO errors                              0                0
                MAC control frames                       0                0
                MAC pause frames                         0                0
                Oversized frames                         0
                Jabber frames                            0
                Fragment frames                          0
                VLAN tagged frames                       0
                Code violations                          0
                Total errors                             0                0
            Filter statistics:
                Input packet count               376916499
                Input packet rejects                    41
                Input DA rejects                         4
                Input SA rejects                         0
                Output packet count                               370414722
                Output packet pad count                                   0
                Output packet error count                                 0
                CAM destination filters: 0, CAM source filters: 0
            Autonegotiation information:
                Negotiation status: Incomplete
            Packet Forwarding Engine configuration:
                Destination slot: 0 (0x00)
            CoS information:
                Direction : Output
                CoS transmit queue               Bandwidth               Buffer Priority   Limit
                                        %            bps     %           usec
                0 best-effort            95      950000000    95              0      low    none
                3 network-control         5       50000000     5              0      low    none
            Interface transmit statistics: Disabled

            Logical interface ge-0/0/1.0 (Index 334) (SNMP ifIndex 605) (Generation 143)
                Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
                Traffic statistics:
                Input  bytes  :          34950288700
                Output bytes  :          42238503795
                Input  packets:            376916510
                Output packets:            370594612
                IPv6 transit statistics:
                Input  bytes  :           3303092203
                Output bytes  :           3127179954
                Input  packets:             41039648
                Output packets:             41594426
                Local statistics:
                Input  bytes  :          13617655381
                Output bytes  :          18694395654
                Input  packets:             85070342
                Output packets:             90794602
                Transit statistics:
                Input  bytes  :          21332633319                 3368 bps
                Output bytes  :          23544108141                 2144 bps
                Input  packets:            291846168                    6 pps
                Output packets:            279800010                    4 pps
                IPv6 transit statistics:
                Input  bytes  :          3303092203                 3360 bps
                Output bytes  :          3127179954                 1136 bps
                Input  packets:            41039648                    5 pps
                Output packets:            41594426                    1 pps
                Protocol inet, MTU: 1500
                Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 164, Route table: 0
                Flags: No-Redirects, Sendbcast-pkt-to-re
                Input Filters: catch_all
                Addresses, Flags: Is-Preferred Is-Primary
                    Destination: 10.169.14.120/30, Local: 10.169.14.122, Broadcast: 10.169.14.123, Generation: 152
                Protocol inet6, MTU: 1500
                Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 2, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 165, Route table: 0
                Input Filters: v6_catch_all
                Addresses, Flags: Is-Preferred Is-Primary
                    Destination: 2001:db8:eb18:6337::/64, Local: 2001:db8:eb18:6337::2
                Generation: 154
                Addresses, Flags: Is-Preferred
                    Destination: fe80::/64, Local: fe80::250:56ff:feff:37f9
                Protocol mpls, MTU: 1488, Maximum labels: 3, Generation: 156
                Protocol multiservice, MTU: Unlimited, Generation: 166, Route table: 0
                Generation: 167, Route table: 0
                Policer: Input: __default_arp_policer__

            Physical interface: ge-0/0/2, Enabled, Physical link is Up
            Interface index: 150, SNMP ifIndex: 528, Generation: 153
            Description: ve-hkgasr01_Gi2[DefaultCost1000]
            Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
            Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
            Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
            Pad to minimum frame size: Disabled
            Device flags   : Present Running
            Interface flags: SNMP-Traps Internal: 0x4000
            Link flags     : None
            CoS queues     : 8 supported, 8 maximum usable queues
            Hold-times     : Up 2000 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 00:50:56:ff:1e:ba, Hardware address: 00:50:56:ff:1e:ba
            Last flapped   : 2020-03-05 16:04:34 UTC (2w6d 15:23 ago)
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :          34302334175                  880 bps
            Output bytes  :          27932035013                  880 bps
            Input  packets:            248114960                    1 pps
            Output packets:            229304654                    0 pps
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Label-switched interface (LSI) traffic statistics:
            Input  bytes  :                    0                    0 bps
            Input  packets:                    0                    0 pps
            Dropped traffic statistics due to STP State:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0,
                L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 47, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0,
                MTU errors: 0, Resource errors: 0
            Active alarms  : None
            Active defects : None
            PCS statistics                      Seconds
                Bit errors                             0
                Errored blocks                         0
            Ethernet FEC statistics              Errors
                FEC Corrected Errors                    0
                FEC Uncorrected Errors                  0
                FEC Corrected Errors Rate               0
                FEC Uncorrected Errors Rate             0
            MAC statistics:                      Receive         Transmit
                Total octets                   38187795706      30274309615
                Total packets                    252983787        229070544
                Unicast packets                  252983783        229070540
                Broadcast packets                        0                0
                Multicast packets                        0                0
                CRC/Align errors                         0                0
                FIFO errors                              0                0
                MAC control frames                       0                0
                MAC pause frames                         0                0
                Oversized frames                         0
                Jabber frames                            0
                Fragment frames                          0
                VLAN tagged frames                       0
                Code violations                          0
                Total errors                             0                0
            Filter statistics:
                Input packet count               252983783
                Input packet rejects                335972
                Input DA rejects                         0
                Input SA rejects                         0
                Output packet count                               229070540
                Output packet pad count                                   0
                Output packet error count                                 0
                CAM destination filters: 0, CAM source filters: 0
            Autonegotiation information:
                Negotiation status: Incomplete
            Packet Forwarding Engine configuration:
                Destination slot: 0 (0x00)
            CoS information:
                Direction : Output
                CoS transmit queue               Bandwidth               Buffer Priority   Limit
                                        %            bps     %           usec
                0 best-effort            95      950000000    95              0      low    none
                3 network-control         5       50000000     5              0      low    none
            Interface transmit statistics: Disabled

            Logical interface ge-0/0/2.0 (Index 336) (SNMP ifIndex 536) (Generation 148)
                Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
                Traffic statistics:
                Input  bytes  :          31231373218
                Output bytes  :          27263935504
                Input  packets:            210377499
                Output packets:            222609631
                Local statistics:
                Input  bytes  :          11458939228
                Output bytes  :          13615419042
                Input  packets:             31742480
                Output packets:             28915016
                Transit statistics:
                Input  bytes  :          19772433990                  880 bps
                Output bytes  :          13648516462                  360 bps
                Input  packets:            178635019                    1 pps
                Output packets:            193694615                    0 pps
                Protocol inet, MTU: 1500
                Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 179, Route table: 0
                Flags: Sendbcast-pkt-to-re
                Addresses, Flags: Is-Preferred Is-Primary
                    Destination: 10.19.198.24/30, Local: 10.19.198.25, Broadcast: 10.19.198.27, Generation: 166
                Protocol mpls, MTU: 1488, Maximum labels: 3, Generation: 180, Route table: 0
                Protocol multiservice, MTU: Unlimited, Generation: 181, Route table: 0
                Policer: Input: __default_arp_policer__

            Physical interface: ge-0/0/3, Enabled, Physical link is Up
            Interface index: 151, SNMP ifIndex: 529, Generation: 154
            Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
            Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
            Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
            Pad to minimum frame size: Disabled
            Device flags   : Present Running
            Interface flags: SNMP-Traps Internal: 0x4000
            Link flags     : None
            CoS queues     : 8 supported, 8 maximum usable queues
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 00:50:56:ff:93:cb, Hardware address: 00:50:56:ff:93:cb
            Last flapped   : 2019-10-25 08:50:18 UTC (21w5d 22:38 ago)
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :              1092968                    0 bps
            Output bytes  :              3419965                    0 bps
            Input  packets:                14619                    0 pps
            Output packets:                17426                    0 pps
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Dropped traffic statistics due to STP State:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0,
                L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 3, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0,
                MTU errors: 0, Resource errors: 0
            Active alarms  : None
            Active defects : None
            PCS statistics                      Seconds
                Bit errors                             0
                Errored blocks                         0
            Ethernet FEC statistics              Errors
                FEC Corrected Errors                    0
                FEC Uncorrected Errors                  0
                FEC Corrected Errors Rate               0
                FEC Uncorrected Errors Rate             0
            MAC statistics:                      Receive         Transmit
                Total octets                       1157295          3441533
                Total packets                        14683            17425
                Unicast packets                      14683            17425
                Broadcast packets                        0                0
                Multicast packets                        0                0
                CRC/Align errors                         0                0
                FIFO errors                              0                0
                MAC control frames                       0                0
                MAC pause frames                         0                0
                Oversized frames                         0
                Jabber frames                            0
                Fragment frames                          0
                VLAN tagged frames                       0
                Code violations                          0
                Total errors                             0                0
            Filter statistics:
                Input packet count                   14683
                Input packet rejects                    65
                Input DA rejects                         0
                Input SA rejects                         0
                Output packet count                                   17425
                Output packet pad count                                   0
                Output packet error count                                 0
                CAM destination filters: 0, CAM source filters: 0
            Autonegotiation information:
                Negotiation status: Incomplete
            Packet Forwarding Engine configuration:
                Destination slot: 0 (0x00)
            CoS information:
                Direction : Output
                CoS transmit queue               Bandwidth               Buffer Priority   Limit
                                        %            bps     %           usec
                0 best-effort            95      950000000    95              0      low    none
                3 network-control         5       50000000     5              0      low    none
            Interface transmit statistics: Disabled

            Logical interface ge-0/0/3.0 (Index 335) (SNMP ifIndex 537) (Generation 146)
                Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
                Traffic statistics:
                Input  bytes  :              1092968
                Output bytes  :              3353155
                Input  packets:                14619
                Output packets:                17426
                Local statistics:
                Input  bytes  :               667980
                Output bytes  :               467670
                Input  packets:                11133
                Output packets:                11135
                Transit statistics:
                Input  bytes  :               424988                    0 bps
                Output bytes  :              2885485                    0 bps
                Input  packets:                 3486                    0 pps
                Output packets:                 6291                    0 pps
                Protocol inet, MTU: 1500
                Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 174, Route table: 0
                Flags: Sendbcast-pkt-to-re
                Addresses, Flags: Is-Preferred Is-Primary
                    Destination: 100.0.0/24, Local: 10.55.0.254, Broadcast: 10.55.0.255, Generation: 162
                Protocol multiservice, MTU: Unlimited, Generation: 175, Route table: 0
                Policer: Input: __default_arp_policer__

            Physical interface: ge-0/0/4, Enabled, Physical link is Down
            Interface index: 152, SNMP ifIndex: 530, Generation: 155
            Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
            Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
            Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
            Pad to minimum frame size: Disabled
            Device flags   : Present Running Down
            Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
            Link flags     : None
            CoS queues     : 8 supported, 8 maximum usable queues
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 00:50:56:ff:3e:28, Hardware address: 00:50:56:ff:3e:28
            Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 22:19 ago)
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0                    0 bps
            Output bytes  :                    0                    0 bps
            Input  packets:                    0                    0 pps
            Output packets:                    0                    0 pps
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Dropped traffic statistics due to STP State:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0,
                L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 2, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0,
                MTU errors: 0, Resource errors: 0
            Active alarms  : LINK
            Active defects : LINK
            PCS statistics                      Seconds
                Bit errors                             0
                Errored blocks                         0
            Ethernet FEC statistics              Errors
                FEC Corrected Errors                    0
                FEC Uncorrected Errors                  0
                FEC Corrected Errors Rate               0
                FEC Uncorrected Errors Rate             0
            MAC statistics:                      Receive         Transmit
                Total octets                             0                0
                Total packets                            0                0
                Unicast packets                          0                0
                Broadcast packets                        0                0
                Multicast packets                        0                0
                CRC/Align errors                         0                0
                FIFO errors                              0                0
                MAC control frames                       0                0
                MAC pause frames                         0                0
                Oversized frames                         0
                Jabber frames                            0
                Fragment frames                          0
                VLAN tagged frames                       0
                Code violations                          0
                Total errors                             0                0
            Filter statistics:
                Input packet count                       0
                Input packet rejects                     0
                Input DA rejects                         0
                Input SA rejects                         0
                Output packet count                                       0
                Output packet pad count                                   0
                Output packet error count                                 0
                CAM destination filters: 0, CAM source filters: 0
            Autonegotiation information:
                Negotiation status: Incomplete
            Packet Forwarding Engine configuration:
                Destination slot: 0 (0x00)
            CoS information:
                Direction : Output
                CoS transmit queue               Bandwidth               Buffer Priority   Limit
                                        %            bps     %           usec
                0 best-effort            95      950000000    95              0      low    none
                3 network-control         5       50000000     5              0      low    none
            Interface transmit statistics: Disabled

            Physical interface: ge-0/0/5, Enabled, Physical link is Down
            Interface index: 153, SNMP ifIndex: 531, Generation: 156
            Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
            Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
            Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
            Pad to minimum frame size: Disabled
            Device flags   : Present Running Down
            Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
            Link flags     : None
            CoS queues     : 8 supported, 8 maximum usable queues
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 2c:6b:f5:ff:01:1d, Hardware address: 2c:6b:f5:ff:01:1d
            Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 22:19 ago)
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0                    0 bps
            Output bytes  :                    0                    0 bps
            Input  packets:                    0                    0 pps
            Output packets:                    0                    0 pps
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Dropped traffic statistics due to STP State:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0,
                L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 2, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0,
                MTU errors: 0, Resource errors: 0
            Active alarms  : LINK
            Active defects : LINK
            PCS statistics                      Seconds
                Bit errors                             0
                Errored blocks                         0
            Ethernet FEC statistics              Errors
                FEC Corrected Errors                    0
                FEC Uncorrected Errors                  0
                FEC Corrected Errors Rate               0
                FEC Uncorrected Errors Rate             0
            MAC statistics:                      Receive         Transmit
                Total octets                             0                0
                Total packets                            0                0
                Unicast packets                          0                0
                Broadcast packets                        0                0
                Multicast packets                        0                0
                CRC/Align errors                         0                0
                FIFO errors                              0                0
                MAC control frames                       0                0
                MAC pause frames                         0                0
                Oversized frames                         0
                Jabber frames                            0
                Fragment frames                          0
                VLAN tagged frames                       0
                Code violations                          0
                Total errors                             0                0
            Filter statistics:
                Input packet count                       0
                Input packet rejects                     0
                Input DA rejects                         0
                Input SA rejects                         0
                Output packet count                                       0
                Output packet pad count                                   0
                Output packet error count                                 0
                CAM destination filters: 0, CAM source filters: 0
            Autonegotiation information:
                Negotiation status: Incomplete
            Packet Forwarding Engine configuration:
                Destination slot: 0 (0x00)
            CoS information:
                Direction : Output
                CoS transmit queue               Bandwidth               Buffer Priority   Limit
                                        %            bps     %           usec
                0 best-effort            95      950000000    95              0      low    none
                3 network-control         5       50000000     5              0      low    none
            Interface transmit statistics: Disabled

            Physical interface: ge-0/0/6, Enabled, Physical link is Down
            Interface index: 154, SNMP ifIndex: 532, Generation: 157
            Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
            Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
            Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
            Pad to minimum frame size: Disabled
            Device flags   : Present Running Down
            Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
            Link flags     : None
            CoS queues     : 8 supported, 8 maximum usable queues
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 2c:6b:f5:ff:01:1e, Hardware address: 2c:6b:f5:ff:01:1e
            Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 22:19 ago)
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0                    0 bps
            Output bytes  :                    0                    0 bps
            Input  packets:                    0                    0 pps
            Output packets:                    0                    0 pps
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Dropped traffic statistics due to STP State:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0,
                L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 2, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0,
                MTU errors: 0, Resource errors: 0
            Active alarms  : LINK
            Active defects : LINK
            PCS statistics                      Seconds
                Bit errors                             0
                Errored blocks                         0
            Ethernet FEC statistics              Errors
                FEC Corrected Errors                    0
                FEC Uncorrected Errors                  0
                FEC Corrected Errors Rate               0
                FEC Uncorrected Errors Rate             0
            MAC statistics:                      Receive         Transmit
                Total octets                             0                0
                Total packets                            0                0
                Unicast packets                          0                0
                Broadcast packets                        0                0
                Multicast packets                        0                0
                CRC/Align errors                         0                0
                FIFO errors                              0                0
                MAC control frames                       0                0
                MAC pause frames                         0                0
                Oversized frames                         0
                Jabber frames                            0
                Fragment frames                          0
                VLAN tagged frames                       0
                Code violations                          0
                Total errors                             0                0
            Filter statistics:
                Input packet count                       0
                Input packet rejects                     0
                Input DA rejects                         0
                Input SA rejects                         0
                Output packet count                                       0
                Output packet pad count                                   0
                Output packet error count                                 0
                CAM destination filters: 0, CAM source filters: 0
            Autonegotiation information:
                Negotiation status: Incomplete
            Packet Forwarding Engine configuration:
                Destination slot: 0 (0x00)
            CoS information:
                Direction : Output
                CoS transmit queue               Bandwidth               Buffer Priority   Limit
                                        %            bps     %           usec
                0 best-effort            95      950000000    95              0      low    none
                3 network-control         5       50000000     5              0      low    none
            Interface transmit statistics: Disabled

            Physical interface: ge-0/0/7, Enabled, Physical link is Down
            Interface index: 155, SNMP ifIndex: 533, Generation: 158
            Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
            Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
            Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
            Pad to minimum frame size: Disabled
            Device flags   : Present Running Down
            Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
            Link flags     : None
            CoS queues     : 8 supported, 8 maximum usable queues
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 2c:6b:f5:ff:01:1f, Hardware address: 2c:6b:f5:ff:01:1f
            Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 22:19 ago)
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0                    0 bps
            Output bytes  :                    0                    0 bps
            Input  packets:                    0                    0 pps
            Output packets:                    0                    0 pps
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Dropped traffic statistics due to STP State:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0,
                L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 2, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0,
                MTU errors: 0, Resource errors: 0
            Active alarms  : LINK
            Active defects : LINK
            PCS statistics                      Seconds
                Bit errors                             0
                Errored blocks                         0
            Ethernet FEC statistics              Errors
                FEC Corrected Errors                    0
                FEC Uncorrected Errors                  0
                FEC Corrected Errors Rate               0
                FEC Uncorrected Errors Rate             0
            MAC statistics:                      Receive         Transmit
                Total octets                             0                0
                Total packets                            0                0
                Unicast packets                          0                0
                Broadcast packets                        0                0
                Multicast packets                        0                0
                CRC/Align errors                         0                0
                FIFO errors                              0                0
                MAC control frames                       0                0
                MAC pause frames                         0                0
                Oversized frames                         0
                Jabber frames                            0
                Fragment frames                          0
                VLAN tagged frames                       0
                Code violations                          0
                Total errors                             0                0
            Filter statistics:
                Input packet count                       0
                Input packet rejects                     0
                Input DA rejects                         0
                Input SA rejects                         0
                Output packet count                                       0
                Output packet pad count                                   0
                Output packet error count                                 0
                CAM destination filters: 0, CAM source filters: 0
            Autonegotiation information:
                Negotiation status: Incomplete
            Packet Forwarding Engine configuration:
                Destination slot: 0 (0x00)
            CoS information:
                Direction : Output
                CoS transmit queue               Bandwidth               Buffer Priority   Limit
                                        %            bps     %           usec
                0 best-effort            95      950000000    95              0      low    none
                3 network-control         5       50000000     5              0      low    none
            Interface transmit statistics: Disabled

            Physical interface: ge-0/0/8, Enabled, Physical link is Down
            Interface index: 156, SNMP ifIndex: 534, Generation: 159
            Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
            Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
            Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
            Pad to minimum frame size: Disabled
            Device flags   : Present Running Down
            Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
            Link flags     : None
            CoS queues     : 8 supported, 8 maximum usable queues
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 2c:6b:f5:ff:01:20, Hardware address: 2c:6b:f5:ff:01:20
            Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 22:19 ago)
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0                    0 bps
            Output bytes  :                    0                    0 bps
            Input  packets:                    0                    0 pps
            Output packets:                    0                    0 pps
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Dropped traffic statistics due to STP State:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0,
                L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 2, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0,
                MTU errors: 0, Resource errors: 0
            Active alarms  : LINK
            Active defects : LINK
            PCS statistics                      Seconds
                Bit errors                             0
                Errored blocks                         0
            Ethernet FEC statistics              Errors
                FEC Corrected Errors                    0
                FEC Uncorrected Errors                  0
                FEC Corrected Errors Rate               0
                FEC Uncorrected Errors Rate             0
            MAC statistics:                      Receive         Transmit
                Total octets                             0                0
                Total packets                            0                0
                Unicast packets                          0                0
                Broadcast packets                        0                0
                Multicast packets                        0                0
                CRC/Align errors                         0                0
                FIFO errors                              0                0
                MAC control frames                       0                0
                MAC pause frames                         0                0
                Oversized frames                         0
                Jabber frames                            0
                Fragment frames                          0
                VLAN tagged frames                       0
                Code violations                          0
                Total errors                             0                0
            Filter statistics:
                Input packet count                       0
                Input packet rejects                     0
                Input DA rejects                         0
                Input SA rejects                         0
                Output packet count                                       0
                Output packet pad count                                   0
                Output packet error count                                 0
                CAM destination filters: 0, CAM source filters: 0
            Autonegotiation information:
                Negotiation status: Incomplete
            Packet Forwarding Engine configuration:
                Destination slot: 0 (0x00)
            CoS information:
                Direction : Output
                CoS transmit queue               Bandwidth               Buffer Priority   Limit
                                        %            bps     %           usec
                0 best-effort            95      950000000    95              0      low    none
                3 network-control         5       50000000     5              0      low    none
            Interface transmit statistics: Disabled

            Physical interface: ge-0/0/9, Enabled, Physical link is Down
            Interface index: 157, SNMP ifIndex: 535, Generation: 160
            Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
            Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
            Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
            Pad to minimum frame size: Disabled
            Device flags   : Present Running Down
            Interface flags: Hardware-Down SNMP-Traps Internal: 0x4000
            Link flags     : None
            CoS queues     : 8 supported, 8 maximum usable queues
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 2c:6b:f5:ff:01:21, Hardware address: 2c:6b:f5:ff:01:21
            Last flapped   : 2019-08-29 09:09:20 UTC (29w6d 22:19 ago)
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0                    0 bps
            Output bytes  :                    0                    0 bps
            Input  packets:                    0                    0 pps
            Output packets:                    0                    0 pps
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Dropped traffic statistics due to STP State:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0,
                L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 2, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0,
                MTU errors: 0, Resource errors: 0
            Active alarms  : LINK
            Active defects : LINK
            PCS statistics                      Seconds
                Bit errors                             0
                Errored blocks                         0
            Ethernet FEC statistics              Errors
                FEC Corrected Errors                    0
                FEC Uncorrected Errors                  0
                FEC Corrected Errors Rate               0
                FEC Uncorrected Errors Rate             0
            MAC statistics:                      Receive         Transmit
                Total octets                             0                0
                Total packets                            0                0
                Unicast packets                          0                0
                Broadcast packets                        0                0
                Multicast packets                        0                0
                CRC/Align errors                         0                0
                FIFO errors                              0                0
                MAC control frames                       0                0
                MAC pause frames                         0                0
                Oversized frames                         0
                Jabber frames                            0
                Fragment frames                          0
                VLAN tagged frames                       0
                Code violations                          0
                Total errors                             0                0
            Filter statistics:
                Input packet count                       0
                Input packet rejects                     0
                Input DA rejects                         0
                Input SA rejects                         0
                Output packet count                                       0
                Output packet pad count                                   0
                Output packet error count                                 0
                CAM destination filters: 0, CAM source filters: 0
            Autonegotiation information:
                Negotiation status: Incomplete
            Packet Forwarding Engine configuration:
                Destination slot: 0 (0x00)
            CoS information:
                Direction : Output
                CoS transmit queue               Bandwidth               Buffer Priority   Limit
                                        %            bps     %           usec
                0 best-effort            95      950000000    95              0      low    none
                3 network-control         5       50000000     5              0      low    none
            Interface transmit statistics: Disabled

            Physical interface: .local., Enabled, Physical link is Up
            Interface index: 0, SNMP ifIndex: 0, Generation: 1
            Type: Loopback, Link-level type: Interface-Specific, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running Loopback
            Interface flags: Point-To-Point
            Link type      : Unspecified
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Logical interface .local..0 (Index 0) (SNMP ifIndex 0) (Generation 1)
                Flags: Point-To-Point Encapsulation: Unspecified
                Bandwidth: 0
                Protocol inet, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 133, Route table: 0
                Flags: None
                Addresses, Flags: Is-Primary
                    Destination: Unspecified, Local: 10.1.0.101, Broadcast: Unspecified, Generation: 133
                Addresses, Flags: None
                    Destination: Unspecified, Local: 10.19.198.25, Broadcast: Unspecified, Generation: 165
                Addresses, Flags: None
                    Destination: Unspecified, Local: 10.55.0.254, Broadcast: Unspecified, Generation: 161
                Addresses, Flags: None
                    Destination: Unspecified, Local: 10.169.14.122, Broadcast: Unspecified, Generation: 151
                Addresses, Flags: None
                    Destination: Unspecified, Local: 10.189.5.93, Broadcast: Unspecified, Generation: 145
                Addresses, Flags: None
                    Destination: Unspecified, Local: 10.189.5.252, Broadcast: Unspecified, Generation: 134
                Protocol iso, MTU: Unlimited, Generation: 132, Route table: 0
                Flags: None
                Protocol inet6, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 130, Route table: 0
                Flags: None
                Addresses, Flags: None
                    Destination: Unspecified, Local: 2001:db8:eb18:6337::2
                Generation: 153
                Addresses, Flags: None
                    Destination: Unspecified, Local: 2001:db8:223c:ca45::b
                Generation: 136
                Addresses, Flags: None
                    Destination: Unspecified, Local: 2001:db8:223c:2c16::1
                Generation: 147
                Addresses, Flags: None
                    Destination: Unspecified, Local: fe80::250:560f:fc8d:7c08
                Generation: 138
                Addresses, Flags: None
                    Destination: Unspecified, Local: fe80::250:56ff:feff:37f9
                Generation: 155
                Addresses, Flags: None
                    Destination: Unspecified, Local: fe80::250:56ff:feff:56b6
                Protocol mpls, MTU: Unlimited, Maximum labels: 3, Generation: 149
                Generation: 137, Route table: 0
                Flags: None
                Protocol 85, MTU: Unlimited, Generation: 129, Route table: 0
                Flags: None

            Logical interface .local..1 (Index 1) (SNMP ifIndex 0) (Generation 2)
                Flags: Point-To-Point Encapsulation: Unspecified
                Bandwidth: 0
                Protocol inet, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 134, Route table: 1
                Flags: None
                Addresses, Flags: Is-Primary
                    Destination: Unspecified, Local: 10.0.0.4, Broadcast: Unspecified, Generation: 130
                Addresses, Flags: None
                    Destination: Unspecified, Local: 172.16.64.1, Broadcast: Unspecified, Generation: 142
                Addresses, Flags: None
                    Destination: Unspecified, Local: 172.16.64.4, Broadcast: Unspecified, Generation: 129
                Protocol inet6, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 131, Route table: 1
                Flags: None
                Addresses, Flags: None
                    Destination: Unspecified, Local: fe80::250:56ff:feff:e2c1
                Generation: 131
                Addresses, Flags: None
                    Destination: Unspecified, Local: 2001:db8:8d82::a:0:0:4
                Protocol vpls, MTU: Unlimited, Generation: 132
                Generation: 138, Route table: 1
                Flags: None

            Logical interface .local..2 (Index 2) (SNMP ifIndex 0) (Generation 2)
                Flags: Point-To-Point Encapsulation: Unspecified
                Bandwidth: 0
                Protocol inet, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 135, Route table: 2
                Flags: None
                Addresses, Flags: Is-Primary
                    Destination: Unspecified, Local: 127.0.0.1, Broadcast: Unspecified, Generation: 140

            Logical interface .local..3 (Index 323) (SNMP ifIndex 0) (Generation 132)
                Flags: Point-To-Point Encapsulation: Unspecified
                Bandwidth: 0
                Protocol inet, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 147, Route table: 3
                Flags: None

            Logical interface .local..4 (Index 324) (SNMP ifIndex 0) (Generation 133)
                Flags: Point-To-Point Encapsulation: Unspecified
                Bandwidth: 0
                Protocol inet, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 148, Route table: 4
                Flags: None
                Addresses, Flags: Is-Primary
                    Destination: Unspecified, Local: 172.16.64.127, Broadcast: Unspecified, Generation: 143

            Logical interface .local..5 (Index 326) (SNMP ifIndex 0) (Generation 135)
                Flags: Point-To-Point Encapsulation: Unspecified
                Bandwidth: 0
                Protocol inet, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 150, Route table: 5
                Flags: None
                Protocol iso, MTU: Unlimited, Generation: 151, Route table: 5
                Flags: None
                Protocol inet6, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 153, Route table: 5
                Flags: None

            Logical interface .local..6 (Index 327) (SNMP ifIndex 0) (Generation 136)
                Flags: Point-To-Point Encapsulation: Unspecified
                Bandwidth: 0
                Protocol mpls, MTU: Unlimited, Maximum labels: 3, Generation: 152, Route table: 6
                Flags: None

            Logical interface .local..7 (Index 328) (SNMP ifIndex 0) (Generation 137)
                Flags: Point-To-Point Encapsulation: Unspecified
                Bandwidth: 0
                Protocol vpls, MTU: Unlimited, Generation: 154, Route table: 7
                Flags: None

            Logical interface .local..36735 (Index 262016) (SNMP ifIndex 0) (Generation 2)
                Flags: Point-To-Point Encapsulation: Unspecified
                Bandwidth: 0

            Logical interface .local..36736 (Index 262017) (SNMP ifIndex 0) (Generation 2)
                Flags: Point-To-Point Encapsulation: Unspecified
                Bandwidth: 0
                Protocol inet, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 136, Route table: 36736
                Flags: None

            Logical interface .local..36737 (Index 262018) (SNMP ifIndex 0) (Generation 2)
                Flags: Point-To-Point Encapsulation: Unspecified
                Bandwidth: 0

            Logical interface .local..36738 (Index 262019) (SNMP ifIndex 0) (Generation 1)
                Flags: Point-To-Point Encapsulation: Unspecified
                Bandwidth: 0

            Physical interface: cbp0, Enabled, Physical link is Up
            Interface index: 129, SNMP ifIndex: 501, Generation: 132
            Type: Ethernet, Link-level type: Ethernet, MTU: 9192, Clocking: Unspecified, Speed: Unspecified
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 2c:6b:f5:ff:01:29, Hardware address: 2c:6b:f5:ff:01:29
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: demux0, Enabled, Physical link is Up
            Interface index: 128, SNMP ifIndex: 502, Generation: 131
            Type: Software-Pseudo, Link-level type: Unspecified, MTU: 9192, Clocking: 1, Speed: Unspecified
            Device flags   : Present Running
            Interface flags: Point-To-Point SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: dsc, Enabled, Physical link is Up
            Interface index: 5, SNMP ifIndex: 5, Generation: 6
            Type: Software-Pseudo, Link-level type: Unspecified, MTU: Unlimited, Clocking: Unspecified, Speed: Unspecified
            Device flags   : Present Running
            Interface flags: Point-To-Point SNMP-Traps
            Link type      : Unspecified
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: em1, Enabled, Physical link is Up
            Interface index: 65, SNMP ifIndex: 23, Generation: 2
            Type: Ethernet, Link-level type: Ethernet, MTU: 1514, Clocking: Unspecified, Speed: Unspecified
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Unspecified
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 00:50:56:ff:e2:c1, Hardware address: 00:50:56:ff:e2:c1
            Alternate link address: Unspecified
            Last flapped   : 2019-08-29 09:03:11 UTC (29w6d 22:25 ago)
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Logical interface em1.0 (Index 3) (SNMP ifIndex 24) (Generation 2)
                Flags: Up SNMP-Traps 0x4000000 Encapsulation: ENET2
                Traffic statistics:
                Input  bytes  :         102691292552
                Output bytes  :         106913726719
                Input  packets:            725074463
                Output packets:            794456958
                IPv6 transit statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Local statistics:
                Input  bytes  :         102691292552
                Output bytes  :         106913726719
                Input  packets:            725074463
                Output packets:            794456958
                Protocol inet, MTU: 1500
                Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 139, Route table: 1
                Flags: Is-Primary
                Addresses, Flags: Is-Preferred
                    Destination: 10/8, Local: 10.0.0.4, Broadcast: 10.255.255.255, Generation: 2
                Addresses, Flags: Preferred Kernel Is-Preferred
                    Destination: 128/2, Local: 172.16.64.1, Broadcast: 172.16.16.255, Generation: 7
                Addresses, Flags: Primary Is-Default Is-Primary
                    Destination: 128/2, Local: 172.16.64.4, Broadcast: 172.16.16.255, Generation: 1
                Protocol inet6, MTU: 1500
                Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 1, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 140, Route table: 1
                Flags: Is-Primary
                Addresses, Flags: Is-Preferred
                    Destination: fe80::/64, Local: fe80::250:56ff:feff:e2c1
                Generation: 3
                Addresses, Flags: Is-Default Is-Preferred Is-Primary
                    Destination: 2001:db8:8d82::/64, Local: 2001:db8:8d82::a:0:0:4
                Protocol tnp, MTU: 1500, Generation: 4
                Generation: 141, Route table: 1
                Flags: Primary, Is-Primary
                Addresses, Flags: None
                    Destination: Unspecified, Local: 0x4, Broadcast: Unspecified, Generation: 5

            Physical interface: esi, Enabled, Physical link is Up
            Interface index: 134, SNMP ifIndex: 503, Generation: 137
            Type: Software-Pseudo, Link-level type: VxLAN-Tunnel-Endpoint, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: fti0, Enabled, Physical link is Up
            Interface index: 136, SNMP ifIndex: 504, Generation: 139
            Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: fti1, Enabled, Physical link is Up
            Interface index: 137, SNMP ifIndex: 505, Generation: 140
            Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: fti2, Enabled, Physical link is Up
            Interface index: 138, SNMP ifIndex: 506, Generation: 141
            Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: fti3, Enabled, Physical link is Up
            Interface index: 139, SNMP ifIndex: 507, Generation: 142
            Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: fti4, Enabled, Physical link is Up
            Interface index: 140, SNMP ifIndex: 508, Generation: 143
            Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: fti5, Enabled, Physical link is Up
            Interface index: 141, SNMP ifIndex: 509, Generation: 144
            Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: fti6, Enabled, Physical link is Up
            Interface index: 142, SNMP ifIndex: 510, Generation: 145
            Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: fti7, Enabled, Physical link is Up
            Interface index: 143, SNMP ifIndex: 511, Generation: 146
            Type: FTI, Link-level type: Flexible-tunnel-Interface, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: fxp0, Enabled, Physical link is Up
            Interface index: 64, SNMP ifIndex: 1, Generation: 1
            Type: Ethernet, Link-level type: Ethernet, MTU: 1514, Clocking: Unspecified, Speed: Unspecified
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Unspecified
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 00:50:56:ff:0a:95, Hardware address: 00:50:56:ff:0a:95
            Alternate link address: Unspecified
            Last flapped   : 2019-08-29 09:03:11 UTC (29w6d 22:25 ago)
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Logical interface fxp0.0 (Index 4) (SNMP ifIndex 13) (Generation 3)
                Flags: Up SNMP-Traps 0x4000000 Encapsulation: ENET2
                Traffic statistics:
                Input  bytes  :             46289683
                Output bytes  :            207724636
                Input  packets:               620829
                Output packets:               896062
                Local statistics:
                Input  bytes  :             46289683
                Output bytes  :            207724636
                Input  packets:               620829
                Output packets:               896062
                Protocol inet, MTU: 1500
                Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 2, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 142, Route table: 0
                Flags: Sendbcast-pkt-to-re, Is-Primary
                Addresses, Flags: Is-Preferred Is-Primary
                    Destination: 1.0.0/24, Local: 10.1.0.101, Broadcast: 10.1.0.255, Generation: 6

            Physical interface: gre, Enabled, Physical link is Up
            Interface index: 10, SNMP ifIndex: 8, Generation: 11
            Type: GRE, Link-level type: GRE, MTU: Unlimited, Speed: Unlimited
            Hold-times     : Up 0 ms, Down 0 ms
            Device flags   : Present Running
            Interface flags: Point-To-Point SNMP-Traps
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0

            Physical interface: ipip, Enabled, Physical link is Up
            Interface index: 11, SNMP ifIndex: 9, Generation: 12
            Type: IPIP, Link-level type: IP-over-IP, MTU: Unlimited, Speed: Unlimited
            Hold-times     : Up 0 ms, Down 0 ms
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0

            Physical interface: irb, Enabled, Physical link is Up
            Interface index: 132, SNMP ifIndex: 512, Generation: 135
            Type: Ethernet, Link-level type: Ethernet, MTU: 1514, Clocking: Unspecified, Speed: Unspecified
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 2c:6b:f5:ff:08:09, Hardware address: 2c:6b:f5:ff:08:09
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: jsrv, Enabled, Physical link is Up
            Interface index: 144, SNMP ifIndex: 513, Generation: 147
            Type: Ethernet, Link-level type: Ethernet, MTU: 1514, Clocking: Unspecified, Speed: Unspecified
            Device flags   : Present Running
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 2c:6b:f5:ff:08:d8, Hardware address: 2c:6b:f5:ff:08:d8
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Logical interface jsrv.1 (Index 325) (SNMP ifIndex 514) (Generation 134)
                Flags: Up 0x24004000 Encapsulation: unknown
                Bandwidth: 1Gbps
                Routing Instance: None Bridging Domain: None
                Traffic statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Local statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Transit statistics:
                Input  bytes  :                    0                    0 bps
                Output bytes  :                    0                    0 bps
                Input  packets:                    0                    0 pps
                Output packets:                    0                    0 pps
                Protocol inet, MTU: 1514
                Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 149, Route table: 4
                Flags: Is-Primary
                Addresses, Flags: Primary Is-Default Is-Preferred Is-Primary
                    Destination: 128/2, Local: 172.16.64.127, Broadcast: 172.16.16.255, Generation: 144

            Physical interface: lo0, Enabled, Physical link is Up
            Interface index: 6, SNMP ifIndex: 6, Generation: 7
            Type: Loopback, Link-level type: Unspecified, MTU: Unlimited, Clocking: Unspecified, Speed: Unspecified
            Device flags   : Present Running Loopback
            Interface flags: SNMP-Traps
            Link type      : Unspecified
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :          38208810127
            Output bytes  :          38208810127
            Input  packets:             33943400
            Output packets:             33943400
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Logical interface lo0.0 (Index 320) (SNMP ifIndex 16) (Generation 129)
                Flags: SNMP-Traps Encapsulation: Unspecified
                Traffic statistics:
                Input  bytes  :                12188
                Output bytes  :                12188
                Input  packets:                   83
                Output packets:                   83
                IPv6 transit statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Local statistics:
                Input  bytes  :                12188
                Output bytes  :                12188
                Input  packets:                   83
                Output packets:                   83
                Transit statistics:
                Input  bytes  :                    0                    0 bps
                Output bytes  :                    0                    0 bps
                Input  packets:                    0                    0 pps
                Output packets:                    0                    0 pps
                IPv6 transit statistics:
                Input  bytes  :                   0                    0 bps
                Output bytes  :                   0                    0 bps
                Input  packets:                   0                    0 pps
                Output packets:                   0                    0 pps
                Protocol inet, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 143, Route table: 0
                Flags: No-Redirects, Sendbcast-pkt-to-re
                Input Filters: local-access-control
                Addresses, Flags: Is-Default Is-Primary
                    Destination: Unspecified, Local: 10.189.5.252, Broadcast: Unspecified, Generation: 135
                Protocol inet6, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 144, Route table: 0
                Input Filters: v6_local-access-control
                Addresses, Flags: Is-Default Is-Primary
                    Destination: Unspecified, Local: 2001:db8:223c:ca45::b
                Generation: 137
                    Destination: Unspecified, Local: fe80::250:560f:fc8d:7c08
                Generation: 139

            Logical interface lo0.16384 (Index 322) (SNMP ifIndex 21) (Generation 131)
                Flags: SNMP-Traps Encapsulation: Unspecified
                Traffic statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Local statistics:
                Input  bytes  :                    0
                Output bytes  :                    0
                Input  packets:                    0
                Output packets:                    0
                Transit statistics:
                Input  bytes  :                    0                    0 bps
                Output bytes  :                    0                    0 bps
                Input  packets:                    0                    0 pps
                Output packets:                    0                    0 pps
                Protocol inet, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 146, Route table: 2
                Addresses, Flags: None
                    Destination: Unspecified, Local: 127.0.0.1, Broadcast: Unspecified, Generation: 141

            Logical interface lo0.16385 (Index 321) (SNMP ifIndex 22) (Generation 130)
                Flags: SNMP-Traps Encapsulation: Unspecified
                Traffic statistics:
                Input  bytes  :          38208797939
                Output bytes  :          38208797939
                Input  packets:             33943317
                Output packets:             33943317
                Local statistics:
                Input  bytes  :          38208797939
                Output bytes  :          38208797939
                Input  packets:             33943317
                Output packets:             33943317
                Transit statistics:
                Input  bytes  :                    0                    0 bps
                Output bytes  :                    0                    0 bps
                Input  packets:                    0                    0 pps
                Output packets:                    0                    0 pps
                Protocol inet, MTU: Unlimited
                Max nh cache: 0, New hold nh limit: 0, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
                Generation: 145, Route table: 1

            Physical interface: lsi, Enabled, Physical link is Up
            Interface index: 4, SNMP ifIndex: 4, Generation: 5
            Type: Software-Pseudo, Link-level type: LSI, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running
            Link type      : Unspecified
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: mtun, Enabled, Physical link is Up
            Interface index: 66, SNMP ifIndex: 12, Generation: 3
            Type: Multicast-GRE, Link-level type: GRE, MTU: Unlimited, Speed: Unlimited
            Hold-times     : Up 0 ms, Down 0 ms
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0

            Physical interface: pimd, Enabled, Physical link is Up
            Interface index: 26, SNMP ifIndex: 11, Generation: 129
            Type: PIMD, Link-level type: PIM-Decapsulator, MTU: Unlimited, Speed: Unlimited
            Hold-times     : Up 0 ms, Down 0 ms
            Device flags   : Present Running
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0

            Physical interface: pime, Enabled, Physical link is Up
            Interface index: 25, SNMP ifIndex: 10, Generation: 130
            Type: PIME, Link-level type: PIM-Encapsulator, MTU: Unlimited, Speed: Unlimited
            Hold-times     : Up 0 ms, Down 0 ms
            Device flags   : Present Running
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0

            Physical interface: pip0, Enabled, Physical link is Up
            Interface index: 130, SNMP ifIndex: 515, Generation: 133
            Type: Ethernet, Link-level type: Ethernet, MTU: 9192, Clocking: Unspecified, Speed: Unspecified
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: 2c:6b:f5:ff:08:c8, Hardware address: 2c:6b:f5:ff:08:c8
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: pp0, Enabled, Physical link is Up
            Interface index: 131, SNMP ifIndex: 516, Generation: 134
            Type: PPPoE, Link-level type: PPPoE, MTU: 1532, Speed: Unspecified
            Device flags   : Present Running
            Interface flags: Point-To-Point SNMP-Traps
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified

            Physical interface: rbeb, Enabled, Physical link is Up
            Interface index: 135, SNMP ifIndex: 517, Generation: 138
            Type: Software-Pseudo, Link-level type: Remote-BEB, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: tap, Enabled, Physical link is Up
            Interface index: 12, SNMP ifIndex: 7, Generation: 13
            Type: Software-Pseudo, Link-level type: Interface-Specific, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running
            Interface flags: SNMP-Traps
            Link type      : Unspecified
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0

            Physical interface: vtep, Enabled, Physical link is Up
            Interface index: 133, SNMP ifIndex: 518, Generation: 136
            Type: Software-Pseudo, Link-level type: VxLAN-Tunnel-Endpoint, MTU: Unlimited, Clocking: Unspecified, Speed: Unlimited
            Device flags   : Present Running
            Link type      : Full-Duplex
            Link flags     : None
            Physical info  : Unspecified
            Hold-times     : Up 0 ms, Down 0 ms
            Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
            Current address: Unspecified, Hardware address: Unspecified
            Alternate link address: Unspecified
            Last flapped   : Never
            Statistics last cleared: Never
            Traffic statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            IPv6 transit statistics:
            Input  bytes  :                    0
            Output bytes  :                    0
            Input  packets:                    0
            Output packets:                    0
            Input errors:
                Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Giants: 0, Policed discards: 0, Resource errors: 0
            Output errors:
                Carrier transitions: 0, Errors: 0, Drops: 0, MTU errors: 0, Resource errors: 0
    """
    }

    golden_parsed_output_2 = {
        "interface-information": {
            "physical-interface": [
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:ff:56:b6",
                    "description": "none/100G/in/hktGCS002_ge-0/0/0",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-mac-statistics": {
                        "input-broadcasts": "0",
                        "input-bytes": "21604601324",
                        "input-code-violations": "0",
                        "input-crc-errors": "0",
                        "input-fifo-errors": "0",
                        "input-fragment-frames": "0",
                        "input-jabber-frames": "0",
                        "input-mac-control-frames": "0",
                        "input-mac-pause-frames": "0",
                        "input-multicasts": "0",
                        "input-oversized-frames": "0",
                        "input-packets": "133726919",
                        "input-unicasts": "133726908",
                        "input-vlan-tagged-frames": "0",
                        "output-broadcasts": "0",
                        "output-bytes": "16828244544",
                        "output-crc-errors": "0",
                        "output-fifo-errors": "0",
                        "output-mac-control-frames": "0",
                        "output-mac-pause-frames": "0",
                        "output-multicasts": "0",
                        "output-packets": "129183374",
                        "output-unicasts": "129183361"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:ff:56:b6",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "input-error-list": {
                        "framing-errors": "0",
                        "input-discards": "0",
                        "input-drops": "0",
                        "input-errors": "0",
                        "input-fifo-errors": "0",
                        "input-l2-channel-errors": "0",
                        "input-l2-mismatch-timeouts": "0",
                        "input-l3-incompletes": "0",
                        "input-resource-errors": "0",
                        "input-runts": "0"
                    },
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:19 UTC (29w6d 22:19 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "148",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-no-redirects": True,
                                        "ifff-sendbcast-pkt-to-re": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        }
                                    },
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "inet6",
                                    "interface-address": [
                                        {
                                            "ifa-destination": "2001:db8:223c:2c16::/64",
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True,
                                                "ifaf-is-primary": True
                                            },
                                            "ifa-local": "2001:db8:223c:2c16::1"
                                        },
                                        {
                                            "ifa-destination": "fe80::/64",
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True
                                            },
                                            "ifa-local": "fe80::250:56ff:feff:56b6"
                                        }
                                    ],
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "mpls",
                                    "generation": "150",
                                    "maximum-labels": "3",
                                    "mtu": "1488"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "multiservice",
                                    "generation": "163",
                                    "mtu": "Unlimited",
                                    "route-table": "0"
                                }
                            ],
                            "encapsulation": "ENET2",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x4004000"
                            },
                            "local-index": "333",
                            "name": "ge-0/0/0.0",
                            "snmp-index": "606",
                            "traffic-statistics": {
                                "input-bytes": "19732539397",
                                "input-packets": "133726363",
                                "ipv6-transit-statistics": {
                                    "input-bytes": "12676733166",
                                    "input-packets": "63558712",
                                    "output-bytes": "11303933633",
                                    "output-packets": "61684919"
                                },
                                "output-bytes": "15997705213",
                                "output-packets": "129306864"
                            },
                            "transit-traffic-statistics": {
                                "input-bps": "3152",
                                "input-bytes": "7055806231",
                                "input-packets": "70167651",
                                "input-pps": "5",
                                "ipv6-transit-statistics": {
                                    "input-bps": "1856",
                                    "input-bytes": "737203554",
                                    "input-packets": "7541948",
                                    "input-pps": "2",
                                    "output-bps": "0",
                                    "output-bytes": "1018758352",
                                    "output-packets": "6986863",
                                    "output-pps": "0"
                                },
                                "output-bps": "816",
                                "output-bytes": "4693771580",
                                "output-packets": "67621945",
                                "output-pps": "1"
                            }
                        }
                    ],
                    "loopback": "Disabled",
                    "lsi-traffic-statistics": {
                        "input-bps": "0",
                        "input-bytes": "0",
                        "input-packets": "0",
                        "input-pps": "0"
                    },
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/0",
                    "output-error-list": {
                        "aged-packets": "0",
                        "carrier-transitions": "1",
                        "hs-link-crc-errors": "0",
                        "mtu-errors": "0",
                        "output-collisions": "0",
                        "output-drops": "0",
                        "output-errors": "0",
                        "output-fifo-errors": "0",
                        "output-resource-errors": "0"
                    },
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "526",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "stp-traffic-statistics": {
                        "stp-input-bytes-dropped": "0",
                        "stp-input-packets-dropped": "0",
                        "stp-output-bytes-dropped": "0",
                        "stp-output-packets-dropped": "0"
                    },
                    "traffic-statistics": {
                        "input-bps": "3152",
                        "input-bytes": "19732539397",
                        "input-packets": "133726363",
                        "input-pps": "5",
                        "ipv6-transit-statistics": {
                            "input-bytes": "737203554",
                            "input-packets": "7541948",
                            "output-bytes": "1018758352",
                            "output-packets": "6986863"
                        },
                        "output-bps": "3160",
                        "output-bytes": "16367814635",
                        "output-packets": "129306863",
                        "output-pps": "4"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Unspecified",
                    "local-index": "145",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "vpls",
                                    "generation": "155",
                                    "mtu": "Unlimited",
                                    "route-table": "1"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "329",
                            "logical-interface-bandwidth": "0",
                            "name": "lc-0/0/0.32769",
                            "snmp-index": "520",
                            "traffic-statistics": {
                                "input-bytes": "0",
                                "input-packets": "0",
                                "output-bytes": "0",
                                "output-packets": "0"
                            },
                            "transit-traffic-statistics": {
                                "input-bps": "0",
                                "input-bytes": "0",
                                "input-packets": "0",
                                "input-pps": "0",
                                "output-bps": "0",
                                "output-bytes": "0",
                                "output-packets": "0",
                                "output-pps": "0"
                            }
                        }
                    ],
                    "name": "lc-0/0/0",
                    "output-error-list": {},
                    "snmp-index": "519",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Unspecified",
                    "local-index": "147",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet6",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "330",
                            "logical-interface-bandwidth": "0",
                            "name": "pfe-0/0/0.16383",
                            "snmp-index": "523",
                            "traffic-statistics": {
                                "input-bytes": "0",
                                "input-packets": "0",
                                "ipv6-transit-statistics": {
                                    "input-bytes": "0",
                                    "input-packets": "0",
                                    "output-bytes": "0",
                                    "output-packets": "0"
                                },
                                "output-bytes": "0",
                                "output-packets": "0"
                            },
                            "transit-traffic-statistics": {
                                "input-bps": "0",
                                "input-bytes": "0",
                                "input-packets": "0",
                                "input-pps": "0",
                                "ipv6-transit-statistics": {
                                    "input-bps": "0",
                                    "input-bytes": "0",
                                    "input-packets": "0",
                                    "input-pps": "0",
                                    "output-bps": "0",
                                    "output-bytes": "0",
                                    "output-packets": "0",
                                    "output-pps": "0"
                                },
                                "output-bps": "0",
                                "output-bytes": "0",
                                "output-packets": "0",
                                "output-pps": "0"
                            }
                        }
                    ],
                    "name": "pfe-0/0/0",
                    "output-error-list": {},
                    "snmp-index": "522",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Unspecified",
                    "local-index": "146",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "331",
                            "logical-interface-bandwidth": "0",
                            "name": "pfh-0/0/0.16383",
                            "snmp-index": "524",
                            "traffic-statistics": {
                                "input-bytes": "0",
                                "input-packets": "0",
                                "output-bytes": "0",
                                "output-packets": "0"
                            },
                            "transit-traffic-statistics": {
                                "input-bps": "0",
                                "input-bytes": "0",
                                "input-packets": "0",
                                "input-pps": "0",
                                "output-bps": "0",
                                "output-bytes": "0",
                                "output-packets": "0",
                                "output-pps": "0"
                            }
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "inet",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "332",
                            "logical-interface-bandwidth": "0",
                            "name": "pfh-0/0/0.16384",
                            "snmp-index": "525",
                            "traffic-statistics": {
                                "input-bytes": "0",
                                "input-packets": "0",
                                "output-bytes": "0",
                                "output-packets": "0"
                            },
                            "transit-traffic-statistics": {
                                "input-bps": "0",
                                "input-bytes": "0",
                                "input-packets": "0",
                                "input-pps": "0",
                                "output-bps": "0",
                                "output-bytes": "0",
                                "output-packets": "0",
                                "output-pps": "0"
                            }
                        }
                    ],
                    "name": "pfh-0/0/0",
                    "output-error-list": {},
                    "snmp-index": "521",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:ff:37:f9",
                    "description": "YW7079/9.6G/BB/sjkGDS221-EC11_xe-0/1/5[SJC]_Area8_Cost100",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-mac-statistics": {
                        "input-broadcasts": "0",
                        "input-bytes": "40247994921",
                        "input-code-violations": "0",
                        "input-crc-errors": "0",
                        "input-fifo-errors": "0",
                        "input-fragment-frames": "0",
                        "input-jabber-frames": "0",
                        "input-mac-control-frames": "0",
                        "input-mac-pause-frames": "0",
                        "input-multicasts": "0",
                        "input-oversized-frames": "0",
                        "input-packets": "376916517",
                        "input-unicasts": "376916499",
                        "input-vlan-tagged-frames": "0",
                        "output-broadcasts": "0",
                        "output-bytes": "45995779695",
                        "output-crc-errors": "0",
                        "output-fifo-errors": "0",
                        "output-mac-control-frames": "0",
                        "output-mac-pause-frames": "0",
                        "output-multicasts": "0",
                        "output-packets": "370414748",
                        "output-unicasts": "370414722"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:ff:37:f9",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "input-error-list": {
                        "framing-errors": "0",
                        "input-discards": "0",
                        "input-drops": "0",
                        "input-errors": "0",
                        "input-fifo-errors": "0",
                        "input-l2-channel-errors": "0",
                        "input-l2-mismatch-timeouts": "0",
                        "input-l3-incompletes": "0",
                        "input-resource-errors": "0",
                        "input-runts": "0"
                    },
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:19 UTC (29w6d 22:19 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "149",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-no-redirects": True,
                                        "ifff-sendbcast-pkt-to-re": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        }
                                    },
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-name": "inet6",
                                    "interface-address": [
                                        {
                                            "ifa-destination": "2001:db8:eb18:6337::/64",
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True,
                                                "ifaf-is-primary": True
                                            },
                                            "ifa-local": "2001:db8:eb18:6337::2"
                                        },
                                        {
                                            "ifa-destination": "fe80::/64",
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True
                                            },
                                            "ifa-local": "fe80::250:56ff:feff:37f9"
                                        }
                                    ],
                                    "intf-curr-cnt": "2",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-name": "mpls",
                                    "generation": "156",
                                    "maximum-labels": "3",
                                    "mtu": "1488"
                                },
                                {
                                    "address-family-name": "multiservice",
                                    "generation": "166",
                                    "mtu": "Unlimited",
                                    "route-table": "0"
                                }
                            ],
                            "encapsulation": "ENET2",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x4004000"
                            },
                            "local-index": "334",
                            "name": "ge-0/0/1.0",
                            "snmp-index": "605",
                            "traffic-statistics": {
                                "input-bytes": "34950288700",
                                "input-packets": "376916510",
                                "ipv6-transit-statistics": {
                                    "input-bytes": "13617655381",
                                    "input-packets": "85070342",
                                    "output-bytes": "18694395654",
                                    "output-packets": "90794602"
                                },
                                "output-bytes": "42238503795",
                                "output-packets": "370594612"
                            },
                            "transit-traffic-statistics": {
                                "input-bps": "3368",
                                "input-bytes": "21332633319",
                                "input-packets": "291846168",
                                "input-pps": "6",
                                "ipv6-transit-statistics": {
                                    "input-bps": "3360",
                                    "input-bytes": "3303092203",
                                    "input-packets": "41039648",
                                    "input-pps": "5",
                                    "output-bps": "1136",
                                    "output-bytes": "3127179954",
                                    "output-packets": "41594426",
                                    "output-pps": "1"
                                },
                                "output-bps": "2144",
                                "output-bytes": "23544108141",
                                "output-packets": "279800010",
                                "output-pps": "4"
                            }
                        }
                    ],
                    "loopback": "Disabled",
                    "lsi-traffic-statistics": {
                        "input-bps": "0",
                        "input-bytes": "0",
                        "input-packets": "0",
                        "input-pps": "0"
                    },
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/1",
                    "output-error-list": {
                        "aged-packets": "0",
                        "carrier-transitions": "1",
                        "hs-link-crc-errors": "0",
                        "mtu-errors": "0",
                        "output-collisions": "0",
                        "output-drops": "0",
                        "output-errors": "0",
                        "output-fifo-errors": "0",
                        "output-resource-errors": "0"
                    },
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "527",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "stp-traffic-statistics": {
                        "stp-input-bytes-dropped": "0",
                        "stp-input-packets-dropped": "0",
                        "stp-output-bytes-dropped": "0",
                        "stp-output-packets-dropped": "0"
                    },
                    "traffic-statistics": {
                        "input-bps": "5304",
                        "input-bytes": "34950288700",
                        "input-packets": "376916510",
                        "input-pps": "9",
                        "ipv6-transit-statistics": {
                            "input-bytes": "3303092203",
                            "input-packets": "41039648",
                            "output-bytes": "3127179954",
                            "output-packets": "41594426"
                        },
                        "output-bps": "8016",
                        "output-bytes": "42783271407",
                        "output-packets": "370594612",
                        "output-pps": "9"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:ff:1e:ba",
                    "description": "ve-hkgasr01_Gi2[DefaultCost1000]",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-mac-statistics": {
                        "input-broadcasts": "0",
                        "input-bytes": "38187795706",
                        "input-code-violations": "0",
                        "input-crc-errors": "0",
                        "input-fifo-errors": "0",
                        "input-fragment-frames": "0",
                        "input-jabber-frames": "0",
                        "input-mac-control-frames": "0",
                        "input-mac-pause-frames": "0",
                        "input-multicasts": "0",
                        "input-oversized-frames": "0",
                        "input-packets": "252983787",
                        "input-unicasts": "252983783",
                        "input-vlan-tagged-frames": "0",
                        "output-broadcasts": "0",
                        "output-bytes": "30274309615",
                        "output-crc-errors": "0",
                        "output-fifo-errors": "0",
                        "output-mac-control-frames": "0",
                        "output-mac-pause-frames": "0",
                        "output-multicasts": "0",
                        "output-packets": "229070544",
                        "output-unicasts": "229070540"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:ff:1e:ba",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "input-error-list": {
                        "framing-errors": "0",
                        "input-discards": "0",
                        "input-drops": "0",
                        "input-errors": "0",
                        "input-fifo-errors": "0",
                        "input-l2-channel-errors": "0",
                        "input-l2-mismatch-timeouts": "0",
                        "input-l3-incompletes": "0",
                        "input-resource-errors": "0",
                        "input-runts": "0"
                    },
                    "interface-flapped": {
                        "#text": "2020-03-05 16:04:34 UTC (2w6d 15:23 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "150",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-sendbcast-pkt-to-re": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        }
                                    },
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-name": "mpls",
                                    "generation": "180",
                                    "maximum-labels": "3",
                                    "mtu": "1488",
                                    "route-table": "0"
                                },
                                {
                                    "address-family-name": "multiservice",
                                    "generation": "181",
                                    "mtu": "Unlimited",
                                    "route-table": "0"
                                }
                            ],
                            "encapsulation": "ENET2",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x4004000"
                            },
                            "local-index": "336",
                            "name": "ge-0/0/2.0",
                            "snmp-index": "536",
                            "traffic-statistics": {
                                "input-bytes": "11458939228",
                                "input-packets": "31742480",
                                "output-bytes": "13615419042",
                                "output-packets": "28915016"
                            },
                            "transit-traffic-statistics": {
                                "input-bps": "880",
                                "input-bytes": "19772433990",
                                "input-packets": "178635019",
                                "input-pps": "1",
                                "output-bps": "360",
                                "output-bytes": "13648516462",
                                "output-packets": "193694615",
                                "output-pps": "0"
                            }
                        }
                    ],
                    "loopback": "Disabled",
                    "lsi-traffic-statistics": {
                        "input-bps": "0",
                        "input-bytes": "0",
                        "input-packets": "0",
                        "input-pps": "0"
                    },
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/2",
                    "output-error-list": {
                        "aged-packets": "0",
                        "carrier-transitions": "47",
                        "hs-link-crc-errors": "0",
                        "mtu-errors": "0",
                        "output-collisions": "0",
                        "output-drops": "0",
                        "output-errors": "0",
                        "output-fifo-errors": "0",
                        "output-resource-errors": "0"
                    },
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "528",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "stp-traffic-statistics": {
                        "stp-input-bytes-dropped": "0",
                        "stp-input-packets-dropped": "0",
                        "stp-output-bytes-dropped": "0",
                        "stp-output-packets-dropped": "0"
                    },
                    "traffic-statistics": {
                        "input-bps": "880",
                        "input-bytes": "34302334175",
                        "input-packets": "248114960",
                        "input-pps": "1",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bps": "880",
                        "output-bytes": "27932035013",
                        "output-packets": "229304654",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "alarm-not-present": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:ff:93:cb",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-mac-statistics": {
                        "input-broadcasts": "0",
                        "input-bytes": "1157295",
                        "input-code-violations": "0",
                        "input-crc-errors": "0",
                        "input-fifo-errors": "0",
                        "input-fragment-frames": "0",
                        "input-jabber-frames": "0",
                        "input-mac-control-frames": "0",
                        "input-mac-pause-frames": "0",
                        "input-multicasts": "0",
                        "input-oversized-frames": "0",
                        "input-packets": "14683",
                        "input-unicasts": "14683",
                        "input-vlan-tagged-frames": "0",
                        "output-broadcasts": "0",
                        "output-bytes": "3441533",
                        "output-crc-errors": "0",
                        "output-fifo-errors": "0",
                        "output-mac-control-frames": "0",
                        "output-mac-pause-frames": "0",
                        "output-multicasts": "0",
                        "output-packets": "17425",
                        "output-unicasts": "17425"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:ff:93:cb",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "input-error-list": {
                        "framing-errors": "0",
                        "input-discards": "0",
                        "input-drops": "0",
                        "input-errors": "0",
                        "input-fifo-errors": "0",
                        "input-l2-channel-errors": "0",
                        "input-l2-mismatch-timeouts": "0",
                        "input-l3-incompletes": "0",
                        "input-resource-errors": "0",
                        "input-runts": "0"
                    },
                    "interface-flapped": {
                        "#text": "2019-10-25 08:50:18 UTC (21w5d 22:38 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "151",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-sendbcast-pkt-to-re": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        }
                                    },
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-name": "multiservice",
                                    "generation": "175",
                                    "mtu": "Unlimited",
                                    "route-table": "0"
                                }
                            ],
                            "encapsulation": "ENET2",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x4004000"
                            },
                            "local-index": "335",
                            "name": "ge-0/0/3.0",
                            "snmp-index": "537",
                            "traffic-statistics": {
                                "input-bytes": "667980",
                                "input-packets": "11133",
                                "output-bytes": "467670",
                                "output-packets": "11135"
                            },
                            "transit-traffic-statistics": {
                                "input-bps": "0",
                                "input-bytes": "424988",
                                "input-packets": "3486",
                                "input-pps": "0",
                                "output-bps": "0",
                                "output-bytes": "2885485",
                                "output-packets": "6291",
                                "output-pps": "0"
                            }
                        }
                    ],
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/3",
                    "output-error-list": {
                        "aged-packets": "0",
                        "carrier-transitions": "3",
                        "hs-link-crc-errors": "0",
                        "mtu-errors": "0",
                        "output-collisions": "0",
                        "output-drops": "0",
                        "output-errors": "0",
                        "output-fifo-errors": "0",
                        "output-resource-errors": "0"
                    },
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "529",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "stp-traffic-statistics": {
                        "stp-input-bytes-dropped": "0",
                        "stp-input-packets-dropped": "0",
                        "stp-output-bytes-dropped": "0",
                        "stp-output-packets-dropped": "0"
                    },
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-bytes": "1092968",
                        "input-packets": "14619",
                        "input-pps": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bps": "0",
                        "output-bytes": "3419965",
                        "output-packets": "17426",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "00:50:56:ff:3e:28",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-mac-statistics": {
                        "input-broadcasts": "0",
                        "input-bytes": "0",
                        "input-code-violations": "0",
                        "input-crc-errors": "0",
                        "input-fifo-errors": "0",
                        "input-fragment-frames": "0",
                        "input-jabber-frames": "0",
                        "input-mac-control-frames": "0",
                        "input-mac-pause-frames": "0",
                        "input-multicasts": "0",
                        "input-oversized-frames": "0",
                        "input-packets": "0",
                        "input-unicasts": "0",
                        "input-vlan-tagged-frames": "0",
                        "output-broadcasts": "0",
                        "output-bytes": "0",
                        "output-crc-errors": "0",
                        "output-fifo-errors": "0",
                        "output-mac-control-frames": "0",
                        "output-mac-pause-frames": "0",
                        "output-multicasts": "0",
                        "output-packets": "0",
                        "output-unicasts": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "00:50:56:ff:3e:28",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "input-error-list": {
                        "framing-errors": "0",
                        "input-discards": "0",
                        "input-drops": "0",
                        "input-errors": "0",
                        "input-fifo-errors": "0",
                        "input-l2-channel-errors": "0",
                        "input-l2-mismatch-timeouts": "0",
                        "input-l3-incompletes": "0",
                        "input-resource-errors": "0",
                        "input-runts": "0"
                    },
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 22:19 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "152",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/4",
                    "output-error-list": {
                        "aged-packets": "0",
                        "carrier-transitions": "2",
                        "hs-link-crc-errors": "0",
                        "mtu-errors": "0",
                        "output-collisions": "0",
                        "output-drops": "0",
                        "output-errors": "0",
                        "output-fifo-errors": "0",
                        "output-resource-errors": "0"
                    },
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "530",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "stp-traffic-statistics": {
                        "stp-input-bytes-dropped": "0",
                        "stp-input-packets-dropped": "0",
                        "stp-output-bytes-dropped": "0",
                        "stp-output-packets-dropped": "0"
                    },
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-bytes": "0",
                        "input-packets": "0",
                        "input-pps": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bps": "0",
                        "output-bytes": "0",
                        "output-packets": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:ff:01:1d",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-mac-statistics": {
                        "input-broadcasts": "0",
                        "input-bytes": "0",
                        "input-code-violations": "0",
                        "input-crc-errors": "0",
                        "input-fifo-errors": "0",
                        "input-fragment-frames": "0",
                        "input-jabber-frames": "0",
                        "input-mac-control-frames": "0",
                        "input-mac-pause-frames": "0",
                        "input-multicasts": "0",
                        "input-oversized-frames": "0",
                        "input-packets": "0",
                        "input-unicasts": "0",
                        "input-vlan-tagged-frames": "0",
                        "output-broadcasts": "0",
                        "output-bytes": "0",
                        "output-crc-errors": "0",
                        "output-fifo-errors": "0",
                        "output-mac-control-frames": "0",
                        "output-mac-pause-frames": "0",
                        "output-multicasts": "0",
                        "output-packets": "0",
                        "output-unicasts": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:ff:01:1d",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "input-error-list": {
                        "framing-errors": "0",
                        "input-discards": "0",
                        "input-drops": "0",
                        "input-errors": "0",
                        "input-fifo-errors": "0",
                        "input-l2-channel-errors": "0",
                        "input-l2-mismatch-timeouts": "0",
                        "input-l3-incompletes": "0",
                        "input-resource-errors": "0",
                        "input-runts": "0"
                    },
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 22:19 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "153",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/5",
                    "output-error-list": {
                        "aged-packets": "0",
                        "carrier-transitions": "2",
                        "hs-link-crc-errors": "0",
                        "mtu-errors": "0",
                        "output-collisions": "0",
                        "output-drops": "0",
                        "output-errors": "0",
                        "output-fifo-errors": "0",
                        "output-resource-errors": "0"
                    },
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "531",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "stp-traffic-statistics": {
                        "stp-input-bytes-dropped": "0",
                        "stp-input-packets-dropped": "0",
                        "stp-output-bytes-dropped": "0",
                        "stp-output-packets-dropped": "0"
                    },
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-bytes": "0",
                        "input-packets": "0",
                        "input-pps": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bps": "0",
                        "output-bytes": "0",
                        "output-packets": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:ff:01:1e",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-mac-statistics": {
                        "input-broadcasts": "0",
                        "input-bytes": "0",
                        "input-code-violations": "0",
                        "input-crc-errors": "0",
                        "input-fifo-errors": "0",
                        "input-fragment-frames": "0",
                        "input-jabber-frames": "0",
                        "input-mac-control-frames": "0",
                        "input-mac-pause-frames": "0",
                        "input-multicasts": "0",
                        "input-oversized-frames": "0",
                        "input-packets": "0",
                        "input-unicasts": "0",
                        "input-vlan-tagged-frames": "0",
                        "output-broadcasts": "0",
                        "output-bytes": "0",
                        "output-crc-errors": "0",
                        "output-fifo-errors": "0",
                        "output-mac-control-frames": "0",
                        "output-mac-pause-frames": "0",
                        "output-multicasts": "0",
                        "output-packets": "0",
                        "output-unicasts": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:ff:01:1e",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "input-error-list": {
                        "framing-errors": "0",
                        "input-discards": "0",
                        "input-drops": "0",
                        "input-errors": "0",
                        "input-fifo-errors": "0",
                        "input-l2-channel-errors": "0",
                        "input-l2-mismatch-timeouts": "0",
                        "input-l3-incompletes": "0",
                        "input-resource-errors": "0",
                        "input-runts": "0"
                    },
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 22:19 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "154",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/6",
                    "output-error-list": {
                        "aged-packets": "0",
                        "carrier-transitions": "2",
                        "hs-link-crc-errors": "0",
                        "mtu-errors": "0",
                        "output-collisions": "0",
                        "output-drops": "0",
                        "output-errors": "0",
                        "output-fifo-errors": "0",
                        "output-resource-errors": "0"
                    },
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "532",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "stp-traffic-statistics": {
                        "stp-input-bytes-dropped": "0",
                        "stp-input-packets-dropped": "0",
                        "stp-output-bytes-dropped": "0",
                        "stp-output-packets-dropped": "0"
                    },
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-bytes": "0",
                        "input-packets": "0",
                        "input-pps": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bps": "0",
                        "output-bytes": "0",
                        "output-packets": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:ff:01:1f",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-mac-statistics": {
                        "input-broadcasts": "0",
                        "input-bytes": "0",
                        "input-code-violations": "0",
                        "input-crc-errors": "0",
                        "input-fifo-errors": "0",
                        "input-fragment-frames": "0",
                        "input-jabber-frames": "0",
                        "input-mac-control-frames": "0",
                        "input-mac-pause-frames": "0",
                        "input-multicasts": "0",
                        "input-oversized-frames": "0",
                        "input-packets": "0",
                        "input-unicasts": "0",
                        "input-vlan-tagged-frames": "0",
                        "output-broadcasts": "0",
                        "output-bytes": "0",
                        "output-crc-errors": "0",
                        "output-fifo-errors": "0",
                        "output-mac-control-frames": "0",
                        "output-mac-pause-frames": "0",
                        "output-multicasts": "0",
                        "output-packets": "0",
                        "output-unicasts": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:ff:01:1f",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "input-error-list": {
                        "framing-errors": "0",
                        "input-discards": "0",
                        "input-drops": "0",
                        "input-errors": "0",
                        "input-fifo-errors": "0",
                        "input-l2-channel-errors": "0",
                        "input-l2-mismatch-timeouts": "0",
                        "input-l3-incompletes": "0",
                        "input-resource-errors": "0",
                        "input-runts": "0"
                    },
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 22:19 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "155",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/7",
                    "output-error-list": {
                        "aged-packets": "0",
                        "carrier-transitions": "2",
                        "hs-link-crc-errors": "0",
                        "mtu-errors": "0",
                        "output-collisions": "0",
                        "output-drops": "0",
                        "output-errors": "0",
                        "output-fifo-errors": "0",
                        "output-resource-errors": "0"
                    },
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "533",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "stp-traffic-statistics": {
                        "stp-input-bytes-dropped": "0",
                        "stp-input-packets-dropped": "0",
                        "stp-output-bytes-dropped": "0",
                        "stp-output-packets-dropped": "0"
                    },
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-bytes": "0",
                        "input-packets": "0",
                        "input-pps": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bps": "0",
                        "output-bytes": "0",
                        "output-packets": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:ff:01:20",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-mac-statistics": {
                        "input-broadcasts": "0",
                        "input-bytes": "0",
                        "input-code-violations": "0",
                        "input-crc-errors": "0",
                        "input-fifo-errors": "0",
                        "input-fragment-frames": "0",
                        "input-jabber-frames": "0",
                        "input-mac-control-frames": "0",
                        "input-mac-pause-frames": "0",
                        "input-multicasts": "0",
                        "input-oversized-frames": "0",
                        "input-packets": "0",
                        "input-unicasts": "0",
                        "input-vlan-tagged-frames": "0",
                        "output-broadcasts": "0",
                        "output-bytes": "0",
                        "output-crc-errors": "0",
                        "output-fifo-errors": "0",
                        "output-mac-control-frames": "0",
                        "output-mac-pause-frames": "0",
                        "output-multicasts": "0",
                        "output-packets": "0",
                        "output-unicasts": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:ff:01:20",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "input-error-list": {
                        "framing-errors": "0",
                        "input-discards": "0",
                        "input-drops": "0",
                        "input-errors": "0",
                        "input-fifo-errors": "0",
                        "input-l2-channel-errors": "0",
                        "input-l2-mismatch-timeouts": "0",
                        "input-l3-incompletes": "0",
                        "input-resource-errors": "0",
                        "input-runts": "0"
                    },
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 22:19 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "156",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/8",
                    "output-error-list": {
                        "aged-packets": "0",
                        "carrier-transitions": "2",
                        "hs-link-crc-errors": "0",
                        "mtu-errors": "0",
                        "output-collisions": "0",
                        "output-drops": "0",
                        "output-errors": "0",
                        "output-fifo-errors": "0",
                        "output-resource-errors": "0"
                    },
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "534",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "stp-traffic-statistics": {
                        "stp-input-bytes-dropped": "0",
                        "stp-input-packets-dropped": "0",
                        "stp-output-bytes-dropped": "0",
                        "stp-output-packets-dropped": "0"
                    },
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-bytes": "0",
                        "input-packets": "0",
                        "input-pps": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bps": "0",
                        "output-bytes": "0",
                        "output-packets": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "active-alarms": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "active-defects": {
                        "interface-alarms": {
                            "ethernet-alarm-link-down": True
                        }
                    },
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "bpdu-error": "None",
                    "current-physical-address": "2c:6b:f5:ff:01:21",
                    "eth-switch-error": "None",
                    "ethernet-fec-statistics": {
                        "fec_ccw_count": "0",
                        "fec_ccw_error_rate": "0",
                        "fec_nccw_count": "0",
                        "fec_nccw_error_rate": "0"
                    },
                    "ethernet-mac-statistics": {
                        "input-broadcasts": "0",
                        "input-bytes": "0",
                        "input-code-violations": "0",
                        "input-crc-errors": "0",
                        "input-fifo-errors": "0",
                        "input-fragment-frames": "0",
                        "input-jabber-frames": "0",
                        "input-mac-control-frames": "0",
                        "input-mac-pause-frames": "0",
                        "input-multicasts": "0",
                        "input-oversized-frames": "0",
                        "input-packets": "0",
                        "input-unicasts": "0",
                        "input-vlan-tagged-frames": "0",
                        "output-broadcasts": "0",
                        "output-bytes": "0",
                        "output-crc-errors": "0",
                        "output-fifo-errors": "0",
                        "output-mac-control-frames": "0",
                        "output-mac-pause-frames": "0",
                        "output-multicasts": "0",
                        "output-packets": "0",
                        "output-unicasts": "0"
                    },
                    "ethernet-pcs-statistics": {
                        "bit-error-seconds": "0",
                        "errored-blocks-seconds": "0"
                    },
                    "hardware-physical-address": "2c:6b:f5:ff:01:21",
                    "if-auto-negotiation": "Enabled",
                    "if-config-flags": {
                        "iff-hardware-down": True,
                        "iff-snmp-traps": True,
                        "internal-flags": "0x4000"
                    },
                    "if-device-flags": {
                        "ifdf-down": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-flow-control": "Enabled",
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "if-remote-fault": "Online",
                    "input-error-list": {
                        "framing-errors": "0",
                        "input-discards": "0",
                        "input-drops": "0",
                        "input-errors": "0",
                        "input-fifo-errors": "0",
                        "input-l2-channel-errors": "0",
                        "input-l2-mismatch-timeouts": "0",
                        "input-l3-incompletes": "0",
                        "input-resource-errors": "0",
                        "input-runts": "0"
                    },
                    "interface-flapped": {
                        "#text": "2019-08-29 09:09:20 UTC (29w6d 22:19 ago)"
                    },
                    "interface-transmit-statistics": "Disabled",
                    "ld-pdu-error": "None",
                    "link-level-type": "Ethernet",
                    "local-index": "157",
                    "loopback": "Disabled",
                    "mru": "1522",
                    "mtu": "1514",
                    "name": "ge-0/0/9",
                    "output-error-list": {
                        "aged-packets": "0",
                        "carrier-transitions": "2",
                        "hs-link-crc-errors": "0",
                        "mtu-errors": "0",
                        "output-collisions": "0",
                        "output-drops": "0",
                        "output-errors": "0",
                        "output-fifo-errors": "0",
                        "output-resource-errors": "0"
                    },
                    "pad-to-minimum-frame-size": "Disabled",
                    "physical-interface-cos-information": {
                        "physical-interface-cos-hw-max-queues": "8",
                        "physical-interface-cos-use-max-queues": "8"
                    },
                    "snmp-index": "535",
                    "sonet-mode": "LAN-PHY",
                    "source-filtering": "Disabled",
                    "speed": "1000mbps",
                    "stp-traffic-statistics": {
                        "stp-input-bytes-dropped": "0",
                        "stp-input-packets-dropped": "0",
                        "stp-output-bytes-dropped": "0",
                        "stp-output-packets-dropped": "0"
                    },
                    "traffic-statistics": {
                        "input-bps": "0",
                        "input-bytes": "0",
                        "input-packets": "0",
                        "input-pps": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bps": "0",
                        "output-bytes": "0",
                        "output-packets": "0",
                        "output-pps": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-loopback": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Unspecified",
                    "local-index": "0",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": [
                                        {
                                            "ifa-flags": {
                                                "ifaf-is-primary": True
                                            }
                                        },
                                        {
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            }
                                        },
                                        {
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            }
                                        },
                                        {
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            }
                                        },
                                        {
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            }
                                        },
                                        {
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            }
                                        }
                                    ],
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "iso",
                                    "generation": "132",
                                    "mtu": "Unlimited",
                                    "route-table": "0"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet6",
                                    "interface-address": [
                                        {
                                            "ifa-destination": "Unspecified",
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            },
                                            "ifa-local": "2001:db8:eb18:6337::2"
                                        },
                                        {
                                            "ifa-destination": "Unspecified",
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            },
                                            "ifa-local": "2001:db8:223c:ca45::b"
                                        },
                                        {
                                            "ifa-destination": "Unspecified",
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            },
                                            "ifa-local": "2001:db8:223c:2c16::1"
                                        },
                                        {
                                            "ifa-destination": "Unspecified",
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            },
                                            "ifa-local": "fe80::250:560f:fc8d:7c08"
                                        },
                                        {
                                            "ifa-destination": "Unspecified",
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            },
                                            "ifa-local": "fe80::250:56ff:feff:37f9"
                                        },
                                        {
                                            "ifa-destination": "Unspecified",
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            },
                                            "ifa-local": "fe80::250:56ff:feff:56b6"
                                        }
                                    ],
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "mpls",
                                    "generation": "149",
                                    "maximum-labels": "3",
                                    "mtu": "Unlimited"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "85",
                                    "generation": "129",
                                    "mtu": "Unlimited",
                                    "route-table": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "0",
                            "logical-interface-bandwidth": "0",
                            "name": ".local..0",
                            "snmp-index": "0"
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": [
                                        {
                                            "ifa-flags": {
                                                "ifaf-is-primary": True
                                            }
                                        },
                                        {
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            }
                                        },
                                        {
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            }
                                        }
                                    ],
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet6",
                                    "interface-address": [
                                        {
                                            "ifa-destination": "Unspecified",
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            },
                                            "ifa-local": "fe80::250:56ff:feff:e2c1"
                                        },
                                        {
                                            "ifa-destination": "Unspecified",
                                            "ifa-flags": {
                                                "ifaf-none": True
                                            },
                                            "ifa-local": "2001:db8:8d82::a:0:0:4"
                                        }
                                    ],
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "vpls",
                                    "generation": "132",
                                    "mtu": "Unlimited"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "1",
                            "logical-interface-bandwidth": "0",
                            "name": ".local..1",
                            "snmp-index": "0"
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-flags": {
                                            "ifaf-is-primary": True
                                        }
                                    },
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "2",
                            "logical-interface-bandwidth": "0",
                            "name": ".local..2",
                            "snmp-index": "0"
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "323",
                            "logical-interface-bandwidth": "0",
                            "name": ".local..3",
                            "snmp-index": "0"
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-flags": {
                                            "ifaf-is-primary": True
                                        }
                                    },
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "324",
                            "logical-interface-bandwidth": "0",
                            "name": ".local..4",
                            "snmp-index": "0"
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "iso",
                                    "generation": "151",
                                    "mtu": "Unlimited",
                                    "route-table": "5"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet6",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "326",
                            "logical-interface-bandwidth": "0",
                            "name": ".local..5",
                            "snmp-index": "0"
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "mpls",
                                    "generation": "152",
                                    "maximum-labels": "3",
                                    "mtu": "Unlimited",
                                    "route-table": "6"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "327",
                            "logical-interface-bandwidth": "0",
                            "name": ".local..6",
                            "snmp-index": "0"
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "vpls",
                                    "generation": "154",
                                    "mtu": "Unlimited",
                                    "route-table": "7"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "328",
                            "logical-interface-bandwidth": "0",
                            "name": ".local..7",
                            "snmp-index": "0"
                        },
                        {
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "262016",
                            "logical-interface-bandwidth": "0",
                            "name": ".local..36735",
                            "snmp-index": "0"
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-none": True
                                    },
                                    "address-family-name": "inet",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "262017",
                            "logical-interface-bandwidth": "0",
                            "name": ".local..36736",
                            "snmp-index": "0"
                        },
                        {
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "262018",
                            "logical-interface-bandwidth": "0",
                            "name": ".local..36737",
                            "snmp-index": "0"
                        },
                        {
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "262019",
                            "logical-interface-bandwidth": "0",
                            "name": ".local..36738",
                            "snmp-index": "0"
                        }
                    ],
                    "name": ".local.",
                    "output-error-list": {},
                    "snmp-index": "0",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "2c:6b:f5:ff:01:29",
                    "hardware-physical-address": "2c:6b:f5:ff:01:29",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "129",
                    "name": "cbp0",
                    "output-error-list": {},
                    "snmp-index": "501",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "128",
                    "name": "demux0",
                    "output-error-list": {},
                    "snmp-index": "502",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Unspecified",
                    "local-index": "5",
                    "name": "dsc",
                    "output-error-list": {},
                    "snmp-index": "5",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "00:50:56:ff:e2:c1",
                    "hardware-physical-address": "00:50:56:ff:e2:c1",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "2019-08-29 09:03:11 UTC (29w6d 22:25 ago)"
                    },
                    "link-type": "Unspecified",
                    "local-index": "65",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": [
                                        {
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True
                                            }
                                        },
                                        {
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True,
                                                "ifaf-kernel": True,
                                                "ifaf-preferred": True
                                            }
                                        },
                                        {
                                            "ifa-flags": {
                                                "ifaf-is-default": True,
                                                "ifaf-is-primary": True,
                                                "ifaf-primary": True
                                            }
                                        }
                                    ],
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "inet6",
                                    "interface-address": [
                                        {
                                            "ifa-destination": "fe80::/64",
                                            "ifa-flags": {
                                                "ifaf-is-preferred": True
                                            },
                                            "ifa-local": "fe80::250:56ff:feff:e2c1"
                                        },
                                        {
                                            "ifa-destination": "2001:db8:8d82::/64",
                                            "ifa-flags": {
                                                "ifaf-is-default": True,
                                                "ifaf-is-preferred": True,
                                                "ifaf-is-primary": True
                                            },
                                            "ifa-local": "2001:db8:8d82::a:0:0:4"
                                        }
                                    ],
                                    "intf-curr-cnt": "1",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                },
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True,
                                        "ifff-primary": True
                                    },
                                    "address-family-name": "tnp",
                                    "generation": "4",
                                    "interface-address": {
                                        "ifa-flags": {
                                            "ifaf-none": True
                                        }
                                    },
                                    "mtu": "1500"
                                }
                            ],
                            "encapsulation": "ENET2",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x4000000"
                            },
                            "local-index": "3",
                            "name": "em1.0",
                            "snmp-index": "24",
                            "traffic-statistics": {
                                "input-bytes": "102691292552",
                                "input-packets": "725074463",
                                "ipv6-transit-statistics": {
                                    "input-bytes": "102691292552",
                                    "input-packets": "725074463",
                                    "output-bytes": "106913726719",
                                    "output-packets": "794456958"
                                },
                                "output-bytes": "106913726719",
                                "output-packets": "794456958"
                            }
                        }
                    ],
                    "name": "em1",
                    "output-error-list": {},
                    "snmp-index": "23",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "134",
                    "name": "esi",
                    "output-error-list": {},
                    "snmp-index": "503",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "136",
                    "name": "fti0",
                    "output-error-list": {},
                    "snmp-index": "504",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "137",
                    "name": "fti1",
                    "output-error-list": {},
                    "snmp-index": "505",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "138",
                    "name": "fti2",
                    "output-error-list": {},
                    "snmp-index": "506",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "139",
                    "name": "fti3",
                    "output-error-list": {},
                    "snmp-index": "507",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "140",
                    "name": "fti4",
                    "output-error-list": {},
                    "snmp-index": "508",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "141",
                    "name": "fti5",
                    "output-error-list": {},
                    "snmp-index": "509",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "142",
                    "name": "fti6",
                    "output-error-list": {},
                    "snmp-index": "510",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "143",
                    "name": "fti7",
                    "output-error-list": {},
                    "snmp-index": "511",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "00:50:56:ff:0a:95",
                    "hardware-physical-address": "00:50:56:ff:0a:95",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "2019-08-29 09:03:11 UTC (29w6d 22:25 ago)"
                    },
                    "link-type": "Unspecified",
                    "local-index": "64",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True,
                                        "ifff-sendbcast-pkt-to-re": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        }
                                    },
                                    "intf-curr-cnt": "2",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1500",
                                    "new-hold-limit": "75000"
                                }
                            ],
                            "encapsulation": "ENET2",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x4000000"
                            },
                            "local-index": "4",
                            "name": "fxp0.0",
                            "snmp-index": "13",
                            "traffic-statistics": {
                                "input-bytes": "46289683",
                                "input-packets": "620829",
                                "output-bytes": "207724636",
                                "output-packets": "896062"
                            }
                        }
                    ],
                    "name": "fxp0",
                    "output-error-list": {},
                    "snmp-index": "1",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "GRE",
                    "local-index": "10",
                    "mtu": "Unlimited",
                    "name": "gre",
                    "snmp-index": "8",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "IP-over-IP",
                    "local-index": "11",
                    "mtu": "Unlimited",
                    "name": "ipip",
                    "snmp-index": "9",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "2c:6b:f5:ff:08:09",
                    "hardware-physical-address": "2c:6b:f5:ff:08:09",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "132",
                    "name": "irb",
                    "output-error-list": {},
                    "snmp-index": "512",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "2c:6b:f5:ff:08:d8",
                    "hardware-physical-address": "2c:6b:f5:ff:08:d8",
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "144",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-is-primary": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-flags": {
                                            "ifaf-is-default": True,
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True,
                                            "ifaf-primary": True
                                        }
                                    },
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "75000",
                                    "mtu": "1514",
                                    "new-hold-limit": "75000"
                                }
                            ],
                            "encapsulation": "unknown",
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True,
                                "internal-flags": "0x24004000"
                            },
                            "local-index": "325",
                            "logical-interface-bandwidth": "1Gbps",
                            "name": "jsrv.1",
                            "snmp-index": "514",
                            "traffic-statistics": {
                                "input-bytes": "0",
                                "input-packets": "0",
                                "output-bytes": "0",
                                "output-packets": "0"
                            },
                            "transit-traffic-statistics": {
                                "input-bps": "0",
                                "input-bytes": "0",
                                "input-packets": "0",
                                "input-pps": "0",
                                "output-bps": "0",
                                "output-bytes": "0",
                                "output-packets": "0",
                                "output-pps": "0"
                            }
                        }
                    ],
                    "name": "jsrv",
                    "output-error-list": {},
                    "snmp-index": "513",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-loopback": True,
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Unspecified",
                    "local-index": "6",
                    "logical-interface": [
                        {
                            "address-family": [
                                {
                                    "address-family-flags": {
                                        "ifff-no-redirects": True,
                                        "ifff-sendbcast-pkt-to-re": True
                                    },
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-flags": {
                                            "ifaf-is-default": True,
                                            "ifaf-is-primary": True
                                        }
                                    },
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                },
                                {
                                    "address-family-name": "inet6",
                                    "interface-address": {
                                        "ifa-destination": "Unspecified",
                                        "ifa-flags": {
                                            "ifaf-is-default": True,
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "fe80::250:560f:fc8d:7c08"
                                    },
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "320",
                            "name": "lo0.0",
                            "snmp-index": "16",
                            "traffic-statistics": {
                                "input-bytes": "12188",
                                "input-packets": "83",
                                "ipv6-transit-statistics": {
                                    "input-bytes": "12188",
                                    "input-packets": "83",
                                    "output-bytes": "12188",
                                    "output-packets": "83"
                                },
                                "output-bytes": "12188",
                                "output-packets": "83"
                            },
                            "transit-traffic-statistics": {
                                "input-bps": "0",
                                "input-bytes": "0",
                                "input-packets": "0",
                                "input-pps": "0",
                                "ipv6-transit-statistics": {
                                    "input-bps": "0",
                                    "input-bytes": "0",
                                    "input-packets": "0",
                                    "input-pps": "0",
                                    "output-bps": "0",
                                    "output-bytes": "0",
                                    "output-packets": "0",
                                    "output-pps": "0"
                                },
                                "output-bps": "0",
                                "output-bytes": "0",
                                "output-packets": "0",
                                "output-pps": "0"
                            }
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-name": "inet",
                                    "interface-address": {
                                        "ifa-flags": {
                                            "ifaf-none": True
                                        }
                                    },
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "322",
                            "name": "lo0.16384",
                            "snmp-index": "21",
                            "traffic-statistics": {
                                "input-bytes": "0",
                                "input-packets": "0",
                                "output-bytes": "0",
                                "output-packets": "0"
                            },
                            "transit-traffic-statistics": {
                                "input-bps": "0",
                                "input-bytes": "0",
                                "input-packets": "0",
                                "input-pps": "0",
                                "output-bps": "0",
                                "output-bytes": "0",
                                "output-packets": "0",
                                "output-pps": "0"
                            }
                        },
                        {
                            "address-family": [
                                {
                                    "address-family-name": "inet",
                                    "intf-curr-cnt": "0",
                                    "intf-dropcnt": "0",
                                    "intf-unresolved-cnt": "0",
                                    "max-local-cache": "0",
                                    "mtu": "Unlimited",
                                    "new-hold-limit": "0"
                                }
                            ],
                            "if-config-flags": {
                                "iff-snmp-traps": True,
                                "iff-up": True
                            },
                            "local-index": "321",
                            "name": "lo0.16385",
                            "snmp-index": "22",
                            "traffic-statistics": {
                                "input-bytes": "38208797939",
                                "input-packets": "33943317",
                                "output-bytes": "38208797939",
                                "output-packets": "33943317"
                            },
                            "transit-traffic-statistics": {
                                "input-bps": "0",
                                "input-bytes": "0",
                                "input-packets": "0",
                                "input-pps": "0",
                                "output-bps": "0",
                                "output-bytes": "0",
                                "output-packets": "0",
                                "output-pps": "0"
                            }
                        }
                    ],
                    "name": "lo0",
                    "output-error-list": {},
                    "snmp-index": "6",
                    "traffic-statistics": {
                        "input-bytes": "38208810127",
                        "input-packets": "33943400",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "38208810127",
                        "output-packets": "33943400"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Unspecified",
                    "local-index": "4",
                    "name": "lsi",
                    "output-error-list": {},
                    "snmp-index": "4",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "GRE",
                    "local-index": "66",
                    "mtu": "Unlimited",
                    "name": "mtun",
                    "snmp-index": "12",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "PIM-Decapsulator",
                    "local-index": "26",
                    "mtu": "Unlimited",
                    "name": "pimd",
                    "snmp-index": "11",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "link-level-type": "PIM-Encapsulator",
                    "local-index": "25",
                    "mtu": "Unlimited",
                    "name": "pime",
                    "snmp-index": "10",
                    "speed": "Unlimited",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "2c:6b:f5:ff:08:c8",
                    "hardware-physical-address": "2c:6b:f5:ff:08:c8",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "130",
                    "name": "pip0",
                    "output-error-list": {},
                    "snmp-index": "515",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "link-level-type": "PPPoE",
                    "link-type": "Full-Duplex",
                    "local-index": "131",
                    "mtu": "1532",
                    "name": "pp0",
                    "snmp-index": "516",
                    "speed": "Unspecified"
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "135",
                    "name": "rbeb",
                    "output-error-list": {},
                    "snmp-index": "517",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-config-flags": {
                        "iff-snmp-traps": True
                    },
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Unspecified",
                    "local-index": "12",
                    "name": "tap",
                    "output-error-list": {},
                    "snmp-index": "7",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                },
                {
                    "admin-status": {
                        "@junos:format": "Enabled"
                    },
                    "current-physical-address": "Unspecified",
                    "hardware-physical-address": "Unspecified",
                    "if-device-flags": {
                        "ifdf-present": True,
                        "ifdf-running": True
                    },
                    "if-media-flags": {
                        "ifmf-none": True
                    },
                    "input-error-list": {},
                    "interface-flapped": {
                        "#text": "Never"
                    },
                    "link-type": "Full-Duplex",
                    "local-index": "133",
                    "name": "vtep",
                    "output-error-list": {},
                    "snmp-index": "518",
                    "traffic-statistics": {
                        "input-bytes": "0",
                        "input-packets": "0",
                        "ipv6-transit-statistics": {
                            "input-bytes": "0",
                            "input-packets": "0",
                            "output-bytes": "0",
                            "output-packets": "0"
                        },
                        "output-bytes": "0",
                        "output-packets": "0"
                    }
                }
            ]
        }
    }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfaces(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfaces(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        interface_obj = ShowInterfaces(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


# =======================================================
# Unit test for 'show interfaces queue {interface}'
# =======================================================
class TestShowInterfacesQueue(unittest.TestCase):
    device = Device(name="aDevice")
    maxDiff = None
    empty_output = {"execute.return_value": ""}

    # show interfaces queue ge-0/0/2
    golden_output = {
        "execute.return_value": """
        Physical interface: ge-0/0/2, Enabled, Physical link is Up
          Interface index: 143, SNMP ifIndex: 601
          Description: to_ixia_2/4
        Forwarding classes: 16 supported, 5 in use
        Egress queues: 8 supported, 5 in use
        Queue: 0, Forwarding classes: Bronze-FC
          Queued:
            Packets              :            1470816406                     0 pps
            Bytes                :          564883280956                     0 bps
          Transmitted:
            Packets              :            1470816406                      0 pps
            Bytes                :          564883280956                     0 bps
            Tail-dropped packets :                     0                     0 pps
            RED-dropped packets  :                     0                     0 pps
             Low                 :                     0                     0 pps
             Medium-low          :                     0                     0 pps
             Medium-high         :                     0                     0 pps
             High                :                     0                     0 pps
            RED-dropped bytes    :                     0                     0 bps
             Low                 :                     0                     0 bps
             Medium-low          :                     0                     0 bps
             Medium-high         :                     0                     0 bps
             High                :                     0                     0 bps
        Queue: 1, Forwarding classes: Platinum-FC
          Queued:
            Packets              :                     0                     0 pps
            Bytes                :                     0                     0 bps
          Transmitted:
            Packets              :                     0                      0 pps
            Bytes                :                     0                     0 bps
            Tail-dropped packets :                     0                     0 pps
            RED-dropped packets  :                     0                     0 pps
             Low                 :                     0                     0 pps
             Medium-low          :                     0                     0 pps
             Medium-high         :                     0                     0 pps
             High                :                     0                     0 pps
            RED-dropped bytes    :                     0                     0 bps
             Low                 :                     0                     0 bps
             Medium-low          :                     0                     0 bps
             Medium-high         :                     0                     0 bps
             High                :                     0                     0 bps
        Queue: 2, Forwarding classes: Gold-FC
          Queued:
            Packets              :                     0                     0 pps
            Bytes                :                     0                     0 bps
          Transmitted:
            Packets              :                     0                      0 pps
            Bytes                :                     0                     0 bps
            Tail-dropped packets :                     0                     0 pps
            RED-dropped packets  :                     0                     0 pps
             Low                 :                     0                     0 pps
             Medium-low          :                     0                     0 pps
             Medium-high         :                     0                     0 pps
             High                :                     0                     0 pps
            RED-dropped bytes    :                     0                     0 bps
             Low                 :                     0                     0 bps
             Medium-low          :                     0                     0 bps
             Medium-high         :                     0                     0 bps
             High                :                     0                     0 bps
        Queue: 3, Forwarding classes: Network-Control-FC
          Queued:
            Packets              :                     0                     0 pps
            Bytes                :                     0                     0 bps
          Transmitted:
            Packets              :                     0                      0 pps
            Bytes                :                     0                     0 bps
            Tail-dropped packets :                     0                     0 pps
            RED-dropped packets  :                     0                     0 pps
             Low                 :                     0                     0 pps
             Medium-low          :                     0                     0 pps
             Medium-high         :                     0                     0 pps
             High                :                     0                     0 pps
            RED-dropped bytes    :                     0                     0 bps
             Low                 :                     0                     0 bps
             Medium-low          :                     0                     0 bps
             Medium-high         :                     0                     0 bps
             High                :                     0                     0 bps
        Queue: 4, Forwarding classes: Silver-FC
          Queued:
            Packets              :                     0                     0 pps
            Bytes                :                     0                     0 bps
          Transmitted:
            Packets              :                     0                      0 pps
            Bytes                :                     0                     0 bps
            Tail-dropped packets :                     0                     0 pps
            RED-dropped packets  :                     0                     0 pps
             Low                 :                     0                     0 pps
             Medium-low          :                     0                     0 pps
             Medium-high         :                     0                     0 pps
             High                :                     0                     0 pps
            RED-dropped bytes    :                     0                     0 bps
             Low                 :                     0                     0 bps
             Medium-low          :                     0                     0 bps
             Medium-high         :                     0                     0 bps
             High                :                     0                     0 bps

    """
    }

    golden_parsed_output = {
        "interface-information": {
            "physical-interface": {
                "description": "to_ixia_2/4",
                "local-index": "143",
                "name": "ge-0/0/2",
                "oper-status": "Up",
                "queue-counters": {
                    "interface-cos-summary": {
                        "intf-cos-forwarding-classes-in-use": "5",
                        "intf-cos-forwarding-classes-supported": "16",
                        "intf-cos-num-queues-in-use": "5",
                        "intf-cos-num-queues-supported": "8",
                        "intf-cos-queue-type": "Egress " "queues",
                    },
                    "queue": [
                        {
                            "forwarding-class-name": "Bronze-FC",
                            "queue-counters-queued-bytes": "564883280956",
                            "queue-counters-queued-bytes-rate": "0",
                            "queue-counters-queued-packets": "1470816406",
                            "queue-counters-queued-packets-rate": "0",
                            "queue-counters-red-bytes": "0",
                            "queue-counters-red-bytes-high": "0",
                            "queue-counters-red-bytes-low": "0",
                            "queue-counters-red-bytes-medium-high": "0",
                            "queue-counters-red-bytes-medium-low": "0",
                            "queue-counters-red-bytes-rate": "0",
                            "queue-counters-red-bytes-rate-high": "0",
                            "queue-counters-red-bytes-rate-low": "0",
                            "queue-counters-red-bytes-rate-medium-high": "0",
                            "queue-counters-red-bytes-rate-medium-low": "0",
                            "queue-counters-red-packets": "0",
                            "queue-counters-red-packets-high": "0",
                            "queue-counters-red-packets-low": "0",
                            "queue-counters-red-packets-medium-high": "0",
                            "queue-counters-red-packets-medium-low": "0",
                            "queue-counters-red-packets-rate": "0",
                            "queue-counters-red-packets-rate-high": "0",
                            "queue-counters-red-packets-rate-low": "0",
                            "queue-counters-red-packets-rate-medium-high": "0",
                            "queue-counters-red-packets-rate-medium-low": "0",
                            "queue-counters-tail-drop-packets": "0",
                            "queue-counters-tail-drop-packets-rate": "0",
                            "queue-counters-trans-bytes": "564883280956",
                            "queue-counters-trans-bytes-rate": "0",
                            "queue-counters-trans-packets": "1470816406",
                            "queue-counters-trans-packets-rate": "0",
                            "queue-number": "0",
                        },
                        {
                            "forwarding-class-name": "Platinum-FC",
                            "queue-counters-queued-bytes": "0",
                            "queue-counters-queued-bytes-rate": "0",
                            "queue-counters-queued-packets": "0",
                            "queue-counters-queued-packets-rate": "0",
                            "queue-counters-red-bytes": "0",
                            "queue-counters-red-bytes-high": "0",
                            "queue-counters-red-bytes-low": "0",
                            "queue-counters-red-bytes-medium-high": "0",
                            "queue-counters-red-bytes-medium-low": "0",
                            "queue-counters-red-bytes-rate": "0",
                            "queue-counters-red-bytes-rate-high": "0",
                            "queue-counters-red-bytes-rate-low": "0",
                            "queue-counters-red-bytes-rate-medium-high": "0",
                            "queue-counters-red-bytes-rate-medium-low": "0",
                            "queue-counters-red-packets": "0",
                            "queue-counters-red-packets-high": "0",
                            "queue-counters-red-packets-low": "0",
                            "queue-counters-red-packets-medium-high": "0",
                            "queue-counters-red-packets-medium-low": "0",
                            "queue-counters-red-packets-rate": "0",
                            "queue-counters-red-packets-rate-high": "0",
                            "queue-counters-red-packets-rate-low": "0",
                            "queue-counters-red-packets-rate-medium-high": "0",
                            "queue-counters-red-packets-rate-medium-low": "0",
                            "queue-counters-tail-drop-packets": "0",
                            "queue-counters-tail-drop-packets-rate": "0",
                            "queue-counters-trans-bytes": "0",
                            "queue-counters-trans-bytes-rate": "0",
                            "queue-counters-trans-packets": "0",
                            "queue-counters-trans-packets-rate": "0",
                            "queue-number": "1",
                        },
                        {
                            "forwarding-class-name": "Gold-FC",
                            "queue-counters-queued-bytes": "0",
                            "queue-counters-queued-bytes-rate": "0",
                            "queue-counters-queued-packets": "0",
                            "queue-counters-queued-packets-rate": "0",
                            "queue-counters-red-bytes": "0",
                            "queue-counters-red-bytes-high": "0",
                            "queue-counters-red-bytes-low": "0",
                            "queue-counters-red-bytes-medium-high": "0",
                            "queue-counters-red-bytes-medium-low": "0",
                            "queue-counters-red-bytes-rate": "0",
                            "queue-counters-red-bytes-rate-high": "0",
                            "queue-counters-red-bytes-rate-low": "0",
                            "queue-counters-red-bytes-rate-medium-high": "0",
                            "queue-counters-red-bytes-rate-medium-low": "0",
                            "queue-counters-red-packets": "0",
                            "queue-counters-red-packets-high": "0",
                            "queue-counters-red-packets-low": "0",
                            "queue-counters-red-packets-medium-high": "0",
                            "queue-counters-red-packets-medium-low": "0",
                            "queue-counters-red-packets-rate": "0",
                            "queue-counters-red-packets-rate-high": "0",
                            "queue-counters-red-packets-rate-low": "0",
                            "queue-counters-red-packets-rate-medium-high": "0",
                            "queue-counters-red-packets-rate-medium-low": "0",
                            "queue-counters-tail-drop-packets": "0",
                            "queue-counters-tail-drop-packets-rate": "0",
                            "queue-counters-trans-bytes": "0",
                            "queue-counters-trans-bytes-rate": "0",
                            "queue-counters-trans-packets": "0",
                            "queue-counters-trans-packets-rate": "0",
                            "queue-number": "2",
                        },
                        {
                            "forwarding-class-name": "Network-Control-FC",
                            "queue-counters-queued-bytes": "0",
                            "queue-counters-queued-bytes-rate": "0",
                            "queue-counters-queued-packets": "0",
                            "queue-counters-queued-packets-rate": "0",
                            "queue-counters-red-bytes": "0",
                            "queue-counters-red-bytes-high": "0",
                            "queue-counters-red-bytes-low": "0",
                            "queue-counters-red-bytes-medium-high": "0",
                            "queue-counters-red-bytes-medium-low": "0",
                            "queue-counters-red-bytes-rate": "0",
                            "queue-counters-red-bytes-rate-high": "0",
                            "queue-counters-red-bytes-rate-low": "0",
                            "queue-counters-red-bytes-rate-medium-high": "0",
                            "queue-counters-red-bytes-rate-medium-low": "0",
                            "queue-counters-red-packets": "0",
                            "queue-counters-red-packets-high": "0",
                            "queue-counters-red-packets-low": "0",
                            "queue-counters-red-packets-medium-high": "0",
                            "queue-counters-red-packets-medium-low": "0",
                            "queue-counters-red-packets-rate": "0",
                            "queue-counters-red-packets-rate-high": "0",
                            "queue-counters-red-packets-rate-low": "0",
                            "queue-counters-red-packets-rate-medium-high": "0",
                            "queue-counters-red-packets-rate-medium-low": "0",
                            "queue-counters-tail-drop-packets": "0",
                            "queue-counters-tail-drop-packets-rate": "0",
                            "queue-counters-trans-bytes": "0",
                            "queue-counters-trans-bytes-rate": "0",
                            "queue-counters-trans-packets": "0",
                            "queue-counters-trans-packets-rate": "0",
                            "queue-number": "3",
                        },
                        {
                            "forwarding-class-name": "Silver-FC",
                            "queue-counters-queued-bytes": "0",
                            "queue-counters-queued-bytes-rate": "0",
                            "queue-counters-queued-packets": "0",
                            "queue-counters-queued-packets-rate": "0",
                            "queue-counters-red-bytes": "0",
                            "queue-counters-red-bytes-high": "0",
                            "queue-counters-red-bytes-low": "0",
                            "queue-counters-red-bytes-medium-high": "0",
                            "queue-counters-red-bytes-medium-low": "0",
                            "queue-counters-red-bytes-rate": "0",
                            "queue-counters-red-bytes-rate-high": "0",
                            "queue-counters-red-bytes-rate-low": "0",
                            "queue-counters-red-bytes-rate-medium-high": "0",
                            "queue-counters-red-bytes-rate-medium-low": "0",
                            "queue-counters-red-packets": "0",
                            "queue-counters-red-packets-high": "0",
                            "queue-counters-red-packets-low": "0",
                            "queue-counters-red-packets-medium-high": "0",
                            "queue-counters-red-packets-medium-low": "0",
                            "queue-counters-red-packets-rate": "0",
                            "queue-counters-red-packets-rate-high": "0",
                            "queue-counters-red-packets-rate-low": "0",
                            "queue-counters-red-packets-rate-medium-high": "0",
                            "queue-counters-red-packets-rate-medium-low": "0",
                            "queue-counters-tail-drop-packets": "0",
                            "queue-counters-tail-drop-packets-rate": "0",
                            "queue-counters-trans-bytes": "0",
                            "queue-counters-trans-bytes-rate": "0",
                            "queue-counters-trans-packets": "0",
                            "queue-counters-trans-packets-rate": "0",
                            "queue-number": "4",
                        },
                    ],
                },
                "snmp-index": "601",
            }
        }
    }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfacesQueue(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfacesQueue(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

#############################################################################
# unitest For show interfaces policers interface
#############################################################################


class test_show_interfaces_policers_interface(unittest.TestCase):
    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    maxDiff = None

    golden_parsed_output = {
        "interface-policer-information": {
        "physical-interface": [
            {
                "admin-status": "up",
                "logical-interface": [
                    {
                        "admin-status": "up",
                        "name": "ge-0/0/2.0",
                        "oper-status": "up",
                        "policer-information": [
                            {
                                "policer-family": "inet",
                                "policer-input": "GE_1M-ge-0/0/2.0-log_int-i",
                                "policer-output": "GE_1M-ge-0/0/2.0-log_int-o"
                            },
                            {
                                "policer-family": "inet6",
                                "policer-input": "GE_1M-ge-0/0/2.0-log_int-i",
                                "policer-output": "GE_1M-ge-0/0/2.0-log_int-o"
                            },
                            {
                                "policer-family": "multiservice",
                                "policer-input": "__default_arp_policer__"
                            }
                        ]
                    }
                ],
                "name": "ge-0/0/2",
                "oper-status": "up"
            }
        ]
    }

    }

    golden_output = {
        "execute.return_value": """
        Interface       Admin Link Proto Input Policer         Output Policer
        ge-0/0/2        up    up
        ge-0/0/2.0      up    up
                                inet  GE_1M-ge-0/0/2.0-log_int-i GE_1M-ge-0/0/2.0-log_int-o
                                inet6 GE_1M-ge-0/0/2.0-log_int-i GE_1M-ge-0/0/2.0-log_int-o
                                multiservice __default_arp_policer__
    """
    }



    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfacesPolicersInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            interface_obj.parse(interface='ge-0/0/2')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfacesPolicersInterface(device=self.device)
        parsed_output = interface_obj.parse(interface='ge-0/0/2')
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowInterfacesStatistics(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': """
        show interfaces statistics
        Physical interface: ge-0/0/0, Enabled, Physical link is Up
        Interface index: 133, SNMP ifIndex: 506
        Link-level type: Ethernet, MTU: 1514, Link-mode: Full-duplex, Speed: 1000mbps,
        BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled,
        Remote fault: Online
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: 5e:00:40:ff:00:00, Hardware address: 5e:00:40:ff:00:00
        Last flapped   : 2020-06-22 22:33:51 EST (1w1d 00:22 ago)
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 712 bps (1 pps)
        Output rate    : 0 bps (0 pps)
        Input errors: 1568, Output errors: 0
        Active alarms  : None
        Active defects : None
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/0.0 (Index 70) (SNMP ifIndex 507)
            Flags: SNMP-Traps 0x4000 Encapsulation: ENET2
            Input packets : 4685
            Output packets: 144
            Security: Zone: trust
            Allowed host-inbound traffic : dhcp http https ssh telnet
            Protocol inet, MTU: 1500
            Flags: Sendbcast-pkt-to-re, Is-Primary
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 172.16.1/24, Local: 172.16.1.55, Broadcast: 172.16.1.255

        Physical interface: gr-0/0/0, Enabled, Physical link is Up
        Interface index: 143, SNMP ifIndex: 519
        Type: GRE, Link-level type: GRE, MTU: Unlimited, Speed: 800mbps
        Link flags     : Scheduler Keepalives DTE
        Device flags   : Present Running
        Interface flags: Point-To-Point
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)

        Physical interface: ip-0/0/0, Enabled, Physical link is Up
        Interface index: 144, SNMP ifIndex: 520
        Type: IPIP, Link-level type: IP-over-IP, MTU: Unlimited, Speed: 800mbps
        Link flags     : Scheduler Keepalives DTE
        Device flags   : Present Running
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)

        Physical interface: lsq-0/0/0, Enabled, Physical link is Up
        Interface index: 145, SNMP ifIndex: 521
        Link-level type: LinkService, MTU: 1504
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps Internal: 0x4000
        Last flapped   : 2020-06-22 22:33:52 EST (1w1d 00:22 ago)
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)

        Physical interface: lt-0/0/0, Enabled, Physical link is Up
        Interface index: 147, SNMP ifIndex: 523
        Type: Logical-tunnel, Link-level type: Logical-tunnel, MTU: Unlimited,
        Speed: 800mbps
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps
        Link flags     : None
        Physical info  : 13
        Current address: 02:96:14:ff:11:43, Hardware address: 02:96:14:ff:11:43
        Last flapped   : Never
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Input errors: 0, Output errors: 0

        Physical interface: mt-0/0/0, Enabled, Physical link is Up
        Interface index: 146, SNMP ifIndex: 522
        Type: Multicast-GRE, Link-level type: GRE, MTU: Unlimited, Speed: 800mbps
        Link flags     : Keepalives DTE
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)

        Physical interface: sp-0/0/0, Enabled, Physical link is Up
        Interface index: 142, SNMP ifIndex: 517
        Type: Adaptive-Services, Link-level type: Adaptive-Services, MTU: 9192,
        Speed: 800mbps
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps Internal: 0x4000
        Link type      : Full-Duplex
        Link flags     : None
        Last flapped   : 2020-06-22 22:33:52 EST (1w1d 00:22 ago)
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Input errors: 0, Output errors: 0

        Logical interface sp-0/0/0.0 (Index 75) (SNMP ifIndex 518)
            Flags: Point-To-Point SNMP-Traps Encapsulation: Adaptive-Services
            Input packets : 0
            Output packets: 0
            Security: Zone: Null
            Protocol inet, MTU: 9192
            Flags: Receive-options, Receive-TTL-Exceeded
            Protocol inet6, MTU: 9192
            Flags: Primary, Is-Primary, Receive-options, Receive-TTL-Exceeded

        Logical interface sp-0/0/0.16383 (Index 76) (SNMP ifIndex 524)
            Flags: Point-To-Point SNMP-Traps Encapsulation: Adaptive-Services
            Input packets : 0
            Output packets: 0
            Security: Zone: Null
            Protocol inet, MTU: 9192
            Flags: Is-Primary, Receive-options, Receive-TTL-Exceeded
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 10.0.0.16, Local: 10.0.0.1
            Addresses
                Local: 10.0.0.6
            Addresses, Flags: Is-Preferred
                Destination: 172.16.66.16, Local: 172.16.64.1
            Addresses
                Local: 172.16.64.6

        Physical interface: ge-0/0/1, Enabled, Physical link is Up
        Interface index: 134, SNMP ifIndex: 508
        Link-level type: Ethernet, MTU: 1514, Link-mode: Full-duplex, Speed: 1000mbps,
        BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled,
        Remote fault: Online
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: fa:16:3e:ff:7f:fd, Hardware address: fa:16:3e:ff:7f:fd
        Last flapped   : 2020-06-22 22:34:01 EST (1w1d 00:22 ago)
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 312 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Input errors: 8, Output errors: 0
        Active alarms  : None
        Active defects : None
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/1.0 (Index 71) (SNMP ifIndex 516)
            Flags: SNMP-Traps 0x4000 Encapsulation: ENET2
            Input packets : 555
            Output packets: 546
            Security: Zone: trust
            Allowed host-inbound traffic : bfd bgp dvmrp igmp ldp msdp nhrp ospf ospf3
            pgm pim rip ripng router-discovery rsvp sap vrrp ping
            Protocol inet, MTU: 1500
            Flags: Sendbcast-pkt-to-re
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 40.0.0/24, Local: 10.70.0.4, Broadcast: 10.70.0.255
            Protocol inet6, MTU: 1500
            Flags: None
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 2001:40::/64, Local: 2001:40::4
            Addresses, Flags: Is-Preferred
                Destination: fe80::/64, Local: fe80::fa16:3eff:feff:7ffd

        Physical interface: ge-0/0/2, Enabled, Physical link is Up
        Interface index: 135, SNMP ifIndex: 509
        Link-level type: Ethernet, MTU: 1514, Link-mode: Full-duplex, Speed: 1000mbps,
        BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled,
        Remote fault: Online
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: fa:16:3e:ff:0e:52, Hardware address: fa:16:3e:ff:0e:52
        Last flapped   : 2020-06-22 22:34:01 EST (1w1d 00:22 ago)
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 528 bps (0 pps)
        Input errors: 2, Output errors: 0
        Active alarms  : None
        Active defects : None
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/2.0 (Index 72) (SNMP ifIndex 525)
            Flags: SNMP-Traps 0x4000 Encapsulation: ENET2
            Input packets : 450
            Output packets: 465
            Security: Zone: trust
            Allowed host-inbound traffic : bfd bgp dvmrp igmp ldp msdp nhrp ospf ospf3
            pgm pim rip ripng router-discovery rsvp sap vrrp ping
            Protocol inet, MTU: 1500
            Flags: Sendbcast-pkt-to-re
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 50.0.0/24, Local: 10.205.0.4, Broadcast: 10.205.0.255
            Protocol inet6, MTU: 1500
            Flags: None
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 2001:50::/64, Local: 2001:50::4
            Addresses, Flags: Is-Preferred
                Destination: fe80::/64, Local: fe80::fa16:3eff:feff:e52

        Physical interface: ge-0/0/3, Enabled, Physical link is Up
        Interface index: 136, SNMP ifIndex: 510
        Link-level type: Ethernet, MTU: 1514, Link-mode: Full-duplex, Speed: 1000mbps,
        BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled,
        Remote fault: Online
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: fa:16:3e:ff:12:8e, Hardware address: fa:16:3e:ff:12:8e
        Last flapped   : 2020-06-22 22:34:01 EST (1w1d 00:22 ago)
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Input errors: 0, Output errors: 0
        Active alarms  : None
        Active defects : None
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/3.0 (Index 73) (SNMP ifIndex 526)
            Flags: SNMP-Traps 0x4000 Encapsulation: ENET2
            Input packets : 0
            Output packets: 0
            Security: Zone: trust
            Allowed host-inbound traffic : bfd bgp dvmrp igmp ldp msdp nhrp ospf ospf3
            pgm pim rip ripng router-discovery rsvp sap vrrp ping
            Protocol inet, MTU: 1500
            Flags: Sendbcast-pkt-to-re
            Protocol inet6, MTU: 1500
            Flags: None
            Addresses, Flags: Is-Preferred
                Destination: fe80::/64, Local: fe80::fa16:3eff:feff:128e

        Physical interface: ge-0/0/4, Enabled, Physical link is Up
        Interface index: 137, SNMP ifIndex: 511
        Link-level type: Ethernet, MTU: 1514, Link-mode: Full-duplex, Speed: 1000mbps,
        BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled,
        Remote fault: Online
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: fa:16:3e:ff:37:bd, Hardware address: fa:16:3e:ff:37:bd
        Last flapped   : 2020-06-22 22:34:02 EST (1w1d 00:22 ago)
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Input errors: 0, Output errors: 0
        Active alarms  : None
        Active defects : None
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/4.0 (Index 74) (SNMP ifIndex 527)
            Flags: SNMP-Traps 0x4000 Encapsulation: ENET2
            Input packets : 0
            Output packets: 0
            Security: Zone: trust
            Allowed host-inbound traffic : bfd bgp dvmrp igmp ldp msdp nhrp ospf ospf3
            pgm pim rip ripng router-discovery rsvp sap vrrp ping
            Protocol inet, MTU: 1500
            Flags: Sendbcast-pkt-to-re
            Protocol inet6, MTU: 1500
            Flags: None
            Addresses, Flags: Is-Preferred
                Destination: fe80::/64, Local: fe80::fa16:3eff:feff:37bd

        Physical interface: ge-0/0/5, Enabled, Physical link is Up
        Interface index: 138, SNMP ifIndex: 512
        Link-level type: Ethernet, MTU: 1514, Link-mode: Full-duplex, Speed: 1000mbps,
        BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled,
        Remote fault: Online
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: fa:16:3e:ff:38:28, Hardware address: fa:16:3e:ff:38:28
        Last flapped   : 2020-06-22 22:34:02 EST (1w1d 00:22 ago)
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Input errors: 0, Output errors: 0
        Active alarms  : None
        Active defects : None
        Interface transmit statistics: Disabled

        Physical interface: ge-0/0/6, Enabled, Physical link is Up
        Interface index: 139, SNMP ifIndex: 513
        Link-level type: Ethernet, MTU: 1514, Link-mode: Full-duplex, Speed: 1000mbps,
        BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled,
        Remote fault: Online
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: fa:16:3e:ff:54:ea, Hardware address: fa:16:3e:ff:54:ea
        Last flapped   : 2020-06-22 22:34:02 EST (1w1d 00:22 ago)
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Input errors: 0, Output errors: 0
        Active alarms  : None
        Active defects : None
        Interface transmit statistics: Disabled

        Physical interface: ge-0/0/7, Enabled, Physical link is Up
        Interface index: 140, SNMP ifIndex: 514
        Link-level type: Ethernet, MTU: 1514, Link-mode: Full-duplex, Speed: 1000mbps,
        BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled,
        Remote fault: Online
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: fa:16:3e:ff:05:a1, Hardware address: fa:16:3e:ff:05:a1
        Last flapped   : 2020-06-22 22:34:02 EST (1w1d 00:22 ago)
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Input errors: 0, Output errors: 0
        Active alarms  : None
        Active defects : None
        Interface transmit statistics: Disabled

        Physical interface: ge-0/0/8, Enabled, Physical link is Up
        Interface index: 141, SNMP ifIndex: 515
        Link-level type: Ethernet, MTU: 1514, Link-mode: Full-duplex, Speed: 1000mbps,
        BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled,
        Remote fault: Online
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: fa:16:3e:ff:a2:b7, Hardware address: fa:16:3e:ff:a2:b7
        Last flapped   : 2020-06-22 22:34:02 EST (1w1d 00:22 ago)
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Input errors: 0, Output errors: 0
        Active alarms  : None
        Active defects : None
        Interface transmit statistics: Disabled

        Physical interface: dsc, Enabled, Physical link is Up
        Interface index: 5, SNMP ifIndex: 5
        Type: Software-Pseudo, MTU: Unlimited
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps
        Link flags     : None
        Last flapped   : Never
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
            Input packets : 0
            Output packets: 0
        Input errors: 0, Output errors: 0

        Physical interface: gre, Enabled, Physical link is Up
        Interface index: 10, SNMP ifIndex: 8
        Type: GRE, Link-level type: GRE, MTU: Unlimited, Speed: Unlimited
        Link flags     : Keepalives DTE
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
            Input packets : 0
            Output packets: 0

        Physical interface: ipip, Enabled, Physical link is Up
        Interface index: 11, SNMP ifIndex: 9
        Type: IPIP, Link-level type: IP-over-IP, MTU: Unlimited, Speed: Unlimited
        Link flags     : Keepalives DTE
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
            Input packets : 0
            Output packets: 0

        Physical interface: lo0, Enabled, Physical link is Up
        Interface index: 6, SNMP ifIndex: 6
        Type: Loopback, MTU: Unlimited
        Device flags   : Present Running Loopback
        Interface flags: SNMP-Traps
        Link flags     : None
        Last flapped   : Never
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
            Input packets : 787
            Output packets: 787
        Input errors: 0, Output errors: 0

        Logical interface lo0.0 (Index 66) (SNMP ifIndex 16)
            Flags: SNMP-Traps Encapsulation: Unspecified
            Input packets : 7
            Output packets: 7
            Security: Zone: trust
            Allowed host-inbound traffic : bfd bgp dvmrp igmp ldp msdp nhrp ospf ospf3
            pgm pim rip ripng router-discovery rsvp sap vrrp ping
            Protocol inet, MTU: Unlimited
            Flags: Sendbcast-pkt-to-re
            Addresses, Flags: Is-Default Is-Primary
                Local: 10.64.4.4
            Protocol inet6, MTU: Unlimited
            Flags: None
            Addresses, Flags: Is-Default Is-Primary
                Local: 2001::4
                Local: fe80::5e00:400f:fc00:0

        Logical interface lo0.16384 (Index 65) (SNMP ifIndex 21)
            Flags: SNMP-Traps Encapsulation: Unspecified
            Input packets : 0
            Output packets: 0
            Security: Zone: Null
            Protocol inet, MTU: Unlimited
            Flags: None
            Addresses
                Local: 127.0.0.1

        Logical interface lo0.16385 (Index 67) (SNMP ifIndex 22)
            Flags: SNMP-Traps Encapsulation: Unspecified
            Input packets : 780
            Output packets: 780
            Security: Zone: Null
            Protocol inet, MTU: Unlimited
            Flags: None
            Addresses, Flags: Is-Default Is-Primary
                Local: 10.0.0.1
            Addresses
                Local: 10.0.0.16
            Addresses
                Local: 172.16.64.1
            Addresses
                Local: 172.16.64.4
            Addresses
                Local: 172.16.66.16

        Logical interface lo0.32768 (Index 64) (SNMP ifIndex 248)
            Flags: Encapsulation: Unspecified
            Input packets : 0
            Output packets: 0
            Security: Zone: Null

        Physical interface: lsi, Enabled, Physical link is Up
        Interface index: 4, SNMP ifIndex: 4
        Type: Software-Pseudo, Link-level type: LSI, MTU: 1496, Speed: Unlimited
        Device flags   : Present Running
        Link flags     : None
        Last flapped   : Never
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
            Input packets : 0
            Output packets: 0
        Input errors: 0, Output errors: 0

        Physical interface: mtun, Enabled, Physical link is Up
        Interface index: 64, SNMP ifIndex: 12
        Type: Multicast-GRE, Link-level type: GRE, MTU: Unlimited, Speed: Unlimited
        Link flags     : Keepalives DTE
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
            Input packets : 0
            Output packets: 0

        Physical interface: pimd, Enabled, Physical link is Up
        Interface index: 26, SNMP ifIndex: 11
        Type: PIMD, Link-level type: PIM-Decapsulator, MTU: Unlimited,
        Speed: Unlimited
        Device flags   : Present Running
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
            Input packets : 0
            Output packets: 0

        Physical interface: pime, Enabled, Physical link is Up
        Interface index: 25, SNMP ifIndex: 10
        Type: PIME, Link-level type: PIM-Encapsulator, MTU: Unlimited,
        Speed: Unlimited
        Device flags   : Present Running
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
            Input packets : 0
            Output packets: 0

        Physical interface: pp0, Enabled, Physical link is Up
        Interface index: 128, SNMP ifIndex: 501
        Type: PPPoE, Link-level type: PPPoE, MTU: 1532
        Device flags   : Present Running
        Interface flags: Point-To-Point SNMP-Traps
        Link type      : Full-Duplex
        Link flags     : None
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Input errors: 0, Output errors: 0

        Physical interface: ppd0, Enabled, Physical link is Up
        Interface index: 130, SNMP ifIndex: 503
        Type: PIMD, Link-level type: PIM-Decapsulator, MTU: Unlimited, Speed: 800mbps
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)

        Physical interface: ppe0, Enabled, Physical link is Up
        Interface index: 131, SNMP ifIndex: 504
        Type: PIME, Link-level type: PIM-Encapsulator, MTU: Unlimited, Speed: 800mbps
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)

        Physical interface: st0, Enabled, Physical link is Up
        Interface index: 129, SNMP ifIndex: 502
        Type: Secure-Tunnel, Link-level type: Secure-Tunnel, MTU: 9192
        Device flags   : Present Running
        Interface flags: Point-To-Point
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)

        Physical interface: tap, Enabled, Physical link is Up
        Interface index: 12, SNMP ifIndex: 7
        Type: Software-Pseudo, Link-level type: Interface-Specific, MTU: Unlimited,
        Speed: Unlimited
        Device flags   : Present Running
        Interface flags: SNMP-Traps
        Link flags     : None
        Last flapped   : Never
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
            Input packets : 0
            Output packets: 0
        Input errors: 0, Output errors: 0

        Physical interface: vlan, Enabled, Physical link is Down
        Interface index: 132, SNMP ifIndex: 505
        Type: VLAN, Link-level type: VLAN, MTU: 1518, Speed: 1000mbps
        Device flags   : Present Running Down
        Interface flags: Hardware-Down
        Link type      : Full-Duplex
        CoS queues     : 8 supported, 8 maximum usable queues
        Current address: fa:16:3e:ff:a2:b7, Hardware address: fa:16:3e:ff:a2:b7
        Last flapped   : 2020-06-22 22:29:08 EST (1w1d 00:26 ago)
        Statistics last cleared: 2020-06-30 22:23:44 EST (00:32:21 ago)
        Input rate     : 0 bps (0 pps)
        Output rate    : 0 bps (0 pps)
        Input errors: 0, Output errors: 0"""
    }

    golden_parsed_output = {
        'interface-information': {
            'physical-interface': [{
                'active-alarms': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'active-defects': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'admin-status': 'Enabled',
                'bpdu-error': 'None',
                'current-physical-address': '5e:00:40:ff:00:00',
                'hardware-physical-address': '5e:00:40:ff:00:00',
                'if-auto-negotiation': 'Enabled',
                'if-config-flags': {
                'iff-snmp-traps': True,
                'internal-flags': '0x4000'
                },
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-flow-control': 'Enabled',
                'if-media-flags': {
                'ifmf-none': True
                },
                'if-remote-fault': 'Online',
                'input-error-count': '1568',
                'interface-flapped': '2020-06-22 '
                '22:33:51 '
                'EST '
                '(1w1d '
                '00:22 '
                'ago)',
                'interface-transmit-statistics': 'Disabled',
                'l2pt-error': 'None',
                'link-level-type': 'Ethernet',
                'link-mode': 'Full-duplex',
                'local-index': '133',
                'logical-interface': [{
                'address-family': [{
                    'address-family-flags': {
                    'ifff-is-primary': True,
                    'ifff-sendbcast-pkt-to-re': True
                    },
                    'address-family-name': 'inet',
                    'interface-address': [{
                    'ifa-broadcast': '172.16.1.255',
                    'ifa-destination': '172.16.1/24',
                    'ifa-flags': {
                        'ifaf-current-preferred': True,
                        'ifaf-current-primary': True
                    },
                    'ifa-local': '172.16.1.55'
                    }],
                    'mtu': '1500'
                }],
                'allowed-host-inbound-traffic': {
                    'inbound-dhcp': True,
                    'inbound-http': True,
                    'inbound-https': True,
                    'inbound-ssh': True,
                    'inbound-telnet': True
                },
                'encapsulation': 'ENET2',
                'if-config-flags': {
                    'iff-snmp-traps': True,
                    'internal-flags': '0x4000'
                },
                'local-index': '70',
                'logical-interface-zone-name': 'trust',
                'name': 'ge-0/0/0.0',
                'snmp-index': '507',
                'traffic-statistics': {
                    'input-packets': '4685',
                    'output-packets': '144'
                }
                }],
                'loopback': 'Disabled',
                'mtu': '1514',
                'name': 'ge-0/0/0',
                'oper-status': 'Up',
                'output-error-count': '0',
                'physical-interface-cos-information': {
                'physical-interface-cos-hw-max-queues': '8',
                'physical-interface-cos-use-max-queues': '8'
                },
                'snmp-index': '506',
                'source-filtering': 'Disabled',
                'speed': '1000mbps',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '712',
                'input-pps': '1',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'local-index': '143',
                'name': 'gr-0/0/0',
                'oper-status': 'Up',
                'snmp-index': '519',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'local-index': '144',
                'name': 'ip-0/0/0',
                'oper-status': 'Up',
                'snmp-index': '520',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'interface-flapped': '2020-06-22 '
                '22:33:52 '
                'EST '
                '(1w1d '
                '00:22 '
                'ago)',
                'local-index': '145',
                'name': 'lsq-0/0/0',
                'oper-status': 'Up',
                'snmp-index': '521',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'admin-status': 'Enabled',
                'current-physical-address': '02:96:14:ff:11:43',
                'hardware-physical-address': '02:96:14:ff:11:43',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-media-flags': {
                'ifmf-none': True
                },
                'input-error-count': '0',
                'interface-flapped': 'Never',
                'local-index': '147',
                'name': 'lt-0/0/0',
                'oper-status': 'Up',
                'output-error-count': '0',
                'snmp-index': '523',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'local-index': '146',
                'name': 'mt-0/0/0',
                'oper-status': 'Up',
                'snmp-index': '522',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-media-flags': {
                'ifmf-none': True
                },
                'input-error-count': '0',
                'interface-flapped': '2020-06-22 '
                '22:33:52 '
                'EST '
                '(1w1d '
                '00:22 '
                'ago)',
                'local-index': '142',
                'logical-interface': [{
                    'address-family': [{
                        'address-family-name': 'inet',
                        'mtu': '9192'
                    },
                    {
                        'address-family-name': 'inet6',
                        'mtu': '9192'
                    }
                    ],
                    'local-index': '75',
                    'logical-interface-zone-name': 'Null',
                    'name': 'sp-0/0/0.0',
                    'snmp-index': '518',
                    'traffic-statistics': {
                    'input-packets': '0',
                    'output-packets': '0'
                    }
                },
                {
                    'address-family': [{
                    'address-family-name': 'inet',
                    'interface-address': [{
                        'ifa-destination': '10.0.0.16',
                        'ifa-flags': {
                            'ifaf-current-preferred': True,
                            'ifaf-current-primary': True
                        },
                        'ifa-local': '10.0.0.1'
                        },
                        {
                        'ifa-flags': {},
                        'ifa-local': '10.0.0.6'
                        },
                        {
                        'ifa-destination': '172.16.66.16',
                        'ifa-flags': {
                            'ifaf-current-preferred': True
                        },
                        'ifa-local': '172.16.64.1'
                        },
                        {
                        'ifa-flags': {},
                        'ifa-local': '172.16.64.6'
                        }
                    ],
                    'mtu': '9192'
                    }],
                    'local-index': '76',
                    'logical-interface-zone-name': 'Null',
                    'name': 'sp-0/0/0.16383',
                    'snmp-index': '524',
                    'traffic-statistics': {
                    'input-packets': '0',
                    'output-packets': '0'
                    }
                }
                ],
                'name': 'sp-0/0/0',
                'oper-status': 'Up',
                'output-error-count': '0',
                'snmp-index': '517',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'active-alarms': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'active-defects': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'admin-status': 'Enabled',
                'bpdu-error': 'None',
                'current-physical-address': 'fa:16:3e:ff:7f:fd',
                'hardware-physical-address': 'fa:16:3e:ff:7f:fd',
                'if-auto-negotiation': 'Enabled',
                'if-config-flags': {
                'iff-snmp-traps': True,
                'internal-flags': '0x4000'
                },
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-flow-control': 'Enabled',
                'if-media-flags': {
                'ifmf-none': True
                },
                'if-remote-fault': 'Online',
                'input-error-count': '8',
                'interface-flapped': '2020-06-22 '
                '22:34:01 '
                'EST '
                '(1w1d '
                '00:22 '
                'ago)',
                'interface-transmit-statistics': 'Disabled',
                'l2pt-error': 'None',
                'link-level-type': 'Ethernet',
                'link-mode': 'Full-duplex',
                'local-index': '134',
                'logical-interface': [{
                'address-family': [{
                    'address-family-flags': {
                        'ifff-sendbcast-pkt-to-re': True
                    },
                    'address-family-name': 'inet',
                    'interface-address': [{
                        'ifa-broadcast': '10.70.0.255',
                        'ifa-destination': '40.0.0/24',
                        'ifa-flags': {
                        'ifaf-current-preferred': True,
                        'ifaf-current-primary': True
                        },
                        'ifa-local': '10.70.0.4'
                    }],
                    'mtu': '1500'
                    },
                    {
                    'address-family-name': 'inet6',
                    'interface-address': [{
                        'ifa-destination': '2001:40::/64',
                        'ifa-flags': {
                            'ifaf-current-preferred': True,
                            'ifaf-current-primary': True
                        },
                        'ifa-local': '2001:40::4'
                        },
                        {
                        'ifa-destination': 'fe80::/64',
                        'ifa-flags': {
                            'ifaf-current-preferred': True
                        },
                        'ifa-local': 'fe80::fa16:3eff:feff:7ffd'
                        }
                    ],
                    'mtu': '1500'
                    }
                ],
                'encapsulation': 'ENET2',
                'if-config-flags': {
                    'iff-snmp-traps': True,
                    'internal-flags': '0x4000'
                },
                'local-index': '71',
                'logical-interface-zone-name': 'trust',
                'name': 'ge-0/0/1.0',
                'snmp-index': '516',
                'traffic-statistics': {
                    'input-packets': '555',
                    'output-packets': '546'
                }
                }],
                'loopback': 'Disabled',
                'mtu': '1514',
                'name': 'ge-0/0/1',
                'oper-status': 'Up',
                'output-error-count': '0',
                'physical-interface-cos-information': {
                'physical-interface-cos-hw-max-queues': '8',
                'physical-interface-cos-use-max-queues': '8'
                },
                'snmp-index': '508',
                'source-filtering': 'Disabled',
                'speed': '1000mbps',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '312',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'active-alarms': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'active-defects': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'admin-status': 'Enabled',
                'bpdu-error': 'None',
                'current-physical-address': 'fa:16:3e:ff:0e:52',
                'hardware-physical-address': 'fa:16:3e:ff:0e:52',
                'if-auto-negotiation': 'Enabled',
                'if-config-flags': {
                'iff-snmp-traps': True,
                'internal-flags': '0x4000'
                },
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-flow-control': 'Enabled',
                'if-media-flags': {
                'ifmf-none': True
                },
                'if-remote-fault': 'Online',
                'input-error-count': '2',
                'interface-flapped': '2020-06-22 '
                '22:34:01 '
                'EST '
                '(1w1d '
                '00:22 '
                'ago)',
                'interface-transmit-statistics': 'Disabled',
                'l2pt-error': 'None',
                'link-level-type': 'Ethernet',
                'link-mode': 'Full-duplex',
                'local-index': '135',
                'logical-interface': [{
                'address-family': [{
                    'address-family-flags': {
                        'ifff-sendbcast-pkt-to-re': True
                    },
                    'address-family-name': 'inet',
                    'interface-address': [{
                        'ifa-broadcast': '10.205.0.255',
                        'ifa-destination': '50.0.0/24',
                        'ifa-flags': {
                        'ifaf-current-preferred': True,
                        'ifaf-current-primary': True
                        },
                        'ifa-local': '10.205.0.4'
                    }],
                    'mtu': '1500'
                    },
                    {
                    'address-family-name': 'inet6',
                    'interface-address': [{
                        'ifa-destination': '2001:50::/64',
                        'ifa-flags': {
                            'ifaf-current-preferred': True,
                            'ifaf-current-primary': True
                        },
                        'ifa-local': '2001:50::4'
                        },
                        {
                        'ifa-destination': 'fe80::/64',
                        'ifa-flags': {
                            'ifaf-current-preferred': True
                        },
                        'ifa-local': 'fe80::fa16:3eff:feff:e52'
                        }
                    ],
                    'mtu': '1500'
                    }
                ],
                'encapsulation': 'ENET2',
                'if-config-flags': {
                    'iff-snmp-traps': True,
                    'internal-flags': '0x4000'
                },
                'local-index': '72',
                'logical-interface-zone-name': 'trust',
                'name': 'ge-0/0/2.0',
                'snmp-index': '525',
                'traffic-statistics': {
                    'input-packets': '450',
                    'output-packets': '465'
                }
                }],
                'loopback': 'Disabled',
                'mtu': '1514',
                'name': 'ge-0/0/2',
                'oper-status': 'Up',
                'output-error-count': '0',
                'physical-interface-cos-information': {
                'physical-interface-cos-hw-max-queues': '8',
                'physical-interface-cos-use-max-queues': '8'
                },
                'snmp-index': '509',
                'source-filtering': 'Disabled',
                'speed': '1000mbps',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '528',
                'output-pps': '0'
                }
            },
            {
                'active-alarms': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'active-defects': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'admin-status': 'Enabled',
                'bpdu-error': 'None',
                'current-physical-address': 'fa:16:3e:ff:12:8e',
                'hardware-physical-address': 'fa:16:3e:ff:12:8e',
                'if-auto-negotiation': 'Enabled',
                'if-config-flags': {
                'iff-snmp-traps': True,
                'internal-flags': '0x4000'
                },
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-flow-control': 'Enabled',
                'if-media-flags': {
                'ifmf-none': True
                },
                'if-remote-fault': 'Online',
                'input-error-count': '0',
                'interface-flapped': '2020-06-22 '
                '22:34:01 '
                'EST '
                '(1w1d '
                '00:22 '
                'ago)',
                'interface-transmit-statistics': 'Disabled',
                'l2pt-error': 'None',
                'link-level-type': 'Ethernet',
                'link-mode': 'Full-duplex',
                'local-index': '136',
                'logical-interface': [{
                'address-family': [{
                    'address-family-flags': {
                        'ifff-sendbcast-pkt-to-re': True
                    },
                    'address-family-name': 'inet',
                    'mtu': '1500'
                    },
                    {
                    'address-family-name': 'inet6',
                    'interface-address': [{
                        'ifa-destination': 'fe80::/64',
                        'ifa-flags': {
                        'ifaf-current-preferred': True
                        },
                        'ifa-local': 'fe80::fa16:3eff:feff:128e'
                    }],
                    'mtu': '1500'
                    }
                ],
                'encapsulation': 'ENET2',
                'if-config-flags': {
                    'iff-snmp-traps': True,
                    'internal-flags': '0x4000'
                },
                'local-index': '73',
                'logical-interface-zone-name': 'trust',
                'name': 'ge-0/0/3.0',
                'snmp-index': '526',
                'traffic-statistics': {
                    'input-packets': '0',
                    'output-packets': '0'
                }
                }],
                'loopback': 'Disabled',
                'mtu': '1514',
                'name': 'ge-0/0/3',
                'oper-status': 'Up',
                'output-error-count': '0',
                'physical-interface-cos-information': {
                'physical-interface-cos-hw-max-queues': '8',
                'physical-interface-cos-use-max-queues': '8'
                },
                'snmp-index': '510',
                'source-filtering': 'Disabled',
                'speed': '1000mbps',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'active-alarms': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'active-defects': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'admin-status': 'Enabled',
                'bpdu-error': 'None',
                'current-physical-address': 'fa:16:3e:ff:37:bd',
                'hardware-physical-address': 'fa:16:3e:ff:37:bd',
                'if-auto-negotiation': 'Enabled',
                'if-config-flags': {
                'iff-snmp-traps': True,
                'internal-flags': '0x4000'
                },
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-flow-control': 'Enabled',
                'if-media-flags': {
                'ifmf-none': True
                },
                'if-remote-fault': 'Online',
                'input-error-count': '0',
                'interface-flapped': '2020-06-22 '
                '22:34:02 '
                'EST '
                '(1w1d '
                '00:22 '
                'ago)',
                'interface-transmit-statistics': 'Disabled',
                'l2pt-error': 'None',
                'link-level-type': 'Ethernet',
                'link-mode': 'Full-duplex',
                'local-index': '137',
                'logical-interface': [{
                'address-family': [{
                    'address-family-flags': {
                        'ifff-sendbcast-pkt-to-re': True
                    },
                    'address-family-name': 'inet',
                    'mtu': '1500'
                    },
                    {
                    'address-family-name': 'inet6',
                    'interface-address': [{
                        'ifa-destination': 'fe80::/64',
                        'ifa-flags': {
                        'ifaf-current-preferred': True
                        },
                        'ifa-local': 'fe80::fa16:3eff:feff:37bd'
                    }],
                    'mtu': '1500'
                    }
                ],
                'encapsulation': 'ENET2',
                'if-config-flags': {
                    'iff-snmp-traps': True,
                    'internal-flags': '0x4000'
                },
                'local-index': '74',
                'logical-interface-zone-name': 'trust',
                'name': 'ge-0/0/4.0',
                'snmp-index': '527',
                'traffic-statistics': {
                    'input-packets': '787',
                    'output-packets': '787'
                }
                }],
                'loopback': 'Disabled',
                'mtu': '1514',
                'name': 'ge-0/0/4',
                'oper-status': 'Up',
                'output-error-count': '0',
                'physical-interface-cos-information': {
                'physical-interface-cos-hw-max-queues': '8',
                'physical-interface-cos-use-max-queues': '8'
                },
                'snmp-index': '511',
                'source-filtering': 'Disabled',
                'speed': '1000mbps',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'active-alarms': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'active-defects': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'admin-status': 'Enabled',
                'bpdu-error': 'None',
                'current-physical-address': 'fa:16:3e:ff:38:28',
                'hardware-physical-address': 'fa:16:3e:ff:38:28',
                'if-auto-negotiation': 'Enabled',
                'if-config-flags': {
                'iff-snmp-traps': True,
                'internal-flags': '0x4000'
                },
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-flow-control': 'Enabled',
                'if-media-flags': {
                'ifmf-none': True
                },
                'if-remote-fault': 'Online',
                'input-error-count': '0',
                'interface-flapped': '2020-06-22 '
                '22:34:02 '
                'EST '
                '(1w1d '
                '00:22 '
                'ago)',
                'interface-transmit-statistics': 'Disabled',
                'l2pt-error': 'None',
                'link-level-type': 'Ethernet',
                'link-mode': 'Full-duplex',
                'local-index': '138',
                'loopback': 'Disabled',
                'mtu': '1514',
                'name': 'ge-0/0/5',
                'oper-status': 'Up',
                'output-error-count': '0',
                'physical-interface-cos-information': {
                'physical-interface-cos-hw-max-queues': '8',
                'physical-interface-cos-use-max-queues': '8'
                },
                'snmp-index': '512',
                'source-filtering': 'Disabled',
                'speed': '1000mbps',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'active-alarms': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'active-defects': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'admin-status': 'Enabled',
                'bpdu-error': 'None',
                'current-physical-address': 'fa:16:3e:ff:54:ea',
                'hardware-physical-address': 'fa:16:3e:ff:54:ea',
                'if-auto-negotiation': 'Enabled',
                'if-config-flags': {
                'iff-snmp-traps': True,
                'internal-flags': '0x4000'
                },
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-flow-control': 'Enabled',
                'if-media-flags': {
                'ifmf-none': True
                },
                'if-remote-fault': 'Online',
                'input-error-count': '0',
                'interface-flapped': '2020-06-22 '
                '22:34:02 '
                'EST '
                '(1w1d '
                '00:22 '
                'ago)',
                'interface-transmit-statistics': 'Disabled',
                'l2pt-error': 'None',
                'link-level-type': 'Ethernet',
                'link-mode': 'Full-duplex',
                'local-index': '139',
                'loopback': 'Disabled',
                'mtu': '1514',
                'name': 'ge-0/0/6',
                'oper-status': 'Up',
                'output-error-count': '0',
                'physical-interface-cos-information': {
                'physical-interface-cos-hw-max-queues': '8',
                'physical-interface-cos-use-max-queues': '8'
                },
                'snmp-index': '513',
                'source-filtering': 'Disabled',
                'speed': '1000mbps',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'active-alarms': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'active-defects': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'admin-status': 'Enabled',
                'bpdu-error': 'None',
                'current-physical-address': 'fa:16:3e:ff:05:a1',
                'hardware-physical-address': 'fa:16:3e:ff:05:a1',
                'if-auto-negotiation': 'Enabled',
                'if-config-flags': {
                'iff-snmp-traps': True,
                'internal-flags': '0x4000'
                },
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-flow-control': 'Enabled',
                'if-media-flags': {
                'ifmf-none': True
                },
                'if-remote-fault': 'Online',
                'input-error-count': '0',
                'interface-flapped': '2020-06-22 '
                '22:34:02 '
                'EST '
                '(1w1d '
                '00:22 '
                'ago)',
                'interface-transmit-statistics': 'Disabled',
                'l2pt-error': 'None',
                'link-level-type': 'Ethernet',
                'link-mode': 'Full-duplex',
                'local-index': '140',
                'loopback': 'Disabled',
                'mtu': '1514',
                'name': 'ge-0/0/7',
                'oper-status': 'Up',
                'output-error-count': '0',
                'physical-interface-cos-information': {
                'physical-interface-cos-hw-max-queues': '8',
                'physical-interface-cos-use-max-queues': '8'
                },
                'snmp-index': '514',
                'source-filtering': 'Disabled',
                'speed': '1000mbps',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'active-alarms': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'active-defects': {
                'interface-alarms': {
                    'alarm-not-present': True
                }
                },
                'admin-status': 'Enabled',
                'bpdu-error': 'None',
                'current-physical-address': 'fa:16:3e:ff:a2:b7',
                'hardware-physical-address': 'fa:16:3e:ff:a2:b7',
                'if-auto-negotiation': 'Enabled',
                'if-config-flags': {
                'iff-snmp-traps': True,
                'internal-flags': '0x4000'
                },
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-flow-control': 'Enabled',
                'if-media-flags': {
                'ifmf-none': True
                },
                'if-remote-fault': 'Online',
                'input-error-count': '0',
                'interface-flapped': '2020-06-22 '
                '22:34:02 '
                'EST '
                '(1w1d '
                '00:22 '
                'ago)',
                'interface-transmit-statistics': 'Disabled',
                'l2pt-error': 'None',
                'link-level-type': 'Ethernet',
                'link-mode': 'Full-duplex',
                'local-index': '141',
                'loopback': 'Disabled',
                'mtu': '1514',
                'name': 'ge-0/0/8',
                'oper-status': 'Up',
                'output-error-count': '0',
                'physical-interface-cos-information': {
                'physical-interface-cos-hw-max-queues': '8',
                'physical-interface-cos-use-max-queues': '8'
                },
                'snmp-index': '515',
                'source-filtering': 'Disabled',
                'speed': '1000mbps',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-media-flags': {
                'ifmf-none': True
                },
                'input-error-count': '0',
                'interface-flapped': 'Never',
                'local-index': '5',
                'name': 'dsc',
                'oper-status': 'Up',
                'output-error-count': '0',
                'snmp-index': '5',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)'
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'local-index': '10',
                'name': 'gre',
                'oper-status': 'Up',
                'snmp-index': '8',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)'
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'local-index': '11',
                'name': 'ipip',
                'oper-status': 'Up',
                'snmp-index': '9',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)'
            },
            {
                'admin-status': 'Enabled',
                'if-media-flags': {
                'ifmf-none': True
                },
                'input-error-count': '0',
                'interface-flapped': 'Never',
                'local-index': '6',
                'logical-interface': [{
                    'address-family': [{
                        'address-family-flags': {
                        'ifff-sendbcast-pkt-to-re': True
                        },
                        'address-family-name': 'inet',
                        'interface-address': [{
                        'ifa-flags': {
                            'ifaf-current-default': True,
                            'ifaf-current-primary': True
                        },
                        'ifa-local': '10.64.4.4'
                        }],
                        'mtu': 'Unlimited'
                    },
                    {
                        'address-family-name': 'inet6',
                        'interface-address': [{
                        'ifa-flags': {
                            'ifaf-current-default': True,
                            'ifaf-current-primary': True
                        },
                        'ifa-local': 'fe80::5e00:400f:fc00:0'
                        }],
                        'mtu': 'Unlimited'
                    }
                    ],
                    'local-index': '66',
                    'logical-interface-zone-name': 'trust',
                    'name': 'lo0.0',
                    'snmp-index': '16',
                    'traffic-statistics': {
                    'input-packets': '7',
                    'output-packets': '7'
                    }
                },
                {
                    'address-family': [{
                    'address-family-name': 'inet',
                    'interface-address': [{
                        'ifa-flags': {},
                        'ifa-local': '127.0.0.1'
                    }],
                    'mtu': 'Unlimited'
                    }],
                    'local-index': '65',
                    'logical-interface-zone-name': 'Null',
                    'name': 'lo0.16384',
                    'snmp-index': '21',
                    'traffic-statistics': {
                    'input-packets': '0',
                    'output-packets': '0'
                    }
                },
                {
                    'address-family': [{
                    'address-family-name': 'inet',
                    'interface-address': [{
                        'ifa-flags': {
                            'ifaf-current-default': True,
                            'ifaf-current-primary': True
                        },
                        'ifa-local': '10.0.0.1'
                        },
                        {
                        'ifa-flags': {},
                        'ifa-local': '10.0.0.16'
                        },
                        {
                        'ifa-flags': {},
                        'ifa-local': '172.16.64.1'
                        },
                        {
                        'ifa-flags': {},
                        'ifa-local': '172.16.64.4'
                        },
                        {
                        'ifa-flags': {},
                        'ifa-local': '172.16.66.16'
                        }
                    ],
                    'mtu': 'Unlimited'
                    }],
                    'local-index': '67',
                    'logical-interface-zone-name': 'Null',
                    'name': 'lo0.16385',
                    'snmp-index': '22',
                    'traffic-statistics': {
                    'input-packets': '780',
                    'output-packets': '780'
                    }
                },
                {
                    'local-index': '64',
                    'logical-interface-zone-name': 'Null',
                    'name': 'lo0.32768',
                    'snmp-index': '248',
                    'traffic-statistics': {
                    'input-packets': '0',
                    'output-packets': '0'
                    }
                }
                ],
                'name': 'lo0',
                'oper-status': 'Up',
                'output-error-count': '0',
                'snmp-index': '6',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)'
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-media-flags': {
                'ifmf-none': True
                },
                'input-error-count': '0',
                'interface-flapped': 'Never',
                'local-index': '4',
                'name': 'lsi',
                'oper-status': 'Up',
                'output-error-count': '0',
                'snmp-index': '4',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)'
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'local-index': '64',
                'name': 'mtun',
                'oper-status': 'Up',
                'snmp-index': '12',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)'
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'local-index': '26',
                'name': 'pimd',
                'oper-status': 'Up',
                'snmp-index': '11',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)'
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'local-index': '25',
                'name': 'pime',
                'oper-status': 'Up',
                'snmp-index': '10',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)'
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-media-flags': {
                'ifmf-none': True
                },
                'input-error-count': '0',
                'local-index': '128',
                'name': 'pp0',
                'oper-status': 'Up',
                'output-error-count': '0',
                'snmp-index': '501',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'local-index': '130',
                'name': 'ppd0',
                'oper-status': 'Up',
                'snmp-index': '503',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'local-index': '131',
                'name': 'ppe0',
                'oper-status': 'Up',
                'snmp-index': '504',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'local-index': '129',
                'name': 'st0',
                'oper-status': 'Up',
                'snmp-index': '502',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            },
            {
                'admin-status': 'Enabled',
                'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
                },
                'if-media-flags': {
                'ifmf-none': True
                },
                'input-error-count': '0',
                'interface-flapped': 'Never',
                'local-index': '12',
                'name': 'tap',
                'oper-status': 'Up',
                'output-error-count': '0',
                'snmp-index': '7',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)'
            },
            {
                'admin-status': 'Enabled',
                'current-physical-address': 'fa:16:3e:ff:a2:b7',
                'hardware-physical-address': 'fa:16:3e:ff:a2:b7',
                'input-error-count': '0',
                'interface-flapped': '2020-06-22 '
                '22:29:08 '
                'EST '
                '(1w1d '
                '00:26 '
                'ago)',
                'local-index': '132',
                'name': 'vlan',
                'oper-status': 'Down',
                'output-error-count': '0',
                'physical-interface-cos-information': {
                'physical-interface-cos-hw-max-queues': '8',
                'physical-interface-cos-use-max-queues': '8'
                },
                'snmp-index': '505',
                'statistics-cleared': '2020-06-30 '
                '22:23:44 '
                'EST '
                '(00:32:21 '
                'ago)',
                'traffic-statistics': {
                'input-bps': '0',
                'input-pps': '0',
                'output-bps': '0',
                'output-pps': '0'
                }
            }
            ]
        }
        }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfacesStatistics(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfacesStatistics(device=self.device)
        parsed_output = interface_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

class TestShowInterfacesExtensive(unittest.TestCase):
    device = Device(name="aDevice")
    maxDiff = None
    empty_output = {"execute.return_value": ""}

    golden_output = {"execute.return_value": """
        show interfaces extensive ge-0/0/0 
        Physical interface: ge-0/0/0, Enabled, Physical link is Up
        Interface index: 148, SNMP ifIndex: 526, Generation: 2988
        Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None, Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None,
        Loopback: Disabled, Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        Pad to minimum frame size: Disabled
        Device flags   : Present Running
        Interface flags: SNMP-Traps Internal: 0x4000
        Link flags     : None
        CoS queues     : 8 supported, 8 maximum usable queues
        Schedulers     : 0
        Hold-times     : Up 0 ms, Down 0 ms
        Damping        : half-life: 0 sec, max-suppress: 0 sec, reuse: 0, suppress: 0, state: unsuppressed
        Current address: 00:50:56:8d:c7:98, Hardware address: 00:50:56:8d:c7:98
        Last flapped   : 2020-08-05 02:58:37 UTC (03:17:16 ago)
        Statistics last cleared: 2020-08-05 06:15:50 UTC (00:00:03 ago)
        Traffic statistics:
        Input  bytes  :                 1900                 3912 bps
        Output bytes  :                  648                 1544 bps
        Input  packets:                   26                    6 pps
        Output packets:                    7                    2 pps
        IPv6 transit statistics:
        Input  bytes  :                  256
        Output bytes  :                    0
        Input  packets:                    4
        Output packets:                    0
        Dropped traffic statistics due to STP State:
        Input  bytes  :                    0
        Output bytes  :                    0
        Input  packets:                    0
        Output packets:                    0
        Input errors:
            Errors: 0, Drops: 0, Framing errors: 0, Runts: 0, Policed discards: 0, L3 incompletes: 0, L2 channel errors: 0, L2 mismatch timeouts: 0, FIFO errors: 0, Resource errors: 0
        Output errors:
            Carrier transitions: 0, Errors: 0, Drops: 0, Collisions: 0, Aged packets: 0, FIFO errors: 0, HS link CRC errors: 0, MTU errors: 0, Resource errors: 0
        Egress queues: 8 supported, 4 in use
        Queue counters:       Queued packets  Transmitted packets      Dropped packets
            0                                0                    0                    0
            1                                0                    0                    0
            2                                0                    0                    0
            3                                2                    2                    0
        Queue number:         Mapped forwarding classes
            0                   best-effort
            1                   expedited-forwarding
            2                   assured-forwarding
            3                   network-control
        Active alarms  : None
        Active defects : None
        PCS statistics                      Seconds
            Bit errors                             0
            Errored blocks                         0
        Ethernet FEC statistics              Errors
            FEC Corrected Errors                    0
            FEC Uncorrected Errors                  0
            FEC Corrected Errors Rate               0
            FEC Uncorrected Errors Rate             0
        MAC statistics:                      Receive         Transmit
            Total octets                          2230              404
            Total packets                           12                2
            Unicast packets                         27                6
            Broadcast packets                        0                0
            Multicast packets                        0                0
            CRC/Align errors                         0                0
            FIFO errors                              0                0
            MAC control frames                       0                0
            MAC pause frames                         0                0
            Oversized frames                         0
            Jabber frames                            0
            Fragment frames                          0
            VLAN tagged frames                       0
            Code violations                          0
            Total errors                             0                0
        Filter statistics:
            Input packet count                      27
            Input packet rejects                    22
            Input DA rejects                         0
            Input SA rejects                         0
            Output packet count                                       6
            Output packet pad count                                   0
            Output packet error count                                 0
            CAM destination filters: 0, CAM source filters: 0
        Autonegotiation information:
            Negotiation status: Incomplete
        Packet Forwarding Engine configuration:
            Destination slot: 0 (0x00)
        CoS information:
            Direction : Output
            CoS transmit queue               Bandwidth               Buffer Priority   Limit
                                    %%            bps     %%           usec
            0 best-effort            95      950000000    95              0      low    none
            3 network-control         5       50000000     5              0      low    none
        Interface transmit statistics: Disabled

        Logical interface ge-0/0/0.0 (Index 332) (SNMP ifIndex 537) (Generation 30193)
            Flags: Up SNMP-Traps 0x4004000 Encapsulation: ENET2
            Traffic statistics:
            Input  bytes  :                 1900
            Output bytes  :                  606
            Input  packets:                   26
            Output packets:                    7
            IPv6 transit statistics:
            Input  bytes  :                  256
            Output bytes  :                    0
            Input  packets:                    4
            Output packets:                    0
            Local statistics:
            Input  bytes  :                    0
            Output bytes  :                  606
            Input  packets:                    0
            Output packets:                    7
            Transit statistics:
            Input  bytes  :                 1900                 3912 bps
            Output bytes  :                    0                    0 bps
            Input  packets:                   26                    6 pps
            Output packets:                    0                    0 pps
            IPv6 transit statistics:
            Input  bytes  :                 256                  504 bps
            Output bytes  :                   0                    0 bps
            Input  packets:                   4                    0 pps
            Output packets:                   0                    0 pps
            Protocol inet, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Generation: 82967, Route table: 0
            Flags: Sendbcast-pkt-to-re
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 20.0.0/24, Local: 20.0.0.1, Broadcast: 20.0.0.255, Generation: 172354
            Protocol inet6, MTU: 1500
            Max nh cache: 75000, New hold nh limit: 75000, Curr nh cnt: 0, Curr new hold cnt: 0, NH drop cnt: 0
            Generation: 82968, Route table: 0
            Flags: Is-Primary
            Addresses, Flags: Is-Preferred Is-Primary
                Destination: 2001:20::/64, Local: 2001:20::1
            Generation: 172356
            Addresses, Flags: Is-Preferred
                Destination: fe80::/64, Local: fe80::250:56ff:fe8d:c798
            Protocol multiservice, MTU: Unlimited, Generation: 172358
            Generation: 82969, Route table: 0
            Flags: Is-Primary
            Policer: Input: __default_arp_policer__
            """}

    golden_parsed_output = {
        'interface-information': {
            'physical-interface': [{
            'name': 'ge-0/0/0',
            'admin-status': {
                '@junos:format': 'Enabled'
            },
            'local-index': '148',
            'snmp-index': '526',
            'link-level-type': 'Ethernet',
            'mtu': '1514',
            'mru': '1522',
            'sonet-mode': 'LAN-PHY',
            'speed': '1000mbps',
            'bpdu-error': 'None',
            'ld-pdu-error': 'None',
            'eth-switch-error': 'None',
            'loopback': 'Disabled',
            'source-filtering': 'Disabled',
            'if-flow-control': 'Enabled',
            'if-auto-negotiation': 'Enabled',
            'if-remote-fault': 'Online',
            'pad-to-minimum-frame-size': 'Disabled',
            'if-device-flags': {
                'ifdf-present': True,
                'ifdf-running': True
            },
            'if-config-flags': {
                'iff-snmp-traps': True,
                'internal-flags': '0x4000'
            },
            'if-media-flags': {
                'ifmf-none': True
            },
            'physical-interface-cos-information': {
                'physical-interface-cos-hw-max-queues': '8',
                'physical-interface-cos-use-max-queues': '8'
            },
            'current-physical-address': '00:50:56:8d:c7:98',
            'hardware-physical-address': '00:50:56:8d:c7:98',
            'interface-flapped': {
                '#text': '2020-08-05 02:58:37 UTC (03:17:16 ago)'
            },
            'traffic-statistics': {
                'input-bytes': '1900',
                'input-bps': '3912',
                'output-bytes': '648',
                'output-bps': '1544',
                'input-packets': '26',
                'input-pps': '6',
                'output-packets': '7',
                'output-pps': '2',
                'ipv6-transit-statistics': {
                'input-bytes': '256',
                'output-bytes': '0',
                'input-packets': '4',
                'output-packets': '0'
                }
            },
            'stp-traffic-statistics': {
                'stp-input-bytes-dropped': '0',
                'stp-output-bytes-dropped': '0',
                'stp-input-packets-dropped': '0',
                'stp-output-packets-dropped': '0'
            },
            'input-error-list': {
                'input-errors': '0',
                'input-drops': '0',
                'framing-errors': '0',
                'input-runts': '0',
                'input-discards': '0',
                'input-l3-incompletes': '0',
                'input-l2-channel-errors': '0',
                'input-l2-mismatch-timeouts': '0',
                'input-fifo-errors': '0',
                'input-resource-errors': '0'
            },
            'output-error-list': {
                'carrier-transitions': '0',
                'output-errors': '0',
                'output-drops': '0',
                'output-collisions': '0',
                'aged-packets': '0',
                'output-fifo-errors': '0',
                'hs-link-crc-errors': '0',
                'mtu-errors': '0',
                'output-resource-errors': '0'
            },
            'queue-counters': {
                'interface-cos-short-summary': {
                'intf-cos-num-queues-supported': '8',
                'intf-cos-num-queues-in-use': '4'
                },
                'queue': [{
                'queue-number': '0',
                'queue-counters-queued-packets': '0',
                'queue-counters-trans-packets': '0',
                'queue-counters-total-drop-packets': '0'
                }, {
                'queue-number': '1',
                'queue-counters-queued-packets': '0',
                'queue-counters-trans-packets': '0',
                'queue-counters-total-drop-packets': '0'
                }, {
                'queue-number': '2',
                'queue-counters-queued-packets': '0',
                'queue-counters-trans-packets': '0',
                'queue-counters-total-drop-packets': '0'
                }, {
                'queue-number': '3',
                'queue-counters-queued-packets': '2',
                'queue-counters-trans-packets': '2',
                'queue-counters-total-drop-packets': '0'
                }]
            },
            'active-alarms': {
                'interface-alarms': {
                'alarm-not-present': True
                }
            },
            'active-defects': {
                'interface-alarms': {
                'alarm-not-present': True
                }
            },
            'ethernet-pcs-statistics': {
                'bit-error-seconds': '0',
                'errored-blocks-seconds': '0'
            },
            'ethernet-fec-statistics': {
                'fec_ccw_count': '0',
                'fec_nccw_count': '0',
                'fec_ccw_error_rate': '0',
                'fec_nccw_error_rate': '0'
            },
            'ethernet-mac-statistics': {
                'input-bytes': '2230',
                'output-bytes': '404',
                'input-packets': '12',
                'output-packets': '2',
                'input-unicasts': '27',
                'output-unicasts': '6',
                'input-broadcasts': '0',
                'output-broadcasts': '0',
                'input-multicasts': '0',
                'output-multicasts': '0',
                'input-crc-errors': '0',
                'output-crc-errors': '0',
                'input-fifo-errors': '0',
                'output-fifo-errors': '0',
                'input-mac-control-frames': '0',
                'output-mac-control-frames': '0',
                'input-mac-pause-frames': '0',
                'output-mac-pause-frames': '0',
                'input-oversized-frames': '0',
                'input-jabber-frames': '0',
                'input-fragment-frames': '0',
                'input-vlan-tagged-frames': '0',
                'input-code-violations': '0'
            },
            'interface-transmit-statistics': 'Disabled',
            'logical-interface': [{
                'name': 'ge-0/0/0.0',
                'local-index': '332',
                'snmp-index': '537',
                'if-config-flags': {
                'iff-up': True,
                'iff-snmp-traps': True,
                'internal-flags': '0x4004000'
                },
                'encapsulation': 'ENET2',
                'traffic-statistics': {
                'input-bytes': '1900',
                'output-bytes': '606',
                'input-packets': '26',
                'output-packets': '7',
                'ipv6-transit-statistics': {
                    'input-bytes': '0',
                    'output-bytes': '606',
                    'input-packets': '0',
                    'output-packets': '7'
                }
                },
                'transit-traffic-statistics': {
                'input-bytes': '1900',
                'input-bps': '3912',
                'output-bytes': '0',
                'output-bps': '0',
                'input-packets': '26',
                'input-pps': '6',
                'output-packets': '0',
                'output-pps': '0',
                'ipv6-transit-statistics': {
                    'input-bytes': '256',
                    'input-bps': '504',
                    'output-bytes': '0',
                    'output-bps': '0',
                    'input-packets': '4',
                    'input-pps': '0',
                    'output-packets': '0',
                    'output-pps': '0'
                }
                },
                'address-family': [{
                'address-family-name': 'inet',
                'mtu': '1500',
                'max-local-cache': '75000',
                'new-hold-limit': '75000',
                'intf-curr-cnt': '0',
                'intf-unresolved-cnt': '0',
                'intf-dropcnt': '0',
                'address-family-flags': {
                    'ifff-sendbcast-pkt-to-re': True
                },
                'interface-address': {
                    'ifa-flags': {
                    'ifaf-is-preferred': True,
                    'ifaf-is-primary': True
                    }
                }
                }, {
                'address-family-name': 'inet6',
                'mtu': '1500',
                'max-local-cache': '75000',
                'new-hold-limit': '75000',
                'intf-curr-cnt': '0',
                'intf-unresolved-cnt': '0',
                'intf-dropcnt': '0',
                'address-family-flags': {
                    'ifff-is-primary': True
                },
                'interface-address': [{
                    'ifa-flags': {
                    'ifaf-is-preferred': True,
                    'ifaf-is-primary': True
                    },
                    'ifa-destination': '2001:20::/64',
                    'ifa-local': '2001:20::1'
                }, {
                    'ifa-flags': {
                    'ifaf-is-preferred': True
                    },
                    'ifa-destination': 'fe80::/64',
                    'ifa-local': 'fe80::250:56ff:fe8d:c798'
                }]
                }, {
                'address-family-name': 'multiservice',
                'mtu': 'Unlimited',
                'generation': '172358',
                'address-family-flags': {
                    'ifff-is-primary': True
                }
                }]
            }]
            }]
        }
        }


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfacesExtensive(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfacesExtensive(device=self.device)
        parsed_output = interface_obj.parse(interface='ge-0/0/0')
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()