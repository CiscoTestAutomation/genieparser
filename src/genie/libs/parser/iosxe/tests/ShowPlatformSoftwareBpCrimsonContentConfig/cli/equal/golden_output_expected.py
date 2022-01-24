expected_output = {
'node': {
    1: {
        'priority': 1,
        'domain': 1, 
        'mode': 'Aggregation', 
        'router_id': '0.0.0.0', 
        'configured_svl_links': {
            'link_id': 1
            },
        'configured_svl_ports': {
            'FourHundredGigE1/0/19': {
                'link': 1, 
                'slot_bay_port': '1:0:19'
                },
            'FourHundredGigE1/0/20': {
                'link': 1, 
                'slot_bay_port': '1:0:20'
                }, 
            'FourHundredGigE1/0/22': {
                'link': 1, 
                'slot_bay_port': '1:0:22'
                }
            },
        'configured_svl_dual_active_detection_ports': {
            'FourHundredGigE1/0/15': {
                'slot_bay_port': '1:0:15'
                },
            'FourHundredGigE1/0/17': {
                'slot_bay_port': '1:0:17'
                }
            }
        },
    2: {
        'priority': 1,
        'domain': 1,
        'mode': 'Aggregation', 
        'router_id': '0.0.0.0', 
        'configured_svl_links': {
           'link_id': 1
           },
        'configured_svl_ports': {
            'FourHundredGigE2/0/19': {
                'link': 1,
                'slot_bay_port': '1:0:19'
                },
            'FourHundredGigE2/0/20': {
                'link': 1,
                'slot_bay_port': '1:0:20'
                },
            'FourHundredGigE2/0/22': {
                'link': 1, 
                'slot_bay_port': '1:0:22'
                }
            }, 
        'configured_svl_dual_active_detection_ports': {
            'FourHundredGigE2/0/16': {
                'slot_bay_port': '1:0:16'
                },
            'FourHundredGigE2/0/18': {
                'slot_bay_port': '1:0:18'
                }
            }
        }
    }
}
