import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ==============================
# Schema for:
#  * 'show wlan id client stats'
# ==============================
class ShowWlanIdClientStatsSchema(MetaParser):
    """Schema for show wlan id client stats."""

    schema = {}


# ==============================
# Parser for:
#  * 'show wlan id client stats'
# ==============================
class ShowWlanIdClientStats(ShowWlanIdClientStatsSchema):
    """Parser for show wlan id client stats"""

    cli_command = "show wlan id client stats"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        else:
            output = output

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
            r"\s+Delete received from AP\s+:\s+(?P<ap_delete>\d+)\n+"
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
            r"\s+802.11w MAX SA queries reached\s+:\s+(?P<sa_queries_reached>\d+)\n+"
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
            r"\s+Policy Manager internal error\s+:\s+(?P<pm_internal_error>\d+)\n+"
            # Mobility WLAN down                                              : 0
            r"\s+Mobility WLAN down\s+:\s+(?P<mobility_wlan_down>\d+)\n+"
            # Mobility tunnel down                                            : 0
            r"\s+Mobility tunnel down\s+:\s+(?P<mobility_tunnel_down>\d+)\n+"
            # 80211v smart roam failed                                        : 0
            r"\s+80211v smart roam failed\s+:\s+(?P<smart_roam_fail>\d+)\n+"
            # DOT11v timer timeout                                            : 0
            r"\s+DOT11v timer timeout\s+:\s+(?P<dot11v_timeout>\d+)\n+"
            # DOT11v association failed                                       : 0
            r"\s+DOT11v association failed \s+:\s+(?P<dot11v_association_fail>\d+)\n+"
            # DOT11r pre-authentication failure                               : 0
            r"\s+DOT11r pre-authentication failure\s+:\s+(?P<dot11v_preauth_fail>\d+)\n+"
            # SAE authentication failure                                      : 0
            r"\s+SAE authentication failure\s+:\s+(?P<sae_auth_fail>\d+)\n+"
            # DOT11 failure                                                   : 0
            r"\s+DOT11 failure \s+:\s+(?P<dot11_fail>\d+)\n+"
            # DOT11 SAE invalid message                                       : 0
            r"\s+DOT11 SAE invalid message\s+:\s+(?P<dot11_sae_invalid>\d+)\n+"
            # DOT11 unsupported client capabilities                           : 0
            r"\s+DOT11 unsupported client capabilities\s+:\s+(?P<dot11_unsupported>\d+)\n+"
            # DOT11 association denied unspecified                            : 0
            r"\s+DOT11 association denied unspecified\s+:\s+(?P<dot11_association_unspecified>\d+)\n+"
            # DOT11 max STA                                                   : 0
            r"\s+DOT11 max STA\s+:\s+(?P<dot11_max_sta>\d+)\n+"
            # DOT11 denied data rates                                         : 0
            r"\s+DOT11 denied data rates\s+:\s+(?P<dot11_data_rates>\d+)\n+"
            # 802.11v Client RSSI lower than the association RSSI threshold   : 0
            r"\s+802.11v Client RSSI lower than the association RSSI threshold\s+:\s+(?P<rssi_low_threshold>\d+)\n+"
            # invalid QoS parameter                                           : 0
            r"\s+invalid QoS parameter\s+:\s+(?P<invalid_qos>\d+)\n+"
            # DOT11 IE validation failed                                      : 0
            r"\s+DOT11 IE validation failed\s+:\s+(?P<dot11_ie_valid>\d+)\n+"
            # DOT11 group cipher in IE validation failed                      : 0
            r"\s+DOT11 group cipher in IE validation failed\s+:\s+(?P<dot11_group_cipher>\d+)\n+"
            # DOT11 invalid pairwise cipher                                   : 0
            r"\s+DOT11 invalid pairwise cipher\s+:\s+(?P<dot11_invalid_pairwise>\d+)\n+"
            # DOT11 invalid AKM                                               : 0
            r"\s+DOT11 invalid AKM \s+:\s+(?P<dot11_invalid_akm>\d+)\n+"
            # DOT11 unsupported RSN version                                   : 0
            r"\s+DOT11 unsupported RSN version\s+:\s+(?P<dot11_unsupported_rsn>\d+)\n+"
            # DOT11 invalid RSNIE capabilities                                : 0
            r"\s+DOT11 invalid RSNIE capabilities\s+:\s+(?P<dot11_invalid_rsnie>\d+)\n+"
            # DOT11 received invalid PMKID in the received RSN IE             : 74
            r"\s+DOT11 received invalid PMKID in the received RSN IE\s+:\s+(?P<dot11_invalid_pkmid>\d+)\n+"
            # DOT11 invalid MDIE                                              : 0
            r"\s+DOT11 invalid MDIE\s+:\s+(?P<dot11_invalid_mdie>\d+)\n+"
            # DOT11 invalid FT IE                                             : 0
            r"\s+DOT11 invalid FT IE\s+:\s+(?P<dot11_invalid_ftie>\d+)\n+"
            # DOT11 QoS policy                                                : 0
            r"\s+DOT11 QoS policy\s+:\s+(?P<dot11_qos_policy>\d+)\n+"
            # DOT11 AP have insufficient bandwidth                            : 0
            r"\s+DOT11 AP have insufficient bandwidth\s+:\s+(?P<dot11_ap_bandwidth>\d+)\n+"
            # DOT11 invalid QoS parameter                                     : 0
            r"\s+DOT11 invalid QoS parameter\s+:\s+(?P<dot11_invalid_qos>\d+)\n+"
            # Client not allowed by assisted roaming                          : 0
            r"\s+Client not allowed by assisted roaming\s+:\s+(?P<not_allowed_roaming>\d+)\n+"
            # IAPP disassociation for wired client                            : 0
            r"\s+IAPP disassociation for wired client\s+:\s+(?P<iapp_disassociate>\d+)\n+"
            # Wired WGB change                                                : 0
            r"\s+Wired WGB change\s+:\s+(?P<wired_wgb_change>\d+)\n+"
            # Wired VLAN change                                               : 0
            r"\s+Wired VLAN change\s+:\s+(?P<wired_vlan_change>\d+)\n+"
            # Wired client deleted due to WGB delete                          : 0
            r"\s+Wired client deleted due to WGB delete\s+:\s+(?P<wired_wgb_delete>\d+)\n+"
            # AVC client re-anchored at the foreign controller                : 0
            r"\s+AVC client re-anchored at the foreign controller\s+:\s+(?P<avc_reanchor>\d+)\n+"
            # WGB Wired client joins as a direct wireless client              : 0
            r"\s+WGB Wired client joins as a direct wireless client\s+:\s+(?P<wgb_wired_joins>\d+)\n+"
            # AP upgrade                                                      : 0
            r"\s+AP upgrade\s+:\s+(?P<ap_upgrade>\d+)\n+"
            # Client DHCP                                                     : 0
            r"\s+Client DHCP\s+:\s+(?P<client_dhcp>\d+)\n+"
            # Client EAP timeout                                              : 0
            r"\s+Client EAP timeout\s+:\s+(?P<eap_timeout>\d+)\n+"
            # Client 8021x failure                                            : 0
            r"\s+Client 8021x failure\s+:\s+(?P<auth_8021x_fail>\d+)\n+"
            # Client device idle                                              : 0
            r"\s+Client device idle\s+:\s+(?P<device_idle>\d+)\n+"
            # Client captive portal security failure                          : 0
            r"\s+Client captive portal security failure\s+:\s+(?P<captive_portal_fail>\d+)\n+"
            # Client decryption failure                                       : 0
            r"\s+Client decryption failure \s+:\s+(?P<decrypt_fail>\d+)\n+"
            # Client interface disabled                                       : 0
            r"\s+Client interface disabled\s+:\s+(?P<int_disable>\d+)\n+"
            # Client user triggered disassociation                            : 0
            r"\s+Client user triggered disassociation\s+:\s+(?P<trigger_disassociate>\d+)\n+"
            # Client miscellaneous reason                                     : 0
            r"\s+Client miscellaneous reason\s+:\s+(?P<misc_reason>\d+)\n+"
            # Unknown                                                         : 0
            r"\s+Unknown\s+:\s+(?P<unknown>\d+)\n+"
            # Client peer triggered                                           : 0
            r"\s+Client peer triggered\s+:\s+(?P<peer_trigger>\d+)\n+"
            # Client beacon loss                                              : 0
            r"\s+Client beacon loss\s+:\s+(?P<beacon_loss>\d+)\n+"
            # Client EAP ID timeout                                           : 10928
            r"\s+Client EAP ID timeout\s+:\s+(?P<eap_id_timeout>\d+)\n+"
            # Client DOT1x timeout                                            : 0
            r"\s+Client DOT1x timeout\s+:\s+(?P<dot1x_timeout>\d+)\n+"
            # Malformed EAP key frame                                         : 0
            r"\s+Malformed EAP key frame\s+:\s+(?P<bad_eap_keyframe>\d+)\n+"
            # EAP key install bit is not expected                             : 0
            r"\s+EAP key install bit is not expected\s+:\s+(?P<eap_keyinstall_unexpected>\d+)\n+"
            # EAP key error bit is not expected                               : 0
            r"\s+EAP key error bit is not expected\s+:\s+(?P<eap_keyerror_unexpected>\d+)\n+"
            # EAP key ACK bit is not expected                                 : 0
            r"\s+EAP key ACK bit is not expected\s+:\s+(?P<eap_keyack_unexpected>\d+)\n+"
            # Invalid key type                                                : 0
            r"\s+Invalid key type\s+:\s+(?P<invalid_key_type>\d+)\n+"
            # EAP key secure bit is not expected                              : 0
            r"\s+EAP key secure bit is not expected\s+:\s+(?P<eap_keysecure_unexected>\d+)\n+"
            # key description version mismatch                                : 0
            r"\s+key description version mismatch\s+:\s+(?P<key_ver_mismatch>\d+)\n+"
            # wrong replay counter                                            : 1
            r"\s+wrong replay counter\s+:\s+(?P<wrong_replay_counter>\d+)\n+"
            # EAP key MIC bit expected                                        : 0
            r"\s+EAP key MIC bit expected\s+:\s+(?P<eap_keymic_expected>\d+)\n+"
            # MIC validation failed                                           : 7
            r"\s+MIC validation failed\s+:\s+(?P<mic_invalid>\d+)\n+"
            # Error while PTK computation                                     : 0
            r"\s+Error while PTK computation\s+:\s+(?P<ptk_error>\d+)\n+"
            # Incorrect credentials                                           : 16
            r"\s+Incorrect credentials\s+:\s+(?P<bad_credentials>\d+)\n+"
            # Client connection lost                                          : 0
            r"\s+Client connection lost\s+:\s+(?P<connection_lost>\d+)\n+"
            # Reauthentication failure                                        : 0
            r"\s+Reauthentication failure\s+:\s+(?P<reauthentication_fail>\d+)\n+"
            # Port admin disabled                                             : 0
            r"\s+Port admin disabled\s+:\s+(?P<port_admin_disabled>\d+)\n+"
            # Supplicant restart                                              : 0
            r"\s+Supplicant restart\s+:\s+(?P<supplicant_restart>\d+)\n+"
            # No IP                                                           : 93
            r"\s+No IP\s+:\s+(?P<no_ip>\d+)\n+"
            # Call admission controller at anchor node                        : 0
            r"\s+Call admission controller at anchor node\s+:\s+(?P<call_admission>\d+)\n+"
            # Anchor no memory                                                : 0
            r"\s+Anchor no memory\s+:\s+(?P<anchor_no_memory>\d+)\n+"
            # Anchor invalid Mobility BSSID                                   : 0
            r"\s+Anchor invalid Mobility BSSID\s+:\s+(?P<anchor_invalid_bssid>\d+)\n+"
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
            r"\s+QoS policy send to AP failure\s+:\s+(?P<qos_send_apfail>\d+)\n+"
            # QoS policy bind on AP failure                                   : 0
            r"\s+QoS policy bind on AP failure\s+:\s+(?P<qos_bind_apfail>\d+)\n+"
            # QoS policy unbind on AP failure                                 : 0
            r"\s+QoS policy unbind on AP failure\s+:\s+(?P<qos_unbind_apfail>\d+)\n+"
            # Static IP anchor discovery failure                              : 0
            r"\s+Static IP anchor discovery failure\s+:\s+(?P<ip_anchor_fail>\d+)\n+"
            # VLAN failure                                                    : 0
            r"\s+VLAN failure\s+:\s+(?P<vlan_fail>\d+)\n+"
            # ACL failure                                                     : 0
            r"\s+ACL failure\s+:\s+(?P<acl_fail>\d+)\n+"
            # Redirect ACL failure                                            : 2
            r"\s+Redirect ACL failure\s+:\s+(?P<redirect_acl_fail>\d+)\n+"
            # Accounting failure                                              : 0
            r"\s+Accounting failure\s+:\s+(?P<account_fail>\d+)\n+"
            # Security group tag failure                                      : 0
            r"\s+Security group tag failure\s+:\s+(?P<security_grouptag_fail>\d+)\n+"
            # FQDN filter definition does not exist                           : 0
            r"\s+FQDN filter definition does not exist\s+:\s+(?P<fqdn_filter_missing>\d+)\n+"
            # Wrong filter type, expected postauth FQDN filter                : 0
            r"\s+Wrong filter type, expected postauth FQDN filter\s+:\s+(?P<wrong_postauth_fqdnfilter>\d+)\n+"
            # Wrong filter type, expected preauth FQDN filter                 : 0
            r"\s+Wrong filter type, expected preauth FQDN filter\s+:\s+(?P<wrong_preauth_fqdnfilter>\d+)\n+"
            # Invalid group id for FQDN filter valid range  1..16             : 0
            r"\s+Invalid group id for FQDN filter valid range  1..16\s+:\s+(?P<invalid_group_id>\d+)\n+"
            # Policy parameter mismatch                                       : 0
            r"\s+Policy parameter mismatch\s+:\s+(?P<policy_mismatch>\d+)\n+"
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
            r"\s+AP initiated delete for SA query timeout\s+:\s+(?P<apinit_sa_timcleout>\d+)\n+"
            # AP initiated delete for channel switch at AP                    : 0
            r"\s+AP initiated delete for channel switch at AP\s+:\s+(?P<apinit_channel_switch>\d+)\n+"
            # AP initiated delete for bad AID                                 : 0
            r"\s+AP initiated delete for bad AID\s+:\s+(?P<apinit_bad_aid>\d+)\n+"
            # AP initiated delete for request                                 : 0
            r"\s+AP initiated delete for request\s+:\s+(?P<apinit_request>\d+)\n+"
            # AP initiated delete for interface reset                         : 0
            r"\s+AP initiated delete for interface reset\s+:\s+(?P<apinit_int_reset>\d+)\n+"
            # AP initiated delete for all on slot                             : 0
            r"\s+AP initiated delete for all on slot\s+:\s+(?P<apinit_all_slots>\d+)\n+"
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
            r"\s+AP initiated delete for sensor station timeout\s+:\s+(?P<apinit_sensor_timeout>\d+)\n+"
            # AP initiated delete for age timeout                             : 0
            r"\s+AP initiated delete for age timeout\s+:\s+(?P<apinit_age_timeout>\d+)\n+"
            # AP initiated delete for transmission fail threshold             : 0
            r"\s+AP initiated delete for transmission fail threshold\s+:\s+(?P<apinit_transmission_fail>\d+)\n+"
            # AP initiated delete for uplink receive timeout                  : 0
            r"\s+AP initiated delete for uplink receive timeout\s+:\s+(?P<apinit_uplink_recieve>\d+)\n+"
            # AP initiated delete for sensor scan next radio                  : 0
            r"\s+AP initiated delete for sensor scan next radio\s+:\s+(?P<apinit_scan_radio>\d+)\n+"
            # AP initiated delete for sensor scan other BSSID                 : 0
            r"\s+AP initiated delete for sensor scan other BSSID\s+:\s+(?P<apinit_scan_bssid>\d+)\n+"
            # AAA server unavailable                                          : 0
            r"\s+AAA server unavailable\s+:\s+(?P<aaa_unavailable>\d+)\n+"
            # AAA server not ready                                            : 0
            r"\s+AAA server not ready\s+:\s+(?P<aaa_notready>\d+)\n+"
            # No dot1x method configuration                                   : 0
            r"\s+No dot1x method configuration\s+:\s+(?P<no_dot1x_config>\d+)\n+"
            # Client Abort                                                    : 0
            r"\s+Client Abort\s+:\s+(?P<client_abort>\d+)\n+"
            # Association connection timeout                                  : 0
            r"\s+Association connection timeout\s+:\s+(?P<conn_assocation_timeout>\d+)\n+"
            # MAC-AUTH connection timeout                                     : 0
            r"\s+MAC-AUTH connection timeout\s+:\s+(?P<conn_macauth_timeout>\d+)\n+"
            # L2-AUTH connection timeout                                      : 882
            r"\s+L2-AUTH connection timeout\s+:\s+(?P<conn_l2auth_timeout>\d+)\n+"
            # L3-AUTH connection timeout                                      : 0
            r"\s+L3-AUTH connection timeout\s+:\s+(?P<conn_l3auth_timeout>\d+)\n+"
            # Mobility connection timeout                                     : 0
            r"\s+Mobility connection timeout\s+:\s+(?P<conn_mobility_timeout>\d+)\n+"
            # static IP connection timeout                                    : 0
            r"\s+static IP connection timeout\s+:\s+(?P<conn_ip_timeout>\d+)\n+"
            # SM session creation timeout                                     : 0
            r"\s+SM session creation timeout\s+:\s+(?P<conn_sm_timeout>\d+)\n+"
            # IP-LEARN connection timeout                                     : 25
            r"\s+IP-LEARN connection timeout\s+:\s+(?P<conn_iplearn_timeout>\d+)\n+"
            # NACK IFID exists                                                : 0
            r"\s+NACK IFID exists\s+:\s+(?P<nack_ifid_exists>\d+)\n+"
            # Radio Down                                                      : 0
            r"\s+Radio Down\s+:\s+(?P<radio_down>\d+)\n+"
            # EoGRE Reset                                                     : 0
            r"\s+EoGRE Reset\s+:\s+(?P<eogre_reset>\d+)\n+"
            # EoGRE Generic Join Failure                                      : 0
            r"\s+EoGRE Generic Join Failure\s+:\s+(?P<eogre_join_fail>\d+)\n+"
            # EoGRE HA-Reconciliation                                         : 0
            r"\s+EoGRE HA-Reconciliation\s+:\s+(?P<eogre_ha_reconcile>\d+)\n+"
            # EoGRE Invalid VLAN                                              : 0
            r"\s+EoGRE Invalid VLAN\s+:\s+(?P<eogre_invalid_vlan>\d+)\n+"
            # EoGRE Invalid Domain                                            : 0
            r"\s+EoGRE Invalid Domain\s+:\s+(?P<eogre_invalid_domain>\d+)\n+"
            # EoGRE Empty Domain                                              : 0
            r"\s+EoGRE Empty Domain\s+:\s+(?P<eogre_empty_omain>\d+)\n+"
            # EoGRE Domain Shut                                               : 0
            r"\s+EoGRE Domain Shut\s+:\s+(?P<eogre_domain_shut>\d+)\n+"
            # EoGRE Invalid Gateway                                           : 0
            r"\s+EoGRE Invalid Gateway\s+:\s+(?P<eogre_invalid_gateway>\d+)\n+"
            # EoGRE All Gateways down                                         : 0
            r"\s+EoGRE All Gateways down\s+:\s+(?P<eogre_gateways_down>\d+)\n+"
            # EoGRE Flex - no active gateway                                  : 0
            r"\s+EoGRE Flex - no active gateway\s+:\s+(?P<eogreflex_no_gateway>\d+)\n+"
            # EoGRE Rule Matching error                                       : 0
            r"\s+EoGRE Rule Matching error\s+:\s+(?P<eogre_rule_error>\d+)\n+"
            # EoGRE AAA Override error                                        : 0
            r"\s+EoGRE AAA Override error\s+:\s+(?P<eogre_aaa_override>\d+)\n+"
            # EoGRE client onboarding error                                   : 0
            r"\s+EoGRE client onboarding error\s+:\s+(?P<eogre_onboarding>\d+)\n+"
            # EoGRE Mobility Handoff error                                    : 0
            r"\s+EoGRE Mobility Handoff error\s+:\s+(?P<eogre_mobility_handoff>\d+)\n+"
            # IP Update timeout                                               : 0
            r"\s+IP Update timeout\s+:\s+(?P<ip_update_timeout>\d+)\n+"
            # L3 VLAN Override connection timeout                         : 0
            r"\s+L3 VLAN Override connection timeout\s+:\s+(?P<l3vlan_override_timeout>\d+)\n+"
            # Mobility peer delete                                            : 0
            r"\s+Mobility peer delete\s+:\s+(?P<mobility_peer_delete>\d+)\n+"
            # NACK IFID mismatch                                              : 0
            r"\s+NACK IFID mismatch\s+:\s+(?P<nack_ifid_mismatch>\d+)\n+"
        )

        capture = client_delete_capture
        info_search = re.search(capture, output, re.MULTILINE)
        info_group = info_search.groupdict()

        wlan_obj = {}

        dict_keys = [
            "anchor",
            "ap",
            "apinit",
            "conn",
            "dot11",
            "dot11v",
            "dot11x",
            "eap",
            "eogre",
            "invalid",
            "mac",
            "mobility",
            "no",
            "policy",
            "qos",
            "wired",
            "wrong",
        ]

        for dict_key in dict_keys:
            rendered_dict = {dict_key: {}}
            for group in info_group:
                # if dict_key plus _ matches the first part in the key
                if f"{dict_key}_" in group:
                    # strip the first part of the key because now it's in a dict
                    group_dict = {group.strip(f"{dict_key}_"): info_group[group]}
                    rendered_dict[dict_key].update(group_dict)

            wlan_obj.update(rendered_dict)