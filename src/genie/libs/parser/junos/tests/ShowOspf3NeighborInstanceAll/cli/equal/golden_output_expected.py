expected_output = {
    "ospf3-neighbor-information-all": {
        "ospf3-instance-neighbor": {
            "ospf3-instance-name": "master",
            "ospf3-realm-neighbor": {
                "ospf3-realm-name": "ipv6-unicast",
                "ospf3-neighbor": [
                    {
                        "interface-name": "ge-0/0/0.0",
                        "ospf-neighbor-state": "Full",
                        "neighbor-id": "10.16.2.2",
                        "neighbor-priority": "128",
                        "activity-timer": "32",
                        "neighbor-address": "fe80::250:56ff:fe8d:c305",
                    },
                    {
                        "interface-name": "ge-0/0/1.0",
                        "ospf-neighbor-state": "Full",
                        "neighbor-id": "10.36.3.3",
                        "neighbor-priority": "128",
                        "activity-timer": "32",
                        "neighbor-address": "fe80::250:56ff:fe8d:fe22",
                    },
                    {
                        "interface-name": "ge-0/0/2.0",
                        "ospf-neighbor-state": "Full",
                        "neighbor-id": "10.16.2.2",
                        "neighbor-priority": "128",
                        "activity-timer": "35",
                        "neighbor-address": "fe80::250:56ff:fe8d:54f2",
                    },
                    {
                        "interface-name": "ge-0/0/3.0",
                        "ospf-neighbor-state": "Full",
                        "neighbor-id": "172.16.81.1",
                        "neighbor-priority": "0",
                        "activity-timer": "38",
                        "neighbor-address": "fe80::200:23ff:fed6:9656",
                    },
                ],
            },
        }
    }
}
