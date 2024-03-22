expected_output = {
    "vrf": {
        "Default": {
            "address_family": {
                "ipv6": {
                    "multicast_group": {
                        "FF05::1": {
                            "source_address": {
                                "2000::1:1": {
                                    "flags": "HW",
                                    "sw_packet_count": 9,
                                    "sw_packets_per_second": 0,
                                    "sw_average_packet_size": 144,
                                    "sw_kbits_per_second": 0,
                                    "sw_total": 0,
                                    "sw_rpf_failed": 0,
                                    "sw_other_drops": 0,
                                    "hw_packet_count": 38797693,
                                    "hw_packets_per_second": 396,
                                    "hw_average_packet_size": 166,
                                    "hw_kbits_per_second": 513,
                                    "hw_total": 0,
                                    "hw_rpf_failed": 0,
                                    "hw_other_drops": 0,
                                    "incoming_interfaces": {
                                        "Null0": {"ingress_flags": "A"}
                                    },
                                    "outgoing_interfaces": {
                                        "GigabitEthernet1/0/6": {
                                            "egress_flags": "F NS",
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
