expected_output = {
    "route-information": {
        "route-table": [
            {
                "active-route-count": "929",
                "destination-count": "929",
                "hidden-route-count": "0",
                "holddown-route-count": "0",
                "rt": [
                    {
                        "rt-destination": "0.0.0.0/0",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w3d 03:12:45"},
                            "metric": "101",
                            "nh": [{"to": "10.169.14.121", "via": "ge-0/0/1.0"}],
                            "preference": "150",
                            "preference2": "10",
                            "protocol-name": "OSPF",
                            "rt-tag": "0",
                        },
                    },
                    {
                        "rt-destination": "10.1.0.0/24",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "29w6d 21:35:55"},
                            "nh": [{"via": "fxp0.0"}],
                            "preference": "0",
                            "protocol-name": "Direct",
                        },
                    },
                    {
                        "rt-entry": {
                            "age": {"#text": "3w3d 03:12:45"},
                            "metric": "20",
                            "nh": [{"to": "10.169.14.121", "via": "ge-0/0/1.0"}],
                            "preference": "150",
                            "preference2": "10",
                            "protocol-name": "OSPF",
                            "rt-tag": "0",
                        }
                    },
                    {
                        "rt-destination": "10.1.0.101/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "29w6d 21:35:55"},
                            "nh": [{"nh-local-interface": "fxp0.0"}],
                            "preference": "0",
                            "protocol-name": "Local",
                        },
                    },
                    {
                        "rt-destination": "10.36.3.3/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "1w0d 15:44:41"},
                            "metric": "1202",
                            "nh": [{"to": "10.169.14.121", "via": "ge-0/0/1.0"}],
                            "preference": "10",
                            "preference2": "10",
                            "protocol-name": "OSPF",
                        },
                    },
                    {
                        "rt-destination": "10.16.0.0/30",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w0d 04:39:36"},
                            "metric": "1200",
                            "nh": [{"to": "10.169.14.121", "via": "ge-0/0/1.0"}],
                            "preference": "10",
                            "preference2": "10",
                            "protocol-name": "OSPF",
                        },
                    },
                    {
                        "rt-destination": "10.100.5.5/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w0d 04:39:36"},
                            "metric": "1201",
                            "nh": [{"to": "10.169.14.121", "via": "ge-0/0/1.0"}],
                            "preference": "10",
                            "preference2": "10",
                            "protocol-name": "OSPF",
                        },
                    },
                    {
                        "rt-destination": "10.220.0.0/16",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {"#text": "3w3d 03:12:24"},
                            "as-path": " (65151 65000) I",
                            "learned-from": "10.169.14.240",
                            "local-preference": "120",
                            "med": "12003",
                            "nh": [{"to": "10.169.14.121", "via": "ge-0/0/1.0"}],
                            "preference": "170",
                            "protocol-name": "BGP",
                            "validation-state": "unverified",
                        },
                    },
                    {
                        "rt-entry": {
                            "age": {"#text": "3w1d 16:51:06"},
                            "as-path": " (65151 65000) I",
                            "learned-from": "10.189.5.253",
                            "local-preference": "120",
                            "med": "12003",
                            "nh": [{"to": "10.189.5.94", "via": "ge-0/0/0.0"}],
                            "preference": "170",
                            "protocol-name": "BGP",
                            "validation-state": "unverified",
                        }
                    },
                ],
                "table-name": "inet.0",
                "total-route-count": "1615",
            }
        ]
    }
}
