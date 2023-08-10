expected_output = {
    'vrf': {
        'Default': {
            'address_family': {
                'ipv6': {
                },
            },
        },
        'green': {
            'address_family': {
                'ipv6': {
                    'multicast_group': {
                        'FF05::1': {
                            'source_address': {
                                'FC00:168:1::201': {
                                    'flags': 'HW',
                                    'hw_average_packet_size': 1000,
                                    'hw_kbits_per_second': 7734,
                                    'hw_other_drops': 0,
                                    'hw_packet_count': 131808,
                                    'hw_packets_per_second': 990,
                                    'hw_rpf_failed': 0,
                                    'hw_total': 0,
                                    'incoming_interfaces': {
                                        'Vlan201': {
                                            'ingress_flags': 'A',
                                        },
                                    },
                                    'outgoing_interfaces': {
                                        'Vlan200': {
                                            'egress_flags': 'F',
                                            'egress_fs_pkt_count': 0,
                                            'egress_hw_pkt_count': 0,
                                            'egress_pkt_rate': 0,
                                            'egress_ps_pkt_count': 23,
                                            'egress_vxlan_cap': 'Encap',
                                            'egress_vxlan_nxthop': '239.1.1.1',
                                            'egress_vxlan_version': 'v4',
                                            'egress_vxlan_vni': '10100',
                                        },
                                        'Vlan202': {
                                            'egress_flags': 'F NS',
                                            'egress_fs_pkt_count': 0,
                                            'egress_hw_pkt_count': 0,
                                            'egress_pkt_rate': 0,
                                            'egress_ps_pkt_count': 23,
                                        },
                                    },
                                    'sw_average_packet_size': 978,
                                    'sw_kbits_per_second': 0,
                                    'sw_other_drops': 0,
                                    'sw_packet_count': 23,
                                    'sw_packets_per_second': 0,
                                    'sw_rpf_failed': 0,
                                    'sw_total': 0,
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}