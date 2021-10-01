

expected_output = {
    'mstp': {
        'mst_instances': {
            0: {
                'mst_id': 0,
                'bridge_priority': 32768,
                'bridge_sysid': 0,
                'bridge_address': '0023.04ff.ad03',
                'topology_change_flag': False,
                'topology_detected_flag': False,
                'time_since_topology_change': '142:22:13',
                'topology_changes': 0,
                'times': {
                    'hold': 1,
                    'topology_change': 70,
                    'notification': 10,
                    'max_age': 40,
                    'hello': 10,
                    'forwarding_delay': 30,
                },
                'timers' : {
                    'hello': 0,
                    'topology_change': 0,
                    'notification': 0,
                },
                'root_of_the_spanning_tree': True,
                'interfaces': {
                    'Port-channel30': {
                        'name': 'Port-channel30',
                        'bridge_assurance_inconsistent': True,
                        'vpc_peer_link_inconsistent': True,
                        'port_num': 4125,
                        'status': 'broken',
                        'cost': 500,
                        'port_priority': 128,
                        'port_identifier': '128.4125',
                        'designated_root_priority': 32768,
                        'designated_root_address': '0023.04ff.ad03',
                        'designated_bridge_priority': 61440,
                        'designated_bridge_address': '4055.39ff.fee7',
                        'designated_port_id': '128.4125',
                        'designated_path_cost': 0,
                        'timers': {
                            'message_age': 0,
                            'forward_delay': 0,
                            'hold': 0,
                        },
                        'port_type' : 'network',
                        'number_of_forward_transitions': 0,
                        'link_type': 'point-to-point',
                        'internal': True,
                        'pvst_simulation': True,
                        'counters': {
                            'bpdu_sent': 110,
                            'bpdu_received': 0
                        }
                    },
                    'Port-channel14': {
                        'name': 'Port-channel14',
                        'bridge_assurance_inconsistent': True,
                        'vpc_peer_link_inconsistent': True,
                        'port_num': 2390,
                        'status': 'broken',
                        'cost': 6660,
                        'port_priority': 128,
                        'port_identifier': '128.2390.',
                        'designated_root_priority': 32768,
                        'designated_root_address': 'd8b1.90ff.c889',
                        'designated_bridge_priority': 32768,
                        'designated_bridge_address': 'd8b1.90ff.c889',
                        'designated_port_id': '128.2390',
                        'designated_path_cost': 0,
                        'timers': {
                            'message_age': 0,
                            'forward_delay': 0,
                            'hold': 0,
                        },
                        'port_type' : 'network',
                        'number_of_forward_transitions': 0,
                        'link_type': 'point-to-point',
                        'internal': True,
                        'pvst_simulation': True,
                        'counters': {
                            'bpdu_sent': 138231,
                            'bpdu_received': 167393
                        }
                    }
                }
            }
        },
        'hello_time': 10,
        'fex_hello_time': 10,
        'max_age': 40,
        'forwarding_delay': 30
    }
}
