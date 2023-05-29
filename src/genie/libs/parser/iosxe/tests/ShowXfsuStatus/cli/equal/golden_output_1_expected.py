expected_output = {
    'reload_fast_platform_status': 'Not started yet',
    'graceful_reload_infra_status': 'Started in stacking mode, not running',
    'uptime_before_fast_reload': 5,
    'client': {
        'ospfv3': {
            'id': '0x10203004',
            'status': 'GR stack none: Up'
        },
        'ospf': {
            'id': '0x10203003',
            'status': 'GR stack none: Up'
        },
        'is_is': {
            'id': '0x10203002',
            'status': 'GR stack none: Up'
        },
        'gr_client_fib': {
            'id': '0x10203001',
            'status': 'GR stack none: Up'
        },
        'gr_client_rib': {
            'id': '0x10203000',
            'status': 'GR stack none: Up'
        }
    }
}