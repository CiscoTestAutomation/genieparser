expected_output = {
    "slot": {
        "0": {
            "route-tables": {
                "CLNP": [
                    {"index": "Default", "routes": "1", "size": "136"},
                    {"index": "5", "routes": "1", "size": "136"},
                ],
                "DHCP-Snooping": [{"index": "Default", "routes": "1", "size": "136"}],
                "IPv4": [
                    {"index": "Default", "routes": "944", "size": "132156"},
                    {"index": "1", "routes": "9", "size": "1256"},
                    {"index": "2", "routes": "8", "size": "1116"},
                    {"index": "3", "routes": "5", "size": "696"},
                    {"index": "4", "routes": "9", "size": "1256"},
                    {"index": "5", "routes": "5", "size": "696"},
                    {"index": "36736", "routes": "5", "size": "696"},
                ],
                "IPv6": [
                    {"index": "Default", "routes": "39", "size": "5824"},
                    {"index": "1", "routes": "6", "size": "872"},
                    {"index": "5", "routes": "6", "size": "872"},
                ],
                "MPLS": [
                    {"index": "Default", "routes": "45", "size": "6296"},
                    {"index": "6", "routes": "1", "size": "136"},
                ],
            }
        }
    }
}
