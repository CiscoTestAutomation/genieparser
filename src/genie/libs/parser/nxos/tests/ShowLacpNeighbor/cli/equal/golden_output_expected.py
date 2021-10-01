

expected_output = {
    'interfaces': {
        'Port-channel1': {
            'members': {
                'Ethernet1/1': {
                    'interface': 'Ethernet1/1',
                    'activity': 'active',
                    'oper_key': 0x8000,
                    'port_num': 0x101,
                    'partner_id': '5e-2-0-1-0-7',
                    'age': 1140,
                    'interval': 'slow',
                    'lacp_port_priority': 32768,
                    'port_state': 0x3d,
                },
                'Ethernet1/2': {
                    'interface': 'Ethernet1/2',
                    'activity': 'active',
                    'oper_key': 0x8000,
                    'port_num': 0x102,
                    'partner_id': '5e-2-0-1-0-7',
                    'age': 1140,
                    'interval': 'slow',
                    'lacp_port_priority': 32768,
                    'port_state': 0x3d,
                },
            }
        },
        'Port-channel2': {
            'members': {
                'Ethernet1/3': {
                    'interface': 'Ethernet1/3',
                    'activity': 'active',
                    'oper_key': 0x1,
                    'port_num': 0x103,
                    'partner_id': '5e-2-0-1-0-7',
                    'age': 625,
                    'interval': 'slow',
                    'lacp_port_priority': 32768,
                    'port_state': 0x3d,
                },
                'Ethernet1/4': {
                    'interface': 'Ethernet1/4',
                    'activity': 'active',
                    'oper_key': 0x1,
                    'port_num': 0x104,
                    'partner_id': '5e-2-0-1-0-7',
                    'age': 638,
                    'interval': 'slow',
                    'lacp_port_priority': 32768,
                    'port_state': 0x3d,
                },
                'Ethernet1/5': {
                    'interface': 'Ethernet1/5',
                    'activity': 'active',
                    'oper_key': 0x1,
                    'port_num': 0x105,
                    'partner_id': '5e-2-0-1-0-7',
                    'age': 834,
                    'interval': 'slow',
                    'lacp_port_priority': 32768,
                    'port_state': 0xd,
                }
            }
        }
    }
}
