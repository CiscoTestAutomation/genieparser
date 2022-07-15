expected_output = {
    "vrf": {
        "red": {
            "address_family": {
                "ipv4": {
                    "multicast_group": {
                        "224.0.0.0/4": {
                            "source_address": {
                                "*": {
                                    "flags": "C",
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 41613,
                                    "sw_rpf_failed": 41613,
                                    "sw_other_drops": 0,
                                }
                            }
                        },
                        "224.0.1.40": {
                            "source_address": {
                                "*": {
                                    "flags": "C",
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                    "outgoing_interfaces": {
                                        "Vlan100": {
                                            "egress_flags": "F IC NS",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0,
                                        }
                                    },
                                }
                            }
                        },
                        "232.0.0.0/8": {
                            "source_address": {
                                "*": {
                                    "flags": "",
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                }
                            }
                        },
                        "232.1.1.1": {
                            "source_address": {
                                "30.0.0.2": {
                                    "flags": "",
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                    "incoming_interfaces": {
                                        "Vlan100": {"ingress_flags": "A"}
                                    },
                                    "outgoing_interfaces": {
                                        "Vlan500": {
                                            "egress_flags": "F",
                                            "egress_vxlan_cap": "Encap",
                                            "egress_vxlan_version": "v4",
                                            "egress_vxlan_vni": "50000",
                                            "egress_vxlan_nxthop": "239.1.1.0",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0,
                                        }
                                    },
                                }
                            }
                        },
                        "232.1.1.2": {
                            "source_address": {
                                "20.0.0.2": {
                                    "flags": "",
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                    "incoming_interfaces": {
                                        "Vlan500": {
                                            "ingress_flags": "A",
                                            "ingress_vxlan_cap": "Decap",
                                        }
                                    },
                                    "outgoing_interfaces": {
                                        "Vlan100": {
                                            "egress_flags": "F NS",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0,
                                        }
                                    },
                                },
                                "20.0.0.4": {
                                    "flags": "",
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                    "outgoing_interfaces": {
                                        "Vlan100": {
                                            "egress_flags": "F NS",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0,
                                        }
                                    },
                                },
                                "20.0.0.5": {
                                    "flags": "",
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                    "outgoing_interfaces": {
                                        "Vlan100": {
                                            "egress_flags": "F NS",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0,
                                        }
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
