expected_output = {
    'vrf': {
        'default': {
            'local_ldp_identifier': {
                '25.97.1.1:0': {
                    'discovery_sources': {
                        'interfaces': {
                            'TenGigE0/3/0/0': {
                                'xmit': True, 
                                'recv': True, 
                                'source_ip_addr': '100.20.0.1', 
                                'transport_ip_addr': '25.97.1.1', 
                                'hello_interval_ms': 5000, 
                                'hello_due_time_ms': 563, 
                                'quick_start': 'enabled', 
                                'ldp_id': {
                                    '95.95.95.95:0': {
                                        'source_ip_addr': '100.20.0.2', 
                                        'transport_ip_addr': '95.95.95.95', 
                                        'holdtime_sec': 15, 
                                        'proposed_local': 15, 
                                        'proposed_peer': 45, 
                                        'expiring_in': 11.0, 
                                        'established_date': 'Sep 14 17:36:35.833', 
                                        'established_elapsed': '00:19:09', 
                                        'last_session_connection_failures': {
                                            '1': {
                                                'timestamp': 'Jan  4 05:20:34.814', 
                                                'reason': 'User cleared session manually', 
                                                'last_up_for': '00:06:56'
                                            }, 
                                            '2': {
                                                'timestamp': 'Jan  4 05:28:48.641', 
                                                'reason': 'User cleared session manually', 
                                                'last_up_for': '00:08:11'
                                            }
                                        }
                                    }
                                }
                            }, 
                            'TenGigE0/3/0/26': {
                                'xmit': True, 
                                'recv': True, 
                                'source_ip_addr': '100.10.0.1', 
                                'transport_ip_addr': '25.97.1.1', 
                                'hello_interval_ms': 5000, 
                                'hello_due_time_ms': 2900, 
                                'quick_start': 'enabled', 
                                'ldp_id': {
                                    '96.96.96.96:0': {
                                        'source_ip_addr': '100.10.0.2', 
                                        'transport_ip_addr': '96.96.96.96', 
                                        'holdtime_sec': 15, 
                                        'proposed_local': 15, 
                                        'proposed_peer': 15, 
                                        'expiring_in': 14.5, 
                                        'established_date': 'Sep 14 17:36:35.834', 
                                        'established_elapsed': '00:19:09', 
                                        'last_session_connection_failures': {
                                            '1': {
                                                'timestamp': 'Jan  4 05:20:34.814', 
                                                'reason': 'User cleared session manually', 
                                                'last_up_for': '00:06:56'
                                            }, 
                                            '2': {
                                                'timestamp': 'Jan  4 05:28:48.641', 
                                                'reason': 'User cleared session manually', 
                                                'last_up_for': '00:08:05'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}