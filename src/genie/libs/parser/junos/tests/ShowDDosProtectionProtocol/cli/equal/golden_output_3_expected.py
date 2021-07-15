expected_output = {
    "ddos-protocols-information": {
        "total-packet-types": "1",
        "mod-packet-types": "0",
        "packet-types-rcvd-packets": "1",
        "packet-types-in-violation": "0",
        "flows-current": "0",
        "flows-cumulative": "0",
        "ddos-protocol-group": {
            "group-name": "RSVP",
            "ddos-protocol": {
                "packet-type": "aggregate",
                "packet-type-description": "Aggregate for all rsvp traffic",
                "ddos-basic-parameters": {
                    "policer-bandwidth": "20000",
                    "policer-burst": "20000",
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
                        "ifd-bandwidth": "20000",
                    },
                },
                "ddos-system-statistics": {
                    "packet-received": "580528875",
                    "packet-arrival-rate": "0",
                    "packet-dropped": "573259829",
                    "packet-arrival-rate-max": "1603269",
                },
                "ddos-instance": [
                    {
                        "protocol-states-locale": "Routing Engine",
                        "ddos-instance-statistics": {
                            "packet-received": "4780226",
                            "packet-arrival-rate": "0",
                            "packet-dropped": "0",
                            "packet-arrival-rate-max": "13927",
                        },
                        "ddos-instance-parameters": {
                            "policer-bandwidth": "20000",
                            "policer-burst": "20000",
                            "policer-enable": "enabled",
                        },
                    },
                    {
                        "protocol-states-locale": "FPC slot 0",
                        "ddos-instance-statistics": {
                            "packet-received": "580528875",
                            "packet-arrival-rate": "0",
                            "packet-dropped": "573259829",
                            "packet-arrival-rate-max": "1603269",
                        },
                        "ddos-instance-parameters": {
                            "policer-bandwidth-scale": "100",
                            "policer-bandwidth": "20000",
                            "policer-burst-scale": "100",
                            "policer-burst": "20000",
                            "policer-enable": "enabled",
                        },
                    },
                    {
                        "protocol-states-locale": "FPC slot 9",
                        "ddos-instance-statistics": {
                            "packet-received": "0",
                            "packet-arrival-rate": "0",
                            "packet-dropped": "0",
                            "packet-arrival-rate-max": "0",
                        },
                        "ddos-instance-parameters": {
                            "policer-bandwidth-scale": "100",
                            "policer-bandwidth": "20000",
                            "policer-burst-scale": "100",
                            "policer-burst": "20000",
                            "policer-enable": "enabled",
                        },
                    },
                ],
            },
        },
    }
}
