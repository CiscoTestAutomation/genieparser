expected_output = {
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
            }
        ]
    }

}
