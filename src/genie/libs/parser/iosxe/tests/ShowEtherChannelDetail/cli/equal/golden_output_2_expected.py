expected_output = {
    'group_state': 'L2',
    'ports': 2,
    'max_ports': 16,
    'port_channels': 1,
    'max_port_channels': 16,
    'protocol': 'LACP',
    'minimum_links': 0,
    'port': {
        'TwoGigabitEthernet1/0/14': {
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
            'age': '0d:00h:01m:11s',
            'local_information': {
                'port': {
                    'TwoGigabitEthernet1/0/14': {
                        'flags': 'SA',
                        'state': 'bndl',
                        'lacp_priority': 32768,
                        'admin_key': '0x1',
                        'oper_key': '0x1',
                        'port_number': '0x10F',
                        'port_state': '0x3D'
                    }
                }
            },
            'partner_information': {
                'port': {
                    'TwoGigabitEthernet1/0/14': {
                        'flags': 'SA',
                        'dev_id': 'a03d.6ea4.6f00',
                        'age': '18s',
                        'lacp_priority': 32768,
                        'admin_key': '0x0',
                        'oper_key': '0x1',
                        'port_number': '0x105',
                        'port_state': '0x3D'
                    }
                }
            }            
        },
        'TwoGigabitEthernet1/0/15': {
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
            'age': '0d:00h:01m:10s',
            'local_information': {
                'port': {
                    'TwoGigabitEthernet1/0/15': {
                        'flags': 'SA',
                        'state': 'bndl',
                        'lacp_priority': 32768,
                        'admin_key': '0x1',
                        'oper_key': '0x1',
                        'port_number': '0x110',
                        'port_state': '0x3D'
                    }
                }
            },
            'partner_information': {
                'port': {
                    'TwoGigabitEthernet1/0/15': {
                        'flags': 'SA',
                        'dev_id': 'a03d.6ea4.6f00',
                        'age': '18s',
                        'lacp_priority': 32768,
                        'admin_key': '0x0',
                        'oper_key': '0x1',
                        'port_number': '0x106',
                        'port_state': '0x3D'
                    }
                }
            }            
        }
    },
    'port_channel': {
        'Po1': {
            'age': '0d:00h:01m:16s',
            'logical_slot': '35/1',
            'number_of_ports': 2,
            'hot_standby': 'null',
            'state': 'Port-channel Ag-Inuse',
            'protocol': 'LACP',
            'port_security': 'Disabled',
            'fast_switchover': 'disabled',
            'dampening': 'disabled',
            'last_port_bundled': {
                'time': '0d:00h:01m:10s',
                'port': 'TwoGigabitEthernet1/0/15'
            },            
            'port': {
                'TwoGigabitEthernet1/0/15': {
                    'index': 0,
                    'load': '00',
                    'ec_state': 'Active',
                    'no_of_bits': 0
                },
                'TwoGigabitEthernet1/0/14': {
                    'index': 0,
                    'load': '00',
                    'ec_state': 'Active',
                    'no_of_bits': 0
                }
            } 
        }
    }
}