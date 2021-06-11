expected_output = {
    "vrf": {
        'default': {
            "address_family": {
                'ipv4': {
                    "instance": {
                        'mpls1': {
                            "interfaces": {
                                'Loopback0': {
                                    "name": 'Loopback0',
                                    "enable": True,
                                    "line_protocol": True,
                                    "ip_address": '25.97.1.1/32',
                                    "demand_circuit": False,
                                    "process_id": 'mpls1',
                                    "router_id": '25.97.1.1',
                                    "interface_type": 'LOOPBACK',
                                    "area": '0',
                                    "bfd": {
                                        "enable": False,
                                    },
                                    "label_stack": {
                                        "primary_label": '0',
                                        "backup_label": '0',
                                        "srte_label": '0',
                                    },
                                    "treated_as_stub_host": True,
                                    "sid": '0',
                                    "strict_spf_sid": '0',
                                    "cost": 1,
                                },
                                'GigabitEthernet0/0/0/0': {
                                    "name": 'GigabitEthernet0/0/0/0',
                                    "enable": True,
                                    "line_protocol": True,
                                    "ip_address": '100.10.0.1/30',
                                    "demand_circuit": False,
                                    "process_id": 'mpls1',
                                    "router_id": '25.97.1.1',
                                    "interface_type": 'POINT_TO_POINT',
                                    "area": '0',
                                    "bfd": {
                                        "enable": True,
                                        "interval": 150,
                                        "multiplier": 3,
                                        "mode": "Default",
                                    },
                                    "label_stack": {
                                        "primary_label": '1',
                                        "backup_label": '3',
                                        "srte_label": '10',
                                    },
                                    "sid": '0',
                                    "strict_spf_sid": '0',
                                    "cost": 1,
                                    "forward_reference": 'No',
                                    "unnumbered": False,
                                    "bandwidth": 1000000,
                                    "nsf_enabled": True,
                                    "transmit_delay": 1,
                                    "state": 'POINT_TO_POINT',
                                    "mtu": 1500,
                                    "max_pkt_sz": 1500,
                                    "hello_interval": 10,
                                    "dead_interval": 40,
                                    "wait_interval": 40,
                                    "retransmit_interval": 5,
                                    "hello_timer": '00:00:04:702',
                                    "index": '1/1',
                                    "flood_queue_length": 0,
                                    "next": '0(0)/0(0)',
                                    "last_flood_scan_length": 1,
                                    "max_flood_scan_length": 7,
                                    "last_flood_scan_time_msec"
                                    : 0,
                                    "max_flood_scan_time_msec"
                                    : 1,
                                    "ls_ack_list": 'current',
                                    "ls_ack_list_length": 0,
                                    "high_water_mark": 19,
                                    "statistics": {
                                        "adj_nbr_count": 1,
                                        "nbr_count": 1,
                                        "num_nbrs_suppress_hello"
                                        : 0,
                                        "multi_area_intf_count"
                                        : 0,
                                    },
                                    "neighbors": {
                                        '100.100.100.100':{
                                            'router_id': '100.100.100.100'
                                        }
                                    }
                                },
                                'GigabitEthernet0/0/0/1': {
                                    "name": 'GigabitEthernet0/0/0/1',
                                    "enable": True,
                                    "line_protocol": True,
                                    "ip_address": '100.20.0.1/30',
                                    "demand_circuit": False,
                                    "process_id": 'mpls1',
                                    "router_id": '25.97.1.1',
                                    "interface_type": 'POINT_TO_POINT',
                                    "area": '0',
                                    "bfd": {
                                        "enable": True,
                                        "interval": 150,
                                        "multiplier": 3,
                                        "mode": "Default",
                                    },
                                    "label_stack": {
                                        "primary_label": '1',
                                        "backup_label": '3',
                                        "srte_label": '10',
                                    },
                                    "sid": '0',
                                    "strict_spf_sid": '0',
                                    "cost": 1,
                                    "forward_reference": 'No',
                                    "unnumbered": False,
                                    "bandwidth": 1000000,
                                    "nsf_enabled": True,
                                    "transmit_delay": 1,
                                    "state": 'POINT_TO_POINT',
                                    "mtu": 1500,
                                    "max_pkt_sz": 1500,
                                    "hello_interval": 10,
                                    "dead_interval": 40,
                                    "wait_interval": 40,
                                    "retransmit_interval": 5,
                                    "hello_timer": '00:00:08:508',
                                    "index": '2/2',
                                    "flood_queue_length": 0,
                                    "next": '0(0)/0(0)',
                                    "last_flood_scan_length": 3,
                                    "max_flood_scan_length": 9,
                                    "last_flood_scan_time_msec"
                                    : 0,
                                    "max_flood_scan_time_msec"
                                    : 1,
                                    "ls_ack_list": 'current',
                                    "ls_ack_list_length": 0,
                                    "high_water_mark": 14,
                                    "statistics": {
                                        "adj_nbr_count": 1,
                                        "nbr_count": 1,
                                        "num_nbrs_suppress_hello"
                                        : 0,
                                        "multi_area_intf_count"
                                        : 0,
                                    },
                                    "neighbors": {
                                        '95.95.95.95':{
                                            'router_id': '95.95.95.95'
                                        }
                                    }
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}