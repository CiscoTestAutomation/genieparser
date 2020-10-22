import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ======================
# Schema for:
#  * 'show wlan summary'
# ======================
class ShowWlanSummarySchema(MetaParser):
    """Schema for show wlan summary."""

    schema = {
        "wlan_summary": {
            "wlan_count": int,
            "wlan_id": {
                int: {
                    "profile_name": str,
                    "ssid": str,
                    "status": str,
                    "security": str
                }
            }
        }
    }


# ======================
# Parser for:
#  * 'show wlan summary'
# ======================
class ShowWlanSummary(ShowWlanSummarySchema):
    """Parser for show wlan summary"""

    cli_command = 'show ap cdp neighbor'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        wlan_summary_dict = {}

        # Number of WLANs: 4
        #
        # ID   Profile Name                     SSID                             Status Security
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 17   lizzard_Global                  lizzard                         UP     [WPA2][802.1x][FT + 802.1x][AES],[FT Enabled]
        # 18   wip_Global                      wip                             UP     [WPA2][802.1x + CCKM][AES]
        # 19   internet_Global                  internet                         UP     [open],MAC Filtering
        # 20   lizzard-l_Global                lizzard-legacy                  UP     [WPA2][802.1x][AES]

        # Number of WLANs: 4
        wlan_count_capture = re.compile(r"^Number\s+of\s+WLANs:\s+(?P<wlan_count>\d+)$")
        # ID   Profile Name                     SSID                             Status Security
        wlan_info_header_capture = re.compile(r"^ID\s+Profile\s+Name\s+SSID\s+Status\s+Security$")
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        delimiter_capture = re.compile(
            r"^----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------$")
        # 17   lizzard_Global                  lizzard                         UP     [WPA2][802.1x][FT + 802.1x][AES],[FT Enabled]
        wlan_info_capture = re.compile(
            r"^(?P<wlan_id>\d+)\s+(?P<profile_name>\S+)\s+(?P<ssid>\S+)\s+(?P<wlan_status>\S+)\s+(?P<status_security>.*$)")

        for line in out.splitlines():
            line = line.strip()
            # Number of WLANs: 4
            if wlan_count_capture.match(line):
                wlan_count_capture_match = wlan_count_capture.match(line)
                groups = wlan_count_capture_match.groupdict()
                if not wlan_summary_dict.get('wlan_summary', {}):
                    wlan_summary_dict['wlan_summary'] = {}
                wlan_count = int(groups['wlan_count'])
                wlan_summary_dict['wlan_summary']['wlan_count'] = wlan_count
                continue
            # ID   Profile Name                     SSID                             Status Security
            elif wlan_info_header_capture.match(line):
                wlan_info_header_capture_match = wlan_info_header_capture.match(line)
                groups = wlan_info_header_capture_match.groupdict()
                continue
            # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            elif delimiter_capture.match(line):
                delimiter_capture_match = delimiter_capture.match(line)
                groups = delimiter_capture_match.groupdict()
                continue
            # 17   lizzard_Global                  lizzard                         UP     [WPA2][802.1x][FT + 802.1x][AES],[FT Enabled]
            elif wlan_info_capture.match(line):
                wlan_info_capture_match = wlan_info_capture.match(line)
                groups = wlan_info_capture_match.groupdict()
                wlan_id = int(groups['wlan_id'])
                profile_name = groups['profile_name']
                ssid = groups['ssid']
                wlan_status = groups['wlan_status']
                status_security = groups['status_security']
                if not wlan_summary_dict['wlan_summary'].get('wlan_id', {}):
                    wlan_summary_dict['wlan_summary']['wlan_id'] = {}
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id] = {}
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'profile_name': profile_name})
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'ssid': ssid})
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'status': wlan_status})
                wlan_summary_dict['wlan_summary']['wlan_id'][wlan_id].update({'security': status_security})
                continue

        return wlan_summary_dict

      
# ==============================
# Schema for:
#  * 'show wlan id client stats'
# ==============================
class ShowWlanIdClientStatsSchema(MetaParser):
    """Schema for show wlan id client stats."""

    schema = {
        "current_client_state_statistics": {
            "authenticating": int,
            "ip_learn": int,
            "mobility": int,
            "run": int,
            "webauth_pending": int,
        },
        "total_client_delete_reasons": {
            "80211_association_failure": int,
            "80211_authentication_failure": int,
            "80211v_client_rssi_lower_than_the_association_rssi_threshold": int,
            "80211v_smart_roam_failed": int,
            "80211w_max_sa_queries_reached": int,
            "8021x_authentication_credential_failure": int,
            "8021x_authentication_timeout": int,
            "aaa_server_not_ready": int,
            "aaa_server_unavailable": int,
            "accounting_failure": int,
            "acl_failure": int,
            "admin_deauthentication": int,
            "anchor_creation_failure": int,
            "anchor_invalid_mobility_bssid": int,
            "anchor_no_memory": int,
            "ap_down/disjoin": int,
            "ap_initiated_delete_for_4_way_handshake_failed": int,
            "ap_initiated_delete_for_age_timeout": int,
            "ap_initiated_delete_for_all_on_slot": int,
            "ap_initiated_delete_for_ap_auth_stop": int,
            "ap_initiated_delete_for_association_expired_at_ap": int,
            "ap_initiated_delete_for_bad_aid": int,
            "ap_initiated_delete_for_channel_change": int,
            "ap_initiated_delete_for_channel_switch_at_ap": int,
            "ap_initiated_delete_for_client_acl_mismatch": int,
            "ap_initiated_delete_for_dhcp_timeout": int,
            "ap_initiated_delete_for_idle_timeout": int,
            "ap_initiated_delete_for_interface_reset": int,
            "ap_initiated_delete_for_mic_failure": int,
            "ap_initiated_delete_for_packet_max_retry": int,
            "ap_initiated_delete_for_reaper_radio": int,
            "ap_initiated_delete_for_reassociation_timeout": int,
            "ap_initiated_delete_for_request": int,
            "ap_initiated_delete_for_sa_query_timeout": int,
            "ap_initiated_delete_for_sensor_scan_next_radio": int,
            "ap_initiated_delete_for_sensor_scan_other_bssid": int,
            "ap_initiated_delete_for_sensor_station_timeout": int,
            "ap_initiated_delete_for_slot_disable": int,
            "ap_initiated_delete_for_stop_reassociation": int,
            "ap_initiated_delete_for_transmission_deauth": int,
            "ap_initiated_delete_for_transmission_fail_threshold": int,
            "ap_initiated_delete_for_uplink_receive_timeout": int,
            "ap_initiated_delete_for_vlan_delete": int,
            "ap_upgrade": int,
            "association_connection_timeout": int,
            "avc_client_re_anchored_at_the_foreign_controller": int,
            "bssid_down": int,
            "call_admission_controller_at_anchor_node": int,
            "client_8021x_failure": int,
            "client_abort": int,
            "client_beacon_loss": int,
            "client_blacklist": int,
            "client_captive_portal_security_failure": int,
            "client_connection_lost": int,
            "client_decryption_failure": int,
            "client_deleted_during_ha_recovery": int,
            "client_device_idle": int,
            "client_dhcp": int,
            "client_dot1x_timeout": int,
            "client_eap_id_timeout": int,
            "client_eap_timeout": int,
            "client_interface_disabled": int,
            "client_miscellaneous_reason": int,
            "client_not_allowed_by_assisted_roaming": int,
            "client_peer_triggered": int,
            "client_user_triggered_disassociation": int,
            "connection_timeout": int,
            "datapath_plumb": int,
            "db_error": int,
            "deauthentication_or_disassociation_request": int,
            "delete_received_from_ap": int,
            "dot11_ap_have_insufficient_bandwidth": int,
            "dot11_association_denied_unspecified": int,
            "dot11_denied_data_rates": int,
            "dot11_failure": int,
            "dot11_group_cipher_in_ie_validation_failed": int,
            "dot11_ie_validation_failed": int,
            "dot11_invalid_akm": int,
            "dot11_invalid_ft_ie": int,
            "dot11_invalid_mdie": int,
            "dot11_invalid_pairwise_cipher": int,
            "dot11_invalid_qos_parameter": int,
            "dot11_invalid_rsnie_capabilities": int,
            "dot11_max_sta": int,
            "dot11_qos_policy": int,
            "dot11_received_invalid_pmkid_in_the_received_rsn_ie": int,
            "dot11_sae_invalid_message": int,
            "dot11_unsupported_client_capabilities": int,
            "dot11_unsupported_rsn_version": int,
            "dot11r_pre_authentication_failure": int,
            "dot11v_association_failed": int,
            "dot11v_timer_timeout": int,
            "due_to_ip_zone_change": int,
            "due_to_mobility_failure": int,
            "due_to_ssid_change": int,
            "due_to_vlan_change": int,
            "eap_key_ack_bit_is_not_expected": int,
            "eap_key_error_bit_is_not_expected": int,
            "eap_key_install_bit_is_not_expected": int,
            "eap_key_mic_bit_expected": int,
            "eap_key_secure_bit_is_not_expected": int,
            "eogre_aaa_override_error": int,
            "eogre_all_gateways_down": int,
            "eogre_client_onboarding_error": int,
            "eogre_domain_shut": int,
            "eogre_empty_domain": int,
            "eogre_flex_no_active_gateway": int,
            "eogre_generic_join_failure": int,
            "eogre_ha_reconciliation": int,
            "eogre_invalid_domain": int,
            "eogre_invalid_gateway": int,
            "eogre_invalid_vlan": int,
            "eogre_mobility_handoff_error": int,
            "eogre_reset": int,
            "eogre_rule_matching_error": int,
            "error_while_ptk_computation": int,
            "fqdn_filter_definition_does_not_exist": int,
            "iapp_disassociation_for_wired_client": int,
            "idle_timeout": int,
            "incorrect_credentials": int,
            "inter_instance_roam_failure": int,
            "internal_error": int,
            "invalid_group_id_for_fqdn_filter_valid_range": int,
            "invalid_key_type": int,
            "invalid_qos_parameter": int,
            "ip_learn_connection_timeout": int,
            "ip_theft": int,
            "ip_update_timeout": int,
            "key_description_version_mismatch": int,
            "l2_auth_connection_timeout": int,
            "l3_auth_connection_timeout": int,
            "l3_authentication_failure": int,
            "l3_vlan_override_connection_timeout": int,
            "mac_and_ip_theft": int,
            "mac_auth_connection_timeout": int,
            "mac_authentication_failure": int,
            "mac_theft": int,
            "malformed_eap_key_frame": int,
            "manually_excluded": int,
            "mic_validation_failed": int,
            "mobility_connection_timeout": int,
            "mobility_peer_delete": int,
            "mobility_tunnel_down": int,
            "mobility_wlan_down": int,
            "nack_ifid_exists": int,
            "nack_ifid_mismatch": int,
            "nas_error": int,
            "no_dot1x_method_configuration": int,
            "no_ip": int,
            "no_operation": int,
            "policy_bind_failure": int,
            "policy_failure": int,
            "policy_manager_internal_error": int,
            "policy_parameter_mismatch": int,
            "port_admin_disabled": int,
            "qos_failure": int,
            "qos_policy_bind_on_ap_failure": int,
            "qos_policy_failure": int,
            "qos_policy_send_to_ap_failure": int,
            "qos_policy_unbind_on_ap_failure": int,
            "radio_down": int,
            "reauth_failure": int,
            "reauthentication_failure": int,
            "redirect_acl_failure": int,
            "sae_authentication_failure": int,
            "security_group_tag_failure": int,
            "session_manager": int,
            "session_timeout": int,
            "sm_session_creation_timeout": int,
            "static_ip_anchor_discovery_failure": int,
            "static_ip_connection_timeout": int,
            "supplicant_request": int,
            "supplicant_restart": int,
            "unknown": int,
            "vlan_failure": int,
            "web_authentication_failure": int,
            "wgb_wired_client_joins_as_a_direct_wireless_client": int,
            "wired_client_cleanup_due_to_wgb_roaming": int,
            "wired_client_deleted_due_to_wgb_delete": int,
            "wired_vlan_change": int,
            "wired_wgb_change": int,
            "wpa_group_key_update_timeout": int,
            "wpa_key_exchange_timeout": int,
            "wrong_filter_type_expected_postauth_fqdn_filter": int,
            "wrong_filter_type_expected_preauth_fqdn_filter": int,
            "wrong_psk": int,
            "wrong_replay_counter": int,
        },
        "wlan_info": {"id": int, "profile_name": "alfa"},
    }



# ==============================
# Parser for:
#  * 'show wlan id client stats'
# ==============================
class ShowWlanIdClientStats(ShowWlanIdClientStatsSchema):
    """Parser for show wlan id client stats"""

    cli_command = "show wlan id {id_number} client stats"

    def cli(self, id_number, output=None):
        if output is None:
            cmd = self.cli_command.format(id_number=id_number)
            out = self.device.execute(cmd)

        else:
            out = output

        # Wlan Profile Name: lizzard_Global, Wlan Id: 17
        # Current client state statistics:
        # -----------------------------------------------------------------------------
        # Authenticating         : 7
        # Mobility               : 0
        # IP Learn               : 0
        # Webauth Pending        : 0
        # Run                    : 2

        # Total client delete reasons
        # ---------------------------
        #     No Operation                                                    : 0
        #     Internal error                                                  : 0
        #     Deauthentication or disassociation request                      : 0
        #     Session Manager                                                 : 0
        #     L3 authentication failure                                       : 0
        #     Delete received from AP                                         : 0
        #     BSSID down                                                      : 1
        #     AP down/disjoin                                                 : 2
        #     Connection timeout                                              : 0
        #     MAC authentication failure                                      : 0
        #     Datapath plumb                                                  : 0
        #     Due to SSID change                                              : 163
        #
        # ...OUTPUT OMITTED...
        #
        #     L3 VLAN Override connection timeout                         : 0
        #     Mobility peer delete                                            : 0
        #     NACK IFID mismatch                                              : 0

        wlan_info_capture = re.compile(
            # Wlan Profile Name: lizzard_Global, Wlan Id: 17
            r"^Wlan Profile Name:\s+(?P<profile_name>\S+), Wlan Id: (?P<id>\d+)$"
        )

        # Current client state statistics:
        client_stats_capture = re.compile(r"^Current client state statistics:$")

        # Total client delete reasons
        client_delete_capture = re.compile(r"^Total client delete reasons$")

        # key : value
        key_value_capture = re.compile(r"^(?P<key>[\S\s]+\S)\s*:\s+(?P<value>\d+)$")
        
        header_group = {}

        wlan_info_obj = {}

        for line in out.splitlines():
            line = line.strip()

            if wlan_info_capture.match(line):
                match = wlan_info_capture.match(line)
                group = match.groupdict()

                group["id"] = int(group["id"])

                wlan_info_obj.update({"wlan_info": group})

            if client_stats_capture.match(line) or client_delete_capture.match(line):
                line_format = line.replace(" ", "_").replace(":", "").lower()
                wlan_info_obj.update({line_format: {}})

                header_group = wlan_info_obj[line_format]

            if key_value_capture.match(line):
                match = key_value_capture.match(line)
                group = match.groupdict()

                format_key = re.sub(r"\s+", "_", group["key"]).replace(".", "").replace(",", "").replace("-", "_").replace("___", "_").strip("__1..16").lower()
                format_value =  int(group["value"])

                print(format_key)

                header_group.update({format_key: format_value})

        return wlan_info_obj