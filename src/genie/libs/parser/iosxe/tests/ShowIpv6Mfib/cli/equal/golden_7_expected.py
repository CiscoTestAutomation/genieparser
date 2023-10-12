expected_output = {
    "vrf": {
        "Default": {
            "address_family": {
                "ipv6": {
                    "multicast_group": {
                        "FF09::11": {
                            "source_address": {
                                "*": {
                                    "flags": "C K HW",
                                    "oif_ic_count": 0,
                                    "oif_a_count": 1,
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
                                        "GigabitEthernet1/0/1": {
                                            "ingress_flags": "RA A MA NS"
                                        }
                                    },
                                    "outgoing_interfaces": {
                                        "L2LISP0.1501": {
                                            "egress_flags": "RF F NS",
                                            "egress_adj_mac": "OCE (lisp decap)",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0
                                        },
                                        "L2LISP0.1502": {
                                            "egress_flags": "RF F NS",
                                            "egress_adj_mac": "OCE (lisp decap)",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0
                                        }
                                    }
                                },
                                "2001:100:11:11::11": {
                                    "flags": "K HW DDE",
                                    "oif_ic_count": 0,
                                    "oif_a_count": 1,
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                    "hw_packet_count": 3135,
                                    "hw_packets_per_second": 1,
                                    "hw_average_packet_size": 122,
                                    "hw_kbits_per_second": 1,
                                    "hw_total": 0,
                                    "hw_rpf_failed": 0,
                                    "hw_other_drops": 0,
                                    "incoming_interfaces": {
                                        "Null0": {
                                            "ingress_flags": "RA A MA"
                                        }
                                    },
                                    "outgoing_interfaces": {
                                        "GigabitEthernet1/0/1": {
                                            "egress_flags": "RF F NS",
                                            "egress_adj_mac": "Adjacency with MAC: 333300000011525400047F1586DD",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0
                                        }
                                    }
                                },
                                "2001:100:22:22::22": {
                                    "flags": "K HW DDE",
                                    "oif_ic_count": 0,
                                    "oif_a_count": 1,
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                    "hw_packet_count": 1568,
                                    "hw_packets_per_second": 0,
                                    "hw_average_packet_size": 134,
                                    "hw_kbits_per_second": 0,
                                    "hw_total": 0,
                                    "hw_rpf_failed": 0,
                                    "hw_other_drops": 0,
                                    "incoming_interfaces": {
                                        "GigabitEthernet1/0/1": {
                                            "ingress_flags": "RA A MA"
                                        }
                                    },
                                    "outgoing_interfaces": {
                                        "L2LISP0.1501": {
                                            "egress_flags": "RF F NS",
                                            "egress_adj_mac": "OCE (lisp decap)",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0
                                        },
                                        "L2LISP0.1502": {
                                            "egress_flags": "RF F NS",
                                            "egress_adj_mac": "OCE (lisp decap)",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0
                                        }
                                    }
                                },
                                "2001:100:33:33::33": {
                                    "flags": "K HW DDE",
                                    "oif_ic_count": 0,
                                    "oif_a_count": 1,
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                    "hw_packet_count": 1568,
                                    "hw_packets_per_second": 0,
                                    "hw_average_packet_size": 134,
                                    "hw_kbits_per_second": 0,
                                    "hw_total": 0,
                                    "hw_rpf_failed": 0,
                                    "hw_other_drops": 0,
                                    "incoming_interfaces": {
                                        "GigabitEthernet1/0/1": {
                                            "ingress_flags": "RA A MA"
                                        }
                                    },
                                    "outgoing_interfaces": {
                                        "L2LISP0.1501": {
                                            "egress_flags": "RF F NS",
                                            "egress_adj_mac": "OCE (lisp decap)",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0
                                        },
                                        "L2LISP0.1502": {
                                            "egress_flags": "RF F NS",
                                            "egress_adj_mac": "OCE (lisp decap)",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0
                                        }
                                    }
                                },
                                "2001:100:88:88:88:88:88:88": {
                                    "flags": "K HW DDE",
                                    "oif_ic_count": 0,
                                    "oif_a_count": 1,
                                    "sw_packet_count": 0,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 0,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                    "hw_packet_count": 1567,
                                    "hw_packets_per_second": 0,
                                    "hw_average_packet_size": 134,
                                    "hw_kbits_per_second": 0,
                                    "hw_total": 0,
                                    "hw_rpf_failed": 0,
                                    "hw_other_drops": 0,
                                    "incoming_interfaces": {
                                        "GigabitEthernet1/0/1": {
                                            "ingress_flags": "RA A MA"
                                        }
                                    },
                                    "outgoing_interfaces": {
                                        "L2LISP0.1501": {
                                            "egress_flags": "RF F NS",
                                            "egress_adj_mac": "OCE (lisp decap)",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0
                                        },
                                        "L2LISP0.1502": {
                                            "egress_flags": "RF F NS",
                                            "egress_adj_mac": "OCE (lisp decap)",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
