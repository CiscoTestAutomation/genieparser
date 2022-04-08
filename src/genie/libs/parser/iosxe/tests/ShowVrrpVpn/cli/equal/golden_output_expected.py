expected_output = {
    'vrrp_vpn': 1,
    'interfaces': {
        'ge2/3.101': {
            'groups': {
                1: {
                    'virtual_ip_address': '182.210.210.201',
                    'virtual_mac_address': '00:00:5e:00:01:01',
                    'priority': 115,
                    'real_priority': 105,
                    'vrrp_state': 'primary',
                    'omp_state': 'up',
                    'advertisement_timer': 1,
                    'primary_down_timer': 3,
                    'last_state_change_time': '2022-01-24T06:56:20+00:00'
                }
            }
        }
    }
}
