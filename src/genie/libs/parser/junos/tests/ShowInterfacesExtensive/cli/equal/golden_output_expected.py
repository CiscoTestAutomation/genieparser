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
                "cos-information": {
                    "cos-stream-information": {
                        "cos-direction": "Output",
                        "cos-queue-configuration": [
                            {
                                "cos-queue-bandwidth": "95",
                                "cos-queue-bandwidth-bps": "950000000",
                                "cos-queue-buffer": "95",
                                "cos-queue-buffer-bytes": "0",
                                "cos-queue-forwarding-class": "best-effort",
                                "cos-queue-limit": "none",
                                "cos-queue-number": "0",
                                "cos-queue-priority": "low"
                            },
                            {
                                "cos-queue-bandwidth": "5",
                                "cos-queue-bandwidth-bps": "50000000",
                                "cos-queue-buffer": "5",
                                "cos-queue-buffer-bytes": "0",
                                "cos-queue-forwarding-class": "network-control",
                                "cos-queue-limit": "none",
                                "cos-queue-number": "3",
                                "cos-queue-priority": "low"
                            }
                        ]
                    }
                },
                "current-physical-address": "00:50:56:ff:55:26",
                "down-hold-time": "0",
                "eth-switch-error": "None",
                "ethernet-fec-statistics": {
                    "fec_ccw_count": "0",
                    "fec_ccw_error_rate": "0",
                    "fec_nccw_count": "0",
                    "fec_nccw_error_rate": "0"
                },
                "ethernet-filter-statistics": {
                    "cam-destination-filter-count": "0",
                    "cam-source-filter-count": "0",
                    "input-packets": "27",
                    "input-reject-count": "22",
                    "input-reject-destination-address-count": "0",
                    "input-reject-source-address-count": "0",
                    "output-packet-error-count": "0",
                    "output-packet-pad-count": "0",
                    "output-packets": "6"
                },
                "ethernet-mac-statistics": {
                    "input-broadcasts": "0",
                    "input-bytes": "2230",
                    "input-code-violations": "0",
                    "input-crc-errors": "0",
                    "input-fifo-errors": "0",
                    "input-fragment-frames": "0",
                    "input-jabber-frames": "0",
                    "input-mac-control-frames": "0",
                    "input-mac-pause-frames": "0",
                    "input-multicasts": "0",
                    "input-oversized-frames": "0",
                    "input-packets": "12",
                    "input-total-errors": "0",
                    "input-unicasts": "27",
                    "input-vlan-tagged-frames": "0",
                    "output-broadcasts": "0",
                    "output-bytes": "404",
                    "output-crc-errors": "0",
                    "output-fifo-errors": "0",
                    "output-mac-control-frames": "0",
                    "output-mac-pause-frames": "0",
                    "output-multicasts": "0",
                    "output-packets": "2",
                    "output-total-errors": "0",
                    "output-unicasts": "6"
                },
                "ethernet-pcs-statistics": {
                    "bit-error-seconds": "0",
                    "errored-blocks-seconds": "0"
                },
                "hardware-physical-address": "00:50:56:ff:55:26",
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
                    "#text": "2020-08-05 02:58:37 UTC (03:17:16 ago)"
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
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "address-family-name": "inet",
                                "generation": "82967",
                                "interface-address": {
                                    "generation": "172354",
                                    "ifa-broadcast": "10.145.0.255",
                                    "ifa-destination": "20.0.0/24",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "10.145.0.1"
                                },
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000",
                                "route-table": "0"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "address-family-name": "inet6",
                                "generation": "172356",
                                "interface-address": [
                                    {
                                        "ifa-destination": "2001:20::/64",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "2001:20::1"
                                    },
                                    {
                                        "ifa-destination": "fe80::/64",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True
                                        },
                                        "ifa-local": "fe80::250:56ff:feff:5526"
                                    }
                                ],
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000",
                                "route-table": "0"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "address-family-name": "inet6",
                                "generation": "172356",
                                "interface-address": [
                                    {
                                        "ifa-destination": "2001:20::/64",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True,
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "2001:20::1"
                                    },
                                    {
                                        "ifa-destination": "fe80::/64",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True
                                        },
                                        "ifa-local": "fe80::250:56ff:feff:5526"
                                    }
                                ],
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000",
                                "route-table": "0"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "address-family-name": "multiservice",
                                "generation": "82969",
                                "mtu": "Unlimited",
                                "policer-information": {},
                                "route-table": "0"
                            }
                        ],
                        "encapsulation": "ENET2",
                        "if-config-flags": {
                            "iff-snmp-traps": True,
                            "iff-up": True,
                            "internal-flags": "0x4004000"
                        },
                        "local-index": "332",
                        "name": "ge-0/0/0.0",
                        "snmp-index": "537",
                        "traffic-statistics": {
                            "input-bytes": "1900",
                            "input-packets": "26",
                            "ipv6-transit-statistics": {
                                "input-bytes": "0",
                                "input-packets": "0",
                                "output-bytes": "606",
                                "output-packets": "7"
                            },
                            "output-bytes": "606",
                            "output-packets": "7"
                        },
                        "transit-traffic-statistics": {
                            "input-bps": "3912",
                            "input-bytes": "1900",
                            "input-packets": "26",
                            "input-pps": "6",
                            "ipv6-transit-statistics": {
                                "input-bps": "504",
                                "input-bytes": "256",
                                "input-packets": "4",
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
                "loopback": "Disabled",
                "mru": "1522",
                "mtu": "1514",
                "name": "ge-0/0/0",
                "oper-status": "Up",
                "output-error-list": {
                    "aged-packets": "0",
                    "carrier-transitions": "0",
                    "hs-link-crc-errors": "0",
                    "mtu-errors": "0",
                    "output-collisions": "0",
                    "output-drops": "0",
                    "output-errors": "0",
                    "output-fifo-errors": "0",
                    "output-resource-errors": "0"
                },
                "pad-to-minimum-frame-size": "Disabled",
                "pfe-information": {
                    "destination-mask": "(0x00)",
                    "destination-slot": "0"
                },
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "queue-counters": {
                    "interface-cos-short-summary": {
                        "intf-cos-num-queues-in-use": "4",
                        "intf-cos-num-queues-supported": "8",
                        "intf-cos-queue-type": "Egress queues"
                    },
                    "queue": [
                        {
                            "forwarding-class-name": "best-effort",
                            "queue-counters-queued-packets": "0",
                            "queue-counters-total-drop-packets": "0",
                            "queue-counters-trans-packets": "0",
                            "queue-number": "0"
                        },
                        {
                            "forwarding-class-name": "expedited-forwarding",
                            "queue-counters-queued-packets": "0",
                            "queue-counters-total-drop-packets": "0",
                            "queue-counters-trans-packets": "0",
                            "queue-number": "1"
                        },
                        {
                            "forwarding-class-name": "assured-forwarding",
                            "queue-counters-queued-packets": "0",
                            "queue-counters-total-drop-packets": "0",
                            "queue-counters-trans-packets": "0",
                            "queue-number": "2"
                        },
                        {
                            "forwarding-class-name": "network-control",
                            "queue-counters-queued-packets": "2",
                            "queue-counters-total-drop-packets": "0",
                            "queue-counters-trans-packets": "2",
                            "queue-number": "3"
                        }
                    ]
                },
                "snmp-index": "526",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "statistics-cleared": "2020-08-05 06:15:50 UTC (00:00:03 ago)",
                "stp-traffic-statistics": {
                    "stp-input-bytes-dropped": "0",
                    "stp-input-packets-dropped": "0",
                    "stp-output-bytes-dropped": "0",
                    "stp-output-packets-dropped": "0"
                },
                "traffic-statistics": {
                    "input-bps": "3912",
                    "input-bytes": "1900",
                    "input-packets": "26",
                    "input-pps": "6",
                    "ipv6-transit-statistics": {
                        "input-bytes": "256",
                        "input-packets": "4",
                        "output-bytes": "0",
                        "output-packets": "0"
                    },
                    "output-bps": "1544",
                    "output-bytes": "648",
                    "output-packets": "7",
                    "output-pps": "2"
                },
                "up-hold-time": "0"
            }
        ]
    }
}