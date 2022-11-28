expected_output = {
    'pid': 5,
    'address_family': 'ipv6',
    'router_id': '1.1.1.1',
    'events': {
        '1': { 
            'date': '*Oct 10 13:19:29.499', 
            'message': 'End of SPF, SPF time 0ms, next wait-interval 200ms'
        },
        '2': { 
            'date': '*Oct 10 13:19:29.499', 
            'message': 'Starting SPF, wait-interval 50ms'
        },
        '3': { 
            'date': '*Oct 10 13:19:29.449', 
            'message': 'Schedule SPF, Area 0, Change in LSA type RLSID 0.0.0.0, Adv-Rtr 1.1.1.1'
        },
        '4': { 
            'date': '*Oct 10 13:19:29.449', 
            'message': 'Generate Changed Type-0x2001 LSA, LSID 0.0.0.0, Seq# 80000001, Age 0, Area 0'
        }
    }
}