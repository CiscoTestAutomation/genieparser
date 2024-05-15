expected_output = {
    'vrf': {
        'Default': {
            'address_family': {
                'ipv6': {
                    'multicast_group': {
                        'FF13::1': {
                            'source_address': {
                                '1111::1': {
                                    'flags': 'HW',
                                    'hw_average_packet_size': 152,
                                    'hw_kbits_per_second': 1,
                                    'hw_other_drops': 0,
                                    'hw_packet_count': 1242,
                                    'hw_packets_per_second': 1,
                                    'hw_rpf_failed': 0,
                                    'hw_total': 0,
                                    'incoming_interfaces': {'Port-channel5': {'ingress_flags': 'A'}},
                                    'outgoing_interfaces': {'Tunnel1': {'egress_flags': 'F '
                                        'NS',
                                        'egress_fs_pkt_count': 0,
                                        'egress_hw_pkt_count': 0,
                                        'egress_pkt_rate': 0,
                                        'egress_ps_pkt_count': 1,
                                        'egress_vxlan_cap': 'Decap',
                                        'egress_vxlan_version': 'v6'}},
                                    'sw_average_packet_size': 134,
                                    'sw_kbits_per_second': 0,
                                    'sw_other_drops': 0,
                                    'sw_packet_count': 1,
                                    'sw_packets_per_second': 0,
                                    'sw_rpf_failed': 0,
                                    'sw_total': 0
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
