expected_output = {
    "interface": {
        "TenGigabitEthernet0/0/1": {
            "dlep_server": {
                "ip_address": "19.19.19.151",
                "udp_port": 55113,
                "udp_socket": 0
            },
            "dlep_local_radio": {
                "ip_address": "19.19.19.121",
                "tcp_port": 9121,
                "tcp_socket_fd": 1,
                "peer_id": 1,
                "virtual_template": 1,
                "description": "radio_9",
                "peer_timers_in_milliseconds": {
                    "heartbeat": 5000,
                    "dead_interval": 10000,
                    "terminate_ack": 20000
                },
                "neighbour_timers_in_seconds": {
                    "neighbor_down_ack": 10
                },
                "supported_metrics": {
                    "link_rlq_rx_metric": 100,
                    "link_rlq_tx_metric": 100,
                    "link_resources_metric": 100,
                    "link_mtu_metric": 100,
                    "link_latency_metric_in_microseconds": 250,
                    "link_cdr_rx_metric_in_bps": 100000000,
                    "link_cdr_tx_metric_in_bps": 100000000,
                    "link_mdr_rx_metric_in_bps": 100000000,
                    "link_mdr_tx_metric_in_bps": 100000000
                }
            }
        },
        "TenGigabitEthernet0/0/2.200": {
            "dlep_server": {
                "ip_address": "18.18.18.111",
                "udp_port": 21115,
                "udp_socket": 2
            },
            "dlep_local_radio": {
                "ip_address": "18.18.18.112",
                "tcp_port": 8111,
                "tcp_socket_fd": 3,
                "peer_id": 2,
                "virtual_template": 2,
                "description": "radio_7_8nw",
                "peer_timers_in_milliseconds": {
                    "heartbeat": 5000,
                    "dead_interval": 10000,
                    "terminate_ack": 20000
                },
                "neighbour_timers_in_seconds": {
                    "neighbor_down_ack": 10
                },
                "supported_metrics": {
                    "link_rlq_rx_metric": 100,
                    "link_rlq_tx_metric": 100,
                    "link_resources_metric": 100,
                    "link_mtu_metric": 100,
                    "link_latency_metric_in_microseconds": 250,
                    "link_cdr_rx_metric_in_bps": 100000000,
                    "link_cdr_tx_metric_in_bps": 100000000,
                    "link_mdr_rx_metric_in_bps": 100000000,
                    "link_mdr_tx_metric_in_bps": 100000000
                }
            }
        }
    }
}
