

expected_output = {
        'mstp': {
            'mst_intances': {
                0: {
                    'mst_id': 0,
                    'vlans_mapped': '1-399,501-4094',
                    'bridge_address': '0023.04ff.ad03',
                    'bridge_priority': 32768,
                    'sys_id': 0,
                    'root_for_cist' : 'this switch',
                    'interfaces': {
                        'Port-channel25': {
                            'name': 'Port-channel25',
                            'port_state': 'broken',
                            'port_id': '128.4125',
                            'port_priority': 128,
                            'port_cost': 500,
                            'bridge_assurance_inconsistent': True,
                            'vpc_peer_link_inconsistent': True,
                            'designated_root_address': '0023.04ff.ad03',
                            'designated_root_priority': 32768,
                            'designated_root_cost': 0,
                            'designated_regional_root_address': '0023.04ff.ad03',
                            'designated_regional_root_priority': 32768,
                            'designated_regional_root_cost': 0,
                            'designated_bridge_address': '4055.39ff.fee7',
                            'designated_bridge_priority': 61440,
                            'designated_bridge_port_id': '128.4125',
                            'timers': {
                                'message_expires_in': 0,
                                'forward_delay': 0,
                                'forward_transitions': 0
                            },
                            'counters': {
                                'bpdu_sent': 113,
                                'bpdu_recieved': 0
                            }
                        }
                    },
                    'operational': {
                        'domain': 'operational',
                        'hello_time': 5,
                        'forwarding_delay': 20,
                        'max_age': 30,
                        'hold_count': 12
                    },
                    'configured': {
                        'domain': 'configured',
                        'hello_time': 10,
                        'forwarding_delay': 30,
                        'max_age': 40,
                        'max_hop': 255
                    }
                }
            }
        }
    }
