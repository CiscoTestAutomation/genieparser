expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        '1': {
                            'interfaces': {
                                'GigabitEthernet0/0/0/0': {
                                    'name': 'GigabitEthernet0/0/0/0',
                                    'demand_circuit': False,
                                    'enable': True,
                                    'line_protocol': True,
                                    'bfd': {
                                        'enable': False
                                    },
                                    'ip_address': '60.111.1.1/30',
                                    'area': '0',
                                    'label_stack': {
                                        'primary_label': '1',
                                        'backup_label': '3',
                                        'srte_label': '10'
                                    },
                                    'process_id': '1',
                                    'router_id': '50.1.1.1',
                                    'interface_type': 'POINT_TO_POINT',
                                    'cost': 1,
                                    'ldp_status': {
                                        'ldp_sync': 'Enabled',
                                        'sync_status': 'Achieved'
                                    },
                                    'transmit_delay': 1,
                                    'state': 'POINT_TO_POINT',
                                    'mtu': 1500,
                                    'max_pkt_sz': 1500,
                                    'forward_reference': 'No',
                                    'unnumbered': False,
                                    'bandwidth': 1000000,
                                    'hello_interval': 10,
                                    'dead_interval': 40,
                                    'wait_interval': 40,
                                    'retransmit_interval': 5,
                                    'hello_timer': '00:00:07:190',
                                    'index': '2/2',
                                    'flood_queue_length': 0,
                                    'next': '0(0)/0(0)',
                                    'last_flood_scan_length': 1,
                                    'max_flood_scan_length': 3,
                                    'last_flood_scan_time_msec': 0,
                                    'max_flood_scan_time_msec': 1069,
                                    'ls_ack_list': 'current',
                                    'ls_ack_list_length': 0,
                                    'high_water_mark': 9,
                                    'statistics': {
                                        'nbr_count': 1,
                                        'adj_nbr_count': 1,
                                        'num_nbrs_suppress_hello': 0,
                                        'multi_area_intf_count': 0
                                    },
                                    'neighbors': {
                                        '50.1.1.2': {
                                            'router_id': '50.1.1.2'
                                        }
                                    },
                                    'authentication': {
                                        'auth_trailer_key': {
                                            'crypto_algorithm': 'md5',
                                            'youngest_key_id': 1
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