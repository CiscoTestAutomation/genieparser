expected_output = {
    "instance": {
        "master": {
            "areas": {
                "0.0.0.1": {
                    "interfaces": {
                        "ge-0/0/0.0": {
                            "state": "PtToPt",
                            "dr_id": "0.0.0.0",
                            "bdr_id": "0.0.0.0",
                            "nbrs_count": 1,
                            "type": "P2P",
                            "address": "172.16.94.1",
                            "mask": "255.255.255.0",
                            "mtu": 500,
                            "cost": 50,
                            "adj_count": 1,
                            "hello": 10,
                            "dead": 20,
                            "rexmit": 10,
                            "ospf_stub_type": "Not Stub",
                            "authentication_type": "None",
                            "ospf_interface": {
                                "protection_type": "Post Convergence",
                                "tilfa": {
                                    "prot_link": "Enabled",
                                    "prot_fate": "No",
                                    "prot_srlg": "No",
                                    "prot_node": 50,
                                },
                                "topology": {"default": {"id": 0, "metric": 50}},
                            },
                        },
                        "ge-0/0/1.0": {
                            "state": "PtToPt",
                            "dr_id": "0.0.0.0",
                            "bdr_id": "0.0.0.0",
                            "nbrs_count": 1,
                            "type": "P2P",
                            "address": "172.16.94.1",
                            "mask": "255.255.255.0",
                            "mtu": 500,
                            "cost": 100,
                            "adj_count": 1,
                            "hello": 10,
                            "dead": 10,
                            "rexmit": 5,
                            "ospf_stub_type": "Not Stub",
                            "authentication_type": "None",
                            "ospf_interface": {
                                "protection_type": "Post Convergence",
                                "tilfa": {
                                    "prot_link": "Enabled",
                                    "prot_fate": "No",
                                    "prot_srlg": "No",
                                    "prot_node": 100,
                                },
                                "topology": {"default": {"id": 0, "metric": 100}},
                            },
                        },
                    }
                }
            }
        }
    }
}
