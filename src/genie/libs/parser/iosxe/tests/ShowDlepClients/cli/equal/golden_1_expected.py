expected_output = {
    'interface': {
        'GigabitEthernet3': {
            'dlep_server': {
                'ip_address': '9.9.9.11',
                'udp_port': 11111,
                'udp_socket': 0
            },
            'dlep_client': {
                'ip_address': '9.9.9.12',
                'tcp_port': 859,
                'tcp_socket_fd': 1,
                'peer_id': 6,
                'virtual_template': 1,
                'description': 'radio_1',
                'peer_timers_in_milliseconds': {
                    'heartbeat': 5000,
                    'dead_interval': 10000,
                    'terminate_ack': 20000
                },
                'neighbour_timers_in_seconds': {
                    'activity_timeout': 0,
                    'neighbor_down_ack': 10
                },
                'supported_metrics': {
                    'link_rlq_rx_metric': 100,
                    'link_rlq_tx_metric': 100,
                    'link_resources_metric': 100,
                    'link_mtu_metric': 100,
                    'link_latency_metric_in_microseconds': 250,
                    'link_cdr_rx_metric_in_bps': 100000000,
                    'link_cdr_tx_metric_in_bps': 100000000,
                    'link_mdr_rx_metric_in_bps': 100000000,
                    'link_mdr_tx_metric_in_bps': 100000000
                }
            }
        },
        'GigabitEthernet5': {
            'dlep_server': {
                'ip_address': '8.8.8.11',
                'udp_port': 11115,
                'udp_socket': 2
            },
            'dlep_client': {
                'ip_address': '8.8.8.12',
                'tcp_port': 856,
                'tcp_socket_fd': 3,
                'peer_id': 5,
                'virtual_template': 2,
                'description': 'radio_2',
                'peer_timers_in_milliseconds': {
                    'heartbeat': 5000,
                    'dead_interval': 10000,
                    'terminate_ack': 20000
                },
                'neighbour_timers_in_seconds': {
                    'activity_timeout': 0,
                    'neighbor_down_ack': 10
                },
                'supported_metrics': {
                    'link_rlq_rx_metric': 100,
                    'link_rlq_tx_metric': 100,
                    'link_resources_metric': 100,
                    'link_mtu_metric': 100,
                    'link_latency_metric_in_microseconds': 250,
                    'link_cdr_rx_metric_in_bps': 100000000,
                    'link_cdr_tx_metric_in_bps': 100000000,
                    'link_mdr_rx_metric_in_bps': 100000000,
                    'link_mdr_tx_metric_in_bps': 100000000
                }
            }
        }
    }
}
