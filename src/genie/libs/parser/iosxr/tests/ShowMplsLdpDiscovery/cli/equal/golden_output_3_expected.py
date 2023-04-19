expected_output = {
    'vrf': {
        'default': {
            'local_ldp_identifier': {
                '1.100.1.2:0': {
                    'discovery_sources': {
                        'interfaces': {
                            'Bundle-Ether10': {
                                'xmit': True,
                                'recv': True,
                                'ldp_id': {
                                    '1.100.1.1:0': {
                                        'holdtime_sec': 15,
                                        'proposed_local': 15,
                                        'proposed_peer': 15,
                                        'established_date': 'Feb 10 05:18:32.242',
                                        'established_elapsed': '02:38:22'
                                    }
                                },
                                'transport_ip_addr': '1.100.1.1'
                            },
                            'GigabitEthernet0/0/0/1': {
                                'xmit': True,
                                'recv': True,
                                'ldp_id': {
                                    '1.100.1.1:0': {
                                        'holdtime_sec': 15,
                                        'proposed_local': 15,
                                        'proposed_peer': 15,
                                        'established_date': 'Feb 10 05:18:24.440',
                                        'established_elapsed': '02:38:29'
                                    }
                                },
                                'transport_ip_addr': '1.100.1.1'
                            },
                            'Targeted': {
                                'xmit': False,
                                'recv': False,
                                'ldp_id': {
                                    '1.100.1.1:0': {
                                        'holdtime_sec': 90,
                                        'proposed_local': 90,
                                        'proposed_peer': 90,
                                        'established_date': 'Feb 10 05:18:28.903',
                                        'established_elapsed': '02:38:25'
                                    }
                                }
                            }
                        }
                    },
                    'targeted_hellos': {
                        '1.100.1.2': {
                            '1.100.1.1': {
                                'xmit': True,
                                'recv': True,
                                'active': False,
                                'passive': False,
                                'active/passive': True
                            }
                        }
                    }
                }
            }
        }
    }
}
