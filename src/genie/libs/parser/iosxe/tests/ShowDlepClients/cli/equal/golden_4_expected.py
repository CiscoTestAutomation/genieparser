expected_output = {
    'interface': {
        'GigabitEthernet1': {
            'dlep_local_radio': {
                'description': 'radio_4',
                'ip_address': '9.9.9.2',
                'neighbour_timers_in_seconds': {
                    'activity_timeout': 0,
                    'neighbor_down_ack': 10
                },
                'peer_id': 271,
                'peer_timers_in_milliseconds': {
                    'dead_interval': 10000,
                    'heartbeat': 5000,
                    'terminate_ack': 20000
                },
                'supported_metrics': {
                    'link_cdr_rx_metric_in_bps': 100000000,
                    'link_cdr_tx_metric_in_bps': 100000000,
                    'link_latency_metric_in_microseconds': 250,
                    'link_mdr_rx_metric_in_bps': 100000000,
                    'link_mdr_tx_metric_in_bps': 100000000,
                    'link_mtu_metric': 100,
                    'link_resources_metric': 100,
                    'link_rlq_rx_metric': 100,
                    'link_rlq_tx_metric': 100
                },
                'tcp_port': 858,
                'tcp_socket_fd': 1,
                'virtual_template': 1
            },
            'dlep_server': {
                'ip_address': '9.9.9.1',
                'udp_port': 11113,
                'udp_socket': 0
            }
        }
    }
}