expected_output = {
    'legend': 'pp = Partially Programmed.', 'bridge_group': {
	'SRv6_ELAN': {
		'bridge_domain': {
			'SRv6_ELAN_Dual_Homing': {
				'state': 'up',
				'id': 0,
				'shg_id': 0,
				'mst_i': 0,
				'coupled_state': 'disabled',
				'vine_state': 'EVPN',
				'mac_learning': 'enabled',
				'mac_withdraw': 'enabled',
				'mac_withdraw_for_access_pw': 'enabled',
				'mac_withdraw_sent_on': 'bridge port up',
				'mac_withdraw_relaying': 'disabled',
				'flooding': {
					'broadcast_multicast': 'enabled',
					'unknown_unicast': 'enabled'
				},
				'mac_aging_time': 300,
				'mac_aging_type': 'inactivity',
				'mac_limit': 4000,
				'mac_limit_action': 'none',
				'mac_limit_notification': 'syslog',
				'mac_limit_reached': 'no',
				'mac_limit_threshold': '75%',
				'mac_port_down_flush': 'enabled',
				'mac_secure': 'disabled',
				'mac_secure_logging': 'disabled',
				'split_horizon_group': 'none',
				'dynamic_arp_inspection': 'disabled',
				'dynamic_arp_logging': 'disabled',
				'ip_source_guard': 'disabled',
				'ip_source_logging': 'disabled',
				'dhcp_v4_snooping': 'disabled',
				'dhcp_v4_snooping_profile': 'none',
				'igmp_snooping': 'disabled',
				'igmp_snooping_profile': 'none',
				'mld_snooping_profile': 'none',
				'storm_control': 'bridge-domain policer',
				'bridge_mtu': '1500',
				'mid_cvpls_config_index': '1',
				'p2mp_pw': 'disabled',
				'multicast_source': 'Not Set',
				'create_time': '10/08/2023 09:10:11 (6d23h ago)',
				'status_changed_since_creation': 'No',
				'ac': {
					'num_ac': 1,
					'num_ac_up': 0,
					'interfaces': {
						'Bundle-Ether5.1002': {
							'state': 'down (Segment-down)',
							'type': 'VLAN',
							'vlan_num_ranges': '1',
							'rewrite_tags': '',
							'vlan_ranges': ['1002', '1002'],
							'mtu': 1500,
							'xc_id': '0xc0000004',
							'interworking': 'none',
							'mst_i': 7,
							'mac_learning': 'enabled',
							'flooding': {
								'broadcast_multicast': 'enabled',
								'unknown_unicast': 'enabled'
							},
							'mac_aging_time': 300,
							'mac_aging_type': 'inactivity',
							'mac_limit': 4000,
							'mac_limit_action': 'none',
							'mac_limit_notification': 'syslog',
							'mac_limit_reached': 'no',
							'mac_limit_threshold': '75%',
							'split_horizon_group': 'none',
							'dhcp_v4_snooping': 'disabled',
							'dhcp_v4_snooping_profile': 'none',
							'igmp_snooping': 'disabled',
							'igmp_snooping_profile': 'none',
							'mld_snooping_profile': 'none'
						}
					}
				},
				'vfi': {
					'num_vfi': 0
				},
				'pw': {
					'num_pw': 0,
					'num_pw_up': 0
				},
				'pbb': {
					'num_pbb': 0,
					'num_pbb_up': 0
				},
				'vni': {
					'num_vni': 0,
					'num_vni_up': 0
				},
				'evpn': {
					'EVPN': {
						'state': 'up',
						'xc_id': '0x80000003',
						'statistics': {
							'packet_totals': {
								'receive': 0,
								'send': 0
							},
							'byte_totals': {
								'receive': 0,
								'send': 0
							},
							'mac_move': '0'
						}
					}
				}
			}
		}
	}
}
}
