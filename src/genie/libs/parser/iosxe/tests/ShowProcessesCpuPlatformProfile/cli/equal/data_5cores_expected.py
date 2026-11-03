expected_output = {
    'cpu_utilization': {
        'cpu_util_five_secs': '10%',
        'cpu_util_one_min': '20%',
        'cpu_util_five_min': '18%',
        'core': {
            'Core 3': {
                'core_cpu_util_five_secs': '0%',
                'core_cpu_util_one_min': '0%',
                'core_cpu_util_five_min': '0%',
            },
            'Core 4': {
                'core_cpu_util_five_secs': '16%',
                'core_cpu_util_one_min': '28%',
                'core_cpu_util_five_min': '30%',
            },
            'Core 5': {
                'core_cpu_util_five_secs': '2%',
                'core_cpu_util_one_min': '14%',
                'core_cpu_util_five_min': '12%',
            },
            'Core 6': {
                'core_cpu_util_five_secs': '30%',
                'core_cpu_util_one_min': '51%',
                'core_cpu_util_five_min': '43%',
            },
            'Core 7': {
                'core_cpu_util_five_secs': '6%',
                'core_cpu_util_one_min': '7%',
                'core_cpu_util_five_min': '7%',
            },
        },
    },
    'plane_process_utilization': {
        'cpu_util_five_secs': '42%',
        'cpu_util_one_min': '86%',
        'cpu_util_five_min': '78%',
    },
    'pid': {
        '19590': {
            'ppid': 19580,
            'five_sec': '149%',
            'one_min': '149%',
            'five_min': '146%',
            'status': 'S',
            'size': 290944,
            'name': 'ucode_pkt_PPE0',
        },
        '19580': {
            'ppid': 18844,
            'five_sec': '0%',
            'one_min': '0%',
            'five_min': '0%',
            'status': 'S',
            'size': 2824,
            'name': 'pman',
        },
    },
}
