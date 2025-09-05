expected_output = {
    'meraki_device_registration': {
        'devices': {
            '1': {
                'cloud_id': 'N/A',
                'error': 'Product type is not supported',
                'mac_address': 'XX:XX:XX:XX:XX:XX',
                'pid': 'C9300-24U',
                'serial_number': 'XXXXXXXXXXX',
                'status': 'Failed',
                'timestamp(utc)': '2024-02-14 03:22:48',
            },
        },
        'url': 'https://example.meraki.com/nodes/register',
    },
    'meraki_tunnel_config': {
        'client_ipv6_addr': '::',
        'fetch_state': 'Config fetch init',
    },
    'meraki_tunnel_interface': {
        'rx_drop_packets': 0,
        'rx_errors': 0,
        'rx_packets': 0,
        'status': 'Disable',
        'tx_drop_packets': 0,
        'tx_errors': 0,
        'tx_packets': 0,
    },
    'meraki_tunnel_state': {
        'primary': 'Down',
        'secondary': 'Down',
    },
    'service_meraki_connect': 'enable',
}