expected_output = {
    'interface': {
        'GigabitEthernet0/0/0': {
            'dlep_local': {
                'ip_address': '9.9.9.11',
                'udp_port': 11111,
                'udp_socket': 0
            },
            'sid': {
                'addresses': {
                    'associated_interface': 'Virtual-Access2',
                    'ipv4': '9.9.9.1',
                    'ipv6_ll': 'FE80::20C:29FF:FED4:B578'
                },
                'mac_address': '000c.29d4.b578',
                'sid_id': 2153,
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