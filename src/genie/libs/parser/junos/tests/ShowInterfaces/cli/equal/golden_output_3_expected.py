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
                        "address-family": [],
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
                "oper-status": "Up",
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