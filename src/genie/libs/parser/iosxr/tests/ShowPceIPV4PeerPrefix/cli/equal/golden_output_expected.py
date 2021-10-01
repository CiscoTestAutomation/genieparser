

expected_output = {
    'nodes': {
        1: {
            'te_router_id': '192.168.0.4',
            'host_name': 'rtrD',
            'isis_system_id': [
                '1921.68ff.1004 level-1',
                '1921.68ff.1004 level-2',
                '1921.68ff.1004 level-2'],
            'asn': [
                65001,
                65001,
                65001],
            'domain_id': [
                1111,
                1111,
                9999],
            'advertised_prefixes': [
                '192.168.0.4',
                '192.168.0.4',
                '192.168.0.4',
                '192.168.0.6']},
        2: {
            'te_router_id': '192.168.0.1',
            'host_name': 'rtrA',
                            'isis_system_id': ['1921.68ff.1001 level-2'],
            'advertised_prefixes': ['192.168.0.1']}}}
