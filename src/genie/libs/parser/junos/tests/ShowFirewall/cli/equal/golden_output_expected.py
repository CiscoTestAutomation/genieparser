expected_output = {
    "firewall-information": {
        "filter-information": [
            {
                "counter": [
                    {
                        "byte-count": "28553344730",
                        "counter-name": "cflow_counter_v4",
                        "packet-count": "151730215",
                    }
                ],
                "filter-name": "catch_all",
            },
            {
                "counter": [
                    {
                        "byte-count": "0",
                        "counter-name": "fragment-test",
                        "packet-count": "0",
                    },
                    {
                        "byte-count": "0",
                        "counter-name": "fragment-test2",
                        "packet-count": "0",
                    },
                    {
                        "byte-count": "1069200810",
                        "counter-name": "last_policer",
                        "packet-count": "19016081",
                    },
                    {
                        "byte-count": "0",
                        "counter-name": "ntp-deny-count",
                        "packet-count": "0",
                    },
                    {
                        "byte-count": "1316",
                        "counter-name": "telnet-deny-count",
                        "packet-count": "23",
                    },
                    {
                        "byte-count": "1385466",
                        "counter-name": "traceroute-udp-deny-count",
                        "packet-count": "8350",
                    },
                ],
                "filter-name": "local-access-control",
                "policer": {
                    "byte-count": "2508396",
                    "packet-count": "48164",
                    "policer-name": "MINIMUM-RATE-POLICER",
                },
            },
            {
                "counter": [
                    {
                        "byte-count": "0",
                        "counter-name": "deny-dst-in",
                        "packet-count": "0",
                    },
                    {
                        "byte-count": "0",
                        "counter-name": "deny-p-in",
                        "packet-count": "0",
                    },
                    {
                        "byte-count": "0",
                        "counter-name": "deny-src-in",
                        "packet-count": "0",
                    },
                ],
                "filter-name": "v4_EXT_inbound",
            },
            {
                "counter": [
                    {
                        "byte-count": "0",
                        "counter-name": "cflow_counter_v4",
                        "packet-count": "0",
                    },
                    {
                        "byte-count": "0",
                        "counter-name": "deny-dst-in",
                        "packet-count": "0",
                    },
                    {
                        "byte-count": "0",
                        "counter-name": "deny-rsvp-in",
                        "packet-count": "0",
                    },
                ],
                "filter-name": "v4_toIPVPN_inbound",
            },
            {
                "counter": [
                    {
                        "byte-count": "12001013864",
                        "counter-name": "cflow_counter_v6",
                        "packet-count": "149192171",
                    }
                ],
                "filter-name": "v6_catch_all",
            },
            {
                "counter": [
                    {
                        "byte-count": "0",
                        "counter-name": "traceroute-udp-deny-count",
                        "packet-count": "0",
                    },
                    {
                        "byte-count": "1061535120",
                        "counter-name": "v6_last_policer",
                        "packet-count": "7859252",
                    },
                ],
                "filter-name": "v6_local-access-control",
                "policer": {
                    "byte-count": "0",
                    "packet-count": "0",
                    "policer-name": "MINIMUM-RATE-POLICER",
                },
            },
            {"filter-name": "__default_bpdu_filter__"},
        ]
    }
}
