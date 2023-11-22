expected_output = {
    "vrf": {
        "Default": {
            "address_family": {
                "ipv6": {
                    "multicast_group": {
                        "FF13::1": {
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
                                    "hw_packet_count": 12,
                                    "hw_packets_per_second": 0,
                                    "hw_average_packet_size": 130,
                                    "hw_kbits_per_second": 0,
                                    "hw_total": 0,
                                    "hw_rpf_failed": 0,
                                    "hw_other_drops": 0,
                                    "incoming_interfaces": {
                                        "GigabitEthernet1/0/14": {
                                            "ingress_flags": "A NS"
                                        }
                                    },
                                    "outgoing_interfaces": {
                                        "Tunnel0": {
                                            "egress_flags": "F NS",
                                            "egress_vxlan_cap": "Decap",
                                            "egress_vxlan_version": "v6",
                                            "egress_hw_pkt_count": 0,
                                            "egress_fs_pkt_count": 0,
                                            "egress_ps_pkt_count": 0,
                                            "egress_pkt_rate": 0,
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
