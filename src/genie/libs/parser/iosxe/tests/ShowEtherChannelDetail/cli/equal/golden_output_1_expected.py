expected_output = {
    'group_state': 'L2',
    'ports': 2,
    'max_ports': 16,
    'port_channels': 1,
    'max_port_channels': 16,
    'protocol': 'LACP',
    'minimum_links': 0,
    'port': {
        'TwentyFiveGigE1/0/13': {
            'port_state': 'Up Mstr Assoc In-Bndl',
            'channel_group': 1,
            'gcchange': '-',
            'mode': "Active",
            'port_channel': 'Po1',
            'gc': '-',
            'pseudo_port_channel': 'Po1', 
            'port_index': 0,
            'load': '0x00',
            'protocol': 'LACP',
            'age': '0d:00h:03m:14s',
            'local_information': {
                'port': {
                    'TwentyFiveGigE1/0/13': {
                        'flags': 'SA',
                        'state': 'bndl',
                        'lacp_priority': 200,
                        'admin_key': '0x1',
                        'oper_key': '0x1',
                        'port_number': '0x10E',
                        'port_state': '0x3D'
                    }
                }
            },
            'partner_information': {
                'port': {
                    'TwentyFiveGigE1/0/13': {
                        'flags': 'SA',
                        'dev_id': '6cb2.ae4a.54c0',
                        'age': '6s',
                        'lacp_priority': 32768,
                        'admin_key': '0x0',
                        'oper_key': '0x1',
                        'port_number': '0x804',
                        'port_state': '0x3D'
                    }
                }
            }            
        },
        'TwentyFiveGigE1/0/15': {
            'port_state': 'Up Mstr Assoc Hot-stdby Not-in-Bndl',
            'channel_group': 1,
            'gcchange': '-',
            'mode': "Active",
            'port_channel': 'null',
            'gc': '-',
            'pseudo_port_channel': 'Po1', 
            'port_index': 0,
            'load': '0x00',
            'protocol': 'LACP',
            'age': '0d:00h:03m:16s',
            'local_information': {
                'port': {
                    'TwentyFiveGigE1/0/15': {
                        'flags': 'FA',
                        'state': 'hot-sby',
                        'lacp_priority': 300,
                        'admin_key': '0x1',
                        'oper_key': '0x1',
                        'port_number': '0x110',
                        'port_state': '0xF'
                    }
                }
            },
            'partner_information': {
                'port': {
                    'TwentyFiveGigE1/0/15': {
                        'flags': 'FA',
                        'dev_id': '6cb2.ae4a.54c0',
                        'age': '0s',
                        'lacp_priority': 32768,
                        'admin_key': '0x0',
                        'oper_key': '0x1',
                        'port_number': '0x803',
                        'port_state': '0xF'
                    }
                }
            }            
        }
    },
    'port_channel': {
        'Po1': {
            'age': '0d:00h:10m:38s',
            'logical_slot': '9/1',
            'number_of_ports': 1,
            'hot_standby': 'TwentyFiveGigE1/0/15',
            'state': 'Port-channel Ag-Inuse',
            'protocol': 'LACP',
            'port_security': 'Disabled',
            'fast_switchover': 'disabled',
            'dampening': 'disabled',
            'last_port_bundled': {
                'time': '0d:00h:03m:14s',
                'port': 'TwentyFiveGigE1/0/13'
            },
            'last_port_unbundled': {
                'time': '0d:00h:03m:16s',
                'port': 'TwentyFiveGigE1/0/15'
            },             
            'port': {
                'TwentyFiveGigE1/0/13': {
                    'index': 0,
                    'load': '00',
                    'ec_state': 'Active',
                    'no_of_bits': 0
                }
            } 
        }
    }
}