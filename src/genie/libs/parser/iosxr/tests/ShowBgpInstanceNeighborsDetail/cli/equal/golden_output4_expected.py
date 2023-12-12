expected_output = {
    'instance': {
        'all': {
            'vrf': {
                'default': {
                    'neighbor': {
                        '50.1.1.8': {
                            'remote_as': 100,
                            'link_state': 'internal link',
                            'local_as_as_no': 100,
                            'local_as_no_prepend': False,
                            'local_as_replace_as': False,
                            'local_as_dual_as': False,
                            'router_id': '50.1.1.8',
                            'session_state': 'established',
                            'up_time': '2d00h',
                            'nsr_state': 'None',
                            'holdtime': 180,
                            'keepalive_interval': 60,
                            'configured_holdtime': 180,
                            'configured_keepalive_interval': 60,
                            'min_acceptable_hold_time': 3,
                            'last_write': '00:00:55',
                            'attempted': 19,
                            'written': 19,
                            'second_last_write': '00:01:55',
                            'second_attempted': 19,
                            'second_written': 19,
                            'last_write_pulse_rcvd': 'Jul 7 09:35:40.671 ',
                            'last_full_not_set_pulse_count': 8654,
                            'last_ka_error_before_reset': '00:00:00',
                            'last_ka_error_ka_not_sent': '00:00:00',
                            'precedence': 'internet',
                            'non_stop_routing': True,
                            'graceful_restart': True,
                            'graceful_restart_restart_time': 120,
                            'graceful_restart_stalepath_time': 360,
                            'multiprotocol_capability': 'received',
                            'bgp_negotiated_capabilities': {
                                'route_refresh': 'advertised received',
                                'graceful_restart': ' received',
                                'four_octets_asn': 'advertised received',
                                'ipv4_unicast': 'advertised received',
                                'vpnv4_unicast': 'advertised received',
                                'ipv6_unicast': 'advertised received',
                                'vpnv6_unicast': 'advertised received',
                                'l2vpn_vpls': 'advertised received',
                                'l2vpn_evpn': 'advertised received'
                            },
                            'messages': {
                                'received': {
                                    'messages_count': 4383,
                                    'notifications': 1,
                                    'queue': 0
                                },
                                'sent': {
                                    'messages_count': 4385,
                                    'notifications': 1,
                                    'queue': 0
                                }
                            },
                            'minimum_time_between_adv_runs': 0,
                            'inbound_message': '3',
                            'outbound_message': '3'
                        },
                        '80.11.1.2': {
                            'remote_as': 5000,
                            'link_state': 'external link',
                            'local_as_as_no': 100,
                            'local_as_no_prepend': False,
                            'local_as_replace_as': False,
                            'local_as_dual_as': False,
                            'router_id': '70.1.1.1',
                            'session_state': 'established',
                            'up_time': '4w6d',
                            'nsr_state': 'None',
                            'holdtime': 180,
                            'keepalive_interval': 60,
                            'configured_holdtime': 180,
                            'configured_keepalive_interval': 60,
                            'min_acceptable_hold_time': 3,
                            'last_write': '00:00:43',
                            'attempted': 19,
                            'written': 19,
                            'second_last_write': '00:01:43',
                            'second_attempted': 19,
                            'second_written': 19,
                            'last_write_pulse_rcvd': 'Jun 8 10:05:28.237 ',
                            'last_full_not_set_pulse_count': 111857,
                            'last_ka_error_before_reset': '00:00:00',
                            'last_ka_error_ka_not_sent': '00:00:00',
                            'precedence': 'internet',
                            'non_stop_routing': True,
                            'graceful_restart': True,
                            'graceful_restart_restart_time': 120,
                            'graceful_restart_stalepath_time': 360,
                            'enforcing_first_as': 'enabled',
                            'multiprotocol_capability': 'received',
                            'bgp_negotiated_capabilities': {
                                'route_refresh': 'advertised received',
                                'graceful_restart': ' received',
                                'four_octets_asn': 'advertised received',
                                'ipv4_unicast': 'advertised received'
                            },
                            'messages': {
                                'received': {
                                    'messages_count': 58559,
                                    'notifications': 0,
                                    'queue': 0
                                },
                                'sent': {
                                    'messages_count': 53439,
                                    'notifications': 2,
                                    'queue': 0
                                }
                            },
                            'minimum_time_between_adv_runs': 30,
                            'inbound_message': '3',
                            'outbound_message': '3',
                            'address_family': {
                                'ipv4 unicast': {
                                    'neighbor_version': 1322,
                                    'update_group': '0.3',
                                    'filter_group': '0.1',
                                    'refresh_request_status': 'No Refresh request being processed',
                                    'route_refresh_request_received': 0,
                                    'route_refresh_request_sent': 0,
                                    'route_map_name_in': 'PASS-ALL',
                                    'route_map_name_out': 'PASS-ALL',
                                    'accepted_prefixes': 1,
                                    'best_paths': 1,
                                    'exact_no_prefixes_denied': 0,
                                    'cummulative_no_prefixes_denied': 0,
                                    'prefix_advertised': 393,
                                    'prefix_suppressed': 2,
                                    'prefix_withdrawn': 365,
                                    'maximum_prefix_max_prefix_no': 1048576,
                                    'maximum_prefix_warning_only': True,
                                    'maximum_prefix_threshold': '75%',
                                    'maximum_prefix_restart': 0,
                                    'eor_status': 'was received during read-only mode',
                                    'last_synced_ack_version': 0,
                                    'last_ack_version': 1322,
                                    'outstanding_version_objects_current': 0,
                                    'outstanding_version_objects_max': 3,
                                    'additional_paths_operation': 'None',
                                    'additional_routes_local_label': 'Unicast SAFI'
                                }
                            },
                            'bgp_session_transport': {
                                'connection': {
                                    'state': 'established',
                                    'connections_established': 3,
                                    'connections_dropped': 2,
                                    'ttl_security': 'enabled'
                                },
                                'transport': {
                                    'local_host': '80.11.1.1',
                                    'local_port': '31495',
                                    'if_handle': '0x00000120',
                                    'foreign_host': '80.11.1.2',
                                    'foreign_port': '179'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
