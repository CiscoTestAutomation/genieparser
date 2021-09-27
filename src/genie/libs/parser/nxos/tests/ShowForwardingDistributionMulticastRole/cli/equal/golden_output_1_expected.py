

expected_output = {
    "distribution": {
        "multicast": {
            "route": {
                "vrf": {
                    'default': {
                        "address_family": {
                            "ipv4": {
                                "num_groups": 5,
                                "gaddr": {
                                    '224.0.0.0/4': {
                                        "grp_len": 4,
                                         "saddr": {
                                              '*': {
                                                "rpf_ifname": 'NULL',
                                                "flags": 'D',
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0
                                                }
                                              }
                                         },
                                    '224.0.0.0/24': {
                                        "grp_len": 24,
                                        "saddr": {
                                            '*': {
                                                "rpf_ifname": 'NULL',
                                                "flags": 'CP',
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 0
                                            }
                                        }
                                    },
                                    '231.100.1.1/32': {
                                        "grp_len": 32,
                                        "saddr": {
                                            '*': {
                                                "rpf_ifname": 'Ethernet1/2',
                                                "flags": 'GLd',
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 30,
                                                    'nve1': {
                                                        'oif': 'nve1',
                                                    },
                                                },
                                            },
                                            '10.76.23.23/32': {
                                                "src_len": 32,
                                                "rpf_ifname": "loopback1",
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 29,
                                                    'Ethernet1/2': {
                                                        'oif': 'Ethernet1/2',
                                                    },
                                                },
                                            }
                                        }
                                    },
                                    '231.1.3.101/32': {
                                        "grp_len": 32,
                                        "saddr": {
                                            '*': {
                                                "rpf_ifname": 'loopback100',
                                                "flags": 'GL',
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 1,
                                                "oifs": {
                                                    "oif_index": 104,
                                                    "Vlan101": {
                                                        "oif": "Vlan101",
                                                        "mem_l2_ports": "port-channel1 nve1",
                                                        "l2_oiflist_index": 44,
                                                    },
                                                },
                                            },
                                        }
                                    },
                                    "238.8.4.101/32": {
                                        "grp_len": 32,
                                        "saddr": {
                                            "10.111.1.3/32": {
                                                "src_len": 32,
                                                "rpf_ifname": 'Vlan101',
                                                "rcv_packets": 0,
                                                "rcv_bytes": 0,
                                                "num_of_oifs": 2,
                                                "oifs": {
                                                    "oif_index": 54,
                                                    'Vlan100': {
                                                        "oif": "Vlan100",
                                                        "encap": 'vxlan',
                                                        "mem_l2_ports": "nve1",
                                                        "l2_oiflist_index": 19,
                                                    },
                                                    'Vlan101': {
                                                        "oif": 'Vlan101',
                                                        "mem_l2_ports": "nve1",
                                                        "l2_oiflist_index": 19,
                                                    },
                                                },
                                            },
                                        }
                                    },
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
