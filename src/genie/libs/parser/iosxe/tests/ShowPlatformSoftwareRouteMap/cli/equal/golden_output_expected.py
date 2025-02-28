expected_output = {
    'route_map': {
        'AAA': {
            'permit': True, 
            'sequence': 100, 
            'match_clauses': 
            {
                'ip_address': '101'
            }, 
            'set_clauses': 
            {
                'ipv4_nexthop': '10.0.0.1', 
                'table_id': 0, 
                'set_force': False
            }
        }
    }
}