expected_output = {
    'vrf': {
        'default': {
            'peer_address': '66:66:66:66::.4342',
            'peer_port': 4342,
            'local_address': '66:66:66:66::.50383',
            'local_port': 50383,
            'capability_exchange_complete': 'Yes',
            'capability_sent_bitmap': '0x000001FF',
            'capability_sent': ['Publish-Subscribe Instance-ID', 'Domain-Info', 'Route-Tag', 'SGT', 'Default-originate',
                                'Service-registration', 'Extranet-policy-propagation', 'Default-ETR Route-metric', 'Unknown vendor type skip'],
            'capability_received_bitmap': '0x000001FF',
            'capability_received': ['Publish-Subscribe Instance-ID', 'Domain-Info', 'Route-Tag', 'SGT', 'Default-originate',
                                    'Service-registration', 'Extranet-policy-propagation', 'Default-ETR Route-metric', 'Unknown vendor type skip'],
            'rx_count': 1,
            'err_count': 0
        }
    }
}
