expected_output = {
    'interface': {
        'TenGigabitEthernet3/1/3': {
            'broadcast_suppression': 'percentage(0-100)',
            'channel': 'yes',
            'cos_rewrite': 'yes',
            'dot1x': 'yes',
            'duplex': 'full',
            'fast_start': 'yes',
            'flowcontrol': 'rx-(off,on,desired),tx-(none)',
            'inline_power': 'no',
            'model': 'WS-C3650-48PD',
            'portsecure': 'yes',
            'qos_scheduling': 'rx-(not configurable on per port basis), tx-(2p6q3t)',
            'span': 'source/destination',
            'speed': '10000',
            'tos_rewrite': 'yes',
            'trunk_encap_type': '802.1Q',
            'trunk_mode': 'on,off,desirable,nonegotiate',
            'type': 'SFP-10G-ACTIVE-CABLE',
            'udld': 'yes',
        }
    }
}