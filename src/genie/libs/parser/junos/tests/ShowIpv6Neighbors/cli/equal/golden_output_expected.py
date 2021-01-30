expected_output = {
    "ipv6-nd-information": {
        "ipv6-nd-entry": [
            {
                "ipv6-nd-expire": "28",
                "ipv6-nd-interface-name": "ge-0/0/1.0",
                "ipv6-nd-isrouter": "yes",
                "ipv6-nd-issecure": "no",
                "ipv6-nd-neighbor-address": "2001:db8:eb18:6337::1",
                "ipv6-nd-neighbor-l2-address": "00:50:56:ff:00:4b",
                "ipv6-nd-state": "reachable",
            },
            {
                "ipv6-nd-expire": "4",
                "ipv6-nd-interface-name": "ge-0/0/0.0",
                "ipv6-nd-isrouter": "yes",
                "ipv6-nd-issecure": "no",
                "ipv6-nd-neighbor-address": "fe80::250:56ff:feff:e04e",
                "ipv6-nd-neighbor-l2-address": "00:50:56:ff:e0:4e",
                "ipv6-nd-state": "delay",
            },
            {
                "ipv6-nd-expire": "43",
                "ipv6-nd-interface-name": "ge-0/0/1.0",
                "ipv6-nd-isrouter": "yes",
                "ipv6-nd-issecure": "no",
                "ipv6-nd-neighbor-address": "fe80::250:56ff:feff:4b",
                "ipv6-nd-neighbor-l2-address": "00:50:56:ff:00:4b",
                "ipv6-nd-state": "reachable",
            },
        ],
        "ipv6-nd-total": "3",
    }
}
