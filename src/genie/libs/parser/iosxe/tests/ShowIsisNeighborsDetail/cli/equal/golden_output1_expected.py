expected_output = {
    "isis": {
        "1": {
            "neighbors": {
                "7600": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "Ethernet0/1": {
                                    "state": "INIT",
                                    "holdtime": "24",
                                    "circuit_id": "rudy.105",
                                    "area_addresses": [
                                        "50.1234",
                                        "49.1234"
                                    ],
                                    "snpa": "aabb.cc00.9d20",
                                    "state_changed": "00:02:07",
                                    "format": "Phase IV",
                                    "remote_tids": [
                                        "0"
                                    ],
                                    "parallel_suppressed": True,
                                    "local_tids": [
                                        "0"
                                    ],
                                    "interface_name": "Ethernet4/0",
                                    "nbr_ckt_id": "17",
                                    "nbr_tlv_rcvd": False,
                                    "mtid_nlpid": [
                                        {
                                            "mtid": "0",
                                            "nlpid": "IPV4"
                                        },
                                        {
                                            "mtid": "0",
                                            "nlpid": "IPV4"
                                        }
                                    ],
                                    "bfd_mtid_afi": [
                                        {
                                            "bfd_mtid": "2",
                                            "bfd_afi": "ipv6"
                                        },
                                        {
                                            "bfd_mtid": "2",
                                            "bfd_afi": "ipv6"
                                        }
                                    ]
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
