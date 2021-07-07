expected_output = {
    "policies": {
        1: {
            'target': 'Twe1/0/42',
            'policy_type': 'PORT',
            'policy_name': 'test',
            'feature': 'Device-tracking',
            'tgt_range': 'vlan all'
        },
        2: {
            'target': 'Twe1/0/42', 
            'policy_type': 'PORT', 
            'policy_name': 'test1', 
            'feature': 'Source guard', 
            'tgt_range': 'vlan all'
        },
        3: {
            'target': 'Twe1/0/42', 
            'policy_type': 'PORT', 
            'policy_name': 'asdf', 
            'feature': 'RA guard', 
            'tgt_range': 'vlan all'
        },
        4: {
            'target': 'vlan 39', 
            'policy_type': 'VLAN', 
            'policy_name': 'test1', 
            'feature': 'Device-tracking', 
            'tgt_range': 'vlan all'
        },
        5: {
            'target': 'vlan 102', 
            'policy_type': 'VLAN', 
            'policy_name': 'DT-PROGRAMMATIC', 
            'feature': 'Device-tracking', 
            'tgt_range': 'vlan all'
        }
    }
}
