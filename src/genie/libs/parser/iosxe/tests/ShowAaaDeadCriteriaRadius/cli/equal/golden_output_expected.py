expected_output = {
        'server_group': 'radius',
        'server': {
            'address': '11.19.12.66',
            'auth_port': 1645,
            'acct_port': 1646
        },
        'dead_criteria': {
            'conf_retransmits': 3,
            'conf_timeout': 5,
            'esti_outstand_access_transactions': 0,
            'esti_outstand_accounting_transactions': 0,
            'dead_detect_time_seconds': 10,
            'computed_retransmit_tries': 10
        },
        'statistics': {
            'max_computed_outstand_transaction': 1,
            'max_computed_dead_detect_time_seconds': 10,
            'max_computed_retransmit': 10
        }
}