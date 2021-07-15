expected_output = {
    "interface-information": {
        "physical-interface": [
            {
                "name": "lo0",
                "oper-status": "Up",
                "admin-status": {"@junos:format": "Enabled"},
                "local-index": "6",
                "snmp-index": "6",
                "if-device-flags": {
                    "ifdf-present": True,
                    "ifdf-running": True,
                    "ifdf-loopback": True,
                },
                "if-config-flags": {"iff-snmp-traps": True},
                "if-media-flags": {"ifmf-none": True},
                "interface-flapped": {"#text": "Never"},
                "traffic-statistics": {
                    "input-packets": "8823688",
                    "output-packets": "8823688",
                },
                "logical-interface": [
                    {
                        "name": "lo0.16384",
                        "local-index": "321",
                        "snmp-index": "21",
                        "if-config-flags": {"iff-up": True, "iff-snmp-traps": True},
                        "traffic-statistics": {
                            "input-packets": "0",
                            "output-packets": "0",
                        },
                        "address-family": [],
                    },
                    {
                        "name": "lo0.16385",
                        "local-index": "320",
                        "snmp-index": "22",
                        "if-config-flags": {"iff-up": True, "iff-snmp-traps": True},
                        "traffic-statistics": {
                            "input-packets": "8821078",
                            "output-packets": "8821078",
                        },
                        "address-family": [],
                    },
                ],
            }
        ]
    }
}
