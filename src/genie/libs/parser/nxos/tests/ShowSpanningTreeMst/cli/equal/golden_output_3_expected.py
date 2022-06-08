

expected_output = {
         'mstp': {
             'mst_intances': {
                 0: {
                    'bridge_address': '5000.0009.0007',
                    'bridge_priority': 32768,
                    'interfaces': {
                        'Ethernet1/1': {
                            'counters': {
                                'bpdu_recieved': 4,
                                'bpdu_sent': 412965
                            },
                            'designated_bridge_address': '5000.0009.0007',
                            'designated_bridge_port_id': '128.1',
                            'designated_bridge_priority': 32768,
                            'designated_regional_root_address': '5000.0009.0007',
                            'designated_regional_root_cost': 0,
                            'designated_regional_root_priority': 32768,
                            'designated_root_address': '5000.0009.0007',
                            'designated_root_cost': 0,
                            'designated_root_priority': 32768,
                            'name': 'Ethernet1/1',
                            'port_cost': 20000,
                            'port_id': '128.1',
                            'port_priority': 128,
                            'port_state': 'designated forwarding',
                            'timers': {
                                'forward_delay': 0,
                                'forward_transitions': 1,
                                'message_expires_in': 0
                            }
                        },
                        'Ethernet1/3': {
                            'counters': {
                                'bpdu_recieved': 0,
                                'bpdu_sent': 412967
                            },
                            'designated_bridge_address': '5000.0009.0007',
                            'designated_bridge_port_id': '128.3',
                            'designated_bridge_priority': 32768,
                            'designated_regional_root_address': '5000.0009.0007',
                            'designated_regional_root_cost': 0,
                            'designated_regional_root_priority': 32768,
                            'designated_root_address': '5000.0009.0007',
                            'designated_root_cost': 0,
                            'designated_root_priority': 32768,
                            'name': 'Ethernet1/3',
                            'port_cost': 20000,
                            'port_id': '128.3',
                            'port_priority': 128,
                            'port_state': 'designated forwarding',
                            'timers': {
                                'forward_delay': 0,
                                'forward_transitions': 1,
                                'message_expires_in': 0
                            }
                        },
                        'Port-channel1': {
                            'counters': {
                                'bpdu_recieved': 2,
                                'bpdu_sent': 412658
                            },
                            'designated_bridge_address': '5000.0009.0007',
                            'designated_bridge_port_id': '128.4096',
                            'designated_bridge_priority': 32768,
                            'designated_regional_root_address': '5000.0009.0007',
                            'designated_regional_root_cost': 0,
                            'designated_regional_root_priority': 32768,
                            'designated_root_address': '5000.0009.0007',
                            'designated_root_cost': 0,
                            'designated_root_priority': 32768,
                            'name': 'Port-channel1',
                            'port_cost': 20000,
                            'port_id': '128.4096',
                            'port_priority': 128,
                            'port_state': 'designated forwarding',
                            'timers': {
                                'forward_delay': 0,
                                'forward_transitions': 1,
                                'message_expires_in': 0
                            }
                        }
                    },
                    'mst_id': 0,
                    'regional_root': 'this switch',
                    'root_for_cist': 'this switch',
                    'sys_id': 0,
                    'vlans_mapped': '1-9,11-19,21-29,31-39,41-4094'
                },
                1: {
                    'bridge_address': '5000.0009.0007',
                    'bridge_priority': 32769,
                    'interfaces': {
                        'Ethernet1/1': {
                            'designated_bridge_address': '5000.0009.0007',
                            'designated_bridge_port_id': '128.1',
                            'designated_bridge_priority': 32769,
                            'designated_root_address': '5000.0009.0007',
                            'designated_root_cost': 0,
                            'designated_root_priority': 32769,
                            'name': 'Ethernet1/1',
                            'port_cost': 20000,
                            'port_id': '128.1',
                            'port_priority': 128,
                            'port_state': 'designated forwarding',
                            'timers': {
                                'forward_delay': 0,
                                'forward_transitions': 1,
                                'message_expires_in': 0
                            }
                        },
                        'Port-channel1': {
                            'designated_bridge_address': '5000.0009.0007',
                            'designated_bridge_port_id': '128.4096',
                            'designated_bridge_priority': 32769,
                            'designated_root_address': '5000.0009.0007',
                            'designated_root_cost': 0,
                            'designated_root_priority': 32769,
                            'name': 'Port-channel1',
                            'port_cost': 20000,
                            'port_id': '128.4096',
                            'port_priority': 128,
                            'port_state': 'designated forwarding',
                            'timers': {
                                'forward_delay': 0,
                                'forward_transitions': 1,
                                'message_expires_in': 0
                            }
                        }
                    },
                    'mst_id': 1,
                    'sys_id': 1,
                    'vlans_mapped': '10,20,30,40'
                }
            }
        }
}
