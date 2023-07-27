expected_output = {
    'vrf': {
        'red': {
            'address_family': {
                'ipv6': {
                    'multicast_group': {
                        'FF05:1::5': {
                            'source_address': {
                                '2000::21': {
                                    'flags': 'HW',
                                    'hw_average_packet_size': 160,
                                    'hw_kbits_per_second': 123,
                                    'hw_other_drops': 0,
                                    'hw_packet_count': 594209,
                                    'hw_packets_per_second': 99,
                                    'hw_rpf_failed': 0,
                                    'hw_total': 0,
                                    'incoming_interfaces': {
                                        'Vlan100': {
                                            'ingress_flags': 'A',
                                        },
                                    },
                                    'outgoing_interfaces': {
                                        'Tunnel5': {
                                            'egress_flags': 'F NS NP',
                                            'egress_fs_pkt_count': 0,
                                            'egress_hw_pkt_count': 0,
                                            'egress_pkt_rate': 0,
                                            'egress_ps_pkt_count': 520569,
                                        },
                                        'Vlan500': {
                                            'egress_flags': 'F',
                                            'egress_fs_pkt_count': 0,
                                            'egress_hw_pkt_count': 0,
                                            'egress_pkt_rate': 0,
                                            'egress_ps_pkt_count': 0,
                                            'egress_vxlan_cap': 'Encap',
                                            'egress_vxlan_nxthop': 'FF55::2',
                                            'egress_vxlan_version': 'v6',
                                            'egress_vxlan_vni': '50000',
                                        },
                                    },
                                    'sw_average_packet_size': 138,
                                    'sw_kbits_per_second': 0,
                                    'sw_other_drops': 0,
                                    'sw_packet_count': 2,
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
