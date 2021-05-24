expected_output = {
    "ddos-protocols-information": {
        "flows-current": "0",
        "flows-cumulative": "0",
        "ddos-protocol-group": {
            "group-name": "Unclassified",
            "ddos-protocol": {
                "packet-type": "host-route-v4",
                "packet-type-description": "unclassified v4 hostbound packets",
                "ddos-basic-parameters": {
                    "policer-bandwidth": "2000",
                    "policer-burst": "10000",
                    "policer-time-recover": "300",
                    "policer-enable": "Yes",
                },
                "ddos-flow-detection": {
                    "detection-mode": "Automatic",
                    "detect-time": "3",
                    "log-flows": "Yes",
                    "recover-time": "60",
                    "timeout-active-flows": "No",
                    "timeout-time": "300",
                    "flow-aggregation-level-states": {
                        "sub-detection-mode": "Automatic",
                        "sub-control-mode": "Drop",
                        "sub-bandwidth": "10",
                        "ifl-detection-mode": "Automatic",
                        "ifl-control-mode": "Drop",
                        "ifl-bandwidth": "10",
                        "ifd-detection-mode": "Automatic",
                        "ifd-control-mode": "Drop",
                        "ifd-bandwidth": "2000",
                    },
                },
                "ddos-system-statistics": {
                    "packet-received": "3",
                    "packet-arrival-rate": "0",
                    "packet-dropped": "0",
                    "packet-arrival-rate-max": "0",
                },
                "ddos-instance": [
                    {
                        "protocol-states-locale": "Routing Engine",
                        "ddos-instance-statistics": {
                            "packet-received": "3",
                            "packet-arrival-rate": "0",
                            "packet-dropped": "0",
                            "packet-arrival-rate-max": "0",
                        },
                        "ddos-instance-parameters": {
                            "policer-bandwidth": "2000",
                            "policer-burst": "10000",
                            "policer-enable": "enabled",
                        },
                    },
                    {
                        "protocol-states-locale": "FPC slot 0",
                        "ddos-instance-statistics": {
                            "packet-received": "3",
                            "packet-arrival-rate": "0",
                            "packet-dropped": "0",
                            "packet-arrival-rate-max": "0",
                        },
                        "ddos-instance-parameters": {
                            "policer-bandwidth-scale": "100",
                            "policer-bandwidth": "2000",
                            "policer-burst-scale": "100",
                            "policer-burst": "10000",
                            "policer-enable": "enabled",
                        },
                    },
                ],
            },
        },
    }
}
