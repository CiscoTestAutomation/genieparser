expected_output = {
    "vrf": {
        "red": {
            "address_family": {
                "ipv4": {
                    "multicast_group": {
                        "224.0.0.0/4": {
                            "source_address": {
                                "*": {
                                    "flags": "C HW",
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 39,
                                    "sw_rpf_failed": 39,
                                    "sw_other_drops": 0,
                                    "hw_packet_count": 0,
                                    "hw_packets_per_second": 0,
                                    "hw_average_packet_size": 0,
                                    "hw_kbits_per_second": 0,
                                    "hw_total": 0,
                                    "hw_rpf_failed": 0,
                                    "hw_other_drops": 0,
                                }
                            }
                        },
                        "224.0.1.40": {
                            "source_address": {
                                "*": {
                                    "flags": "C HW",
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                    "hw_packet_count": 0,
                                    "hw_packets_per_second": 0,
                                    "hw_average_packet_size": 0,
                                    "hw_kbits_per_second": 0,
                                    "hw_total": 0,
                                    "hw_rpf_failed": 0,
                                    "hw_other_drops": 0,
                                    "incoming_interfaces": {
                                        "Vlan500": {
                                            "ingress_flags": "A NS",
                                            "ingress_vxlan_cap": "Decap",
                                        }
                                    },
                                    "outgoing_interfaces": {
                                        "Loopback1": {
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
                        "226.1.1.1": {
                            "source_address": {
                                "*": {
                                    "flags": "C HW",
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                    "hw_packet_count": 0,
                                    "hw_packets_per_second": 0,
                                    "hw_average_packet_size": 0,
                                    "hw_kbits_per_second": 0,
                                    "hw_total": 0,
                                    "hw_rpf_failed": 0,
                                    "hw_other_drops": 0,
                                    "incoming_interfaces": {
                                        "Vlan500": {
                                            "ingress_flags": "A",
                                            "ingress_vxlan_cap": "Decap",
                                        }
                                    },
                                },
                                "30.0.0.2": {
                                    "flags": "HW",
                                    "sw_packet_count": 2,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 20,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 1,
                                    "sw_rpf_failed": 1,
                                    "sw_other_drops": 0,
                                    "hw_packet_count": 245685,
                                    "hw_packets_per_second": 100,
                                    "hw_average_packet_size": 64,
                                    "hw_kbits_per_second": 50,
                                    "hw_total": 0,
                                    "hw_rpf_failed": 0,
                                    "hw_other_drops": 0,
                                    "incoming_interfaces": {
                                        "Vlan100": {"ingress_flags": "A"}
                                    },
                                    "outgoing_interfaces": {
                                        "Vlan500": {
                                            "egress_flags": "F",
                                            "egress_vxlan_cap": "Encap",
                                            "egress_vxlan_version": "v6",
                                            "egress_vxlan_vni": "50000",
                                            "egress_vxlan_nxthop": "FF13::1",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0,
                                        }
                                    },
                                },
                            }
                        },
                        "232.0.0.0/8": {
                            "source_address": {
                                "*": {
                                    "flags": "HW",
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 46575,
                                    "sw_rpf_failed": 46575,
                                    "sw_other_drops": 0,
                                    "hw_packet_count": 0,
                                    "hw_packets_per_second": 0,
                                    "hw_average_packet_size": 0,
                                    "hw_kbits_per_second": 0,
                                    "hw_total": 0,
                                    "hw_rpf_failed": 0,
                                    "hw_other_drops": 0,
                                }
                            }
                        },
                    }
                }
            }
        }
    }
}
