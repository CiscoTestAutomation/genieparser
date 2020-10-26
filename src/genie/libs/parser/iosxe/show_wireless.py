import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional



# ==========================================
# Schema for:
#  * 'show wireless profile policy detailed {policy_name}'
# ==========================================
class ShowWirelessProfilePolicyDetailedSchema(MetaParser):
    """Schema for show wireless profile policy detailed {policy_name}."""

    schema = {
        "policy_profile_name" : str,
        "description": str,
        "status": str,
        "vlan": str,
        "multicast_vlan": str,
        Optional("wireless_mgmt_interface_vlan"): str,
        "multicast_filter": str,
        "qbss_load": str,
        "passive_client": str,
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
#  * 'show wireless profile policy detailed {policy_name}'
# ==========================================
class ShowWirelessProfilePolicyDetailed(ShowWirelessProfilePolicyDetailedSchema):
    """Parser for show wireless profile policy detailed {policy_name}"""

    cli_command = 'show wireless profile policy detailed {policy_name}'

    def cli(self, policy_name="",  output=None):
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
        # Egress
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


# ==============================
# Schema for:
#  * 'show wireless cts summary'
# ==============================
class ShowWirelessCtsSummarySchema(MetaParser):
    """Schema for show wireless cts summary."""

    schema = {
        "local_mode_cts_configuration": {
            "policy_profile_name": {
                Optional(Any()): {
                    Optional("sgacl_enforcement"): str,
                    Optional("inline_tagging"): str,
                    Optional("default_sgt"): int
                }
            }
        },
        "flex_mode_cts_configuration": {
            "policy_profile_name": {
                Optional(Any()): {
                    Optional("sgacl_enforcement"): str,
                    Optional("inline_tagging"): str
                }
            }
        }
    }


# ==============================
# Parser for:
#  * 'show wireless cts summary'
# ==============================
class ShowWirelessCtsSummary(ShowWirelessCtsSummarySchema):
    """Parser for show wireless cts summary"""

    cli_command = 'show wireless cts summary'
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output=output

        # Local Mode CTS Configuration
        #
        # Policy Profile Name               SGACL Enforcement     Inline-Tagging   Default-Sgt
        # ----------------------------------------------------------------------------------------
        # default-policy-profile            DISABLED              DISABLED         0
        # lizzard_Fabric_F_dee07a54        DISABLED              DISABLED         0
        # internet_Fabric_F_ed7a6bda        DISABLED              DISABLED         0
        # lizzard_l_Fabric_F_90c6dccd      DISABLED              DISABLED         0
        #
        #
        # Flex Mode CTS Configuration
        #
        # Flex Profile Name                 SGACL Enforcement     Inline-Tagging
        # -----------------------------------------------------------------------
        # default-flex-profile              DISABLED              DISABLED

        # Local Mode CTS Configuration
        p_local = re.compile(r"Local\s+Mode\s+CTS\s+Configuration$")

        # Policy Profile Name               SGACL Enforcement     Inline-Tagging   Default-Sgt
        p_local_header = re.compile(r"^Policy\s+Profile\s+Name\s+SGACL\s+Enforcement\s+Inline-Tagging\s+Default-Sgt$")

        # ----------------------------------------------------------------------------------------
        p_hyphen_delimiter = re.compile(r"^-+$")

        # wip-b60                        DISABLED              DISABLED         0
        p_local_policy = re.compile(r"^(?P<name>\S+)\s+(?P<sgacl>\S+)\s+(?P<tag>\S+)\s+(?P<sgt>\d+)$")

        # Flex Mode CTS Configuration
        p_flex = re.compile(r"^Flex\s+Mode\s+CTS\s+Configuration$")

        # Flex Profile Name                 SGACL Enforcement     Inline-Tagging
        p_flex_header = re.compile(r"^Flex\s+Profile\s+Name\s+SGACL\s+Enforcement\s+Inline-Tagging$")

        # default-flex-profile              DISABLED              DISABLED
        p_flex_policy = re.compile(r"(?P<name>\S+)\s+(?P<sgacl>\S+)\s+(?P<tag>\S+)$")


        wireless_cts_summary_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # Local Mode CTS Configuration
            if p_local.match(line):
                continue
            # Policy Profile Name               SGACL Enforcement     Inline-Tagging   Default-Sgt
            elif p_local_header.match(line):
                if not wireless_cts_summary_dict.get("local_mode_cts_configuration"):
                    wireless_cts_summary_dict.update({ "local_mode_cts_configuration": {} })
                continue
            # ----------------------------------------------------------------------------------------
            elif p_hyphen_delimiter.match(line):
                continue
            # north-policy-profile              DISABLED              DISABLED         0
            elif p_local_policy.match(line):
                match = p_local_policy.match(line)
                group = match.groupdict()
                if not wireless_cts_summary_dict["local_mode_cts_configuration"].get("policy_profile_name"):
                    wireless_cts_summary_dict["local_mode_cts_configuration"].update({ "policy_profile_name": {} })
                wireless_cts_summary_dict["local_mode_cts_configuration"]["policy_profile_name"].update({ group["name"] : {} })
                wireless_cts_summary_dict["local_mode_cts_configuration"]["policy_profile_name"][group["name"]].update({ "sgacl_enforcement": group["sgacl"],
                                                                                                                        "inline_tagging": group["tag"],
                                                                                                                        "default_sgt": int(group["sgt"])
                                                                                                                        })
                continue
            # Flex Mode CTS Configuration
            elif p_flex.match(line):
                continue
            # Flex Profile Name                 SGACL Enforcement     Inline-Tagging
            elif p_flex_header.match(line):
                if not wireless_cts_summary_dict.get("flex_mode_cts_configuration"):
                    wireless_cts_summary_dict.update({ "flex_mode_cts_configuration": {} })
                continue
            # default-flex-profile              DISABLED              DISABLED
            elif p_flex_policy.match(line):
                match = p_flex_policy.match(line)
                group = match.groupdict()
                if not wireless_cts_summary_dict["flex_mode_cts_configuration"].get("policy_profile_name"):
                    wireless_cts_summary_dict["flex_mode_cts_configuration"].update({ "policy_profile_name": {} })
                wireless_cts_summary_dict["flex_mode_cts_configuration"]["policy_profile_name"].update({ group["name"] : {} })
                wireless_cts_summary_dict["flex_mode_cts_configuration"]["policy_profile_name"][group["name"]].update({ "sgacl_enforcement": group["sgacl"],
                                                                                                                        "inline_tagging": group["tag"]
                                                                                                                        })
                continue

        return wireless_cts_summary_dict

# ========================================
# Schema for:
#  * 'show wireless fabric client summary'
# ========================================
class ShowWirelessFabricClientSummarySchema(MetaParser):
    """Schema for show wireless fabric client summary."""

    schema = {
        "number_of_fabric_clients" : int,
        Optional("mac_address") : {
            Optional(str) : {
                Optional("ap_name") : str,
                Optional("wlan") : int,
                Optional("state") : str,
                Optional("protocol") : str,
                Optional("method") : str,
            }
        }
    }

# ========================================
# Parser for:
#  * 'show wireless fabric client summary'
# ========================================
class ShowWirelessFabricClientSummary(ShowWirelessFabricClientSummarySchema):
    """Parser for show wireless fabric client summary"""

    cli_command = 'show wireless fabric client summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output=output

        show_wireless_fabric_client_summary_dict = {}


        # Number of Fabric Clients : 8

        # MAC Address    AP Name                          WLAN State              Protocol Method
        # --------------------------------------------------------------------------------------------
        # 58bf.ea72.1730 a2-11-cap43                   17   Run                11ac     Dot1x
        # 58bf.ea73.39b4 a2-11-cap50                   19   IP Learn           11n(2.4) MAB
        # 58bf.ea47.1c4c a2-11-cap52                   19   Webauth Pending    11n(2.4) MAB
        # --------------------------------------------------------------------------------------------
        # 58bf.ea47.1c59 a2-11-cap46                   17   Run                11ac     Dot1x
        # 58bf.ea41.eac4 a2-12-cap15                   19   Webauth Pending    11n(2.4) MAB
        # 58bf.eaef.9769 a2-11-cap44                   19   Webauth Pending    11n(2.4) MAB
        # --------------------------------------------------------------------------------------------
        # 58bf.ea02.5c2a a2-12-cap17                   19   Webauth Pending    11ac     MAB
        # 58bf.ea09.f357 a2-12-cap17                   19   Webauth Pending    11ac     MAB

        # Number of Fabric Clients : 8
        p_clients = re.compile(r"^Number\s+of\s+Fabric\s+Clients\s+:\s+(?P<clients>\S+)$")

        # MAC Address    AP Name                          WLAN State              Protocol Method
        p_header = re.compile(r"^MAC\s+Address\s+AP\s+Name\s+WLAN\s+State\s+Protocol\s+Method$")

        # -------------------------------------------------------------------------------------------------------------------------
        p_delimiter = re.compile(
            r"^-------------------------------------------------------------------------------------------------------------------------$")

        # 58bf.ea72.1730 a2-11-cap43                   17   Run                11ac     Dot1x
        p_client_info = re.compile(r"^(?P<mac>\S{4}\.\S{4}\.\S{4})\s+(?P<name>\S+)\s+(?P<wlan>\S+)\s+(?P<state>.*)\s+(?P<protocol>\S+)\s+(?P<method>(Dot1x|MAB))$")


        show_wireless_fabric_client_summary_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # Number of Fabric Clients : 8
            if p_clients.match(line):
                match = p_clients.match(line)
                client_count = int(match.group('clients'))
                if not show_wireless_fabric_client_summary_dict.get('number_of_fabric_clients'):
                    show_wireless_fabric_client_summary_dict.update({'number_of_fabric_clients' : client_count})
                continue
            # MAC Address    AP Name                          WLAN State              Protocol Method
            elif p_header.match(line):
                match = p_header.match(line)
                continue
            # -------------------------------------------------------------------------------------------------------------------------
            elif p_delimiter.match(line):
                match = p_delimiter.match(line)
                continue
            # 58bf.ea72.1730 a2-11-cap43                   17   Run                11ac     Dot1x
            elif p_client_info.match(line):
                match = p_client_info.match(line)
                groups = match.groupdict()
                mac_address = groups['mac']
                ap_name = groups['name']
                wlan = int(groups['wlan'])
                state = groups['state'].strip()
                protocol = groups['protocol']
                method = groups['method']
                if not show_wireless_fabric_client_summary_dict.get('mac_address'):
                    show_wireless_fabric_client_summary_dict['mac_address'] = {}
                show_wireless_fabric_client_summary_dict['mac_address'].update({mac_address : {'ap_name' : ap_name, 'wlan' : wlan, 'state' : state, 'protocol' : protocol, 'method' : method}})

        return show_wireless_fabric_client_summary_dict


# =================================
# Schema for:
#  * 'show wireless fabric summary'
# =================================
class ShowWirelessFabricSummarySchema(MetaParser):
    """Schema for show wireless fabric summary."""

    schema = {
        "fabric_status": str,
        Optional("control_plane"): {
            Optional("ip_address"): {
                Optional(str): {
                    Optional("name"): str,
                    Optional("key"): str,
                    Optional("status"): str
                }
            }
        },
        Optional("fabric_vnid_mapping"): {
            Optional("l2_vnid"): {
                Optional(int): {
                    Optional("name"): str,
                    Optional("l3_vnid"): int,
                    Optional("control_plane_name"): str,
                    Optional("ip_address"): str,
                    Optional("subnet"): str
                }
            }
        }
    }


# =================================
# Parser for:
#  * 'show wireless fabric summary'
# =================================
class ShowWirelessFabricSummary(ShowWirelessFabricSummarySchema):
    """Parser for show wireless fabric summary"""

    cli_command = 'show wireless fabric summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output=output

        # Fabric Status      : Enabled
        #
        #
        # Control-plane:
        # Name                             IP-address        Key                              Status
        # --------------------------------------------------------------------------------------------
        # default-control-plane            10.10.90.16       099fff                           Up
        # default-control-plane            10.10.90.22       099fff                           Up
        #
        #
        # Fabric VNID Mapping:
        # Name               L2-VNID        L3-VNID        IP Address             Subnet        Control plane name
        # ----------------------------------------------------------------------------------------------------------------------
        # Data                8192           0                                  0.0.0.0            default-control-plane
        # Guest               8189           0                                  0.0.0.0            default-control-plane
        # Voice               8191           0                                  0.0.0.0            default-control-plane
        # Fabric_B_INFRA_VN     8188           4097           10.10.40.0          255.255.254.0      default-control-plane
        # Physical_Security     8190           0                                  0.0.0.0            default-control-plane



        # Fabric Status      : Enabled
        p_status = re.compile(r"^Fabric\s+Status\s+:\s+(?P<status>(Enabled|Disabled))$")

        # Control-plane:
        p_control = re.compile(r"^Control-plane:$")

        # Name                             IP-address        Key                              Status
        p_header_1 = re.compile(r"^Name\s+IP-address\s+Key\s+Status$")

        # --------------------------------------------------------------------------------------------
        p_delimiter_1 = re.compile(r"^--------------------------------------------------------------------------------------------$")

        # default-control-plane            10.10.90.11       fa85ff                           Up
        p_cp_client = re.compile(r"^(?P<cp_name>\S+)\s+(?P<cp_ip_address>\S+)\s+(?P<cp_key>\S+)\s+(?P<cp_status>\S+)$")

        # Fabric VNID Mapping:
        p_vnid = re.compile(r"^Fabric\s+VNID\s+Mapping:$")

        # Name               L2-VNID        L3-VNID        IP Address             Subnet        Control plane name
        p_header_2 = re.compile(r"^Name\s+L2-VNID\s+L3-VNID\s+IP\s+Address\s+Subnet\s+Control\s+plane\s+name$")

        # ----------------------------------------------------------------------------------------------------------------------
        p_delimiter_2 = re.compile(r"^----------------------------------------------------------------------------------------------------------------------$")

        # Data                8192           0                                  0.0.0.0            default-control-plane
        p_vnid_mappings = re.compile(r"^(?P<vnid_name>\S+)\s+(?P<vnid_l2>\d+)\s+(?P<vnid_l3>\d+)\s+(?P<vnid_ip_address>\S+)\s+(?P<vnid_subnet>\S+)\s+(?P<vnid_cp_name>\S+)$")

        # Voice               8191           0                                  0.0.0.0            default-control-plane
        p_vnid_mappings_no_ip = re.compile(r"^(?P<vnid_name>\S+)\s+(?P<vnid_l2>\d+)\s+(?P<vnid_l3>\d+)\s+(?P<vnid_subnet>\S+)\s+(?P<vnid_cp_name>\S+)$")


        show_wireless_fabric_summary_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # Fabric Status      : Enabled
            if p_status.match(line):
                match = p_status.match(line)
                status = match.group("status")
                if status == "Enabled":
                    if not show_wireless_fabric_summary_dict.get("fabric_status"):
                        show_wireless_fabric_summary_dict.update({ "fabric_status" : status })
                else:
                    if not show_wireless_fabric_summary_dict.get("fabric_status"):
                        show_wireless_fabric_summary_dict.update({ "fabric_status" : status })
                continue
            # Control-plane:
            elif p_control.match(line):
                continue
            # Name                             IP-address        Key                              Status
            elif p_header_1.match(line):
                continue
            # --------------------------------------------------------------------------------------------
            elif p_delimiter_1.match(line):
                continue
            # default-control-plane            10.10.90.11       fa85ff                           Up
            elif p_cp_client.match(line):
                if not show_wireless_fabric_summary_dict.get("control_plane"):
                    show_wireless_fabric_summary_dict.update({ "control_plane" : { "ip_address" : {} }})
                match = p_cp_client.match(line)
                groups = match.groupdict()
                show_wireless_fabric_summary_dict["control_plane"]["ip_address"].update({ groups["cp_ip_address"] : { "name" : groups["cp_name"], "key": groups["cp_key"], "status" : groups["cp_status"]} })
                continue
            # Fabric VNID Mapping:
            elif p_vnid.match(line):
                if not show_wireless_fabric_summary_dict.get("fabric_vnid_mapping"):
                    show_wireless_fabric_summary_dict.update({ "fabric_vnid_mapping": { "l2_vnid" : {} }})
                continue
            # Name               L2-VNID        L3-VNID        IP Address             Subnet        Control plane name
            elif p_header_2.match(line):
                continue
            # ----------------------------------------------------------------------------------------------------------------------
            elif p_delimiter_2.match(line):
                continue
            # Fabric_B_INFRA_VN     8188           4097           10.10.40.0          255.255.254.0      default-control-plane
            elif p_vnid_mappings.match(line):
                match = p_vnid_mappings.match(line)
                groups = match.groupdict()
                show_wireless_fabric_summary_dict["fabric_vnid_mapping"]["l2_vnid"].update({ int(groups["vnid_l2"]) : { "name": groups["vnid_name"], "l3_vnid": int(groups["vnid_l3"]), "ip_address": groups["vnid_ip_address"],
                                                                                "subnet": groups["vnid_subnet"], "control_plane_name": groups["vnid_cp_name"]}})
                continue
            # Voice               8191           0                                  0.0.0.0            default-control-plane
            elif p_vnid_mappings_no_ip.match(line):
                match = p_vnid_mappings_no_ip.match(line)
                groups = match.groupdict()
                show_wireless_fabric_summary_dict["fabric_vnid_mapping"]["l2_vnid"].update({ int(groups["vnid_l2"]) : { "name": groups["vnid_name"], "l3_vnid": int(groups["vnid_l3"]), "control_plane_name": groups["vnid_name"] }})
                continue

        return show_wireless_fabric_summary_dict


# =================================
# Schema for:
#  * 'show wireless client summary'
# =================================
class ShowWirelessClientSummarySchema(MetaParser):
    """Schema for show wireless client summary."""

    schema = {
        "wireless_client_summary": {
            "wireless_client_count": int,
            Optional("included_clients"): {
                Optional(int): {
                    Optional("id"): int,
                    Optional("mac_address"): str,
                    Optional("ap_name"): str,
                    Optional("type"): str,
                    Optional("state"): str,
                    Optional("protocol"): str,
                    Optional("method"): str,
                    Optional("role"): str
                }
            },
            "wireless_excluded_client_count": int,
            Optional("excluded_clients"): {
                Optional(int): {
                    Optional("id"): int,
                    Optional("mac_address"): str,
                    Optional("ap_name"): str,
                    Optional("type"): str,
                    Optional("state"): str,
                    Optional("protocol"): str,
                    Optional("method"): str,
                    Optional("role"): str
                }
            }
        }
    }

# =================================
# Parser for:
#  * 'show wireless client summary'
# =================================
class ShowWirelessClientSummary(ShowWirelessClientSummarySchema):
    """Parser for show wireless client summary"""

    cli_command = 'show wireless client summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output

        show_wireless_client_summary_dict = {}

        # Number of Clients: 13
        #
        # MAC Address    AP Name                                        Type ID   State             Protocol Method     Role
        # -------------------------------------------------------------------------------------------------------------------------
        # 58bf.ea58.b399 b80-72-cap16                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.ea58.b463 b80-82-cap16                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.ea58.b4ae b80-12-cap17                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.ea58.b4b1 b80-32-cap13                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.ea58.b4b6 b80-42-cap13                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.ea30.90cc b80-22-cap14                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.eaa4.c601 b80-32-cap4                                  WLAN 19   IP Learn          11n(2.4) MAB        Local
        # 58bf.eae8.9e46 b80-51-cap7                                  WLAN 17   Authenticating    11ac     Dot1x      Unknown
        # 58bf.ea28.dbba b80-61-cap4                                  WLAN 17   Authenticating    11ac     Dot1x      Unknown
        # 58bf.ea32.c516 b80-62-cap1                                  WLAN 19   IP Learn          11n(5)   MAB        Local
        # 58bf.eaf0.3746 b80-12-cap14                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.eab2.9354 b80-51-cap6                                  WLAN 17   Run               11n(5)   Dot1x      Local
        # 58bf.ea15.f311 b80-61-cap4                                  WLAN 19   Webauth Pending   11n(2.4) MAB        Local
        #
        # Number of Excluded Clients: 2
        #
        # MAC Address    AP Name                          Type ID   State              Protocol Method
        # ------------------------------------------------------------------------------------------------
        # 58bf.ea8a.20e6 b80-61-cap20                   WLAN 17   Excluded           11ac     Dot1x
        # 58bf.ea37.4442 b80-62-cap14                   WLAN 17   Excluded           11ac     Dot1x

        # Number of Clients: 13
        wireless_client_count_capture = re.compile(r"^Number\s+of\s+Clients:\s+(?P<wireless_client_count>\d+)$")
        # MAC Address    AP Name                                        Type ID   State             Protocol Method     Role
        wireless_client_info_header_capture = re.compile(
            r"^MAC\s+Address\s+AP\s+Name\s+Type\s+ID\s+State\s+Protocol\s+Method\s+Role$")
        # -------------------------------------------------------------------------------------------------------------------------
        delimiter_capture = re.compile(
            r"^-------------------------------------------------------------------------------------------------------------------------$")
        # 58bf.ea58.b399 b80-72-cap16                                 WLAN 17   Run               11ac     Dot1x      Local
        wireless_client_info_capture = re.compile(
            r"^(?P<mac_address>\S+)\s+(?P<ap_name>\S+)\s+(?P<type>\S+)\s+(?P<id>\d+)\s+(?P<state>.*)\s+(?P<protocol>\S+)\s+(?P<method>(Dot1x|MAB))\s+(?P<role>\S+)$")
        # Number of Excluded Clients: 2
        wireless_excluded_client_count_capture = re.compile(
            r"^Number\s+of\s+Excluded\s+Clients:\s+(?P<wireless_excluded_client_count>\d+)$")
        # MAC Address    AP Name                          Type ID   State              Protocol Method
        exclude_client_header_capture = re.compile(
            r"^MAC\s+Address\s+AP\s+Name\s+Type\s+ID\s+State\s+Protocol\s+Method$")
        # ------------------------------------------------------------------------------------------------
        delimiter_2_capture = re.compile(
            r"^------------------------------------------------------------------------------------------------$")
        # 58bf.ea8a.20e6 b80-61-cap20                   WLAN 17   Excluded           11ac     Dot1x
        wireless_excluded_clients_info_capture = re.compile(
            r"^(?P<mac_address>\S+)\s+(?P<ap_name>\S+)\s+(?P<type>\S+)\s+(?P<id>\d+)\s+(?P<state>\S+)\s+(?P<protocol>\S+)\s+(?P<method>\S+)$")

        include_index = 0
        exclude_index = 0

        for line in output.splitlines():
            line = line.strip()
            # Number of Clients: 13
            if wireless_client_count_capture.match(line):
                wireless_client_count_capture_match = wireless_client_count_capture.match(line)
                groups = wireless_client_count_capture_match.groupdict()
                if not show_wireless_client_summary_dict.get('wireless_client_summary', {}):
                    show_wireless_client_summary_dict['wireless_client_summary'] = {}
                wireless_client_count = int(groups['wireless_client_count'])
                show_wireless_client_summary_dict['wireless_client_summary'][
                    'wireless_client_count'] = wireless_client_count
                continue
            # MAC Address    AP Name                                        Type ID   State             Protocol Method     Role
            elif wireless_client_info_header_capture.match(line):
                wireless_client_info_header_capture_match = wireless_client_info_header_capture.match(line)
                groups = wireless_client_info_header_capture_match.groupdict()
                continue
            # -------------------------------------------------------------------------------------------------------------------------
            elif delimiter_capture.match(line):
                delimiter_capture_match = delimiter_capture.match(line)
                groups = delimiter_capture_match.groupdict()
                continue
            # 58bf.ea58.b399 b80-72-cap16                                 WLAN 17   Run               11ac     Dot1x      Local
            elif wireless_client_info_capture.match(line):
                wireless_client_info_capture_match = wireless_client_info_capture.match(line)
                groups = wireless_client_info_capture_match.groupdict()
                mac_address = groups['mac_address']
                ap_name = groups['ap_name']
                type = groups['type']
                id = int(groups['id'])
                state = groups['state'].strip()
                print(state)
                protocol = groups['protocol']
                method = groups['method']
                role = groups['role']
                if not show_wireless_client_summary_dict['wireless_client_summary'].get('included_clients'):
                    show_wireless_client_summary_dict['wireless_client_summary']['included_clients'] = {}
                include_index = include_index + 1
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'].update(
                    {include_index: {}})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'id': id})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'mac_address': mac_address})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'ap_name': ap_name})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'type': type})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'id': id})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'state': state})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'protocol': protocol})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'method': method})
                show_wireless_client_summary_dict['wireless_client_summary']['included_clients'][include_index].update(
                    {'role': role})
                continue
            # Number of Excluded Clients: 2
            elif wireless_excluded_client_count_capture.match(line):
                wireless_excluded_client_count_capture_match = wireless_excluded_client_count_capture.match(line)
                groups = wireless_excluded_client_count_capture_match.groupdict()
                wireless_excluded_client_count = int(groups['wireless_excluded_client_count'])
                show_wireless_client_summary_dict['wireless_client_summary'][
                    'wireless_excluded_client_count'] = wireless_excluded_client_count
                continue
            # MAC Address    AP Name                          Type ID   State              Protocol Method
            elif exclude_client_header_capture.match(line):
                exclude_client_header_capture_match = exclude_client_header_capture.match(line)
                groups = exclude_client_header_capture_match.groupdict()
                continue
            # ------------------------------------------------------------------------------------------------
            elif delimiter_2_capture.match(line):
                delimiter_2_capture_match = delimiter_2_capture.match(line)
                groups = delimiter_2_capture_match.groupdict()
                continue
            # 58bf.ea8a.20e6 b80-61-cap20                   WLAN 17   Excluded           11ac     Dot1x
            elif wireless_excluded_clients_info_capture.match(line):
                wireless_excluded_clients_info_capture_match = wireless_excluded_clients_info_capture.match(line)
                groups = wireless_excluded_clients_info_capture_match.groupdict()
                mac_address = groups['mac_address']
                ap_name = groups['ap_name']
                type = groups['type']
                id = int(groups['id'])
                state = groups['state'].strip()
                protocol = groups['protocol']
                method = groups['method']
                if not show_wireless_client_summary_dict['wireless_client_summary'].get('excluded_clients'):
                    show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'] = {}
                exclude_index = exclude_index + 1
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'].update(
                    {exclude_index: {}})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'id': id})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'mac_address': mac_address})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'ap_name': ap_name})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'type': type})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'id': id})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'state': state})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'protocol': protocol})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'method': method})
                show_wireless_client_summary_dict['wireless_client_summary']['excluded_clients'][exclude_index].update(
                    {'role': role})
                continue

        return show_wireless_client_summary_dict


# ===================================
# Schema for:
#  * 'show wireless mobility ap-list'
# ===================================
class ShowWirelessMobilityApListSchema(MetaParser):
    """Schema for show wireless mobility ap-list."""

    schema = {
        "ap_name": {
            Any(): {
                "ap_radio_mac": str,
                "controller_ip": str,
                "learnt_from": str,
            }
        }
    }


# ===================================
# Parser for:
#  * 'show wireless mobility ap-list'
# ===================================
class ShowWirelessMobilityApList(ShowWirelessMobilityApListSchema):
    """Parser for show wireless mobility ap-list"""

    cli_command = "show wireless mobility ap-list"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output

        # AP name                           AP radio MAC      Controller IP     Learnt from
        # --------------------------------------------------------------------------------------
        # b80-72-cap30                    58bf.eab3.1420    10.10.7.177      Self
        # b80-81-cap4                     58bf.ea13.62a0    10.10.7.177      Self
        # b80-52-cap6                     58bf.ea13.75e0    10.10.7.177      Self

        # AP name                           AP radio MAC      Controller IP     Learnt from
        ap_header_capture = re.compile(
            r"^AP\s+name\s+AP\s+radio\s+MAC\s+Controller\s+IP\s+Learnt\s+from$"
        )

        # b80-72-cap30                    58bf.eab3.1420    10.10.7.177      Self
        ap_info_capture = re.compile(
            r"^(?P<ap_name>\S+)\s+(?P<ap_radio_mac>\S{4}\.\S{4}\.\S{4})\s+(?P<controller_ip>\d+\.\d+\.\d+\.\d+)\s+(?P<learnt_from>\S+)$"
        )

        ap_info_obj = {}

        for line in output.splitlines():

            line = line.strip()

            if ap_header_capture.match(line):
                continue

            elif ap_info_capture.match(line):
                ap_info_capture_match = ap_info_capture.match(line)
                groups = ap_info_capture_match.groupdict()

                if not ap_info_obj.get("ap_name", {}):
                    ap_info_obj["ap_name"] = {}

                ap_name_dict = {
                    # ap_name: b80-72-cap30
                    groups["ap_name"]: {
                        # radio_mac: 58bf.eab3.1420
                        "ap_radio_mac": groups["ap_radio_mac"],
                        # controller_ip: 10.10.7.177
                        "controller_ip": groups["controller_ip"],
                        # learnt_from: Self
                        "learnt_from": groups["learnt_from"],
                    }
                }

                ap_info_obj["ap_name"].update(ap_name_dict)

        return ap_info_obj


# ===================================
# Schema for:
#  * 'show wireless mobility summary'
# ===================================
class ShowWirelessMobilitySummarySchema(MetaParser):
    """Schema for show wireless mobility summary."""

    schema = {
        "controller_config": {
            "group_name": str,
            "ipv4": str,
            "mac_address": str,
            "multicast_ipv4": str,
            "multicast_ipv6": str,
            "pmtu": str,
            "public_ip": str,
            "status": str,
        },
        "mobility_summary": {
            "domain_id": str,
            "dscp_value": str,
            "group_name": str,
            "keepalive": str,
            "mac_addr": str,
            "mgmt_ipv4": str,
            "mgmt_ipv6": str,
            "mgmt_vlan": str,
            "multi_ipv4": str,
            "multi_ipv6": str,
        },
    }


# ===================================
# Parser for:
#  * 'show wireless mobility summary'
# ===================================
class ShowWirelessMobilitySummary(ShowWirelessMobilitySummarySchema):
    """Parser for show wireless mobility summary"""

    cli_command = "show wireless mobility summary"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        else:
            output = output

        # Mobility Summary

        # Wireless Management VLAN: 299
        # Wireless Management IP Address: 10.10.7.177
        # Wireless Management IPv6 Address:
        # Mobility Control Message DSCP Value: 48
        # Mobility Keepalive Interval/Count: 10/3
        # Mobility Group Name: b80-mobility
        # Mobility Multicast Ipv4 address: 0.0.0.0
        # Mobility Multicast Ipv6 address: ::
        # Mobility MAC Address: 58bf.ea35.b60b
        # Mobility Domain Identifier: 0x61b3

        # Controllers configured in the Mobility Domain:

        # IP                                        Public Ip                                  MAC Address         Group Name                       Multicast IPv4    Multicast IPv6                              Status                       PMTU
        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 10.10.7.177                               N/A                                        58bf.ea35.b60b      b80-mobility                0.0.0.0           ::                                          N/A                          N/A

        # Mobility Summary
        mobility_summary_capture = (
            r"^"
            # Wireless Management VLAN: 299
            r"Wireless Management VLAN:\s+(?P<mgmt_vlan>\S+)\n+"
            # Wireless Management IP Address: 10.10.7.177
            r"Wireless Management IP Address:\s+(?P<mgmt_ipv4>\d+\.\d+\.\d+\.\d+)\n+"
            # Wireless Management IPv6 Address:
            r"Wireless Management IPv6 Address:\s+(?P<mgmt_ipv6>\S*)\n+"
            # Mobility Control Message DSCP Value: 48
            r"Mobility Control Message DSCP Value:\s+(?P<dscp_value>\S+)\n+"
            # Mobility Keepalive Interval/Count: 10/3
            r"Mobility Keepalive Interval/Count:\s+(?P<keepalive>\S+)\n+"
            # Mobility Group Name: b80-mobility
            r"Mobility Group Name:\s+(?P<group_name>\S+)\n+"
            # Mobility Multicast Ipv4 address: 0.0.0.0
            r"Mobility Multicast Ipv4 address:\s+(?P<multi_ipv4>\d+\.\d+\.\d+\.\d+)\n+"
            # Mobility Multicast Ipv6 address: ::
            r"Mobility Multicast Ipv6 address:\s+(?P<multi_ipv6>\S+)\n+"
            # Mobility MAC Address: 58bf.ea35.b60b
            r"Mobility MAC Address:\s+(?P<mac_addr>\S{4}\.\S{4}\.\S{4})\n+"
            # Mobility Domain Identifier: 0x61b3
            r"Mobility Domain Identifier:\s+(?P<domain_id>\S+)"
        )

        # Controllers configured in the Mobility Domain:
        controller_config_capture = (
            r"^"
            # 10.10.7.177
            r"(?P<ipv4>\d+\.\d+\.\d+\.\d+)\s+"
            # N/A
            r"(?P<public_ip>\S+)\s+"
            # 58bf.ea35.b60b
            r"(?P<mac_address>\S{4}\.\S{4}\.\S{4})\s+"
            # b80-mobility
            r"(?P<group_name>\S+)\s+"
            # 0.0.0.0
            r"(?P<multicast_ipv4>\d+\.\d+\.\d+\.\d+)\s+"
            # ::
            r"(?P<multicast_ipv6>\S+)\s+"
            # N/A
            r"(?P<status>\S+)\s+"
            # N/A
            r"(?P<pmtu>\S+)\s+$"
        )

        mobility_info_obj = {}

        info_dict_keys = ["mobility_summary", "controller_config"]
        info_captures = [mobility_summary_capture, controller_config_capture]

        for key, capture in zip(info_dict_keys, info_captures):

            info_search = re.search(capture, output, re.MULTILINE)

            if info_search:
                info_group = info_search.groupdict()
                mobility_info_obj[key] = info_group

        return mobility_info_obj


# =========================================
# Schema for:
#  * 'show wireless profile policy summary'
# =========================================
class ShowWirelessProfilePolicySummarySchema(MetaParser):
    """Schema for show wireless profile policy summary."""

    schema = {
        "policy_count": int,
        "policy_name": {
            Any(): {
              "description": str,
              "status": str
            },
        }
    }

# =========================================
# Parser for:
#  * 'show wireless profile policy summary'
# =========================================
class ShowWirelessProfilePolicySummary(ShowWirelessProfilePolicySummarySchema):
    """Parser for show wireless profile policy summary"""

    cli_command = ['show wireless profile policy summary']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
        else:
            output = output

        # Number of Policy Profiles: 31

        # Policy Profile Name               Description                             Status
        # -----------------------------------------------------------------------------------------
        # wip-b60                        b60-voice                             ENABLED
        # wip-b70                        b70-voice                             ENABLED
        # wip-b80                        b80-voice                             ENABLED
        # lizzard_b60                    b60-lizzard/legacy                   ENABLED
        # lizzard_b70                    b70-lizzard/legacy                   ENABLED
        # lizzard_b80                    b80-lizzard/legacy                   ENABLED
        # internet-b60                    b60-guest                             ENABLED
        # internet-b70                    b70-guest                             ENABLED
        # internet-b80                    b80-guest                             ENABLED
        # lizzard_b70_1                  Not required                            ENABLED

        # Number of Policy Profiles: 31
        policy_count_capture = re.compile(r"^Number of Policy Profiles:\s+(?P<policy_count>\d+)$")

        # wip-b60                        b60-voice                             ENABLED
        policy_info_capture = re.compile(
            # wip-b60
            r"^(?P<policy_name>\S+)\s+"
            # b60-voice
            r"(?P<description>Not required|default policy profile|\S+)\s+"
            # ENABLED
            r"(?P<status>ENABLED|DISABLED)$"
        )

        policy_info_obj = {}

        for line in output.splitlines():
            line = line.strip()

            if policy_count_capture.match(line):
                policy_count_match = policy_count_capture.match(line)

                # only grab the first entry from output
                if not policy_info_obj.get("policy_count"):
                    group = policy_count_match.groupdict()

                    # convert value from str to int
                    policy_count_dict = {"policy_count": int(group["policy_count"])}

                    policy_info_obj.update(policy_count_dict)

            if policy_info_capture.match(line):
                policy_info_match = policy_info_capture.match(line)
                group = policy_info_match.groupdict()

                policy_info_dict = {group["policy_name"]: {}}
                policy_info_dict[group["policy_name"]].update(group)
                policy_info_dict[group["policy_name"]].pop("policy_name")

                if not policy_info_obj.get("policy_name"):
                    policy_info_obj["policy_name"] = {}

                policy_info_obj["policy_name"].update(policy_info_dict)

        return policy_info_obj


# ===================================
# Schema for:
#  * 'show wireless stats ap join summary'
# ========================================
class ShowWirelessStatsApJoinSummarySchema(MetaParser):
    """Schema for show wireless stats ap join summary."""

    schema = {
        "ap_count": int,
        "base_mac": {
            Any(): {
                "ap_name": str,
                "disconnect_reason": str,
                "failure_phase": str,
                "ip_address": str,
                "status": str,
                "visitors_mac": str,
            }
        },
    }

# ========================================
# Parser for:
#  * 'show wireless stats ap join summary'
# ========================================
class ShowWirelessStatsApJoinSummary(ShowWirelessStatsApJoinSummarySchema):
    """Parser for show wireless stats ap join summary"""

    cli_command = ["show wireless stats ap join summary"]

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Number of APs: 61

        # Base MAC        visitors MAC    AP Name                           IP Address                                Status      Last Failure Phase    Last Disconnect Reason
        # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 706d.0598.6fc0  706d.0598.0320  AP706d.0598.0320                  10.10.116.22                             Not Joined  Join                  Ap auth pending
        # 706d.0544.d2c0  706d.0544.1bf0  visitors-hydra                    10.10.78.156                              Not Joined  Join                  Ap auth pending
        # 706d.0544.d580  706d.0544.1ca0  visitors-hydra                    10.10.82.200                             Not Joined  Join                  Ap auth pending
        # 0042.5a0a.1fb0  006b.f116.0ff0  visitors-1815i                     10.10.139.90                             Joined      Join                  Ap auth pending
        # 706d.0593.aac0  706d.0592.5148  visitors-hydra2                   10.10.36.138                               Not Joined  Join                  Ap auth pending
        # 706d.0593.ae20  706d.0592.5220  visitors-hydra5                   10.10.36.138                               Not Joined  Join                  Ap auth pending
        # 00be.7506.42c0  706d.0568.44d0  visitors-1815t                      10.10.236.197                            Joined      Join                  Ap auth pending
        # 706d.05be.6890  706d.053e.e3f0  visitors-1815i                    10.10.152.239                            Joined      Join                  Ap auth pending
        # 706d.05be.adc0  706d.053e.f540  visitors-mallorca                  10.10.40.15                              Not Joined  Join                  Ap auth pending
        # 706d.05be.bc20  706d.053e.f8d8  visitors-mallorca                  10.10.7.234                              Not Joined  Join                  Ap auth pending

        # Number of APs: 61
        ap_count_capture = re.compile(r"^Number of APs:\s+(?P<ap_count>\d+)$")

        # 706d.0598.6fc0  706d.0598.0320  AP706d.0598.0320                  10.10.116.22                             Not Joined  Join                  Ap auth pending
        ap_join_capture = re.compile(
            # 706d.0598.6fc0
            r"^(?P<base_mac>[a-f0-9]{4}\.[a-f0-9]{4}\.[a-f0-9]{4})\s+"
            # 706d.0598.0320
            r"(?P<visitors_mac>[a-f0-9]{4}\.[a-f0-9]{4}\.[a-f0-9]{4})\s+"
            # AP706d.0598.0320
            r"(?P<ap_name>\S+)\s+"
            # 10.10.116.22
            r"(?P<ip_address>[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\s+"
            # Not Joined
            r"(?P<status>Not Joined|Joined)\s+"
            # Join
            r"(?P<failure_phase>\S+)\s+"
            # Ap auth pending
            r"(?P<disconnect_reason>.*)$"
        )

        wireless_info_obj = {}

        for line in out.splitlines():
            line = line.strip()
            if ap_count_capture.match(line):
                # only grab the first entry from output
                if not wireless_info_obj.get("ap_count"):
                    ap_count_match = ap_count_capture.match(line)
                    group = ap_count_match.groupdict()
                    # convert value from str to int
                    ap_count_dict = {"ap_count": int(group["ap_count"])}
                    wireless_info_obj.update(ap_count_dict)
            if ap_join_capture.match(line):
                ap_join_match = ap_join_capture.match(line)
                group = ap_join_match.groupdict()
                # pull the base_mac to use as key then pop it from the dict
                ap_info_dict = {group["base_mac"]: {}}
                ap_info_dict[group["base_mac"]].update(group)
                ap_info_dict[group["base_mac"]].pop("base_mac")
                if not wireless_info_obj.get("base_mac"):
                    wireless_info_obj["base_mac"] = {}
                wireless_info_obj["base_mac"].update(ap_info_dict)

        return wireless_info_obj


# ====================================
# Schema for:
#  * 'show wireless client mac {mac_address} detail'
# ====================================
class ShowWirelessClientMacDetailSchema(MetaParser):
    """Schema for show wireless client mac {mac_address} detail."""

    schema = {
          "client_mac_address": str,
          "client_mac_type": str,
          "client_ipv4_address": str,
          "client_ipv6_addresses": str,
          "client_username": str,
          "ap_mac_address": str,
          "ap_name": str,
          "ap_slot": int,
          "client_state": str,
          "policy_profile": str,
          "flex_profile": str,
          "wireless_lan_id": int,
          "wlan_profile_name": str,
          "wireless_lan_network_name_ssid": str,
          "bssid": str,
          "connected_for_seconds": int,
          "protocol": str,
          "channel": int,
          "client_iif_id": str,
          "association_id": int,
          "authentication_alogrithm": str,
          "idle_state_timeout": str,
          "re_authentication_timeout_secs": {
              "configured": int,
              "remaining_time": int
          },
          "input_policy_name": str,
          "input_policy_state": str,
          "input_policy_source": str,
          "output_policy_name": str,
          "output_policy_state": str,
          "output_policy_source": str,
          "wmm_support": str,
          "u_apsd_support": {
              "status": str,
              "u_apsd_value": int,
              "apsd_acs": list
          },
          "fastlane_support": str,
          "client_active_state": str,
          "power_save": str,
          "current_rate": float,
          "supported_rates": list,
          "mobility": {
              "move_count": int,
              "mobility_role": str,
              "mobility_roam_type": str,
              Optional("mobility_complete_timestamp"): {
                  Optional("date"): str,
                  Optional("time"): str,
                  Optional("timezone"): str
              }
          },
          "client_join_time": {
              "date": str,
              "time": str,
              "timezone": str
          },
          "client_state_servers": str,
          "client_acls": str,
          "policy_manager_state": str,
          "last_policy_manager_state": str,
          "client_entry_create_time_secs": int,
          "policy_type": str,
          "encryption_cipher": str,
          "authentication_key_management": str,
          "user_defined_private_network": str,
          "user_defined_private_network_drop_unicast": str,
          "encrypted_traffic_analytics": str,
          "protected_management_frame__802.11w": str,
          "eap_type": str,
          "vlan_override_after_webauth": str,
          "vlan": str,
          "multicast_vlan": int,
          "wifi_direct_capabilities": {
              "wifi_direct_capable": str
          },
          "central_nat": str,
          "session_manager": {
              "point_of_attachment": str,
              "iif_id": str,
              "authorized": str,
              "session_timeout": int,
              "common_session_id": str,
              "acct_session_id": str,
              "last_tried_aaa_server_details": {
                  "server_ip": str
              },
              "auth_method_status_list": {
                  "method": str,
                  "sm_state": str,
                  "sm_bend_state": str
              },
              "local_policies": {
                  "service_template": str,
                  "vlan_group": str,
                  "absolute_timer": int
              },
              "server_policies": {
                  "output_sgt": str
              },
              "resultant_policies": {
                  "output_sgt": str,
                  "vlan_name": str,
                  "vlan_group": str,
                  "vlan": int,
                  "absolute_timer": int
              }
          },
          "dns_snooped_ipv4_addresses": str,
          "dns_snooped_ipv6_addresses": str,
          "client_capabilities": {
              "cf_pollable": str,
              "cf_poll_request": str,
              "short_preamble": str,
              "pbcc": str,
              "channel_agility": str,
              "listen_interval": int
          },
          "fast_bss_transition_details": {
              "reassociation_timeout": int
          },
          "11v_bss_transition": str,
          "11v_dms_capable": str,
          "qos_map_capable": str,
          "flexconnect_data_switching": str,
          "flexconnect_dhcp_status": str,
          "flexconnect_authentication": str,
          "flexconnect_central_association": str,
          "client_statistics": {
              "number_of_bytes_received": int,
              "number_of_bytes_sent": int,
              "number_of_packets_received": int,
              "number_of_packets_sent": int,
              "number_of_policy_errors": int,
              "radio_signal_strength_indicator_dbm": str,
              "signal_to_noise_ration_db": int
          },
          "fabric_status": "Disabled",
          "radio_measurement_enabled_capabilities": {
              "capabilities": list
          },
          "client_scan_report": str,
          "nearby_ap_statistics": {
              "ap_names": dict
          },
          "eogre": str,
          "device_info": {
              "device_type": str,
              "device_name": str,
              "protocol_map": str,
              "device_os": str,
              "protocols": list
          },
          "max_client_protocol_capability": str,
          "cellular_capability": str
          }


# ====================================
# Parser for:
#  * 'show wireless client mac {mac_address} detail'
# ====================================
class ShowWirelessClientMacDetail(ShowWirelessClientMacDetailSchema):
    """Parser for show wireless client mac {mac_address} detail"""

    cli_command = 'show wireless client mac detail'

    def change_data_type(self, value):
        if value.isdigit():
            value = value.strip()
            value = int(value)
        else:
            try:
                # Change strings to float if possible
                value = float(value)
            except ValueError:
                # if the value is not an int or float, leave it as a string.
                pass
        return value

    def cli(self, mac_address="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mac_address=mac_address))
        else:
          output = output


        # Client MAC Address : 0aba.dd93.ac36
        # Client MAC Type : Locally Administered Address
        # Client IPv4 Address : 10.22.4.19
        # Client IPv6 Addresses : fe80::8ba:ddff:fe93:ac36
        # Client Username : aking
        # AP MAC Address : 70b3.1875.7f00
        # AP Name: b1-11-cap9
        # AP slot : 0
        # Client State : Associated
        # Policy Profile : lizzard_b1
        # Flex Profile : N/A
        # Wireless LAN Id: 20
        # WLAN Profile Name: lizzard-l_Global
        # Wireless LAN Network Name (SSID): lizzard-legacy
        # BSSID : 70b3.1875.7f03
        # Connected For : 3233 seconds
        # Protocol : 802.11n - 2.4 GHz
        # Channel : 6
        # Client IIF-ID : 0xa0000012
        # Association Id : 1
        # Authentication Algorithm : Open System
        # Idle state timeout : N/A
        # Re-Authentication Timeout : 36000 sec (Remaining time: 32768 sec)
        # Session Warning Time : Timer not running
        # Input Policy Name  : client-default
        # Input Policy State : Installed
        # Input Policy Source : QOS Internal Policy
        # Output Policy Name  : client-default
        # Output Policy State : Installed
        # Output Policy Source : QOS Internal Policy
        # WMM Support : Enabled
        # U-APSD Support : Enabled
        #   U-APSD value : 0
        #   APSD ACs    : BK, BE, VI, VO
        # ...OUTPUT OMITTED...


        nearby_ap = ""
        section_tracker = []
        device_protocols = []
        client_mac_dict = {}
        device_section = False

        # U-APSD Support : Enabled
        p_uapsd = re.compile(r"^U-APSD\s+Support\s+:\s+(?P<status>\S+)$")

        # Client MAC Type : Universally Administered Address
        p_client_mac_type = re.compile(r"^Client\s+MAC\s+Type\s+:\s+(?P<value>.*)$")

        # Connected For : 3233 seconds
        p_connected = re.compile(r"^Connected\s+For\s+:\s+(?P<value>\d+)\s+seconds$")

        # Protocol : 802.11n - 2.4 GHz
        p_protocol = re.compile(r"^Protocol\s+:\s+(?P<value>.*)")

        # Re-Authentication Timeout : 36000 sec (Remaining time: 32768 sec)
        p_re_timer = re.compile(r"^Re-Authentication\s+Timeout\s+:\s+(?P<value>\d+)\s+sec\s+\(Remaining\s+time:\s+(?P<remain>\d+)\s+sec\)$")

        # Re-Authentication Timeout : 36000 sec (Timer not running)
        p_re_timer_not_running = re.compile(r"^^Re-Authentication\s+Timeout\s+:\s+(?P<value>\d+)\s+sec\s+\(Timer\s+not\s+running\)$")

        # Authentication Algorithm : Open System
        p_authen_algorithm = re.compile(r"^Authentication\s+Algorithm\s+:\s+(?P<value>.*)$")

        # Input Policy Source : QOS Internal Policy
        p_input_policy_source = re.compile(r"^Input\s+Policy\s+Source\s+:\s+(?P<value>.*)$")

        # Output Policy Source : QOS Internal Policy
        p_output_policy_source = re.compile(r"^Output\s+Policy\s+Source\s+:\s+(?P<value>.*)$")

        # APSD ACs    : BK, BE, VI, VO
        p_uapsd_ac = re.compile(r"^APSD\s+ACs\s+:\s+(?P<ac>.*)$")

        # Mobility
        p_mobility = re.compile(r"^Mobility:$")

        # Mobility Complete Timestamp : 10/22/2020 08:07:55 IST
        p_mobility_timestamp = re.compile(r"^Mobility\s+Complete\s+Timestamp\s+:\s+(?P<date>\S+)\s+(?P<time>\S+)\s+(?P<timezone>\S+)$")

        # Mobility Roam Type          : Unknown
        p_mobility_roam = re.compile(r"^Mobility\s+Roam\s+Type\s+:\s+(?P<value>\S+)$")

        # Supported Rates : 24.0,36.0,48.0,54.0
        p_supported_rates = re.compile(r"^Supported\s+Rates\s+:\s+(?P<value>.*)$")

        # Client Join Time:
        p_client_join = re.compile(r"^Client\s+Join\s+Time:$")

        # Join Time Of Client : 10/22/2020 08:46:54 IST
        p_client_join_time = re.compile(r"^Join\s+Time\s+Of\s+Client\s+:\s+(?P<date>\S+)\s+(?P<time>\S+)\s+(?P<timezone>\S+)$")

        # Last Policy Manager State : IP Learn Complete
        p_last_policy = re.compile(r"^Last\s+Policy\s+Manager\s+State\s+:\s+(?P<value>.*)$")

        # Client Entry Create Time : 5572 seconds
        p_client_entry_create = re.compile(r"^Client\s+Entry\s+Create\s+Time\s+:\s+(?P<value>\d+)\s+seconds$")

        # Encryption Cipher : CCMP (AES)
        p_encryption_cipher = re.compile(r"Encryption\s+Cipher\s+:\s+(?P<value>.*)$")

        # EAP Type : Not Applicable
        p_eap_type = re.compile(r"^EAP\s+Type\s+:\s+(?P<value>.*)$")

        # WiFi Direct Capabilities:
        p_wifi_capabilities = re.compile(r"WiFi\s+Direct\s+Capabilities:$")

        # Central NAT : DISABLED
        p_central_nat = re.compile(r"^Central\s+NAT\s+:\s+(?P<value>\S+)$")

        # Session Manager:
        p_session = re.compile(r"^Session\s+Manager:")

        # Last Tried Aaa Server Details:
        p_last_tried_aaa = re.compile(r"^Last\s+Tried\s+Aaa\s+Server\s+Details:")

        # Auth Method Status List
        p_auth_method = re.compile(r"^Auth\s+Method\s+Status\s+List$")

        # Local Policies:
        p_local_policies = re.compile(r"^Local\s+Policies:$")

        # Service Template : wlan_svc_lizzard_b1_local (priority 254)
        p_service_template = re.compile(r"^Service\s+Template\s+:\s+(?P<template>.*)$")

        # Server Policies:
        p_server_policies = re.compile(r"^Server\s+Policies:$")

        # Resultant Policies:
        p_resultant_policies = re.compile(r"^Resultant\s+Policies:$")

        # Client Capabilities
        p_client_capabilities = re.compile(r"^Client\s+Capabilities$")

        # DNS Snooped IPv4 Addresses : None
        p_dns_ipv4 = re.compile(r"^DNS\s+Snooped\s+IPv4\s+Addresses\s+:\s+(?P<value>\S+)$")

        # DNS Snooped IPv6 Addresses : None
        p_dns_ipv6 = re.compile(r"^DNS\s+Snooped\s+IPv6\s+Addresses\s+:\s+(?P<value>\S+)$")

        # CF Pollable : Not implemented
        p_cf_pollable = re.compile(r"^CF\s+Pollable\s+:\s+(?P<value>.*)$")

        # CF Poll Request : Not implemented
        p_cf_poll_request = re.compile(r"^CF\s+Poll\s+Request\s+:\s+(?P<value>.*)$")

        # Short Preamble : Not implemented
        p_short_preamble = re.compile(r"^Short\s+Preamble\s+:\s+(?P<value>.*)$")

        # PBCC : Not implemented
        p_pbcc = re.compile(r"^PBCC\s+:\s+(?P<value>.*)$")

        # Channel Agility : Not implemented
        p_channel_agility = re.compile(r"Channel\s+Agility\s+:\s+(?P<value>.*)$")

        # Fast BSS Transition Details :
        p_fast_bss = re.compile(r"^Fast\s+BSS\s+Transition\s+Details\s+:$")

        # Reassociation Timeout : 0
        p_reassoc_timeout = re.compile(r"^Reassociation\s+Timeout\s+:\s+(?P<value>\d+)")

        # Client Statistics:
        p_client_statistics = re.compile(r"^Client\s+Statistics:$")

        # Fabric status : Disabled
        p_fabric_status = re.compile(r"^Fabric\s+status\s+:\s+(?P<value>\S+)$")

        # Radio Measurement Enabled Capabilities
        p_radio_measurement = re.compile(r"^Radio\s+Measurement\s+Enabled\s+Capabilities$")

        # Client Scan Report Time : Timer not running
        p_client_scan_report = re.compile(r"^Client\s+Scan\s+Report\s+Time\s+:\s+(?P<value>.*)")

        # Radio Signal Strength Indicator : -64 dBm
        p_radio_strength = re.compile(r"^Radio\s+Signal\s+Strength\s+Indicator\s+:\s+(?P<value>\S+)\s+dBm$")

        # Signal to Noise Ratio : 30 dB
        p_s2n = re.compile(r"^Signal\s+to\s+Noise\s+Ratio\s+:\s+(?P<value>\d+)\s+dB$")

        # Capabilities: Link Measurement, Neighbor Report, Repeated Measurements, Passive Beacon Measurement, Active Beacon Measurement, Table Beacon Measurement, RM MIB
        p_capabilities = re.compile(r"Capabilities:\s+(?P<value>.*)")

        # Client Scan Report Time : Timer not running
        p_client_scan_report_no = re.compile(r"^Client\s+Scan\s+Report\s+Time\s+:\s+(?P<value>.*)$")

        # Protocol Map     : 0x000029  (OUI, DHCP, HTTP)
        p_protocol_map = re.compile(r"Protocol\s+Map\s+:\s+(?P<value>.*)$")

        # Device OS        : Linux; U; Android 10; RMX1825 Build/QP1A.190711.020
        p_device_os = re.compile(r"^Device\s+OS\s+:\s+(?P<value>.*)$")

        # Nearby AP Statistics:
        p_nearby_ap = re.compile(r"^Nearby\s+AP\s+Statistics:$")

        # b1-72-cap16 (slot 0)
        p_ap = re.compile(r"^(?P<name>.*)\(slot\s+(?P<value>\d+)\)$")

        # antenna 0: 0 s ago	........ -62  dBm
        p_ant_0 = re.compile(r"^antenna\s+0:\s+(?P<sec>\d+)\s+s\s+ago\s+........\s+(?P<value>\S+)\s+dBm$")

        # antenna 1: 0 s ago	........ -62  dBm
        p_ant_1 = re.compile(r"^antenna\s+1:\s+(?P<sec>\d+)\s+s\s+ago\s+........\s+(?P<value>\S+)\s+dBm$")


        # EoGRE : Pending Classification
        p_eogre = re.compile(r"^EoGRE\s+:\s+(?P<value>.*)$")

        # Device Type      : Android
        p_device_type = re.compile(r"^Device\s+Type\s+:\s+(?P<value>\S+)$")

        # Device Name      : android-dhcp-10
        p_device_name = re.compile(r"^Device\s+Name\s+:\s+(?P<value>.*)$")

        # Max Client Protocol Capability: 802.11ac Wave 2
        p_max_client_protocol_capability = re.compile(r"^Max\s+Client\s+Protocol\s+Capability:\s+(?P<value>.*)$")

        # [key] : [value]
        p_colon_split = re.compile(r"^(?P<key>[\S\s]+\S)\s*: +(?P<value>\S+)$")


        for line in output.splitlines():
            line = line.strip()
            if p_uapsd.match(line):
                # U-APSD Support : Enabled
                match = p_uapsd.match(line)
                client_mac_dict.update({ "u_apsd_support": {} })
                client_mac_dict["u_apsd_support"].update({ "status": match.group("status")})
                section_tracker.append("u_apsd_support")
                continue
            elif p_connected.match(line):
                # Connected For : 3233 seconds
                match = p_connected.match(line)
                client_mac_dict.update({ "connected_for_seconds": int(match.group("value")) })
                continue
            elif p_client_mac_type.match(line):
                # Client MAC Type : Universally Administered Address
                match = p_client_mac_type.match(line)
                client_mac_dict.update({ "client_mac_type": match.group("value")})
                continue
            elif p_protocol.match(line) and device_section == False:
                # Protocol : 802.11n - 2.4 GHz
                match = p_protocol.match(line)
                client_mac_dict.update({ "protocol": match.group("value")})
                device_section = True
                continue
            elif p_authen_algorithm.match(line):
                # Authentication Algorithm : Open System
                match = p_authen_algorithm.match(line)
                client_mac_dict.update({ "authentication_alogrithm": match.group("value")})
                continue
            elif p_re_timer.match(line):
                # Re-Authentication Timeout : 36000 sec (Remaining time: 32768 sec)
                match = p_re_timer.match(line)
                client_mac_dict.update({ "re_authentication_timeout_secs": {} })
                client_mac_dict["re_authentication_timeout_secs"].update({ "configured": int(match.group("value")) })
                client_mac_dict["re_authentication_timeout_secs"].update({ "remaining_time": int(match.group("remain")) })
                continue
            elif p_re_timer_not_running.match(line):
                # Re-Authentication Timeout : 36000 sec (Timer not running)
                match = p_re_timer_not_running.match(line)
                client_mac_dict.update({ "re_authentication_timeout_secs": {} })
                client_mac_dict["re_authentication_timeout_secs"].update({ "configured": int(match.group("value")) })
                client_mac_dict["re_authentication_timeout_secs"].update({ "remaining_time": "timer not running" })
                continue
            elif p_input_policy_source.match(line):
                # Input Policy Source : QOS Internal Policy
                match = p_input_policy_source.match(line)
                client_mac_dict.update({ "input_policy_source": match.group("value") })
                continue
            elif p_output_policy_source.match(line):
                # Output Policy Source : QOS Internal Policy
                match = p_output_policy_source.match(line)
                client_mac_dict.update({ "output_policy_source": match.group("value") })
                continue
            elif p_supported_rates.match(line):
                # Supported Rates : 24.0,36.0,48.0,54.0
                match = p_supported_rates.match(line)
                rates_list = [x.strip() for x in match.group("value").split(',')]
                client_mac_dict.update({ "supported_rates": rates_list })
            elif p_uapsd_ac.match(line):
                # APSD ACs    : BK, BE, VI, VO
                section_tracker.pop()
                match = p_uapsd_ac.match(line)
                ac_list = [x.strip() for x in match.group("ac").split(',')]
                client_mac_dict["u_apsd_support"].update({ "apsd_acs": ac_list })
                continue
            elif p_mobility.match(line):
                # Mobility:
                client_mac_dict.update({ "mobility": {} })
                section_tracker.append("mobility")
                continue
            elif p_client_join.match(line):
                # Client Join Time:
                client_mac_dict.update({ "client_join_time": {} })
                section_tracker.append("client_join_time")
                continue
            elif p_client_join_time.match(line):
                # Join Time Of Client : 10/22/2020 08:46:54 IST
                section_tracker.pop()
                match = p_client_join_time.match(line)
                group = match.groupdict()
                client_mac_dict["client_join_time"].update({ "date": group["date"] })
                client_mac_dict["client_join_time"].update({ "time": group["time"] })
                client_mac_dict["client_join_time"].update({ "timezone": group["timezone"] })
                continue
            elif p_eap_type.match(line):
                # EAP Type : Not Applicable
                match = p_eap_type.match(line)
                client_mac_dict.update({ "eap_type" : match.group("value") })
                continue
            elif p_mobility_timestamp.match(line):
                # Mobility Complete Timestamp : 10/22/2020 08:07:55 IST
                match = p_mobility_timestamp.match(line)
                group = match.groupdict()
                client_mac_dict["mobility"].update({ "mobility_complete_timestamp": {}})
                client_mac_dict["mobility"]["mobility_complete_timestamp"].update({ "date": group["date"] })
                client_mac_dict["mobility"]["mobility_complete_timestamp"].update({ "time": group["time"] })
                client_mac_dict["mobility"]["mobility_complete_timestamp"].update({ "timezone": group["timezone"] })
                continue
            elif p_mobility_roam.match(line):
                # Mobility Roam Type          : Unknown
                section_tracker.pop()
                match = p_mobility_roam.match(line)
                client_mac_dict["mobility"].update({ "mobility_roam_type": match.group("value") })
                continue
            elif p_last_policy.match(line):
                # Last Policy Manager State : IP Learn Complete
                match = p_last_policy.match(line)
                client_mac_dict.update({ "last_policy_manager_state": match.group("value") })
                continue
            elif p_client_entry_create.match(line):
                # Client Entry Create Time : 5572 seconds
                match = p_client_entry_create.match(line)
                client_mac_dict.update({ "client_entry_create_time_secs": int(match.group("value")) })
                continue
            elif p_encryption_cipher.match(line):
                # Encryption Cipher : CCMP (AES)
                match = p_encryption_cipher.match(line)
                client_mac_dict.update({ "encryption_cipher": match.group("value") })
                continue
            elif p_wifi_capabilities.match(line):
                # WiFi Direct Capabilities:
                client_mac_dict.update({ "wifi_direct_capabilities": {} })
                section_tracker.append("wifi_direct_capabilities")
                continue
            elif p_central_nat.match(line):
                # Central NAT : DISABLED
                client_mac_dict.update({ "central_nat": match.group("value") })
                continue
            elif p_session.match(line):
                # Session Manager:
                section_tracker.pop()
                client_mac_dict.update({ "session_manager": {} })
                section_tracker.append("session_manager")
                continue
            elif p_last_tried_aaa.match(line):
                # Last Tried Aaa Server Details:
                client_mac_dict["session_manager"].update({"last_tried_aaa_server_details": {} })
                section_tracker.append("last_tried_aaa_server_details")
                continue
            elif p_dns_ipv4.match(line):
                # DNS Snooped IPv4 Addresses : None
                match = p_dns_ipv4.match(line)
                client_mac_dict.update({ "dns_snooped_ipv4_addresses": match.group("value") })
                continue
            elif p_dns_ipv6.match(line):
                # DNS Snooped IPv6 Addresses : None
                match = p_dns_ipv6.match(line)
                client_mac_dict.update({ "dns_snooped_ipv6_addresses": match.group("value") })
                continue
            elif p_auth_method.match(line):
                # Auth Method Status List
                section_tracker.pop()
                client_mac_dict["session_manager"].update({ "auth_method_status_list": {} })
                section_tracker.append("auth_method_status_list")
                continue
            elif p_local_policies.match(line):
                # Local Policies:
                section_tracker.pop()
                client_mac_dict["session_manager"].update({ "local_policies": {} })
                section_tracker.append("local_policies")
                continue
            elif p_service_template.match(line):
                # Service Template : wlan_svc_lizzard_b1_local (priority 254)
                match = p_service_template.match(line)
                client_mac_dict["session_manager"]["local_policies"].update({ "service_template": match.group("template") })
                continue
            elif p_server_policies.match(line):
                # Server Policies:
                section_tracker.pop()
                client_mac_dict["session_manager"].update({ "server_policies": {} })
                section_tracker.append("server_policies")
                continue
            elif p_resultant_policies.match(line):
                # Resultant Policies:
                section_tracker.pop()
                client_mac_dict["session_manager"].update({ "resultant_policies": {} })
                section_tracker.append("resultant_policies")
                continue
            elif p_client_capabilities.match(line):
                # Client Capabilities
                section_tracker.pop()
                section_tracker.pop()
                client_mac_dict.update({ "client_capabilities": {} })
                section_tracker.append("client_capabilities")
                continue
            elif p_cf_pollable.match(line):
                # CF Pollable : Not implemented
                match = p_cf_pollable.match(line)
                client_mac_dict["client_capabilities"].update({ "cf_pollable": match.group("value") })
                continue
            elif p_cf_poll_request.match(line):
                # CF Poll Request : Not implemented
                match = p_cf_poll_request.match(line)
                client_mac_dict["client_capabilities"].update({ "cf_poll_request": match.group("value") })
                continue
            elif p_short_preamble.match(line):
                # Short Preamble : Not implemented
                match = p_short_preamble.match(line)
                client_mac_dict["client_capabilities"].update({ "short_preamble": match.group("value") })
                continue
            elif p_channel_agility.match(line):
                # Channel Agility : Not implemented
                match = p_channel_agility.match(line)
                client_mac_dict["client_capabilities"].update({ "channel_agility": match.group("value") })
                continue
            elif p_pbcc.match(line):
                # Listen Interval : 0
                match = p_pbcc.match(line)
                client_mac_dict["client_capabilities"].update({ "pbcc": match.group("value") })
                continue
            elif p_fast_bss.match(line):
                # Fast BSS Transition Details :
                section_tracker.pop()
                client_mac_dict.update({ "fast_bss_transition_details": {} })
                continue
            elif p_reassoc_timeout.match(line):
                # Reassociation Timeout : 0
                match = p_reassoc_timeout.match(line)
                client_mac_dict["fast_bss_transition_details"].update({ "reassociation_timeout": int(match.group("value"))})
            elif p_client_statistics.match(line):
                # Client Statistics:
                client_mac_dict.update({"client_statistics": {} })
                section_tracker.append("client_statistics")
                continue
            elif p_fabric_status.match(line):
                match = p_fabric_status.match(line)
                client_mac_dict.update({ "fabric_status": match.group("value") })
                continue
            elif p_radio_measurement.match(line):
                # Radio Measurement Enabled Capabilities
                section_tracker.pop()
                client_mac_dict.update({ "radio_measurement_enabled_capabilities": {} })
                continue
            elif p_capabilities.match(line):
                # Capabilities: Link Measurement, Neighbor Report, Repeated Measurements, Passive Beacon Measurement, Active Beacon Measurement, Table Beacon Measurement, RM MIB
                match = p_capabilities.match(line)
                cap_list = [x.strip() for x in match.group("value").split(",")]
                client_mac_dict["radio_measurement_enabled_capabilities"].update({ "capabilities": cap_list })
                continue
            elif p_radio_strength.match(line):
                # Radio Signal Strength Indicator : -64 dBm
                match = p_radio_strength.match(line)
                client_mac_dict["client_statistics"].update({ "radio_signal_strength_indicator_dbm": match.group("value") })
                continue
            elif p_s2n.match(line):
                # Signal to Noise Ratio : 30 dB
                match = p_s2n.match(line)
                client_mac_dict["client_statistics"].update({ "signal_to_noise_ration_db": int(match.group("value")) })
                continue
            elif p_nearby_ap.match(line):
                # Nearby AP Statistics:
                client_mac_dict.update({ "nearby_ap_statistics": { "ap_names": {} }})
                continue
            elif p_ap.match(line):
                # b1-72-cap16 (slot 0)
                match = p_ap.match(line)
                nearby_ap = match.group("name")
                client_mac_dict["nearby_ap_statistics"]["ap_names"].update({ nearby_ap: {} })
                client_mac_dict["nearby_ap_statistics"]["ap_names"][nearby_ap].update({ "slot": match.group("value") })
                continue
            elif p_ant_0.match(line):
                # antenna 0: 0 s ago	........ -62  dBm
                match = p_ant_0.match(line)
                client_mac_dict["nearby_ap_statistics"]["ap_names"][nearby_ap].update({ "antenna_0": {} })
                client_mac_dict["nearby_ap_statistics"]["ap_names"][nearby_ap]["antenna_0"].update({ "seconds_ago": match.group("sec") })
                client_mac_dict["nearby_ap_statistics"]["ap_names"][nearby_ap]["antenna_0"].update({ "dbm": match.group("value") })
                continue
            elif p_ant_1.match(line):
                # antenna 1: 0 s ago	........ -62  dBm
                match = p_ant_1.match(line)
                client_mac_dict["nearby_ap_statistics"]["ap_names"][nearby_ap].update({ "antenna_1": {} })
                client_mac_dict["nearby_ap_statistics"]["ap_names"][nearby_ap]["antenna_1"].update({ "seconds_ago": match.group("sec") })
                client_mac_dict["nearby_ap_statistics"]["ap_names"][nearby_ap]["antenna_1"].update({ "dbm": match.group("value") })
                continue
            elif p_eogre.match(line):
                # EoGRE : Pending Classification
                match = p_eogre.match(line)
                client_mac_dict.update({ "eogre": match.group("value") })
                continue
            elif p_device_type.match(line):
                # Device Type      : Android
                match = p_device_type.match(line)
                client_mac_dict.update({ "device_info": {} })
                client_mac_dict["device_info"].update({ "device_type": match.group("value") })
                continue
            elif p_device_name.match(line):
                # Device Name      : android-dhcp-10
                match = p_device_name.match(line)
                client_mac_dict["device_info"].update({ "device_name": match.group("value") })
                continue
            elif p_client_scan_report_no.match(line):
                # Client Scan Report Time : Timer not running
                match = p_client_scan_report_no.match(line)
                client_mac_dict.update({ "client_scan_report": match.group("value") })
                continue
            elif p_protocol_map.match(line):
                # Protocol Map     : 0x000029  (OUI, DHCP, HTTP)
                match = p_protocol_map.match(line)
                client_mac_dict["device_info"].update({ "protocol_map": match.group("value") })
                continue
            elif p_device_os.match(line):
                # Device OS        : Linux; U; Android 10; RMX1825 Build/QP1A.190711.020
                match = p_device_os.match(line)
                client_mac_dict["device_info"].update({ "device_os" : match.group("value") })
                continue
            elif p_protocol.match(line) and device_section == True:
                # Protocol         : DHCP
                match = p_protocol.match(line)
                device_protocols.append(match.group("value") )
                client_mac_dict["device_info"].update({ "protocols": device_protocols })
                device_section = True
                continue
            elif p_max_client_protocol_capability.match(line):
                # Max Client Protocol Capability: 802.11ac Wave 2
                match = p_max_client_protocol_capability.match(line)
                client_mac_dict.update({ "max_client_protocol_capability": match.group("value") })
                continue
            elif p_colon_split.match(line):
                # [key] : [value]
                match = p_colon_split.match(line)
                group = match.groupdict()

                if group["key"][-1] == ")":
                    group["key"] = group["key"][:-1]

                group["key"] = group["key"].replace(" ", "_").replace("-", "_").replace("(", "_").replace(")", "_").replace("__", "_").lower()
                group["value"] = self.change_data_type(group["value"])

                if group["key"] == "data":
                    continue

                if len(section_tracker) == 0:
                    client_mac_dict.update({ group["key"]: group["value"] })
                elif len(section_tracker) == 1:
                    client_mac_dict[section_tracker[-1]].update({ group["key"]: group["value"] })
                elif len(section_tracker) == 2:
                    client_mac_dict[section_tracker[-2]][section_tracker[-1]].update({ group["key"]: group["value"] })


        return client_mac_dict
