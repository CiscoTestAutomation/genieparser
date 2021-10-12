

expected_output = {
    'interfaces': {
        'Port-channel10': {
            'first_oper_port': 'Ethernet1/26',
            'last_bundled_member': 'Ethernet1/26',
            'last_update_success': True,
            'members': {
                'Ethernet1/25': {
                    'activity': 'on',
                    'is_first_oper_port': False,
                    'status': 'up'
                },
                'Ethernet1/26': {
                    'activity': 'on',
                    'is_first_oper_port': True,
                    'status': 'up'
                }
            },
            'port_channel_age': '0d:00h:13m:14s',
            'time_last_bundle': '0d:00h:13m:10s',
            'total_ports': 2,
            'up_ports': 2
        },
        'Port-channel100': {
            'first_oper_port': 'Ethernet1/5',
            'last_bundled_member': 'Ethernet1/5',
            'last_update_success': True,
            'members': {
                'Ethernet1/5': {
                    'activity': 'active',
                    'is_first_oper_port': True,
                    'status': 'up'
                }
            },
            'port_channel_age': '0d:00h:12m:30s',
            'time_last_bundle': '0d:00h:12m:30s',
            'total_ports': 1,
            'up_ports': 1
        },
        'Port-channel200': {
            'first_oper_port': 'Ethernet1/6',
            'last_bundled_member': 'Ethernet1/6',
            'last_update_success': True,
            'members': {
                'Ethernet1/6': {
                    'activity': 'active',
                    'is_first_oper_port': True,
                    'status': 'up'
                }
            },
            'port_channel_age': '0d:00h:12m:25s',
            'time_last_bundle': '0d:00h:12m:25s',
            'total_ports': 1,
            'up_ports': 1
        }
    }
}
