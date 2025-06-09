expected_output = {
    'GigabitEthernet0/0/2': {
        'admin_configs': {
            'mode': 'Synchronous',
            'esmc_tx': 'Enable',
            'esmc_rx': 'Enable',
            'ql_tx': '-',
            'ql_rx': '-'
        },
        'operational_status': {
            'port_status': 'UP',
            'ql_receive': 'QL-SEC',
            'ql_transmit': 'QL-DNU',
            'ql_rx_overrided': '-',
            'esmc_info_rate': 1,
            'esmc_expiry': 5,
            'esmc_tx_timer': 'Running',
            'esmc_rx_timer': 'Running',
            'esmc_tx_interval_count': 1,
            'esmc_info_pkts_in': 1080133,
            'esmc_info_pkts_out': 1095993,
            'esmc_event_pkts_in': 4,
            'esmc_event_pkts_out': 34
        }
    }
}
