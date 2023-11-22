expected_output = {
    'vrf': {
        'red': {
            'address_family': {
                'ipv6': {
                    'multicast_group': {
                        'FF33::1': {
                            'source_address': {
                                '192:168:3::1': {
                                    'flags': '',
                                    'sw_average_packet_size': 0,
                                    'sw_kbits_per_second': 0,
                                    'sw_other_drops': 0,
                                    'sw_packet_count': 0,
                                    'sw_packets_per_second': 0,
                                    'sw_rpf_failed': 0,
                                    'sw_total': 0,
                                    'incoming_interfaces': {
                                        'Vlan10': {
                                            'ingress_flags': 'A',
                                        },
                                    },
                                    'outgoing_interfaces': {
                                        'LISP0.101,100:44:44::44': {
                                            'egress_flags': 'F',
                                            'egress_fs_pkt_count': 0,
                                            'egress_hw_pkt_count': 0,
                                            'egress_pkt_rate': 0,
                                            'egress_ps_pkt_count': 0,
                                            'egress_rloc': '100:88:88::88'
                                        },
                                        'LISP0.101,100:88:88::88': {
                                            'egress_flags': 'F',
                                            'egress_fs_pkt_count': 0,
                                            'egress_hw_pkt_count': 0,
                                            'egress_pkt_rate': 0,
                                            'egress_ps_pkt_count': 0,
                                            'egress_rloc': '100:55:55::55'
                                        },
                                        'LISP0.101,100:55:55::55': {
                                            'egress_flags': 'F',
                                            'egress_fs_pkt_count': 0,
                                            'egress_hw_pkt_count': 0,
                                            'egress_pkt_rate': 0,
                                            'egress_ps_pkt_count': 0,
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
