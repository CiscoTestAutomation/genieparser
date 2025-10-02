expected_output = {
    'vrf': {
        'CUST_A': {
            'type': 'ip vrf',
            'rd': '100:1',
            'route_target': {
                'export': ['100:1'],
                'import': ['100:1']
            },
            'interfaces': {
                'TenGigabitEthernet0/0/8': {
                    'ip_vrf_forwarding': 'CUST_A',
                    'ip_address': '15.0.0.1',
                    'ip_mask': '255.255.255.0',
                    'ip_nbar_protocol_discovery': True,
                    'ip_nat_inside': True,
                    'negotiation_auto': True
                },
                'TenGigabitEthernet0/0/9': {
                    'ip_vrf_forwarding': 'CUST_A',
                    'ip_address': '80.0.0.1',
                    'ip_mask': '255.255.255.0',
                    'ip_nbar_protocol_discovery': True,
                    'ip_nat_outside': True,
                    'negotiation_auto': True
                }
            },
            'nat_rules': {
                'nat_rule_1': {
                    'type': 'inside',
                    'local_ip': '15.0.0.2',
                    'global_ip': '16.0.0.2',
                    'vrf': 'CUST_A',
                    'match_in_vrf': True
                },
                'nat_rule_2': {
                    'type': 'inside',
                    'local_ip': '15.1.1.1',
                    'global_ip': '16.1.1.1',
                    'vrf': 'CUST_A',
                    'match_in_vrf': True
                }
            },
            'routes': {
                'route_1': {
                    'network': '15.0.0.0',
                    'mask': '255.0.0.0',
                    'interface': 'TenGigabitEthernet0/0/8',
                    'next_hop': '15.0.0.2'
                },
                'route_2': {
                    'network': '16.0.0.0',
                    'mask': '255.0.0.0',
                    'interface': 'TenGigabitEthernet0/0/8',
                    'next_hop': '15.0.0.2'
                },
                'route_3': {
                    'network': '70.0.0.0',
                    'mask': '255.0.0.0',
                    'interface': 'TenGigabitEthernet0/0/9',
                    'next_hop': '80.0.0.2'
                },
                'route_4': {
                    'network': '80.0.0.0',
                    'mask': '255.0.0.0',
                    'interface': 'TenGigabitEthernet0/0/9',
                    'next_hop': '80.0.0.2'
                }
            }
        },
        'CUST_B': {
            'type': 'ip vrf',
            'rd': '101:1',
            'route_target': {
                'export': ['101:1'],
                'import': ['101:1']
            },
            'interfaces': {
                'TenGigabitEthernet0/0/7': {
                    'ip_vrf_forwarding': 'CUST_B',
                    'ip_address': '15.0.0.1',
                    'ip_mask': '255.255.255.0',
                    'ip_nbar_protocol_discovery': True,
                    'ip_nat_inside': True,
                    'negotiation_auto': True
                },
                'TenGigabitEthernet0/0/10': {
                    'ip_vrf_forwarding': 'CUST_B',
                    'ip_address': '80.0.0.1',
                    'ip_mask': '255.255.255.0',
                    'ip_nbar_protocol_discovery': True,
                    'ip_nat_outside': True,
                    'negotiation_auto': True
                }
            },
            'nat_rules': {
                'nat_rule_1': {
                    'type': 'inside',
                    'local_ip': '15.0.0.2',
                    'global_ip': '16.0.0.2',
                    'vrf': 'CUST_B',
                    'match_in_vrf': True
                },
                'nat_rule_2': {
                    'type': 'inside',
                    'local_ip': '15.1.1.1',
                    'global_ip': '16.1.1.1',
                    'vrf': 'CUST_B',
                    'match_in_vrf': True
                }
            },
            'routes': {
                'route_1': {
                    'network': '15.0.0.0',
                    'mask': '255.0.0.0',
                    'interface': 'TenGigabitEthernet0/0/7',
                    'next_hop': '15.0.0.2'
                },
                'route_2': {
                    'network': '16.0.0.0',
                    'mask': '255.0.0.0',
                    'interface': 'TenGigabitEthernet0/0/7',
                    'next_hop': '15.0.0.2'
                },
                'route_3': {
                    'network': '70.0.0.0',
                    'mask': '255.0.0.0',
                    'interface': 'TenGigabitEthernet0/0/10',
                    'next_hop': '80.0.0.2'
                },
                'route_4': {
                    'network': '80.0.0.0',
                    'mask': '255.0.0.0',
                    'interface': 'TenGigabitEthernet0/0/10',
                    'next_hop': '80.0.0.2'
                }
            }
        },
        'Mgmt-intf': {
            'type': 'vrf definition',
            'address_family': {
                'ipv4': {},
                'ipv6': {}
            },
            'interfaces': {
                'GigabitEthernet0': {
                    'ip_vrf_forwarding': 'Mgmt-intf',
                    'ip_address': '1.46.18.179',
                    'ip_mask': '255.255.0.0',
                    'negotiation_auto': True
                }
            },
            'routes': {
                'route_1': {
                    'network': '223.255.254.0',
                    'mask': '255.255.255.0',
                    'next_hop': '1.46.0.1'
                }
            }
        }
    }
}
