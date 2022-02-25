expected_output = {
    'active_startup_time': 0,
    'bulksync_time': 0,
    'copy_to_running_config_time': 0,
    'last_configuration_file_parsed': {'number_of_commands': 0, 'time': '0'},
    'parser_cache': {'hits': '856', 'misses': '1245', 'status': 'enabled'},
    'parser_last_bootup_cache_hits': {
        'bootup_clear_parser_cache': 0,
        'bootup_hits': 0,
        'bootup_misses': 0
    },
    'standby_startup_time': 0,
    'top_10_slowest_command': {
        1: {'command': 'copy ' 'flash:/BTRACE__C9300-48P__000001__',
            'date': '2022/01/14',
            'function': '0x5604C4273080',
            'time': 1191,
            'time_with_seconds': '04:02:51.818',
            'time_zone': 'UTC'
        },
        2: {'command': 'verify /md5 ''flash:cat9k-rpboot.BLD_POLA',
            'date': '2022/01/14',
            'function': '0x5604C4279D90',
            'time': 1530,
            'time_with_seconds': '04:00:45.563',
            'time_zone': 'UTC'
        },
        3: {'command': 'ping vrf Mgmt-vrf 10.106.16.20',
            'date': '2022/01/25',
            'function': '0x5604C400CCC0',
            'time': 2002,
            'time_with_seconds': '06:18:53.303',
            'time_zone': 'UTC'
        },
        4: {'command': 'delete /force /recursive ''crashinfo:/tra',
            'date': '2022/01/14',
            'function': '0x5604C4278BF0',
            'time': 2866,
            'time_with_seconds': '04:01:38.300',
            'time_zone': 'UTC'
        },
        5: {'command': 'install remove inactive',
            'date': '2022/01/25',
            'function': '0x5604C03ACC10',
            'time': 2912,
            'time_with_seconds': '06:37:08.655',
            'time_zone': 'UTC'
        },
        6: {'command': 'request platform software crft ''collect',
            'date': '2022/01/14',
            'function': '0x5604C03ACC10',
            'time': 3458,
            'time_with_seconds': '04:01:30.205',
            'time_zone': 'UTC'
        },
        7: {'command': 'install remove inactive',
            'date': '2022/01/14',
            'function': '0x5604C03ACC10',
            'time': 3732,
            'time_with_seconds': '03:56:34.759',
            'time_zone': 'UTC'
        },
        8: {'command': 'install remove inactive',
            'date': '2022/01/14',
            'function': '0x5604C03ACC10',
            'time': 3807,
            'time_with_seconds': '03:58:51.311',
            'time_zone': 'UTC'
        },
        9: {'command': 'request platform software trace ''archive',
            'date': '2022/01/14',
            'function': '0x5604C03ACC10',
            'time': 24053,
            'time_with_seconds': '04:02:48.595',
            'time_zone': 'UTC'
        },
        10: {'command': 'copy ''tftp://10.106.16.20//auto/tftp-blr',
            'date': '2022/01/25',
            'function': '0x5604C4273080',
            'time': 138291,
            'time_with_seconds': '06:45:20.381',
            'time_zone': 'UTC'
        }
    }
}
