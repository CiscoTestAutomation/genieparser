import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ==========================================
# Schema for:
#  * 'show wireless profile policy detailed'
# ==========================================
class ShowWirelessProfilePolicyDetailedSchema(MetaParser):
    """Schema for show wireless profile policy detailed."""

    schema = {
        "policy_profile_name" : str,
        "description": str,
        "status": str,
        "vlan": str,
        "multicast_vlan": str,
        Optional("wireless_mgmt_interface_vlan"): str,
        "multicast_filter": str,
        "qbss_load": str,
        "passive_client": "DISABLED",
        "et_analytics": str,
        "staticip_mobility": str,
        "wlan_switching_policy": {
            "flex_central_switching": str,
            "flex_central_authentication": str,
            "flex_central_dhcp": str,
            "flex_nat_pat": str,
            "flex_central_assoc": str
        },
        "wlan_flex_policy": {
            "vlan_based_central_switching": str
        },
        "wlan_acl": {
            "ipv4_acl": str,
            "ipv6_acl": str,
            "l2_acl": str,
            "preauth_urlfilter_list": str,
            "postauth_urlfilter_list": str
        },
        "wlan_timeout": {
            "session_timeout": int,
            "idle_timeout": int,
            "idle_threshold": int,
            "guest_timeout": str
        },
        "wlan_local_profiling": {
            "subscriber_policy_name": str,
            "radius_profiling": str,
            "http_tlv_caching": str,
            "dhcp_tlv_caching": str
        },
        "cts_policy": {
            "inline_tagging": str,
            "sgacl_enforcement": str,
            "default_sgt": int
        },
        "wlan_mobility": {
            "anchor": str
        },
        "avc_visibility": str,
        "ipv4_flow_monitors": list,
        "ipv6_flow_monitors": list,
        "nbar_protocol_discovery": str,
        "reanchoring": str,
        "classmap_for_reanchoring": {
            "classmap_name": str
        },
        "qos_per_ssid": {
            "ingress_service_name": str,
            "egress_service_name": str
        },
        "qos_per_client": {
            "ingress_service_name": str,
            "egress_service_name": str
        },
        "umbrella_information": {
            "cisco_umbrella_parameter_map": str,
            "dhcp_dns_option": str,
            "mode": str
        },
        "autoqos_mode": str,
        "call_snooping": str,
        "tunnel_profile": {
            "profile_name": str
        },
        "fabric_profile": {
            "profile_name": str
        },
        "accounting_list": {
            "accounting_list": str
        },
        "dhcp": {
            "required": str,
            "server_address": str,
            "opt82": {
                "dhcpopt82enable": str,
                "dhcpopt82ascii": str,
                "dhcpopt82rid": str,
                "apmac": str,
                "ssid": str,
                "ap_ethmac": str,
                "apname": str,
                "policy_tag": str,
                "ap_location": str,
                "vlan_id": str
            }
        },
        "exclusionlist_params": {
            "exclusionlist": str,
            "exclusiontimeout": int
        },
        "aaa_policy_params": {
            "aaa_override": str,
            "aaa_nac": str,
            "aaa_policy_name": str
        },
        "wgb_policy_params": {
            "broadcast_tagging": str
        },
        "hotspot_2.0_server-name": str,
        "mobility_anchor_list": dict,
        "mdns_gateway": {
            "mdns_service_policy_name": str
        },
        "policy_proxy_settings": {
            "arp_proxy_state": str,
            "ipv6_proxy_state": str
        },
        "airtime_fairness_profile": {
            "2.4ghz_atf_policy": str,
            "5ghz_atf_policy": str
        }
    }


# ==========================================
# Parser for:
#  * 'show wireless profile policy detailed'
# ==========================================
class ShowWirelessProfilePolicyDetailed(ShowWirelessProfilePolicyDetailedSchema):
    """Parser for show wireless profile policy detailed"""

    cli_command = 'show wireless profile policy detailed'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output=output
 
        # Policy Profile Name                 : lizzard_Fabric_F_90c67354
        # Description                         : lizzard_Fabric_F_90c67354
        # Status                              : ENABLED
        # VLAN                                : 1
        # Multicast VLAN                      : 0
        # Wireless management interface VLAN  : 10
        # Multicast Filter                    : DISABLED
        # QBSS Load                           : ENABLED
        # Passive Client                      : DISABLED
        # ET-Analytics                        : DISABLED
        # StaticIP Mobility                   : DISABLED
        # WLAN Switching Policy
        # Flex Central Switching            : DISABLED
        # Flex Central Authentication       : ENABLED
        # Flex Central DHCP                 : DISABLED
        # Flex NAT PAT                      : DISABLED
        # Flex Central Assoc                : ENABLED
        # WLAN Flex Policy
        # VLAN based Central Switching      : DISABLED
        # WLAN ACL
        # IPv4 ACL                          : Not Configured
        # IPv6 ACL                          : Not Configured
        # Layer2 ACL                        : Not Configured
        # Preauth urlfilter list            : Not Configured
        # Postauth urlfilter list           : Not Configured
        # WLAN Timeout
        # Session Timeout                   : 36000
        # Idle Timeout                      : 7200
        # Idle Threshold                    : 0
        # Guest LAN Session Timeout         : DISABLED
        # WLAN Local Profiling
        # Subscriber Policy Name            : Not Configured
        # RADIUS Profiling                  : ENABLED
        # HTTP TLV caching                  : DISABLED
        # DHCP TLV caching                  : DISABLED
        # CTS Policy
        # Inline Tagging                    : DISABLED
        # SGACL Enforcement                 : DISABLED
        # Default SGT                       : 0
        # WLAN Mobility
        # Anchor                            : DISABLED
        # AVC VISIBILITY                      : Enabled
        # IPv4 Flow Monitors
        # Ingress
        #     sc-udp-vip-001               
        # Egress
        #     sc-udp-vip-001               
        # IPv6 Flow Monitors
        # Ingress
        # Egress
        # NBAR Protocol Discovery             : Disabled
        # Reanchoring                         : Disabled
        # Classmap name for Reanchoring
        # Reanchoring Classmap Name         : Not Configured
        # QOS per SSID
        # Ingress Service Name              : platinum-up
        # Egress Service Name               : platinum
        # QOS per Client
        # Ingress Service Name              : Not Configured
        # Egress Service Name               : Not Configured
        # Umbrella information
        # Cisco Umbrella Parameter Map      : Not Configured
        # DHCP DNS Option                   : ENABLED
        # Mode                              : ignore
        # Autoqos Mode                        : None
        # Call Snooping                       : Disabled
        # Tunnel Profile
        # Profile Name                      : Not Configured
        # Calendar Profile
        # Fabric Profile
        # Profile Name                      : lizzard_Fabric_F_90c67354
        # Accounting list
        # Accounting List                   : dnac-client-radius-group
        # DHCP
        # required                          : ENABLED
        # server address                    : 0.0.0.0
        # Opt82
        # DhcpOpt82Enable                   : DISABLED
        # DhcpOpt82Ascii                    : DISABLED
        # DhcpOpt82Rid                      : DISABLED
        # APMAC                             : DISABLED
        # SSID                              : DISABLED
        # AP_ETHMAC                         : DISABLED
        # APNAME                            : DISABLED
        # POLICY TAG                        : DISABLED
        # AP_LOCATION                       : DISABLED
        # VLAN_ID                           : DISABLED
        # Exclusionlist Params
        # Exclusionlist                     : ENABLED
        # Exclusion Timeout                 : 60
        # AAA Policy Params
        # AAA Override                      : ENABLED
        # NAC                               : ENABLED
        # NAC Type                          : ISE NAC
        # AAA Policy name                   : default-aaa-policy
        # WGB Policy Params
        # Broadcast Tagging                 : DISABLED
        # Client VLAN                       : Unknown
        # Hotspot 2.0 Server name             : Not Configured
        # Mobility Anchor List
        # IP Address                                  Priority
        # -------------------------------------------------------
        # mDNS Gateway
        # mDNS Service Policy name          : default-mdns-service-policy
        # User Private Network              : Disabled
        # User Private Network Unicast Drop  : Disabled
        # Policy Proxy Settings
        # ARP Proxy State                   : DISABLED
        # IPv6 Proxy State                  : None
        # Airtime-fairness Profile
        # 2.4Ghz ATF Policy                 : default-atf-policy
        # 5Ghz ATF Policy                   : default-atf-policy
        # Policy Profile Name                 : default-policy-profile
        p_policy_profile_name = re.compile(r"^Policy\s+Profile\s+Name\s+:\s+(?P<name>\S+)$")
        # Description                         : default policy profile
        p_description = re.compile(r"^Description\s+:\s+(?P<value>.*)$")
        # Status                              : DISABLED
        p_status = re.compile(r"^Status\s+:\s+(?P<value>\S+)$")
        # VLAN                                : VLAN0100
        p_vlan = re.compile(r"^VLAN\s+:\s+(?P<value>\S+)$")
        # Multicast VLAN                      : 0
        p_multi_vlan = re.compile(r"^Multicast\s+VLAN\s+:\s+(?P<value>\S+)$")
        # OSEN client VLAN                    : 
        p_osen = re.compile(r"^OSEN\s+client\s+VLAN\s+:\s+(?P<value>.*)$")
        # Wireless management interface VLAN  : 10
        p_wireless_mgmt = re.compile(r"^Wireless\s+management\s+interface\s+VLAN\s+:\s+(?P<value>\S+)$")
        # Multicast Filter                    : DISABLED
        p_multi_filter = re.compile(r"^Multicast\s+Filter\s+:\s+(?P<value>\S+)$")
        # QBSS Load                           : ENABLED
        p_qbss = re.compile(r"^QBSS\s+Load\s+:\s+(?P<value>\S+)$")
        # Passive Client                      : DISABLED
        p_passive_client = re.compile(r"^Passive\s+Client\s+:\s+(?P<value>\S+)$")
        # ET-Analytics                        : DISABLED
        p_et_analytics = re.compile(r"^ET-Analytics\s+:\s+(?P<value>\S+)$")
        # StaticIP Mobility                   : DISABLED
        p_static_ip = re.compile(r"^StaticIP\s+Mobility\s+:\s+(?P<value>\S+)$")
        # WLAN Switching Policy
        p_wlan_switching_policy = re.compile(r"^WLAN\s+Switching\s+Policy$")
        # Flex Central Switching            : ENABLED
        p_f_central_switch = re.compile(r"^Flex\s+Central\s+Switching\s+:\s+(?P<value>\S+)$")
        # Flex Central Authentication       : ENABLED
        p_f_central_auth = re.compile(r"^Flex\s+Central\s+Authentication\s+:\s+(?P<value>\S+)$")
        # Flex Central DHCP                 : ENABLED
        p_f_central_dhcp = re.compile(r"^Flex\s+Central\s+DHCP\s+:\s+(?P<value>\S+)$")
        # Flex NAT PAT                      : DISABLED
        p_f_nat_pat = re.compile(r"^Flex\s+NAT\s+PAT\s+:\s+(?P<value>\S+)$")
        # Flex Central Assoc                : ENABLED
        p_f_central_assoc = re.compile(r"^Flex\s+Central\s+Assoc\s+:\s+(?P<value>\S+)$")
        # WLAN Flex Policy
        p_wlan_flex_policy = re.compile(r"^WLAN\s+Flex\s+Policy$")
        # VLAN based Central Switching      : DISABLED
        p_vlan_central_switching = re.compile(r"^VLAN\s+based\s+Central\s+Switching\s+:\s+(?P<value>\S+)$")
        # WLAN ACL
        p_wlan_acl = re.compile(r"^WLAN\s+ACL$")
        # IPv4 ACL                          : Not Configured
        p_ipv4_acl = re.compile(r"^IPv4\s+ACL\s+:\s+(?P<value>.*)$")
        # IPv6 ACL                          : Not Configured
        p_ipv6_acl = re.compile(r"^IPv6\s+ACL\s+:\s+(?P<value>.*)$")
        # Layer2 ACL                        : Not Configured
        p_l2_acl = re.compile(r"^Layer2\s+ACL\s+:\s+(?P<value>.*)$")
        # Preauth urlfilter list            : Not Configured
        p_pre_url_filter = re.compile(r"^Preauth\s+urlfilter\s+list\s+:\s+(?P<value>.*)$")
        # Postauth urlfilter list           : Not Configured
        p_post_url_filter = re.compile(r"^Postauth\s+urlfilter\s+list\s+:\s+(?P<value>.*)$")
        # WLAN Timeout
        p_wlan_timeout = re.compile(r"^WLAN\s+Timeout$")
        # Session Timeout                   : 1800
        p_session_timeout = re.compile(r"^Session\s+Timeout\s+:\s+(?P<value>\d+)$")
        # Idle Timeout                      : 300
        p_idle_timeout = re.compile(r"^Idle\s+Timeout\s+:\s+(?P<value>\d+)$")
        # Idle Threshold                    : 0
        p_idle_threshold = re.compile(r"^Idle\s+Threshold\s+:\s+(?P<value>\d+)$")
        # Guest LAN Session Timeout         : DISABLED
        p_guest_timeout = re.compile(r"^Guest\s+LAN\s+Session\s+Timeout\s+:\s+(?P<value>\S+)$")
        # WLAN Local Profiling
        p_wlan_local_profiling = re.compile(r"^WLAN\s+Local\s+Profiling$")
        # Subscriber Policy Name            : Not Configured
        p_subcriber_policy_name = re.compile(r"^Subscriber\s+Policy\s+Name\s+:\s+(?P<name>.*)$")
        # RADIUS Profiling                  : DISABLED
        p_radius_profiling = re.compile(r"^RADIUS\s+Profiling\s+:\s+(?P<value>\S+)$")
        # HTTP TLV caching                  : DISABLED
        p_hhtp_tlv_cache = re.compile(r"^HTTP\s+TLV\s+caching\s+:\s+(?P<value>\S+)$")
        # DHCP TLV caching                  : DISABLED
        p_dhcp_tlv_cache = re.compile(r"^DHCP\s+TLV\s+caching\s+:\s+(?P<value>\S+)$")
        # CTS Policy
        p_cts_policy = re.compile(r"^CTS\s+Policy$")
        # Inline Tagging                    : DISABLED
        p_inline_tagging = re.compile(r"^Inline\s+Tagging\s+:\s+(?P<value>\S+)$")
        # SGACL Enforcement                 : DISABLED
        p_sgacl_enforcement = re.compile(r"^SGACL\s+Enforcement\s+:\s+(?P<value>\S+)$")
        # Default SGT                       : 0
        p_default_sgt = re.compile(r"^Default\s+SGT\s+:\s+(?P<value>\d+)$")
        # WLAN Mobility
        p_wlan_mobility = re.compile(r"^WLAN\s+Mobility$")
        # Anchor                            : DISABLED
        p_anchor = re.compile(r"^Anchor\s+:\s+(?P<value>\S+)$")
        # AVC VISIBILITY                      : Disabled
        p_avc_visibility = re.compile(r"^AVC\s+VISIBILITY\s+:\s+(?P<value>\S+)$")
        # IPv4 Flow Monitors
        p_ipv4_flow = re.compile(r"^IPv4\s+Flow\s+Monitors$")
        # Ingress
        p_ingress = re.compile(r"^Ingress$")
        # Egress
        p_egress = re.compile(r"^Egress$")
        # IPv6 Flow Monitors
        p_ipv6_flow = re.compile(r"^IPv6\s+Flow\s+Monitors$")
        # Ingress
        p_ingress = re.compile(r"^Ingress$")
        # Egress
        p_egress = re.compile(r"^Egress$")
        # NBAR Protocol Discovery             : Disabled
        p_nbar = re.compile(r"^NBAR\s+Protocol\s+Discovery\s+:\s+(?P<value>\S+)$")
        # Reanchoring                         : Disabled
        p_reanchoring = re.compile(r"^Reanchoring\s+:\s+(?P<value>\S+)$")
        # Classmap name for Reanchoring
        p_reanchor_classmap = re.compile(r"^Classmap\s+name\s+for\s+Reanchoring$")
        # Reanchoring Classmap Name         : Not Configured
        p_reanchor_classmap_name = re.compile(r"^Reanchoring\s+Classmap\s+Name\s+:\s+(?P<name>.*)$")
        # QOS per SSID
        p_qos_ssid = re.compile(r"^QOS\s+per\s+SSID$")
        # Ingress Service Name              : platinum-up
        p_ingress_service_name = re.compile(r"^Ingress\s+Service\s+Name\s+:\s+(?P<name>.*)$")
        # Egress Service Name               : platinum
        p_egress_service_name = re.compile(r"^Egress\s+Service\s+Name\s+:\s+(?P<name>.*)$")
        # QOS per Client
        p_qos = re.compile(r"^QOS\s+per\s+Client$")
        # Ingress Service Name              : Not Configured
        p_ingress_service_name = re.compile(r"^Ingress\s+Service\s+Name\s+:\s+(?P<name>.*)$")
        # Egress Service Name               : Not Configured
        p_egress_service_name = re.compile(r"^Egress\s+Service\s+Name\s+:\s+(?P<name>.*)$")
        # Umbrella information
        p_umbrella = re.compile(r"^Umbrella\s+information$")
        # Cisco Umbrella Parameter Map      : Not Configured
        p_umbrella_parameter = re.compile(r"^Cisco\s+Umbrella\s+Parameter\s+Map\s+:\s+(?P<value>.*)$")
        # DHCP DNS Option                   : ENABLED
        p_umbrella_dhcp = re.compile(r"^DHCP\s+DNS\s+Option\s+:\s+(?P<value>.*)$")
        # Mode                              : ignore
        p_umbrella_mode = re.compile(r"^Mode\s+:\s+(?P<value>.*)$")
        # Autoqos Mode                        : Voice
        p_autoqos = re.compile(r"^Autoqos\s+Mode\s+:\s+(?P<value>.*)$")
        # Call Snooping                       : Disabled
        p_call_snooping = re.compile(r"^Call\s+Snooping\s+:\s+(?P<value>.*)$")
        # Tunnel Profile
        p_tunnel_profile = re.compile(r"^Tunnel\s+Profile$")
        # Profile Name                      : Not Configured
        p_profile_name = re.compile(r"^Profile\s+Name\s+:\s+(?P<name>.*)$")
        # Calendar Profile
        p_calendar_profile = re.compile(r"^Calendar\s+Profile$")
        # Fabric Profile
        p_fabric_profile = re.compile(r"^Fabric\s+Profile$")
        # Accounting list
        p_accounting = re.compile(r"^Accounting\s+list$")
        # Accounting List                   : Not Configured
        p_accounting_list = re.compile(r"^Accounting\s+List\s+:\s+(?P<value>.*)$")
        # DHCP
        p_dhcp = re.compile(r"^DHCP$")
        # required                          : DISABLED
        p_dhcp_required = re.compile(r"^required\s+:\s+(?P<value>\S+)$")
        # server address                    : 0.0.0.0
        p_dhcp_server_address = re.compile(r"^server\s+address\s+:\s+(?P<value>\S+)$")
        # Opt82
        p_dhcp_opt82 = re.compile(r"^Opt82$")
        # DhcpOpt82Enable                   : DISABLED
        p_dhcp_opt82_on = re.compile(r"^DhcpOpt82Enable\s+:\s+(?P<value>\S+)$")
        # DhcpOpt82Ascii                    : DISABLED
        p_dhcp_opt82_ascii = re.compile(r"^DhcpOpt82Ascii\s+:\s+(?P<value>\S+)$")
        # DhcpOpt82Rid                      : DISABLED
        p_dhcp_opt82_rid = re.compile(r"^DhcpOpt82Rid\s+:\s+(?P<value>\S+)$")
        # APMAC                             : DISABLED
        p_dhcp_opt82_apmac = re.compile(r"^APMAC\s+:\s+(?P<value>\S+)$")
        # SSID                              : DISABLED
        p_dhcp_opt82_ssid = re.compile(r"^SSID\s+:\s+(?P<value>\S+)$")
        # AP_ETHMAC                         : DISABLED
        p_dhcp_opt82_ethmac = re.compile(r"^AP_ETHMAC\s+:\s+(?P<value>\S+)$")
        # APNAME                            : DISABLED
        p_dhcp_opt82_apname = re.compile(r"^APNAME\s+:\s+(?P<value>\S+)$")
        # POLICY TAG                        : DISABLED
        p_dhcp_opt82_policy_tag = re.compile(r"^POLICY\s+TAG\s+:\s+(?P<value>\S+)$")
        # AP_LOCATION                       : DISABLED
        p_dhcp_opt82_ap_loc = re.compile(r"^AP_LOCATION\s+:\s+(?P<value>\S+)$")
        # VLAN_ID                           : DISABLED
        p_dhcp_opt82_vid = re.compile(r"^VLAN_ID\s+:\s+(?P<value>\S+)$")
        # Exclusionlist Params
        p_exclusion_params = re.compile(r"^Exclusionlist\s+Params$")
        # Exclusionlist                     : ENABLED
        p_exclusionlist = re.compile(r"^Exclusionlist\s+:\s+(?P<value>\S+)")
        # Exclusion Timeout                 : 60
        p_exclusion_timeout = re.compile(r"Exclusion\s+Timeout\s+:\s+(?P<value>\d+)$")
        # AAA Policy Params
        p_aaa_policy = re.compile(r"^AAA\s+Policy\s+Params$")
        # AAA Override                      : DISABLED
        p_aaa_override = re.compile(r"^AAA\s+Override\s+:\s+(?P<value>\S+)$")
        # NAC                               : DISABLED
        p_aaa_nac = re.compile(r"^NAC\s+:\s+(?P<value>\S+)$")
        # AAA Policy name                   : default-aaa-policy
        p_aaa_policy_name = re.compile(r"^AAA\s+Policy\s+name\s+:\s+(?P<name>\S+)$")
        # WGB Policy Params
        p_wgb_policy = re.compile(r"^WGB\s+Policy\s+Params$")
        # Broadcast Tagging                 : DISABLED
        p_wgb_broadcast = re.compile(r"^Broadcast\s+Tagging\s+:\s+(?P<value>\S+)$")
        # Client VLAN                       : DISABLED
        p_wgb_client_vlan = re.compile(r"^client\s+VLAN\s+:\s+(?P<value>\S+)$")
        # Hotspot 2.0 Server name             : Not Configured
        p_hotspot_name = re.compile(r"^Hotspot\s+2.0\s+Server\s+name\s+:\s+(?P<name>.*)$")
        # Mobility Anchor List
        p_mobility = re.compile(r"^Mobility\s+Anchor\s+List$")
        # IP Address                                  Priority
        p_mobility_header = re.compile(r"^IP\s+Address\s+Priority$")
        # -------------------------------------------------------
        p_mobility_delimeter = re.compile(r"^-+$")
        # 10.10.10.10                                     1
        p_mobility_clients = re.compile(r"^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<priority>\S+)$")
        # mDNS Gateway
        p_mdns = re.compile(r"^mDNS\s+Gateway$")
        # mDNS Service Policy name          : default-mdns-service-policy
        p_mdns_policy_name = re.compile(r"^mDNS\s+Service\s+Policy\s+name\s+:\s+(?P<value>.*)$")
        # User Defined (Private) Network              : Disabled
        p_user_private = re.compile(r"^User\s+Defined\s+\(Private\)\s+Network\s+:\s+(?P<value>\S+)$")
        # User Defined (Private) Network Unicast Drop  : Disabled
        p_user_private_unicast = re.compile(r"^User\s+Defined\s+\(Private\)\s+Network\s+Unicast\s+Drop\s+:\s+(?P<value>\S+)$")
        # Policy Proxy Settings
        p_policy_proxy = re.compile(r"^Policy\s+Proxy\s+Settings$")
        # ARP Proxy State                   : DISABLED
        p_policy_proxy_arp = re.compile(r"^ARP\s+Proxy\s+State\s+:\s+(?P<value>\S+)$")
        # IPv6 Proxy State                  : None
        p_policy_ipv6_proxy_arp = re.compile(r"^IPv6\s+Proxy\s+State\s+:\s+(?P<value>\S+)$")
        # Airtime-fairness Profile
        p_airtime = re.compile(r"^Airtime-fairness\s+Profile$")
        # 2.4Ghz ATF Policy                 : default-atf-policy
        p_airtime_24 = re.compile(r"^2.4Ghz\s+ATF\s+Policy\s+:\s+(?P<value>.*)$")
        # 5Ghz ATF Policy                   : default-atf-policy
        p_airtime_5 = re.compile(r"^5Ghz\s+ATF\s+Policy\s+:\s+(?P<value>.*)$")

        show_wireless_profile_policy_dict = {}
        checkline_flows = ""
        checkline_qos = ""
        checkline_profile_name = ""

        for line in output.splitlines():
            line = line.strip()
            if p_policy_profile_name.match(line):
              # Policy Profile Name                 : default-policy-profile
              match = p_policy_profile_name.match(line)
              show_wireless_profile_policy_dict.update({ "policy_profile_name" : match.group("name") })
              continue
            elif p_description.match(line):
              # Description                         : default policy profile
              match = p_description.match(line)
              show_wireless_profile_policy_dict.update({ "description" : match.group("value") })
              continue
            elif p_status.match(line):
              # Status                              : DISABLED
              match = p_status.match(line)
              show_wireless_profile_policy_dict.update({ "status" : match.group("value") })
              continue
            elif p_vlan.match(line):
              # VLAN                                : VLAN0100
              match = p_vlan.match(line)
              show_wireless_profile_policy_dict.update({ "vlan" : match.group("value") })
              continue
            elif p_multi_vlan.match(line):
              # Multicast VLAN                      : 0
              match = p_multi_vlan.match(line)
              show_wireless_profile_policy_dict.update({ "multicast_vlan" : match.group("value") })
              continue
            elif p_wireless_mgmt.match(line):
              # Wireless management interface VLAN  : 10
              match = p_wireless_mgmt.match(line)
              show_wireless_profile_policy_dict.update({ "wireless_mgmt_interface_vlan" : match.group("value") })
              continue
            elif p_osen.match(line):
              # OSEN client VLAN                    : 
              match = p_osen.match(line)
              show_wireless_profile_policy_dict.update({ "osen_client_vlan" : match.group("value") })
              continue
            elif p_multi_filter.match(line):
              # Multicast Filter                    : DISABLED
              match = p_multi_filter.match(line)
              show_wireless_profile_policy_dict.update({ "multicast_filter" : match.group("value") })
              continue
            elif p_qbss.match(line):
              # QBSS Load                           : ENABLED
              match = p_qbss.match(line)
              show_wireless_profile_policy_dict.update({ "qbss_load" : match.group("value") })
              continue
            elif p_passive_client.match(line):
              # Passive Client                      : DISABLED
              match = p_passive_client.match(line)
              show_wireless_profile_policy_dict.update({ "passive_client" : match.group("value") })
              continue
            elif p_et_analytics.match(line):
              # ET-Analytics                        : DISABLED
              match = p_et_analytics.match(line)
              show_wireless_profile_policy_dict.update({ "et_analytics" : match.group("value") })
              continue
            elif p_static_ip.match(line):
              # StaticIP Mobility                   : DISABLED
              match = p_static_ip.match(line)
              show_wireless_profile_policy_dict.update({ "staticip_mobility" : match.group("value") })
              continue
            elif p_wlan_switching_policy.match(line):
              # WLAN Switching Policy
              match = p_wlan_switching_policy.match(line)
              if not show_wireless_profile_policy_dict.get("wlan_switching_policy"):
                show_wireless_profile_policy_dict.update({ "wlan_switching_policy": {} })
              continue
            elif p_f_central_switch.match(line):
              # Flex Central Switching            : ENABLED
              match = p_f_central_switch.match(line)
              show_wireless_profile_policy_dict["wlan_switching_policy"].update({ "flex_central_switching" : match.group("value") })
              continue
            elif p_f_central_auth.match(line):
              # Flex Central Authentication       : ENABLED
              match = p_f_central_auth.match(line)
              show_wireless_profile_policy_dict["wlan_switching_policy"].update({ "flex_central_authentication" : match.group("value") })
              continue
            elif p_f_central_dhcp.match(line):
              # Flex Central DHCP                 : ENABLED
              match = p_f_central_dhcp.match(line)
              show_wireless_profile_policy_dict["wlan_switching_policy"].update({ "flex_central_dhcp" : match.group("value") })
              continue
            elif p_f_nat_pat.match(line):
              # Flex NAT PAT                      : DISABLED
              match = p_f_nat_pat.match(line)
              show_wireless_profile_policy_dict["wlan_switching_policy"].update({ "flex_nat_pat" : match.group("value") })
              continue
            elif p_f_central_assoc.match(line):
              # Flex Central Assoc                : ENABLED
              match = p_f_central_assoc.match(line)
              show_wireless_profile_policy_dict["wlan_switching_policy"].update({ "flex_central_assoc" : match.group("value") })
              continue
            elif p_wlan_flex_policy.match(line):
              # WLAN Flex Policy
              if not show_wireless_profile_policy_dict.get("wlan_flex_policy"):
                show_wireless_profile_policy_dict.update({ "wlan_flex_policy": {} })
              continue
            elif p_vlan_central_switching.match(line):
              # VLAN based Central Switching      : DISABLED
              match = p_vlan_central_switching.match(line)
              show_wireless_profile_policy_dict["wlan_flex_policy"].update({ "vlan_based_central_switching" : match.group("value") })
              continue
            # WLAN ACL
            elif p_wlan_acl.match(line):
              if not show_wireless_profile_policy_dict.get("wlan_acl"):
                show_wireless_profile_policy_dict.update({ "wlan_acl": {} })
              continue
            elif p_ipv4_acl.match(line):
              # IPv4 ACL                          : Not Configured
              match = p_ipv4_acl.match(line)
              show_wireless_profile_policy_dict["wlan_acl"].update({ "ipv4_acl" : match.group("value") })
              continue
            elif p_ipv6_acl.match(line):
              # IPv6 ACL                          : Not Configured
              match = p_ipv6_acl.match(line)
              show_wireless_profile_policy_dict["wlan_acl"].update({ "ipv6_acl" : match.group("value") })
              continue
            elif p_l2_acl.match(line):
              # Layer2 ACL                        : Not Configured
              match = p_l2_acl.match(line)
              show_wireless_profile_policy_dict["wlan_acl"].update({ "l2_acl" : match.group("value") })
              continue
            elif p_pre_url_filter.match(line):
              # Preauth urlfilter list            : Not Configured
              match = p_pre_url_filter.match(line)
              show_wireless_profile_policy_dict["wlan_acl"].update({ "preauth_urlfilter_list" : match.group("value") })
              continue
            elif p_post_url_filter.match(line):
              # Postauth urlfilter list           : Not Configured
              match = p_post_url_filter.match(line)
              show_wireless_profile_policy_dict["wlan_acl"].update({ "postauth_urlfilter_list" : match.group("value") })
              continue
            elif p_wlan_timeout.match(line):
              # WLAN Timeout
              if not show_wireless_profile_policy_dict.get("wlan_timeout"):
                show_wireless_profile_policy_dict.update({ "wlan_timeout": {} })
              continue
            elif p_session_timeout.match(line):
              # Session Timeout                   : 1800
              match = p_session_timeout.match(line)
              show_wireless_profile_policy_dict["wlan_timeout"].update({ "session_timeout": int(match.group("value")) })
              continue
            elif p_idle_timeout.match(line):
              # Idle Timeout                      : 300
              match = p_idle_timeout.match(line)
              show_wireless_profile_policy_dict["wlan_timeout"].update({ "idle_timeout": int(match.group("value")) })
              continue
            elif p_idle_threshold.match(line):
              # Idle Threshold                    : 0
              match = p_idle_threshold.match(line)
              show_wireless_profile_policy_dict["wlan_timeout"].update({ "idle_threshold": int(match.group("value")) })
              continue
            elif p_guest_timeout.match(line):
              # Guest LAN Session Timeout         : DISABLED
              match = p_guest_timeout.match(line)
              show_wireless_profile_policy_dict["wlan_timeout"].update({ "guest_timeout": match.group("value") })
              continue
            elif p_wlan_local_profiling.match(line):
              # WLAN Local Profiling
              if not show_wireless_profile_policy_dict.get("wlan_local_profiling"):
                show_wireless_profile_policy_dict.update({ "wlan_local_profiling": {} })
              continue
            elif p_subcriber_policy_name.match(line):
              # Subscriber Policy Name            : Not Configured
              match = p_subcriber_policy_name.match(line)
              show_wireless_profile_policy_dict["wlan_local_profiling"].update({ "subscriber_policy_name": match.group("name") })
              continue
            elif p_radius_profiling.match(line):
              # RADIUS Profiling                  : DISABLED
              match = p_radius_profiling.match(line)
              show_wireless_profile_policy_dict["wlan_local_profiling"].update({ "radius_profiling": match.group("value") })
              continue
            elif p_hhtp_tlv_cache.match(line):
              # HTTP TLV caching                  : DISABLED
              match = p_hhtp_tlv_cache.match(line)
              show_wireless_profile_policy_dict["wlan_local_profiling"].update({ "http_tlv_caching": match.group("value") })
              continue
            elif p_dhcp_tlv_cache.match(line):
              # DHCP TLV caching                  : DISABLED
              match = p_dhcp_tlv_cache.match(line)
              show_wireless_profile_policy_dict["wlan_local_profiling"].update({ "dhcp_tlv_caching": match.group("value") })
              continue
            elif p_cts_policy.match(line):
              # CTS Policy
              if not show_wireless_profile_policy_dict.get("cts_policy"):
                show_wireless_profile_policy_dict.update({ "cts_policy": {} })
              continue
            elif p_inline_tagging.match(line):
              # Inline Tagging                    : DISABLED
              match = p_inline_tagging.match(line)
              show_wireless_profile_policy_dict["cts_policy"].update({ "inline_tagging": match.group("value") })
              continue
            elif p_sgacl_enforcement.match(line):
              # SGACL Enforcement                 : DISABLED
              match = p_sgacl_enforcement.match(line)
              show_wireless_profile_policy_dict["cts_policy"].update({ "sgacl_enforcement": match.group("value") })
              continue
            elif p_default_sgt.match(line):
              # Default SGT                       : 0
              match = p_default_sgt.match(line)
              show_wireless_profile_policy_dict["cts_policy"].update({ "default_sgt": int(match.group("value")) })
              continue
            elif p_wlan_mobility.match(line):
              # WLAN Mobility
              if not show_wireless_profile_policy_dict.get("wlan_mobility"):
                show_wireless_profile_policy_dict.update({ "wlan_mobility": {} })
              continue
            elif p_anchor.match(line):
              # Anchor                            : DISABLED
              match = p_anchor.match(line)
              show_wireless_profile_policy_dict["wlan_mobility"].update({ "anchor": match.group("value") })
              continue
            elif p_avc_visibility.match(line):
              # AVC VISIBILITY                      : Disabled
              match = p_avc_visibility.match(line)
              show_wireless_profile_policy_dict.update({ "avc_visibility": match.group("value") })
              continue
            elif p_ipv4_flow.match(line):
              # IPv4 Flow Monitors
              checkline_flows = "ipv4"
              if not show_wireless_profile_policy_dict.get("ipv4_flow_monitors"):
                show_wireless_profile_policy_dict.update({ "ipv4_flow_monitors": [] })
              continue
            elif p_ipv6_flow.match(line):
              checkline_flows = "ipv6"
              # IPv6 Flow Monitors
              if not show_wireless_profile_policy_dict.get("ipv6_flow_monitors"):
                show_wireless_profile_policy_dict.update({ "ipv6_flow_monitors": [] })
              continue
            elif p_ingress.match(line):
              # Ingress
              if checkline_flows == "ipv4":
                show_wireless_profile_policy_dict["ipv4_flow_monitors"].append("ingress")
              elif checkline_flows == "ipv6":
                show_wireless_profile_policy_dict["ipv6_flow_monitors"].append("ingress")
              continue
            elif p_egress.match(line):
              # Egress
              if checkline_flows == "ipv4":
                show_wireless_profile_policy_dict["ipv4_flow_monitors"].append("egress")
              elif checkline_flows == "ipv6":
                show_wireless_profile_policy_dict["ipv6_flow_monitors"].append("egress")
              continue
            elif p_nbar.match(line):
              # NBAR Protocol Discovery             : Disabled
              match = p_nbar.match(line)
              show_wireless_profile_policy_dict.update({ "nbar_protocol_discovery": match.group("value") })
              continue
            elif p_reanchoring.match(line):
              # Reanchoring                         : Disabled
              match = p_reanchoring.match(line)
              show_wireless_profile_policy_dict.update({ "reanchoring": match.group("value") })
              continue
            elif p_reanchor_classmap.match(line):
              # Classmap name for Reanchoring
              if not show_wireless_profile_policy_dict.get("classmap_for_reanchoring"):
                show_wireless_profile_policy_dict.update({ "classmap_for_reanchoring": {} })
              continue
            elif p_reanchor_classmap_name.match(line):
              # Reanchoring Classmap Name         : Not Configured
              match = p_reanchor_classmap_name.match(line)
              show_wireless_profile_policy_dict["classmap_for_reanchoring"].update({ "classmap_name": match.group("name") })
              continue
            elif p_qos_ssid.match(line):
              # QOS per SSID
              checkline_qos = "ssid"
              if not show_wireless_profile_policy_dict.get("qos_per_ssid"):
                show_wireless_profile_policy_dict.update({ "qos_per_ssid": {} })
              continue
            elif p_qos.match(line):
              # QOS per Client
              checkline_qos = "client"
              if not show_wireless_profile_policy_dict.get("qos_per_client"):
                show_wireless_profile_policy_dict.update({ "qos_per_client": {} })
              continue
            elif p_ingress_service_name.match(line):
              # Ingress Service Name              : platinum-up
              match = p_ingress_service_name.match(line)
              if checkline_qos == "ssid":
                show_wireless_profile_policy_dict["qos_per_ssid"].update({ "ingress_service_name": match.group("name") })
              elif checkline_qos == "client":
                show_wireless_profile_policy_dict["qos_per_client"].update({ "ingress_service_name": match.group("name") })
              continue
            elif p_egress_service_name.match(line):
              # Egress Service Name               : platinum
              match = p_egress_service_name.match(line)
              if checkline_qos == "ssid":
                show_wireless_profile_policy_dict["qos_per_ssid"].update({ "egress_service_name": match.group("name") })
              elif checkline_qos == "client":
                show_wireless_profile_policy_dict["qos_per_client"].update({ "egress_service_name": match.group("name") })
              continue
            elif p_umbrella.match(line):
              # Umbrella information
              if not show_wireless_profile_policy_dict.get("umbrella_information"):
                show_wireless_profile_policy_dict.update({ "umbrella_information": {} })
              continue
            elif p_umbrella_parameter.match(line):
              # Cisco Umbrella Parameter Map      : Not Configured
              match = p_umbrella_parameter.match(line)
              show_wireless_profile_policy_dict["umbrella_information"].update({ "cisco_umbrella_parameter_map": match.group("value") })
              continue
            elif p_umbrella_dhcp.match(line):
              # DHCP DNS Option                   : ENABLED
              match = p_umbrella_dhcp.match(line)
              show_wireless_profile_policy_dict["umbrella_information"].update({ "dhcp_dns_option": match.group("value") })
              continue
            elif p_umbrella_mode.match(line):
              # Mode                              : ignore
              match = p_umbrella_mode.match(line)
              show_wireless_profile_policy_dict["umbrella_information"].update({ "mode": match.group("value") })
              continue
            elif p_autoqos.match(line):
              # Autoqos Mode                        : Voice
              match = p_autoqos.match(line)
              show_wireless_profile_policy_dict.update({ "autoqos_mode": match.group("value") })
              continue
            elif p_call_snooping.match(line):
              # Call Snooping                       : Disabled
              match = p_call_snooping.match(line)
              show_wireless_profile_policy_dict.update({ "call_snooping": match.group("value") })
              continue
            elif p_tunnel_profile.match(line):
              # Tunnel Profile
              checkline_profile_name = "tunnel"
              if not show_wireless_profile_policy_dict.get("tunnel_profile"):
                show_wireless_profile_policy_dict.update({ "tunnel_profile": {} })
              continue
            elif p_fabric_profile.match(line):
              # Fabric Profile
              checkline_profile_name = "fabric"
              if not show_wireless_profile_policy_dict.get("fabric_profile"):
                show_wireless_profile_policy_dict.update({ "fabric_profile": {} })
              continue
            elif p_profile_name.match(line):
              # Profile Name                      : Not Configured
              match = p_profile_name.match(line)
              if checkline_profile_name == "tunnel":
                show_wireless_profile_policy_dict["tunnel_profile"].update({ "profile_name": match.group("name")})
              elif checkline_profile_name == "fabric":
                show_wireless_profile_policy_dict["fabric_profile"].update({ "profile_name": match.group("name")})
              continue
            elif p_calendar_profile.match(line):
              # Calendar Profile
              continue
            elif p_accounting_list.match(line):
              # Accounting List                   : Not Configured
              match = p_accounting_list.match(line)
              show_wireless_profile_policy_dict["accounting_list"].update({ "accounting_list": match.group("value") })
              continue
            elif p_accounting.match(line):
              # Accounting list
              if not show_wireless_profile_policy_dict.get("accounting_list"):
                show_wireless_profile_policy_dict.update({ "accounting_list": {} })
              continue
            elif p_dhcp.match(line):
              # DHCP
              if not show_wireless_profile_policy_dict.get("dhcp"):
                show_wireless_profile_policy_dict.update({ "dhcp": {} })
              continue
            elif p_dhcp_required.match(line):
              # required                          : DISABLED
              match = p_dhcp_required.match(line)
              show_wireless_profile_policy_dict["dhcp"].update({ "required": match.group("value") })
              continue
            elif p_dhcp_server_address.match(line):
              # server address                    : 0.0.0.0
              match = p_dhcp_server_address.match(line)
              show_wireless_profile_policy_dict["dhcp"].update({ "server_address": match.group("value") })
              continue
            elif p_dhcp_opt82.match(line):
              # Opt82
              if not show_wireless_profile_policy_dict["dhcp"].get("opt82"):
                show_wireless_profile_policy_dict["dhcp"].update({ "opt82": {} })
              continue
            elif p_dhcp_opt82_on.match(line):
              # DhcpOpt82Enable                   : DISABLED
              match = p_dhcp_opt82_on.match(line)
              show_wireless_profile_policy_dict["dhcp"]["opt82"].update({ "dhcpopt82enable": match.group("value") })
              continue
            elif p_dhcp_opt82_ascii.match(line):
              # DhcpOpt82Ascii                    : DISABLED
              match = p_dhcp_opt82_ascii.match(line)
              show_wireless_profile_policy_dict["dhcp"]["opt82"].update({ "dhcpopt82ascii": match.group("value") })
              continue
            elif p_dhcp_opt82_rid.match(line):
              # DhcpOpt82Rid                      : DISABLED
              match = p_dhcp_opt82_rid.match(line)
              show_wireless_profile_policy_dict["dhcp"]["opt82"].update({ "dhcpopt82rid": match.group("value") })
              continue
            elif p_dhcp_opt82_apmac.match(line):
              # APMAC                             : DISABLED
              match = p_dhcp_opt82_apmac.match(line)
              show_wireless_profile_policy_dict["dhcp"]["opt82"].update({ "apmac": match.group("value") })
              continue
            elif p_dhcp_opt82_ssid.match(line):
              # SSID                              : DISABLED
              match = p_dhcp_opt82_ssid.match(line)
              show_wireless_profile_policy_dict["dhcp"]["opt82"].update({ "ssid": match.group("value") })
              continue
            elif p_dhcp_opt82_ethmac.match(line):
              # AP_ETHMAC                         : DISABLED
              match = p_dhcp_opt82_ethmac.match(line)
              show_wireless_profile_policy_dict["dhcp"]["opt82"].update({ "ap_ethmac": match.group("value") })
              continue
            elif p_dhcp_opt82_apname.match(line):
              # APNAME                            : DISABLED
              match = p_dhcp_opt82_apname.match(line)
              show_wireless_profile_policy_dict["dhcp"]["opt82"].update({ "apname": match.group("value") })
              continue
            elif p_dhcp_opt82_policy_tag.match(line):
              # POLICY TAG                        : DISABLED
              match = p_dhcp_opt82_policy_tag.match(line)
              show_wireless_profile_policy_dict["dhcp"]["opt82"].update({ "policy_tag": match.group("value") })
              continue
            elif p_dhcp_opt82_ap_loc.match(line):
              # AP_LOCATION                       : DISABLED
              match = p_dhcp_opt82_ap_loc.match(line)
              show_wireless_profile_policy_dict["dhcp"]["opt82"].update({ "ap_location": match.group("value") })
              continue
            elif p_dhcp_opt82_vid.match(line):
              # VLAN_ID                           : DISABLED
              match = p_dhcp_opt82_vid.match(line)
              show_wireless_profile_policy_dict["dhcp"]["opt82"].update({ "vlan_id": match.group("value") })
              continue
            elif p_exclusion_params.match(line):
              # Exclusionlist Params
              if not show_wireless_profile_policy_dict.get("exclusionlist_params"):
                show_wireless_profile_policy_dict.update({ "exclusionlist_params": {} })
              continue 
            elif p_exclusionlist.match(line):
              # Exclusionlist                     : ENABLED
              match = p_exclusionlist.match(line)
              show_wireless_profile_policy_dict["exclusionlist_params"].update({ "exclusionlist": match.group("value") })
              continue
            elif p_exclusion_timeout.match(line):
              # Exclusion Timeout                 : 60
              match = p_exclusion_timeout.match(line)
              show_wireless_profile_policy_dict["exclusionlist_params"].update({ "exclusiontimeout": int(match.group("value")) })
              continue
            elif p_aaa_policy.match(line):
              # AAA Policy Params
              if not show_wireless_profile_policy_dict.get("aaa_policy_params"):
                show_wireless_profile_policy_dict.update({ "aaa_policy_params": {} })
              continue
            elif p_aaa_override.match(line):
              # AAA Override                      : DISABLED
              match = p_aaa_override.match(line)
              show_wireless_profile_policy_dict["aaa_policy_params"].update({ "aaa_override": match.group("value") })
              continue
            elif p_aaa_nac.match(line):
              # NAC                               : DISABLED
              match = p_aaa_nac.match(line)
              show_wireless_profile_policy_dict["aaa_policy_params"].update({ "aaa_nac": match.group("value") })
              continue
            elif p_aaa_policy_name.match(line):
              # AAA Policy name                   : default-aaa-policy
              match = p_aaa_policy_name.match(line)
              show_wireless_profile_policy_dict["aaa_policy_params"].update({ "aaa_policy_name": match.group("name") })
              continue
            elif p_wgb_policy.match(line):
              # WGB Policy Params
              if not show_wireless_profile_policy_dict.get("wgb_policy_params"):
                show_wireless_profile_policy_dict.update({ "wgb_policy_params": {} })
              continue
            elif p_wgb_broadcast.match(line):
              # Broadcast Tagging                 : DISABLED
              match = p_wgb_broadcast.match(line)
              show_wireless_profile_policy_dict["wgb_policy_params"].update({ "broadcast_tagging": match.group("value") })
              continue
            elif p_wgb_client_vlan.match(line):
              # Client VLAN                       : DISABLED
              match = p_wgb_client_vlan.match(line)
              show_wireless_profile_policy_dict["wgb_policy_params"].update({ "client_vlan": match.group("value") })
              continue
            elif p_hotspot_name.match(line):
              # Hotspot 2.0 Server name             : Not Configured
              match = p_hotspot_name.match(line)
              show_wireless_profile_policy_dict.update({ "hotspot_2.0_server-name": match.group("name") })
              continue
            elif p_mobility.match(line):
              # Mobility Anchor List
              if not show_wireless_profile_policy_dict.get("mobility_anchor_list"):
                show_wireless_profile_policy_dict.update({ "mobility_anchor_list": {} })
              continue
            elif p_mobility_header.match(line):
              # IP Address                                  Priority
              continue
            elif p_mobility_clients.match(line):
              # 10.10.10.10                                    1
              match = p_mobility_clients.match(line)
              ip_address = match.group("ip")
              priority = match.group("priority")
              show_wireless_profile_policy_dict["mobility_anchor_list"].update({ "ip_address": { ip_address: {} }})
              show_wireless_profile_policy_dict["mobility_anchor_list"]["ip_address"][ip_address].update({ "priority": priority })
            elif p_mdns.match(line):
              # mDNS Gateway
              if not show_wireless_profile_policy_dict.get("mdns_gateway"):
                show_wireless_profile_policy_dict.update({ "mdns_gateway": {} })
              continue
            elif p_mdns_policy_name.match(line):
              # mDNS Service Policy name          : default-mdns-service-policy
              match = p_mdns_policy_name.match(line)
              show_wireless_profile_policy_dict["mdns_gateway"].update({ "mdns_service_policy_name": match.group("value") })
              continue
            elif p_user_private.match(line):
              # User Defined (Private) Network              : Disabled
              match = p_user_private.match(line)
              show_wireless_profile_policy_dict.update({ "user_defined_private_network": match.group("value") })
              continue
            elif p_user_private_unicast.match(line):
              # User Defined (Private) Network Unicast Drop  : Disabled
              match = p_user_private_unicast.match(line)
              show_wireless_profile_policy_dict.update({ "user_defined_private_network_unicast_drop": match.group("value") })
              continue
            elif p_policy_proxy.match(line):
              # Policy Proxy Settings
              if not show_wireless_profile_policy_dict.get("policy_proxy_settings"):
                show_wireless_profile_policy_dict.update({ "policy_proxy_settings": {} })
              continue
            elif p_policy_proxy_arp.match(line):
              # ARP Proxy State                   : DISABLED
              match = p_policy_proxy_arp.match(line)
              show_wireless_profile_policy_dict["policy_proxy_settings"].update({ "arp_proxy_state": match.group("value") })
              continue
            elif p_policy_ipv6_proxy_arp.match(line):
              # IPv6 Proxy State                  : None
              match = p_policy_ipv6_proxy_arp.match(line)
              show_wireless_profile_policy_dict["policy_proxy_settings"].update({ "ipv6_proxy_state": match.group("value") })
              continue
            elif p_airtime.match(line):
              # Airtime-fairness Profile
              if not show_wireless_profile_policy_dict.get("airtime_fairness_profile"):
                show_wireless_profile_policy_dict.update({ "airtime_fairness_profile": {} })
              continue
            elif p_airtime_24.match(line):
              # 2.4Ghz ATF Policy                 : default-atf-policy
              match = p_airtime_24.match(line)
              show_wireless_profile_policy_dict["airtime_fairness_profile"].update({ "2.4ghz_atf_policy": match.group("value") })
              continue
            elif p_airtime_5.match(line):
              # 5Ghz ATF Policy                   : default-atf-policy
              match = p_airtime_5.match(line)
              show_wireless_profile_policy_dict["airtime_fairness_profile"].update({ "5ghz_atf_policy": match.group("value") })
              continue
            
        return show_wireless_profile_policy_dict