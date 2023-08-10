expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'instance': {
                        '200': {
                            'interfaces': {
                                'GigabitEthernet0/0/0/2': {
                                    'name': 'GigabitEthernet0/0/0/2',
                                    'demand_circuit': False,
                                    'enable': False,
                                    'line_protocol': False,
                                    'bfd': {
                                        'enable': False
                                    },
                                    'ip_address': '200.6.1.1/30',
                                    'area': '200',
                                    'sid': '0',
                                    'strict_spf_sid': '0',
                                    'label_stack': {
                                        'primary_label': '0',
                                        'backup_label': '0',
                                        'srte_label': '0'
                                    },
                                    'process_id': '200',
                                    'router_id': '100.1.1.200',
                                    'interface_type': 'BROADCAST',
                                    'cost': 1,
                                    'transmit_delay': 1,
                                    'state': 'DOWN',
                                    'priority': 1,
                                    'mtu': 1500,
                                    'max_pkt_sz': 1500,
                                    'hello_interval': 10,
                                    'dead_interval': 40,
                                    'wait_interval': 40,
                                    'retransmit_interval': 5,
                                    'nsf_enabled': True,
                                    'index': '1/1',
                                    'flood_queue_length': 0,
                                    'next': '0(0)/0(0)',
                                    'last_flood_scan_length': 0,
                                    'max_flood_scan_length': 0,
                                    'last_flood_scan_time_msec': 0,
                                    'max_flood_scan_time_msec': 0,
                                    'ls_ack_list': 'current',
                                    'ls_ack_list_length': 0,
                                    'high_water_mark': 0,
                                    'statistics': {
                                        'nbr_count': 0,
                                        'adj_nbr_count': 0,
                                        'num_nbrs_suppress_hello': 0,
                                        'multi_area_intf_count': 0
                                    },
                                    'neighbors': {}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}