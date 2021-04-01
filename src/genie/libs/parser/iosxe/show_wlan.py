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

    cli_command = 'show wlan summary'

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

   
# ==================
# Schema for:
#  * 'show wlan all'
# ==================
class ShowWlanAllSchema(MetaParser):
    """Schema for show wlan all."""

    schema = {
        "wlan_names" : {
            Optional(str): {
                "identifier": int,
                Optional("description"): str,
                "ssid": str,
                "status": str,
                "broadcast_ssid": str,
                "advertise_ap_name": str,
                "universal_ap_admin": str,
                "max_clients_wlan": int,
                "max_clients_ap": int,
                "max_clients_ap_radio": int,
                "okc": str,
                "active_clients": int,
                "chd_per_wlan": str,
                "wmm": str,
                Optional("wifi_direct_policy"): str,
                "channel_scan_defer_priority": {
                    "priority": list
                },
                "scan_defer_time_msecs": int,
                "media_stream_multicast_direct": str,
                "ccx_aironet_support": str,
                "p2p_blocking_action": str,
                "radio_policy": str,
                Optional("dtim_period_dot11a"): str,
                Optional("dtim_period_dot11b"): str,
                "local_eap_authentication": str,
                "mac_filter_authorization_list_name": str,
                "mac_filter_override_authorization_list_name": str,
                "dot1x_authentication_list_name": str,
                "dot1x_authorization_list_name": str,
                "security": {
                "dot11_authentication": str,
                    "static_wep_keys": str,
                    "wifi_protected_access_wpa1_wpa2_wpa3": str,
                    Optional("wifi_protected_access_wpa"): {
                        Optional("wpa_ssn_ie"): str
                    },
                    Optional("wifi_protected_access_wpa2"): {
                        Optional("wpa2_rsn_ie"): str,
                        Optional("wpa2_attributes"): {
                            Optional("mpsk"): str,
                            Optional("aes"): str,
                            Optional("ccmp256"): str,
                            Optional("gcmp128"): str,
                            Optional("gcmp256"): str,
                            Optional("randomized_gtk"): str
                        }
                    },
                    Optional("wifi_protected_access_wpa3"): {
                        Optional("wpa3_ie"): str
                    },
                    Optional("auth_key_mgmt"): {
                        Optional("dot1x"): str,
                        Optional("psk"): str,
                        Optional("cckm"): str,
                        Optional("ft_dot1x"): str,
                        Optional("ft_psk"): str,
                        Optional("dot1x_sha256"): str,
                        Optional("psk_sha256"): str,
                        Optional("sae"): str,
                        Optional("owe"): str,
                        Optional("suiteb_1x"): str,
                        Optional("suiteb192_1x"): str
                    },
                    Optional("cckm_tsf_tolerance_msecs"): int,
                    "owe_transition_mode": str,
                    "osen": str,
                    "ft_support": str,
                    "ft_support": {
                        "ft_support_status": str,
                        "ft_reassociation_timer_secs": int,
                        "ft_over_the_ds_mode": str
                    },
                    "pmf_support": {
                        "pmf_support_status": str,
                        "pmf_association_comeback_timeout_secs": int,
                        "pmf_sa_query_time_msecs": int
                    },
                    "web_based_authenticaion": str,
                    "conditional_web_redirect": str,
                    "splash_page_web_redirect": str,
                    "webauth_on_mac_filter_failure": str,
                    "webauth_authentication_list_name": str,
                    "webauth_authorization_list_name": str,
                    "webauth_parameter_map": str
                },
                "band_select": str,
                "load_balancing": str,
                "multicast_buffer": str,
                Optional("multicast_buffer_size"): int,
                Optional("multicast_buffer_frames"): int,
                "ip_source_guard": str,
                "assisted_roaming": {
                    "neighbbor_list": str,
                    "prediction_list": str,
                    "dual_band_support": str
                },
                "ieee_dot11v_parameters": {
                    "directed_multicast_service": str,
                    "bss_max_idle": {
                        "bss_max_idle_status": str,
                        "protected_mode": str
                    },
                    "traffic_filtering_servce": str,
                    "bss_transition": {
                        "bss_transition_status": str,
                        "disassociation_imminent": {
                            "disassociation_imminent_status": str,
                            "optimised_roaming_timer": int,
                            "timer": int,
                        },
                        Optional("dual_neighbor_list"): str,
                },
                    "wmn_sleep_mode": str
                },
                "dot11ac_mu_mimo": str,
                "dot11ax_parameters": {
                    "ofdma_downlink": str,
                    "ofdma_uplink": str,
                    "mu_mimo_downlink": str,
                    "mu_mimo_uplink": str,
                    "bss_target_wake_up_time": str,
                    "bss_target_wake_up_time_broadcast_support": str
                },
                "mdns_gateway_status": str,
                "wifi_alliance_agile_multiband": str,
                "device_analytics": {
                    "advertise_support": str,
                    "share_data_with_client": str
                },
                Optional("client_scan_report_11k_beacon_radio_measurement"): {
                    "request_on_association": str,
                    "request_on_roam": str,
                },
                Optional("wifi_to_cellular_steering"): str,
            }
        }
    }


# ==================
# Parser for:
#  * 'show wlan all'
# ==================
class ShowWlanAll(ShowWlanAllSchema):
    """Parser for show wlan all"""

    cli_command = 'show wlan all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output=output

        # WLAN Profile Name     : lizzard_Fabric_F_cf6efda4
        # ================================================
        # Identifier                                     : 17
        # Description                                    :
        # Network Name (SSID)                            : lizzard
        # Status                                         : Enabled
        # Broadcast SSID                                 : Enabled
        # Advertise-Apname                               : Disabled
        # Universal AP Admin                             : Disabled
        # Max Associated Clients per WLAN                : 0
        # Max Associated Clients per AP per WLAN         : 0
        # Max Associated Clients per AP Radio per WLAN   : 200
        # OKC                                            : Enabled
        # Number of Active Clients                       : 4
        # CHD per WLAN                                   : Enabled
        # WMM                                            : Allowed
        # Channel Scan Defer Priority:
        #   Priority (default)                           : 5
        #   Priority (default)                           : 6
        # Scan Defer Time (msecs)                        : 100
        # Media Stream Multicast-direct                  : Disabled
        # CCX - AironetIe Support                        : Disabled
        # Peer-to-Peer Blocking Action                   : Disabled
        # Radio Policy                                   : 802.11a only
        # DTIM period for 802.11a radio                  :
        # DTIM period for 802.11b radio                  :
        # Local EAP Authentication                       : Disabled
        # Mac Filter Authorization list name             : Disabled
        # Mac Filter Override Authorization list name    : Disabled
        # Accounting list name                           :
        # 802.1x authentication list name                : dnac-list
        # 802.1x authorization list name                 : Disabled
        # Security
        #     802.11 Authentication                      : Open System
        #     Static WEP Keys                            : Disabled
        #     Wi-Fi Protected Access (WPA/WPA2/WPA3)     : Enabled
        #         WPA (SSN IE)                           : Disabled
        #         WPA2 (RSN IE)                          : Enabled
        #             MPSK                               : Disabled
        #             AES Cipher                         : Enabled
        #             CCMP256 Cipher                     : Disabled
        #             GCMP128 Cipher                     : Disabled
        #             GCMP256 Cipher                     : Disabled
        #             Randomized GTK                     : Disabled
        #         WPA3 (WPA3 IE)                         : Disabled
        #         Auth Key Management
        #             802.1x                             : Enabled
        #             PSK                                : Disabled
        #             CCKM                               : Disabled
        #             FT dot1x                           : Enabled
        #             FT PSK                             : Disabled
        #             Dot1x-SHA256                       : Disabled
        #             PSK-SHA256                         : Disabled
        #             SAE                                : Disabled
        #             OWE                                : Disabled
        #             SUITEB-1X                          : Disabled
        #             SUITEB192-1X                       : Disabled
        #     CCKM TSF Tolerance                         : 1000
        #     OWE Transition Mode                        : Disabled
        #     OSEN                                       : Disabled
        #     FT Support                                 : Enabled
        #         FT Reassociation Timeout               : 20
        #         FT Over-The-DS mode                    : Disabled
        #     PMF Support                                : Disabled
        #         PMF Association Comeback Timeout       : 1
        #         PMF SA Query Time                      : 200
        #     Web Based Authentication                   : Disabled
        #     Conditional Web Redirect                   : Disabled
        #     Splash-Page Web Redirect                   : Disabled
        #     Webauth On-mac-filter Failure              : Disabled
        #     Webauth Authentication List Name           : Disabled
        #     Webauth Authorization List Name            : Disabled
        #     Webauth Parameter Map                      : Disabled
        # Band Select                                    : Disabled
        # Load Balancing                                 : Disabled
        # Multicast Buffer                               : Disabled
        # Multicast Buffer Size                          : 0
        # IP Source Guard                                : Disabled
        # Assisted-Roaming
        #     Neighbor List                              : Enabled
        #     Prediction List                            : Disabled
        #     Dual Band Support                          : Disabled
        # IEEE 802.11v parameters
        #     Directed Multicast Service                 : Enabled
        #     BSS Max Idle                               : Enabled
        #         Protected Mode                         : Disabled
        #     Traffic Filtering Service                  : Disabled
        #     BSS Transition                             : Enabled
        #         Disassociation Imminent                : Disabled
        #             Optimised Roaming Timer            : 40
        #             Timer                              : 200
        #     WNM Sleep Mode                             : Disabled
        # 802.11ac MU-MIMO                               : Enabled
        # 802.11ax parameters
        #     OFDMA Downlink                             : Enabled
        #     OFDMA Uplink                               : Enabled
        #     MU-MIMO Downlink                           : Enabled
        #     MU-MIMO Uplink                             : Enabled
        #     BSS Target Wake Up Time                    : Enabled
        #     BSS Target Wake Up Time Broadcast Support  : Enabled
        # mDNS Gateway Status                            : Bridge
        # WIFI Alliance Agile Multiband                  : Disabled
        # Device Analytics
        #     Advertise Support                          : Enabled
        #     Share Data with Client                     : Disabled
        # Client Scan Report (11k Beacon Radio Measurement)
        #     Request on Association                     : Disabled
        #     Request on Roam                            : Disabled
        # WiFi to Cellular Steering                      : Disabled        

        # WLAN Profile Name     : north
        p_name = re.compile(r"^WLAN\s+Profile\s+Name\s+:\s+(?P<value>\S+)$")

        # ================================================
        p_delimeter = re.compile(r"^=+$")

        # Identifier                                     : 1
        p_identifier = re.compile(r"^Identifier\s+:\s+(?P<value>\d+)$")

        # Description                                    :
        p_description = re.compile(r"^Description\s+:\s+(?P<value>.*)$")

        # Network Name (SSID)                            : north
        p_name_ssid = re.compile(r"^Network\s+Name\s+\(SSID\)\s+:\s+(?P<value>\S+)$")

        # Status                                         : Enabled
        p_status = re.compile(r"^Status\s+:\s+(?P<value>\S+)$")

        # Broadcast SSID                                 : Enabled
        p_broadcast = re.compile(r"^Broadcast\s+SSID\s+:\s+(?P<value>\S+)$")

        # Advertise-Apname                               : Disabled
        p_advertise = re.compile(r"^Advertise-Apname\s+:\s+(?P<value>\S+)$")

        # Universal AP Admin                             : Disabled
        p_universal_admin = re.compile(r"^Universal\s+AP\s+Admin\s+:\s+(?P<value>\S+)$")

        # Max Associated Clients per WLAN                : 0
        p_max_clients_wlan = re.compile(r"^Max\s+Associated\s+Clients\s+per\s+WLAN\s+:\s+(?P<value>\d+)$")

        # Max Associated Clients per AP per WLAN         : 0
        p_max_clients_ap = re.compile(r"^Max\s+Associated\s+Clients\s+per\s+AP\s+per\s+WLAN\s+:\s+(?P<value>\d+)$")

        # Max Associated Clients per AP Radio per WLAN   : 200
        p_max_clients_radio = re.compile(r"^Max\s+Associated\s+Clients\s+per\s+AP\s+Radio\s+per\s+WLAN\s+:\s+(?P<value>\d+)$")

        # OKC                                            : Enabled
        p_okc = re.compile(r"^OKC\s+:\s+(?P<value>\S+)$")

        # Number of Active Clients                       : 4
        p_active_clients = re.compile(r"^Number\s+of\s+Active\s+Clients\s+:\s+(?P<value>\d+)$")

        # CHD per WLAN                                   : Enabled
        p_chd = re.compile(r"^CHD\s+per\s+WLAN\s+:\s+(?P<value>\S+)$")

        # WMM                                            : Allowed
        p_wmm = re.compile(r"^WMM\s+:\s+(?P<value>\S+)$")

        # WiFi Direct Policy                             : Disabled
        p_direct_policy = re.compile(r"^WiFi\s+Direct\s+Policy\s+:\s+(?P<value>\S+)$")

        # Channel Scan Defer Priority:
        p_channel_scan = re.compile(r"Channel\s+Scan\s+Defer\s+Priority:$")

        # Priority (default)                           : 5
        # Priority (default)                           : 6
        p_priority = re.compile(r"^Priority\s+\(default\)\s+:\s+(?P<value>\d+)$")

        # Scan Defer Time (msecs)                        : 100
        p_scan_defer = re.compile(r"^Scan\s+Defer\s+Time\s+\(msecs\)\s+:\s+(?P<value>\d+)$")

        # Media Stream Multicast-direct                  : Disabled
        p_media_multi = re.compile(r"^Media\s+Stream\s+Multicast-direct\s+:\s+(?P<value>\S+)$")

        # CCX - AironetIe Support                        : Disabled
        p_ccx_aironet = re.compile(r"^CCX\s+-\s+AironetIe\s+Support\s+:\s+(?P<value>\S+)$")

        # Peer-to-Peer Blocking Action                   : Disabled
        p_p2p_block = re.compile(r"^Peer-to-Peer\s+Blocking\s+Action\s+:\s+(?P<value>\S+)$")

        # Radio Policy                                   : 802.11a only
        p_radio_policy = re.compile(r"^Radio\s+Policy\s+:\s+(?P<value>.*)$")

        # DTIM period for 802.11a radio                  :
        p_dtim_a = re.compile(r"^DTIM\s+period\s+for\s+802.11a\s+radio\s+:\s+(?P<value>.*)$")

        # DTIM period for 802.11b radio                  :
        p_dtim_b = re.compile(r"^DTIM\s+period\s+for\s+802.11b\s+radio\s+:\s+(?P<value>.*)$")

        # Local EAP Authentication                       : Disabled
        p_local_eap = re.compile(r"^Local\s+EAP\s+Authentication\s+:\s+(?P<value>\S+)$")

        # Mac Filter Authorization list name             : Disabled
        p_mac_filter_auth = re.compile(r"^Mac\s+Filter\s+Authorization\s+list\s+name\s+:\s+(?P<value>\S+)$")

        # Mac Filter Override Authorization list name    : Disabled
        p_mac_filter_override = re.compile(r"^Mac\s+Filter\s+Override\s+Authorization\s+list\s+name\s+:\s+(?P<value>\S+)$")

        # Accounting list name                           :
        p_accounting_list = re.compile(r"^Accounting\s+list\s+name\s+:\s+(?P<value>.*)$")

        # 802.1x authentication list name                : default
        p_dot1x_authen = re.compile(r"^802.1x\s+authentication\s+list\s+name\s+:\s+(?P<value>\S+)$")

        # 802.1x authorization list name                 : Disabled
        p_dot1x_author = re.compile(r"^802.1x\s+authorization\s+list\s+name\s+:\s+(?P<value>\S+)$")

        # Security
        p_security = re.compile(r"^Security$")

        # 802.11 Authentication                      : Open System
        p_dot11_authen = re.compile(r"^802.11\s+Authentication\s+:\s+(?P<value>.*)$")

        # Static WEP Keys                            : Disabled
        p_static_wep = re.compile(r"^Static\s+WEP\s+Keys\s+:\s+(?P<value>.*)$")

        # Wi-Fi Protected Access (WPA/WPA2/WPA3)     : Enabled
        p_pro_access = re.compile(r"^Wi-Fi\s+Protected\s+Access\s+\(WPA\/WPA2\/WPA3\)\s+:\s+(?P<value>\S+)$")

        # WPA (SSN IE)                           : Disabled
        p_wpa_ssn = re.compile(r"^WPA\s+\(SSN\s+IE\)\s+:\s+(?P<value>\S+)$")

        # WPA2 (RSN IE)                          : Enabled
        p_wpa2_rsn = re.compile(r"^WPA2\s+\(RSN\s+IE\)\s+:\s+(?P<value>\S+)$")

        # MPSK                               : Disabled
        p_mpsk = re.compile(r"^MPSK\s+:\s+(?P<value>\S+)$")

        # AES Cipher                         : Enabled
        p_aes = re.compile(r"^AES\s+Cipher\s+:\s+(?P<value>\S+)$")

        # CCMP256 Cipher                     : Disabled
        p_ccmp256 = re.compile(r"^CCMP256\s+Cipher\s+:\s+(?P<value>\S+)$")

        # GCMP128 Cipher                     : Disabled
        p_gcmp128 = re.compile(r"^GCMP128\s+Cipher\s+:\s+(?P<value>\S+)$")

        # GCMP256 Cipher                     : Disabled
        p_gcmp256 = re.compile(r"^GCMP256\s+Cipher\s+:\s+(?P<value>\S+)$")

        # Randomized GTK                     : Disabled
        p_gtk = re.compile(r"^Randomized\s+GTK\s+:\s+(?P<value>\S+)$")

        # WPA3 (WPA3 IE)                         : Disabled
        p_wpa3 = re.compile(r"^WPA3\s+\(WPA3\s+IE\)\s+:\s+(?P<value>\S+)$")

        # Auth Key Management
        p_auth_key_mgmt = re.compile(r"^Auth\s+Key\s+Management$")

        # 802.1x                             : Enabled
        p_key_dot1x = re.compile(r"^802.1x\s+:\s+(?P<value>\S+)$")

        # PSK                                : Disabled
        p_key_psk = re.compile(r"^PSK\s+:\s+(?P<value>\S+)$")

        # CCKM                               : Disabled
        p_key_cckm = re.compile(r"^CCKM\s+:\s+(?P<value>\S+)$")

        # FT dot1x                           : Disabled
        p_key_ftdot1x = re.compile(r"^FT\s+dot1x\s+:\s+(?P<value>\S+)$")

        # FT PSK                             : Disabled
        p_key_ftpsk = re.compile(r"^FT\s+PSK\s+:\s+(?P<value>\S+)$")

        # Dot1x-SHA256                       : Disabled
        p_key_dot1xsha = re.compile(r"^Dot1x-SHA256\s+:\s+(?P<value>\S+)$")

        # PSK-SHA256                         : Disabled
        p_key_psksha = re.compile(r"^PSK-SHA256\s+:\s+(?P<value>\S+)$")

        # SAE                                : Disabled
        p_key_sae = re.compile(r"^SAE\s+:\s+(?P<value>\S+)$")

        # OWE                                : Disabled
        p_key_owe = re.compile(r"^OWE\s+:\s+(?P<value>\S+)$")

        # SUITEB-1X                          : Disabled
        p_key_suiteb = re.compile(r"^SUITEB-1X\s+:\s+(?P<value>\S+)$")

        # SUITEB192-1X                       : Disabled
        p_key_suiteb192 = re.compile(r"^SUITEB192-1X\s+:\s+(?P<value>\S+)$")

        # CCKM TSF Tolerance (msecs)                 : 1000
        p_cckm_tsf_msec = re.compile(r"^CCKM\s+TSF\s+Tolerance\s+\(msecs\)\s+:\s+(?P<value>\d+)$")

        # CCKM TSF Tolerance                 : 1000
        p_cckm_tsf = re.compile(r"^CCKM\s+TSF\s+Tolerance\s+:\s+(?P<value>\d+)$")

        # OWE Transition Mode                        : Disabled
        p_owe_transition = re.compile(r"^OWE\s+Transition\s+Mode\s+:\s+(?P<value>\S+)$")

        # OSEN                                       : Disabled
        p_osen = re.compile(r"^OSEN\s+:\s+(?P<value>\S+)$")

        # FT Support                                 : Adaptive
        p_ftsupport = re.compile(r"^FT\s+Support\s+:\s+(?P<value>\S+)$")

        # FT Reassociation Timeout (secs)        : 20
        p_ft_re_timeout_secs = re.compile(r"^FT\s+Reassociation\s+Timeout\s+\(secs\)\s+:\s+(?P<value>\d+)$")

        # FT Reassociation Timeout        : 20
        p_ft_re_timeout = re.compile(r"^FT\s+Reassociation\s+Timeout\s+:\s+(?P<value>\d+)$")

        # FT Over-The-DS mode                    : Disabled
        p_ft_dst = re.compile(r"^FT\s+Over-The-DS\s+mode\s+:\s+(?P<value>\S+)$")

        # PMF Support                                : Disabled
        p_pmf = re.compile(r"^PMF\s+Support\s+:\s+(?P<value>\S+)$")

        # PMF Association Comeback Timeout (secs): 1
        p_association_comeback_secs = re.compile(r"^PMF\s+Association\s+Comeback\s+Timeout\s+\(secs\):\s+(?P<value>\d+)$")

        # PMF Association Comeback Timeout : 1
        p_association_comeback = re.compile(r"^PMF\s+Association\s+Comeback\s+Timeout\s+:\s+(?P<value>\d+)$")

        # PMF SA Query Time (msecs)              : 200
        p_pmf_sa_msecs = re.compile(r"^PMF\s+SA\s+Query\s+Time\s+\(msecs\)\s+:\s+(?P<value>\d+)$")

        # PMF SA Query Time              : 200
        p_pmf_sa = re.compile(r"^PMF\s+SA\s+Query\s+Time\s+:\s+(?P<value>\d+)$")

        # Web Based Authentication                   : Disabled
        p_web_authen = re.compile(r"^Web\s+Based\s+Authentication\s+:\s+(?P<value>\S+)$")

        # Conditional Web Redirect                   : Disabled
        p_web_redirect = re.compile(r"^Conditional\s+Web\s+Redirect\s+:\s+(?P<value>\S+)$")

        # Splash-Page Web Redirect                   : Disabled
        p_splash_page = re.compile(r"^Splash-Page\s+Web\s+Redirect\s+:\s+(?P<value>\S+)$")

        # Webauth On-mac-filter Failure              : Disabled
        p_webauth_mac = re.compile(r"^Webauth\s+On-mac-filter\s+Failure\s+:\s+(?P<value>\S+)$")

        # Webauth Authentication List Name           : Disabled
        p_webauthen_list = re.compile(r"^Webauth\s+Authentication\s+List\s+Name\s+:\s+(?P<value>\S+)$")

        # Webauth Authorization List Name            : Disabled
        p_webauthor_list = re.compile(r"^Webauth\s+Authorization\s+List\s+Name\s+:\s+(?P<value>\S+)$")

        # Webauth Parameter Map                      : Disabled
        p_webauthen_map = re.compile(r"^Webauth\s+Parameter\s+Map\s+:\s+(?P<value>\S+)$")

        # Band Select                                    : Disabled
        p_band_select = re.compile(r"^Band\s+Select\s+:\s+(?P<value>\S+)$")

        # Load Balancing                                 : Disabled
        p_load_balancing = re.compile(r"^Load\s+Balancing\s+:\s+(?P<value>\S+)$")

        # Multicast Buffer                               : Disabled
        p_multi_buffer = re.compile(r"^Multicast\s+Buffer\s+:\s+(?P<value>\S+)$")

        # Multicast Buffers (frames)                     : 0
        p_multi_buffer_frames = re.compile(r"^Multicast\s+Buffers?\s+\(frames\)\s+:\s+(?P<value>\d+)$")

        # Multicast Buffer Size                          : 0
        p_multi_buffer_size = re.compile(r"^Multicast\s+Buffer\s+Size\s+:\s+(?P<value>\d+)$")

        # IP Source Guard                                : Disabled
        p_ip_sourceguard = re.compile(r"^IP\s+Source\s+Guard\s+:\s+(?P<value>\S+)$")

        # Assisted-Roaming
        p_assisted_roaming = re.compile(r"^Assisted-Roaming$")

        # Neighbor List                              : Enabled
        p_ar_neighbor_list = re.compile(r"^Neighbor\s+List\s+:\s+(?P<value>\S+)$")

        # Prediction List                            : Disabled
        p_ar_prediction = re.compile(r"^Prediction\s+List\s+:\s+(?P<value>\S+)$")

        # Dual Band Support                          : Disabled
        p_ar_db = re.compile(r"^Dual\s+Band\s+Support\s+:\s+(?P<value>\S+)$")

        # IEEE 802.11v parameters
        p_ieee_11v = re.compile(r"^IEEE\s+802.11v\s+parameters$")

        # Directed Multicast Service                 : Enabled
        p_11v_multicast = re.compile(r"^Directed\s+Multicast\s+Service\s+:\s+(?P<value>\S+)$")

        # BSS Max Idle                               : Enabled
        p_11v_bss = re.compile(r"^BSS\s+Max\s+Idle\s+:\s+(?P<value>\S+)$")

        # Protected Mode                         : Disabled
        p_11v_bss_protected = re.compile(r"^Protected\s+Mode\s+:\s+(?P<value>\S+)$")

        # Traffic Filtering Service                  : Disabled
        p_11v_filtering = re.compile(r"^Traffic\s+Filtering\s+Service\s+:\s+(?P<value>\S+)$")

        # BSS Transition                             : Enabled
        p_11v_bss_trans = re.compile(r"^BSS\s+Transition\s+:\s+(?P<value>\S+)$")

        # Disassociation Imminent                : Disabled
        p_11v_bss_trans_disassoc = re.compile(r"^Disassociation\s+Imminent\s+:\s+(?P<value>\S+)$")

        # Optimised Roaming Timer (TBTTS)    : 40
        p_11v_bss_trans_disassoc_tbtts = re.compile(r"^Optimised\s+Roaming\s+Timer\s+\(TBTTS\)\s+:\s+(?P<value>\d+)$")

        # Timer (TBTTS)                      : 200
        p_11v_bss_trans_disassoc_timer = re.compile(r"^Timer\s+\(TBTTS\)\s+:\s+(?P<value>\d+)$")

        # Optimised Roaming Timer (TBTTS)    : 40
        p_11v_bss_trans_disassoc_tbtts_extra = re.compile(r"^Optimised\s+Roaming\s+Timer\s+\(TBTTS\)\s+:\s+(?P<value>\d+)$")

        # Timer (TBTTS)                      : 200
        p_11v_bss_trans_disassoc_timer_extra = re.compile(r"^Timer\s+\(TBTTS\)\s+:\s+(?P<value>\d+)$")

        # Optimised Roaming Timer    : 40
        p_11v_bss_trans_disassoc_tbtts = re.compile(r"^Optimised\s+Roaming\s+Timer\s+:\s+(?P<value>\d+)$")

        # Timer                       : 200
        p_11v_bss_trans_disassoc_timer = re.compile(r"^Timer\s+:\s+(?P<value>\d+)$")

        # Dual Neighbor List                     : Disabled
        p_11v_dual_neighbor = re.compile(r"^Dual\s+Neighbor\s+List\s+:\s+(?P<value>\S+)$")

        # WNM Sleep Mode                             : Disabled
        p_11v_wnm = re.compile(r"^WNM\s+Sleep\s+Mode\s+:\s+(?P<value>\S+)$")

        # 802.11ac MU-MIMO                               : Enabled
        p_11ac_mimo = re.compile(r"^802.11ac\s+MU-MIMO\s+:\s+(?P<value>\S+)$")

        # 802.11ax parameters
        p_11ax_params = re.compile(r"^802.11ax\s+parameters$")

        # OFDMA Downlink                             : Enabled
        p_11ax_ofdma_down = re.compile(r"^OFDMA\s+Downlink\s+:\s+(?P<value>\S+)$")

        # OFDMA Uplink                               : Enabled
        p_11ax_ofdma_up = re.compile(r"^OFDMA\s+Uplink\s+:\s+(?P<value>\S+)$")

        # MU-MIMO Downlink                           : Enabled
        p_11ax_mimo_down = re.compile(r"^MU-MIMO\s+Downlink\s+:\s+(?P<value>\S+)$")

        # MU-MIMO Uplink                             : Enabled
        p_11ax_mimo_up = re.compile(r"^MU-MIMO\s+Uplink\s+:\s+(?P<value>\S+)$")

        # BSS Target Wake Up Time                    : Enabled
        p_11ax_bss = re.compile(r"^BSS\s+Target\s+Wake\s+Up\s+Time\s+:\s+(?P<value>\S+)$")

        # BSS Target Wake Up Time Broadcast Support  : Enabled
        p_11ax_bss_broad = re.compile(r"^BSS\s+Target\s+Wake\s+Up\s+Time\s+Broadcast\s+Support\s+:\s+(?P<value>\S+)$")

        # mDNS Gateway Status                            : Bridge
        p_mdns = re.compile(r"^mDNS\s+Gateway\s+Status\s+:\s+(?P<value>\S+)$")

        # WIFI Alliance Agile Multiband                  : Disabled
        p_wifi_alliance = re.compile(r"^WIFI\s+Alliance\s+Agile\s+Multiband\s+:\s+(?P<value>\S+)$")

        # Device Analytics
        p_device_analytics = re.compile(r"^Device\s+Analytics$")

        # Advertise Support                          : Enabled
        p_da_advetise = re.compile(r"^Advertise\s+Support\s+:\s+(?P<value>\S+)$")

        # Share Data with Client                     : Disabled
        p_da_share = re.compile(r"^Share\s+Data\s+with\s+Client\s+:\s+(?P<value>\S+)$")

        # Client Scan Report (11k Beacon Radio Measurement)
        p_client_11k = re.compile(r"^Client\s+Scan\s+Report\s+\(11k\s+Beacon\s+Radio\s+Measurement\)$")

        # Request on Association                     : Disabled
        p_client_11k_assoc = re.compile(r"^Request\s+on\s+Association\s+:\s+(?P<value>\S+)$")

        # Request on Roam                            : Disabled
        p_client_11k_roam = re.compile(r"^Request\s+on\s+Roam\s+:\s+(?P<value>\S+)$")

        # WiFi to Cellular Steering                      : Disabled
        P_wifi_steering = re.compile(r"^WiFi\s+to\s+Cellular\s+Steering\s+:\s+(?P<value>\S+)$")


        wlan_dict = {}
        current_wlan = ""

        for line in output.splitlines():
            line = line.strip()
            if p_name.match(line):
                # WLAN Profile Name     : north
                match = p_name.match(line)
                if not wlan_dict.get("wlan_names"):
                    wlan_dict.update({ "wlan_names": {} })
                wlan_dict["wlan_names"].update({ match.group("value") : {} })
                current_wlan = match.group("value")
                continue
            elif p_delimeter.match(line):
                continue
            elif p_identifier.match(line):
                # Identifier                                     : 1
                match = p_identifier.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "identifier": int(match.group("value")) })
                continue
            elif p_description.match(line):
                # Description                                    :
                match = p_description.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "description": match.group("value") })
                continue
            elif p_name_ssid.match(line):
                # Description                                    :
                match = p_name_ssid.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "ssid": match.group("value") })
                continue
            elif p_status.match(line):
                # Status                                         : Enabled
                match = p_status.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "status": match.group("value") })
                continue
            elif p_broadcast.match(line):
                # Broadcast SSID                                 : Enabled
                match = p_broadcast.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "broadcast_ssid": match.group("value") })
                continue
            elif p_advertise.match(line):
                # Advertise-Apname                               : Disabled
                match = p_advertise.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "advertise_ap_name": match.group("value") })
                continue
            elif p_universal_admin.match(line):
                # Universal AP Admin                             : Disabled
                match = p_universal_admin.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "universal_ap_admin": match.group("value") })
                continue
            elif p_max_clients_wlan.match(line):
                # Max Associated Clients per WLAN                : 0
                match = p_max_clients_wlan.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "max_clients_wlan": int(match.group("value")) })
                continue
            elif p_max_clients_ap.match(line):
                # Max Associated Clients per AP per WLAN         : 0
                match = p_max_clients_ap.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "max_clients_ap": int(match.group("value")) })
                continue
            elif p_max_clients_radio.match(line):
                # Max Associated Clients per AP Radio per WLAN   : 200
                match = p_max_clients_radio.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "max_clients_ap_radio": int(match.group("value")) })
                continue
            elif p_max_clients_radio.match(line):
                # Max Associated Clients per AP Radio per WLAN   : 200
                match = p_max_clients_radio.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "max_clients_ap_radio": int(match.group("value")) })
                continue
            elif p_okc.match(line):
                # OKC                                            : Enabled
                match = p_okc.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "okc": match.group("value") })
                continue
            elif p_active_clients.match(line):
                # Number of Active Clients                       : 4
                match = p_active_clients.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "active_clients": int(match.group("value")) })
                continue
            elif p_chd.match(line):
                # CHD per WLAN                                   : Enabled
                match = p_chd.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "chd_per_wlan": match.group("value") })
                continue
            elif p_wmm.match(line):
                # WMM                                            : Allowed
                match = p_wmm.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "wmm": match.group("value") })
                continue
            elif p_direct_policy.match(line):
                # WiFi Direct Policy                             : Disabled
                match = p_direct_policy.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "wifi_direct_policy": match.group("value") })
                continue
            elif p_channel_scan.match(line):
                # Channel Scan Defer Priority:
                match = p_direct_policy.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "channel_scan_defer_priority": {} })
                continue
            elif p_priority.match(line):
                # Priority (default)                           : 5
                match = p_priority.match(line)
                if not wlan_dict["wlan_names"][current_wlan]["channel_scan_defer_priority"].get("priority"):
                    wlan_dict["wlan_names"][current_wlan]["channel_scan_defer_priority"].update({"priority": [] })
                wlan_dict["wlan_names"][current_wlan]["channel_scan_defer_priority"]["priority"].append(int(match.group("value")))
                continue
            elif p_scan_defer.match(line):
                # Scan Defer Time (msecs)                        : 100
                match = p_scan_defer.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "scan_defer_time_msecs": int(match.group("value")) })
                continue
            elif p_media_multi.match(line):
                # Media Stream Multicast-direct                  : Disabled
                match = p_media_multi.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "media_stream_multicast_direct": match.group("value") })
                continue
            elif p_ccx_aironet.match(line):
                # CCX - AironetIe Support                        : Disabled
                match = p_ccx_aironet.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "ccx_aironet_support": match.group("value") })
                continue
            elif p_p2p_block.match(line):
                # Peer-to-Peer Blocking Action                   : Disabled
                match = p_p2p_block.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "p2p_blocking_action": match.group("value") })
                continue
            elif p_radio_policy.match(line):
                # Radio Policy                                   : 802.11a only
                match = p_radio_policy.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "radio_policy": match.group("value") })
                continue
            elif p_dtim_a.match(line):
                # DTIM period for 802.11a radio                  :
                match = p_dtim_a.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "dtim_period_dot11a": match.group("value") })
                continue
            elif p_dtim_b.match(line):
                # DTIM period for 802.11b radio                  :
                match = p_dtim_b.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "dtim_period_dot11b": match.group("value") })
                continue
            elif p_local_eap.match(line):
                # Local EAP Authentication                       : Disabled
                match = p_local_eap.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "local_eap_authentication": match.group("value") })
                continue
            elif p_mac_filter_auth.match(line):
                # Mac Filter Authorization list name             : Disabled
                match = p_mac_filter_auth.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "mac_filter_authorization_list_name": match.group("value") })
                continue
            elif p_mac_filter_override.match(line):
                # Mac Filter Override Authorization list name    : Disabled
                match = p_mac_filter_override.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "mac_filter_override_authorization_list_name": match.group("value") })
                continue
            elif p_accounting_list.match(line):
                # Accounting list name                           :
                match = p_accounting_list.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "accounting_list_name": match.group("value") })
                continue
            elif p_dot1x_authen.match(line):
                # 802.1x authentication list name                : default
                match = p_dot1x_authen.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "dot1x_authentication_list_name": match.group("value") })
                continue
            elif p_dot1x_author.match(line):
                # 802.1x authorization list name                 : Disabled
                match = p_dot1x_author.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "dot1x_authorization_list_name": match.group("value") })
                continue
            elif p_security.match(line):
                # Security
                if not wlan_dict["wlan_names"][current_wlan].get("security"):
                    wlan_dict["wlan_names"][current_wlan].update({ "security": {} })
                continue
            elif p_dot11_authen.match(line):
                # 802.11 Authentication                      : Open System
                match = p_dot11_authen.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "dot11_authentication": match.group("value") })
                continue
            elif p_static_wep.match(line):
                # Static WEP Keys                            : Disabled
                match = p_static_wep.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "static_wep_keys": match.group("value") })
                continue
            elif p_pro_access.match(line):
                # Wi-Fi Protected Access (WPA/WPA2/WPA3)     : Enabled
                match = p_pro_access.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "wifi_protected_access_wpa1_wpa2_wpa3": match.group("value") })
                continue
            elif p_wpa_ssn.match(line):
                # WPA (SSN IE)                           : Disabled
                match = p_wpa_ssn.match(line)
                if not wlan_dict["wlan_names"][current_wlan]["security"].get("wifi_protected_access_wpa"):
                    wlan_dict["wlan_names"][current_wlan]["security"].update({ "wifi_protected_access_wpa": {} })
                wlan_dict["wlan_names"][current_wlan]["security"]["wifi_protected_access_wpa"].update({ "wpa_ssn_ie" : match.group("value") })
                continue
            elif p_wpa2_rsn.match(line):
                # WPA2 (RSN IE)                          : Enabled
                match = p_wpa2_rsn.match(line)
                if not wlan_dict["wlan_names"][current_wlan]["security"].get("wifi_protected_access_wpa2"):
                    wlan_dict["wlan_names"][current_wlan]["security"].update({ "wifi_protected_access_wpa2": {} })
                wlan_dict["wlan_names"][current_wlan]["security"]["wifi_protected_access_wpa2"].update({ "wpa2_rsn_ie" : match.group("value") })
                continue
            elif p_mpsk.match(line):
                # MPSK                               : Disabled
                match = p_mpsk.match(line)
                if not wlan_dict["wlan_names"][current_wlan]["security"]["wifi_protected_access_wpa2"].get("wpa2_attributes"):
                    wlan_dict["wlan_names"][current_wlan]["security"]["wifi_protected_access_wpa2"].update({ "wpa2_attributes": {} })
                wlan_dict["wlan_names"][current_wlan]["security"]["wifi_protected_access_wpa2"]["wpa2_attributes"].update({ "mpsk" : match.group("value") })
                continue
            elif p_aes.match(line):
                # AES Cipher                         : Enabled
                match = p_aes.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["wifi_protected_access_wpa2"]["wpa2_attributes"].update({ "aes" : match.group("value") })
                continue
            elif p_ccmp256.match(line):
                # CCMP256 Cipher                     : Disabled
                match = p_ccmp256.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["wifi_protected_access_wpa2"]["wpa2_attributes"].update({ "ccmp256" : match.group("value") })
                continue
            elif p_gcmp128.match(line):
                # GCMP128 Cipher                     : Disabled
                match = p_gcmp128.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["wifi_protected_access_wpa2"]["wpa2_attributes"].update({ "gcmp128" : match.group("value") })
                continue
            elif p_gcmp256.match(line):
                # GCMP128 Cipher                     : Disabled
                match = p_gcmp256.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["wifi_protected_access_wpa2"]["wpa2_attributes"].update({ "gcmp256" : match.group("value") })
                continue
            elif p_gtk.match(line):
                # Randomized GTK                     : Disabled
                match = p_gtk.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["wifi_protected_access_wpa2"]["wpa2_attributes"].update({ "randomized_gtk" : match.group("value") })
                continue
            elif p_wpa3.match(line):
                # WPA3 (WPA3 IE)                         : Disabled
                match = p_wpa3.match(line)
                if not wlan_dict["wlan_names"][current_wlan]["security"].get("wifi_protected_access_wpa3"):
                    wlan_dict["wlan_names"][current_wlan]["security"].update({ "wifi_protected_access_wpa3": {} })
                wlan_dict["wlan_names"][current_wlan]["security"]["wifi_protected_access_wpa3"].update({ "wpa3_ie" : match.group("value") })
                continue
            elif p_auth_key_mgmt.match(line):
                # Auth Key Management
                if not wlan_dict["wlan_names"][current_wlan]["security"].get("auth_key_mgmt"):
                    wlan_dict["wlan_names"][current_wlan]["security"].update({ "auth_key_mgmt": {} })
                continue
            elif p_key_dot1x.match(line):
                # 802.1x                             : Enabled
                match = p_key_dot1x.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["auth_key_mgmt"].update({ "dot1x": match.group("value")})
                continue
            elif p_key_psk.match(line):
                # PSK                                : Disabled
                match = p_key_psk.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["auth_key_mgmt"].update({ "psk": match.group("value")})
                continue
            elif p_key_cckm.match(line):
                # CCKM                               : Disabled
                match = p_key_cckm.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["auth_key_mgmt"].update({ "cckm": match.group("value")})
                continue
            elif p_key_ftdot1x.match(line):
                # FT dot1x                           : Disabled
                match = p_key_ftdot1x.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["auth_key_mgmt"].update({ "ft_dot1x": match.group("value")})
                continue
            elif p_key_ftpsk.match(line):
                # FT PSK                             : Disabled
                match = p_key_ftpsk.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["auth_key_mgmt"].update({ "ft_psk": match.group("value")})
                continue
            elif p_key_dot1xsha.match(line):
                # Dot1x-SHA256                       : Disabled
                match = p_key_dot1xsha.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["auth_key_mgmt"].update({ "dot1x_sha256": match.group("value")})
                continue
            elif p_key_psksha.match(line):
                # PSK-SHA256                         : Disabled
                match = p_key_psksha.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["auth_key_mgmt"].update({ "psk_sha256": match.group("value")})
                continue
            elif p_key_sae.match(line):
                # SAE                                : Disabled
                match = p_key_sae.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["auth_key_mgmt"].update({ "sae": match.group("value")})
                continue
            elif p_key_owe.match(line):
                # OWE                                : Disabled
                match = p_key_owe.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["auth_key_mgmt"].update({ "owe": match.group("value")})
                continue
            elif p_key_suiteb.match(line):
                # SUITEB-1X                          : Disabled
                match = p_key_suiteb.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["auth_key_mgmt"].update({ "suiteb_1x": match.group("value")})
                continue
            elif p_key_suiteb192.match(line):
                # SUITEB192-1X                       : Disabled
                match = p_key_suiteb192.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["auth_key_mgmt"].update({ "suiteb192_1x": match.group("value")})
                continue
            elif p_cckm_tsf.match(line):
                # CCKM TSF Tolerance                 : 1000
                match = p_cckm_tsf.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "cckm_tsf_tolerance_msecs": int(match.group("value")) })
                continue
            elif p_cckm_tsf_msec.match(line):
                # CCKM TSF Tolerance (msecs)                 : 1000
                match = p_cckm_tsf_msec.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "cckm_tsf_tolerance_msecs": int(match.group("value")) })
                continue
            elif p_owe_transition.match(line):
                # OWE Transition Mode                        : Disabled
                match = p_owe_transition.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "owe_transition_mode": match.group("value") })
                continue
            elif p_osen.match(line):
                # OSEN                                       : Disabled
                match = p_osen.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "osen": match.group("value") })
                continue
            elif p_ftsupport.match(line):
                # FT Support                                 : Adaptive
                match = p_ftsupport.match(line)
                if not wlan_dict["wlan_names"][current_wlan]["security"].get("ft_support"):
                    wlan_dict["wlan_names"][current_wlan]["security"].update({ "ft_support": {} })
                wlan_dict["wlan_names"][current_wlan]["security"]["ft_support"].update({ "ft_support_status": match.group("value")})
            elif p_ft_re_timeout_secs.match(line):
                # FT Reassociation Timeout (secs)        : 20
                match = p_ft_re_timeout_secs.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["ft_support"].update({ "ft_reassociation_timer_secs": int(match.group("value")) })
                continue
            elif p_ft_re_timeout.match(line):
                # FT Reassociation Timeout (secs)        : 20
                match = p_ft_re_timeout.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["ft_support"].update({ "ft_reassociation_timer_secs": int(match.group("value")) })
                continue
            elif p_ft_dst.match(line):
                # FT Over-The-DS mode                    : Disabled
                match = p_ft_dst.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["ft_support"].update({ "ft_over_the_ds_mode": match.group("value") })
                continue
            elif p_pmf.match(line):
                # PMF Support                                : Disabled
                match = p_pmf.match(line)
                if not wlan_dict["wlan_names"][current_wlan]["security"].get("pmf_support"):
                    wlan_dict["wlan_names"][current_wlan]["security"].update({ "pmf_support": {} })
                wlan_dict["wlan_names"][current_wlan]["security"]["pmf_support"].update({ "pmf_support_status": match.group("value") })
                continue
            elif p_association_comeback_secs.match(line):
                # PMF Association Comeback Timeout (secs): 1
                match = p_association_comeback_secs.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["pmf_support"].update({ "pmf_association_comeback_timeout_secs": int(match.group("value")) })
                continue
            elif p_association_comeback.match(line):
                match = p_association_comeback.match(line)
                # PMF Association Comeback Timeout (secs): 1
                wlan_dict["wlan_names"][current_wlan]["security"]["pmf_support"].update({ "pmf_association_comeback_timeout_secs": int(match.group("value")) })
                continue
            elif p_pmf_sa_msecs.match(line):
                # PMF SA Query Time (msecs)              : 200
                match = p_pmf_sa_msecs.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["pmf_support"].update({ "pmf_sa_query_time_msecs": int(match.group("value")) })
                continue
            elif p_pmf_sa.match(line):
                # PMF SA Query Time (msecs)              : 200
                match = p_pmf_sa.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"]["pmf_support"].update({ "pmf_sa_query_time_msecs": int(match.group("value")) })
                continue
            elif p_web_authen.match(line):
                # Web Based Authentication                   : Disabled
                match = p_web_authen.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "web_based_authenticaion": match.group("value") })
                continue
            elif p_web_redirect.match(line):
                # Conditional Web Redirect                   : Disabled
                match = p_web_redirect.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "conditional_web_redirect": match.group("value") })
                continue
            elif p_splash_page.match(line):
                # Splash-Page Web Redirect                   : Disabled
                match = p_splash_page.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "splash_page_web_redirect": match.group("value") })
                continue
            elif p_webauth_mac.match(line):
                # Webauth On-mac-filter Failure              : Disabled
                match = p_webauth_mac.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "webauth_on_mac_filter_failure": match.group("value") })
                continue
            elif p_webauthen_list.match(line):
                # Webauth Authentication List Name           : Disabled
                match = p_webauthen_list.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "webauth_authentication_list_name": match.group("value") })
                continue
            elif p_webauthor_list.match(line):
                # Webauth Authorization List Name            : Disabled
                match = p_webauthor_list.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "webauth_authorization_list_name": match.group("value") })
                continue
            elif p_webauthen_map.match(line):
                # Webauth Parameter Map                      : Disabled
                match = p_webauthen_map.match(line)
                wlan_dict["wlan_names"][current_wlan]["security"].update({ "webauth_parameter_map": match.group("value") })
                continue
            elif p_band_select.match(line):
                # Band Select                                    : Disabled
                match = p_band_select.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "band_select": match.group("value") })
                continue
            elif p_load_balancing.match(line):
                # Load Balancing                                 : Disabled
                match = p_load_balancing.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "load_balancing": match.group("value") })
                continue
            elif p_multi_buffer.match(line):
                # Multicast Buffer                               : Disabled
                match = p_multi_buffer.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "multicast_buffer": match.group("value") })
                continue
            elif p_multi_buffer_frames.match(line):
                # Multicast Buffers (frames)                     : 0
                match = p_multi_buffer_frames.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "multicast_buffer_frames": int(match.group("value")) })
                continue
            elif p_multi_buffer_size.match(line):
                # Multicast Buffer Size                          : 0
                match = p_multi_buffer_size.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "multicast_buffer_size": int(match.group("value")) })
                continue
            elif p_ip_sourceguard.match(line):
                # IP Source Guard                                : Disabled
                match = p_ip_sourceguard.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "ip_source_guard": match.group("value") })
                continue
            elif p_assisted_roaming.match(line):
                # Assisted-Roaming
                if not wlan_dict["wlan_names"][current_wlan].get("assisted_roaming"):
                    wlan_dict["wlan_names"][current_wlan].update({ "assisted_roaming": {} })
                continue
            elif p_ar_neighbor_list.match(line):
                # Neighbor List                              : Enabled
                match = p_ar_neighbor_list.match(line)
                wlan_dict["wlan_names"][current_wlan]["assisted_roaming"].update({ "neighbbor_list": match.group("value") })
                continue
            elif p_ar_prediction.match(line):
                # Prediction List                            : Disabled
                match = p_ar_prediction.match(line)
                wlan_dict["wlan_names"][current_wlan]["assisted_roaming"].update({ "prediction_list": match.group("value") })
                continue
            elif p_ar_db.match(line):
                # Dual Band Support                          : Disabled
                match = p_ar_db.match(line)
                wlan_dict["wlan_names"][current_wlan]["assisted_roaming"].update({ "dual_band_support": match.group("value") })
                continue
            elif p_ieee_11v.match(line):
                # IEEE 802.11v parameters
                if not wlan_dict["wlan_names"][current_wlan].get("ieee_dot11v_parameters"):
                    wlan_dict["wlan_names"][current_wlan].update({ "ieee_dot11v_parameters": {} })
                continue
            elif p_11v_multicast.match(line):
                # Directed Multicast Service                 : Enabled
                match = p_11v_multicast.match(line)
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"].update({ "directed_multicast_service": match.group("value") })
                continue
            elif p_11v_bss.match(line):
                # BSS Max Idle                               : Enabled
                match = p_11v_bss.match(line)
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"].update({ "bss_max_idle": {} })
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"]["bss_max_idle"].update({ "bss_max_idle_status": match.group("value") })
                continue
            elif p_11v_bss_protected.match(line):
                # Protected Mode                         : Disabled
                match = p_11v_bss_protected.match(line)
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"]["bss_max_idle"].update({ "protected_mode": match.group("value") })
                continue
            elif p_11v_filtering.match(line):
                # Traffic Filtering Service                  : Disabled
                match = p_11v_filtering.match(line)
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"].update({ "traffic_filtering_servce": match.group("value") })
                continue
            elif p_11v_bss_trans.match(line):
                # BSS Transition                             : Enabled
                match = p_11v_bss_trans.match(line)
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"].update({ "bss_transition": {}})
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"]["bss_transition"].update({ "bss_transition_status": match.group("value") })
                continue
            elif p_11v_bss_trans_disassoc.match(line):
                # Disassociation Imminent                : Disabled
                match = p_11v_bss_trans_disassoc.match(line)
                if not wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"]["bss_transition"].get("disassociation_imminent"):
                    wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"]["bss_transition"].update({ "disassociation_imminent": {} })
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"]["bss_transition"]["disassociation_imminent"].update({ "disassociation_imminent_status": match.group("value") })
                continue
            elif p_11v_bss_trans_disassoc_tbtts_extra.match(line):
                # Optimised Roaming Timer (TBTTS)    : 40
                match = p_11v_bss_trans_disassoc_tbtts_extra.match(line)
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"]["bss_transition"]["disassociation_imminent"].update({ "optimised_roaming_timer": int(match.group("value")) })
                continue
            elif p_11v_bss_trans_disassoc_timer_extra.match(line):
                # Timer (TBTTS)                      : 200
                match = p_11v_bss_trans_disassoc_timer_extra.match(line)
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"]["bss_transition"]["disassociation_imminent"].update({ "timer": int(match.group("value")) })
                continue
            elif p_11v_bss_trans_disassoc_tbtts.match(line):
                # Optimised Roaming Timer (TBTTS)    : 40
                match = p_11v_bss_trans_disassoc_tbtts.match(line)
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"]["bss_transition"]["disassociation_imminent"].update({ "optimised_roaming_timer": int(match.group("value")) })
                continue
            elif p_11v_bss_trans_disassoc_timer.match(line):
                # Timer (TBTTS)                      : 200
                match = p_11v_bss_trans_disassoc_timer.match(line)
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"]["bss_transition"]["disassociation_imminent"].update({ "timer": int(match.group("value")) })
                continue
            elif p_11v_dual_neighbor.match(line):
               # Dual Neighbor List                     : Disabled
                match = p_11v_dual_neighbor.match(line)
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"]["bss_transition"].update({ "dual_neighbor_list": match.group("value") })
                continue
            elif p_11v_wnm.match(line):
                # BSS Max Idle                               : Enabled
                match = p_11v_wnm.match(line)
                wlan_dict["wlan_names"][current_wlan]["ieee_dot11v_parameters"].update({ "wmn_sleep_mode": match.group("value") })
                continue
            elif p_11ac_mimo.match(line):
                # 802.11ac MU-MIMO                               : Enabled
                match = p_11ac_mimo.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "dot11ac_mu_mimo": match.group("value") })
                continue
            elif p_11ax_params.match(line):
                # 802.11ax parameters
                if not wlan_dict["wlan_names"][current_wlan].get("dot11ax_parameters"):
                    wlan_dict["wlan_names"][current_wlan].update({ "dot11ax_parameters": {} })
                continue
            elif p_11ax_ofdma_down.match(line):
                # OFDMA Downlink                             : Enabled
                match = p_11ax_ofdma_down.match(line)
                wlan_dict["wlan_names"][current_wlan]["dot11ax_parameters"].update({ "ofdma_downlink": match.group("value") })
                continue
            elif p_11ax_ofdma_up.match(line):
                # OFDMA Uplink                             : Enabled
                match = p_11ax_ofdma_up.match(line)
                wlan_dict["wlan_names"][current_wlan]["dot11ax_parameters"].update({ "ofdma_uplink": match.group("value") })
                continue
            elif p_11ax_mimo_down.match(line):
                # MU-MIMO Downlink                           : Enabled
                match = p_11ax_mimo_down.match(line)
                wlan_dict["wlan_names"][current_wlan]["dot11ax_parameters"].update({ "mu_mimo_downlink": match.group("value") })
                continue
            elif p_11ax_mimo_up.match(line):
                # MU-MIMO Downlink                           : Enabled
                match = p_11ax_mimo_up.match(line)
                wlan_dict["wlan_names"][current_wlan]["dot11ax_parameters"].update({ "mu_mimo_uplink": match.group("value") })
                continue
            elif p_11ax_bss.match(line):
                # BSS Target Wake Up Time                    : Enabled
                match = p_11ax_bss.match(line)
                wlan_dict["wlan_names"][current_wlan]["dot11ax_parameters"].update({ "bss_target_wake_up_time": match.group("value") })
                continue
            elif p_11ax_bss_broad.match(line):
                # BSS Target Wake Up Time                    : Enabled
                match = p_11ax_bss_broad.match(line)
                wlan_dict["wlan_names"][current_wlan]["dot11ax_parameters"].update({ "bss_target_wake_up_time_broadcast_support": match.group("value") })
                continue
            elif p_mdns.match(line):
                # mDNS Gateway Status                            : Bridge
                match = p_mdns.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "mdns_gateway_status": match.group("value") })
                continue
            elif p_wifi_alliance.match(line):
                # WIFI Alliance Agile Multiband                  : Disabled
                match = p_wifi_alliance.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "wifi_alliance_agile_multiband": match.group("value") })
                continue
            elif p_device_analytics.match(line):
                # Device Analytics
                if not wlan_dict["wlan_names"][current_wlan].get("device_analytics"):
                    wlan_dict["wlan_names"][current_wlan].update({ "device_analytics": {} })
                continue
            elif p_da_advetise.match(line):
                match = p_da_advetise.match(line)
                # Advertise Support                          : Enabled
                wlan_dict["wlan_names"][current_wlan]["device_analytics"].update({ "advertise_support": match.group("value")})
                continue
            elif p_da_share.match(line):
                match = p_da_share.match(line)
                # Share Data with Client                     : Disabled
                wlan_dict["wlan_names"][current_wlan]["device_analytics"].update({ "share_data_with_client": match.group("value")})
                continue
            elif p_client_11k.match(line):
                # Client Scan Report (11k Beacon Radio Measurement)
                if not wlan_dict["wlan_names"][current_wlan].get("client_scan_report_11k_beacon_radio_measurement"):
                    wlan_dict["wlan_names"][current_wlan].update({ "client_scan_report_11k_beacon_radio_measurement": {} })
                continue
            elif p_client_11k_assoc.match(line):
                # Request on Association                     : Disabled
                match = p_client_11k_assoc.match(line)
                wlan_dict["wlan_names"][current_wlan]["client_scan_report_11k_beacon_radio_measurement"].update({ "request_on_association": match.group("value") })
                continue
            elif p_client_11k_roam.match(line):
                # Request on Roam                            : Disabled
                match = p_client_11k_roam.match(line)
                wlan_dict["wlan_names"][current_wlan]["client_scan_report_11k_beacon_radio_measurement"].update({ "request_on_roam": match.group("value") })
                continue
            elif P_wifi_steering.match(line):
                # WiFi to Cellular Steering                      : Disabled
                match = P_wifi_steering.match(line)
                wlan_dict["wlan_names"][current_wlan].update({ "wifi_to_cellular_steering": match.group("value") })
                continue

        return wlan_dict

     

      
# ==============================
# Schema for:
#  * 'show wlan id client stats'
# ==============================
class ShowWlanIdClientStatsSchema(MetaParser):
    """Schema for show wlan id client stats."""

    schema = {
        "wlan_id": {
            int: {
                "profile_name": str,
                "current_client_state_statistics": {
                    "authenticating": int,
                    "mobility": int,
                    "ip_learn": int,
                    "webauth_pending": int,
                    "run": int,
                },
                "total_client_delete_reasons": {
                    "no_operation": int,
                    "internal_error": int,
                    "deauthentication_or_disassociation_request": int,
                    "session_manager": int,
                    "l3_authentication_failure": int,
                    "delete_received_from_ap": int,
                    "bssid_down": int,
                    "ap_down_disjoin": int,
                    "connection_timeout": int,
                    "mac_authentication_failure": int,
                    "datapath_plumb": int,
                    "due_to_ssid_change": int,
                    "due_to_vlan_change": int,
                    "due_to_ip_zone_change": int,
                    "admin_deauthentication": int,
                    "qos_failure": int,
                    "wpa_key_exchange_timeout": int,
                    "wpa_group_key_update_timeout": int,
                    "80211w_max_sa_queries_reached": int,
                    "client_deleted_during_ha_recovery": int,
                    "client_blacklist": int,
                    "inter_instance_roam_failure": int,
                    "due_to_mobility_failure": int,
                    "session_timeout": int,
                    "idle_timeout": int,
                    "supplicant_request": int,
                    "nas_error": int,
                    "policy_manager_internal_error": int,
                    "mobility_wlan_down": int,
                    "mobility_tunnel_down": int,
                    "80211v_smart_roam_failed": int,
                    "dot11v_timer_timeout": int,
                    "dot11v_association_failed": int,
                    "dot11r_pre_authentication_failure": int,
                    "sae_authentication_failure": int,
                    "dot11_failure": int,
                    "dot11_sae_invalid_message": int,
                    "dot11_unsupported_client_capabilities": int,
                    "dot11_association_denied_unspecified": int,
                    "dot11_max_sta": int,
                    "dot11_denied_data_rates": int,
                    "80211v_client_rssi_lower_than_the_association_rssi_threshold": int,
                    "invalid_qos_parameter": int,
                    "dot11_ie_validation_failed": int,
                    "dot11_group_cipher_in_ie_validation_failed": int,
                    "dot11_invalid_pairwise_cipher": int,
                    "dot11_invalid_akm": int,
                    "dot11_unsupported_rsn_version": int,
                    "dot11_invalid_rsnie_capabilities": int,
                    "dot11_received_invalid_pmkid_in_the_received_rsn_ie": int,
                    "dot11_invalid_mdie": int,
                    "dot11_invalid_ft_ie": int,
                    "dot11_qos_policy": int,
                    "dot11_ap_have_insufficient_bandwidth": int,
                    "dot11_invalid_qos_parameter": int,
                    "client_not_allowed_by_assisted_roaming": int,
                    "iapp_disassociation_for_wired_client": int,
                    "wired_wgb_change": int,
                    "wired_vlan_change": int,
                    "wired_client_deleted_due_to_wgb_delete": int,
                    "avc_client_re_anchored_at_the_foreign_controller": int,
                    "wgb_wired_client_joins_as_a_direct_wireless_client": int,
                    "ap_upgrade": int,
                    "client_dhcp": int,
                    "client_eap_timeout": int,
                    "client_8021x_failure": int,
                    "client_device_idle": int,
                    "client_captive_portal_security_failure": int,
                    "client_decryption_failure": int,
                    "client_interface_disabled": int,
                    "client_user_triggered_disassociation": int,
                    "client_miscellaneous_reason": int,
                    "unknown": int,
                    "client_peer_triggered": int,
                    "client_beacon_loss": int,
                    "client_eap_id_timeout": int,
                    "client_dot1x_timeout": int,
                    "malformed_eap_key_frame": int,
                    "eap_key_install_bit_is_not_expected": int,
                    "eap_key_error_bit_is_not_expected": int,
                    "eap_key_ack_bit_is_not_expected": int,
                    "invalid_key_type": int,
                    "eap_key_secure_bit_is_not_expected": int,
                    "key_description_version_mismatch": int,
                    "wrong_replay_counter": int,
                    "eap_key_mic_bit_expected": int,
                    "mic_validation_failed": int,
                    "error_while_ptk_computation": int,
                    "incorrect_credentials": int,
                    "client_connection_lost": int,
                    "reauthentication_failure": int,
                    "port_admin_disabled": int,
                    "supplicant_restart": int,
                    "no_ip": int,
                    "call_admission_controller_at_anchor_node": int,
                    "anchor_no_memory": int,
                    "anchor_invalid_mobility_bssid": int,
                    "anchor_creation_failure": int,
                    "db_error": int,
                    "wired_client_cleanup_due_to_wgb_roaming": int,
                    "manually_excluded": int,
                    "80211_association_failure": int,
                    "80211_authentication_failure": int,
                    "8021x_authentication_timeout": int,
                    "8021x_authentication_credential_failure": int,
                    "web_authentication_failure": int,
                    "policy_bind_failure": int,
                    "ip_theft": int,
                    "mac_theft": int,
                    "mac_and_ip_theft": int,
                    "qos_policy_failure": int,
                    "qos_policy_send_to_ap_failure": int,
                    "qos_policy_bind_on_ap_failure": int,
                    "qos_policy_unbind_on_ap_failure": int,
                    "static_ip_anchor_discovery_failure": int,
                    "vlan_failure": int,
                    "acl_failure": int,
                    "redirect_acl_failure": int,
                    "accounting_failure": int,
                    "security_group_tag_failure": int,
                    "fqdn_filter_definition_does_not_exist": int,
                    "wrong_filter_type_expected_postauth_fqdn_filter": int,
                    "wrong_filter_type_expected_preauth_fqdn_filter": int,
                    "invalid_group_id_for_fqdn_filter_valid_range": int,
                    "policy_parameter_mismatch": int,
                    "reauth_failure": int,
                    "wrong_psk": int,
                    "policy_failure": int,
                    "ap_initiated_delete_for_idle_timeout": int,
                    "ap_initiated_delete_for_client_acl_mismatch": int,
                    "ap_initiated_delete_for_ap_auth_stop": int,
                    "ap_initiated_delete_for_association_expired_at_ap": int,
                    "ap_initiated_delete_for_4_way_handshake_failed": int,
                    "ap_initiated_delete_for_dhcp_timeout": int,
                    "ap_initiated_delete_for_reassociation_timeout": int,
                    "ap_initiated_delete_for_sa_query_timeout": int,
                    "ap_initiated_delete_for_channel_switch_at_ap": int,
                    "ap_initiated_delete_for_bad_aid": int,
                    "ap_initiated_delete_for_request": int,
                    "ap_initiated_delete_for_interface_reset": int,
                    "ap_initiated_delete_for_all_on_slot": int,
                    "ap_initiated_delete_for_reaper_radio": int,
                    "ap_initiated_delete_for_slot_disable": int,
                    "ap_initiated_delete_for_mic_failure": int,
                    "ap_initiated_delete_for_vlan_delete": int,
                    "ap_initiated_delete_for_channel_change": int,
                    "ap_initiated_delete_for_stop_reassociation": int,
                    "ap_initiated_delete_for_packet_max_retry": int,
                    "ap_initiated_delete_for_transmission_deauth": int,
                    "ap_initiated_delete_for_sensor_station_timeout": int,
                    "ap_initiated_delete_for_age_timeout": int,
                    "ap_initiated_delete_for_transmission_fail_threshold": int,
                    "ap_initiated_delete_for_uplink_receive_timeout": int,
                    "ap_initiated_delete_for_sensor_scan_next_radio": int,
                    "ap_initiated_delete_for_sensor_scan_other_bssid": int,
                    "aaa_server_unavailable": int,
                    "aaa_server_not_ready": int,
                    "no_dot1x_method_configuration": int,
                    "client_abort": int,
                    "association_connection_timeout": int,
                    "mac_auth_connection_timeout": int,
                    "l2_auth_connection_timeout": int,
                    "l3_auth_connection_timeout": int,
                    "mobility_connection_timeout": int,
                    "static_ip_connection_timeout": int,
                    "sm_session_creation_timeout": int,
                    "ip_learn_connection_timeout": int,
                    "nack_ifid_exists": int,
                    "radio_down": int,
                    "eogre_reset": int,
                    "eogre_generic_join_failure": int,
                    "eogre_ha_reconciliation": int,
                    "eogre_invalid_vlan": int,
                    "eogre_invalid_domain": int,
                    "eogre_empty_domain": int,
                    "eogre_domain_shut": int,
                    "eogre_invalid_gateway": int,
                    "eogre_all_gateways_down": int,
                    "eogre_flex_no_active_gateway": int,
                    "eogre_rule_matching_error": int,
                    "eogre_aaa_override_error": int,
                    "eogre_client_onboarding_error": int,
                    "eogre_mobility_handoff_error": int,
                    "ip_update_timeout": int,
                    "l3_vlan_override_connection_timeout": int,
                    "mobility_peer_delete": int,
                    "nack_ifid_mismatch": int,
                },
            }
        }
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
            r"^Wlan Profile Name:\s+(?P<profile_name>\S+), Wlan Id: (?P<wlan_id>\d+)$"
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

            match = wlan_info_capture.match(line)
            if match:
                group = match.groupdict()

                group["wlan_id"] = int(group["wlan_id"])

                # pull a key from group to use as new_key
                new_key = "wlan_id"
                new_group = {group[new_key]: {}}

                # update and pop new_key
                new_group[group[new_key]].update(group)
                new_group[group[new_key]].pop(new_key)

                if not wlan_info_obj.get(new_key):
                    wlan_info_obj[new_key] = {}

                wlan_info_obj[new_key].update(new_group)

                current_group = wlan_info_obj[new_key][group[new_key]]

                continue

            if client_stats_capture.match(line) or client_delete_capture.match(line):
                line_format = line.replace(" ", "_").replace(":", "").lower()
                current_group.update({line_format: {}})

                header_group = current_group[line_format]

                continue

            match = key_value_capture.match(line)
            if match:
                group = match.groupdict()

                space_format_key = re.sub(r" - |\s+|-|/", "_", group["key"])
                format_key = re.sub(r"\.|,", "", space_format_key).strip("_116").lower()
                format_value =  int(group["value"])

                header_group.update({format_key: format_value})

                continue

        return wlan_info_obj

