expected_output = {
    'mode': 'rapid-pvst',
    'root_bridge': 'none',
    'extended_system_id': True,
    'portfast': True,
    'portfast_bpdu_guard': False,
    'portfast_bpdu_filter': False,
    'loopguard': False,
    'etherchannel_misconfig_guard': True,
    'uplinkfast': False,
    'backbonefast': False,
    'spannig_tree_name': {
        '300_vlans': {
            'blocking': 300,
            'listening': 0,
            'learning': 0,
            'forwarding': 600,
            'stp_active': 900
        }
    }
}