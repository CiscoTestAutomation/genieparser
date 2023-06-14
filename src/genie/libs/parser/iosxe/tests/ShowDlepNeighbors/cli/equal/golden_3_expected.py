expected_output = {
    'interface': {
        'GigabitEthernet1': {
            'dlep_local': {
                'ip_address': '9.9.9.1',
                'udp_port': 11113,
                'udp_socket': 0
            },
            'sid': {
                'addresses': {
                    'associated_interface': 'Virtual-Access2',
                    'ipv4': '9.9.9.11',
                    'ipv6_ll': 'FE80::8AFC:5DFF:FE32:900'
                },
                'mac_address': '88fc.5d32.0900',
                'sid_id': 2372,
                'supported_metrics': {
                    'cdr_rx_metric_in_bps': 100000000,
                    'cdr_tx_metric_in_bps': 100000000,
                    'latency_metric_in_microseconds': 250,
                    'mdr_rx_metric_in_bps': 100000000,
                    'mdr_tx_metric_in_bps': 100000000,
                    'mtu_metric': 1500,
                    'resources_metric': 100,
                    'rlq_rx_metric': 100,
                    'rlq_tx_metric': 100
                }
            }
        }
    }
}