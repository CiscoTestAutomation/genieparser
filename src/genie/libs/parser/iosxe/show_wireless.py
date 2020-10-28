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
        # 58bf.eaff.89a2 a2-11-cap43                   17   Run                11ac     Dot1x     
        # 58bf.eaff.ac28 a2-11-cap50                   19   IP Learn           11n(2.4) MAB       
        # 58bf.eaff.6393 a2-11-cap52                   19   Webauth Pending    11n(2.4) MAB       
        # --------------------------------------------------------------------------------------------
        # 58bf.eaff.63a0 a2-11-cap46                   17   Run                11ac     Dot1x     
        # 58bf.eaff.2c06 a2-12-cap15                   19   Webauth Pending    11n(2.4) MAB       
        # 58bf.eaff.8759 a2-11-cap44                   19   Webauth Pending    11n(2.4) MAB       
        # --------------------------------------------------------------------------------------------
        # 58bf.eaff.5e2c a2-12-cap17                   19   Webauth Pending    11ac     MAB       
        # 58bf.eaff.fc60 a2-12-cap17                   19   Webauth Pending    11ac     MAB   

        # Number of Fabric Clients : 8
        p_clients = re.compile(r"^Number\s+of\s+Fabric\s+Clients\s+:\s+(?P<clients>\S+)$")

        # MAC Address    AP Name                          WLAN State              Protocol Method
        p_header = re.compile(r"^MAC\s+Address\s+AP\s+Name\s+WLAN\s+State\s+Protocol\s+Method$")

        # -------------------------------------------------------------------------------------------------------------------------
        p_delimiter = re.compile(
            r"^-------------------------------------------------------------------------------------------------------------------------$")

        # 58bf.eaff.89a2 a2-11-cap43                   17   Run                11ac     Dot1x
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
            # 58bf.eaff.89a2 a2-11-cap43                   17   Run                11ac     Dot1x
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
        # 58bf.eaff.0cf1 b80-72-cap16                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.eaff.0dbb b80-82-cap16                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.eaff.0d07 b80-12-cap17                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.eaff.0d0a b80-32-cap13                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.eaff.0d0f b80-42-cap13                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.eaff.c0fc b80-22-cap14                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.eaff.6ba5 b80-32-cap4                                  WLAN 19   IP Learn          11n(2.4) MAB        Local
        # 58bf.eaff.872f b80-51-cap7                                  WLAN 17   Authenticating    11ac     Dot1x      Unknown
        # 58bf.eaff.04e2 b80-61-cap4                                  WLAN 17   Authenticating    11ac     Dot1x      Unknown
        # 58bf.eaff.f748 b80-62-cap1                                  WLAN 19   IP Learn          11n(5)   MAB        Local
        # 58bf.eaff.2837 b80-12-cap14                                 WLAN 17   Run               11ac     Dot1x      Local
        # 58bf.eaff.4607 b80-51-cap6                                  WLAN 17   Run               11n(5)   Dot1x      Local
        # 58bf.eaff.0926 b80-61-cap4                                  WLAN 19   Webauth Pending   11n(2.4) MAB        Local
        #
        # Number of Excluded Clients: 2
        #
        # MAC Address    AP Name                          Type ID   State              Protocol Method
        # ------------------------------------------------------------------------------------------------
        # 58bf.eaff.aa71 b80-61-cap20                   WLAN 17   Excluded           11ac     Dot1x
        # 58bf.eaff.7b79 b80-62-cap14                   WLAN 17   Excluded           11ac     Dot1x

        # Number of Clients: 13
        wireless_client_count_capture = re.compile(r"^Number\s+of\s+Clients:\s+(?P<wireless_client_count>\d+)$")
        # MAC Address    AP Name                                        Type ID   State             Protocol Method     Role
        wireless_client_info_header_capture = re.compile(
            r"^MAC\s+Address\s+AP\s+Name\s+Type\s+ID\s+State\s+Protocol\s+Method\s+Role$")
        # -------------------------------------------------------------------------------------------------------------------------
        delimiter_capture = re.compile(
            r"^-------------------------------------------------------------------------------------------------------------------------$")
        # 58bf.eaff.0cf1 b80-72-cap16                                 WLAN 17   Run               11ac     Dot1x      Local
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
        # 58bf.eaff.aa71 b80-61-cap20                   WLAN 17   Excluded           11ac     Dot1x
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
            # 58bf.eaff.0cf1 b80-72-cap16                                 WLAN 17   Run               11ac     Dot1x      Local
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
            # 58bf.eaff.aa71 b80-61-cap20                   WLAN 17   Excluded           11ac     Dot1x
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
        # b80-72-cap30                    58bf.eaff.c7d3    10.10.7.177      Self
        # b80-81-cap4                     58bf.eaff.75b3    10.10.7.177      Self
        # b80-52-cap6                     58bf.eaff.88f3    10.10.7.177      Self

        # AP name                           AP radio MAC      Controller IP     Learnt from
        ap_header_capture = re.compile(
            r"^AP\s+name\s+AP\s+radio\s+MAC\s+Controller\s+IP\s+Learnt\s+from$"
        )

        # b80-72-cap30                    58bf.eaff.c7d3    10.10.7.177      Self
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
                        # radio_mac: 58bf.eaff.c7d3
                        "ap_radio_mac": groups["ap_radio_mac"],
                        # controller_ip: 10.10.7.177
                        "controller_ip": groups["controller_ip"],
                        # learnt_from: Self
                        "learnt_from": groups["learnt_from"],
                    }
                }

                ap_info_obj["ap_name"].update(ap_name_dict)

        return ap_info_obj
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
        # 58bf.eaff.89a2 a2-11-cap43                   17   Run                11ac     Dot1x     
        # 58bf.eaff.ac28 a2-11-cap50                   19   IP Learn           11n(2.4) MAB       
        # 58bf.eaff.6393 a2-11-cap52                   19   Webauth Pending    11n(2.4) MAB       
        # --------------------------------------------------------------------------------------------
        # 58bf.eaff.63a0 a2-11-cap46                   17   Run                11ac     Dot1x     
        # 58bf.eaff.2c06 a2-12-cap15                   19   Webauth Pending    11n(2.4) MAB       
        # 58bf.eaff.8759 a2-11-cap44                   19   Webauth Pending    11n(2.4) MAB       
        # --------------------------------------------------------------------------------------------
        # 58bf.eaff.5e2c a2-12-cap17                   19   Webauth Pending    11ac     MAB       
        # 58bf.eaff.fc60 a2-12-cap17                   19   Webauth Pending    11ac     MAB   

        # Number of Fabric Clients : 8
        p_clients = re.compile(r"^Number\s+of\s+Fabric\s+Clients\s+:\s+(?P<clients>\S+)$")

        # MAC Address    AP Name                          WLAN State              Protocol Method
        p_header = re.compile(r"^MAC\s+Address\s+AP\s+Name\s+WLAN\s+State\s+Protocol\s+Method$")

        # -------------------------------------------------------------------------------------------------------------------------
        p_delimiter = re.compile(
            r"^-------------------------------------------------------------------------------------------------------------------------$")

        # 58bf.eaff.89a2 a2-11-cap43                   17   Run                11ac     Dot1x
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
            # 58bf.eaff.89a2 a2-11-cap43                   17   Run                11ac     Dot1x
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
        # Mobility MAC Address: 58bf.eaff.eb40
        # Mobility Domain Identifier: 0x61b3

        # Controllers configured in the Mobility Domain:

        # IP                                        Public Ip                                  MAC Address         Group Name                       Multicast IPv4    Multicast IPv6                              Status                       PMTU
        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # 10.10.7.177                               N/A                                        58bf.eaff.eb40      b80-mobility                0.0.0.0           ::                                          N/A                          N/A

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
            # Mobility MAC Address: 58bf.eaff.eb40
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
            # 58bf.eaff.eb40
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
        # 706d.05ff.0859  706d.05ff.9bb8  AP706d.05ff.9bb8                  10.10.116.22                             Not Joined  Join                  Ap auth pending
        # 706d.05ff.1705  706d.05ff.5f35  visitors-hydra                    10.10.78.156                              Not Joined  Join                  Ap auth pending
        # 706d.05ff.1ac4  706d.05ff.60e4  visitors-hydra                    10.10.82.200                             Not Joined  Join                  Ap auth pending
        # 0042.5aff.29ba  006b.f1ff.2507  visitors-1815i                     10.10.139.90                             Joined      Join                  Ap auth pending
        # 706d.05ff.3e54  706d.05ff.e3da  visitors-hydra2                   10.10.36.138                               Not Joined  Join                  Ap auth pending
        # 706d.05ff.42b3  706d.05ff.e4b2  visitors-hydra5                   10.10.36.138                               Not Joined  Join                  Ap auth pending
        # 00be.75ff.48c6  706d.05ff.ac39  visitors-1815t                      10.10.236.197                            Joined      Join                  Ap auth pending
        # 706d.05ff.274f  706d.05ff.222f  visitors-1815i                    10.10.152.239                            Joined      Join                  Ap auth pending
        # 706d.05ff.6c7f  706d.05ff.347e  visitors-mallorca                  10.10.40.15                              Not Joined  Join                  Ap auth pending
        # 706d.05ff.7bde  706d.05ff.3717  visitors-mallorca                  10.10.7.234                              Not Joined  Join                  Ap auth pending

        # Number of APs: 61
        ap_count_capture = re.compile(r"^Number of APs:\s+(?P<ap_count>\d+)$")

        # 706d.05ff.0859  706d.05ff.9bb8  AP706d.05ff.9bb8                  10.10.116.22                             Not Joined  Join                  Ap auth pending
        ap_join_capture = re.compile(
            # 706d.05ff.0859
            r"^(?P<base_mac>[a-f0-9]{4}\.[a-f0-9]{4}\.[a-f0-9]{4})\s+"
            # 706d.05ff.9bb8
            r"(?P<visitors_mac>[a-f0-9]{4}\.[a-f0-9]{4}\.[a-f0-9]{4})\s+"
            # AP706d.05ff.9bb8
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


# =================================
# Schema for:
#  * 'show wireless stats mobility'
# =================================
class ShowWirelessStatsMobilitySchema(MetaParser):
    """Schema for show wireless stats mobility."""

    schema = {
      "mobility_event_statistics": {
          "joined_as": {
              "local": int,
              "foreign": int,
              "export_foreign": int,
              "export_anchor": int,
          },
          "delete": {"local": int, "remote": int},
          "role_changes": {"local_to_anchor": int, "anchor_to_local": int},
          "roam_stats": {
              "l2_roam_count": int,
              "l3_roam_count": int,
              "flex_client_roam_count": int,
              "inter_wncd_roam_count": int,
              "intra_wncd_roam_count": int,
              "remote_inter_cntrl_roam_count": int,
              "remote_webauth_pending_roams": int,
          },
          "anchor_request": {
              "sent": int,
              "grant_received": int,
              "deny_received": int,
              "received": int,
              "grant_sent": int,
              "deny_sent": int,
          },
          "handoff_status_received": {
              "success": int,
              "group_mismatch": int,
              "client_unknown": int,
              "client_blacklisted": int,
              "ssid_mismatch": int,
              "denied": int,
              "l3_vlan_override": int,
              "unknown_peer": int,
          },
          "handoff_status_sent": {
              "success": int,
              "group_mismatch": int,
              "client_unknown": int,
              "client_blacklisted": int,
              "ssid_mismatch": int,
              "denied": int,
              "l3_vlan_override": int,
          },
          "export_anchor": {
              "request_sent": int,
              "response_received": {
                  "ok": int,
                  "deny_generic": int,
                  "client_blacklisted": int,
                  "client_limit_reached": int,
                  "profile_mismatch": int,
                  "deny_unknown_reason": int,
                  "request_received": int,
              },
              "response_sent": {
                  "ok": int,
                  "deny_generic": int,
                  "client_blacklisted": int,
                  "client_limit_reached": int,
                  "profile_mismatch": int,
              },
          },
      },
      "mm_mobility_event_statistics": {
          "event_data_allocs": int,
          "event_data_frees": int,
          "fsm_set_allocs": int,
          "fsm_set_frees": int,
          "timer_allocs": int,
          "timer_frees": int,
          "timer_starts": int,
          "timer_stops": int,
          "invalid_events": int,
          "internal_errors": int,
          "delete_internal_errors": int,
          "roam_internal_errors": int,
      },
      "mmif_mobility_event_statistics": {
          "event_data_allocs": int,
          "event_data_frees": int,
          "invalid_events": int,
          "event_schedule_errors": int,
          "mmif_internal_errors": {
              "ipc_failure": int,
              "database_failure": int,
              "invalid_parameters": int,
              "mobility_message_decode_failure": int,
              "fsm_failure": int,
              "client_handoff_success": int,
              "client_handoff_failure": int,
              "anchor_deny": int,
              "remote_delete": int,
              "tunnel_down_delete": int,
              "mbssid_down": int,
              "unknown_failure": int,
          },
      },
    }


# =================================
# Parser for:
#  * 'show wireless stats mobility'
# =================================
class ShowWirelessStatsMobility(ShowWirelessStatsMobilitySchema):
    """Parser for show wireless stats mobility"""

    cli_command = 'show wireless stats mobility'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)

        else:
          out = output

        # Mobility event statistics:
        mobility_event_statistics_capture = re.compile(r"^Mobility event statistics:$")

        # Joined as
        joined_as_capture = re.compile(r"^Joined as$")

        # Delete
        delete_capture = re.compile(r"^Delete$")

        # Role changes
        role_changes_capture = re.compile(r"^Role changes$")

        # Roam stats
        roam_stats_capture = re.compile(r"^Roam stats$")

        # Anchor Request
        anchor_request_capture = re.compile(r"^Anchor Request$")

        # Handoff Status Received
        handoff_status_received_capture = re.compile(r"^Handoff Status Received$")

        # Handoff Status Sent
        handoff_status_sent_capture = re.compile(r"^Handoff Status Sent$")

        # Export Anchor
        export_anchor_capture = re.compile(r"^Export Anchor$")

        # Response Received             :
        export_anchor_response_received_capture = re.compile(r"Response Received\s+:")

        # Response Sent             :
        export_anchor_response_sent_capture = re.compile(r"Response Sent\s+:")

        # MM mobility event statistics:
        mm_mobility_event_statistics_capture = re.compile(
            r"^MM mobility event statistics:$"
        )

        # MMIF mobility event statistics:
        mmif_mobility_event_statistics_capture = re.compile(
            r"^MMIF mobility event statistics:$"
        )

        # MMIF internal errors:
        mmif_internal_errors_capture = re.compile(r"^MMIF internal errors:$")

        # key : value
        key_value_capture = re.compile(r"^(?P<key>[\S\s]+\S)\s*:\s+(?P<value>\d+)$")

        wireless_info_obj = {}

        for line in out.splitlines():
            line = line.strip()

            header_capture_list = [
                mobility_event_statistics_capture,
                mm_mobility_event_statistics_capture,
                mmif_mobility_event_statistics_capture,
            ]

            for capture in header_capture_list:
                if capture.match(line):
                    line_format = line.replace(" ", "_").lower().strip(":")

                    header_group = wireless_info_obj.setdefault(line_format, {})
                    header_tracking = "header"

            subheader_capture_list = [
                joined_as_capture,
                delete_capture,
                role_changes_capture,
                roam_stats_capture,
                anchor_request_capture,
                handoff_status_received_capture,
                handoff_status_sent_capture,
                export_anchor_capture,
                mmif_internal_errors_capture,
            ]

            for capture in subheader_capture_list:
                if capture.match(line):
                    line_format = line.replace(" ", "_").lower().strip(":")

                    subheader_group = header_group.setdefault(line_format, {})
                    header_tracking = "subheader"

            sub_subheader_capture_list = [export_anchor_response_received_capture, export_anchor_response_sent_capture]
            
            for capture in sub_subheader_capture_list:
                if capture.match(line):
                    line_format = line.strip(":").strip().replace(" ", "_").lower()

                    sub_subheader_group = subheader_group.setdefault(line_format, {})
                    header_tracking = "sub_subheader"

            if key_value_capture.match(line):
                match = key_value_capture.match(line)
                group = match.groupdict()

                # format the keys and values
                format_key = group["key"].replace("-", "_").replace(" ", "_").lower()
                format_value = int(group["value"])

                # special case for the Deny key formatting
                if re.match(r"^Deny\s+", group["key"]):
                    format_key = group["key"].replace("-", "").replace(" ", "_").replace("__", "_").lower()

                if header_tracking == "header":
                    # update current header group
                    header_group.update({format_key: format_value})

                if header_tracking == "subheader":
                    # update current subheader group
                    subheader_group.update({format_key: format_value})

                if header_tracking == "sub_subheader":
                    # update current sub subheader group
                    sub_subheader_group.update({format_key: format_value})


        return wireless_info_obj
