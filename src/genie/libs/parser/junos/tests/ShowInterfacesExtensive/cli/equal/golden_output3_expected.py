expected_output = {
    "interface-information": {
        "physical-interface": [
            {
                "name": "ae0",
                "admin-status": {"@junos:format": "Enabled"},
                "local-index": "159",
                "snmp-index": "539",
                "pad-to-minimum-frame-size": "Disabled",
                "if-device-flags": {"ifdf-present": True, "ifdf-running": True},
                "if-config-flags": {"iff-snmp-traps": True, "internal-flags": "0x4000"},
                "current-physical-address": "2c:6b:f5:d6:f8:c0",
                "hardware-physical-address": "2c:6b:f5:d6:f8:c0",
                "interface-flapped": {
                    "#text": "2021-01-08 00:13:28 JST (00:03:32 ago)"
                },
                "statistics-cleared": "Never",
                "traffic-statistics": {
                    "input-bytes": "227807",
                    "input-bps": "3432",
                    "output-bytes": "173544",
                    "output-bps": "2120",
                    "input-packets": "2357",
                    "input-pps": "4",
                    "output-packets": "1341",
                    "output-pps": "2",
                    "ipv6-transit-statistics": {
                        "input-bytes": "912",
                        "output-bytes": "0",
                        "input-packets": "14",
                        "output-packets": "0",
                    },
                },
                "stp-traffic-statistics": {
                    "stp-input-bytes-dropped": "0",
                    "stp-output-bytes-dropped": "0",
                    "stp-input-packets-dropped": "0",
                    "stp-output-packets-dropped": "0",
                },
                "ethernet-mac-statistics": {
                    "input-broadcasts": "0",
                    "output-broadcasts": "0",
                    "input-multicasts": "0",
                    "output-multicasts": "0",
                },
                "input-error-list": {
                    "input-errors": "0",
                    "input-drops": "0",
                    "framing-errors": "0",
                    "input-runts": "0",
                    "input-giants": "0",
                    "input-discards": "0",
                    "input-resource-errors": "0",
                },
                "output-error-list": {
                    "carrier-transitions": "0",
                    "output-errors": "0",
                    "output-drops": "0",
                    "mtu-errors": "0",
                    "output-resource-errors": "0",
                },
                "queue-counters": {
                    "queue": [
                        {
                            "queue-number": "0",
                            "queue-counters-queued-packets": "0",
                            "queue-counters-trans-packets": "0",
                            "queue-counters-total-drop-packets": "0",
                            "forwarding-class-name": "best-effort",
                        },
                        {
                            "queue-number": "1",
                            "queue-counters-queued-packets": "0",
                            "queue-counters-trans-packets": "0",
                            "queue-counters-total-drop-packets": "0",
                            "forwarding-class-name": "expedited-forwarding",
                        },
                        {
                            "queue-number": "2",
                            "queue-counters-queued-packets": "0",
                            "queue-counters-trans-packets": "0",
                            "queue-counters-total-drop-packets": "0",
                            "forwarding-class-name": "assured-forwarding",
                        },
                        {
                            "queue-number": "3",
                            "queue-counters-queued-packets": "0",
                            "queue-counters-trans-packets": "0",
                            "queue-counters-total-drop-packets": "0",
                            "forwarding-class-name": "network-control",
                        },
                        {
                            "queue-number": "0",
                            "queue-counters-queued-packets": "1",
                            "queue-counters-trans-packets": "1",
                            "queue-counters-total-drop-packets": "0",
                        },
                        {
                            "queue-number": "1",
                            "queue-counters-queued-packets": "0",
                            "queue-counters-trans-packets": "0",
                            "queue-counters-total-drop-packets": "0",
                        },
                        {
                            "queue-number": "2",
                            "queue-counters-queued-packets": "0",
                            "queue-counters-trans-packets": "0",
                            "queue-counters-total-drop-packets": "0",
                        },
                        {
                            "queue-number": "3",
                            "queue-counters-queued-packets": "1336",
                            "queue-counters-trans-packets": "1336",
                            "queue-counters-total-drop-packets": "0",
                        },
                    ],
                    "interface-cos-short-summary": {
                        "intf-cos-num-queues-supported": "8",
                        "intf-cos-num-queues-in-use": "4",
                    },
                },
                "logical-interface": [
                    {
                        "name": "ae0.0",
                        "local-index": "320",
                        "snmp-index": "542",
                        "if-config-flags": {
                            "iff-up": True,
                            "iff-snmp-traps": True,
                            "internal-flags": "0x4004000",
                        },
                        "encapsulation": "ENET2",
                        "address-family": [
                            {
                                "address-family-name": "inet",
                                "mtu": "1500",
                                "max-local-cache": "75000",
                                "new-hold-limit": "75000",
                                "intf-curr-cnt": "0",
                                "intf-unresolved-cnt": "0",
                                "intf-dropcnt": "0",
                            },
                            {
                                "generation": "172",
                                "route-table": "0",
                                "address-family-flags": {
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "interface-address": {
                                    "ifa-flags": {
                                        "ifaf-is-default": True,
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True,
                                    },
                                    "ifa-destination": "10.0.0/24",
                                    "ifa-local": "10.0.0.1",
                                    "ifa-broadcast": "10.0.0.255",
                                    "generation": "164",
                                },
                            },
                            {
                                "address-family-name": "inet6",
                                "mtu": "1500",
                                "max-local-cache": "75000",
                                "new-hold-limit": "75000",
                                "intf-curr-cnt": "0",
                                "intf-unresolved-cnt": "0",
                                "intf-dropcnt": "0",
                            },
                            {
                                "generation": "173",
                                "route-table": "0",
                                "address-family-flags": {"ifff-is-primary": True},
                                "interface-address": {
                                    "ifa-flags": {
                                        "ifaf-is-default": True,
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True,
                                    },
                                    "ifa-destination": "2001:10::/64",
                                    "ifa-local": "2001:10::1",
                                },
                            },
                            {
                                "generation": "166",
                                "interface-address": {
                                    "ifa-flags": {"ifaf-is-preferred": True},
                                    "ifa-destination": "fe80::/64",
                                    "ifa-local": "fe80::2e6b:f5ff:fed6:f8c0",
                                },
                            },
                            {
                                "address-family-name": "multiservice",
                                "mtu": "Unlimited",
                                "generation": "168",
                            },
                            {
                                "generation": "174",
                                "route-table": "0",
                                "address-family-flags": {"ifff-is-primary": True},
                                "policer-information": {},
                            },
                        ],
                    }
                ],
            }
        ]
    }
}
