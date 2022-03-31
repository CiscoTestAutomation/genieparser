expected_output = {
    'interface': {
        'GigabitEthernet0/0/2.150': {
            'group_number': {
                2: {
                    'address_family': 'IPv4',
                    'state': 'INIT',
                    'state_duration': {
                        'hours': 6,
                        'minutes': 40,
                        'seconds': 47.0
                    },
                    'virtual_ip_address': 'no address',
                    'virtual_mac_address': '0000.5E00.0102',
                    'advertise_interval': 1000,
                    'preemption_state': 'enabled',
                    'priority': 250,
                    'state_change_reason': 'VRRP_INIT',
                    'tloc_preference': 0,
                    'master_router': 'unknown',
                    'master_router_priority': 'unknown',
                    'master_advertisement_interval': 'unknown',
                    'master_down_interval': 'unknown',
                    'flags': '1/0',
                    'vrrpv3_advertisements': {
                        'sent': 0,
                        'errors': 0,
                        'rcvd': 0
                    },
                    'vrrpv2_advertisements': {
                        'sent': 0,
                        'errors': 0,
                        'rcvd': 0
                    },
                    'group_discarded_packets': {
                        'total': 0,
                        'vrrpv2_incompatibility': 0,
                        'ip_address_owner_conflicts': 0,
                        'invalid_address_count': 0,
                        'ip_address_configuration_mismatch': 0,
                        'invalid_advert_interval': 0,
                        'adverts_received_in_Init_state': 0,
                        'invalid_group_other_reason': 0
                    },
                    'group_state_transition': {
                        'init_to_master': 0,
                        'init_to_backup': 0,
                        'backup_to_master': 0,
                        'master_to_backup': 0,
                        'master_to_init': 0,
                        'backup_to_init': 0
                    }
                }
            }
        },
        'GigabitEthernet0/0/6.101': {
            'group_number': {
                1: {
                    'address_family': 'IPv4',
                    'state': 'BACKUP',
                    'state_duration': {
                        'hours': 5,
                        'minutes': 41,
                        'seconds': 27.0
                    },
                    'virtual_ip_address': '192.105.105.201',
                    'virtual_mac_address': '0000.5E00.0101',
                    'advertise_interval': 1000,
                    'preemption_state': 'enabled',
                    'priority': 200,
                    'state_change_reason': 'VRRP_PREEMPT',
                    'tloc_preference': 0,
                    'track_object': {
                        'omp': {
                            'state': 'UP'
                        }
                    },
                    'master_router': '192.105.105.91',
                    'master_router_priority': '220',
                    'master_advertisement_interval': '1000',
                    'master_down_interval': '3218 msec (expires in 3066 msec)',
                    'flags': '0/1',
                    'vrrpv3_advertisements': {
                        'sent': 23,
                        'errors': 0,
                        'rcvd': 26331
                    },
                    'vrrpv2_advertisements': {
                        'sent': 23,
                        'errors': 0,
                        'rcvd': 2
                    },
                    'group_discarded_packets': {
                        'total': 26361,
                        'vrrpv2_incompatibility': 26329,
                        'ip_address_owner_conflicts': 0,
                        'invalid_address_count': 0,
                        'ip_address_configuration_mismatch': 0,
                        'invalid_advert_interval': 0,
                        'adverts_received_in_Init_state': 32,
                        'invalid_group_other_reason': 0
                    },
                    'group_state_transition': {
                        'init_to_master': 0,
                        'init_to_backup': 2,
                        'backup_to_master': 2,
                        'master_to_backup': 1,
                        'master_to_init': 1,
                        'backup_to_init': 0
                    }
                }
            }
        },
        'GigabitEthernet0/0/6.102': {
            'group_number': {
                2: {
                    'address_family': 'IPv4',
                    'state': 'MASTER',
                    'state_duration': {
                        'hours': 5,
                        'minutes': 41,
                        'seconds': 37.0
                    },
                    'virtual_ip_address': '192.105.105.202',
                    'virtual_mac_address': '0000.5E00.0102',
                    'advertise_interval': 3000,
                    'preemption_state': 'enabled',
                    'priority': 100,
                    'state_change_reason': 'VRRP_MASTER_NO_RESP',
                    'tloc_preference': 0,
                    'track_object': {
                        'omp': {
                            'state': 'UP'
                        }
                    },
                    'master_router': '192.105.105.102 (local)',
                    'master_router_priority': '100',
                    'master_advertisement_interval': '3000',
                    'master_down_interval': 'unknown',
                    'flags': '1/1',
                    'vrrpv3_advertisements': {
                        'sent': 7598,
                        'errors': 0,
                        'rcvd': 3592
                    },
                    'vrrpv2_advertisements': {
                        'sent': 7598,
                        'errors': 0,
                        'rcvd': 1
                    },
                    'group_discarded_packets': {
                        'total': 3623,
                        'vrrpv2_incompatibility': 3591,
                        'ip_address_owner_conflicts': 0,
                        'invalid_address_count': 0,
                        'ip_address_configuration_mismatch': 3593,
                        'invalid_advert_interval': 0,
                        'adverts_received_in_Init_state': 32,
                        'invalid_group_other_reason': 0
                    },
                    'group_state_transition': {
                        'init_to_master': 0,
                        'init_to_backup': 2,
                        'backup_to_master': 2,
                        'master_to_backup': 0,
                        'master_to_init': 1,
                        'backup_to_init': 0
                    }
                }
            }
        }
    }
}
