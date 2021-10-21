

expected_output = {
    'rapid_pvst': {
        'forwarding_delay': 15,
        'hello_time': 2,
        'max_age': 20,
        'vlans': {
            109: {
                'bridge_address': '0023.04ff.ad0e',
                'bridge_priority': 20480,
                'bridge_sysid': 109,
                'interfaces': {
                    'Port-channel101': {
                        'cost': 1,
                        'counters': {
                            'bpdu_received': 0,
                            'bpdu_sent': 231106
                        },
                        'designated_bridge_address': '0026.98ff.e460',
                        'designated_bridge_priority': 20589,
                        'designated_path_cost': 0,
                        'designated_port_id': '128.4196',
                        'designated_root_address': '0023.04ff.ad0e',
                        'designated_root_priority': 20589,
                        'internal': False,
                        'link_type': 'shared',
                        'name': 'Port-channel101',
                        'number_of_forward_transitions': 0,
                        'port_identifier': '128.4196',
                        'port_num': 4196,
                        'port_priority': 128,
                        'status': 'designated',
                        'timers': {
                            'forward_delay': 0,
                            'hold': 0,
                            'message_age': 0
                        }
                    },
                    'Port-channel31': {
                        'cost': 2,
                        'counters': {
                            'bpdu_received': 3245744,
                            'bpdu_sent': 3245614
                        },
                        'designated_bridge_address': '0026.98ff.e460',
                        'designated_bridge_priority': 0,
                        'designated_path_cost': 0,
                        'designated_port_id': '128.4126',
                        'designated_root_address': '0023.04ff.ad0e',
                        'designated_root_priority': 20589,
                        'internal': False,
                        'link_type': 'point-to-point',
                        'name': 'Port-channel31',
                        'number_of_forward_transitions': 1,
                        'port_identifier': '128.4126',
                        'port_num': 4126,
                        'port_priority': 128,
                        'port_type': 'network',
                        'status': 'root',
                        'timers': {
                            'forward_delay': 0,
                            'hold': 0,
                            'message_age': 3
                        }
                    },
                   'Port-channel99': {
                        'cost': 1,
                        'counters': {
                            'bpdu_received': 0,
                            'bpdu_sent': 2725887
                        },
                        'designated_bridge_address': '0026.98ff.e460',
                        'designated_bridge_priority': 20589,
                        'designated_path_cost': 0,
                        'designated_port_id': '128.4194',
                        'designated_root_address': '0023.04ff.ad0e',
                        'designated_root_priority': 20589,
                        'internal': False,
                        'link_type': 'point-to-point',
                        'name': 'Port-channel99',
                        'number_of_forward_transitions': 0,
                        'port_identifier': '128.4194',
                        'port_num': 4194,
                        'port_priority': 128,
                        'root_guard': True,
                        'status': 'designated',
                        'timers': {
                            'forward_delay': 0,
                            'hold': 0,
                            'message_age': 0
                        }
                    }
                },
                'root_of_the_spanning_tree': True,
                'time_since_topology_change': '126:41:16',
                'timers': {
                    'hello': 0,
                    'notification': 0,
                    'topology_change': 0
                },
                'times': {
                    'forwarding_delay': 15,
                    'hello': 2,
                    'hold': 1,
                    'max_age': 20,
                    'notification': 2,
                    'topology_change': 35
                },
                'topology_change_flag': False,
                'topology_changes': 8,
                'topology_detected_flag': False,
                'topology_from_port': 'port-channel31',
                'vlan_id': 109
            },
            110: {
                'bridge_address': '0023.04ff.ad0e',
                'bridge_priority': 20480,
                'bridge_sysid': 110,
                'interfaces': {
                    'Port-channel31': {
                    'cost': 2,
                    'counters': {
                        'bpdu_received': 3245745,
                        'bpdu_sent': 3245614
                    },
                    'designated_bridge_address': '0026.98ff.e460',
                    'designated_bridge_priority': 0,
                    'designated_path_cost': 0,
                    'designated_port_id': '128.4126',
                    'designated_root_address': '0023.04ff.ad0e',
                    'designated_root_priority': 20590,
                    'internal': False,
                    'link_type': 'point-to-point',
                    'name': 'Port-channel31',
                    'number_of_forward_transitions': 1,
                    'port_identifier': '128.4126',
                    'port_num': 4126,
                    'port_priority': 128,
                    'port_type': 'network',
                    'status': 'root',
                    'timers': {
                        'forward_delay': 0,
                        'hold': 0,
                        'message_age': 3
                        }
                    },
                   'Port-channel99': {
                        'cost': 1,
                        'counters': {
                            'bpdu_received': 0,
                            'bpdu_sent': 2725886
                        },
                        'designated_bridge_address': '0026.98ff.e460',
                        'designated_bridge_priority': 20590,
                        'designated_path_cost': 0,
                        'designated_port_id': '128.4194',
                        'designated_root_address': '0023.04ff.ad0e',
                        'designated_root_priority': 20590,
                        'internal': False,
                        'link_type': 'point-to-point',
                        'name': 'Port-channel99',
                        'number_of_forward_transitions': 0,
                        'port_identifier': '128.4194',
                        'port_num': 4194,
                        'port_priority': 128,
                        'root_guard': True,
                        'status': 'designated',
                        'timers': {
                            'forward_delay': 0,
                            'hold': 0,
                            'message_age': 0
                        }
                    }
                },
                'root_of_the_spanning_tree': True,
                'time_since_topology_change': '123:32:30',
                'timers': {
                    'hello': 0,
                    'notification': 0,
                    'topology_change': 0
                },
                'times': {
                    'forwarding_delay': 15,
                    'hello': 2,
                    'hold': 1,
                    'max_age': 20,
                    'notification': 2,
                    'topology_change': 35
                },
                'topology_change_flag': False,
                'topology_changes': 9,
                'topology_detected_flag': False,
                'topology_from_port': 'port-channel31',
                'vlan_id': 110
            },
            122: {
                'bridge_address': '0023.04ff.ad0e',
                'bridge_priority': 20480,
                'bridge_sysid': 122,
                'interfaces': {
                    'Port-channel31': {
                        'cost': 2,
                        'counters': {  
                            'bpdu_received': 3245745,
                            'bpdu_sent': 3245614
                        },
                        'designated_bridge_address': '0026.98ff.e460',
                        'designated_bridge_priority': 0,
                        'designated_path_cost': 0,
                        'designated_port_id': '128.4126',
                        'designated_root_address': '0023.04ff.ad0e',
                        'designated_root_priority': 20602,
                        'internal': False,
                        'link_type': 'point-to-point',
                        'name': 'Port-channel31',
                        'number_of_forward_transitions': 1,
                        'port_identifier': '128.4126',
                        'port_num': 4126,
                        'port_priority': 128,
                        'port_type': 'network',
                        'status': 'root',
                        'timers': {
                            'forward_delay': 0,
                            'hold': 0,
                            'message_age': 3
                        }
                    },
                    'Port-channel99': {
                        'cost': 1,
                        'counters': {
                            'bpdu_received': 0,
                            'bpdu_sent': 2725887
                        },
                        'topology_change': True,
                        'designated_bridge_address': '0026.98ff.e460',
                        'designated_bridge_priority': 20602,
                        'designated_path_cost': 0,
                        'designated_port_id': '128.4194',
                        'designated_root_address': '0023.04ff.ad0e',
                        'designated_root_priority': 20602,
                        'internal': False,
                        'link_type': 'point-to-point',
                        'name': 'Port-channel99',
                        'number_of_forward_transitions': 0,
                        'port_identifier': '128.4194',
                        'port_num': 4194,
                        'port_priority': 128,
                        'root_guard': True,
                        'status': 'designated',
                        'timers': {
                            'forward_delay': 0,
                            'hold': 0,
                            'message_age': 0
                        }
                    }
                },
                'time_since_topology_change': '123:10:02',
                'timers': {
                    'hello': 0,
                    'notification': 0,
                    'topology_change': 0
                },
                'times': {
                    'forwarding_delay': 15,
                    'hello': 2,
                    'hold': 1,
                    'max_age': 20,
                    'notification': 2,
                    'topology_change': 35
                },
                'topology_change_flag': False,
                'topology_changes': 9,
                'topology_detected_flag': False,
                'topology_from_port': 'port-channel31',
                'vlan_id': 122
            }
        }
    }
}
