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
        Optional("client_delete"): {
            "aaa_not_ready": int,
            "aaa_unavailable": int,
            "accounting_fail": int,
            "acl_fail": int,
            "admin_deauth": int,
            "anchor": {
                "call_admission_controller": int,
                "create_fail": int,
                "invalid_mobility_bssid": int,
                "no_memory": int,
                "static_ip_fail": int,
            },
            "ap_down": int,
            "ap_upgrade": int,
            "apinit": {
                "4way_fail": int,
                "acl_mismatch": int,
                "age_timeout": int,
                "all_slot": int,
                "association_expired": int,
                "auth_stop": int,
                "bad_aid": int,
                "channel_change": int,
                "channel_switch": int,
                "dhcp_timeout": int,
                "idle_timeout": int,
                "interface_reset": int,
                "max_retry": int,
                "mic_fail": int,
                "reaper_radio": int,
                "reassocation_timeout": int,
                "request": int,
                "sa_timeout": int,
                "scan_next_radio": int,
                "scan_other_bssid": int,
                "sensor_station_timeout": int,
                "slot_disable": int,
                "stop_reassociation": int,
                "transmission_deauth": int,
                "transmission_fail_threshold": int,
                "uplink_recieve_timeout": int,
                "vlan_delete": int,
            },
            "avc_client_reanchor": int,
            "bad_credentials": int,
            "blacklist": int,
            "bssid_down": int,
            "cleanup_wgb_roam": int,
            "client": {
                "abort": int,
                "auth_8021x_fail": int,
                "beacon_loss": int,
                "captive_portal_fail": int,
                "connection_lost": int,
                "decrypt_fail": int,
                "device_idle": int,
                "dhcp": int,
                "dot1x_timeout": int,
                "eap_id_timeout": int,
                "eap_timeout": int,
                "int_disable": int,
                "misc_reason": int,
                "peer_trigger": int,
                "trigger_disassociate": int,
            },
            "connection_timeout": {
                "assocation": int,
                "iplearn": int,
                "l2auth": int,
                "l3auth": int,
                "l3vlan_override": int,
                "macauth": int,
                "mobility": int,
                "sm_session_creation": int,
                "static_ip": int,
            },
            "datapath_plumb": int,
            "db_error": int,
            "deauth_request": int,
            "delete_from_ap": int,
            "dot11": {
                "ap_insufficient_bandwidth": int,
                "assocation_fail": int,
                "auth_fail": int,
                "denied_data_rates": int,
                "denied_unspecified": int,
                "fail": int,
                "groupcipher_validation_failed": int,
                "ie_validation_failed": int,
                "invalid_akm": int,
                "invalid_ft_ie": int,
                "invalid_mdie": int,
                "invalid_pairwise_cipher": int,
                "invalid_pkmid": int,
                "invalid_qos_parameter": int,
                "invalid_rsnie_capabilities": int,
                "max_sta": int,
                "qos_policy": int,
                "sae_auth_fail": int,
                "sae_invalid": int,
                "unsupported_client": int,
                "unsupported_rsn_version": int,
            },
            "dot11v": {
                "association_fail": int,
                "preauth_fail": int,
                "rssi_low_threshold": int,
                "smart_roam_fail": int,
                "timer_timeout": int,
            },
            "dot11w_max_sa": int,
            "dot11x_auth_timeout": int,
            "dot11x_credential_fail": int,
            "dot1x_no_config": int,
            "eap": {
                "bad_keyframe": int,
                "invalid_key_type": int,
                "key_ack_unexpected": int,
                "key_error_unexpected": int,
                "key_install_unexpected": int,
                "key_mic_expected": int,
                "key_secure_unexected": int,
                "key_version_mismatch": int,
                "mic_validation_failed": int,
            },
            "eogre": {
                "aaa_override_error": int,
                "all_gateways_down": int,
                "domain_shut": int,
                "empty_domain": int,
                "flex_no_gateway": int,
                "generic_join_fail": int,
                "ha_reconcile": int,
                "invalid_domain": int,
                "invalid_gateway": int,
                "invalid_vlan": int,
                "mobility_handoff_error": int,
                "onboarding_error": int,
                "reset": int,
                "rule_error": int,
            },
            "fqdn": {
                "filter_missing": int,
                "invalid_group_id": int,
                "wrong_postauth_filter": int,
                "wrong_preauth_filter": int,
            },
            "ha_recovery": int,
            "iapp_disassociate_wired": int,
            "idle_timeout": int,
            "internal_error": int,
            "ip_theft": int,
            "ip_update_timeout": int,
            "ip_zone_change": int,
            "l3_auth_fail": int,
            "mac": {"auth_fail": int, "ip_theft": int, "theft": int},
            "manually_excluded": int,
            "mobility": {"fail": int, "peer_delete": int, "tunnel_down": int, "wlan_down": int},
            "nack_ifid_exists": int,
            "nack_ifid_mismatch": int,
            "nas_error": int,
            "no_ip": int,
            "no_operation": int,
            "not_allowed_roaming": int,
            "policy": {
                "bind_fail": int,
                "fail": int,
                "manager_error": int,
                "manager_mismatch": int,
            },
            "port_admin_disabled": int,
            "ptk_error": int,
            "qos": {
                "bind_ap_fail": int,
                "fail": int,
                "invalid_parameter": int,
                "policy_fail": int,
                "send_ap_fail": int,
                "unbind_ap_fail": int,
            },
            "radio_down": int,
            "reauth_fail": int,
            "reauthentication_fail": int,
            "redirect_acl_fail": int,
            "roam_fail": int,
            "security_grouptag_fail": int,
            "session_manager": int,
            "session_timeout": int,
            "ssid_change": int,
            "supplicant_request": int,
            "supplicant_restart": int,
            "unknown": int,
            "vlan_change": int,
            "vlan_fail": int,
            "web_auth_fail": int,
            "wired": {
                "vlan_change": int,
                "wbg_joins": int,
                "wgb_change": int,
                "wgb_delete": int,
            },
            "wpa_groupkey_timeout": int,
            "wpa_key_timeout": int,
            "wrong_psk": int,
            "wrong_replay_counter": int,
        },
        Optional("client_stats"): {
            "auth": int,
            "ip_learn": int,
            "mobility": int,
            "run": int,
            "webauth": int,
        },
        Optional("wlan"): {"id": int, "profile_name": str},
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
        # [--OUTPUT OMITTED--]
        #
        #     L3 VLAN Override connection timeout                         : 0
        #     Mobility peer delete                                            : 0
        #     NACK IFID mismatch                                              : 0


        wlan_capture = (
            # Wlan Profile Name: lizzard_Global, Wlan Id: 17
            r"^Wlan Profile Name:\s+(?P<profile_name>\S+), Wlan Id: (?P<id>\d+)$"
        )

        # Current client state statistics:
        client_stats_capture = (
            r"^"
            #   Authenticating         : 7
            r"\s+Authenticating\s+:\s+(?P<auth>\d+)\n+"
            #   Mobility               : 0
            r"\s+Mobility\s+:\s+(?P<mobility>\d+)\n+"
            #   IP Learn               : 0
            r"\s+IP Learn\s+:\s+(?P<ip_learn>\d+)\n+"
            #   Webauth Pending        : 0
            r"\s+Webauth Pending\s+:\s+(?P<webauth>\d+)\n+"
            #   Run                    : 2
            r"\s+Run\s+:\s+(?P<run>\d+)\n+"
        )

        # Total client delete reasons
        client_delete_capture = (
            r"^"
            # No Operation                                                    : 0
            r"\s+No Operation\s+:\s+(?P<no_operation>\d+)\n+"
            # Internal error                                                  : 0
            r"\s+Internal error\s+:\s+(?P<internal_error>\d+)\n+"
            # Deauthentication or disassociation request                      : 0
            r"\s+Deauthentication or disassociation request\s+:\s+(?P<deauth_request>\d+)\n+"
            # Session Manager                                                 : 0
            r"\s+Session Manager\s+:\s+(?P<session_manager>\d+)\n+"
            # L3 authentication failure                                       : 0
            r"\s+L3 authentication failure\s+:\s+(?P<l3_auth_fail>\d+)\n+"
            # Delete received from AP                                         : 0
            r"\s+Delete received from AP\s+:\s+(?P<delete_from_ap>\d+)\n+"
            # BSSID down                                                      : 1
            r"\s+BSSID down\s+:\s+(?P<bssid_down>\d+)\n+"
            # AP down/disjoin                                                 : 2
            r"\s+AP down/disjoin\s+:\s+(?P<ap_down>\d+)\n+"
            # Connection timeout                                              : 0
            r"\s+Connection timeout\s+:\s+(?P<connection_timeout>\d+)\n+"
            # MAC authentication failure                                      : 0
            r"\s+MAC authentication failure\s+:\s+(?P<mac_auth_fail>\d+)\n+"
            # Datapath plumb                                                  : 0
            r"\s+Datapath plumb\s+:\s+(?P<datapath_plumb>\d+)\n+"
            # Due to SSID change                                              : 163
            r"\s+Due to SSID change\s+:\s+(?P<ssid_change>\d+)\n+"
            # Due to VLAN change                                              : 0
            r"\s+Due to VLAN change\s+:\s+(?P<vlan_change>\d+)\n+"
            # Due to IP Zone change                                              : 0
            r"\s+Due to IP Zone change\s+:\s+(?P<ip_zone_change>\d+)\n+"
            # Admin deauthentication                                          : 0
            r"\s+Admin deauthentication\s+:\s+(?P<admin_deauth>\d+)\n+"
            # QoS failure                                                     : 0
            r"\s+QoS failure\s+:\s+(?P<qos_fail>\d+)\n+"
            # WPA key exchange timeout                                        : 13
            r"\s+WPA key exchange timeout\s+:\s+(?P<wpa_key_timeout>\d+)\n+"
            # WPA group key update timeout                                    : 101
            r"\s+WPA group key update timeout\s+:\s+(?P<wpa_groupkey_timeout>\d+)\n+"
            # 802.11w MAX SA queries reached                                  : 0
            r"\s+802.11w MAX SA queries reached\s+:\s+(?P<dot11w_max_sa>\d+)\n+"
            # Client deleted during HA recovery                               : 0
            r"\s+Client deleted during HA recovery\s+:\s+(?P<ha_recovery>\d+)\n+"
            # Client blacklist                                                : 0
            r"\s+Client blacklist\s+:\s+(?P<blacklist>\d+)\n+"
            # Inter instance roam failure                                     : 0
            r"\s+Inter instance roam failure\s+:\s+(?P<roam_fail>\d+)\n+"
            # Due to mobility failure                                         : 0
            r"\s+Due to mobility failure\s+:\s+(?P<mobility_fail>\d+)\n+"
            # Session timeout                                                 : 2
            r"\s+Session timeout\s+:\s+(?P<session_timeout>\d+)\n+"
            # Idle timeout                                                    : 0
            r"\s+Idle timeout\s+:\s+(?P<idle_timeout>\d+)\n+"
            # Supplicant request                                              : 25
            r"\s+Supplicant request\s+:\s+(?P<supplicant_request>\d+)\n+"
            # NAS error                                                       : 0
            r"\s+NAS error\s+:\s+(?P<nas_error>\d+)\n+"
            # Policy Manager internal error                                   : 0
            r"\s+Policy Manager internal error\s+:\s+(?P<policy_manager_error>\d+)\n+"
            # Mobility WLAN down                                              : 0
            r"\s+Mobility WLAN down\s+:\s+(?P<mobility_wlan_down>\d+)\n+"
            # Mobility tunnel down                                            : 0
            r"\s+Mobility tunnel down\s+:\s+(?P<mobility_tunnel_down>\d+)\n+"
            # 80211v smart roam failed                                        : 0
            r"\s+80211v smart roam failed\s+:\s+(?P<dot11v_smart_roam_fail>\d+)\n+"
            # DOT11v timer timeout                                            : 0
            r"\s+DOT11v timer timeout\s+:\s+(?P<dot11v_timer_timeout>\d+)\n+"
            # DOT11v association failed                                       : 0
            r"\s+DOT11v association failed \s+:\s+(?P<dot11v_association_fail>\d+)\n+"
            # DOT11r pre-authentication failure                               : 0
            r"\s+DOT11r pre-authentication failure\s+:\s+(?P<dot11v_preauth_fail>\d+)\n+"
            # SAE authentication failure                                      : 0
            r"\s+SAE authentication failure\s+:\s+(?P<dot11_sae_auth_fail>\d+)\n+"
            # DOT11 failure                                                   : 0
            r"\s+DOT11 failure \s+:\s+(?P<dot11_fail>\d+)\n+"
            # DOT11 SAE invalid message                                       : 0
            r"\s+DOT11 SAE invalid message\s+:\s+(?P<dot11_sae_invalid>\d+)\n+"
            # DOT11 unsupported client capabilities                           : 0
            r"\s+DOT11 unsupported client capabilities\s+:\s+(?P<dot11_unsupported_client>\d+)\n+"
            # DOT11 association denied unspecified                            : 0
            r"\s+DOT11 association denied unspecified\s+:\s+(?P<dot11_denied_unspecified>\d+)\n+"
            # DOT11 max STA                                                   : 0
            r"\s+DOT11 max STA\s+:\s+(?P<dot11_max_sta>\d+)\n+"
            # DOT11 denied data rates                                         : 0
            r"\s+DOT11 denied data rates\s+:\s+(?P<dot11_denied_data_rates>\d+)\n+"
            # 802.11v Client RSSI lower than the association RSSI threshold   : 0
            r"\s+802.11v Client RSSI lower than the association RSSI threshold\s+:\s+(?P<dot11v_rssi_low_threshold>\d+)\n+"
            # invalid QoS parameter                                           : 0
            r"\s+invalid QoS parameter\s+:\s+(?P<qos_invalid_parameter>\d+)\n+"
            # DOT11 IE validation failed                                      : 0
            r"\s+DOT11 IE validation failed\s+:\s+(?P<dot11_ie_validation_failed>\d+)\n+"
            # DOT11 group cipher in IE validation failed                      : 0
            r"\s+DOT11 group cipher in IE validation failed\s+:\s+(?P<dot11_groupcipher_validation_failed>\d+)\n+"
            # DOT11 invalid pairwise cipher                                   : 0
            r"\s+DOT11 invalid pairwise cipher\s+:\s+(?P<dot11_invalid_pairwise_cipher>\d+)\n+"
            # DOT11 invalid AKM                                               : 0
            r"\s+DOT11 invalid AKM \s+:\s+(?P<dot11_invalid_akm>\d+)\n+"
            # DOT11 unsupported RSN version                                   : 0
            r"\s+DOT11 unsupported RSN version\s+:\s+(?P<dot11_unsupported_rsn_version>\d+)\n+"
            # DOT11 invalid RSNIE capabilities                                : 0
            r"\s+DOT11 invalid RSNIE capabilities\s+:\s+(?P<dot11_invalid_rsnie_capabilities>\d+)\n+"
            # DOT11 received invalid PMKID in the received RSN IE             : 74
            r"\s+DOT11 received invalid PMKID in the received RSN IE\s+:\s+(?P<dot11_invalid_pkmid>\d+)\n+"
            # DOT11 invalid MDIE                                              : 0
            r"\s+DOT11 invalid MDIE\s+:\s+(?P<dot11_invalid_mdie>\d+)\n+"
            # DOT11 invalid FT IE                                             : 0
            r"\s+DOT11 invalid FT IE\s+:\s+(?P<dot11_invalid_ft_ie>\d+)\n+"
            # DOT11 QoS policy                                                : 0
            r"\s+DOT11 QoS policy\s+:\s+(?P<dot11_qos_policy>\d+)\n+"
            # DOT11 AP have insufficient bandwidth                            : 0
            r"\s+DOT11 AP have insufficient bandwidth\s+:\s+(?P<dot11_ap_insufficient_bandwidth>\d+)\n+"
            # DOT11 invalid QoS parameter                                     : 0
            r"\s+DOT11 invalid QoS parameter\s+:\s+(?P<dot11_invalid_qos_parameter>\d+)\n+"
            # Client not allowed by assisted roaming                          : 0
            r"\s+Client not allowed by assisted roaming\s+:\s+(?P<not_allowed_roaming>\d+)\n+"
            # IAPP disassociation for wired client                            : 0
            r"\s+IAPP disassociation for wired client\s+:\s+(?P<iapp_disassociate_wired>\d+)\n+"
            # Wired WGB change                                                : 0
            r"\s+Wired WGB change\s+:\s+(?P<wired_wgb_change>\d+)\n+"
            # Wired VLAN change                                               : 0
            r"\s+Wired VLAN change\s+:\s+(?P<wired_vlan_change>\d+)\n+"
            # Wired client deleted due to WGB delete                          : 0
            r"\s+Wired client deleted due to WGB delete\s+:\s+(?P<wired_wgb_delete>\d+)\n+"
            # AVC client re-anchored at the foreign controller                : 0
            r"\s+AVC client re-anchored at the foreign controller\s+:\s+(?P<avc_client_reanchor>\d+)\n+"
            # WGB Wired client joins as a direct wireless client              : 0
            r"\s+WGB Wired client joins as a direct wireless client\s+:\s+(?P<wired_wbg_joins>\d+)\n+"
            # AP upgrade                                                      : 0
            r"\s+AP upgrade\s+:\s+(?P<ap_upgrade>\d+)\n+"
            # Client DHCP                                                     : 0
            r"\s+Client DHCP\s+:\s+(?P<client_dhcp>\d+)\n+"
            # Client EAP timeout                                              : 0
            r"\s+Client EAP timeout\s+:\s+(?P<client_eap_timeout>\d+)\n+"
            # Client 8021x failure                                            : 0
            r"\s+Client 8021x failure\s+:\s+(?P<client_auth_8021x_fail>\d+)\n+"
            # Client device idle                                              : 0
            r"\s+Client device idle\s+:\s+(?P<client_device_idle>\d+)\n+"
            # Client captive portal security failure                          : 0
            r"\s+Client captive portal security failure\s+:\s+(?P<client_captive_portal_fail>\d+)\n+"
            # Client decryption failure                                       : 0
            r"\s+Client decryption failure \s+:\s+(?P<client_decrypt_fail>\d+)\n+"
            # Client interface disabled                                       : 0
            r"\s+Client interface disabled\s+:\s+(?P<client_int_disable>\d+)\n+"
            # Client user triggered disassociation                            : 0
            r"\s+Client user triggered disassociation\s+:\s+(?P<client_trigger_disassociate>\d+)\n+"
            # Client miscellaneous reason                                     : 0
            r"\s+Client miscellaneous reason\s+:\s+(?P<client_misc_reason>\d+)\n+"
            # Unknown                                                         : 0
            r"\s+Unknown\s+:\s+(?P<unknown>\d+)\n+"
            # Client peer triggered                                           : 0
            r"\s+Client peer triggered\s+:\s+(?P<client_peer_trigger>\d+)\n+"
            # Client beacon loss                                              : 0
            r"\s+Client beacon loss\s+:\s+(?P<client_beacon_loss>\d+)\n+"
            # Client EAP ID timeout                                           : 10928
            r"\s+Client EAP ID timeout\s+:\s+(?P<client_eap_id_timeout>\d+)\n+"
            # Client DOT1x timeout                                            : 0
            r"\s+Client DOT1x timeout\s+:\s+(?P<client_dot1x_timeout>\d+)\n+"
            # Malformed EAP key frame                                         : 0
            r"\s+Malformed EAP key frame\s+:\s+(?P<eap_bad_keyframe>\d+)\n+"
            # EAP key install bit is not expected                             : 0
            r"\s+EAP key install bit is not expected\s+:\s+(?P<eap_key_install_unexpected>\d+)\n+"
            # EAP key error bit is not expected                               : 0
            r"\s+EAP key error bit is not expected\s+:\s+(?P<eap_key_error_unexpected>\d+)\n+"
            # EAP key ACK bit is not expected                                 : 0
            r"\s+EAP key ACK bit is not expected\s+:\s+(?P<eap_key_ack_unexpected>\d+)\n+"
            # Invalid key type                                                : 0
            r"\s+Invalid key type\s+:\s+(?P<eap_invalid_key_type>\d+)\n+"
            # EAP key secure bit is not expected                              : 0
            r"\s+EAP key secure bit is not expected\s+:\s+(?P<eap_key_secure_unexected>\d+)\n+"
            # key description version mismatch                                : 0
            r"\s+key description version mismatch\s+:\s+(?P<eap_key_version_mismatch>\d+)\n+"
            # wrong replay counter                                            : 1
            r"\s+wrong replay counter\s+:\s+(?P<wrong_replay_counter>\d+)\n+"
            # EAP key MIC bit expected                                        : 0
            r"\s+EAP key MIC bit expected\s+:\s+(?P<eap_key_mic_expected>\d+)\n+"
            # MIC validation failed                                           : 7
            r"\s+MIC validation failed\s+:\s+(?P<eap_mic_validation_failed>\d+)\n+"
            # Error while PTK computation                                     : 0
            r"\s+Error while PTK computation\s+:\s+(?P<ptk_error>\d+)\n+"
            # Incorrect credentials                                           : 16
            r"\s+Incorrect credentials\s+:\s+(?P<bad_credentials>\d+)\n+"
            # Client connection lost                                          : 0
            r"\s+Client connection lost\s+:\s+(?P<client_connection_lost>\d+)\n+"
            # Reauthentication failure                                        : 0
            r"\s+Reauthentication failure\s+:\s+(?P<reauthentication_fail>\d+)\n+"
            # Port admin disabled                                             : 0
            r"\s+Port admin disabled\s+:\s+(?P<port_admin_disabled>\d+)\n+"
            # Supplicant restart                                              : 0
            r"\s+Supplicant restart\s+:\s+(?P<supplicant_restart>\d+)\n+"
            # No IP                                                           : 93
            r"\s+No IP\s+:\s+(?P<no_ip>\d+)\n+"
            # Call admission controller at anchor node                        : 0
            r"\s+Call admission controller at anchor node\s+:\s+(?P<anchor_call_admission_controller>\d+)\n+"
            # Anchor no memory                                                : 0
            r"\s+Anchor no memory\s+:\s+(?P<anchor_no_memory>\d+)\n+"
            # Anchor invalid Mobility BSSID                                   : 0
            r"\s+Anchor invalid Mobility BSSID\s+:\s+(?P<anchor_invalid_mobility_bssid>\d+)\n+"
            # Anchor creation failure                                         : 0
            r"\s+Anchor creation failure\s+:\s+(?P<anchor_create_fail>\d+)\n+"
            # DB error                                                        : 0
            r"\s+DB error\s+:\s+(?P<db_error>\d+)\n+"
            # Wired client cleanup due to WGB roaming                         : 0
            r"\s+Wired client cleanup due to WGB roaming\s+:\s+(?P<cleanup_wgb_roam>\d+)\n+"
            # Manually excluded                                               : 0
            r"\s+Manually excluded\s+:\s+(?P<manually_excluded>\d+)\n+"
            # 802.11 association failure                                      : 0
            r"\s+802.11 association failure\s+:\s+(?P<dot11_assocation_fail>\d+)\n+"
            # 802.11 authentication failure                                   : 0
            r"\s+802.11 authentication failure\s+:\s+(?P<dot11_auth_fail>\d+)\n+"
            # 802.1X authentication timeout                                   : 0
            r"\s+802.1X authentication timeout\s+:\s+(?P<dot11x_auth_timeout>\d+)\n+"
            # 802.1X authentication credential failure                        : 0
            r"\s+802.1X authentication credential failure\s+:\s+(?P<dot11x_credential_fail>\d+)\n+"
            # Web authentication failure                                      : 0
            r"\s+Web authentication failure\s+:\s+(?P<web_auth_fail>\d+)\n+"
            # Policy bind failure                                             : 0
            r"\s+Policy bind failure\s+:\s+(?P<policy_bind_fail>\d+)\n+"
            # IP theft                                                        : 0
            r"\s+IP theft\s+:\s+(?P<ip_theft>\d+)\n+"
            # MAC theft                                                       : 0
            r"\s+MAC theft\s+:\s+(?P<mac_theft>\d+)\n+"
            # MAC and IP theft                                                : 0
            r"\s+MAC and IP theft\s+:\s+(?P<mac_ip_theft>\d+)\n+"
            # QoS policy failure                                              : 0
            r"\s+QoS policy failure\s+:\s+(?P<qos_policy_fail>\d+)\n+"
            # QoS policy send to AP failure                                   : 0
            r"\s+QoS policy send to AP failure\s+:\s+(?P<qos_send_ap_fail>\d+)\n+"
            # QoS policy bind on AP failure                                   : 0
            r"\s+QoS policy bind on AP failure\s+:\s+(?P<qos_bind_ap_fail>\d+)\n+"
            # QoS policy unbind on AP failure                                 : 0
            r"\s+QoS policy unbind on AP failure\s+:\s+(?P<qos_unbind_ap_fail>\d+)\n+"
            # Static IP anchor discovery failure                              : 0
            r"\s+Static IP anchor discovery failure\s+:\s+(?P<anchor_static_ip_fail>\d+)\n+"
            # VLAN failure                                                    : 0
            r"\s+VLAN failure\s+:\s+(?P<vlan_fail>\d+)\n+"
            # ACL failure                                                     : 0
            r"\s+ACL failure\s+:\s+(?P<acl_fail>\d+)\n+"
            # Redirect ACL failure                                            : 2
            r"\s+Redirect ACL failure\s+:\s+(?P<redirect_acl_fail>\d+)\n+"
            # Accounting failure                                              : 0
            r"\s+Accounting failure\s+:\s+(?P<accounting_fail>\d+)\n+"
            # Security group tag failure                                      : 0
            r"\s+Security group tag failure\s+:\s+(?P<security_grouptag_fail>\d+)\n+"
            # FQDN filter definition does not exist                           : 0
            r"\s+FQDN filter definition does not exist\s+:\s+(?P<fqdn_filter_missing>\d+)\n+"
            # Wrong filter type, expected postauth FQDN filter                : 0
            r"\s+Wrong filter type, expected postauth FQDN filter\s+:\s+(?P<fqdn_wrong_postauth_filter>\d+)\n+"
            # Wrong filter type, expected preauth FQDN filter                 : 0
            r"\s+Wrong filter type, expected preauth FQDN filter\s+:\s+(?P<fqdn_wrong_preauth_filter>\d+)\n+"
            # Invalid group id for FQDN filter valid range  1..16             : 0
            r"\s+Invalid group id for FQDN filter valid range  1..16\s+:\s+(?P<fqdn_invalid_group_id>\d+)\n+" #HEY
            # Policy parameter mismatch                                       : 0
            r"\s+Policy parameter mismatch\s+:\s+(?P<policy_manager_mismatch>\d+)\n+"
            # Reauth failure                                                  : 0
            r"\s+Reauth failure\s+:\s+(?P<reauth_fail>\d+)\n+"
            # Wrong PSK                                                       : 0
            r"\s+Wrong PSK\s+:\s+(?P<wrong_psk>\d+)\n+"
            # Policy failure                                                  : 0
            r"\s+Policy failure\s+:\s+(?P<policy_fail>\d+)\n+"
            # AP initiated delete for idle timeout                            : 164
            r"\s+AP initiated delete for idle timeout\s+:\s+(?P<apinit_idle_timeout>\d+)\n+"
            # AP initiated delete for client ACL mismatch                     : 0
            r"\s+AP initiated delete for client ACL mismatch\s+:\s+(?P<apinit_acl_mismatch>\d+)\n+"
            # AP initiated delete for AP auth stop                            : 0
            r"\s+AP initiated delete for AP auth stop\s+:\s+(?P<apinit_auth_stop>\d+)\n+"
            # AP initiated delete for association expired at AP               : 0
            r"\s+AP initiated delete for association expired at AP\s+:\s+(?P<apinit_association_expired>\d+)\n+"
            # AP initiated delete for 4-way handshake failed                  : 0
            r"\s+AP initiated delete for 4-way handshake failed\s+:\s+(?P<apinit_4way_fail>\d+)\n+"
            # AP initiated delete for DHCP timeout                            : 0
            r"\s+AP initiated delete for DHCP timeout\s+:\s+(?P<apinit_dhcp_timeout>\d+)\n+"
            # AP initiated delete for reassociation timeout                   : 0
            r"\s+AP initiated delete for reassociation timeout\s+:\s+(?P<apinit_reassocation_timeout>\d+)\n+"
            # AP initiated delete for SA query timeout                        : 0
            r"\s+AP initiated delete for SA query timeout\s+:\s+(?P<apinit_sa_timeout>\d+)\n+"
            # AP initiated delete for channel switch at AP                    : 0
            r"\s+AP initiated delete for channel switch at AP\s+:\s+(?P<apinit_channel_switch>\d+)\n+"
            # AP initiated delete for bad AID                                 : 0
            r"\s+AP initiated delete for bad AID\s+:\s+(?P<apinit_bad_aid>\d+)\n+"
            # AP initiated delete for request                                 : 0
            r"\s+AP initiated delete for request\s+:\s+(?P<apinit_request>\d+)\n+"
            # AP initiated delete for interface reset                         : 0
            r"\s+AP initiated delete for interface reset\s+:\s+(?P<apinit_interface_reset>\d+)\n+"
            # AP initiated delete for all on slot                             : 0
            r"\s+AP initiated delete for all on slot\s+:\s+(?P<apinit_all_slot>\d+)\n+"
            # AP initiated delete for reaper radio                            : 0
            r"\s+AP initiated delete for reaper radio\s+:\s+(?P<apinit_reaper_radio>\d+)\n+"
            # AP initiated delete for slot disable                            : 0
            r"\s+AP initiated delete for slot disable\s+:\s+(?P<apinit_slot_disable>\d+)\n+"
            # AP initiated delete for MIC failure                             : 0
            r"\s+AP initiated delete for MIC failure\s+:\s+(?P<apinit_mic_fail>\d+)\n+"
            # AP initiated delete for VLAN delete                             : 0
            r"\s+AP initiated delete for VLAN delete\s+:\s+(?P<apinit_vlan_delete>\d+)\n+"
            # AP initiated delete for channel change                          : 0
            r"\s+AP initiated delete for channel change\s+:\s+(?P<apinit_channel_change>\d+)\n+"
            # AP initiated delete for stop reassociation                      : 0
            r"\s+AP initiated delete for stop reassociation\s+:\s+(?P<apinit_stop_reassociation>\d+)\n+"
            # AP initiated delete for packet max retry                        : 0
            r"\s+AP initiated delete for packet max retry\s+:\s+(?P<apinit_max_retry>\d+)\n+"
            # AP initiated delete for transmission deauth                     : 0
            r"\s+AP initiated delete for transmission deauth\s+:\s+(?P<apinit_transmission_deauth>\d+)\n+"
            # AP initiated delete for sensor station timeout                  : 0
            r"\s+AP initiated delete for sensor station timeout\s+:\s+(?P<apinit_sensor_station_timeout>\d+)\n+"
            # AP initiated delete for age timeout                             : 0
            r"\s+AP initiated delete for age timeout\s+:\s+(?P<apinit_age_timeout>\d+)\n+"
            # AP initiated delete for transmission fail threshold             : 0
            r"\s+AP initiated delete for transmission fail threshold\s+:\s+(?P<apinit_transmission_fail_threshold>\d+)\n+"
            # AP initiated delete for uplink receive timeout                  : 0
            r"\s+AP initiated delete for uplink receive timeout\s+:\s+(?P<apinit_uplink_recieve_timeout>\d+)\n+"
            # AP initiated delete for sensor scan next radio                  : 0
            r"\s+AP initiated delete for sensor scan next radio\s+:\s+(?P<apinit_scan_next_radio>\d+)\n+"
            # AP initiated delete for sensor scan other BSSID                 : 0
            r"\s+AP initiated delete for sensor scan other BSSID\s+:\s+(?P<apinit_scan_other_bssid>\d+)\n+"
            # AAA server unavailable                                          : 0
            r"\s+AAA server unavailable\s+:\s+(?P<aaa_unavailable>\d+)\n+"
            # AAA server not ready                                            : 0
            r"\s+AAA server not ready\s+:\s+(?P<aaa_not_ready>\d+)\n+"
            # No dot1x method configuration                                   : 0
            r"\s+No dot1x method configuration\s+:\s+(?P<dot1x_no_config>\d+)\n+"
            # Client Abort                                                    : 0
            r"\s+Client Abort\s+:\s+(?P<client_abort>\d+)\n+"
            # Association connection timeout                                  : 0
            r"\s+Association connection timeout\s+:\s+(?P<connection_timeout_assocation>\d+)\n+"
            # MAC-AUTH connection timeout                                     : 0
            r"\s+MAC-AUTH connection timeout\s+:\s+(?P<connection_timeout_macauth>\d+)\n+"
            # L2-AUTH connection timeout                                      : 882
            r"\s+L2-AUTH connection timeout\s+:\s+(?P<connection_timeout_l2auth>\d+)\n+"
            # L3-AUTH connection timeout                                      : 0
            r"\s+L3-AUTH connection timeout\s+:\s+(?P<connection_timeout_l3auth>\d+)\n+"
            # Mobility connection timeout                                     : 0
            r"\s+Mobility connection timeout\s+:\s+(?P<connection_timeout_mobility>\d+)\n+"
            # static IP connection timeout                                    : 0
            r"\s+static IP connection timeout\s+:\s+(?P<connection_timeout_static_ip>\d+)\n+"
            # SM session creation timeout                                     : 0
            r"\s+SM session creation timeout\s+:\s+(?P<connection_timeout_sm_session_creation>\d+)\n+"
            # IP-LEARN connection timeout                                     : 25
            r"\s+IP-LEARN connection timeout\s+:\s+(?P<connection_timeout_iplearn>\d+)\n+"
            # NACK IFID exists                                                : 0
            r"\s+NACK IFID exists\s+:\s+(?P<nack_ifid_exists>\d+)\n+"
            # Radio Down                                                      : 0
            r"\s+Radio Down\s+:\s+(?P<radio_down>\d+)\n+"
            # EoGRE Reset                                                     : 0
            r"\s+EoGRE Reset\s+:\s+(?P<eogre_reset>\d+)\n+"
            # EoGRE Generic Join Failure                                      : 0
            r"\s+EoGRE Generic Join Failure\s+:\s+(?P<eogre_generic_join_fail>\d+)\n+"
            # EoGRE HA-Reconciliation                                         : 0
            r"\s+EoGRE HA-Reconciliation\s+:\s+(?P<eogre_ha_reconcile>\d+)\n+"
            # EoGRE Invalid VLAN                                              : 0
            r"\s+EoGRE Invalid VLAN\s+:\s+(?P<eogre_invalid_vlan>\d+)\n+"
            # EoGRE Invalid Domain                                            : 0
            r"\s+EoGRE Invalid Domain\s+:\s+(?P<eogre_invalid_domain>\d+)\n+"
            # EoGRE Empty Domain                                              : 0
            r"\s+EoGRE Empty Domain\s+:\s+(?P<eogre_empty_domain>\d+)\n+"
            # EoGRE Domain Shut                                               : 0
            r"\s+EoGRE Domain Shut\s+:\s+(?P<eogre_domain_shut>\d+)\n+"
            # EoGRE Invalid Gateway                                           : 0
            r"\s+EoGRE Invalid Gateway\s+:\s+(?P<eogre_invalid_gateway>\d+)\n+"
            # EoGRE All Gateways down                                         : 0
            r"\s+EoGRE All Gateways down\s+:\s+(?P<eogre_all_gateways_down>\d+)\n+"
            # EoGRE Flex - no active gateway                                  : 0
            r"\s+EoGRE Flex - no active gateway\s+:\s+(?P<eogre_flex_no_gateway>\d+)\n+"
            # EoGRE Rule Matching error                                       : 0
            r"\s+EoGRE Rule Matching error\s+:\s+(?P<eogre_rule_error>\d+)\n+"
            # EoGRE AAA Override error                                        : 0
            r"\s+EoGRE AAA Override error\s+:\s+(?P<eogre_aaa_override_error>\d+)\n+"
            # EoGRE client onboarding error                                   : 0
            r"\s+EoGRE client onboarding error\s+:\s+(?P<eogre_onboarding_error>\d+)\n+"
            # EoGRE Mobility Handoff error                                    : 0
            r"\s+EoGRE Mobility Handoff error\s+:\s+(?P<eogre_mobility_handoff_error>\d+)\n+"
            # IP Update timeout                                               : 0
            r"\s+IP Update timeout\s+:\s+(?P<ip_update_timeout>\d+)\n+"
            # L3 VLAN Override connection timeout                         : 0
            r"\s+L3 VLAN Override connection timeout\s+:\s+(?P<connection_timeout_l3vlan_override>\d+)\n+"
            # Mobility peer delete                                            : 0
            r"\s+Mobility peer delete\s+:\s+(?P<mobility_peer_delete>\d+)\n+"
            # NACK IFID mismatch                                              : 0
            r"\s+NACK IFID mismatch\s+:\s+(?P<nack_ifid_mismatch>\d+)\n+"
        )

        wlan_obj = {}

        if re.search(wlan_capture, out, re.MULTILINE):
            search = re.search(wlan_capture, out, re.MULTILINE)
            group = search.groupdict()

            # convert str to int
            group["id"] = int(group["id"])

            new_group = {"wlan": group}
            wlan_obj.update(new_group)

        if re.search(client_stats_capture, out, re.MULTILINE):
            search = re.search(client_stats_capture, out, re.MULTILINE)
            group = search.groupdict()

            for item in group:
                # convert str to int
                group[item] = int(group[item])

            new_group = {"client_stats": group}
            wlan_obj.update(new_group)

        if re.search(client_delete_capture, out, re.MULTILINE):
            search = re.search(client_delete_capture, out, re.MULTILINE)
            group = search.groupdict()

            for item in group:
                # convert str to int
                group[item] = int(group[item])

            new_group = {"client_delete": group}

            key_list = [
                "anchor",
                "apinit",
                "client",
                "connection_timeout",
                "dot11",
                "dot11v",
                "eap",
                "eogre",
                "fqdn",
                "mac",
                "mobility",
                "policy",
                "qos",
                "wired",
            ]

            for key in key_list:
                new_key_group = {key: {}}

                for item in new_group["client_delete"].copy():
                    # if the key from key_list is found in item
                    if re.search(f"^{key}_", item):
                        # replace the key and update with new_dict
                        new_key = re.sub(f"^{key}_", "", item)
                        new_dict = {new_key: new_group["client_delete"][item]}

                        new_key_group[key].update(new_dict)
                        new_group["client_delete"].pop(item)

                new_group["client_delete"].update(new_key_group)

            wlan_obj.update(new_group)

        return wlan_obj
