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
                    'disc_ago': 120,
                    'offer_ago': 118,
                    'req_ago': 60,
                    'ack_delay': 0.0012,
                    'renew_at': 30,
                    'exp_at': 90,
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
