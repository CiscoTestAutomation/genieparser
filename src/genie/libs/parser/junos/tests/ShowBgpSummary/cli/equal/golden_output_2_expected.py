expected_output = {
    "bgp-information": {
        "bgp-peer": [
            {
                "elapsed-time": {
                    "#text": "9"
                },
                "flap-count": "1",
                "input-messages": "2",
                "output-messages": "3",
                "peer-address": "10.145.0.2",
                "peer-as": "3",
                "peer-state": "0/0/0/0              0/0/0/0",
                "route-queue-count": "0"
            },
            {
                "bgp-rib": [
                    {
                        "accepted-prefix-count": "0",
                        "active-prefix-count": "0",
                        "name": "inet6.0",
                        "received-prefix-count": "0",
                        "suppressed-prefix-count": "0"
                    }
                ],
                "elapsed-time": {
                    "#text": "5"
                },
                "flap-count": "1",
                "input-messages": "2",
                "output-messages": "3",
                "peer-address": "2001:20::2",
                "peer-as": "3",
                "peer-state": "Establ",
                "route-queue-count": "0"
            }
        ],
        "bgp-rib": [
            {
                "active-prefix-count": "0",
                "damped-prefix-count": "0",
                "history-prefix-count": "0",
                "name": "inet.0",
                "pending-prefix-count": "0",
                "suppressed-prefix-count": "0",
                "total-prefix-count": "0"
            },
            {
                "active-prefix-count": "0",
                "damped-prefix-count": "0",
                "history-prefix-count": "0",
                "name": "inet6.0",
                "pending-prefix-count": "0",
                "suppressed-prefix-count": "0",
                "total-prefix-count": "0"
            }
        ],
        "down-peer-count": "0",
        "group-count": "2",
        "peer-count": "2"
    }
}