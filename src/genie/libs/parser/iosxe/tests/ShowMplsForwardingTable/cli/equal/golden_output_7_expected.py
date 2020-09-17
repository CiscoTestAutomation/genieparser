expected_output = {
    "vrf": {
        "default": {
            "local_label": {
                39: {
                    "outgoing_label_or_vc": {
                        "16052": {
                            "prefix_or_tunnel_id": {
                                "10.169.14.241/32": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/1/7": {
                                            "bytes_label_switched": 0,
                                            "merged": True,
                                            "next_hop": "10.169.196.217",
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                16052: {
                    "outgoing_label_or_vc": {
                        "16052": {
                            "prefix_or_tunnel_id": {
                                "10.169.14.241/32": {
                                    "outgoing_interface": {
                                        "GigabitEthernet0/1/7": {
                                            "bytes_label_switched": 0,
                                            "merged": True,
                                            "next_hop": "10.169.196.217",
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
            }
        }
    }
}
