expected_output = {
    'policy_id': 'lp00003',
    'policy_name': 'infra-2-ptrace',
    'policy_severity': 'INFO',
    'policy_event': 'Process attempted to perform ptrace operations without sufficient privileges',
    'event_history': {
        1: {
            'time': '07:40:51.318 UTC Thu Sep 17 2026',
            'mode': 'monitor',
            'process': '/usr/bin/strace',
        },
        2: {
            'time': '07:40:51.318 UTC Thu Sep 17 2026',
            'mode': 'monitor',
            'process': '/usr/bin/strace',
        },
        3: {
            'time': '07:40:51.319 UTC Thu Sep 17 2026',
            'mode': 'monitor',
            'process': '/usr/bin/strace',
        },
        4: {
            'time': '10:03:09.479 UTC Fri Sep 18 2026',
            'mode': 'enforce',
            'process': '/usr/bin/strace',
        },
        5: {
            'time': '10:03:09.479 UTC Fri Sep 18 2026',
            'mode': 'enforce',
            'process': '/usr/bin/strace',
        },
        6: {
            'time': '10:03:09.480 UTC Fri Sep 18 2026',
            'mode': 'enforce',
            'process': '/usr/bin/strace',
        },
        7: {
            'time': '10:03:09.481 UTC Fri Sep 18 2026',
            'mode': 'monitor',
            'process': '/usr/bin/my process',
        },
    },
}
