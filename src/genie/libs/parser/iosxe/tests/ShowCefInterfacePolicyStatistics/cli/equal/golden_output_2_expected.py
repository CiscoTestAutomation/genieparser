expected_output = {
    'interfaces': {
        'FastEthernet0/1/0': {
            'status': 'down',
            'if_number': 5,
            'corr_hwidb_fast_if_number': 5,
            'corr_hwidb_firstsw_if_number': 5,
            'policy_accounting_status': 'OSPF based Policy accounting on input is enabled',
            'direction': 'input',
            'policy_statistics': {
                '1': {'packets': 5, 'bytes': 500},
                '2': {'packets': 3, 'bytes': 300},
                '3': {'packets': 0, 'bytes': 0},
                '4': {'packets': 0, 'bytes': 0},
                '5': {'packets': 0, 'bytes': 0}
            }
        }
    }
}