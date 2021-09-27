

expected_output = {
    'interfaces': {
        'Port-channel1': {
            'last_update_success': True,
            'total_ports': 2,
            'up_ports': 2,
            'first_oper_port': 'Ethernet1/1',
            'port_channel_age': '0d:02h:31m:22s',
            'time_last_bundle': '0d:02h:28m:30s',
            'last_bundled_member': 'Ethernet1/2',
            'members': {
                'Ethernet1/1': {
                    'activity': 'active',
                    'status': 'up',
                    'is_first_oper_port': True
                },
                'Ethernet1/2': {
                    'activity': 'active',
                    'status': 'up',
                    'is_first_oper_port': False
                }
            }
        },
        'Port-channel2': {
            'last_update_success': True,
            'total_ports': 3,
            'up_ports': 2,
            'first_oper_port': 'Ethernet1/4',
            'port_channel_age': '0d:02h:27m:37s',
            'time_last_bundle': '0d:00h:12m:50s',
            'last_bundled_member': 'Ethernet1/5',
            'time_last_unbundle': '0d:00h:14m:05s',
            'last_unbundled_member': 'Ethernet1/5',
            'members': {
                'Ethernet1/3': {
                    'activity': 'passive',
                    'status': 'up',
                    'is_first_oper_port': False
                },
                'Ethernet1/4': {
                    'activity': 'passive',
                    'status': 'up',
                    'is_first_oper_port': True
                },
                'Ethernet1/5': {
                    'activity': 'passive',
                    'status': 'hot-standy',
                    'is_first_oper_port': False
                }
            }
        }
    }
}
