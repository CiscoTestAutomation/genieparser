expected_output = {
    'last_configuration_file_parsed': {
        'number_of_commands': 15,
        'time': '5'
    },
    'parser_cache': {
        'status': 'enabled',
        'hits': '253',
        'misses': '890'
    },
    'active_startup_time': 0,
    'standby_startup_time': 0,
    'copy_to_running_config_time': 0,
    'bulksync_time': 233,
    'top_10_slowest_command': {
        1: {
            'function': '0x562ECABA2200',
            'time': 112,
            'command': 'show file systems'
        },
        2: {
            'function': '0x562ECABA2200',
            'time': 112,
            'command': 'show file systems'
        },
        3: {
            'function': '0x562ECCCB5A50',
            'time': 206,
            'command': 'vrf forwarding Mgmt-vrf'
        },
        4: {
            'function': '0x562ECA487050',
            'time': 310,
            'command': 'show running-config all'
        },
        5: {
            'function': '0x562ECABA8120',
            'time': 944,
            'command': 'dir flash:'
        },
        6: {
            'function': '0x562ECABA8120',
            'time': 949,
            'command': 'dir flash:'
        },
        7: {
            'function': '0x562ECA481F40',
            'time': 1340,
            'command': 'en'
        },
        8: {
            'function': '0x562ECA481F40',
            'time': 1725,
            'command': 'en'
        },
        9: {
            'function': '0x562ECA397150',
            'time': 4257,
            'command': 'connect 3'
        },
        10: {
            'function': '0x562EC582FFD0',
            'time': 6614,
            'command': 'show version running'
        }
    },
    'parser_last_bootup_cache_hits': {
        'bootup_hits': 75,
        'bootup_misses': 414,
        'bootup_clear_parser_cache': 21
    }
}