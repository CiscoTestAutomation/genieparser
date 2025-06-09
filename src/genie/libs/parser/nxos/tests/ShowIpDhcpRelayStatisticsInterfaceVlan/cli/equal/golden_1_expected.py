expected_output = data = {
    'message_types': {
        'discover': {'rx': 16, 'tx': 16, 'drops': 0},
        'offer': {'rx': 16, 'tx': 16, 'drops': 0},
        'request': {'rx': 322, 'tx': 322, 'drops': 0},
        'ack': {'rx': 322, 'tx': 322, 'drops': 0},
        'release': {'rx': 18, 'tx': 18, 'drops': 0},
        'decline': {'rx': 0, 'tx': 0, 'drops': 0},
        'inform': {'rx': 0, 'tx': 0, 'drops': 0},
        'nack': {'rx': 0, 'tx': 0, 'drops': 0},
        'total': {'rx': 694, 'tx': 694, 'drops': 0}
    },
    'dhcp_server_stats': {
        'servers': [{
            'server': '192.0.2.42',
            'vrf': '', 
            'request': 356, 
            'response': 338
        }]
    },
    'dhcp_l3_fwd_stats': {
        'total_packets_received': 0,
        'total_packets_forwarded': 0,
        'total_packets_dropped': 0
    },
    'non_dhcp_drop_stats': {
        'total_packets_received': 0,
        'total_packets_forwarded': 0,
        'total_packets_dropped': 0
    },
    'dhcp_drop_stats': {
        'dhcp_relay_not_enabled': 0,
        'invalid_dhcp_message_type': 0,
        'interface_error': 0,
        'tx_failure_towards_server': 0,
        'tx_failure_towards_client': 0,
        'unknown_output_interface': 0,
        'unknown_vrf_or_interface_for_server': 0,
        'max_hops_exceeded': 0,
        'option_82_validation_failed': 0,
        'packet_malformed': 0,
        'dhcp_request_dropped_on_mct': 0,
        'relay_trusted_port_not_configured': 0
    }
}