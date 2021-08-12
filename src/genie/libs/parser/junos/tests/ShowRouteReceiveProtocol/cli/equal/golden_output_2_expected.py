expected_output = {
    "route-information": {
        "route-table": [
            {
                "active-route-count": "24",
                "destination-count": "24",
                "hidden-route-count": "0",
                "holddown-route-count": "0",
                "rt": [
                    {
                        "rt-destination": "2001:db8:7fc5:ca45::1/128",
                        "rt-entry": {
                            "as-path": "I",
                            "local-preference": "100",
                            "med": "2",
                            "nh": {"to": "2001:db8:7fc5:ca45::4"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:7fc5:ca45::2/128",
                        "rt-entry": {
                            "as-path": "I",
                            "local-preference": "100",
                            "med": "1",
                            "nh": {"to": "2001:db8:7fc5:ca45::4"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:7fc5:ca45::3/128",
                        "rt-entry": {
                            "as-path": "I",
                            "local-preference": "100",
                            "med": "1",
                            "nh": {"to": "2001:db8:7fc5:ca45::4"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:7fc5:ca45::4/128",
                        "rt-entry": {
                            "as-path": "I",
                            "local-preference": "100",
                            "nh": {"to": "2001:db8:7fc5:ca45::4"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:7fc5:ca45::5/128",
                        "rt-entry": {
                            "as-path": "I",
                            "local-preference": "100",
                            "med": "3",
                            "nh": {"to": "2001:db8:7fc5:ca45::4"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:7fc5:d3e9::/64",
                        "rt-entry": {
                            "as-path": "I",
                            "local-preference": "100",
                            "med": "2",
                            "nh": {"to": "2001:db8:7fc5:ca45::4"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:7fc5:d8be::/64",
                        "rt-entry": {
                            "as-path": "I",
                            "local-preference": "100",
                            "med": "2",
                            "nh": {"to": "2001:db8:7fc5:ca45::4"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:7fc5:dd95::/64",
                        "rt-entry": {
                            "as-path": "I",
                            "local-preference": "100",
                            "nh": {"to": "2001:db8:7fc5:ca45::4"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:7fc5:e26e::/64",
                        "rt-entry": {
                            "as-path": "I",
                            "local-preference": "100",
                            "nh": {"to": "2001:db8:7fc5:ca45::4"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:7fc5:e749::/64",
                        "rt-entry": {
                            "as-path": "I",
                            "local-preference": "100",
                            "med": "3",
                            "nh": {"to": "2001:db8:7fc5:ca45::4"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:7fc5:9a4b::2/128",
                        "rt-entry": {
                            "as-path": "I",
                            "local-preference": "100",
                            "nh": {"to": "2001:db8:7fc5:ca45::2"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:7fc5:9a4b::3/128",
                        "rt-entry": {
                            "as-path": "I",
                            "local-preference": "100",
                            "nh": {"to": "2001:db8:7fc5:ca45::3"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:7fc5:9a4b::4/128",
                        "rt-entry": {
                            "active-tag": "*",
                            "as-path": "I",
                            "local-preference": "100",
                            "nh": {"to": "2001:db8:7fc5:ca45::4"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:22::/48",
                        "rt-entry": {
                            "active-tag": "*",
                            "as-path": "65509 I",
                            "med": "1000",
                            "nh": {"to": "2001:db8:7fc5:ca45::2"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:a280::/48",
                        "rt-entry": {
                            "active-tag": "*",
                            "as-path": "65509 I",
                            "med": "1000",
                            "nh": {"to": "2001:db8:7fc5:ca45::2"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:6880::/48",
                        "rt-entry": {
                            "active-tag": "*",
                            "as-path": "65509 I",
                            "local-preference": "100",
                            "med": "1000",
                            "nh": {"to": "2001:db8:7fc5:ca45::2"},
                            "protocol-name": "BGP",
                        },
                    },
                    {
                        "rt-destination": "2001:db8:3000::/48",
                        "rt-entry": {
                            "active-tag": "*",
                            "as-path": "65509 I",
                            "local-preference": "100",
                            "nh": {"to": "2001:db8:7fc5:ca45::2"},
                            "protocol-name": "BGP",
                        },
                    },
                ],
                "table-name": "inet6.0",
                "total-route-count": "36",
            },
        ]
    }
}


