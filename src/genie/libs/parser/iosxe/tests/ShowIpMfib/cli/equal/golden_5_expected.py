expected_output = {
    "vrf": {
        "Default": {"address_family": {"ipv4": {}}},
        "vrf21": {
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
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                    "hw_packet_count": "NA",
                                    "hw_packets_per_second": "NA",
                                    "hw_average_packet_size": "NA",
                                    "hw_kbits_per_second": "NA",
                                    "hw_total": "NA",
                                    "hw_rpf_failed": "NA",
                                    "hw_other_drops": "NA",
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
                                    "hw_packet_count": "NA",
                                    "hw_packets_per_second": "NA",
                                    "hw_average_packet_size": "NA",
                                    "hw_kbits_per_second": "NA",
                                    "hw_total": "NA",
                                    "hw_rpf_failed": "NA",
                                    "hw_other_drops": "NA",
                                    "outgoing_interfaces": {
                                        "Vlan21": {
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
                    }
                }
            }
        },
    }
}
