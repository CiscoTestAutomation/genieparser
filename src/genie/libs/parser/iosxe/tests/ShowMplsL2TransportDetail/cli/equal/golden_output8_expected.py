expected_output={
    'interface': {
        'GigabitEthernet2.2': {
            'status': 'up',
            'line_protocol_status': 'up',
            'ethernet_vlan': {
                '10/101': {
                    'status': 'up'
                }
            },
            'destination_address': {
                '10.0.0.1': {
                    'vc_id': {
                        '2': {
                            'vc_status': 'up'
                        }
                    },
                    'output_interface': 'GigabitEthernet1',
                    'imposed_label_stack': '{16 16}',
                    'preferred_path': 'not configured',
                    'default_path': 'active',
                    'next_hop': '100.2.0.1'
                }
            },
            'create_time': '00:16:21',
            'last_status_change_time': '00:00:48',
            'last_label_fsm_state_change_time': '00:03:51',
            'signaling_protocol': {
                'LDP': {
                    'peer_id': '10.0.0.1:0',
                    'peer_state': 'up',
                    'targeted_hello_ip': '10.0.0.3',
                    'id': '10.0.0.1',
                    'status': 'UP',
                    'mpls_vc_labels': {
                        'local': '16',
                        'remote': '16'
                    },
                    'group_id': {
                        'local': '7',
                        'remote': '0'
                    },
                    'mtu': {
                        'local': '1500',
                        'remote': '1500'
                    }
                }
            },
            'graceful_restart': 'not configured and not enabled',
            'non_stop_routing': 'not configured and not enabled',
            'status_tlv_support': 'enabled/supported',
            'ldp_route_enabled': 'enabled',
            'label_state_machine': 'established, LruRru',
            'last_status_name': {
                'local_dataplane': {
                    'received': 'No fault'
                },
                'bfd_dataplane': {
                    'received': 'Not sent'
                },
                'bfd_peer_monitor': {
                    'received': 'No fault'
                },
                'local_ac__circuit': {
                    'received': 'No fault',
                    'sent': 'No fault'
                },
                'local_pw_if_circ': {
                    'received': 'No fault'
                },
                'local_ldp_tlv': {
                    'sent': 'No fault'
                },
                'remote_ldp_tlv': {
                    'received': 'No fault'
                },
                'remote_ldp_adj': {
                    'received': 'No fault'
                }
            },
            'sequencing': {
                'received': 'disabled',
                'sent': 'disabled'
            },
            'statistics': {
                'packets': {
                    'received': 20,
                    'sent': 20
                },
                'bytes': {
                    'received': 2720,
                    'sent': 2800
                },
                'packets_drop': {
                    'received': 0,
                    'seq_error': 0,
                    'sent': 0
                }
            }
        }
    }
}