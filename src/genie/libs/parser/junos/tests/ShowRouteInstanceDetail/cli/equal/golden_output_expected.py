expected_output = {
    "instance-information": {
        "instance-core": [
            {
                "instance-name": "master",
                "instance-rib": [
                    {
                        "irib-active-count": "929",
                        "irib-hidden-count": "0",
                        "irib-holddown-count": "0",
                        "irib-name": "inet.0",
                        "irib-route-count": "1615",
                    },
                    {
                        "irib-active-count": "11",
                        "irib-hidden-count": "0",
                        "irib-holddown-count": "0",
                        "irib-name": "inet.3",
                        "irib-route-count": "11",
                    },
                    {
                        "irib-active-count": "44",
                        "irib-hidden-count": "0",
                        "irib-holddown-count": "0",
                        "irib-name": "mpls.0",
                        "irib-route-count": "44",
                    },
                    {
                        "irib-active-count": "22",
                        "irib-hidden-count": "0",
                        "irib-holddown-count": "0",
                        "irib-name": "inet6.0",
                        "irib-route-count": "23",
                    },
                ],
                "instance-state": "Active",
                "instance-type": "forwarding",
                "router-id": "10.189.5.252",
            },
            {
                "instance-interface": [
                    {"interface-name": "pfh-0/0/0.16383"},
                    {"interface-name": "pfe-0/0/0.16383"},
                    {"interface-name": "lo0.16385"},
                    {"interface-name": "em1.0"},
                ],
                "instance-name": "__juniper_private1__",
                "instance-rib": [
                    {
                        "irib-active-count": "5",
                        "irib-hidden-count": "0",
                        "irib-holddown-count": "0",
                        "irib-name": "__juniper_private1__.inet.0",
                        "irib-route-count": "6",
                    },
                    {
                        "irib-active-count": "3",
                        "irib-hidden-count": "0",
                        "irib-holddown-count": "0",
                        "irib-name": "__juniper_private1__.inet6.0",
                        "irib-route-count": "3",
                    },
                ],
                "instance-state": "Active",
                "instance-type": "forwarding",
                "router-id": "0.0.0.0",
            },
            {
                "instance-interface": [
                    {"interface-name": "pfh-0/0/0.16384"},
                    {"interface-name": "lo0.16384"},
                ],
                "instance-name": "__juniper_private2__",
                "instance-rib": [
                    {
                        "irib-active-count": "0",
                        "irib-hidden-count": "1",
                        "irib-holddown-count": "0",
                        "irib-name": "__juniper_private2__.inet.0",
                        "irib-route-count": "1",
                    }
                ],
                "instance-state": "Active",
                "instance-type": "forwarding",
                "router-id": "0.0.0.0",
            },
            {
                "instance-name": "__juniper_private4__",
                "instance-state": "Active",
                "instance-type": "forwarding",
                "router-id": "0.0.0.0",
            },
            {
                "instance-name": "__master.anon__",
                "instance-state": "Active",
                "instance-type": "forwarding",
                "router-id": "0.0.0.0",
            },
            {
                "instance-name": "mgmt_junos",
                "instance-state": "Active",
                "instance-type": "forwarding",
                "router-id": "0.0.0.0",
            },
        ]
    }
}
