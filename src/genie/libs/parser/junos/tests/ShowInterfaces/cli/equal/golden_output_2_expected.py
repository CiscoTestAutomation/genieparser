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
                "current-physical-address": "00:50:56:ff:56:b6",
                "description": "none/100G/in/hktGCS002_ge-0/0/0",
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
                    "input-packets": "133726908",
                    "input-reject-count": "118",
                    "input-reject-destination-address-count": "60",
                    "input-reject-source-address-count": "0",
                    "output-packet-error-count": "0",
                    "output-packet-pad-count": "0",
                    "output-packets": "129183361"
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
                    "input-total-errors": "0",
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
                    "output-total-errors": "0",
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
                                "address-family-name": "inet",
                                "intf-curr-cnt": "1",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-no-redirects": True,
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "generation": "160",
                                "interface-address": {
                                    "generation": "146",
                                    "ifa-broadcast": "10.189.5.95",
                                    "ifa-destination": "10.189.5.92/30",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "10.189.5.93"
                                },
                                "route-table": "0"
                            },
                            {
                                "address-family-name": "inet6",
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
                                "generation": "161",
                                "interface-address": {
                                    "ifa-destination": "2001:db8:223c:2c16::/64",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "2001:db8:223c:2c16::1"
                                },
                                "route-table": "0"
                            },
                            {
                                "generation": "148",
                                "interface-address": {
                                    "ifa-destination": "fe80::/64",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True
                                    },
                                    "ifa-local": "fe80::250:56ff:feff:56b6"
                                }
                            },
                            {
                                "address-family-name": "mpls",
                                "generation": "150",
                                "maximum-labels": "3",
                                "mtu": "1488"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "generation": "162",
                                "route-table": "0"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "address-family-name": "multiservice",
                                "generation": "163",
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
                "pfe-information": {
                    "destination-mask": "(0x00)",
                    "destination-slot": "0"
                },
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "526",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "statistics-cleared": "Never",
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
                },
                "up-hold-time": "2000"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                                "generation": "156",
                                "route-table": "1"
                            },
                            {
                                "address-family-name": "inet6",
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
                                "generation": "157",
                                "route-table": "1"
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                                "generation": "158",
                                "route-table": "1"
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
                                    "ifff-is-primary": True
                                },
                                "generation": "159",
                                "route-table": "2"
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
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
                "current-physical-address": "00:50:56:ff:37:f9",
                "description": "YW7079/9.6G/BB/sjkGDS221-EC11_xe-0/1/5[SJC]_Area8_Cost100",
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
                    "input-packets": "376916499",
                    "input-reject-count": "41",
                    "input-reject-destination-address-count": "4",
                    "input-reject-source-address-count": "0",
                    "output-packet-error-count": "0",
                    "output-packet-pad-count": "0",
                    "output-packets": "370414722"
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
                    "input-total-errors": "0",
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
                    "output-total-errors": "0",
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
                                "address-family-name": "inet",
                                "intf-curr-cnt": "1",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-no-redirects": True,
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "generation": "164",
                                "interface-address": {
                                    "generation": "152",
                                    "ifa-broadcast": "10.169.14.123",
                                    "ifa-destination": "10.169.14.120/30",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "10.169.14.122"
                                },
                                "route-table": "0"
                            },
                            {
                                "address-family-name": "inet6",
                                "intf-curr-cnt": "2",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "generation": "165",
                                "interface-address": {
                                    "ifa-destination": "2001:db8:eb18:6337::/64",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "2001:db8:eb18:6337::2"
                                },
                                "route-table": "0"
                            },
                            {
                                "generation": "154",
                                "interface-address": {
                                    "ifa-destination": "fe80::/64",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True
                                    },
                                    "ifa-local": "fe80::250:56ff:feff:37f9"
                                }
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
                            },
                            {
                                "generation": "167",
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
                "pfe-information": {
                    "destination-mask": "(0x00)",
                    "destination-slot": "0"
                },
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "527",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "statistics-cleared": "Never",
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
                },
                "up-hold-time": "2000"
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
                "current-physical-address": "00:50:56:ff:1e:ba",
                "description": "ve-hkgasr01_Gi2[DefaultCost1000]",
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
                    "input-packets": "252983783",
                    "input-reject-count": "335972",
                    "input-reject-destination-address-count": "0",
                    "input-reject-source-address-count": "0",
                    "output-packet-error-count": "0",
                    "output-packet-pad-count": "0",
                    "output-packets": "229070540"
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
                    "input-total-errors": "0",
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
                    "output-total-errors": "0",
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
                                "address-family-name": "inet",
                                "intf-curr-cnt": "1",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "generation": "179",
                                "interface-address": {
                                    "generation": "166",
                                    "ifa-broadcast": "10.19.198.27",
                                    "ifa-destination": "10.19.198.24/30",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "10.19.198.25"
                                },
                                "route-table": "0"
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
                "pfe-information": {
                    "destination-mask": "(0x00)",
                    "destination-slot": "0"
                },
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "528",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "statistics-cleared": "Never",
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
                },
                "up-hold-time": "2000"
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
                "current-physical-address": "00:50:56:ff:93:cb",
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
                    "input-packets": "14683",
                    "input-reject-count": "65",
                    "input-reject-destination-address-count": "0",
                    "input-reject-source-address-count": "0",
                    "output-packet-error-count": "0",
                    "output-packet-pad-count": "0",
                    "output-packets": "17425"
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
                    "input-total-errors": "0",
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
                    "output-total-errors": "0",
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
                                "address-family-name": "inet",
                                "intf-curr-cnt": "1",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "generation": "174",
                                "interface-address": {
                                    "generation": "162",
                                    "ifa-broadcast": "10.55.0.255",
                                    "ifa-destination": "100.0.0/24",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "10.55.0.254"
                                },
                                "route-table": "0"
                            },
                            {
                                "address-family-name": "multiservice",
                                "generation": "175",
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
                "pfe-information": {
                    "destination-mask": "(0x00)",
                    "destination-slot": "0"
                },
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "529",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "statistics-cleared": "Never",
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
                },
                "up-hold-time": "0"
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
                "current-physical-address": "00:50:56:ff:3e:28",
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
                    "input-packets": "0",
                    "input-reject-count": "0",
                    "input-reject-destination-address-count": "0",
                    "input-reject-source-address-count": "0",
                    "output-packet-error-count": "0",
                    "output-packet-pad-count": "0",
                    "output-packets": "0"
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
                    "input-total-errors": "0",
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
                    "output-total-errors": "0",
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
                "pfe-information": {
                    "destination-mask": "(0x00)",
                    "destination-slot": "0"
                },
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "530",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "statistics-cleared": "Never",
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
                },
                "up-hold-time": "0"
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
                "current-physical-address": "2c:6b:f5:ff:01:1d",
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
                    "input-packets": "0",
                    "input-reject-count": "0",
                    "input-reject-destination-address-count": "0",
                    "input-reject-source-address-count": "0",
                    "output-packet-error-count": "0",
                    "output-packet-pad-count": "0",
                    "output-packets": "0"
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
                    "input-total-errors": "0",
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
                    "output-total-errors": "0",
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
                "pfe-information": {
                    "destination-mask": "(0x00)",
                    "destination-slot": "0"
                },
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "531",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "statistics-cleared": "Never",
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
                },
                "up-hold-time": "0"
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
                "current-physical-address": "2c:6b:f5:ff:01:1e",
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
                    "input-packets": "0",
                    "input-reject-count": "0",
                    "input-reject-destination-address-count": "0",
                    "input-reject-source-address-count": "0",
                    "output-packet-error-count": "0",
                    "output-packet-pad-count": "0",
                    "output-packets": "0"
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
                    "input-total-errors": "0",
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
                    "output-total-errors": "0",
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
                "pfe-information": {
                    "destination-mask": "(0x00)",
                    "destination-slot": "0"
                },
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "532",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "statistics-cleared": "Never",
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
                },
                "up-hold-time": "0"
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
                "current-physical-address": "2c:6b:f5:ff:01:1f",
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
                    "input-packets": "0",
                    "input-reject-count": "0",
                    "input-reject-destination-address-count": "0",
                    "input-reject-source-address-count": "0",
                    "output-packet-error-count": "0",
                    "output-packet-pad-count": "0",
                    "output-packets": "0"
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
                    "input-total-errors": "0",
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
                    "output-total-errors": "0",
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
                "pfe-information": {
                    "destination-mask": "(0x00)",
                    "destination-slot": "0"
                },
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "533",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "statistics-cleared": "Never",
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
                },
                "up-hold-time": "0"
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
                "current-physical-address": "2c:6b:f5:ff:01:20",
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
                    "input-packets": "0",
                    "input-reject-count": "0",
                    "input-reject-destination-address-count": "0",
                    "input-reject-source-address-count": "0",
                    "output-packet-error-count": "0",
                    "output-packet-pad-count": "0",
                    "output-packets": "0"
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
                    "input-total-errors": "0",
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
                    "output-total-errors": "0",
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
                "pfe-information": {
                    "destination-mask": "(0x00)",
                    "destination-slot": "0"
                },
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "534",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "statistics-cleared": "Never",
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
                },
                "up-hold-time": "0"
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
                "current-physical-address": "2c:6b:f5:ff:01:21",
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
                    "input-packets": "0",
                    "input-reject-count": "0",
                    "input-reject-destination-address-count": "0",
                    "input-reject-source-address-count": "0",
                    "output-packet-error-count": "0",
                    "output-packet-pad-count": "0",
                    "output-packets": "0"
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
                    "input-total-errors": "0",
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
                    "output-total-errors": "0",
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
                "pfe-information": {
                    "destination-mask": "(0x00)",
                    "destination-slot": "0"
                },
                "physical-interface-cos-information": {
                    "physical-interface-cos-hw-max-queues": "8",
                    "physical-interface-cos-use-max-queues": "8"
                },
                "snmp-index": "535",
                "sonet-mode": "LAN-PHY",
                "source-filtering": "Disabled",
                "speed": "1000mbps",
                "statistics-cleared": "Never",
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
                },
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                                "generation": "133",
                                "interface-address": [
                                    {
                                        "generation": "133",
                                        "ifa-broadcast": "Unspecified",
                                        "ifa-destination": "Unspecified",
                                        "ifa-flags": {
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "10.1.0.101"
                                    },
                                    {
                                        "generation": "165",
                                        "ifa-broadcast": "Unspecified",
                                        "ifa-destination": "Unspecified",
                                        "ifa-flags": {
                                            "ifaf-none": True
                                        },
                                        "ifa-local": "10.19.198.25"
                                    },
                                    {
                                        "generation": "161",
                                        "ifa-broadcast": "Unspecified",
                                        "ifa-destination": "Unspecified",
                                        "ifa-flags": {
                                            "ifaf-none": True
                                        },
                                        "ifa-local": "10.55.0.254"
                                    },
                                    {
                                        "generation": "151",
                                        "ifa-broadcast": "Unspecified",
                                        "ifa-destination": "Unspecified",
                                        "ifa-flags": {
                                            "ifaf-none": True
                                        },
                                        "ifa-local": "10.169.14.122"
                                    },
                                    {
                                        "generation": "145",
                                        "ifa-broadcast": "Unspecified",
                                        "ifa-destination": "Unspecified",
                                        "ifa-flags": {
                                            "ifaf-none": True
                                        },
                                        "ifa-local": "10.189.5.93"
                                    },
                                    {
                                        "generation": "134",
                                        "ifa-broadcast": "Unspecified",
                                        "ifa-destination": "Unspecified",
                                        "ifa-flags": {
                                            "ifaf-none": True
                                        },
                                        "ifa-local": "10.189.5.252"
                                    }
                                ],
                                "route-table": "0"
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
                                "address-family-name": "inet6",
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
                                "generation": "130",
                                "interface-address": {
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-none": True
                                    },
                                    "ifa-local": "2001:db8:eb18:6337::2"
                                },
                                "route-table": "0"
                            },
                            {
                                "generation": "153",
                                "interface-address": {
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-none": True
                                    },
                                    "ifa-local": "2001:db8:223c:ca45::b"
                                }
                            },
                            {
                                "generation": "136",
                                "interface-address": {
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-none": True
                                    },
                                    "ifa-local": "2001:db8:223c:2c16::1"
                                }
                            },
                            {
                                "generation": "147",
                                "interface-address": {
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-none": True
                                    },
                                    "ifa-local": "fe80::250:560f:fc8d:7c08"
                                }
                            },
                            {
                                "generation": "138",
                                "interface-address": {
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-none": True
                                    },
                                    "ifa-local": "fe80::250:56ff:feff:37f9"
                                }
                            },
                            {
                                "generation": "155",
                                "interface-address": {
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-none": True
                                    },
                                    "ifa-local": "fe80::250:56ff:feff:56b6"
                                }
                            },
                            {
                                "address-family-name": "mpls",
                                "generation": "149",
                                "maximum-labels": "3",
                                "mtu": "Unlimited"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-none": True
                                },
                                "generation": "137",
                                "route-table": "0"
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
                                "generation": "134",
                                "interface-address": [
                                    {
                                        "generation": "130",
                                        "ifa-broadcast": "Unspecified",
                                        "ifa-destination": "Unspecified",
                                        "ifa-flags": {
                                            "ifaf-is-primary": True
                                        },
                                        "ifa-local": "10.0.0.4"
                                    },
                                    {
                                        "generation": "142",
                                        "ifa-broadcast": "Unspecified",
                                        "ifa-destination": "Unspecified",
                                        "ifa-flags": {
                                            "ifaf-none": True
                                        },
                                        "ifa-local": "172.16.64.1"
                                    },
                                    {
                                        "generation": "129",
                                        "ifa-broadcast": "Unspecified",
                                        "ifa-destination": "Unspecified",
                                        "ifa-flags": {
                                            "ifaf-none": True
                                        },
                                        "ifa-local": "172.16.64.4"
                                    }
                                ],
                                "route-table": "1"
                            },
                            {
                                "address-family-name": "inet6",
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
                                "generation": "131",
                                "interface-address": {
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-none": True
                                    },
                                    "ifa-local": "fe80::250:56ff:feff:e2c1"
                                },
                                "route-table": "1"
                            },
                            {
                                "generation": "131",
                                "interface-address": {
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-none": True
                                    },
                                    "ifa-local": "2001:db8:8d82::a:0:0:4"
                                }
                            },
                            {
                                "address-family-name": "vpls",
                                "generation": "132",
                                "mtu": "Unlimited"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-none": True
                                },
                                "generation": "138",
                                "route-table": "1"
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
                                "generation": "135",
                                "interface-address": {
                                    "generation": "140",
                                    "ifa-broadcast": "Unspecified",
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "127.0.0.1"
                                },
                                "route-table": "2"
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
                                "generation": "147",
                                "route-table": "3"
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
                                "generation": "148",
                                "interface-address": {
                                    "generation": "143",
                                    "ifa-broadcast": "Unspecified",
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "172.16.64.127"
                                },
                                "route-table": "4"
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
                                "generation": "150",
                                "route-table": "5"
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
                                "address-family-name": "inet6",
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
                                "generation": "153",
                                "route-table": "5"
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
                                "generation": "136",
                                "route-table": "36736"
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "2c:6b:f5:ff:01:29",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "00:50:56:ff:e2:c1",
                "down-hold-time": "0",
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
                                "address-family-name": "inet",
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
                                "generation": "139",
                                "interface-address": [
                                    {
                                        "generation": "2",
                                        "ifa-broadcast": "10.255.255.255",
                                        "ifa-destination": "10/8",
                                        "ifa-flags": {
                                            "ifaf-is-preferred": True
                                        },
                                        "ifa-local": "10.0.0.4"
                                    },
                                    {
                                        "generation": "7",
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
                                        "generation": "1",
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
                                "route-table": "1"
                            },
                            {
                                "address-family-name": "inet6",
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
                                "generation": "140",
                                "interface-address": {
                                    "ifa-destination": "fe80::/64",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True
                                    },
                                    "ifa-local": "fe80::250:56ff:feff:e2c1"
                                },
                                "route-table": "1"
                            },
                            {
                                "generation": "3",
                                "interface-address": {
                                    "ifa-destination": "2001:db8:8d82::/64",
                                    "ifa-flags": {
                                        "ifaf-is-default": True,
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "2001:db8:8d82::a:0:0:4"
                                }
                            },
                            {
                                "address-family-name": "tnp",
                                "generation": "4",
                                "mtu": "1500"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True,
                                    "ifff-primary": True
                                },
                                "generation": "141",
                                "interface-address": {
                                    "generation": "5",
                                    "ifa-broadcast": "Unspecified",
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-none": True
                                    },
                                    "ifa-local": "0x4"
                                },
                                "route-table": "1"
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "00:50:56:ff:0a:95",
                "down-hold-time": "0",
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
                                "address-family-name": "inet",
                                "intf-curr-cnt": "2",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1500",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True,
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "generation": "142",
                                "interface-address": {
                                    "generation": "6",
                                    "ifa-broadcast": "10.1.0.255",
                                    "ifa-destination": "1.0.0/24",
                                    "ifa-flags": {
                                        "ifaf-is-preferred": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "10.1.0.101"
                                },
                                "route-table": "0"
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "2c:6b:f5:ff:08:09",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "2c:6b:f5:ff:08:d8",
                "down-hold-time": "0",
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
                                "address-family-name": "inet",
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "75000",
                                "mtu": "1514",
                                "new-hold-limit": "75000"
                            },
                            {
                                "address-family-flags": {
                                    "ifff-is-primary": True
                                },
                                "generation": "149",
                                "interface-address": {
                                    "generation": "144",
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
                                "route-table": "4"
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                                    "ifff-no-redirects": True,
                                    "ifff-sendbcast-pkt-to-re": True
                                },
                                "generation": "143",
                                "interface-address": {
                                    "generation": "135",
                                    "ifa-broadcast": "Unspecified",
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-is-default": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "10.189.5.252"
                                },
                                "route-table": "0"
                            },
                            {
                                "address-family-name": "inet6",
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "0",
                                "mtu": "Unlimited",
                                "new-hold-limit": "0"
                            },
                            {
                                "generation": "144",
                                "interface-address": {
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-is-default": True,
                                        "ifaf-is-primary": True
                                    },
                                    "ifa-local": "fe80::250:560f:fc8d:7c08"
                                },
                                "route-table": "0"
                            },
                            {
                                "generation": "137"
                            },
                            {
                                "generation": "139"
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
                                "intf-curr-cnt": "0",
                                "intf-dropcnt": "0",
                                "intf-unresolved-cnt": "0",
                                "max-local-cache": "0",
                                "mtu": "Unlimited",
                                "new-hold-limit": "0"
                            },
                            {
                                "generation": "146",
                                "interface-address": {
                                    "generation": "141",
                                    "ifa-broadcast": "Unspecified",
                                    "ifa-destination": "Unspecified",
                                    "ifa-flags": {
                                        "ifaf-none": True
                                    },
                                    "ifa-local": "127.0.0.1"
                                },
                                "route-table": "2"
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
                            },
                            {
                                "generation": "145",
                                "route-table": "1"
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
                "statistics-cleared": "Never",
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
                },
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "2c:6b:f5:ff:08:c8",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "speed": "Unspecified",
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            },
            {
                "admin-status": {
                    "@junos:format": "Enabled"
                },
                "current-physical-address": "Unspecified",
                "down-hold-time": "0",
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
                "statistics-cleared": "Never",
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
                "up-hold-time": "0"
            }
        ]
    }
}
