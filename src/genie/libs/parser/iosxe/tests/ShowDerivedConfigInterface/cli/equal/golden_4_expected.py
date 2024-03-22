expected_output = {
    'derived_config': {
        'GigabitEthernet3/0/3': {
            'ip_dhcp_snooping_limit_rate': 15,
            'load_interval': 30,
            'service_policy': {
                'input': 'AutoConf-4.0-CiscoPhone-Input-Policy',
                'output': 'AutoConf-4.0-Output-Policy',
            },
            'spanning_tree': {
                'bpduguard': 'enable',
                'portfast': True,
            },
            'storm_control': {
                'action': 'trap',
                'broadcast_level_pps': '1k',
                'multicast_level_pps': '2k',
            },
            'switchport_block': 'unicast',
            'switchport_mode': 'access',
            'switchport_port_security': {
                'aging_time': 2,
                'aging_type': 'inactivity',
                'maximum': {
                    '2': {
                        'vlan': 'access',
                    },
                    '3': {
                    },
                },
                'switchport_port_security': True,
                'violation': 'restrict',
            }
        }
    }
}