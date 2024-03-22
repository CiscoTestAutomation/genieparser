expected_output = {
    "vrf":{
        "Default":{
            "address_family":{
                "ipv4":{
                    "multicast_group":{
                        "239.0.0.7":{
                            "source_address":{
                                "7.255.0.4":{
                                    "flags":"HW",
                                    "sw_packet_count":6,
                                    "sw_packets_per_second":0,
                                    "sw_average_packet_size":108,
                                    "sw_kbits_per_second":0,
                                    "sw_total":0,
                                    "sw_rpf_failed":0,
                                    "sw_other_drops":0,
                                    "hw_packet_count":15864306,
                                    "hw_packets_per_second":989,
                                    "hw_average_packet_size":126,
                                    "hw_kbits_per_second":974,
                                    "hw_total":0,
                                    "hw_rpf_failed":0,
                                    "hw_other_drops":0,
                                    "incoming_interfaces": {
                                        "Port-channel101": {
                                            "ingress_flags": "A"
                                        }
                                    },
                                    "outgoing_interfaces":{
                                        "L2LISP0.699":{
                                            "egress_flags":"F NS",
                                            "egress_hw_pkt_count":0,
                                            "egress_fs_pkt_count":0,
                                            "egress_ps_pkt_count":0,
                                            "egress_pkt_rate":0
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
