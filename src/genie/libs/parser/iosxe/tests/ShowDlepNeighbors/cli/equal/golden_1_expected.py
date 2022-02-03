expected_output = {
    'interface': {
        'GigabitEthernet3': {
            'dlep_server': {
                'ip_address': '9.9.9.11',
                'udp_port': 11111,
                'udp_socket': 0
            },
            'sid': {
                'sid_id': 2154,
                'mac_address': '0050.56bd.7503',
                'addresses': {
                    'ipv4': '9.9.9.1',
                    'ipv6_ll': 'FE80::21E:BDFF:FE08:5000'
                },
                'supported_metrics': {
                    'rlq_rx_metric': 100,
                    'rlq_tx_metric': 100,
                    'resources_metric': 100,
                    'mtu_metric': 1500,
                    'latency_metric_in_microseconds': 250,
                    'cdr_rx_metric_in_bps': 100000000,
                    'cdr_tx_metric_in_bps': 100000000,
                    'mdr_rx_metric_in_bps': 100000000,
                    'mdr_tx_metric_in_bps': 100000000
                }
            }
        },
        'GigabitEthernet5': {
            'dlep_server': {
                'ip_address': '8.8.8.11',
                'udp_port': 11115,
                'udp_socket': 2
            },
            'sid': {
                'sid_id': 2155,
                'mac_address': '0050.56bd.0174',
                'addresses': {
                    'ipv4': '8.8.8.1',
                    'ipv6_ll': 'FE80::21E:BDFF:FE08:5000'
                },
                'supported_metrics': {
                    'rlq_rx_metric': 100,
                    'rlq_tx_metric': 100,
                    'resources_metric': 100,
                    'mtu_metric': 1500,
                    'latency_metric_in_microseconds': 250,
                    'cdr_rx_metric_in_bps': 100000000,
                    'cdr_tx_metric_in_bps': 100000000,
                    'mdr_rx_metric_in_bps': 100000000,
                    'mdr_tx_metric_in_bps': 100000000
                }
            }
        }
    }
}