expected_output = {
    'client_mac_address': '1cbf.cee6.9419',
    'client_mac_type': 'Universally Administered Address',
    'client_ipv4_address': '10.28.50.67',
    'client_username': 'Cisco',
    'ap_mac_address': '3c41.0e3b.c420',
    'ap_name': 'DMZ-AP-1',
    'ap_slot': 1,
    'client_state': 'Associated',
    'policy_profile': 'TEST-DMZ-En_Global_NF_5d6f92e7',
    'flex_profile': 'default-flex-profile',
    'wireless_lan_id': 17,
    'wlan_profile_name': 'TEST-DMZ-En_Global_NF_5d6f92e7',
    'wireless_lan_network_name_ssid': 'TEST-DMZ-Enterprise',
    'bssid': '3c41.0e3b.c42f',
    'connected_for_seconds': 396317,
    'protocol': '802.11ac',
    'channel': 48,
    'client_iif_id': '0xa0000002',
    'association_id': 1,
    'authentication_alogrithm': 'Open System',
    'idle_state_timeout': 'N/A',
    're_authentication_timeout_secs': {
        'configured': 1800, 'remaining_time': 1574
    },
    'session_warning_time': 'Timer not running',
    'input_policy_name': 'None',
    'input_policy_state': 'None',
    'input_policy_source': 'None',
    'output_policy_name': 'None',
    'output_policy_state': 'None',
    'output_policy_source': 'None',
    'wmm_support': 'Enabled',
    'u_apsd_support': {
        'status': 'Disabled'
    },
    'fastlane_support': 'Disabled',
    'client_active_state': 'Active',
    'power_save': 'OFF',
    'current_rate': 'm8 ss2',
    'supported_rates': [6.0, 9.0, 12.0, 18.0, 24.0, 36.0, 48.0, 54.0],
    'aaa_qos_rate_limit_parameters': {
        'upstream': {
            'qos_average_data_rate_kbps': 0,
            'qos_realtime_average_data_rate_kbps': 0,
            'qos_burst_data_rate_kbps': 0,
            'qos_realtime_burst_data_rate_kbps': 0
        },
        'downstream': {
            'qos_average_data_rate_kbps': 0,
            'qos_realtime_average_data_rate_kbps': 0,
            'qos_burst_data_rate_kbps': 0,
            'qos_realtime_burst_data_rate_kbps': 0
        }
    },
    'mobility': {
        'move_count': 0,
        'mobility_role': 'Local',
        'mobility_roam_type': 'None',
        'mobility_complete_timestamp': '02/15/2022 18:02:56 UTC'
    },
    'client_join_time': '02/17/2022 16:33:45 UTC',
    'client_state_servers': 'None',
    'client_acls': 'None',
    'policy_manager_state': 'Run',
    'last_policy_manager_state': 'IP Learn Complete',
    'client_entry_create_time_secs': 563766,
    'policy_type': 'WPA2',
    'encryption_cipher': 'CCMP (AES)',
    'authentication_key_management': '802.1x',
    'user_defined_private_network': 'Disabled',
    'user_defined_private_network_drop_unicast': 'Disabled',
    'encrypted_traffic_analytics': 'No',
    'protected_management_frame__802.11w': 'No',
    'eap_type': 'EAP-TLS',
    'vlan_override_after_webauth': 'No',
    'vlan': 'ENT-VLAN-DMZ',
    'multicast_vlan': 0,
    'wifi_direct_capabilities': {
        'wifi_direct_capable': 'No'
    },
    'central_nat': 'DISABLED',
    'session_manager': {
        'point_of_attachment': 'capwap_90000006',
        'iif_id': '0x90000006',
        'authorized': 'TRUE',
        'session_timeout': 1800,
        'common_session_id': '02321C0A00000026FE8D3B2D',
        'acct_session_id': '0x00000007',
        'last_tried_aaa_server_details': {
            'server_ip': '172.16.18.2'
        },
        'auth_method_status_list': {
            'method': {
                'Dot1x': {
                    'sm_state': 'AUTHENTICATED',
                    'sm_bend_state': 'IDLE'
                }
            }
        },
        'local_policies': {
            'service_template': {
                'wlan_svc_TEST-DMZ-En_Global_NF_5d6f92e7_local (priority 254)': {
                    'absolute_timer': 1800
                }
            }
        },
        'server_policies': {
            'vlan': 'ENT-VLAN-DMZ'
        },
        'resultant_policies': {
            'vlan_name': 'ENT-VLAN-DMZ',
            'vlan': 20,
            'absolute_timer': 1800
        }
    },
    'dns_snooped_ipv4_addresses': 'None',
    'dns_snooped_ipv6_addresses': 'None',
    'client_capabilities': {
        'cf_pollable': 'Not implemented',
        'cf_poll_request': 'Not implemented',
        'short_preamble': 'Not implemented',
        'pbcc': 'Not implemented',
        'channel_agility': 'Not implemented',
        'listen_interval': 0
    },
    'fast_bss_transition_details': {
        'reassociation_timeout': 20
    },
    '11v_bss_transition': 'Implemented',
    '11v_dms_capable': 'No',
    'qos_map_capable': 'No',
    'flexconnect_data_switching': 'Central',
    'flexconnect_dhcp_status': 'Central',
    'flexconnect_authentication': 'Central',
    'client_statistics': {
        'number_of_bytes_received': 12844445,
        'number_of_bytes_sent': 10484743,
        'number_of_packets_received': 102748,
        'number_of_packets_sent': 58259,
        'number_of_policy_errors': 0,
        'radio_signal_strength_indicator_dbm': -27,
        'signal_to_noise_ration_db': 56
    },
    'fabric_status': 'Disabled',
    'radio_measurement_enabled_capabilities': {
        'capabilities': [
            'Neighbor Report',
            'Passive Beacon Measurement',
            'Active Beacon Measurement',
            'AP Channel Report'
        ]
    },
    'client_scan_report_time': 'Timer not running',
    'nearby_ap_statistics': {
    },
    'eogre': 'Pending Classification',
    'device_info': {
        'device_type': 'Microsoft-Workstation',
        'device_name': 'MSFT 5.0',
        'protocol_map': '0x000009  (OUI, DHCP)',
        'protocols': {
            'DHCP': {
                1: {
                    'type': '12   19',
                    'data_size': '13',
                    'data': [
                        '00000000 00 0c 00 0f 44 45 53 4b  54 4f 50 2d 37 51 55 36 |....DESKTOP-7QU6|',
                        '00000010 44 4a 30 |DJ0             |'
                    ]
                },
                2: {
                    'type': '60   12',
                    'data_size': '0c',
                    'data': [
                        '00000000 00 3c 00 08 4d 53 46 54  20 35 2e 30 |.<..MSFT 5.0    |'
                    ]
                },
                3: {
                    'type': '55   18',
                    'data_size': '12',
                    'data': [
                        '00000000 00 37 00 0e 01 03 06 0f  1f 21 2b 2c 2e 2f 77 79 |.7.......!+,./wy|',
                        '00000010 f9 fc |..              |'
                    ]
                }
            }
        }
    },
    'max_client_protocol_capability': '802.11ac Wave 2',
    'cellular_capability': 'N/A',
    'advanced_scheduling_requests_details': {
        'Apple Specific Requests(ASR) Capabilities/Statistics': {
            'regular_asr_support': 'DISABLED'
        }
    }
}
