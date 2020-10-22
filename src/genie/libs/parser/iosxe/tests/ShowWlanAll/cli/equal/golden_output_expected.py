expected_output = {
    "wlan_names": {
        "lizzard_Fabric_F_cf6efda4": {
            "identifier": 17,
            "ssid": "lizzard",
            "status": "Enabled",
            "broadcast_ssid": "Enabled",
            "advertise_ap_name": "Disabled",
            "universal_ap_admin": "Disabled",
            "max_clients_wlan": 0,
            "max_clients_ap": 0,
            "max_clients_ap_radio": 200,
            "okc": "Enabled",
            "active_clients": 4,
            "chd_per_wlan": "Enabled",
            "wmm": "Allowed",
            "channel_scan_defer_priority": {
                "priority": [
                    5,
                    6
                ]
            },
            "scan_defer_time_msecs": 100,
            "media_stream_multicast_direct": "Disabled",
            "ccx_aironet_support": "Disabled",
            "p2p_blocking_action": "Disabled",
            "radio_policy": "802.11a only",
            "local_eap_authentication": "Disabled",
            "mac_filter_authorization_list_name": "Disabled",
            "mac_filter_override_authorization_list_name": "Disabled",
            "dot1x_authentication_list_name": "dnac-list",
            "dot1x_authorization_list_name": "Disabled",
            "security": {
                "dot11_authentication": "Open System",
                "static_wep_keys": "Disabled",
                "wifi_protected_access_wpa1_wpa2_wpa3": "Enabled",
                "wifi_protected_access_wpa": {
                    "wpa_ssn_ie": "Disabled"
                },
                "wifi_protected_access_wpa2": {
                    "wpa2_rsn_ie": "Enabled",
                    "wpa2_attributes": {
                        "mpsk": "Disabled",
                        "aes": "Enabled",
                        "ccmp256": "Disabled",
                        "gcmp128": "Disabled",
                        "gcmp256": "Disabled",
                        "randomized_gtk": "Disabled"
                    }
                },
                "wifi_protected_access_wpa3": {
                    "wpa3_ie": "Disabled"
                },
                "auth_key_mgmt": {
                    "dot1x": "Enabled",
                    "psk": "Disabled",
                    "cckm": "Disabled",
                    "ft_dot1x": "Enabled",
                    "ft_psk": "Disabled",
                    "dot1x_sha256": "Disabled",
                    "psk_sha256": "Disabled",
                    "sae": "Disabled",
                    "owe": "Disabled",
                    "suiteb_1x": "Disabled",
                    "suiteb192_1x": "Disabled"
                },
                "cckm_tsf_tolerance_msecs": 1000,
                "owe_transition_mode": "Disabled",
                "osen": "Disabled",
                "ft_support": {
                    "ft_support_status": "Enabled",
                    "ft_reassociation_timer_secs": 20,
                    "ft_over_the_ds_mode": "Disabled"
                },
                "pmf_support": {
                    "pmf_support_status": "Disabled",
                    "pmf_association_comeback_timeout_secs": 1,
                    "pmf_sa_query_time_msecs": 200
                },
                "web_based_authenticaion": "Disabled",
                "conditional_web_redirect": "Disabled",
                "splash_page_web_redirect": "Disabled",
                "webauth_on_mac_filter_failure": "Disabled",
                "webauth_authentication_list_name": "Disabled",
                "webauth_authorization_list_name": "Disabled",
                "webauth_parameter_map": "Disabled"
            },
            "band_select": "Disabled",
            "load_balancing": "Disabled",
            "multicast_buffer": "Disabled",
            "multicast_buffer_size": 0,
            "ip_source_guard": "Disabled",
            "assisted_roaming": {
                "neighbbor_list": "Enabled",
                "prediction_list": "Disabled",
                "dual_band_support": "Disabled"
            },
            "ieee_dot11v_parameters": {
                "directed_multicast_service": "Enabled",
                "bss_max_idle": {
                    "bss_max_idle_status": "Enabled",
                    "protected_mode": "Disabled"
                },
                "traffic_filtering_servce": "Disabled",
                "bss_transition": {
                    "bss_transition_status": "Enabled",
                    "disassociation_imminent": {
                        "disassociation_imminent_status": "Disabled",
                        "optimised_roaming_timer": 40,
                        "timer": 200
                    }
                },
                "wmn_sleep_mode": "Disabled"
            },
            "dot11ac_mu_mimo": "Enabled",
            "dot11ax_parameters": {
                "ofdma_downlink": "Enabled",
                "ofdma_uplink": "Enabled",
                "mu_mimo_downlink": "Enabled",
                "mu_mimo_uplink": "Enabled",
                "bss_target_wake_up_time": "Enabled",
                "bss_target_wake_up_time_broadcast_support": "Enabled"
            },
            "mdns_gateway_status": "Bridge",
            "wifi_alliance_agile_multiband": "Disabled",
            "device_analytics": {
                "advertise_support": "Enabled",
                "share_data_with_client": "Disabled"
            }
        },
        "internet_Fabric_F_ed7ae33f": {
            "identifier": 19,
            "ssid": "internet",
            "status": "Enabled",
            "broadcast_ssid": "Enabled",
            "advertise_ap_name": "Disabled",
            "universal_ap_admin": "Disabled",
            "max_clients_wlan": 0,
            "max_clients_ap": 0,
            "max_clients_ap_radio": 200,
            "okc": "Enabled",
            "active_clients": 5,
            "chd_per_wlan": "Enabled",
            "wmm": "Allowed",
            "channel_scan_defer_priority": {
                "priority": [
                    5,
                    6
                ]
            },
            "scan_defer_time_msecs": 100,
            "media_stream_multicast_direct": "Disabled",
            "ccx_aironet_support": "Disabled",
            "p2p_blocking_action": "Disabled",
            "radio_policy": "All",
            "local_eap_authentication": "Disabled",
            "mac_filter_authorization_list_name": "default",
            "mac_filter_override_authorization_list_name": "Disabled",
            "dot1x_authentication_list_name": "Disabled",
            "dot1x_authorization_list_name": "Disabled",
            "security": {
                "dot11_authentication": "Open System",
                "static_wep_keys": "Disabled",
                "wifi_protected_access_wpa1_wpa2_wpa3": "Disabled",
                "owe_transition_mode": "Disabled",
                "osen": "Disabled",
                "ft_support": {
                    "ft_support_status": "Disabled",
                    "ft_reassociation_timer_secs": 20,
                    "ft_over_the_ds_mode": "Disabled"
                },
                "pmf_support": {
                    "pmf_support_status": "Disabled",
                    "pmf_association_comeback_timeout_secs": 1,
                    "pmf_sa_query_time_msecs": 200
                },
                "web_based_authenticaion": "Disabled",
                "conditional_web_redirect": "Disabled",
                "splash_page_web_redirect": "Disabled",
                "webauth_on_mac_filter_failure": "Disabled",
                "webauth_authentication_list_name": "Disabled",
                "webauth_authorization_list_name": "Disabled",
                "webauth_parameter_map": "Disabled"
            },
            "band_select": "Disabled",
            "load_balancing": "Disabled",
            "multicast_buffer": "Disabled",
            "multicast_buffer_size": 0,
            "ip_source_guard": "Disabled",
            "assisted_roaming": {
                "neighbbor_list": "Enabled",
                "prediction_list": "Disabled",
                "dual_band_support": "Disabled"
            },
            "ieee_dot11v_parameters": {
                "directed_multicast_service": "Enabled",
                "bss_max_idle": {
                    "bss_max_idle_status": "Enabled",
                    "protected_mode": "Disabled"
                },
                "traffic_filtering_servce": "Disabled",
                "bss_transition": "Enabled",
                "bss_transition": {
                    "bss_transition_status": "Enabled",
                    "disassociation_imminent": {
                        "disassociation_imminent_status": "Disabled",
                        "optimised_roaming_timer": 40,
                        "timer": 200
                    }
                },
                "wmn_sleep_mode": "Disabled"
            },
            "dot11ac_mu_mimo": "Enabled",
            "dot11ax_parameters": {
                "ofdma_downlink": "Enabled",
                "ofdma_uplink": "Enabled",
                "mu_mimo_downlink": "Enabled",
                "mu_mimo_uplink": "Enabled",
                "bss_target_wake_up_time": "Enabled",
                "bss_target_wake_up_time_broadcast_support": "Enabled"
            },
            "mdns_gateway_status": "Bridge",
            "wifi_alliance_agile_multiband": "Disabled",
            "device_analytics": {
                "advertise_support": "Enabled",
                "share_data_with_client": "Disabled"
            }
        },
        "lizzard_l_Fabric_F_90c6fda4": {
            "identifier": 18,
            "ssid": "lizzard_legacy",
            "status": "Enabled",
            "broadcast_ssid": "Disabled",
            "advertise_ap_name": "Disabled",
            "universal_ap_admin": "Disabled",
            "max_clients_wlan": 0,
            "max_clients_ap": 0,
            "max_clients_ap_radio": 200,
            "okc": "Enabled",
            "active_clients": 0,
            "chd_per_wlan": "Enabled",
            "wmm": "Allowed",
            "channel_scan_defer_priority": {
                "priority": [
                    5,
                    6
                ]
            },
            "scan_defer_time_msecs": 100,
            "media_stream_multicast_direct": "Disabled",
            "ccx_aironet_support": "Disabled",
            "p2p_blocking_action": "Disabled",
            "radio_policy": "802.11b and 802.11g only",
            "local_eap_authentication": "Disabled",
            "mac_filter_authorization_list_name": "Disabled",
            "mac_filter_override_authorization_list_name": "Disabled",
            "dot1x_authentication_list_name": "dnac-list",
            "dot1x_authorization_list_name": "Disabled",
            "security": {
                "dot11_authentication": "Open System",
                "static_wep_keys": "Disabled",
                "wifi_protected_access_wpa1_wpa2_wpa3": "Enabled",
                "wifi_protected_access_wpa": {
                    "wpa_ssn_ie": "Disabled"
                },
                "wifi_protected_access_wpa2": {
                    "wpa2_rsn_ie": "Enabled",
                    "wpa2_attributes": {
                        "mpsk": "Disabled",
                        "aes": "Enabled",
                        "ccmp256": "Disabled",
                        "gcmp128": "Disabled",
                        "gcmp256": "Disabled",
                        "randomized_gtk": "Disabled"
                    }
                },
                "wifi_protected_access_wpa3": {
                    "wpa3_ie": "Disabled"
                },
                "auth_key_mgmt": {
                    "dot1x": "Enabled",
                    "psk": "Disabled",
                    "cckm": "Disabled",
                    "ft_dot1x": "Disabled",
                    "ft_psk": "Disabled",
                    "dot1x_sha256": "Disabled",
                    "psk_sha256": "Disabled",
                    "sae": "Disabled",
                    "owe": "Disabled",
                    "suiteb_1x": "Disabled",
                    "suiteb192_1x": "Disabled"
                },
                "cckm_tsf_tolerance_msecs": 1000,
                "owe_transition_mode": "Disabled",
                "osen": "Disabled",
                "ft_support": {
                    "ft_support_status": "Adaptive",
                    "ft_reassociation_timer_secs": 20,
                    "ft_over_the_ds_mode": "Disabled"
                },
                "pmf_support": {
                    "pmf_support_status": "Disabled",
                    "pmf_association_comeback_timeout_secs": 1,
                    "pmf_sa_query_time_msecs": 200
                },
                "web_based_authenticaion": "Disabled",
                "conditional_web_redirect": "Disabled",
                "splash_page_web_redirect": "Disabled",
                "webauth_on_mac_filter_failure": "Disabled",
                "webauth_authentication_list_name": "Disabled",
                "webauth_authorization_list_name": "Disabled",
                "webauth_parameter_map": "Disabled"
            },
            "band_select": "Disabled",
            "load_balancing": "Disabled",
            "multicast_buffer": "Disabled",
            "multicast_buffer_size": 0,
            "ip_source_guard": "Disabled",
            "assisted_roaming": {
                "neighbbor_list": "Enabled",
                "prediction_list": "Disabled",
                "dual_band_support": "Disabled"
            },
            "ieee_dot11v_parameters": {
                "directed_multicast_service": "Enabled",
                "bss_max_idle": {
                    "bss_max_idle_status": "Enabled",
                    "protected_mode": "Disabled"
                },
                "traffic_filtering_servce": "Disabled",
                "bss_transition": {
                    "bss_transition_status": "Enabled",
                    "disassociation_imminent": {
                        "disassociation_imminent_status": "Disabled",
                        "optimised_roaming_timer": 40,
                        "timer": 200
                    }
                },
                "wmn_sleep_mode": "Disabled"
            },
            "dot11ac_mu_mimo": "Enabled",
            "dot11ax_parameters": {
                "ofdma_downlink": "Enabled",
                "ofdma_uplink": "Enabled",
                "mu_mimo_downlink": "Enabled",
                "mu_mimo_uplink": "Enabled",
                "bss_target_wake_up_time": "Enabled",
                "bss_target_wake_up_time_broadcast_support": "Enabled"
            },
            "mdns_gateway_status": "Bridge",
            "wifi_alliance_agile_multiband": "Disabled",
            "device_analytics": {
                "advertise_support": "Enabled",
                "share_data_with_client": "Disabled"
            }
        }
    }
}
