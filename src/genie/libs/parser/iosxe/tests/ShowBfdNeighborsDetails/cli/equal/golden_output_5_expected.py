expected_output = {
    'our_address': {
        '10.50.10.106': {
            'neighbor_address': {
                '10.50.10.100': {
                    'ld_rd': '23/14',
                    'rh_rs': 'Up',
                    'state': 'Up',
                    'interface': 'GigabitEthernet1/0/19',
                    'ld': 23,
                    'rd': 14,
                    'session': {
                        'state': 'UP',
                        'echo_function': True,
                        'echo_interval_ms': 2000
                    },
                    'session_host': 'Software',
                    'handle': 3,
                    'local_diag': 0,
                    'demand_mode': 0,
                    'poll_bit': 0,
                    'min_tx_int': 1000000,
                    'min_rx_int': 1000000,
                    'multiplier': 3,
                    'received_min_rx_int': 1000000,
                    'received_multiplier': 6,
                    'holddown': 0,
                    'holddown_hits': 0,
                    'hello': 1000,
                    'hello_hits': 41511,
                    'rx': {
                        'count': 41515,
                        'min_int_ms': 1,
                        'max_int_ms': 1004,
                        'avg_int_ms': 877,
                        'last_ms_ago': 296
                    },
                    'tx': {
                        'count': 41513,
                        'min_int_ms': 1,
                        'max_int_ms': 1004,
                        'avg_int_ms': 880,
                        'last_ms_ago': 578
                    },
                    'echo_rx': {
                        'count': 20777,
                        'min_int_ms': 1505,
                        'max_int_ms': 2003,
                        'avg_int_ms': 1751,
                        'last_ms_ago': 721
                    },
                    'echo_tx': {
                        'count': 20777,
                        'min_int_ms': 1506,
                        'max_int_ms': 2003,
                        'avg_int_ms': 1751,
                        'last_ms_ago': 722
                    },
                    'elapsed_time_watermarks': '0 0',
                    'elapsed_time_watermarks_last': 0,
                    'registered_protocols': [
                        'OSPF',
                        'CEF'
                    ],
                    'up_time': '10:07:15',
                    'last_packet': {
                        'version': 1,
                        'diagnostic': 0,
                        'state_bit': 'Up',
                        'demand_bit': 0,
                        'poll_bit': 0,
                        'final_bit': 0,
                        'c_bit': 0,
                        'multiplier': 6,
                        'length': 24,
                        'my_discr': 14,
                        'your_discr': 23,
                        'min_tx_int': 1000000,
                        'min_rx_int': 1000000,
                        'min_echo_int': 2000000
                    }
                }
            }
        }
    }
}
