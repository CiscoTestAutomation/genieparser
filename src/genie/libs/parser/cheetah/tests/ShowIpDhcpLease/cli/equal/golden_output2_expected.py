expected_output = {
    'interfaces': {
        'wired0': {
            'lease_server': '192.0.2.1',
            'leases': [
                {
                    'vlan': 0,
                    'added_by': 'C',
                    'active': True,
                    'state': 'bound',
                    'disc_ago': 240,
                    'offer_ago': 238,
                    'req_ago': 90,
                    'ack_delay': 0.0014,
                    'renew_at': 60,
                    'exp_at': 120,
                    'ip': '192.0.2.196/24',
                    'gw': '192.0.2.1',
                    'bcast': '192.0.2.255',
                    'dns': '0.0.0.0',
                    'mtu': 0,
                }
            ],
        }
    }
}
