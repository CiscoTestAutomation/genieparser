expected_output = {
    'interfaces': {
        'GigabitEthernet0/0': {
            'name': '',
            'link_status': False,
            'line_protocol': True,
            'interface_state': True,
            'config_status': False,
            'config_issue': 'nameif',
            'control_point_states': {
                'interface': {
                    'interface_number': 3,
                    'interface_config_status': 'active',
                    'interface_state': 'not active'
                }
            }
        },
        'GigabitEthernet0/1': {
            'name': '',
            'link_status': False,
            'line_protocol': True,
            'interface_state': True,
            'config_status': False,
            'config_issue': 'nameif',
            'control_point_states': {
                'interface': {
                    'interface_number': 4,
                    'interface_config_status': 'active',
                    'interface_state': 'not active'
                }
            }
        },
        'GigabitEthernet0/2': {
            'name': '',
            'link_status': False,
            'line_protocol': True,
            'interface_state': True,
            'config_status': False,
            'config_issue': 'nameif',
            'control_point_states': {
                'interface': {
                    'interface_number': 5,
                    'interface_config_status': 'active',
                    'interface_state': 'not active'
                }
            }
        },
        'GigabitEthernet0/3': {
            'name': '',
            'link_status': False,
            'line_protocol': True,
            'interface_state': True,
            'config_status': False,
            'config_issue': 'nameif',
            'control_point_states': {
                'interface': {
                    'interface_number': 6,
                    'interface_config_status': 'active',
                    'interface_state': 'not active'
                }
            }
        },
        'GigabitEthernet0/4': {
            'name': '',
            'link_status': False,
            'line_protocol': True,
            'interface_state': True,
            'config_status': False,
            'config_issue': 'nameif',
            'control_point_states': {
                'interface': {
                    'interface_number': 7,
                    'interface_config_status': 'active',
                    'interface_state': 'not active'
                }
            }
        },
        'GigabitEthernet0/5': {
            'name': '',
            'link_status': False,
            'line_protocol': True,
            'interface_state': True,
            'config_status': False,
            'config_issue': 'nameif',
            'control_point_states': {
                'interface': {
                    'interface_number': 8,
                    'interface_config_status': 'active',
                    'interface_state': 'not active'
                }
            }
        },
        'GigabitEthernet0/6': {
            'name': '',
            'link_status': False,
            'line_protocol': True,
            'interface_state': True,
            'config_status': False,
            'config_issue': 'nameif',
            'control_point_states': {
                'interface': {
                    'interface_number': 9,
                    'interface_config_status': 'active',
                    'interface_state': 'not active'
                }
            }
        },
        'Internal-Data0/0': {
            'name': 'nlp_int_tap',
            'link_status': True,
            'line_protocol': True,
            'interface_state': True,
            'config_status': True,
            'mac_address': '0000.01ff.0001',
            'mtu': 1500,
            'ipv4': {
                '169.254.1.1': {
                    'ip': '169.254.1.1'
                }
            },
            'subnet': '255.255.255.248',
            'traffic_statistics': {
                'packets_input': 10,
                'bytes_input': 756,
                'packets_output': 5,
                'bytes_output': 300,
                'packets_dropped': 10
            },
            'control_point_states': {
                'interface': {
                    'interface_number': 10,
                    'interface_config_status': 'active',
                    'interface_state': 'active'
                }
            }
        },
        'Management0/0': {
            'name': 'management',
            'link_status': True,
            'line_protocol': True,
            'interface_state': True,
            'config_status': True,
            'mac_address': '5254.00ff.bbcd',
            'mtu': 1500,
            'ipv4': {
                '10.224.128.27': {
                    'ip': '10.224.128.27'
                }
            },
            'subnet': '255.255.254.0',
            'traffic_statistics': {
                'packets_input': 1872,
                'bytes_input': 131463,
                'packets_output': 2486,
                'bytes_output': 283239,
                'packets_dropped': 214
            },
            'control_point_states': {
                'interface': {
                    'interface_number': 2,
                    'interface_config_status': 'active',
                    'interface_state': 'active'
                }
            }
        }
    }
}