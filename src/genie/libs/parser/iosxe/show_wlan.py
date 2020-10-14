import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


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

    def cli(self, id_number="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        else:
            output = output

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
            # Wlan Profile Name: lizzard_Global, Wlan Id: int
            r"^Wlan Profile Name:\s+(?P<profile_name>\S+), Wlan Id: (?P<id>\d+)$"
        )

        # Current client state statistics:
        client_stats_capture = (
            r"^"
            #   Authenticating         : int
            r"\s+Authenticating\s+:\s+(?P<auth>\d+)\s+"
            #   Mobility               : int
            r"\s+Mobility\s+:\s+(?P<mobility>\d+)\s+"
            #   IP Learn               : int
            r"\s+IP Learn\s+:\s+(?P<ip_learn>\d+)\s+"
            #   Webauth Pending        : int
            r"\s+Webauth Pending\s+:\s+(?P<webauth>\d+)\s+"
            #   Run                    : int
            r"\s+Run\s+:\s+(?P<run>\d+)\s+"
        )

        # Total client delete reasons
        client_delete_capture = (
            r"^"
            # No Operation                                                    : int
            r"\s+No Operation\s+:\s+(?P<no_operation>\d+)\s+"
            # Internal error                                                  : int
            r"\s+Internal error\s+:\s+(?P<internal_error>\d+)\s+"
            # Deauthentication or disassociation request                      : int
            r"\s+Deauthentication or disassociation request\s+:\s+(?P<deauth_request>\d+)\s+"
            # Session Manager                                                 : int
            r"\s+Session Manager\s+:\s+(?P<session_manager>\d+)\s+"
            # L3 authentication failure                                       : int
            r"\s+L3 authentication failure\s+:\s+(?P<l3_auth_fail>\d+)\s+"
            # Delete received from AP                                         : int
            r"\s+Delete received from AP\s+:\s+(?P<delete_from_ap>\d+)\s+"
            # BSSID down                                                      : int
            r"\s+BSSID down\s+:\s+(?P<bssid_down>\d+)\s+"
            # AP down/disjoin                                                 : int
            r"\s+AP down/disjoin\s+:\s+(?P<ap_down>\d+)\s+"
            # Connection timeout                                              : int
            r"\s+Connection timeout\s+:\s+(?P<connection_timeout>\d+)\s+"
            # MAC authentication failure                                      : int
            r"\s+MAC authentication failure\s+:\s+(?P<mac_auth_fail>\d+)\s+"
            # Datapath plumb                                                  : int
            r"\s+Datapath plumb\s+:\s+(?P<datapath_plumb>\d+)\s+"
            # Due to SSID change                                              : int
            r"\s+Due to SSID change\s+:\s+(?P<ssid_change>\d+)\s+"
            # Due to VLAN change                                              : int
            r"\s+Due to VLAN change\s+:\s+(?P<vlan_change>\d+)\s+"
            # Due to IP Zone change                                              : int
            r"\s+Due to IP Zone change\s+:\s+(?P<ip_zone_change>\d+)\s+"
            # Admin deauthentication                                          : int
            r"\s+Admin deauthentication\s+:\s+(?P<admin_deauth>\d+)\s+"
            # QoS failure                                                     : int
            r"\s+QoS failure\s+:\s+(?P<qos_fail>\d+)\s+"
            # WPA key exchange timeout                                        : int
            r"\s+WPA key exchange timeout\s+:\s+(?P<wpa_key_timeout>\d+)\s+"
            # WPA group key update timeout                                    : int
            r"\s+WPA group key update timeout\s+:\s+(?P<wpa_groupkey_timeout>\d+)\s+"
            # 802.11w MAX SA queries reached                                  : int
            r"\s+802.11w MAX SA queries reached\s+:\s+(?P<dot11w_max_sa>\d+)\s+"
            # Client deleted during HA recovery                               : int
            r"\s+Client deleted during HA recovery\s+:\s+(?P<ha_recovery>\d+)\s+"
            # Client blacklist                                                : int
            r"\s+Client blacklist\s+:\s+(?P<blacklist>\d+)\s+"
            # Inter instance roam failure                                     : int
            r"\s+Inter instance roam failure\s+:\s+(?P<roam_fail>\d+)\s+"
            # Due to mobility failure                                         : int
            r"\s+Due to mobility failure\s+:\s+(?P<mobility_fail>\d+)\s+"
            # Session timeout                                                 : int
            r"\s+Session timeout\s+:\s+(?P<session_timeout>\d+)\s+"
            # Idle timeout                                                    : int
            r"\s+Idle timeout\s+:\s+(?P<idle_timeout>\d+)\s+"
            # Supplicant request                                              : int
            r"\s+Supplicant request\s+:\s+(?P<supplicant_request>\d+)\s+"
            # NAS error                                                       : int
            r"\s+NAS error\s+:\s+(?P<nas_error>\d+)\s+"
            # Policy Manager internal error                                   : int
            r"\s+Policy Manager internal error\s+:\s+(?P<policy_manager_error>\d+)\s+"
            # Mobility WLAN down                                              : int
            r"\s+Mobility WLAN down\s+:\s+(?P<mobility_wlan_down>\d+)\s+"
            # Mobility tunnel down                                            : int
            r"\s+Mobility tunnel down\s+:\s+(?P<mobility_tunnel_down>\d+)\s+"
            # 80211v smart roam failed                                        : int
            r"\s+80211v smart roam failed\s+:\s+(?P<dot11v_smart_roam_fail>\d+)\s+"
            # DOT11v timer timeout                                            : int
            r"\s+DOT11v timer timeout\s+:\s+(?P<dot11v_timer_timeout>\d+)\s+"
            # DOT11v association failed                                       : int
            r"\s+DOT11v association failed \s+:\s+(?P<dot11v_association_fail>\d+)\s+"
            # DOT11r pre-authentication failure                               : int
            r"\s+DOT11r pre-authentication failure\s+:\s+(?P<dot11v_preauth_fail>\d+)\s+"
            # SAE authentication failure                                      : int
            r"\s+SAE authentication failure\s+:\s+(?P<dot11_sae_auth_fail>\d+)\s+"
            # DOT11 failure                                                   : int
            r"\s+DOT11 failure \s+:\s+(?P<dot11_fail>\d+)\s+"
            # DOT11 SAE invalid message                                       : int
            r"\s+DOT11 SAE invalid message\s+:\s+(?P<dot11_sae_invalid>\d+)\s+"
            # DOT11 unsupported client capabilities                           : int
            r"\s+DOT11 unsupported client capabilities\s+:\s+(?P<dot11_unsupported_client>\d+)\s+"
            # DOT11 association denied unspecified                            : int
            r"\s+DOT11 association denied unspecified\s+:\s+(?P<dot11_denied_unspecified>\d+)\s+"
            # DOT11 max STA                                                   : int
            r"\s+DOT11 max STA\s+:\s+(?P<dot11_max_sta>\d+)\s+"
            # DOT11 denied data rates                                         : int
            r"\s+DOT11 denied data rates\s+:\s+(?P<dot11_denied_data_rates>\d+)\s+"
            # 802.11v Client RSSI lower than the association RSSI threshold   : int
            r"\s+802.11v Client RSSI lower than the association RSSI threshold\s+:\s+(?P<dot11v_rssi_low_threshold>\d+)\s+"
            # invalid QoS parameter                                           : int
            r"\s+invalid QoS parameter\s+:\s+(?P<qos_invalid_parameter>\d+)\s+"
            # DOT11 IE validation failed                                      : int
            r"\s+DOT11 IE validation failed\s+:\s+(?P<dot11_ie_validation_failed>\d+)\s+"
            # DOT11 group cipher in IE validation failed                      : int
            r"\s+DOT11 group cipher in IE validation failed\s+:\s+(?P<dot11_groupcipher_validation_failed>\d+)\s+"
            # DOT11 invalid pairwise cipher                                   : int
            r"\s+DOT11 invalid pairwise cipher\s+:\s+(?P<dot11_invalid_pairwise_cipher>\d+)\s+"
            # DOT11 invalid AKM                                               : int
            r"\s+DOT11 invalid AKM \s+:\s+(?P<dot11_invalid_akm>\d+)\s+"
            # DOT11 unsupported RSN version                                   : int
            r"\s+DOT11 unsupported RSN version\s+:\s+(?P<dot11_unsupported_rsn_version>\d+)\s+"
            # DOT11 invalid RSNIE capabilities                                : int
            r"\s+DOT11 invalid RSNIE capabilities\s+:\s+(?P<dot11_invalid_rsnie_capabilities>\d+)\s+"
            # DOT11 received invalid PMKID in the received RSN IE             : int
            r"\s+DOT11 received invalid PMKID in the received RSN IE\s+:\s+(?P<dot11_invalid_pkmid>\d+)\s+"
            # DOT11 invalid MDIE                                              : int
            r"\s+DOT11 invalid MDIE\s+:\s+(?P<dot11_invalid_mdie>\d+)\s+"
            # DOT11 invalid FT IE                                             : int
            r"\s+DOT11 invalid FT IE\s+:\s+(?P<dot11_invalid_ft_ie>\d+)\s+"
            # DOT11 QoS policy                                                : int
            r"\s+DOT11 QoS policy\s+:\s+(?P<dot11_qos_policy>\d+)\s+"
            # DOT11 AP have insufficient bandwidth                            : int
            r"\s+DOT11 AP have insufficient bandwidth\s+:\s+(?P<dot11_ap_insufficient_bandwidth>\d+)\s+"
            # DOT11 invalid QoS parameter                                     : int
            r"\s+DOT11 invalid QoS parameter\s+:\s+(?P<dot11_invalid_qos_parameter>\d+)\s+"
            # Client not allowed by assisted roaming                          : int
            r"\s+Client not allowed by assisted roaming\s+:\s+(?P<not_allowed_roaming>\d+)\s+"
            # IAPP disassociation for wired client                            : int
            r"\s+IAPP disassociation for wired client\s+:\s+(?P<iapp_disassociate_wired>\d+)\s+"
            # Wired WGB change                                                : int
            r"\s+Wired WGB change\s+:\s+(?P<wired_wgb_change>\d+)\s+"
            # Wired VLAN change                                               : int
            r"\s+Wired VLAN change\s+:\s+(?P<wired_vlan_change>\d+)\s+"
            # Wired client deleted due to WGB delete                          : int
            r"\s+Wired client deleted due to WGB delete\s+:\s+(?P<wired_wgb_delete>\d+)\s+"
            # AVC client re-anchored at the foreign controller                : int
            r"\s+AVC client re-anchored at the foreign controller\s+:\s+(?P<avc_client_reanchor>\d+)\s+"
            # WGB Wired client joins as a direct wireless client              : int
            r"\s+WGB Wired client joins as a direct wireless client\s+:\s+(?P<wired_wbg_joins>\d+)\s+"
            # AP upgrade                                                      : int
            r"\s+AP upgrade\s+:\s+(?P<ap_upgrade>\d+)\s+"
            # Client DHCP                                                     : int
            r"\s+Client DHCP\s+:\s+(?P<client_dhcp>\d+)\s+"
            # Client EAP timeout                                              : int
            r"\s+Client EAP timeout\s+:\s+(?P<client_eap_timeout>\d+)\s+"
            # Client 8021x failure                                            : int
            r"\s+Client 8021x failure\s+:\s+(?P<client_auth_8021x_fail>\d+)\s+"
            # Client device idle                                              : int
            r"\s+Client device idle\s+:\s+(?P<client_device_idle>\d+)\s+"
            # Client captive portal security failure                          : int
            r"\s+Client captive portal security failure\s+:\s+(?P<client_captive_portal_fail>\d+)\s+"
            # Client decryption failure                                       : int
            r"\s+Client decryption failure \s+:\s+(?P<client_decrypt_fail>\d+)\s+"
            # Client interface disabled                                       : int
            r"\s+Client interface disabled\s+:\s+(?P<client_int_disable>\d+)\s+"
            # Client user triggered disassociation                            : int
            r"\s+Client user triggered disassociation\s+:\s+(?P<client_trigger_disassociate>\d+)\s+"
            # Client miscellaneous reason                                     : int
            r"\s+Client miscellaneous reason\s+:\s+(?P<client_misc_reason>\d+)\s+"
            # Unknown                                                         : int
            r"\s+Unknown\s+:\s+(?P<unknown>\d+)\s+"
            # Client peer triggered                                           : int
            r"\s+Client peer triggered\s+:\s+(?P<client_peer_trigger>\d+)\s+"
            # Client beacon loss                                              : int
            r"\s+Client beacon loss\s+:\s+(?P<client_beacon_loss>\d+)\s+"
            # Client EAP ID timeout                                           : int
            r"\s+Client EAP ID timeout\s+:\s+(?P<client_eap_id_timeout>\d+)\s+"
            # Client DOT1x timeout                                            : int
            r"\s+Client DOT1x timeout\s+:\s+(?P<client_dot1x_timeout>\d+)\s+"
            # Malformed EAP key frame                                         : int
            r"\s+Malformed EAP key frame\s+:\s+(?P<eap_bad_keyframe>\d+)\s+"
            # EAP key install bit is not expected                             : int
            r"\s+EAP key install bit is not expected\s+:\s+(?P<eap_key_install_unexpected>\d+)\s+"
            # EAP key error bit is not expected                               : int
            r"\s+EAP key error bit is not expected\s+:\s+(?P<eap_key_error_unexpected>\d+)\s+"
            # EAP key ACK bit is not expected                                 : int
            r"\s+EAP key ACK bit is not expected\s+:\s+(?P<eap_key_ack_unexpected>\d+)\s+"
            # Invalid key type                                                : int
            r"\s+Invalid key type\s+:\s+(?P<eap_invalid_key_type>\d+)\s+"
            # EAP key secure bit is not expected                              : int
            r"\s+EAP key secure bit is not expected\s+:\s+(?P<eap_key_secure_unexected>\d+)\s+"
            # key description version mismatch                                : int
            r"\s+key description version mismatch\s+:\s+(?P<eap_key_version_mismatch>\d+)\s+"
            # wrong replay counter                                            : int
            r"\s+wrong replay counter\s+:\s+(?P<wrong_replay_counter>\d+)\s+"
            # EAP key MIC bit expected                                        : int
            r"\s+EAP key MIC bit expected\s+:\s+(?P<eap_key_mic_expected>\d+)\s+"
            # MIC validation failed                                           : int
            r"\s+MIC validation failed\s+:\s+(?P<eap_mic_validation_failed>\d+)\s+"
            # Error while PTK computation                                     : int
            r"\s+Error while PTK computation\s+:\s+(?P<ptk_error>\d+)\s+"
            # Incorrect credentials                                           : int
            r"\s+Incorrect credentials\s+:\s+(?P<bad_credentials>\d+)\s+"
            # Client connection lost                                          : int
            r"\s+Client connection lost\s+:\s+(?P<client_connection_lost>\d+)\s+"
            # Reauthentication failure                                        : int
            r"\s+Reauthentication failure\s+:\s+(?P<reauthentication_fail>\d+)\s+"
            # Port admin disabled                                             : int
            r"\s+Port admin disabled\s+:\s+(?P<port_admin_disabled>\d+)\s+"
            # Supplicant restart                                              : int
            r"\s+Supplicant restart\s+:\s+(?P<supplicant_restart>\d+)\s+"
            # No IP                                                           : int
            r"\s+No IP\s+:\s+(?P<no_ip>\d+)\s+"
            # Call admission controller at anchor node                        : int
            r"\s+Call admission controller at anchor node\s+:\s+(?P<anchor_call_admission_controller>\d+)\s+"
            # Anchor no memory                                                : int
            r"\s+Anchor no memory\s+:\s+(?P<anchor_no_memory>\d+)\s+"
            # Anchor invalid Mobility BSSID                                   : int
            r"\s+Anchor invalid Mobility BSSID\s+:\s+(?P<anchor_invalid_mobility_bssid>\d+)\s+"
            # Anchor creation failure                                         : int
            r"\s+Anchor creation failure\s+:\s+(?P<anchor_create_fail>\d+)\s+"
            # DB error                                                        : int
            r"\s+DB error\s+:\s+(?P<db_error>\d+)\s+"
            # Wired client cleanup due to WGB roaming                         : int
            r"\s+Wired client cleanup due to WGB roaming\s+:\s+(?P<cleanup_wgb_roam>\d+)\s+"
            # Manually excluded                                               : int
            r"\s+Manually excluded\s+:\s+(?P<manually_excluded>\d+)\s+"
            # 802.11 association failure                                      : int
            r"\s+802.11 association failure\s+:\s+(?P<dot11_assocation_fail>\d+)\s+"
            # 802.11 authentication failure                                   : int
            r"\s+802.11 authentication failure\s+:\s+(?P<dot11_auth_fail>\d+)\s+"
            # 802.1X authentication timeout                                   : int
            r"\s+802.1X authentication timeout\s+:\s+(?P<dot11x_auth_timeout>\d+)\s+"
            # 802.1X authentication credential failure                        : int
            r"\s+802.1X authentication credential failure\s+:\s+(?P<dot11x_credential_fail>\d+)\s+"
            # Web authentication failure                                      : int
            r"\s+Web authentication failure\s+:\s+(?P<web_auth_fail>\d+)\s+"
            # Policy bind failure                                             : int
            r"\s+Policy bind failure\s+:\s+(?P<policy_bind_fail>\d+)\s+"
            # IP theft                                                        : int
            r"\s+IP theft\s+:\s+(?P<ip_theft>\d+)\s+"
            # MAC theft                                                       : int
            r"\s+MAC theft\s+:\s+(?P<mac_theft>\d+)\s+"
            # MAC and IP theft                                                : int
            r"\s+MAC and IP theft\s+:\s+(?P<mac_ip_theft>\d+)\s+"
            # QoS policy failure                                              : int
            r"\s+QoS policy failure\s+:\s+(?P<qos_policy_fail>\d+)\s+"
            # QoS policy send to AP failure                                   : int
            r"\s+QoS policy send to AP failure\s+:\s+(?P<qos_send_ap_fail>\d+)\s+"
            # QoS policy bind on AP failure                                   : int
            r"\s+QoS policy bind on AP failure\s+:\s+(?P<qos_bind_ap_fail>\d+)\s+"
            # QoS policy unbind on AP failure                                 : int
            r"\s+QoS policy unbind on AP failure\s+:\s+(?P<qos_unbind_ap_fail>\d+)\s+"
            # Static IP anchor discovery failure                              : int
            r"\s+Static IP anchor discovery failure\s+:\s+(?P<anchor_static_ip_fail>\d+)\s+"
            # VLAN failure                                                    : int
            r"\s+VLAN failure\s+:\s+(?P<vlan_fail>\d+)\s+"
            # ACL failure                                                     : int
            r"\s+ACL failure\s+:\s+(?P<acl_fail>\d+)\s+"
            # Redirect ACL failure                                            : int
            r"\s+Redirect ACL failure\s+:\s+(?P<redirect_acl_fail>\d+)\s+"
            # Accounting failure                                              : int
            r"\s+Accounting failure\s+:\s+(?P<accounting_fail>\d+)\s+"
            # Security group tag failure                                      : int
            r"\s+Security group tag failure\s+:\s+(?P<security_grouptag_fail>\d+)\s+"
            # FQDN filter definition does not exist                           : int
            r"\s+FQDN filter definition does not exist\s+:\s+(?P<fqdn_filter_missing>\d+)\s+"
            # Wrong filter type, expected postauth FQDN filter                : int
            r"\s+Wrong filter type, expected postauth FQDN filter\s+:\s+(?P<fqdn_wrong_postauth_filter>\d+)\s+"
            # Wrong filter type, expected preauth FQDN filter                 : int
            r"\s+Wrong filter type, expected preauth FQDN filter\s+:\s+(?P<fqdn_wrong_preauth_filter>\d+)\s+"
            # Invalid group id for FQDN filter valid range  1..16             : int
            r"\s+Invalid group id for FQDN filter valid range  1..16\s+:\s+(?P<fqdn_invalid_group_id>\d+)\s+"
            # Policy parameter mismatch                                       : int
            r"\s+Policy parameter mismatch\s+:\s+(?P<policy_manager_mismatch>\d+)\s+"
            # Reauth failure                                                  : int
            r"\s+Reauth failure\s+:\s+(?P<reauth_fail>\d+)\s+"
            # Wrong PSK                                                       : int
            r"\s+Wrong PSK\s+:\s+(?P<wrong_psk>\d+)\s+"
            # Policy failure                                                  : int
            r"\s+Policy failure\s+:\s+(?P<policy_fail>\d+)\s+"
            # AP initiated delete for idle timeout                            : int
            r"\s+AP initiated delete for idle timeout\s+:\s+(?P<apinit_idle_timeout>\d+)\s+"
            # AP initiated delete for client ACL mismatch                     : int
            r"\s+AP initiated delete for client ACL mismatch\s+:\s+(?P<apinit_acl_mismatch>\d+)\s+"
            # AP initiated delete for AP auth stop                            : int
            r"\s+AP initiated delete for AP auth stop\s+:\s+(?P<apinit_auth_stop>\d+)\s+"
            # AP initiated delete for association expired at AP               : int
            r"\s+AP initiated delete for association expired at AP\s+:\s+(?P<apinit_association_expired>\d+)\s+"
            # AP initiated delete for 4-way handshake failed                  : int
            r"\s+AP initiated delete for 4-way handshake failed\s+:\s+(?P<apinit_4way_fail>\d+)\s+"
            # AP initiated delete for DHCP timeout                            : int
            r"\s+AP initiated delete for DHCP timeout\s+:\s+(?P<apinit_dhcp_timeout>\d+)\s+"
            # AP initiated delete for reassociation timeout                   : int
            r"\s+AP initiated delete for reassociation timeout\s+:\s+(?P<apinit_reassocation_timeout>\d+)\s+"
            # AP initiated delete for SA query timeout                        : int
            r"\s+AP initiated delete for SA query timeout\s+:\s+(?P<apinit_sa_timeout>\d+)\s+"
            # AP initiated delete for channel switch at AP                    : int
            r"\s+AP initiated delete for channel switch at AP\s+:\s+(?P<apinit_channel_switch>\d+)\s+"
            # AP initiated delete for bad AID                                 : int
            r"\s+AP initiated delete for bad AID\s+:\s+(?P<apinit_bad_aid>\d+)\s+"
            # AP initiated delete for request                                 : int
            r"\s+AP initiated delete for request\s+:\s+(?P<apinit_request>\d+)\s+"
            # AP initiated delete for interface reset                         : int
            r"\s+AP initiated delete for interface reset\s+:\s+(?P<apinit_interface_reset>\d+)\s+"
            # AP initiated delete for all on slot                             : int
            r"\s+AP initiated delete for all on slot\s+:\s+(?P<apinit_all_slot>\d+)\s+"
            # AP initiated delete for reaper radio                            : int
            r"\s+AP initiated delete for reaper radio\s+:\s+(?P<apinit_reaper_radio>\d+)\s+"
            # AP initiated delete for slot disable                            : int
            r"\s+AP initiated delete for slot disable\s+:\s+(?P<apinit_slot_disable>\d+)\s+"
            # AP initiated delete for MIC failure                             : int
            r"\s+AP initiated delete for MIC failure\s+:\s+(?P<apinit_mic_fail>\d+)\s+"
            # AP initiated delete for VLAN delete                             : int
            r"\s+AP initiated delete for VLAN delete\s+:\s+(?P<apinit_vlan_delete>\d+)\s+"
            # AP initiated delete for channel change                          : int
            r"\s+AP initiated delete for channel change\s+:\s+(?P<apinit_channel_change>\d+)\s+"
            # AP initiated delete for stop reassociation                      : int
            r"\s+AP initiated delete for stop reassociation\s+:\s+(?P<apinit_stop_reassociation>\d+)\s+"
            # AP initiated delete for packet max retry                        : int
            r"\s+AP initiated delete for packet max retry\s+:\s+(?P<apinit_max_retry>\d+)\s+"
            # AP initiated delete for transmission deauth                     : int
            r"\s+AP initiated delete for transmission deauth\s+:\s+(?P<apinit_transmission_deauth>\d+)\s+"
            # AP initiated delete for sensor station timeout                  : int
            r"\s+AP initiated delete for sensor station timeout\s+:\s+(?P<apinit_sensor_station_timeout>\d+)\s+"
            # AP initiated delete for age timeout                             : int
            r"\s+AP initiated delete for age timeout\s+:\s+(?P<apinit_age_timeout>\d+)\s+"
            # AP initiated delete for transmission fail threshold             : int
            r"\s+AP initiated delete for transmission fail threshold\s+:\s+(?P<apinit_transmission_fail_threshold>\d+)\s+"
            # AP initiated delete for uplink receive timeout                  : int
            r"\s+AP initiated delete for uplink receive timeout\s+:\s+(?P<apinit_uplink_recieve_timeout>\d+)\s+"
            # AP initiated delete for sensor scan next radio                  : int
            r"\s+AP initiated delete for sensor scan next radio\s+:\s+(?P<apinit_scan_next_radio>\d+)\s+"
            # AP initiated delete for sensor scan other BSSID                 : int
            r"\s+AP initiated delete for sensor scan other BSSID\s+:\s+(?P<apinit_scan_other_bssid>\d+)\s+"
            # AAA server unavailable                                          : int
            r"\s+AAA server unavailable\s+:\s+(?P<aaa_unavailable>\d+)\s+"
            # AAA server not ready                                            : int
            r"\s+AAA server not ready\s+:\s+(?P<aaa_not_ready>\d+)\s+"
            # No dot1x method configuration                                   : int
            r"\s+No dot1x method configuration\s+:\s+(?P<dot1x_no_config>\d+)\s+"
            # Client Abort                                                    : int
            r"\s+Client Abort\s+:\s+(?P<client_abort>\d+)\s+"
            # Association connection timeout                                  : int
            r"\s+Association connection timeout\s+:\s+(?P<connection_timeout_assocation>\d+)\s+"
            # MAC-AUTH connection timeout                                     : int
            r"\s+MAC-AUTH connection timeout\s+:\s+(?P<connection_timeout_macauth>\d+)\s+"
            # L2-AUTH connection timeout                                      : int
            r"\s+L2-AUTH connection timeout\s+:\s+(?P<connection_timeout_l2auth>\d+)\s+"
            # L3-AUTH connection timeout                                      : int
            r"\s+L3-AUTH connection timeout\s+:\s+(?P<connection_timeout_l3auth>\d+)\s+"
            # Mobility connection timeout                                     : int
            r"\s+Mobility connection timeout\s+:\s+(?P<connection_timeout_mobility>\d+)\s+"
            # static IP connection timeout                                    : int
            r"\s+static IP connection timeout\s+:\s+(?P<connection_timeout_static_ip>\d+)\s+"
            # SM session creation timeout                                     : int
            r"\s+SM session creation timeout\s+:\s+(?P<connection_timeout_sm_session_creation>\d+)\s+"
            # IP-LEARN connection timeout                                     : int
            r"\s+IP-LEARN connection timeout\s+:\s+(?P<connection_timeout_iplearn>\d+)\s+"
            # NACK IFID exists                                                : int
            r"\s+NACK IFID exists\s+:\s+(?P<nack_ifid_exists>\d+)\s+"
            # Radio Down                                                      : int
            r"\s+Radio Down\s+:\s+(?P<radio_down>\d+)\s+"
            # EoGRE Reset                                                     : int
            r"\s+EoGRE Reset\s+:\s+(?P<eogre_reset>\d+)\s+"
            # EoGRE Generic Join Failure                                      : int
            r"\s+EoGRE Generic Join Failure\s+:\s+(?P<eogre_generic_join_fail>\d+)\s+"
            # EoGRE HA-Reconciliation                                         : int
            r"\s+EoGRE HA-Reconciliation\s+:\s+(?P<eogre_ha_reconcile>\d+)\s+"
            # EoGRE Invalid VLAN                                              : int
            r"\s+EoGRE Invalid VLAN\s+:\s+(?P<eogre_invalid_vlan>\d+)\s+"
            # EoGRE Invalid Domain                                            : int
            r"\s+EoGRE Invalid Domain\s+:\s+(?P<eogre_invalid_domain>\d+)\s+"
            # EoGRE Empty Domain                                              : int
            r"\s+EoGRE Empty Domain\s+:\s+(?P<eogre_empty_domain>\d+)\s+"
            # EoGRE Domain Shut                                               : int
            r"\s+EoGRE Domain Shut\s+:\s+(?P<eogre_domain_shut>\d+)\s+"
            # EoGRE Invalid Gateway                                           : int
            r"\s+EoGRE Invalid Gateway\s+:\s+(?P<eogre_invalid_gateway>\d+)\s+"
            # EoGRE All Gateways down                                         : int
            r"\s+EoGRE All Gateways down\s+:\s+(?P<eogre_all_gateways_down>\d+)\s+"
            # EoGRE Flex - no active gateway                                  : int
            r"\s+EoGRE Flex - no active gateway\s+:\s+(?P<eogre_flex_no_gateway>\d+)\s+"
            # EoGRE Rule Matching error                                       : int
            r"\s+EoGRE Rule Matching error\s+:\s+(?P<eogre_rule_error>\d+)\s+"
            # EoGRE AAA Override error                                        : int
            r"\s+EoGRE AAA Override error\s+:\s+(?P<eogre_aaa_override_error>\d+)\s+"
            # EoGRE client onboarding error                                   : int
            r"\s+EoGRE client onboarding error\s+:\s+(?P<eogre_onboarding_error>\d+)\s+"
            # EoGRE Mobility Handoff error                                    : int
            r"\s+EoGRE Mobility Handoff error\s+:\s+(?P<eogre_mobility_handoff_error>\d+)\s+"
            # IP Update timeout                                               : int
            r"\s+IP Update timeout\s+:\s+(?P<ip_update_timeout>\d+)\s+"
            # L3 VLAN Override connection timeout                         : int
            r"\s+L3 VLAN Override connection timeout\s+:\s+(?P<connection_timeout_l3vlan_override>\d+)\s+"
            # Mobility peer delete                                            : int
            r"\s+Mobility peer delete\s+:\s+(?P<mobility_peer_delete>\d+)\s+"
            # NACK IFID mismatch                                              : int
            r"\s+NACK IFID mismatch\s+:\s+(?P<nack_ifid_mismatch>\d+)\s+"
        )

        wlan_obj = {}

        if re.search(wlan_capture, output, re.MULTILINE):
            search = re.search(wlan_capture, output, re.MULTILINE)
            group = search.groupdict()

            # convert str to int
            group["id"] = int(group["id"])

            new_group = {"wlan": group}
            wlan_obj.update(new_group)

        if re.search(client_stats_capture, output, re.MULTILINE):
            search = re.search(client_stats_capture, output, re.MULTILINE)
            group = search.groupdict()

            for item in group:
                # convert str to int
                group[item] = int(group[item])

            new_group = {"client_stats": group}
            wlan_obj.update(new_group)

        if re.search(client_delete_capture, output, re.MULTILINE):
            search = re.search(client_delete_capture, output, re.MULTILINE)
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
