expected_output = {
    "lacp-interface-information-list": {
        "lacp-interface-information": {
            "lag-lacp-header": {"aggregate-name": "ae4"},
            "lag-lacp-protocol": [
                {
                    "lacp-mux-state": "Collecting distributing",
                    "lacp-receive-state": "Current",
                    "lacp-transmit-state": "Fast periodic",
                    "name": "xe-3/0/1",
                }
            ],
            "lag-lacp-state": [
                {
                    "lacp-activity": "Active",
                    "lacp-aggregation": "Yes",
                    "lacp-collecting": "Yes",
                    "lacp-defaulted": "No",
                    "lacp-distributing": "Yes",
                    "lacp-expired": "No",
                    "lacp-role": "Actor",
                    "lacp-synchronization": "Yes",
                    "lacp-timeout": "Fast",
                    "name": "xe-3/0/1",
                },
                {
                    "lacp-activity": "Active",
                    "lacp-aggregation": "Yes",
                    "lacp-collecting": "Yes",
                    "lacp-defaulted": "No",
                    "lacp-distributing": "Yes",
                    "lacp-expired": "No",
                    "lacp-role": "Partner",
                    "lacp-synchronization": "Yes",
                    "lacp-timeout": "Fast",
                    "name": "xe-3/0/1",
                },
            ],
        }
    }
}
