expected_output = {
    'policy_map': { 
        'TEST': { 
            'class': { 
                'class-default': { 
                    'qos_set': { 'precedence': '5'}
                    },
                'gold': {
                    'qos_set': {'precedence': '4'}
                    },
                'premium': { 
                    'priority_percent': '10',
                    'qos_set': {'cos': '5'}
                },
                'silver': { 
                    'qos_set': { 'dscp': 'af21'}
                    }
            }
        }
    }
}
