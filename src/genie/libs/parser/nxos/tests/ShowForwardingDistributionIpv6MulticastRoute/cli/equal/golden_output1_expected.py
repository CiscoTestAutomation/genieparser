expected_output = {
    "distribution": {
        "multicast": {
            "route": {
                "vrf": {
                    "default": {
                        "address_family": {
                            "ipv6": {
                                "table_id": "0x80000001",
                                "num_groups": 17,
                                "legend": {
                                    "C": "Control Route",
                                    "D": "Drop Route",
                                    "G": "Local Group (directly connected receivers)",
                                    "O": "Drop on RPF Fail",
                                    "P": "Punt to supervisor",
                                    "L": "SRC behind L3",
                                    "d": "Decap Route",
                                    "Nf": "VPC None-Forwarder",
                                    "dm": "MVPN Decap Route",
                                    "em": "Encap Route",
                                    "rm": "Source is DCI Remote",
                                },
                                "gaddr": {
                                    "ff05::2/128": {
                                        "grp_len": 128,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "DG",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 1,
                                                    "Ethernet1/8": {
                                                        "oif": "Ethernet1/8",
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    "ff1e::/64": {
                                        "grp_len": 64,
                                        "saddr": {
                                            "*": {
                                                "bidir_rp_ordinal": 9,
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 3,
                                                    "Ethernet1/1": {
                                                        "oif": "Ethernet1/1",
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    "ff1e::1:1:12/128": {
                                        "grp_len": 128,
                                        "saddr": {
                                            "*": {
                                                "bidir_rp_ordinal": 9,
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 2,
                                                "oifs": {
                                                    "oif_index": 26,
                                                    "Ethernet1/1": {
                                                        "oif": "Ethernet1/1",
                                                    },
                                                    "Ethernet1/8": {
                                                        "oif": "Ethernet1/8",
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    "ff1e::1:1:13/128": {
                                        "grp_len": 128,
                                        "saddr": {
                                            "*": {
                                                "bidir_rp_ordinal": 9,
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 2,
                                                "oifs": {
                                                    "oif_index": 26,
                                                    "Ethernet1/1": {
                                                        "oif": "Ethernet1/1",
                                                    },
                                                    "Ethernet1/8": {
                                                        "oif": "Ethernet1/8",
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    "ff32::/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "D",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0,
                                            },
                                        },
                                    },
                                    "ff33::/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "D",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0,
                                            },
                                        },
                                    },
                                    "ff34::/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "D",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0,
                                            },
                                        },
                                    },
                                    "ff35::/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "D",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0,
                                            },
                                        },
                                    },
                                    "ff36::/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "D",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0,
                                            },
                                        },
                                    },
                                    "ff37::/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "D",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0,
                                            },
                                        },
                                    },
                                    "ff38::/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "D",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0,
                                            },
                                        },
                                    },
                                    "ff39::/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "D",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0,
                                            },
                                        },
                                    },
                                    "ff3a::/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "D",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0,
                                            },
                                        },
                                    },
                                    "ff3b::/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "D",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0,
                                            },
                                        },
                                    },
                                    "ff3c::/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "D",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0,
                                            },
                                        },
                                    },
                                    "ff3d::/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "D",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0,
                                            },
                                        },
                                    },
                                    "ff3e::/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "*": {
                                                "rpf_ifname": "NULL",
                                                "flags": "D",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
