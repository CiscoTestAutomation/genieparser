import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or



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

    def cli(self, policy_name="", output=None):
        if output is None:
            cmd = self.cli_command.format(policy_name=policy_name)
            output = self.device.execute(cmd)
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
                Optional("type") : str,
                Optional("wlan") : int,
                Optional("state") : str,
                Optional("protocol") : str,
                Optional("method") : str,
                Optional("l2_vnid") : int,
                Optional("rloc_ip") : str,
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

        ret_dict = {}


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

        # 58bf.eaff.89a2 a2-11-cap43                   17   Run                11ac     Dot1x
        p_client_info = re.compile(r"^(?P<mac>\S{4}\.\S{4}\.\S{4})\s+(?P<name>\S+)\s+(?P<wlan>\S+)\s+(?P<state>.*)\s+(?P<protocol>\S+)\s+(?P<method>(Dot1x|MAB|None|SAE))$")

        # MAC Address    AP Name                  Type ID   State              Protocol Method     L2 VNID    RLOC IP
        # dca6.3249.1877 AP-E6-25C0               WLAN 18   Run                11n(2.4) Dot1x      8189       10.240.240.3
        p_client_info_n = re.compile(r"^(?P<mac>\S{4}\.\S{4}\.\S{4})\s+(?P<name>\S+)\s+(?P<wtype>\w+)\s+(?P<wlan>\d+)\s+(?P<state>(\w+\s*\w+))\s+(?P<protocol>\S+)\s+(?P<method>(Dot1x|MAB|None|SAE))\s+(?P<l2_vnid>\d+)\s+(?P<rloc_ip>((\d{1,3}\.){3}\d{1,3}))$")

        for line in output.splitlines():
            line = line.strip()
            # Number of Fabric Clients : 8
            if p_clients.match(line):
                match = p_clients.match(line)
                client_count = int(match.group('clients'))
                if not ret_dict.get('number_of_fabric_clients'):
                    ret_dict.update({'number_of_fabric_clients' : client_count})
                continue

            # 58bf.eaff.89a2 a2-11-cap43                   17   Run                11ac     Dot1x
            if p_client_info.match(line):
                match = p_client_info.match(line)
                groups = match.groupdict()
                mac_address = groups['mac']
                ap_name = groups['name']
                wlan = int(groups['wlan'])
                state = groups['state'].strip()
                protocol = groups['protocol']
                method = groups['method']
                if not ret_dict.get('mac_address'):
                    ret_dict['mac_address'] = {}
                ret_dict['mac_address'].update({mac_address : {'ap_name' : ap_name,
                                                               'wlan' : wlan,
                                                               'state' : state,
                                                               'protocol' : protocol,
                                                               'method' : method}})

            # dca6.3249.1877 AP-E6-25C0               WLAN 18   Run                11n(2.4) Dot1x      8189       10.240.240.3
            if p_client_info_n.match(line):
                match = p_client_info_n.match(line)
                groups = match.groupdict()
                mac_address = groups['mac']
                ap_name = groups['name']
                wtype = groups['wtype']
                wlan = int(groups['wlan'])
                state = groups['state'].strip()
                protocol = groups['protocol']
                method = groups['method']
                l2_vnid = int(groups['l2_vnid'])
                rloc_ip = groups['rloc_ip']
                if not ret_dict.get('mac_address'):
                    ret_dict['mac_address'] = {}
                ret_dict['mac_address'].update({mac_address : {'ap_name': ap_name,
                                                               'type': wtype,
                                                               'wlan': wlan,
                                                               'state': state,
                                                               'protocol': protocol,
                                                               'method': method,
                                                               'l2_vnid': l2_vnid,
                                                               'rloc_ip':rloc_ip}})
        return ret_dict


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
        # 200d.b033.01fe Site6-FE2-9162                               WLAN 19   Run              11ac      None        Local
        # 0e4d.72bc.3014 Site6-FE2-9162                               WLAN 19   Run               11ax(5)  SAE        Local
        wireless_client_info_capture = re.compile(
            r"^(?P<mac_address>\S+)\s+(?P<ap_name>\S+)\s+(?P<type>\S+)\s+(?P<id>\d+)\s+(?P<state>.*)\s+(?P<protocol>\S+)\s+(?P<method>(Dot1x|MAB|SAE|None))\s+(?P<role>\S+)$")
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
            r"(?P<pmtu>\S+)\s*$"
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
        Optional("client_ipv6_addresses"): str,
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
        Optional("re_authentication_timeout_secs"): {
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
            Optional("u_apsd_value"): int,
            Optional("apsd_acs"): list
        },
        "fastlane_support": str,
        "client_active_state": str,
        "power_save": str,
        Optional("current_rate"): Or(float, str),
        "supported_rates": list,
        Optional("aaa_qos_rate_limit_parameters"): {
            "upstream": {
                "qos_average_data_rate_kbps": int,
                "qos_realtime_average_data_rate_kbps": int,
                "qos_burst_data_rate_kbps": int,
                "qos_realtime_burst_data_rate_kbps": int
            },
            "downstream": {
                "qos_average_data_rate_kbps": int,
                "qos_realtime_average_data_rate_kbps": int,
                "qos_burst_data_rate_kbps": int,
                "qos_realtime_burst_data_rate_kbps": int
            }
        },
        "mobility": {
            "move_count": int,
            "mobility_role": str,
            "mobility_roam_type": str,
            Optional("mobility_complete_timestamp"): str
        },
        "client_join_time": str,
        "client_state_servers": str,
        "client_acls": str,
        "policy_manager_state": str,
        "last_policy_manager_state": str,
        "client_entry_create_time_secs": int,
        "policy_type": str,
        "encryption_cipher": str,
        Optional("authentication_key_management"): str,
        "user_defined_private_network": str,
        "user_defined_private_network_drop_unicast": str,
        "encrypted_traffic_analytics": str,
        "protected_management_frame__802.11w": str,
        "eap_type": str,
        "vlan_override_after_webauth": str,
        "vlan": Or(int, str),
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
            Optional("last_tried_aaa_server_details"): {
                "server_ip": str
            },
            "auth_method_status_list": {
                "method": {
                    Any(): {
                        Optional("sm_state"): str,
                        Optional("sm_bend_state"): str,
                        Optional("authen_status"): str
                    }
                }
            },
            "local_policies": {
                "service_template": {
                    Any(): {
                        Optional("vlan_group"): str,
                        Optional("vlan"): Or(int, str),
                        "absolute_timer": int
                    }
                }
            },
            "server_policies": {
                Optional("output_sgt"): str,
                Optional("url_redirect_acl"): str,
                Optional("url_redirect"): str,
                Optional("vlan"): Or(int, str)
            },
            "resultant_policies": {
                Optional("output_sgt"): str,
                "vlan_name": str,
                Optional("vlan_group"): str,
                "vlan": Or(int, str),
                "absolute_timer": int,
                Optional("url_redirect_acl"): str,
                Optional("url_redirect"): str,
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
        Optional("flexconnect_central_association"): str,
        "client_statistics": {
            "number_of_bytes_received": int,
            "number_of_bytes_sent": int,
            "number_of_packets_received": int,
            "number_of_packets_sent": int,
            "number_of_policy_errors": int,
            "radio_signal_strength_indicator_dbm": int,
            "signal_to_noise_ration_db": int
        },
        "fabric_status": str,
        "radio_measurement_enabled_capabilities": {
            "capabilities": list
        },
        "client_scan_report_time": str,
        "nearby_ap_statistics": {
            Optional("ap_names"): {
                Optional(Any()): {
                    Optional("antenna"): {
                        Optional(Any()): {
                            Optional("seconds_ago"): int,
                            Optional("dbm"): int
                        }
                    }
                }
            }
        },
        "eogre": str,
        Optional("device_info"): {
            "device_type": str,
            "device_name": str,
            "protocol_map": str,
            Optional("device_os"): str,
            "protocols": {
                Any(): {
                    Any(): {
                        "type": str,
                        "data_size": str,
                        "data": list
                    }
                }
            }
        },
        Optional("max_client_protocol_capability"): str,
        "cellular_capability": str,
        Optional("session_warning_time"): str,
        Optional("session_timeout"): str,
        Optional("advanced_scheduling_requests_details"): {
            Any(): {
                Optional("regular_asr_support"): str
            }
        }
    }


# ====================================
# Parser for:
#  * 'show wireless client mac {mac_address} detail'
# ====================================
class ShowWirelessClientMacDetail(ShowWirelessClientMacDetailSchema):
    """
    Parser for show wireless client mac {mac_address} detail

    arguments:
    mac_address: mac address of the device to be checked, looks like xxxx.yyyy.zzzz
    """

    cli_command = 'show wireless client mac {mac_address} detail'

    def cli(self, mac_address="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mac_address=mac_address))
        else:
            output = output

        # Client Mac Address : abcd:1234:dcba
        # Client IPv6 Addresses : fe80::1
        p0 = re.compile(r'^Client (?P<address_type>\S+) (Address|Addresses) : (?P<address>[\S]+)$')

        # Client MAC Type : Locally Administered Address
        p1 = re.compile(r'^Client MAC Type : (?P<client_mac_type>[\S ]+)$')

        p2 = re.compile(r'^Client Username *: (?P<client_username>\S+)')

        # AP MAC Address : bead:4321:dead
        p3 = re.compile(r'^AP MAC Address : (?P<ap_mac_address>\S+)$')

        # AP Name: b1-11-cap9
        p4 = re.compile(r'^AP Name: (?P<ap_name>\S+)$')

        # AP slot : 0
        p5 = re.compile(r'^AP slot : (?P<ap_slot>\d+)$')

        # Client State : Associated
        p6 = re.compile(r'^Client State : (?P<client_state>\S+)$')

        # Policy Profile : profile_1
        p7 = re.compile(r'^Policy Profile : (?P<policy_profile>\S+)$')

        # Flex Profile : N/A
        p8 = re.compile(r'^Flex Profile : (?P<flex_profile>\S+)$')

        # Wireless LAN Id: 20
        p9 = re.compile(r'^Wireless LAN Id: (?P<wireless_lan_id>\d+)$')

        # WLAN Profile Name: lizzard-l_Global
        p10 = re.compile(r'^WLAN Profile Name: (?P<wlan_profile_name>\S+)$')

        # Wireless LAN Network Name (SSID): lizzard-legacy
        p11 = re.compile(r'^Wireless LAN Network Name \(SSID\): (?P<wireless_lan_network_name_ssid>\S+)$')

        # BSSID : 70b3.18ff.f478
        p12 = re.compile(r'^BSSID : (?P<bssid>\S+)$')

        # Connected For : 3233 seconds
        p13 = re.compile(r'^Connected For : (?P<connected_for_seconds>\d+) seconds$')

        # Protocol : 802.11n - 2.4 GHz
        p14 = re.compile(r'^Protocol +: (?P<protocol>[\S ]+)$')

        # Protocol : 802.11n - 2.4 GHz
        p14_1 = re.compile(r'^Device Protocol +: (?P<protocol>[\S ]+)$')

        # Channel : 6
        p15 = re.compile(r'^Channel : (?P<channel>\d+)$')

        # Client IIF-ID : 0xa0000001
        p16 = re.compile(r'^Client IIF-ID : (?P<client_iif_id>\S+)$')

        # Association Id : 1
        p17 = re.compile(r'^Association Id : (?P<association_id>\d+)$')

        # Authentication Algorithm : Open System
        p18 = re.compile(r'^Authentication Algorithm : (?P<authentication_alogrithm>[\S ]+)$')

        # Idle state timeout : N/A
        p19 = re.compile(r'^Idle state timeout : (?P<idle_state_timeout>\S+)$')

        # Re-Authentication Timeout : 36000 sec (Remaining time: 32768 sec)
        p20 = re.compile(r'^Re-Authentication Timeout : (?P<configured>\d+) sec '
                         r'\(Remaining time: (?P<remaining_time>\d+) sec\)$')

        # Session Warning Time : Timer not running
        p21 = re.compile(r'^Session Warning Time : (?P<session_warning_time>[\S ]+)$')

        # Session Timeout : 1800 sec (Timer not running)
        p21_1 = re.compile(r'^Session Timeout : (?P<session_timeout>[\S ]+)$')

        # Input Policy Name  : client-default
        p22 = re.compile(r'^Input Policy Name +: (?P<input_policy_name>\S+)$')

        # Input Policy State : Installed
        p23 = re.compile(r'^Input Policy State : (?P<input_policy_state>\S+)$')

        # Input Policy Source : QOS Internal Policy
        p24 = re.compile(r'^Input Policy Source : (?P<input_policy_source>[\S ]+)$')

        # Output Policy Name  : client-default
        p25 = re.compile(r'^Output Policy Name +: (?P<output_policy_name>\S+)$')

        # Output Policy State : Installed
        p26 = re.compile(r'^Output Policy State : (?P<output_policy_state>\S+)$')

        # Output Policy Source : QOS Internal Policy
        p27 = re.compile(r'^Output Policy Source : (?P<output_policy_source>[\S ]+)$')

        # WMM Support : Enabled
        p28 = re.compile(r'^WMM Support : (?P<wmm_support>\S+)$')

        # U-APSD Support : Enabled
        p29 = re.compile(r'^U-APSD Support : (?P<status>\S+)$')

        #   U-APSD value : 0
        p29_1 = re.compile(r'^U-APSD value : (?P<u_apsd_value>\d+)$')

        #   APSD ACs    : BK, BE, VI, VO
        p29_2 = re.compile(r'^APSD ACs +: (?P<apsd_acs>[\S ]+)$')

        # Fastlane Support : Disabled
        p30 = re.compile(r'^Fastlane Support : (?P<fastlane_support>\S+)$')

        # Client Active State : In-Active
        p31 = re.compile(r'^Client Active State : (?P<client_active_state>\S+)$')

        # Power Save : ON
        p32 = re.compile(r'^Power Save : (?P<power_save>\S+)$')

        # Current Rate : 6.0
        p33 = re.compile(r'^Current Rate : (?P<current_rate>[\S ]+)$')

        # Supported Rates : 24.0,36.0,48.0,54.0
        p34 = re.compile(r'^Supported Rates : (?P<supported_rates>\S+)$')

        # AAA QoS Rate Limit Parameters:
        #   QoS Average Data Rate Upstream             : 0 (kbps)
        #   QoS Realtime Average Data Rate Upstream    : 0 (kbps)
        #   QoS Burst Data Rate Upstream               : 0 (kbps)
        #   QoS Realtime Burst Data Rate Upstream      : 0 (kbps)
        #   QoS Average Data Rate Downstream           : 0 (kbps)
        #   QoS Realtime Average Data Rate Downstream  : 0 (kbps)
        #   QoS Burst Data Rate Downstream             : 0 (kbps)
        #   QoS Realtime Burst Data Rate Downstream    : 0 (kbps)
        p35 = re.compile(r'^QoS (?P<type>(Average|Realtime Average|Burst|Realtime Burst)) Data Rate '
                         r'(?P<direction>(Upstream|Downstream)) +: (?P<rate>\d+) \(kbps\)$')

        # Mobility:
        #   Move Count                  : 0
        #   Mobility Role               : Local
        #   Mobility Roam Type          : None
        #   Mobility Complete Timestamp : 10/22/2020 08:07:55 IST
        p36 = re.compile(r'^Move Count +: (?P<move_count>\d+)$')
        p36_1 = re.compile(r'^Mobility (?P<type>Role|Roam Type|Complete Timestamp) +: (?P<value>\S+$|[\S ]+$)')

        # Client Join Time:
        #   Join Time Of Client : 10/22/2020 08:46:54 IST
        p37 = re.compile(r'^Join Time Of Client : (?P<client_join_time>[\S ]+)$')

        # Client State Servers : None
        p38 = re.compile(r'^Client State Servers : (?P<client_state_servers>\S+)$')

        # Client ACLs : None
        p39 = re.compile(r'^Client ACLs : (?P<client_acls>\S+)$')

        # Policy Manager State: Webauth Pending
        p40 = re.compile(r'^Policy Manager State: (?P<policy_manager_state>[\S ]+)$')

        # Last Policy Manager State : IP Learn Complete
        p41 = re.compile(r'^Last Policy Manager State : (?P<last_policy_manager_state>[\S ]+)$')

        # Client Entry Create Time : 5572 seconds
        p42 = re.compile(r'^Client Entry Create Time : (?P<client_entry_create_time_secs>\d+) seconds$')

        # Policy Type : WPA2
        p43 = re.compile(r'^Policy Type : (?P<policy_type>\S+)$')

        # Encryption Cipher : CCMP (AES)
        p44 = re.compile(r'^Encryption Cipher : (?P<encryption_cipher>[\S ]+)$')

        # Authentication Key Management : 802.1x
        p45 = re.compile(r'^Authentication Key Management : (?P<authentication_key_management>\S+)$')

        # User Defined (Private) Network : Disabled
        p46 = re.compile(r'^User Defined \(Private\) Network : (?P<user_defined_private_network>\S+)$')

        # User Defined (Private) Network Drop Unicast : Disabled
        p46_1 = re.compile(r'^User Defined \(Private\) Network Drop Unicast : '
                           r'(?P<user_defined_private_network_drop_unicast>\S+)$')

        # Encrypted Traffic Analytics : No
        p47 = re.compile(r'^Encrypted Traffic Analytics : (?P<encrypted_traffic_analytics>\S+)$')

        # Protected Management Frame - 802.11w : No
        p48 = re.compile(r'^Protected Management Frame - 802.11w : (?P<protected_management_frame>\S+)')

        # EAP Type : PEAP
        p49 = re.compile(r'^EAP Type : (?P<eap_type>[\S ]+)$')

        # VLAN Override after Webauth : No
        p50 = re.compile(r'^VLAN Override after Webauth : (?P<vlan_override_after_webauth>\S+)$')

        # VLAN : b1-vg-data
        p51 = re.compile(r'^VLAN +: (?P<vlan>\S+)$')

        # Multicast VLAN : 0
        p52 = re.compile(r'^Multicast VLAN : (?P<multicast_vlan>\d+)$')

        # WiFi Direct Capabilities:
        #   WiFi Direct Capable           : No
        p53 = re.compile(r'^WiFi Direct Capable +: (?P<wifi_direct_capable>\S+)$')

        # Central NAT : DISABLED
        p54 = re.compile(r'^Central NAT : (?P<central_nat>\S+)$')

        # Session Manager:
        p55 = re.compile(r'^Session Manager:$')

        #   Point of Attachment : capwap_00000aa1
        p55_1 = re.compile(r'^Point of Attachment : (?P<point_of_attachment>\S+)$')

        #   IIF ID             : 0x00000AA1
        p55_2 = re.compile(r'^IIF ID +: (?P<iif_id>\S+)$')

        #   Authorized         : TRUE
        p55_3 = re.compile(r'^Authorized +: (?P<authorized>\S+)$')

        #   Session timeout    : 36000
        # Not to be confused with "Session Timeout" which is captured by p22_1
        p55_4 = re.compile(r'^Session timeout +: (?P<session_timeout>\S+)$')

        #   Common Session ID: B12A400A000007000000700A
        p55_5 = re.compile(r'^Common Session ID: (?P<common_session_id>\S+)$')

        #   Acct Session ID  : 0x00005512
        p55_6 = re.compile(r'^Acct Session ID +: (?P<acct_session_id>\S+)$')
        #   Last Tried Aaa Server Details:
        #   	Server IP : 10.11.12.13
        p55_7 = re.compile(r'^Server IP +: (?P<server_ip>\S+)$')

        #   Auth Method Status List
        #   	Method : Dot1x
        p56 = re.compile(r'^Method : (?P<method>\S+)$')

        #   		SM State         : AUTHENTICATED
        p56_1 = re.compile(r'^SM State +: (?P<sm_state>\S+)$')

        #   		SM Bend State    : IDLE
        p56_2 = re.compile(r'^SM Bend State +: (?P<sm_bend_state>\S+)$')

        #           Authen Status   : Success
        p56_3 = re.compile(r'^Authen Status +: (?P<authen_status>\S+)$')

        #   Local Policies:
        #   	Service Template : wlan_service_template_local (priority 254)
        p57 = re.compile(r'^Local Policies:$')
        p57_1 = re.compile(r'^Service Template : (?P<service_template>[\S ]+)$')

        #   Server Policies:
        p58 = re.compile(r'^Server Policies:$')

        #   Resultant Policies:
        p59 = re.compile(r'^Resultant Policies:$')

        #   		Vlan Group       : data-group
        p60 = re.compile(r'^Vlan Group +: (?P<vlan_group>\S+)$')

        #   		Absolute-Timer   : 36000
        p61 = re.compile(r'^Absolute-Timer +: (?P<absolute_timer>\d+)$')

        #   		Output SGT       : 000a-09
        p62 = re.compile(r'^Output SGT +: (?P<output_sgt>\S+)$')

        #   		VLAN Name        : b1-data-1
        p63 = re.compile(r'^VLAN Name +: (?P<vlan_name>\S+)$')

        #                 URL Redirect ACL : ACL_WEBAUTH_REDIRECT
        p64 = re.compile(r'^URL Redirect ACL : (?P<url_redirect_acl>\S+)$')

        #                 URL Redirect     : https://web.address:8443/portal/gateway
        p65 = re.compile(r'URL Redirect +: (?P<url_redirect>\S+)$')

        # DNS Snooped IPv4 Addresses : None
        # DNS Snooped IPv6 Addresses : None
        p66 = re.compile(r'^DNS Snooped (?P<ip_ver>(IPv4|IPv6)) Addresses : (?P<addresses>\S+)$')

        # Client Capabilities
        #   CF Pollable : Not implemented
        p67 = re.compile(r'^CF Pollable : (?P<cf_pollable>[\S ]+)$')

        #   CF Poll Request : Not implemented
        p67_1 = re.compile(r'^CF Poll Request : (?P<cf_poll_request>[\S ]+)$')

        #   Short Preamble : Not implemented
        p67_2 = re.compile(r'^Short Preamble : (?P<short_preamble>[\S ]+)$')

        #   PBCC : Not implemented
        p67_3 = re.compile(r'^PBCC : (?P<pbcc>[\S ]+)$')

        #   Channel Agility : Not implemented
        p67_4 = re.compile(r'^Channel Agility : (?P<channel_agility>[\S ]+)$')

        #   Listen Interval : 0
        p67_5 = re.compile(r'^Listen Interval : (?P<listen_interval>\d+)$')

        # Fast BSS Transition Details :
        #   Reassociation Timeout : 0
        p68 = re.compile(r'^Reassociation Timeout : (?P<reassociation_timeout>\d+)$')

        # 11v BSS Transition : Implemented
        p69 = re.compile(r'^11v BSS Transition : (?P<bss_transition>[\S ]+)$')

        # 11v DMS Capable : No
        p70 = re.compile(r'^11v DMS Capable : (?P<dms_capable>\S+)$')

        # QoS Map Capable : No
        p71 = re.compile(r'^QoS Map Capable : (?P<qos_map_capable>\S+)$')

        # FlexConnect Data Switching : N/A
        # FlexConnect Dhcp Status : N/A
        # FlexConnect Authentication : N/A
        # FlexConnect Central Association : N/A
        p72 = re.compile(r'^FlexConnect (?P<type>.+?) : (?P<value>\S+)$')

        # Client Statistics:
        #   Number of Bytes Received : 3083748
        #   Number of Bytes Sent : 2063114
        #   Number of Packets Received : 9048
        #   Number of Packets Sent : 3686
        # Client Statistics:
        #   Number of Bytes Received : 3083748
        #   Number of Bytes Sent : 2063114
        #   Number of Packets Received : 9048
        #   Number of Packets Sent : 3686
        #   Number of Policy Errors : 0
        p73 = re.compile(r'^Number of (?P<item>(Bytes|Packets)) (?P<direction>(Sent|Received)) ((to|from) Client )?: '
                         r'(?P<value>\d+)$')

        #   Number of Policy Errors : 0
        p73_1 = re.compile(r'^Number of Policy Errors : (?P<number_of_policy_errors>\d+)$')

        #   Radio Signal Strength Indicator : -84 dBm
        p73_2 = re.compile(r'^Radio Signal Strength Indicator : (?P<rssi>[\d-]+) dBm$')

        #   Signal to Noise Ratio : 10 dB
        p73_3 = re.compile(r'Signal to Noise Ratio : (?P<snr>\d+) dB$')

        # Fabric status : Disabled
        p74 = re.compile(r'^Fabric status : (?P<fabric_status>\S+)$')

        # Radio Measurement Enabled Capabilities
        #   Capabilities: Link Measurement, Neighbor Report, Repeated Measurements, Passive Beacon Measurement, RM MIB
        p75 = re.compile(r'^Capabilities: (?P<capabilities>[\S ]+)$')

        # Client Scan Report Time : Timer not running
        p76 = re.compile(r'^Client Scan Report Time : (?P<client_scan_report_time>[\S ]+)$')

        # Nearby AP Statistics:
        #   prateekk_cos_1 (slot 1)
        #   	antenna 0: 13 s ago	........ -25  dBm
        #   	antenna 1: 13 s ago	........ -25  dBm
        p77 = re.compile(r'^Nearby AP Statistics:$')
        p77_1 = re.compile(r'^(?P<ap_name>\S+) \(slot (?P<slot>\d+)\)$')
        p77_2 = re.compile(r'^antenna (?P<antenna>\d+): (?P<time>\d+) s ago\s\.+ (?P<rssi>[\d-]+) +dBm$')

        # EoGRE : Pending Classification
        p78 = re.compile(r'^EoGRE : (?P<eogre>[\S ]+)$')

        # Device Classification Information:
        # Device Type      : Android
        p79 = re.compile(r'^Device Type +: (?P<device_type>[\S ]+)$')

        # Device Name      : android-dhcp-10
        # Device Name      : MSFT 5.0
        p79_1 = re.compile(r'^Device Name +: (?P<device_name>[\S ]+)$')

        # Protocol Map     : 0x000029  (OUI, DHCP, HTTP)
        p79_2 = re.compile(r'^Protocol Map +: (?P<protocol_map>[\S ]+)$')

        # Device OS        : Linux; U; Android 10; RMX1825 Build/QP1A.190711.020
        p79_3 = re.compile(r'^Device OS +: (?P<device_os>.+?)$')

        # Type             : 12   12
        p79_4 = re.compile(r'^Type +: (?P<type>[\d ]+)$')

        # Data             : 0c
        p79_5 = re.compile(r'^Data +: (?P<data_size>[\da-f]+)$')

        # 00000000  00 0c 00 08 72 65 61 6c  6d 65 2d 33               |....realme-3    |
        # 00000030  42 75 69 6c 64 2f 51 50  31 41 2e 31 39 30 37 31  |Build/QP1A.19071|
        # 00000010  44 4a 30                                          |DJ0             |
        p79_6 = re.compile(r'^(?P<byte>\d{8}) +(?P<hex>[\da-f ]+?) +(?P<piped>\|.+)$')

        # Max Client Protocol Capability: 802.11ac Wave 2
        p80 = re.compile(r'^Max Client Protocol Capability: (?P<max_client_protocol_capability>[\S ]+)$')

        # Cellular Capability : N/A
        p81 = re.compile(r'^Cellular Capability : (?P<cellular_capability>[\S ]+)$')

        # Advanced Scheduling Requests Details:
        #   Apple Specific Requests(ASR) Capabilities/Statistics:
        #     Regular ASR support: DISABLED
        p82 = re.compile(r'^Advanced Scheduling Requests Details:$')
        p82_1 = re.compile(r'^(?P<request_type>Apple Specific Requests.+?):$')
        p82_2 = re.compile(r'^Regular ASR support: (?P<regular_asr_support>\S+)$')

        ret_dict = {}
        local_policies, server_policies, resultant_policies = None, None, None
        device_info = None
        data_index = None
        for line in output.splitlines():
            line = line.strip()

            # Client Mac Address : abcd:1234:dcba
            # Client IPv6 Addresses : fe80::1
            m = p0.match(line)
            if m:
                address_type = m.groupdict()['address_type'].lower()
                address = m.groupdict()['address']

                if address_type == "ipv6":
                    ret_dict.update({f"client_{address_type}_addresses": address})
                else:
                    ret_dict.update({f"client_{address_type}_address": address})
                continue

            # Client MAC Type : Locally Administered Address
            m = p1.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Client Username : j_doe
            m = p2.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # AP MAC Address : bead:4321:dead
            m = p3.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # AP Name: ap1
            m = p4.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # AP slot : 0
            m = p5.match(line)
            if m:
                ret_dict.update({"ap_slot": int(m.groupdict()['ap_slot'])})
                continue

            # Client State : Associated
            m = p6.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Policy Profile : profile_1
            m = p7.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Flex Profile : N/A
            m = p8.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Wireless LAN Id: 20
            m = p9.match(line)
            if m:
                ret_dict.update({"wireless_lan_id": int(m.groupdict()['wireless_lan_id'])})
                continue

            # WLAN Profile Name: global_profile
            m = p10.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Wireless LAN Network Name (SSID): legitimate-wifi
            m = p11.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # BSSID : 70b3.18ff.f478
            m = p12.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Connected For : 3233 seconds
            m = p13.match(line)
            if m:
                ret_dict.update({"connected_for_seconds": int(m.groupdict()['connected_for_seconds'])})
                continue

            # Protocol : 802.11n - 2.4 GHz
            # Protocol         : DHCP
            m = p14.match(line)
            if m:
                if device_info:
                    protocol_dict = device_info_dict.setdefault("protocols", {}). \
                        setdefault(m.groupdict()['protocol'], {})
                    data_index = None
                    continue
                ret_dict.update(m.groupdict())
                continue

            # Device Protocol  : DHCP
            m = p14_1.match(line)
            if m:
                if device_info:
                    protocol_dict = device_info_dict.setdefault("protocols", {}). \
                        setdefault(m.groupdict()['protocol'], {})
                    data_index = None
                continue

            # Channel : 6
            m = p15.match(line)
            if m:
                ret_dict.update({"channel": int(m.groupdict()['channel'])})
                continue

            # Client IIF-ID : 0xa0000001
            m = p16.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Association Id : 1
            m = p17.match(line)
            if m:
                ret_dict.update({"association_id": int(m.groupdict()['association_id'])})
                continue

            # Authentication Algorithm : Open System
            m = p18.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Idle state timeout : N/A
            m = p19.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Re-Authentication Timeout : 36000 sec (Remaining time: 32768 sec)
            m = p20.match(line)
            if m:
                reauthentication_dict = ret_dict.setdefault("re_authentication_timeout_secs", {})
                reauthentication_dict.update({
                    "configured": int(m.groupdict()['configured']),
                    "remaining_time": int(m.groupdict()['remaining_time'])
                })
                continue

            # Session Warning Time : Timer not running
            m = p21.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Session Timeout : 1800 sec (Timer not running)
            m = p21_1.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Input Policy Name  : client-default
            m = p22.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Input Policy State : Installed
            m = p23.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Input Policy Source : QOS Internal Policy
            m = p24.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Output Policy Name  : client-default
            m = p25.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Output Policy State : Installed
            m = p26.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Output Policy Source : QOS Internal Policy
            m = p27.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # WMM Support : Enabled
            m = p28.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # U-APSD Support : Enabled
            m = p29.match(line)
            if m:
                u_apsd_dict = ret_dict.setdefault("u_apsd_support", {})
                u_apsd_dict.update({"status": m.groupdict()['status']})
                continue

            #   U-APSD value : 0
            m = p29_1.match(line)
            if m:
                u_apsd_dict.update({"u_apsd_value": int(m.groupdict()['u_apsd_value'])})
                continue

            #   APSD ACs    : BK, BE, VI, VO
            m = p29_2.match(line)
            if m:
                apsd_acs = m.groupdict()['apsd_acs'].split(', ')
                u_apsd_dict.update({"apsd_acs": apsd_acs})
                continue

            # Fastlane Support : Disabled
            m = p30.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Client Active State : In-Active
            m = p31.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Power Save : ON
            m = p32.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Current Rate : 6.0
            m = p33.match(line)
            if m:
                try:
                    current_rate = float(m.groupdict()['current_rate'])
                except ValueError:
                    current_rate = m.groupdict()['current_rate']
                ret_dict.update({"current_rate": current_rate})
                continue

            # Supported Rates : 24.0,36.0,48.0,54.0
            m = p34.match(line)
            if m:
                supported_rates = [float(rate) for rate in m.groupdict()['supported_rates'].split(',')]
                ret_dict.update({"supported_rates": supported_rates})
                continue

            # AAA QoS Rate Limit Parameters:
            #   QoS Average Data Rate Upstream             : 0 (kbps)
            #   QoS Realtime Average Data Rate Upstream    : 0 (kbps)
            #   QoS Burst Data Rate Upstream               : 0 (kbps)
            #   QoS Realtime Burst Data Rate Upstream      : 0 (kbps)
            #   QoS Average Data Rate Downstream           : 0 (kbps)
            #   QoS Realtime Average Data Rate Downstream  : 0 (kbps)
            #   QoS Burst Data Rate Downstream             : 0 (kbps)
            #   QoS Realtime Burst Data Rate Downstream    : 0 (kbps)
            m = p35.match(line)
            if m:
                qos_rate_limit_dict = ret_dict.setdefault("aaa_qos_rate_limit_parameters", {})

                group = {k: v.lower() for k, v in m.groupdict().items()}
                limit_type = f"qos_{group['type'].replace(' ', '_')}_data_rate_kbps"

                if group['direction'] == "upstream":
                    qos_upstream_dict = qos_rate_limit_dict.setdefault("upstream", {})
                    qos_upstream_dict.update({limit_type: int(group['rate'])})
                elif group['direction'] == "downstream":
                    qos_downstream_dict = qos_rate_limit_dict.setdefault("downstream", {})
                    qos_downstream_dict.update({limit_type: int(group['rate'])})
                continue

            # Mobility:
            #   Move Count                  : 0
            m = p36.match(line)
            if m:
                mobility_dict = ret_dict.setdefault("mobility", {})
                mobility_dict.update({"move_count": int(m.groupdict()['move_count'])})
                continue

            #   Mobility Role               : Local
            #   Mobility Roam Type          : None
            #   Mobility Complete Timestamp : 10/22/2020 08:07:55 IST
            m = p36_1.match(line)
            if m:
                type = m.groupdict()['type'].lower().replace(' ', '_')
                mobility_dict.update({f"mobility_{type}": m.groupdict()['value']})
                continue

            # Client Join Time:
            #   Join Time Of Client : 10/22/2020 08:46:54 IST
            m = p37.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Client State Servers : None
            m = p38.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Client ACLs : None
            m = p39.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Policy Manager State: Webauth Pending
            m = p40.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Last Policy Manager State : IP Learn Complete
            m = p41.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Client Entry Create Time : 5572 seconds
            m = p42.match(line)
            if m:
                ret_dict.update({"client_entry_create_time_secs": int(m.groupdict()['client_entry_create_time_secs'])})
                continue

            # Policy Type : WPA2
            m = p43.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Encryption Cipher : CCMP (AES)
            m = p44.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Authentication Key Management : 802.1x
            m = p45.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # User Defined (Private) Network : Disabled
            m = p46.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # User Defined (Private) Network Drop Unicast : Disabled
            m = p46_1.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Encrypted Traffic Analytics : No
            m = p47.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Protected Management Frame - 802.11w : No
            m = p48.match(line)
            if m:
                ret_dict.update({"protected_management_frame__802.11w": m.groupdict()['protected_management_frame']})
                continue

            # EAP Type : PEAP
            m = p49.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # VLAN Override after Webauth : No
            m = p50.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # VLAN : b1-vg-data
            # VLAN             : 20
            m = p51.match(line)
            if m:
                try:
                    vlan = int(m.groupdict()['vlan'])
                except ValueError:
                    vlan = m.groupdict()['vlan']
                if local_policies:
                    local_policies_dict.update({"vlan": vlan})
                elif server_policies:
                    server_policies_dict.update({"vlan": vlan})
                elif resultant_policies:
                    resultant_policies_dict.update({"vlan": vlan})
                else:
                    ret_dict.update({"vlan": vlan})
                continue

            # Multicast VLAN : 0
            m = p52.match(line)
            if m:
                ret_dict.update({"multicast_vlan": int(m.groupdict()['multicast_vlan'])})
                continue

            # WiFi Direct Capabilities:
            #   WiFi Direct Capable           : No
            m = p53.match(line)
            if m:
                wifi_direct_dict = ret_dict.setdefault("wifi_direct_capabilities", {})
                wifi_direct_dict.update(m.groupdict())
                continue

            # Central NAT : DISABLED
            m = p54.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Session Manager:
            m = p55.match(line)
            if m:
                session_dict = ret_dict.setdefault("session_manager", {})
                continue

            #   Point of Attachment : capwap_00000aa1
            m = p55_1.match(line)
            if m:
                session_dict.update(m.groupdict())
                continue

            #   IIF ID             : 0x00000AA1
            m = p55_2.match(line)
            if m:
                session_dict.update(m.groupdict())
                continue

            #   Authorized         : TRUE
            m = p55_3.match(line)
            if m:
                session_dict.update(m.groupdict())
                continue

            #   Session timeout    : 36000
            m = p55_4.match(line)
            if m:
                session_dict.update({"session_timeout": int(m.groupdict()['session_timeout'])})
                continue

            #   Common Session ID: B12A400A000007000000700A
            m = p55_5.match(line)
            if m:
                session_dict.update(m.groupdict())
                continue

            #   Acct Session ID  : 0x00005512
            m = p55_6.match(line)
            if m:
                session_dict.update(m.groupdict())
                continue

            #   Last Tried Aaa Server Details:
            #   	Server IP : 10.11.12.13
            m = p55_7.match(line)
            if m:
                session_dict.update({"last_tried_aaa_server_details": m.groupdict()})
                continue

            #   Auth Method Status List
            #   	Method : Dot1x
            m = p56.match(line)
            if m:
                auth_method_status_dict = session_dict.setdefault("auth_method_status_list", {}). \
                    setdefault('method', {}).setdefault(m.groupdict()['method'], {})
                continue

            #   		SM State         : AUTHENTICATED
            m = p56_1.match(line)
            if m:
                auth_method_status_dict.update(m.groupdict())
                continue

            #   		SM Bend State    : IDLE
            m = p56_2.match(line)
            if m:
                auth_method_status_dict.update(m.groupdict())
                continue

            #           Authen Status   : Success
            m = p56_3.match(line)
            if m:
                auth_method_status_dict.update(m.groupdict())
                continue

            #   Local Policies:
            if p57.match(line):
                local_policies_dict = session_dict.setdefault("local_policies", {}).setdefault("service_template", {})
                local_policies = True
                continue

            #   	Service Template : wlan_service_template_local (priority 254)
            m = p57_1.match(line)
            if m:
                local_policies_dict = local_policies_dict.setdefault(m.groupdict()['service_template'], {})
                continue

            #   Server Policies:
            if p58.match(line):
                server_policies_dict = session_dict.setdefault("server_policies", {})
                local_policies = None
                server_policies = True
                continue

            #   Resultant Policies:
            if p59.match(line):
                resultant_policies_dict = session_dict.setdefault("resultant_policies", {})
                server_policies = None
                resultant_policies = True
                continue

            #   		Vlan Group       : data-group
            m = p60.match(line)
            if m:
                if local_policies:
                    local_policies_dict.update(m.groupdict())
                    continue
                if resultant_policies:
                    resultant_policies_dict.update(m.groupdict())
                    continue

            #   		Absolute-Timer   : 36000
            m = p61.match(line)
            if m:
                if local_policies:
                    local_policies_dict.update({"absolute_timer": int(m.groupdict()['absolute_timer'])})
                    continue
                if resultant_policies:
                    resultant_policies_dict.update({"absolute_timer": int(m.groupdict()['absolute_timer'])})
                    continue

            #   		Output SGT       : 000a-09
            m = p62.match(line)
            if m:
                if server_policies:
                    server_policies_dict.update(m.groupdict())
                    continue
                if resultant_policies:
                    resultant_policies_dict.update(m.groupdict())
                    continue

            #   		VLAN Name        : b1-data-1
            m = p63.match(line)
            if m:
                resultant_policies_dict.update(m.groupdict())
                continue

            #                 URL Redirect ACL : ACL_WEBAUTH_REDIRECT
            m = p64.match(line)
            if m:
                if server_policies:
                    server_policies_dict.update(m.groupdict())
                    continue
                if resultant_policies:
                    resultant_policies_dict.update(m.groupdict())
                    continue

            #                 URL Redirect     : https://web.address:8443/portal/gateway
            m = p65.match(line)
            if m:
                if server_policies:
                    server_policies_dict.update(m.groupdict())
                    continue
                if resultant_policies:
                    resultant_policies_dict.update(m.groupdict())
                    continue

            # DNS Snooped IPv4 Addresses : None
            # DNS Snooped IPv6 Addresses : None
            m = p66.match(line)
            if m:
                ip_version = m.groupdict()['ip_ver'].lower()
                ret_dict.update({f"dns_snooped_{ip_version}_addresses": m.groupdict()['addresses']})
                continue

            # Client Capabilities
            #   CF Pollable : Not implemented
            m = p67.match(line)
            if m:
                client_capabilites_dict = ret_dict.setdefault("client_capabilities", {})
                client_capabilites_dict.update(m.groupdict())
                continue

            #   CF Poll Request : Not implemented
            m = p67_1.match(line)
            if m:
                client_capabilites_dict.update(m.groupdict())
                continue

            #   Short Preamble : Not implemented
            m = p67_2.match(line)
            if m:
                client_capabilites_dict.update(m.groupdict())
                continue

            #   PBCC : Not implemented
            m = p67_3.match(line)
            if m:
                client_capabilites_dict.update(m.groupdict())
                continue

            #   Channel Agility : Not implemented
            m = p67_4.match(line)
            if m:
                client_capabilites_dict.update(m.groupdict())
                continue

            #   Listen Interval : 0
            m = p67_5.match(line)
            if m:
                client_capabilites_dict.update({"listen_interval": int(m.groupdict()['listen_interval'])})
                continue

            # Fast BSS Transition Details :
            #   Reassociation Timeout : 0
            m = p68.match(line)
            if m:
                fast_bss_transition_dict = ret_dict.setdefault("fast_bss_transition_details", {})
                fast_bss_transition_dict.update({"reassociation_timeout": int(m.groupdict()['reassociation_timeout'])})
                continue

            # 11v BSS Transition : Implemented
            m = p69.match(line)
            if m:
                ret_dict.update({"11v_bss_transition": m.groupdict()['bss_transition']})
                continue

            # 11v DMS Capable : No
            m = p70.match(line)
            if m:
                ret_dict.update({"11v_dms_capable": m.groupdict()['dms_capable']})
                continue

            # QoS Map Capable : No
            m = p71.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # FlexConnect Data Switching : Central
            # FlexConnect Dhcp Status : N/A
            # FlexConnect Authentication : N/A
            # FlexConnect Central Association : N/A
            m = p72.match(line)
            if m:
                flexconnect_key = f"flexconnect_{m.groupdict()['type'].lower().replace(' ', '_')}"
                ret_dict.update({flexconnect_key: m.groupdict()['value']})
                continue

            # Client Statistics:
            #   Number of Bytes Received : 3083748
            #   Number of Bytes Sent : 2063114
            #   Number of Packets Received : 9048
            #   Number of Packets Sent : 3686
            #
            # Client Statistics:
            #   Number of Bytes Received : 3083748
            #   Number of Bytes Sent : 2063114
            #   Number of Packets Received : 9048
            #   Number of Packets Sent : 3686
            #   Number of Policy Errors : 0
            m = p73.match(line)
            if m:
                client_statistics_dict = ret_dict.setdefault("client_statistics", {})

                key = f"number_of_{m.groupdict()['item'].lower()}_{m.groupdict()['direction'].lower()}"
                client_statistics_dict.update({key: int(m.groupdict()['value'])})
                continue

            #   Number of Policy Errors : 0
            m = p73_1.match(line)
            if m:
                client_statistics_dict.update({
                    "number_of_policy_errors": int(m.groupdict()['number_of_policy_errors'])
                })
                continue

            #   Radio Signal Strength Indicator : -84 dBm
            m = p73_2.match(line)
            if m:
                client_statistics_dict.update({"radio_signal_strength_indicator_dbm": int(m.groupdict()['rssi'])})
                continue

            #   Signal to Noise Ratio : 10 dB
            m = p73_3.match(line)
            if m:
                client_statistics_dict.update({"signal_to_noise_ration_db": int(m.groupdict()['snr'])})
                continue

            # Fabric status : Disabled
            m = p74.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Radio Measurement Enabled Capabilities
            #   Capabilities: Link Measurement, Neighbor Report, Repeated Measurements, Passive Beacon Measurement
            m = p75.match(line)
            if m:
                radio_measurement_capabilities_dict = ret_dict.setdefault("radio_measurement_enabled_capabilities", {})
                radio_measurement_capabilities_dict.update({
                    "capabilities": [capability for capability in m.groupdict()['capabilities'].split(', ')]
                })
                continue

            # Client Scan Report Time : Timer not running
            m = p76.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Nearby AP Statistics:
            if p77.match(line):
                nearby_ap_dict = ret_dict.setdefault("nearby_ap_statistics", {})
                continue

            #   prateekk_cos_1 (slot 1)
            m = p77_1.match(line)
            if m:
                ap_name = line
                ap_dict = nearby_ap_dict.setdefault("ap_names", {}).setdefault(ap_name, {})
                continue

            #   	antenna 0: 13 s ago	........ -25  dBm
            #   	antenna 1: 13 s ago	........ -25  dBm
            m = p77_2.match(line)
            if m:
                antenna_dict = ap_dict.setdefault("antenna", {})
                antenna_dict.update({
                    f"antenna {m.groupdict()['antenna']}": {
                        "seconds_ago": int(m.groupdict()['time']),
                        "dbm": int(m.groupdict()['rssi'])
                    }
                })
                continue

            # EoGRE : Pending Classification
            m = p78.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Device Type      : Android
            m = p79.match(line)
            if m:
                device_info_dict = ret_dict.setdefault("device_info", {})
                device_info_dict.update(m.groupdict())
                device_info = True
                continue

            # Device Name      : android-dhcp-10
            m = p79_1.match(line)
            if m:
                device_info_dict.update(m.groupdict())
                continue

            # Protocol Map     : 0x000029  (OUI, DHCP, HTTP)
            m = p79_2.match(line)
            if m:
                device_info_dict.update(m.groupdict())
                continue

            # Device OS        : Linux; U; Android 10; RMX1825 Build/QP1A.190711.020
            m = p79_3.match(line)
            if m:
                device_info_dict.update(m.groupdict())
                continue

            # Type             : 12   12
            m = p79_4.match(line)
            if m:
                if data_index:
                    data_index += 1
                else:
                    data_index = 1

                data_dict = protocol_dict.setdefault(data_index, {})
                data_dict.update(m.groupdict())
                continue

            # Data             : 0c
            # 00000000  00 0c 00 08 72 65 61 6c  6d 65 2d 33               |....realme-3    |
            # 00000030  42 75 69 6c 64 2f 51 50  31 41 2e 31 39 30 37 31  |Build/QP1A.19071|
            # 00000010  44 4a 30                                          |DJ0             |
            m = p79_5.match(line)
            if m:
                data_dict.update(m.groupdict())
                data_dict.update({"data": []})
                continue

            m = p79_6.match(line)
            if m:
                packet = f"{m.groupdict()['byte']} {m.groupdict()['hex']} {m.groupdict()['piped']}"
                data_dict.setdefault("data", []).append(packet)
                continue

            # Max Client Protocol Capability: 802.11ac Wave 2
            m = p80.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Cellular Capability : N/A
            m = p81.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Advanced Scheduling Requests Details:
            if p82.match(line):
                advanced_scheduling_dict = ret_dict.setdefault("advanced_scheduling_requests_details", {})
                continue

            #   Apple Specific Requests(ASR) Capabilities/Statistics:
            m = p82_1.match(line)
            if m:
                specific_request_dict = advanced_scheduling_dict.setdefault(m.groupdict()['request_type'], {})
                continue

            #     Regular ASR support: DISABLED
            m = p82_2.match(line)
            if m:
                specific_request_dict.update(m.groupdict())
                continue

        return ret_dict


# ======================================
# Schema for:
#  * 'show wireless fabric vnid mapping'
# ======================================
class ShowWirelessFabricVnidMappingSchema(MetaParser):
    """Schema for show wireless fabric vnid mapping."""

    schema = {
      "fabric_vnid_mapping" : {
        "name": {
          str : {
            "l2_vnid": int,
            "l3_vnid": int,
            Optional("ip_address"): str,
            "subnet": str,
            "control_plane_name": str
          }
        }
      }
    }
    

# ======================================    
# Parser for:
#  * 'show wireless fabric vnid mapping'
# ======================================
class ShowWirelessFabricVnidMapping(ShowWirelessFabricVnidMappingSchema):
    """Parser for show wireless fabric vnid mapping"""

    cli_command = 'show wireless fabric vnid mapping'
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
          output = output

        # Fabric VNID Mapping:
        #   Name               L2-VNID        L3-VNID        IP Address             Subnet       Control plane name
        # ----------------------------------------------------------------------------------------------------------------------
        #   Data                8190           0                                  0.0.0.0            default-control-plane
        #   Guest               8189           0                                  0.0.0.0            default-control-plane
        #   Voice               8191           0                                  0.0.0.0            default-control-plane
        #   Fabric_A_INF_VN     8188           4097           10.8.132.0          255.255.254.0      default-control-plane
        #   Physical_Security     8192           0                                  0.0.0.0            default-control-plane

        # Fabric VNID Mapping:
        p_fabric_mapping = re.compile(r"^Fabric\s+VNID\s+Mapping:")

        # Data                8190           0                                  0.0.0.0            default-control-plane
        p_fabric_row_4 = re.compile(r"^(?P<name>\S+)\s+(?P<l2_vnid>\d+)\s+(?P<l3_vnid>\d+)"
                                    r"\s+(?P<subnet>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
                                    r"\s+(?P<control_name>\S+)$")

        # Fabric_A_INF_VN     8188           4097           10.8.132.0          255.255.254.0      default-control-plane
        p_fabric_row_5 = re.compile(r"^(?P<name>\S+)\s+(?P<l2_vnid>\d+)\s+(?P<l3_vnid>\d+)\s+"
                                    r"(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
                                    r"(?P<subnet>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
                                    r"(?P<control_name>\S+)")


        fabric_dict = {}

        for line in output.splitlines():
            line = line.strip()
            if p_fabric_mapping.match(line):
                # Fabric VNID Mapping:
                fabric_dict.update({ "fabric_vnid_mapping": {} })
                continue
            elif p_fabric_row_5.match(line):
                match = p_fabric_row_5.match(line)
                group = match.groupdict()
                if not fabric_dict["fabric_vnid_mapping"].get("name"):
                    fabric_dict["fabric_vnid_mapping"].update({ "name": {} })
                fabric_dict["fabric_vnid_mapping"]["name"].update({ group["name"] : {} })
                fabric_dict["fabric_vnid_mapping"]["name"][group["name"]].update({ "l2_vnid": int(group["l2_vnid"]), "l3_vnid": int(group["l3_vnid"]) })
                fabric_dict["fabric_vnid_mapping"]["name"][group["name"]].update({ "ip_address": group["ip"], "subnet": group["subnet"] })
                fabric_dict["fabric_vnid_mapping"]["name"][group["name"]].update({ "control_plane_name": group["control_name"] })
                continue
            elif p_fabric_row_4.match(line):
                match = p_fabric_row_4.match(line)
                group = match.groupdict()
                if not fabric_dict["fabric_vnid_mapping"].get("name"):
                    fabric_dict["fabric_vnid_mapping"].update({ "name": {} })
                fabric_dict["fabric_vnid_mapping"]["name"].update({ group["name"] : {} })
                fabric_dict["fabric_vnid_mapping"]["name"][group["name"]].update({ "l2_vnid": int(group["l2_vnid"]), "l3_vnid": int(group["l3_vnid"]) })
                fabric_dict["fabric_vnid_mapping"]["name"][group["name"]].update({ "subnet": group["subnet"], "control_plane_name": group["control_name"] })
                continue

        return fabric_dict
      

# ==============================================
# Schema for:
#  * 'show wireless stats client delete reasons'
# ==============================================
class ShowWirelessStatsClientDeleteReasonsSchema(MetaParser):
    """Schema for show wireless stats client delete reasons."""

    schema = {
            "total_client_delete_reasons": {
                "controller_deletes": {
                    "no_operation": int,
                    "unknown": int,
                    "session_manager": int,
                    "connection_timeout": int,
                    "datapath_plumb": int,
                    "wpa_key_exchange_timeout": int,
                    "802.11w_max_sa_queries_reached": int,
                    "client_deleted_during_ha_recovery": int,
                    "inter_instance_roam_failure": int,
                    "inter_instance_roam_success": int,
                    "inter_controller_roam_success": int,
                    "due_to_mobility_failure": int,
                    "nas_error": int,
                    "policy_manager_internal_error": int,
                    "80211v_smart_roam_failed": int,
                    "dot11v_association_failed": int,
                    "dot11r_pre_authentication_failure": int,
                    "sae_authentication_failure": int,
                    "dot11_failure": int,
                    "dot11_sae_invalid_message": int,
                    "dot11_denied_data_rates": int,
                    "802.11v_client_rssi_lower_than_the_association_rssi_threshold": int,
                    "invalid_qos_parameter": int,
                    "dot11_ie_validation_failed": int,
                    "dot11_group_cipher_in_ie_validation_failed": int,
                    "dot11_invalid_pairwise_cipher": int,
                    "dot11_invalid_akm": int,
                    "dot11_unsupported_rsn_version": int,
                    "dot11_invalid_rsnie_capabilities": int,
                    "dot11_received_invalid_pmkid_in_the_received_rsn_ie": int,
                    "dot11_received_invalid_pmk_length": int,
                    "dot11_invalid_mdie": int,
                    "dot11_invalid_ft_ie": int,
                    "dot11_aid_allocation_conflicts": int,
                    "avc_client_re_anchored_at_the_foreign_controller": int,
                    "client_eap_id_timeout": int,
                    "client_dot1x_timeout": int,
                    "malformed_eap_key_frame": int,
                    "eap_key_install_bit_is_not_expected": int,
                    "eap_key_error_bit_is_not_expected": int,
                    "eap_key_ack_bit_is_not_expected": int,
                    "invalid_key_type": int,
                    "eap_key_secure_bit_is_not_expected": int,
                    "key_description_version_mismatch": int,
                    "wrong_replay_counter": 8,
                    "eap_key_mic_bit_expected": int,
                    "mic_validation_failed": int,
                    "mac_theft": int,
                    "ip_theft": int,
                    "policy_bind_failure": int,
                    "web_authentication_failure": int,
                    "802.1x_authentication_credential_failure": int,
                    "802.1x_authentication_timeout": int,
                    "802.11_authentication_failure": int,
                    "802.11_association_failure": int,
                    "manually_excluded": int,
                    "db_error": int,
                    "anchor_creation_failure": int,
                    "anchor_invalid_mobility_bssid": int,
                    "anchor_no_memory": int,
                    "call_admission_controller_at_anchor_node": int,
                    "supplicant_restart": int,
                    "port_admin_disabled": int,
                    "reauthentication_failure": int,
                    "client_connection_lost": int,
                    "error_while_ptk_computation": int,
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
                    "wrong_filter_type,_expected_postauth_fqdn_filter": int,
                    "wrong_filter_type,_expected_preauth_fqdn_filter": int,
                    "invalid_group_id_for_fqdn_filter_valid_range_1_16": int,
                    "policy_parameter_mismatch": int,
                    "reauth_failure": int,
                    "wrong_psk": int,
                    "policy_failure": int,
                    "aaa_server_unavailable": int,
                    "aaa_server_not_ready": int,
                    "no_dot1x_method_configuration": int,
                    "association_connection_timeout": int,
                    "mac_auth_connection_timeout": int,
                    "l2_auth_connection_timeout": int,
                    "l3_auth_connection_timeout": int,
                    "mobility_connection_timeout": int,
                    "static_ip_connection_timeout": int,
                    "sm_session_creation_timeout": int,
                    "ip_learn_connection_timeout": int,
                    "nack_ifid_exists": int,
                    "guest_lan_invalid_mbssid": int,
                    "guest_lan_no_memory": int,
                    "guest_lan_ceate_request_failed": int,
                    "eogre_reset": int,
                    "eogre_generic_join_failure": int,
                    "eogre_ha_reconciliation": int,
                    "wired_idle_timeout": int,
                    "ip_update_timeout": int,
                    "sae_commit_received_in_associated_state": int,
                    "nack_ifid_mismatch": int,
                    "eogre_invalid_vlan": int,
                    "eogre_empty_domain": int,
                    "eogre_invalid_domain": int,
                    "eogre_domain_shut": int,
                    "eogre_invalid_gateway": int,
                    "eogre_all_gateways_down": int,
                    "eogre_flex_no_active_gateway": int,
                    "eogre_rule_matching_error": int,
                    "eogre_aaa_override_error": int,
                    "eogre_client_onboarding_error": int,
                    "eogre_mobility_handoff_error": int,
                    "l3_vlan_override_connection_timeout": int,
                    "delete_received_from_ap": int,
                    "qos_failure": int,
                    "wpa_group_key_update_timeout": int,
                    "client_blacklist": int,
                    "dot11_unsupported_client_capabilities": int,
                    "dot11_association_denied_unspecified": int,
                    "dot11_ap_have_insufficient_bandwidth": int,
                    "dot11_invalid_qos_parameter": int,
                    "client_not_allowed_by_assisted_roaming": int,
                    "wired_client_deleted_due_to_wgb_delete": int,
                    "client_abort": int,
                    "mobility_peer_delete": int,
                    "no_ip": int,
                    "bssid_down": 1,
                    "dot11_qos_policy": int,
                    "roam_across_policy_profile_deny": int,
                    "4way_handshake_failure_m1_issue": int,
                    "4way_handshake_failure_m3_issue": int,
                    "exclusion_policy_template_fail": int,
                    "dot11_cipher_suite_rejected": int
                },
                "informational_delete_reason": {
                    "mobility_wlan_down": int,
                    "ap_upgrade": int,
                    "l3_authentication_failure": int,
                    "ap_down_disjoin": 2,
                    "mac_authentication_failure": int,
                    "due_to_ssid_change": int,
                    "due_to_vlan_change": int,
                    "admin_deauthentication": int,
                    "session_timeout": int,
                    "idle_timeout": int,
                    "supplicant_request": int,
                    "mobility_tunnel_down": int,
                    "dot11v_timer_timeout": int,
                    "dot11_max_sta": int,
                    "iapp_disassociation_for_wired_client": int,
                    "wired_wgb_change": int,
                    "wired_vlan_change": int,
                    "wgb_wired_client_joins_as_a_direct_wireless_client": int,
                    "incorrect_credentials": int,
                    "wired_client_cleanup_due_to_wgb_roaming": int,
                    "radio_down": int,
                    "mobility_failure_on_fast_roam": 54,
                    "due_to_ip_zone_change": int
                },
                "client_initiate_delete": {
                    "deauthentication_or_disassociation_request": int,
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
                    "client_beacon_loss": int
                },
                "ap_deletes": {
                    "ap_initiated_delete_when_client_is_sending_disassociation": int,
                    "ap_initiated_delete_for_idle_timeout": int,
                    "ap_initiated_delete_for_client_acl_mismatch": int,
                    "ap_initiated_delete_for_ap_auth_stop": int,
                    "ap_initiated_delete_for_association_expired_at_ap": int,
                    "ap_initiated_delete_for_4_way_handshake_failed": int,
                    "ap_initiated_delete_for_dhcp_timeout": int,
                    "ap_initiated_delete_for_reassociation_timeout": int,
                    "ap_initiated_delete_for_sa_query_timeout": int,
                    "ap_initiated_delete_for_intra_ap_roam": int,
                    "ap_initiated_delete_for_channel_switch_at_ap": int,
                    "ap_initiated_delete_for_bad_aid": int,
                    "ap_initiated_delete_for_request": int,
                    "ap_initiated_delete_for_interface_reset": int,
                    "ap_initiated_delete_for_all_on_slot": int,
                    "ap_initiated_delete_for_reaper_radio": int,
                    "ap_initiated_delete_for_slot_disable": int,
                    "ap_initiated_delete_for_mic_failure": int,
                    "ap_initiated_delete_for_vlan_delete": int,
                    "ap_initiated_delete_for_channel_change": 5,
                    "ap_initiated_delete_for_stop_reassociation": int,
                    "ap_initiated_delete_for_packet_max_retry": int,
                    "ap_initiated_delete_for_transmission_deauth": int,
                    "ap_initiated_delete_for_sensor_station_timeout": int,
                    "ap_initiated_delete_for_age_timeout": int,
                    "ap_initiated_delete_for_transmission_fail_threshold": int,
                    "ap_initiated_delete_for_uplink_receive_timeout": int,
                    "ap_initiated_delete_for_sensor_scan_next_radio": int,
                    "ap_initiated_delete_for_sensor_scan_other_bssid": int,
                    "ap_initiated_delete_for_auth_timeout_and_web_auth_timeout": int,
                    "ap_initiated_delete_for_sending_deauth_pak_to_client": int
                }
            }
        }



# ==============================================
# Parser for:
#  * 'show wireless stats client delete reasons'
# ==============================================
class ShowWirelessStatsClientDeleteReasons(ShowWirelessStatsClientDeleteReasonsSchema):
    """Parser for show wireless stats client delete reasons"""

    cli_command = 'show wireless stats client delete reasons'
    
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
      
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
          output = output

        section_tracker = []
        client_delete_dict = {}
        
        # Total client delete reasons
        p_total_client_delete_reasons = re.compile(r"^Total\s+client\s+delete\s+reasons$")

        # Controller deletes
        p_controller_deletes = re.compile(r"^Controller\s+deletes$")

        # Informational Delete Reason
        p_informational_delete = re.compile(r"^Informational\s+Delete\s+Reason$")

        # Client initiate delete
        p_client_initiate_delete = re.compile(r"^Client\s+initiate\s+delete$")

        # AP Deletes
        p_ap_deletes = re.compile(r"^AP\s+Deletes$")

        # [key] : [value]
        p_colon_split = re.compile(r"^(?P<key>[\S\s]+\S)\s*: +(?P<value>\d+)$")


        for line in output.splitlines():
            line = line.strip()
            if p_total_client_delete_reasons.match(line):
                # Total client delete reasons
                client_delete_dict.update({ "total_client_delete_reasons": {} })
                section_tracker.append("total_client_delete_reasons")
                continue
            elif p_controller_deletes.match(line):
                # Controller deletes
                client_delete_dict["total_client_delete_reasons"].update({ "controller_deletes": {} })
                section_tracker.append("controller_deletes")
                continue
            elif p_informational_delete.match(line):
                # Informational Delete Reason
                section_tracker.pop()
                client_delete_dict["total_client_delete_reasons"].update({ "informational_delete_reason": {} })
                section_tracker.append("informational_delete_reason")
                continue
            elif p_client_initiate_delete.match(line):
                # Client initiate delete
                section_tracker.pop()
                client_delete_dict["total_client_delete_reasons"].update({ "client_initiate_delete": {} })
                section_tracker.append("client_initiate_delete")
                continue
            elif p_ap_deletes.match(line):
                # AP Deletes
                section_tracker.pop()
                client_delete_dict["total_client_delete_reasons"].update({ "ap_deletes": {} })
                section_tracker.append("ap_deletes")
                continue
            elif p_colon_split.match(line):
                # [key] : [value]
                match = p_colon_split.match(line)
                group = match.groupdict()
                group["key"] = group["key"].replace(" ", "_").replace("-", "_").replace("..", "_").replace("/", "_").replace("___", "_").replace("__", "_").lower()
                group["value"] = self.change_data_type(group["value"])
                if len(section_tracker) == 1:
                    client_delete_dict[section_tracker[-1]].update({ group["key"]: group["value"] })
                elif len(section_tracker) == 2:
                    client_delete_dict[section_tracker[-2]][section_tracker[-1]].update({ group["key"]: group["value"] })

        return client_delete_dict

# ======================================
# Schema for:
#  * 'show wireless stats client detail'
# ======================================
class ShowWirelessStatsClientDetailSchema(MetaParser):
    """Schema for show wireless stats client detail."""

    schema = {
    "total_clients": int,
    "protocol_statistics_client_count": {
        "802_11b": int,
        "802_11g": int,
        "802_11a": int,
        "802_11n_2_4ghz": int,
        "802_11n_5_ghz": int,
        "802_11ac": int,
        "802_11ax_5_ghz": int,
        "802_11ax_2_4_ghz": int
    },
    "current_client_state_statistics": {
        "authenticating": int,
        "mobility": int,
        "ip_learn": int,
        "webauth_pending": int,
        "run": int,
        "delete_in_progress": int
    },
    "client_summary": {
        "current_clients": int,
        "excluded_clients": int,
        "disabled_clients": int,
        "foreign_clients": int,
        "anchor_clients": int,
        "local_clients": int,
        "idle_clients": int
    },
    "client_global_statistics": {
        "total_association_requests_received": int,
        "total_association_attempts": int,
        "total_ft_localauth_requests": int,
        "total_association_failures": int,
        "total_association_response_accepts": int,
        "total_association_response_rejects": int,
        "total_association_response_errors": int,
        "total_association_failures_due_to_blacklist": int,
        "total_association_drops_due_to_multicast_mac": int,
        "total_association_drops_due_to_throttling": int,
        "total_association_drops_due_to_unknown_bssid": int,
        "total_association_drops_due_to_parse_failure": int,
        "total_association_drops_due_to_other_reasons": int,
        "total_association_requests_wired_clients": int,
        "total_association_drops_wired_clients": int,
        "total_association_success_wired_clients": int,
        "total_peer_association_requests_wired_clients": int,
        "total_peer_association_drops_wired_clients": int,
        "total_peer_association_success_wired_clients": int,
        "total_association_success_wifi_direct_clients": int,
        "total_association_rejects_wifi_direct_clients": int,
        "total_11r_ft_authentication_requests_received": int,
        "total_11r_ft_authentication_response_success": int,
        "total_11r_ft_authentication_response_failure":int,
        "total_11r_ft_action_requests_received": int,
        "total_11r_ft_action_response_success": int,
        "total_11r_ft_action_response_failure": int,
        "total_11r_pmkr0_name_mismatch": int,
        "total_11r_pmkr1_name_mismatch": int,
        "total_11r_mdid_mismatch": int,
        "total_aid_allocation_failures": int,
        "total_aid_free_failures": int,
        "total_roam_across_policy_profiles": int,
        "roam_attempts": {
            "total_roam_attempts": int,
            "total_cckm_roam_attempts": int,
            "total_11r_roam_attempts": int,
            "total_11r_slow_roam_attempts": int,
            "total_11i_fast_roam_attempts": int,
            "total_11i_slow_roam_attempts": int,
            "total_other_roam_type_attempts": int
        },
        "total_roam_failures_in_dot11": int,
        "total_11r_flex_roam_attempts": int,
        "wpa3_sae": {
            "total_wpa3_sae_attempts": int,
            "total_wpa3_sae_successful_authentications": int,
            "total_wpa3_sae_authentication_failures": int,
            "total_incomplete_protocol_failures": int,
            "total_wpa3_sae_commit_messages_received": int,
            "total_wpa3_sae_commit_messages_rejected": int,
            "total_unsupported_group_rejections": int,
            "total_wpa3_sae_commit_messages_sent": int,
            "total_wpa3_sae_confirm_messages_received": int,
            "total_wpa3_sae_confirm_messages_rejected": int,
            "total_wpa3_sae_message_confirm_field_mismatch": int,
            "total_wpa3_sae_confirm_message_invalid_length": int,
            "total_wpa3_sae_confirm_messages_sent": int,
            "total_wpa3_sae_open_sessions": int,
            "total_sae_message_drops_due_to_throttling": int
        },
        "flexconnect_local_auth_roam": {
            "total_flexconnect_local_auth_roam_attempts": int,
            "total_ap_11i_fast_roam_attempts": int,
            "total_ap_11i_slow_roam_attempts": int
        },
        "total_client_state_starts": int,
        "total_client_state_associated": int,
        "total_client_state_l2auth_success": int,
        "total_client_state_l2auth_failures": int,
        "total_blacklisted_clients_on_dot1xauth_failure": int,
        "total_client_state_mab_attempts": int,
        "total_client_state_mab_failed": int,
        "total_client_state_ip_learn_attempts": int,
        "total_client_state_ip_learn_failed": int,
        "total_client_state_l3_auth_attempts": int,
        "total_client_state_l3_auth_failed": int,
        "total_client_state_session_push_attempts": int,
        "total_client_state_session_push_failed": int,
        "total_client_state_run": int,
        "total_client_idle_state_attempts": int,
        "total_client_deleted": int
    },
    "total_clients_recovered_from_idle_state": {
        "total_clients_intra_wncd_idle_to_run": int,
        "total_clients_inter_wncd_roam_in_idle_state": int,
        "total_clients_l2_roam_in_idle_state": int,
        "total_clients_l3_roam_in_idle_state": int,
        "total_add_mobiles_sent": int,
        "total_delete_mobiles_sent": int,
        "total_client_deferred_delete_mobiles": int,
        "total_client_deferred_delete_mobiles_sent": int,
        "total_client_deferred_delete_mobile_timeouts": int,
        "total_udn_payloads_sent": int,
        "total_key_exchange_attempts": int,
        "total_broadcast_key_exchange_attempts": int,
        "total_broadcast_key_exchange_failures": int,
        "total_eapol_key_sent": int,
        "total_eapol_key_received": int,
        "total_m1_sent": int,
        "total_m3_sent": int,
        "total_m5_sent": int,
        "total_m2_received": int,
        "total_m4_received": int,
        "total_m6_received": int,
        "total_m1_resent": int,
        "total_m3_resent": int,
        "total_m5_resent": int,
        "total_data_path_client_create": int,
        "total_data_path_client_create_success": int,
        "total_data_path_client_create_failed": int,
        "total_data_path_deplumb_client_create": int,
        "total_data_path_deplumb_client_create_success": int,
        "total_data_path_deplumb_client_create_fail": int,
        "total_data_path_client_update": int,
        "total_data_path_client_update_success": int,
        "total_data_path_client_update_failed": 0,
        "total_data_path_client_delete": int,
        "total_data_path_client_delete_success": int,
        "total_data_path_client_delete_failed": int,
        "total_data_path_client_nack": int,
        "total_data_path_client_delete_nack": int,
        "total_data_path_client_unknown_nack": int,
        "total_dms_requests_received_in_action_frame": int,
        "total_dms_responses_sent_in_action_frame": int,
        "total_dms_requests_received_in_re_assoc_request": int,
        "total_l3_vlan_override_vlan_change_received": int,
        "total_l3_vlan_override_disassociations_sent": int,
        "total_l3_vlan_override_re_associations_received": int,
        "total_l3_vlan_override_successful_vlan_change": int,
        "total_ppsk_key_generation_cache_hit": int,
        "total_ppsk_key_generation_cache_miss": int
    },
    "client_state_statistics": {
        "average_time_in_each_state_ms": {
            "associated_state": int,
            "l2_state": int,
            "mobility_state": int,
            "ip_learn_state": int,
            "l3_auth_state": int
        },
        "average_run_state_latency_ms": int,
        "average_run_state_latency_without_user_delay_ms": int,
        "latency_distribution_ms": {
            "1_100": int,
            "100_200": int,
            "200_300": int,
            "300_600": int,
            "600_1000": int,
            "1000+": int
        }
    },
    "webauth_http_statistics": {
        "intercepted_http_requests": int,
        "io_read_events": int,
        "received_http_messages": int,
        "io_write_events": int,
        "sent_http_replies": int,
        "io_aaa_messages": int,
        "ssl_ok": int,
        "ssl_read_would_block": int,
        "ssl_write_would_block": int,
        "socket_opens": int,
        "socket_closes": int
    },
    "time_spent_in_each_httpd_state_msec": {
        "io_reading_state": {
            "total": int,
            "max": int,
            "min": int,
            "samples": int
        },
        "io_writing_state": {
            "total": int,
            "max": int,
            "min": int,
            "samples": int
        },
        "io_aaa_state": {
            "total": int,
            "max": int,
            "min": int,
            "samples": int
        },
        "method_after_reading": {
            "total": int,
            "max": int,
            "min": int,
            "samples": int
        },
        "method_after_writing": {
            "total": int,
            "max": int,
            "min": int,
            "samples": int
        },
        "method_after_aaa": {
            "total": int,
            "max": int,
            "min": int,
            "samples": int
        }
    },
    "webauth_http_status_counts": {
        "http_200_ok": int,
        "http_201_created": int,
        "http_202_accepted": int,
        "http_203_provisional_info": int,
        "http_204_no_content": int,
        "http_300_multiple_choices": int,
        "http_301_moved_permanently": int,
        "http_302_moved_temporarily": int,
        "http_303_method": int,
        "http_304_not_modified": int,
        "http_400_bad_request": int,
        "http_401_unauthorized": int,
        "http_402_payment_required": int,
        "http_403_forbidden": int,
        "http_404_not_found": int,
        "http_405_method_not_allowed": int,
        "http_406_none_acceptable": int,
        "http_407_proxy_auth_required": int,
        "http_408_request_timeout": int,
        "http_409_conflict": int,
        "http_410_gone": int,
        "http_500_internal_server_error": int,
        "http_501_not_implemeneted": int,
        "http_502_bad_gateway": int,
        "http_503_service_unavailable": int,
        "http_504_gateway_timeout": int
    },
    "webauth_backpressure_queue_counters": {
        "pending_ssl_handshakes": int,
        "pending_https_new_requests": int,
        "pending_aaa_replies": int
    },
    "dot1x_global_statistics": {
        "rx_start": int,
        "rx_logoff": int,
        "rx_resp": int,
        "rx_resp_id": int,
        "rx_req": int,
        "rx_invalid": int,
        "rx_len_error": int,
        "rx_total": int,
        "tx_start": int,
        "tx_logoff": int,
        "tx_resp": int,
        "tx_req": int,
        "re_tx_req": int,
        "re_tx_req_fail": int,
        "tx_req_id": int,
        "re_tx_req_id": int
    },
    "total_client_delete_reasons": {
        "controller_deletes": {
            "no_operation": int,
            "unknown": int,
            "session_manager": int,
            "connection_timeout": int,
            "datapath_plumb": int,
            "wpa_key_exchange_timeout": int,
            "802_11w_max_sa_queries_reached": int,
            "client_deleted_during_ha_recovery": int,
            "inter_instance_roam_failure": int,
            "inter_instance_roam_success": int,
            "inter_controller_roam_success": int,
            "due_to_mobility_failure": int,
            "nas_error": int,
            "policy_manager_internal_error": int,
            "80211v_smart_roam_failed": int,
            "dot11v_association_failed": int,
            "dot11r_pre_authentication_failure": int,
            "sae_authentication_failure": int,
            "dot11_failure": int,
            "dot11_sae_invalid_message": int,
            "dot11_denied_data_rates": int,
            "802_11v_client_rssi_lower_than_the_association_rssi_threshold": int,
            "invalid_qos_parameter": int,
            "dot11_ie_validation_failed": int,
            "dot11_group_cipher_in_ie_validation_failed": int,
            "dot11_invalid_pairwise_cipher": int,
            "dot11_invalid_akm": int,
            "dot11_unsupported_rsn_version": int,
            "dot11_invalid_rsnie_capabilities": int,
            "dot11_received_invalid_pmkid_in_the_received_rsn_ie": int,
            "dot11_received_invalid_pmk_length": int,
            "dot11_invalid_mdie": int,
            "dot11_invalid_ft_ie": int,
            "dot11_aid_allocation_conflicts": int,
            "avc_client_re_anchored_at_the_foreign_controller": int,
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
            "mac_theft": int,
            "ip_theft": int,
            "policy_bind_failure": int,
            "web_authentication_failure": int,
            "802_1x_authentication_credential_failure": int,
            "802_1x_authentication_timeout": int,
            "802_11_authentication_failure": int,
            "802_11_association_failure": int,
            "manually_excluded": int,
            "db_error": int,
            "anchor_creation_failure": int,
            "anchor_invalid_mobility_bssid": int,
            "anchor_no_memory": int,
            "call_admission_controller_at_anchor_node": int,
            "supplicant_restart": int,
            "port_admin_disabled": int,
            "reauthentication_failure": int,
            "client_connection_lost": int,
            "error_while_ptk_computation": int,
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
            "wrong_filter_type,_expected_postauth_fqdn_filter": int,
            "wrong_filter_type,_expected_preauth_fqdn_filter": int,
            "invalid_group_id_for_fqdn_filter_valid_range_1_16": int,
            "policy_parameter_mismatch": int,
            "reauth_failure": int,
            "wrong_psk": int,
            "policy_failure": int,
            "aaa_server_unavailable": int,
            "aaa_server_not_ready": int,
            "no_dot1x_method_configuration": int,
            "association_connection_timeout": int,
            "mac_auth_connection_timeout": int,
            "l2_auth_connection_timeout": int,
            "l3_auth_connection_timeout": int,
            "mobility_connection_timeout": int,
            "static_ip_connection_timeout": int,
            "sm_session_creation_timeout": int,
            "ip_learn_connection_timeout": int,
            "nack_ifid_exists": int,
            "guest_lan_invalid_mbssid": int,
            "guest_lan_no_memory": int,
            "guest_lan_ceate_request_failed": int,
            "eogre_reset": int,
            "eogre_generic_join_failure": int,
            "eogre_ha_reconciliation": int,
            "wired_idle_timeout": int,
            "ip_update_timeout": int,
            "sae_commit_received_in_associated_state":int,
            "nack_ifid_mismatch":int,
            "eogre_invalid_vlan":int,
            "eogre_empty_domain":int,
            "eogre_invalid_domain":int,
            "eogre_domain_shut":int,
            "eogre_invalid_gateway":int,
            "eogre_all_gateways_down": int,
            "eogre_flex_no_active_gateway": int,
            "eogre_rule_matching_error": int,
            "eogre_aaa_override_error": int,
            "eogre_client_onboarding_error": int,
            "eogre_mobility_handoff_error": int,
            "l3_vlan_override_connection_timeout": int,
            "delete_received_from_ap": int,
            "qos_failure": int,
            "wpa_group_key_update_timeout": int,
            "client_blacklist": int,
            "dot11_unsupported_client_capabilities": int,
            "dot11_association_denied_unspecified": int,
            "dot11_ap_have_insufficient_bandwidth": int,
            "dot11_invalid_qos_parameter": int,
            "client_not_allowed_by_assisted_roaming": int,
            "wired_client_deleted_due_to_wgb_delete": int,
            "client_abort": int,
            "mobility_peer_delete": int,
            "no_ip": int,
            "bssid_down": int,
            "dot11_qos_policy": int,
            "roam_across_policy_profile_deny": int,
            "4way_handshake_failure_m1_issue": int,
            "4way_handshake_failure_m3_issue": int,
            "exclusion_policy_template_fail": int,
            "dot11_cipher_suite_rejected": int
        },
        "informational_delete_reason": {
            "mobility_wlan_down": int,
            "ap_upgrade": int,
            "l3_authentication_failure": int,
            "ap_down_disjoin": int,
            "mac_authentication_failure": int,
            "due_to_ssid_change": int,
            "due_to_vlan_change": int,
            "admin_deauthentication": int,
            "session_timeout": int,
            "idle_timeout": int,
            "supplicant_request": int,
            "mobility_tunnel_down": int,
            "dot11v_timer_timeout": int,
            "dot11_max_sta": int,
            "iapp_disassociation_for_wired_client": int,
            "wired_wgb_change": int,
            "wired_vlan_change": int,
            "wgb_wired_client_joins_as_a_direct_wireless_client": int,
            "incorrect_credentials": int,
            "wired_client_cleanup_due_to_wgb_roaming": int,
            "radio_down": int,
            "mobility_failure_on_fast_roam": int,
            "due_to_ip_zone_change": int
        },
        "client_initiate_delete": {
            "deauthentication_or_disassociation_request": int,
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
            "client_beacon_loss": int
        },
        "ap_deletes": {
            "ap_initiated_delete_when_client_is_sending_disassociation": int,
            "ap_initiated_delete_for_idle_timeout": int,
            "ap_initiated_delete_for_client_acl_mismatch": int,
            "ap_initiated_delete_for_ap_auth_stop": int,
            "ap_initiated_delete_for_association_expired_at_ap": int,
            "ap_initiated_delete_for_4_way_handshake_failed": int,
            "ap_initiated_delete_for_dhcp_timeout": int,
            "ap_initiated_delete_for_reassociation_timeout": int,
            "ap_initiated_delete_for_sa_query_timeout": int,
            "ap_initiated_delete_for_intra_ap_roam": int,
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
            "ap_initiated_delete_for_auth_timeout_and_web_auth_timeout": int,
            "ap_initiated_delete_for_sending_deauth_pak_to_client": int
        }
    }
}


# ======================================
# Parser for:
#  * 'show wireless stats client detail'
# ======================================
class ShowWirelessStatsClientDetail(ShowWirelessStatsClientDetailSchema):
    """Parser for show wireless stats client detail"""

    cli_command = 'show wireless stats client detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
          output = output
            
        # Total Number of Clients : 16
        p_total_client = re.compile(r"^Total\s+Number\s+of\s+Clients\s+:\s+(?P<value>\d+)$")

        # Protocol Statistics
        p_protocol_stats_section = re.compile(r"^Protocol\s+Statistics$")

        # Current client state statistics:
        p_current_client_stats_section = re.compile(r"^Current\s+client\s+state\s+statistics:$")

        # Client Summary
        p_client_summary_section = re.compile(r"^Client\s+Summary$")

        # client global statistics:
        p_client_global_s1 = re.compile(r"^client\s+global\s+statistics:$")

        # Total roam attempts                              : 4200
        p_client_global_s2 = re.compile(r"^Total\s+roam\s+attempts\s+:\s+(?P<total_roam>\d+)$")

        # Total roam failures in dot11                     : 5
        p_client_global_s3 = re.compile(r"Total\s+roam\s+failures\s+in\s+dot11\s+:\s+(?P<dot11>\d+)$")

        # Total WPA3 SAE attempts                          : 0
        p_client_global_s4 = re.compile(r"Total\s+WPA3\s+SAE\s+attempts\s+:\s+(?P<wpa3_sae>\d+)$")

        # Total Flexconnect local-auth roam attempts       : 0
        p_client_global_s5 = re.compile(r"^Total\s+Flexconnect\s+local-auth\s+roam\s+attempts\s+:\s+(?P<flex_roam>\d+)$")

        # Total client state starts                        : 41695
        p_client_global_s6 = re.compile(r"^Total\s+client\s+state\s+starts\s+:\s+(?P<start_state>\d+)$")

        # client state statistics:
        p_client_state_stats = re.compile(r"^client\s+state\s+statistics:$")

        # Total clients recovered from idle state:
        p_total_clients_recovered_idle = re.compile(r"^Total\s+clients\s+recovered\s+from\s+idle\s+state:$")

        # Average Time in Each State (ms)
        p_average_time_state = re.compile(r"Average\s+Time\s+in\s+Each\s+State\s+\(ms\)")

        # Average Run State Latency (ms) : 5
        p_average_run_latency = re.compile(r"^Average\s+Run\s+State\s+Latency\s+\(ms\)\s+:\s+(?P<run_latency>\d+)$")

        # Average Run State Latency without user delay (ms) : 1
        p_average_run_latency_user = re.compile(r"^Average\s+Run\s+State\s+Latency\s+without\s+user\s+delay\s+\(ms\)\s+:\s+(?P<run_latency_user>\d+)$")

        # Latency Distribution (ms)
        p_latency_distribution = re.compile(r"^Latency\s+Distribution\s+\(ms\)$")

        # Webauth HTTP Statistics
        p_webhttp_stats = re.compile(r"^Webauth\s+HTTP\s+Statistics$")

        # Time spent in each httpd states (in msecs)
        p_time_spent_http_states_section = re.compile(r"Time\s+spent\s+in\s+each\s+httpd\s+states\s+\(in\s+msecs\)")

        # IO Reading state          4654682      58788          0     294534
        p_time_spent_io_read = re.compile(r"IO\s+Reading\s+state\s+(?P<total>\d+)\s+(?P<max>\d+)\s+(?P<min>\d+)\s+(?P<samples>\d+)")

        # IO Writing state             6445          1          0     293834
        p_time_spent_io_write = re.compile(r"IO\s+Writing\s+state\s+(?P<total>\d+)\s+(?P<max>\d+)\s+(?P<min>\d+)\s+(?P<samples>\d+)")

        # IO AAA state                    0          0          0          0
        p_time_spent_io_aaa = re.compile(r"IO\s+AAA\s+state\s+(?P<total>\d+)\s+(?P<max>\d+)\s+(?P<min>\d+)\s+(?P<samples>\d+)")

        # Method after reading         9865          1          0     294534
        p_time_spent_method_read = re.compile(r"Method\s+after\s+reading\s+(?P<total>\d+)\s+(?P<max>\d+)\s+(?P<min>\d+)\s+(?P<samples>\d+)")

        # Method after writing           31          1          0     293834
        p_time_spent_method_writing = re.compile(r"Method\s+after\s+writing\s+(?P<total>\d+)\s+(?P<max>\d+)\s+(?P<min>\d+)\s+(?P<samples>\d+)")

        # Method after AAA                0          0          0          0
        p_time_spent_method_aaa = re.compile(r"Method\s+after\s+AAA\s+(?P<total>\d+)\s+(?P<max>\d+)\s+(?P<min>\d+)\s+(?P<samples>\d+)")

        # Webauth HTTP status counts
        p_webauth_http_status_counts = re.compile(r"^Webauth\s+HTTP\s+status\s+counts$")

        # Webauth backpressure queue counters
        p_webauth_backpressure = re.compile(r"Webauth\s+backpressure\s+queue\s+counters")

        # Dot1x Global Statistics
        p_dot1x_global_section = re.compile(r"Dot1x\s+Global\s+Statistics")

        # RxStart = 6657 RxLogoff = 18  RxResp = 104310 RxRespID = 15453
        p_dot1x_rxstart = re.compile(r"^RxStart\s+=\s+(?P<start>\d+)\s+RxLogoff\s+=\s+(?P<logoff>\d+)\s+RxResp\s+=\s+(?P<resp>\d+)\s+RxRespID\s+=\s+(?P<respid>\d+)$")

        # RxReq = 0 RxInvalid = 0  RxLenErr = 0
        p_dot1x_req = re.compile(r"^RxReq\s+=\s+(?P<req>\d+)\s+RxInvalid\s+=\s+(?P<invalid>\d+)\s+RxLenErr\s+=\s+(?P<lenerror>\d+)$")

        # RxTotal = 126939
        p_dot1x_rx_total = re.compile(r"^RxTotal\s+=\s+(?P<total>\d+)$")

        # TxStart = 0 TxLogoff = 0  TxResp = 0
        p_dot1x_txstart = re.compile(r"^TxStart\s+=\s+(?P<start>\d+)\s+TxLogoff\s+=\s+(?P<logoff>\d+)\s+TxResp\s+=\s+(?P<resp>\d+)$")

        # TxReq = 117345 ReTxReq = 3909  ReTxReqFail = 11528
        p_dot1_tx_req = re.compile(r"^TxReq\s+=\s+(?P<req>\d+)\s+ReTxReq\s+=\s+(?P<rereq>\d+)\s+ReTxReqFail\s+=\s+(?P<txfail>\d+)$")

        # TxReqID = 67670 ReTxReqID = 29908  ReTxReqIDFail = 1310
        p_dot1_tx_reqid = re.compile(r"TxReqID\s+=\s+(?P<reqid>\d+)\s+ReTxReqID\s+=\s+(?P<rereqid>\d+)\s+ReTxReqIDFail\s+=\s+(?P<reqidfail>\d+)$")

        # TxTotal = 185057
        p_dot1_tx_total = re.compile(r"TxTotal\s+=\s+(?P<tx_total>\d+)$")
        
        # Total client delete reasons
        p_total_client_delete_reasons = re.compile(r"^Total\s+client\s+delete\s+reasons$")

        # Controller deletes
        p_controller_deletes = re.compile(r"^Controller\s+deletes$")

        # Informational Delete Reason
        p_informational_delete = re.compile(r"^Informational\s+Delete\s+Reason$")

        # Client initiate delete
        p_client_initiate_delete = re.compile(r"^Client\s+initiate\s+delete$")

        # AP Deletes
        p_ap_deletes = re.compile(r"^AP\s+Deletes$")

        # [key] : [value]
        p_colon_split = re.compile(r"^(?P<key>[\S\s]+\S)\s*: +(?P<value>\d+)$")
        
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
        
        
        section_tracker = []
        client_detail_dict = {}

        for line in output.splitlines():
          line = line.strip()
          if p_total_client.match(line):
              # Total Number of Clients : 16
              m_total_client = p_total_client.match(line)
              client_detail_dict.update({ "total_clients": int(m_total_client.group("value")) })
              continue
          elif p_protocol_stats_section.match(line):
              # Protocol Statistics
              client_detail_dict.update({ "protocol_statistics_client_count": {} })
              section_tracker.append("protocol_statistics_client_count")
              continue
          elif p_current_client_stats_section.match(line):
              # Current client state statistics:
              section_tracker.pop()
              client_detail_dict.update({ "current_client_state_statistics": {} })
              section_tracker.append("current_client_state_statistics")
              continue
          elif p_client_summary_section.match(line):
              # Client Summary
              section_tracker.pop()
              client_detail_dict.update({ "client_summary": {} })
              section_tracker.append("client_summary")
              continue
          elif p_client_global_s1.match(line):
              # client global statistics:
              section_tracker.pop()
              client_detail_dict.update({ "client_global_statistics": {} })
              section_tracker.append("client_global_statistics")
              continue
          elif p_client_global_s2.match(line):
              # Total roam attempts                              : 4200
              m_client_global_s2 = p_client_global_s2.match(line)
              client_detail_dict["client_global_statistics"].update({ "roam_attempts": {} })
              client_detail_dict["client_global_statistics"]["roam_attempts"].update( {"total_roam_attempts": int(m_client_global_s2.group("total_roam")) })
              section_tracker.append("roam_attempts")
              continue
          elif p_client_global_s3.match(line):
              # Total roam failures in dot11                     : 5
              section_tracker.pop()
              match = p_client_global_s3.match(line)
              client_detail_dict["client_global_statistics"].update({ "total_roam_failures_in_dot11": int(match.group("dot11")) })
              continue
          elif p_client_global_s4.match(line):
              # Total WPA3 SAE attempts                          : 0
              m_client_global_s4 = p_client_global_s4.match(line)
              client_detail_dict["client_global_statistics"].update({ "wpa3_sae": {} })
              client_detail_dict["client_global_statistics"]["wpa3_sae"].update({ "total_wpa3_sae_attempts": int(m_client_global_s4.group("wpa3_sae")) })
              section_tracker.append("wpa3_sae")
              continue
          elif p_client_global_s5.match(line):
              # Total Flexconnect local-auth roam attempts       : 0
              section_tracker.pop()
              m_client_global_s5 = p_client_global_s5.match(line)
              client_detail_dict["client_global_statistics"].update({ "flexconnect_local_auth_roam": {} })
              client_detail_dict["client_global_statistics"]["flexconnect_local_auth_roam"].update({ "total_flexconnect_local_auth_roam_attempts": int(m_client_global_s5.group("flex_roam")) })
              section_tracker.append("flexconnect_local_auth_roam")
              continue
          elif p_client_global_s6.match(line):
              # Total client state starts                        : 41695
              section_tracker.pop()
              match = p_client_global_s6.match(line)
              client_detail_dict["client_global_statistics"].update({ "total_client_state_starts": int(match.group("start_state")) })
              continue
          elif p_total_clients_recovered_idle.match(line):
              # Total clients recovered from idle state:
              section_tracker.pop()
              client_detail_dict.update({ "total_clients_recovered_from_idle_state": {}})
              section_tracker.append("total_clients_recovered_from_idle_state")
              continue
          elif p_client_state_stats.match(line):
              # client state statistics:
              section_tracker.pop()
              client_detail_dict.update({ "client_state_statistics": {} })
              section_tracker.append("client_state_statistics")
              continue
          elif p_average_time_state.match(line):
              # Average Time in Each State (ms)
              client_detail_dict["client_state_statistics"].update({ "average_time_in_each_state_ms": {} })
              section_tracker.append("average_time_in_each_state_ms")
              continue
          elif p_average_run_latency.match(line):
              # Average Run State Latency (ms) : 5
              m_average_run_latency = p_average_run_latency.match(line)
              client_detail_dict["client_state_statistics"].update({"average_run_state_latency_ms": int(m_average_run_latency.group("run_latency")) })
              continue
          elif p_average_run_latency_user.match(line):
              # Average Run State Latency without user delay (ms) : 1
              m_average_run_latency_user = p_average_run_latency_user.match(line)
              client_detail_dict["client_state_statistics"].update({"average_run_state_latency_without_user_delay_ms": int(m_average_run_latency_user.group("run_latency_user")) })
              continue
          elif p_latency_distribution.match(line):
              # Latency Distribution (ms)
              section_tracker.pop()
              client_detail_dict["client_state_statistics"].update({ "latency_distribution_ms": {} })
              section_tracker.append("latency_distribution_ms")
          elif p_webhttp_stats.match(line):
              # Webauth HTTP Statistics
              section_tracker.pop()
              section_tracker.pop()
              client_detail_dict.update({ "webauth_http_statistics": {} })
              section_tracker.append("webauth_http_statistics")
              continue
          elif p_time_spent_http_states_section.match(line):
              # Time spent in each httpd states (in msecs)
              client_detail_dict.update({ "time_spent_in_each_httpd_state_msec": {} })
              continue
          elif p_time_spent_io_read.match(line):
              # IO Reading state          4654682      58788          0     294534
              m_time_spent_io_read = p_time_spent_io_read.match(line)
              group_m_time_spent_io_read = m_time_spent_io_read.groupdict()
              client_detail_dict["time_spent_in_each_httpd_state_msec"].update({ "io_reading_state": {} })
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["io_reading_state"].update({"total": int(group_m_time_spent_io_read["total"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["io_reading_state"].update({"max": int(group_m_time_spent_io_read["max"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["io_reading_state"].update({"min": int(group_m_time_spent_io_read["min"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["io_reading_state"].update({"samples": int(group_m_time_spent_io_read["samples"])})
              continue
          elif p_time_spent_io_write.match(line):
              # IO Writing state          4654682      58788          0     294534
              m_time_spent_io_write = p_time_spent_io_write.match(line)
              group_m_time_spent_io_write = m_time_spent_io_write.groupdict()
              client_detail_dict["time_spent_in_each_httpd_state_msec"].update({ "io_writing_state": {} })
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["io_writing_state"].update({"total": int(group_m_time_spent_io_write["total"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["io_writing_state"].update({"max": int(group_m_time_spent_io_write["max"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["io_writing_state"].update({"min": int(group_m_time_spent_io_write["min"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["io_writing_state"].update({"samples": int(group_m_time_spent_io_write["samples"])})
              continue
          elif p_time_spent_io_aaa.match(line):
              # IO AAA state                    0          0          0          0
              m_time_spent_io_aaa = p_time_spent_io_aaa.match(line)
              group_m_time_spent_io_aaa = m_time_spent_io_aaa.groupdict()
              client_detail_dict["time_spent_in_each_httpd_state_msec"].update({ "io_aaa_state": {} })
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["io_aaa_state"].update({"total": int(group_m_time_spent_io_aaa["total"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["io_aaa_state"].update({"max": int(group_m_time_spent_io_aaa["max"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["io_aaa_state"].update({"min": int(group_m_time_spent_io_aaa["min"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["io_aaa_state"].update({"samples": int(group_m_time_spent_io_aaa["samples"])})
              continue
          elif p_time_spent_method_read.match(line):
              # Method after reading         9865          1          0     294534
              m_time_spent_method_read = p_time_spent_method_read.match(line)
              group_m_time_spent_method_read = m_time_spent_method_read.groupdict()
              client_detail_dict["time_spent_in_each_httpd_state_msec"].update({ "method_after_reading": {} })
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["method_after_reading"].update({"total": int(group_m_time_spent_method_read["total"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["method_after_reading"].update({"max": int(group_m_time_spent_method_read["max"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["method_after_reading"].update({"min": int(group_m_time_spent_method_read["min"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["method_after_reading"].update({"samples": int(group_m_time_spent_method_read["samples"])})
              continue
          elif p_time_spent_method_writing.match(line):
              # Method after writing           31          1          0     293834
              m_time_spent_method_writing = p_time_spent_method_writing.match(line)
              group_m_time_spent_method_writing = m_time_spent_method_writing.groupdict()
              client_detail_dict["time_spent_in_each_httpd_state_msec"].update({ "method_after_writing": {} })
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["method_after_writing"].update({"total": int(group_m_time_spent_method_writing["total"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["method_after_writing"].update({"max": int(group_m_time_spent_method_writing["max"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["method_after_writing"].update({"min": int(group_m_time_spent_method_writing["min"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["method_after_writing"].update({"samples": int(group_m_time_spent_method_writing["samples"])})
              continue
          elif p_time_spent_method_aaa.match(line):
              # Method after AAA                0          0          0          0
              m_time_spent_method_aaa = p_time_spent_method_aaa.match(line)
              group_m_time_spent_method_aaa = m_time_spent_method_aaa.groupdict()
              client_detail_dict["time_spent_in_each_httpd_state_msec"].update({ "method_after_aaa": {} })
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["method_after_aaa"].update({"total": int(group_m_time_spent_method_aaa["total"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["method_after_aaa"].update({"max": int(group_m_time_spent_method_aaa["max"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["method_after_aaa"].update({"min": int(group_m_time_spent_method_aaa["min"])})
              client_detail_dict["time_spent_in_each_httpd_state_msec"]["method_after_aaa"].update({"samples": int(group_m_time_spent_method_aaa["samples"])})
              continue
          elif p_webauth_http_status_counts.match(line):
              # Webauth HTTP status counts
              section_tracker.pop()
              client_detail_dict.update({ "webauth_http_status_counts": {} })
              section_tracker.append("webauth_http_status_counts")
              continue
          elif p_webauth_backpressure.match(line):
              # Webauth backpressure queue counters
              section_tracker.pop()
              client_detail_dict.update({ "webauth_backpressure_queue_counters": {} })
              section_tracker.append("webauth_backpressure_queue_counters")
              continue
          elif p_dot1x_global_section.match(line):
              # Dot1x Global Statistics
              client_detail_dict.update({ "dot1x_global_statistics": {} })
              continue
          elif p_dot1x_rxstart.match(line):
              # RxStart = 6657 RxLogoff = 18  RxResp = 104310 RxRespID = 15453
              m_dot1x_rxstart = p_dot1x_rxstart.match(line)
              group_m_dot1x_rxstart = m_dot1x_rxstart.groupdict()
              client_detail_dict["dot1x_global_statistics"].update({ "rx_start": int(group_m_dot1x_rxstart["start"]) })
              client_detail_dict["dot1x_global_statistics"].update({ "rx_logoff": int(group_m_dot1x_rxstart["logoff"]) })
              client_detail_dict["dot1x_global_statistics"].update({ "rx_resp": int(group_m_dot1x_rxstart["resp"]) })
              client_detail_dict["dot1x_global_statistics"].update({ "rx_resp_id": int(group_m_dot1x_rxstart["respid"]) })
              continue
          elif p_dot1x_req.match(line):
              # RxReq = 0 RxInvalid = 0  RxLenErr = 0
              m_dot1x_req = p_dot1x_req.match(line)
              group_m_dot1x_req = m_dot1x_req.groupdict()
              client_detail_dict["dot1x_global_statistics"].update({ "rx_req": int(group_m_dot1x_req["req"]) })
              client_detail_dict["dot1x_global_statistics"].update({ "rx_invalid": int(group_m_dot1x_req["invalid"]) })
              client_detail_dict["dot1x_global_statistics"].update({ "rx_len_error": int(group_m_dot1x_req["lenerror"]) })
              continue
          elif p_dot1x_rx_total.match(line):
              # RxTotal = 126939
              m_dot1x_rx_total = p_dot1x_rx_total.match(line)
              client_detail_dict["dot1x_global_statistics"].update({ "rx_total": int(m_dot1x_rx_total.group("total")) })
              continue
          elif p_dot1x_txstart.match(line):
              # TxStart = 0 TxLogoff = 0  TxResp = 0
              m_dot1x_txstart = p_dot1x_txstart.match(line)
              group_m_dot1x_txstart = m_dot1x_txstart.groupdict()
              client_detail_dict["dot1x_global_statistics"].update({ "tx_start": int(group_m_dot1x_txstart["start"]) })
              client_detail_dict["dot1x_global_statistics"].update({ "tx_logoff": int(group_m_dot1x_txstart["logoff"]) })
              client_detail_dict["dot1x_global_statistics"].update({ "tx_resp": int(group_m_dot1x_txstart["resp"]) })
              continue
          elif p_dot1_tx_req.match(line):
              # TxReq = 117345 ReTxReq = 3909  ReTxReqFail = 11528
              m_dot1_tx_req = p_dot1_tx_req.match(line)
              group_m_dot1_tx_req = m_dot1_tx_req.groupdict()
              client_detail_dict["dot1x_global_statistics"].update({ "tx_req": int(group_m_dot1_tx_req["req"]) })
              client_detail_dict["dot1x_global_statistics"].update({ "re_tx_req": int(group_m_dot1_tx_req["rereq"]) })
              client_detail_dict["dot1x_global_statistics"].update({ "re_tx_req_fail": int(group_m_dot1_tx_req["txfail"]) })
              continue
          elif p_dot1_tx_reqid.match(line):
              # TxReqID = 67670 ReTxReqID = 29908  ReTxReqIDFail = 1310
              m_dot1_tx_reqid = p_dot1_tx_reqid.match(line)
              group_m_dot1_tx_reqid = m_dot1_tx_reqid.groupdict()
              client_detail_dict["dot1x_global_statistics"].update({ "tx_req_id": int(group_m_dot1_tx_reqid["reqid"]) })
              client_detail_dict["dot1x_global_statistics"].update({ "re_tx_req_id": int(group_m_dot1_tx_reqid["rereqid"]) })
              client_detail_dict["dot1x_global_statistics"].update({ "re_tx_req_fail": int(group_m_dot1_tx_reqid["reqidfail"]) })
              continue
          elif p_total_client_delete_reasons.match(line):
              # Total client delete reasons
              section_tracker.pop()
              client_detail_dict.update({ "total_client_delete_reasons": {} })
              section_tracker.append("total_client_delete_reasons")
              continue
          elif p_controller_deletes.match(line):
              # Controller deletes
              client_detail_dict["total_client_delete_reasons"].update({ "controller_deletes": {} })
              section_tracker.append("controller_deletes")
              continue
          elif p_informational_delete.match(line):
              # Informational Delete Reason
              section_tracker.pop()
              client_detail_dict["total_client_delete_reasons"].update({ "informational_delete_reason": {} })
              section_tracker.append("informational_delete_reason")
              continue
          elif p_client_initiate_delete.match(line):
              # Client initiate delete
              section_tracker.pop()
              client_detail_dict["total_client_delete_reasons"].update({ "client_initiate_delete": {} })
              section_tracker.append("client_initiate_delete")
              continue
          elif p_ap_deletes.match(line):
              # AP Deletes
              section_tracker.pop()
              client_detail_dict["total_client_delete_reasons"].update({ "ap_deletes": {} })
              section_tracker.append("ap_deletes")
              continue
          elif p_colon_split.match(line):
              # [key] : [value]
              match = p_colon_split.match(line)
              group = match.groupdict()
              group["key"] = group["key"].replace(" ", "_").replace(".", "_").replace("-", "_").replace("___", "_").replace("__", "_").replace("/", "_").lower()
              group["value"] = int(group["value"])
              if len(section_tracker) == 1:
                  client_detail_dict[section_tracker[-1]].update({ group["key"]: group["value"] })
              elif len(section_tracker) == 2:
                  client_detail_dict[section_tracker[-2]][section_tracker[-1]].update({ group["key"]: group["value"] })


        return client_detail_dict

      
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


# ========================================
# Schema for:
#  * 'show wireless management trustpoint'
# ========================================
class ShowWirelessManagementTrustPointSchema(MetaParser):
    """ Schema for :
        show wireless management trustpoint"""

    schema = {
        "trustpoint_name": str,
        "certificate_info": str,
        "private_key_info": str,
        "fips_suitability": str,
        Optional("certificate_type"): str,
        Optional("certificate_hash"): str
    }


# ========================================
# Parser for:
#  * 'show wireless management trustpoint'
# ========================================

class ShowWirelessManagementTrustPoint(ShowWirelessManagementTrustPointSchema):
    """Parser for :
        show wireless management trustpoint"""

    cli_command = 'show wireless management trustpoint'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ret_dict = {}

        # Trustpoint Name : ewlc-tp1  
        p1 = re.compile(r'^Trustpoint +Name +:( +(?P<trustpoint_name>.*))?$')
        
        # Certificate Info : Available
        p2 = re.compile(r'^Certificate +Info +: +(?P<certificate_info>.*)$')
        
        # Certificate Type : SSC
        p3 = re.compile(r'^Certificate +Type +: +(?P<certificate_type>.*)$')
        
        # FIPS suitability : Not Applicable
        p4 = re.compile(r'^FIPS +suitability +: +(?P<fips_suitability>.*)$')
        
        # Private key Info : Available
        p5 = re.compile(r'^Private +key +Info +: +(?P<private_key_info>.*)$')
        
        # Certificate Hash : 4a5d777c5b2071c17faef376febc08398702184e       
        p6 = re.compile(r'^Certificate +Hash +: +(?P<certificate_hash>.*)$')
        
         
        for line in out.splitlines():
        
            # Trustpoint Name : ewlc-tp1
            m = p1.match(line)            
            if m:
                trustpoint_name = m.groupdict()['trustpoint_name']
                if trustpoint_name:
                    ret_dict["trustpoint_name"] = trustpoint_name.strip()
                else:
                    ret_dict["trustpoint_name"] = ""
                
            # Certificate Info : Available                
            m = p2.match(line)
            if m:
                ret_dict["certificate_info"] = m.groupdict()['certificate_info'].strip()
        
            # Certificate Type : SSC        
            m = p3.match(line)
            if m:
                ret_dict["certificate_type"] = m.groupdict()['certificate_type'].strip()
                
            # FIPS suitability : Not Applicable        
            m = p4.match(line)
            if m:
                ret_dict["fips_suitability"] = m.groupdict()['fips_suitability'].strip()
        
            # Private key Info : Available         
            m = p5.match(line)
            if m:
                ret_dict["private_key_info"] = m.groupdict()['private_key_info'].strip()
        
            # Certificate Hash : 4a5d777c5b2071c17faef376febc08398702184e
            m = p6.match(line)
            if m:
                ret_dict["certificate_hash"] = m.groupdict()['certificate_hash'].strip()
              
        return ret_dict   


# ========================================
# Schema for:
#  * 'show wireless multicast'
# ========================================
class ShowWirelessMulticastSchema(MetaParser):
    """ Schema for :
        show wireless multicast"""

    schema = {
        "multicast": bool,
        "ap_capwap_multicast": str,
        "wireless_broadcast": bool,
        "mcast_no_ip_mcast": bool,
        "mcast_link_local": bool,
        Optional("ipv4_mcast_group_address"): str,
        Optional("ipv6_mcast_group_address"): str,
    }


# ========================================
# Parser for:
#  * 'show wireless multicast'
# ========================================
class ShowWirelessMulticast(ShowWirelessMulticastSchema):
    """Parser for :
        show wireless multicast"""

    cli_command = 'show wireless multicast'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ret_dict = {}

        str_to_bool_map = {
            'Enabled': True,
            'Disabled': False
        }

        # Multicast                               : Enabled
        p1_rgx = r'Multicast\s+:\s+(?P<multicast>(Enabled|Disabled))'

        # AP Capwap Multicast                     : Unicast
        p2_rgx = r'Capwap Multicast\s+:\s+(?P<ap_capwap_multicast>(Unicast|Multicast))'

        # Wireless Broadcast                      : Disabled
        p3_rgx = r'Broadcast\s+:\s+(?P<wireless_broadcast>(Enabled|Disabled))'

        # Wireless Multicast non-ip-mcast         : Disabled
        p4_rgx = r'non-ip-mcast\s+:\s+(?P<mcast_no_ip_mcast>(Enabled|Disabled))'

        # Wireless Multicast link-local           : Enabled
        p5_rgx = r'link-local\s+:\s+(?P<mcast_link_local>(Enabled|Disabled))'

        # AP Capwap IPv4 Multicast group Address  : 239.1.1.1
        p6_rgx = r'IPv4[\s\w]+:\s+(?P<ipv4>((\d{1,3}\.){3}\d{1,3}))'

        # AP Capwap IPv6 Multicast group Address  : ff11::1
        p7_rgx = r'IPv6[\s\w]+:\s+(?P<ipv6>(([a-fA-F\d]{1,4}:*:?){1,7}[a-fA-F\d]{1,4}))'

        for line in out.splitlines():

            # # Multicast                               : Enabled
            m = re.search(p1_rgx, line)
            if m:
                multicast = m.groupdict()['multicast']
                ret_dict['multicast'] = str_to_bool_map[multicast]
                continue

            # AP Capwap Multicast                     : Unicast
            m = re.search(p2_rgx, line)
            if m:
                ap_capwap_multicast = m.groupdict()['ap_capwap_multicast']
                ret_dict['ap_capwap_multicast'] = ap_capwap_multicast
                continue

            # Wireless Broadcast                      : Disabled
            m = re.search(p3_rgx, line)
            if m:
                wireless_broadcast = m.groupdict()['wireless_broadcast']
                ret_dict['wireless_broadcast'] = str_to_bool_map[wireless_broadcast]
                continue

            # Wireless Multicast non-ip-mcast         : Disabled
            m = re.search(p4_rgx, line)
            if m:
                mcast_no_ip_mcast = m.groupdict()['mcast_no_ip_mcast']
                ret_dict['mcast_no_ip_mcast'] = str_to_bool_map[mcast_no_ip_mcast]
                continue

            # Wireless Multicast link-local           : Enabled
            m = re.search(p5_rgx, line)
            if m:
                mcast_link_local = m.groupdict()['mcast_link_local']
                ret_dict['mcast_link_local'] = str_to_bool_map[mcast_link_local]
                continue

            # AP Capwap IPv4 Multicast group Address  : 239.1.1.1
            m = re.search(p6_rgx, line)
            if m:
                ipv4 = m.groupdict()['ipv4']
                ret_dict['ipv4_mcast_group_address'] = ipv4
                continue

            # AP Capwap IPv6 Multicast group Address  : ff11::1
            m = re.search(p7_rgx, line)
            if m:
                ipv6 = m.groupdict()['ipv6']
                ret_dict['ipv6_mcast_group_address'] = ipv6

        return ret_dict


# ========================================
# Schema for:
#  * 'show wireless profile flex summary'
# ========================================
class ShowWirelessProfileFlexSummarySchema(MetaParser):
    """ Schema for :
        show wireless profile flex summary"""

    schema = {
        "count": int,
        "flex_profiles": {
            Any(): {
                'description': Optional(str)
            }
        }
    }


# ========================================
# Parser for:
#  * 'show wireless profile flex summary'
# ========================================
class ShowWirelessProfileFlexSummary(ShowWirelessProfileFlexSummarySchema):
    """Parser for :
        show wireless profile flex summary"""

    cli_command = 'show wireless profile flex summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        # Number of Flex Profiles: 4
        p_count = re.compile(r'Number\sof\sFlex\sProfiles:\s(?P<count>\d+)')
        # ------------------------------------------------------------------------
        p_line = re.compile(r'-+$')
        # Flex Profile Name                 Description
        p_header = re.compile(r'Flex\sProfile\sName\s+Description')
        # myflexp1                          My first profile
        # myflexp2
        # myflexp3                          2023 profile
        p_line_double = re.compile(r'^(?P<flexp_name>[\w\.-]+)\s+(?P<desc>(\w+\s?)+)$|(?P<flexp_name_single>[\w\.-]+)')
        for line in output.splitlines():
            line = line.strip()
            flex_dict = ret_dict.setdefault('flex_profiles', {})
            # Flex Profile Name                 Description
            m = re.match(p_header, line)
            if m:
                continue
            # ------------------------------------------------------------------------
            m = re.match(p_line, line)
            if m:
                continue
            # Number of Flex Profiles: 4
            m = re.match(p_count, line)
            if m:
                ret_dict.update({'count': int(m.groupdict().get('count'))})
                continue
            # myflexp1                          My first profile
            # myflexp2
            # myflexp3                          2023 profile
            m = re.match(p_line_double, line)
            if m:
                m_dict = m.groupdict()
                flexp_name_single = m_dict.get('flexp_name_single')
                flexp_name = m_dict.get('flexp_name')
                flex_dict.update({flexp_name or flexp_name_single:{
                   'description': "" if flexp_name_single else m_dict['desc'].strip()
                   }})
                continue
            continue

        return ret_dict


# ========================================
# Schema for:
#  * 'show wireless tag site summary'
# ========================================
class ShowWirelessTagSiteSummarySchema(MetaParser):
    """ Schema for :
        show wireless tag site summary"""

    schema = {
        "count": int,
        "site_tags": {
            Any(): {
                'description': str
            }
        }
    }


# ========================================
# Parser for:
#  * 'show wireless tag site summary'
# ========================================
class ShowWirelessTagSiteSummary(ShowWirelessTagSiteSummarySchema):
    """Parser for :
        show wireless tag site summary"""

    cli_command = 'show wireless tag site summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        ret_dict = {}
        # Number of Site Tags: 7
        p_count = re.compile(r'Number\sof\sSite\sTags:\s(?P<count>\d+)')
        # ------------------------------------------------------------------------
        p_line = re.compile(r'-+$')
        # Site Tag Name                     Description
        p_header = re.compile(r'Site\sTag\sName\s+Description')
        # sometag                           Some description
        # sometagwithnodescription
        p_line_double = re.compile(r'^(?P<site_name>[\w\.-]+)\s+(?P<desc>(\w+\s?)+)$|(?P<site_name_single>[\w\.-]+)')
        for line in output.splitlines():
            line = line.strip()
            site_dict = ret_dict.setdefault('site_tags', {})
            # Site Tag Name                     Description
            m = re.match(p_header, line)
            if m:
                continue
            # ------------------------------------------------------------------------
            m = re.match(p_line, line)
            if m:
                continue
            # Number of Site Tags: 7
            m = re.match(p_count, line)
            if m:
                ret_dict.update({'count': int(m.groupdict().get('count'))})
                continue
            # sometag                           Some description
            # sometagwithnodescription
            m = re.match(p_line_double, line)
            if m:
                m_dict = m.groupdict()
                site_name_single = m_dict.get('site_name_single')
                site_name = m_dict.get('site_name')
                site_dict.update({site_name or site_name_single:{
                   'description': "" if site_name_single else m_dict['desc'].strip()
                   }})
                continue

        return ret_dict


# ========================================
# Schema for:
#  * 'show wireless mesh ap backhaul'
# ========================================
class ShowWirelessMeshApBackhaulSchema(MetaParser):
    """ Schema for :
        show wireless mesh ap backhaul"""

    schema = {
        Any(): {'backhaul_slot': str,
                'radio_type': str,
                'radio_subband': str,
                'mesh_radio_role': str,
                'admin_state': str,
                'oper_state': str,
                'current_channel': str,
                'antenna_type': str,
                'antenna_gain': str}
    }


# ========================================
# Parser for:
#  * 'show wireless mesh ap backhaul'
# ========================================
class ShowWirelessMeshApBackhaul(ShowWirelessMeshApBackhaulSchema):
    """Parser for :
        show wireless mesh ap backhaul"""

    cli_command = 'show wireless mesh ap backhaul'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        # MAC Address : 488b.0a78.c8a0
        p_mac_addr = re.compile(r"MAC\sAddress\s:\s+(?P<mac_add>(([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4}))")
        # Current Backhaul Slot: 1
        p_backhaul_slot = re.compile(r"^Current\sBackhaul\sSlot:\s+(?P<backhaul_slot>(\d))$")
        # Radio Type: Main
        p_radio_type = re.compile(r"^Radio\sType:\s+(?P<radio_type>(\w+))$")
        # Radio Subband: All
        p_radio_subband = re.compile(r"^Radio\sSubband:\s+(?P<radio_subband>(\w+))$")
        # Mesh Radio Role: Downlink
        p_mesh_radio_role = re.compile(r"^Mesh\sRadio\sRole:\s+(?P<mesh_radio_role>(\w+))$")
        # Administrative State: Disabled
        p_admin_state = re.compile(r"^Administrative\sState:\s+(?P<admin_state>(\w+))$")
        # Operation State: Down
        p_oper_state = re.compile(r"^Operation\sState:\s+(?P<oper_state>(\w+))$")
        # Current Tx Power Level: *4
        p_current_tx_power = re.compile(r"^CurrentsTx\sPower\sLevel:\s+(?P<current_tx_power>(\*?\d+))$")
        # Current Channel: (157,161)*
        p_current_channel = re.compile(r"^Current\sChannel:\s+(?P<current_channel>(\(\d+[,\d]+?\)\*?))$")
        # Antenna Type: C-ANT-DART-RPTNC
        p_antenna_type = re.compile(r"^Antenna\sType:\s?(?P<antenna_type>(N\/A|[\w-]+|$))")
        # Internal Antenna Gain (in .5 dBm units): 1
        p_antenna_gain = re.compile(r".* Gain \(.*\):\s(?P<antenna_gain>(\d+))$")

        for line in output.splitlines():
            line = line.strip()
            # MAC Address : 488b.0a78.c8a0
            m = re.match(p_mac_addr, line)
            if m:
                curr_mac = m.groupdict().get('mac_add').strip()
                mac_dict = ret_dict.setdefault(curr_mac, {})
                continue
            # Current Backhaul Slot: 1
            m = re.match(p_backhaul_slot, line)
            if m:
                mac_dict['backhaul_slot'] = m.groupdict().get('backhaul_slot')
                continue
            # Radio Type: Main
            m = re.match(p_radio_type, line)
            if m:
                mac_dict['radio_type'] = m.groupdict().get('radio_type')
                continue
            # Radio Subband: All
            m = re.match(p_radio_subband, line)
            if m:
                mac_dict['radio_subband'] = m.groupdict().get('radio_subband')
                continue
            # Mesh Radio Role: Downlink
            m = re.match(p_mesh_radio_role, line)
            if m:
                mac_dict['mesh_radio_role'] = m.groupdict().get('mesh_radio_role')
                continue
            # Administrative State: Disabled
            m = re.match(p_admin_state, line)
            if m:
                mac_dict['admin_state'] = m.groupdict().get('admin_state')
                continue
            # Operation State: Down
            m = re.match(p_oper_state, line)
            if m:
                mac_dict['oper_state'] = m.groupdict().get('oper_state')
                continue
            # Current Tx Power Level: *4
            m = re.match(p_current_tx_power, line)
            if m:
                mac_dict['current_tx_power'] = m.groupdict().get('current_tx_power')
                continue
            # Current Channel: (157,161)*
            m = re.match(p_current_channel, line)
            if m:
                mac_dict['current_channel'] = m.groupdict().get('current_channel')
                continue
            # Antenna Type: C-ANT-DART-RPTNC|N/A
            m = re.match(p_antenna_type, line)
            if m:
                mac_dict['antenna_type'] = m.groupdict().get('antenna_type')
                continue
            # Internal Antenna Gain (in .5 dBm units): 1
            m = re.match(p_antenna_gain, line)
            if m:
                mac_dict['antenna_gain'] = m.groupdict().get('antenna_gain')
                continue

        return ret_dict
