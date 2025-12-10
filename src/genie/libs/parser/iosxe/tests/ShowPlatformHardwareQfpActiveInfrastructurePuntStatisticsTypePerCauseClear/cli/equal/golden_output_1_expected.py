expected_output = {
    'global_per_cause_statistics': {
        'number_of_punt_causes': 165,
        'per_punt_cause_statistics': {
            '003': {
                'counter_id': '003',
                'punt_cause_name': 'Layer2 control and legacy',
                'packets_received': 859,
                'packets_transmitted': 859,
            },
            '007': {
                'counter_id': '007',
                'punt_cause_name': 'ARP request or response',
                'packets_received': 2424,
                'packets_transmitted': 2424,
            },
            '021': {
                'counter_id': '021',
                'punt_cause_name': 'RP<->QFP keepalive',
                'packets_received': 303,
                'packets_transmitted': 303,
            },
            '055': {
                'counter_id': '055',
                'punt_cause_name': 'For-us control',
                'packets_received': 4,
                'packets_transmitted': 4,
            },
        }
    },
    'per_inject_cause_statistics': {
        'number_of_inject_causes': 56,
        'per_inject_cause_statistics': {
            '005': {
                'counter_id': '005',
                'inject_cause_name': 'QFP <->RP keepalive',
                'packets_received': 303,
                'packets_transmitted': 0,
            },
            '007': {
                'counter_id': '007',
                'inject_cause_name': 'QFP adjacency-id lookup',
                'packets_received': 3,
                'packets_transmitted': 3,
            },
        }
    }
}