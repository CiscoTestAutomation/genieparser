expected_output = {
	'instance': {
		'all': {
			'vrf': {
				'default': {
					'neighbor': {
						'1.1.1.1': {
							'remote_as': 200,
							'link_state': 'internal link',
							'local_as_as_no': 200,
							'local_as_no_prepend': False,
							'local_as_replace_as': False,
							'local_as_dual_as': False,
							'router_id': '0.0.0.0',
							'session_state': 'active',
							'nsr_state': 'None',
							'bfd': {
								'bfd_status': 'enabled',
								'session_status': 'up',
								'mininterval': 150,
								'multiplier': 3
							},
							'bgp_neighbor_counters': {
								'messages': {
									'sent': {
										'bfd discriminators': 0
									},
									'received': {
										'bfd discriminators': 3
									}
								}
							},
							'holdtime': 180,
							'keepalive_interval': 60,
							'configured_holdtime': 180,
							'configured_keepalive_interval': 60,
							'min_acceptable_hold_time': 3,
							'last_write': '00:15:52',
							'attempted': 85,
							'written': 85,
							'last_write_pulse_rcvd': 'Jan 16 09:36:40.945 ',
							'last_full_not_set_pulse_count': 58,
							'last_ka_error_before_reset': '00:00:00',
							'last_ka_error_ka_not_sent': '00:00:00',
							'precedence': 'internet',
							'non_stop_routing': True,
							'graceful_restart': True,
							'graceful_restart_restart_time': 120,
							'graceful_restart_stalepath_time': 360,
							'multiprotocol_capability': 'received',
							'messages': {
								'received': {
									'messages_count': 29,
									'notifications': 0,
									'queue': 0
								},
								'sent': {
									'messages_count': 30,
									'notifications': 0,
									'queue': 0
								}
							},
							'minimum_time_between_adv_runs': 0,
							'inbound_message': '3',
							'outbound_message': '3',
							'address_family': {
								'ipv4 unicast': {
									'neighbor_version': 0,
									'update_group': '0.4',
									'filter_group': '0.0',
									'refresh_request_status': 'No Refresh request being processed',
									'route_refresh_request_received': 0,
									'route_refresh_request_sent': 0,
									'accepted_prefixes': 0,
									'best_paths': 0,
									'exact_no_prefixes_denied': 0,
									'cummulative_no_prefixes_denied': 0,
									'prefix_advertised': 0,
									'prefix_suppressed': 0,
									'prefix_withdrawn': 0,
									'eor_status': 'was received during read-only mode',
									'last_synced_ack_version': 0,
									'last_ack_version': 0,
									'additional_paths_operation': 'None',
									'send_multicast_attributes': True,
									'additional_routes_local_label': 'Unicast SAFI'
								}
							},
							'bgp_session_transport': {
								'connection': {
									'state': 'established',
									'connections_established': 1,
									'connections_dropped': 1
								},
								'transport': {
									'local_host': '1.1.1.2',
									'local_port': '44866',
									'if_handle': '0x000004a0',
									'foreign_host': '1.1.1.1',
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