
expected_output = {
    'interfaces': {
        'GigabitEthernet0/0/0': {
            'description': 'WAN',
            'mtu': 1508,
            'negotiation_auto': True,
            'pppoe': {
                'enabled': True,
                'group': 'global',
            },
            'pppoe_client': {
                'dial_pool_number': 2,
                'ppp_max_payload': 1500,
            },
            'service_policy_output': 'SHAPING',
        },
    },
}