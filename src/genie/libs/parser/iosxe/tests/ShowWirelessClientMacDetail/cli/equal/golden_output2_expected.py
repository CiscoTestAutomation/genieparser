expected_output = {
    'client_mac_address': 'dca6.325d.150f',
    'client_mac_type': 'Universally Administered Address',
    'client_ipv4_address': '46.123.31.1',
    'client_ipv6_addresses': 'fe80::dc86:d296:e307:c8ce',
    'client_username': 'DC-A6-32-5D-15-0F',
    'ap_mac_address': '10b3.d63e.5ce0',
    'ap_name': 'AP084F.A9A2.86A4',
    'ap_slot': 1,
    'client_state': 'Associated',
    'policy_profile': 'IOSXE-D1-INETIU-WLANID-512',
    'flex_profile': 'N/A',
    'wireless_lan_id': 512,
    'wlan_profile_name': 'IOSXE-D1-INetIU-CWA',
    'wireless_lan_network_name_ssid': 'IOSXE-D1-INetiU-CWA',
    'bssid': '10b3.d63e.5cee',
    'connected_for_seconds': 166,
    'protocol': '802.11ac',
    'channel': 128,
    'client_iif_id': '0xa0000001',
    'association_id': 1,
    'authentication_alogrithm': 'Open System',
    'idle_state_timeout': 'N/A',
    'session_timeout': '1800 sec (Timer not running)',
    'session_warning_time': 'Timer not running',
    'input_policy_name': 'None',
    'input_policy_state': 'None',
    'input_policy_source': 'None',
    'output_policy_name': 'None',
    'output_policy_state': 'None',
    'output_policy_source': 'None',
    'wmm_support': 'Enabled',
    'u_apsd_support': {
        'status': 'Enabled',
        'u_apsd_value': 0,
        'apsd_acs': ['BK', 'BE', 'VI', 'VO']
    },
    'fastlane_support': 'Disabled',
    'client_active_state': 'Active',
    'power_save': 'OFF',
    'current_rate': 'm9 ss1',
    'supported_rates': [9.0, 18.0, 36.0, 48.0, 54.0],
    'mobility': {
        'move_count': 0,
        'mobility_role': 'Local',
        'mobility_roam_type': 'None',
        'mobility_complete_timestamp': '06/15/2021 15:06:12 British',
    },
    'client_join_time': '06/15/2021 15:06:12 British',
    'client_state_servers': 'None',
    'client_acls': 'None',
    'policy_manager_state': 'Webauth Pending',
    'last_policy_manager_state': 'IP Learn Complete',
    'client_entry_create_time_secs': 166,
    'policy_type': 'N/A',
    'encryption_cipher': 'None',
    'user_defined_private_network': 'Disabled',
    'user_defined_private_network_drop_unicast': 'Disabled',
    'encrypted_traffic_analytics': 'No',
    'protected_management_frame__802.11w': 'No',
    'eap_type': 'Not Applicable',
    'vlan_override_after_webauth': 'No',
    'vlan': 'WLC-DATA',
    'multicast_vlan': 0,
    'wifi_direct_capabilities': {
        'wifi_direct_capable': 'No'
    },
    'central_nat': 'DISABLED',
    'session_manager': {
        'point_of_attachment': 'capwap_90000004',
        'iif_id': '0x90000004',
        'authorized': 'TRUE',
        'session_timeout': 1800,
        'common_session_id': '445A583B000011D9103562E6',
        'acct_session_id': '0x0000005e',
        'last_tried_aaa_server_details': {
            'server_ip': '120.11.78.100'
        },
        'auth_method_status_list': {
            'method': {
                'MAB': {
                    'sm_state': 'TERMINATE',
                    'authen_status': 'Success'
                }
            }
        },
        'local_policies': {
            'service_template': {
                'wlan_svc_IOSXE-D1-INETIU-WLANID-512_local (priority 254)': {
                    'vlan': 'WLC-DATA',
                    'absolute_timer': 1800
                }
            }
        },
        'server_policies': {
            'url_redirect_acl': 'ACL_WEBAUTH_REDIRECT',
            'url_redirect': 'https://<placeholder>-WLAN-ISE.lab.<placeholder>:8443/portal/gateway?sessionId=445A583B000011D9103562E6&portal=f0ae43f0-7159-11e7-a355-005056aba474&action=cwa&token=5041ffbf4f184469c4db42e2a92ea637'},
        'resultant_policies': {
            'url_redirect_acl': 'ACL_WEBAUTH_REDIRECT',
            'url_redirect': 'https://<placeholder>-WLAN-ISE.lab.<placeholder>:8443/portal/gateway?sessionId=445A583B000011D9103562E6&portal=f0ae43f0-7159-11e7-a355-005056aba474&action=cwa&token=5041ffbf4f184469c4db42e2a92ea637',
            'vlan_name': 'WLC-DATA',
            'vlan': 145,
            'absolute_timer': 1800,
        },
    },
    'dns_snooped_ipv4_addresses': 'None',
    'dns_snooped_ipv6_addresses': 'None',
    'client_capabilities': {
        'cf_pollable': 'Not implemented',
        'cf_poll_request': 'Not implemented',
        'short_preamble': 'Not implemented',
        'pbcc': 'Not implemented',
        'channel_agility': 'Not implemented',
        'listen_interval': 0,
    },
    'fast_bss_transition_details': {
        'reassociation_timeout': 20
    },
    '11v_bss_transition': 'Implemented',
    '11v_dms_capable': 'No',
    'qos_map_capable': 'No',
    'flexconnect_data_switching': 'N/A',
    'flexconnect_dhcp_status': 'N/A',
    'flexconnect_authentication': 'N/A',
    'flexconnect_central_association': 'N/A',
    'client_statistics': {
        'number_of_bytes_received': 208,
        'number_of_bytes_sent': 0,
        'number_of_packets_received': 4,
        'number_of_packets_sent': 2,
        'number_of_policy_errors': 0,
        'radio_signal_strength_indicator_dbm': -37,
        'signal_to_noise_ration_db': 54,
    },
    'fabric_status': 'Disabled',
    'radio_measurement_enabled_capabilities': {
        'capabilities': [
            'Neighbor Report',
            'Passive Beacon Measurement',
            'Active Beacon Measurement',
            'Table Beacon Measurement',
            'Statistics Measurement',
            'AP Channel Report',
        ]
    },
    'client_scan_report_time': 'Timer not running',
    'nearby_ap_statistics': {},
    'eogre': 'Pending Classification',
    'max_client_protocol_capability': '802.11ac Wave 2',
    'cellular_capability': 'N/A',
}
