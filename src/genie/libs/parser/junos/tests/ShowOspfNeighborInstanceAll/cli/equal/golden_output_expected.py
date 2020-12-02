expected_output = {
    "ospf-neighbor-information-all": {
        "ospf-instance-neighbor": {
            "ospf-instance-name": "master",
            "ospf-neighbor": [
                {
                    "neighbor-address": "10.189.5.94",
                    "interface-name": "ge-0/0/0.0",
                    "ospf-neighbor-state": "Full",
                    "neighbor-id": "10.189.5.253",
                    "neighbor-priority": "128",
                    "activity-timer": "32",
                },
                {
                    "neighbor-address": "10.169.14.121",
                    "interface-name": "ge-0/0/1.0",
                    "ospf-neighbor-state": "Full",
                    "neighbor-id": "10.169.14.240",
                    "neighbor-priority": "128",
                    "activity-timer": "33",
                },
                {
                    "neighbor-address": "10.19.198.26",
                    "interface-name": "ge-0/0/2.0",
                    "ospf-neighbor-state": "Full",
                    "neighbor-id": "10.19.198.239",
                    "neighbor-priority": "1",
                    "activity-timer": "33",
                },
            ],
        }
    }
}
