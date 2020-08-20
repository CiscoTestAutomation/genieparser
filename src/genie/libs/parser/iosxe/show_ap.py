import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ===========================
# Schema for:
#  * 'show ap config general'
# ===========================
class ShowApConfigGeneralSchema(MetaParser):
    """Schema for show ap config general."""

    schema = {
        "ap_config_general_info": {
            str: {
                "cisco_ap_identifier": str,
                "country_code": str,
                "regulatory_domain_allowed_by_country": str,
                "ap_country_code": str,
                "slot_0": str,
                "slot_1": str,
                "mac_address": str,
                "ip_address_configuration": str,
                "ip_address": str,
                "ip_netmask": str,
                "gateway_ip_address": str,
                "fallback_ip_address_being_used": str,
                "domain": str,
                "name_server": str,
                "capwap_path_mtu": int,
                "capwap_active_window_size": int,
                "telnet_state": str,
                "cpu_type": str,
                "memory_type": str,
                "memory_size": str,
                "ssh_state": str,
                "cisco_ap_location": str,
                "site_tag_name": str,
                "rf_tag_name": str,
                "policy_tag_name": str,
                "ap_join_profile": str,
                "flex_profile": str,
                "ap_filter_name": str,
                "primary_cisco_controller_name": str,
                "primary_cisco_controller_ip_address": str,
                "secondary_cisco_controller_name": str,
                "secondary_cisco_controller_ip_address": str,
                "tertiary_cisco_controller_name": str,
                "tertiary_cisco_controller_ip_address": str,
                "administrative_state": str,
                "operation_state": str,
                "nat_external_ip_address": str,
                "ap_certificate_type": str,
                "ap_mode": str,
                "ap_vlan_tagging_state": str,
                "ap_vlan_tag": int,
                "capwap_preferred_mode": str,
                "capwap_udp_lite": str,
                "ap_submode": str,
                "office_extend_mode": str,
                "dhcp_server": str,
                "remote_ap_debug": str,
                "logging_trap_severity_level": str,
                "logging_syslog_facility": str,
                "software_version": str,
                "boot_version": str,
                "mini_ios_version": str,
                "stats_reporting_period": int,
                "led_state": str,
                "led_flash_state": str,
                "led_flash_timer": int,
                "mdns_group_id": int,
                "mdns_rule_name": str,
                "poe_pre_standard_switch": str,
                "poe_power_injector_mac_address": str,
                "power_type/mode": str,
                "number_of_slots": int,
                "ap_model": str,
                "ios_version": str,
                "reset_button": str,
                "ap_serial_number": str,
                "management_frame_validation": str,
                "management_frame_protection": str,
                "ap_user_name": str,
                "ap_802.1x_user_mode": str,
                "ap_802.1x_user_name": str,
                "cisco_ap_system_logging_host": str,
                "cisco_ap_secured_logging_tls_mode": str,
                "ap_up_time": str,
                "ap_capwap_up_time": str,
                "join_date_and_time": str,
                "join_taken_time": str,
                "join_priority": int,
                "ap_link_latency": str,
                "ap_lag_configuration_status": str,
                "lag_support_for_ap": str,
                "rogue_detection": str,
                "rogue_containment_auto_rate": str,
                "rogue_containment_of_standalone_flexconnect_aps": str,
                "rogue_detection_report_interval": int,
                "rogue_ap_minimum_rssi": float,
                "rogue_ap_minimum_transient_time": int,
                "ap_tcp_mss_adjust": str,
                "ap_tcp_mss_size": int,
                "ap_ipv6_tcp_mss_adjust": str,
                "ap_ipv6_tcp_mss_size": int,
                "hyperlocation_admin_status": str,
                "retransmit_count": int,
                "retransmit_interval": int,
                "fabric_status": str,
                "fips_status": str,
                "wlancc_status": str,
                "usb_module_type": str,
                "usb_module_state": str,
                "usb_operational_state": str,
                "usb_override": str,
                "gas_rate_limit_admin_status": str,
                "wpa3_capability": str,
                "ewc_ap_capability": str,
                "awips_capability": str,
                "proxy_hostname": str,
                "proxy_port": str,
                "proxy_no_proxy_list": str,
                "grpc_server_status": str,
                "unencrypted_data_keep_alive": str,
                "local_dhcp_server": str,
                "traffic_distribution_statistics_capability": str,
                "dual_dfs_statistics": str
            }
        }
    }


# ===========================
# Parser for:
#  * 'show ap config general'
# ===========================
class ShowApConfigGeneral(ShowApConfigGeneralSchema):
    """Parser for show ap config general"""

    cli_command = 'show ap config general'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ap_config_general_dict = {}

#         Cisco AP Name   : bg-1-cap1
# =================================================
#
# Cisco AP Identifier                             : 70b3.d278.e03e
# Country Code                                    : IN
# Regulatory Domain Allowed by Country            : 802.11bg:-A   802.11a:-DN
# AP Country Code                                 : IN  - India
# AP Regulatory Domain
#   Slot 0                                        : -A
#   Slot 1                                        : -D
# MAC Address                                     : 70b3.1711.acbb
# IP Address Configuration                        : DHCP
# IP Address                                      : 10.10.5.14
# IP Netmask                                      : 255.255.254.0
# Gateway IP Address                              : 10.10.5.1
# Fallback IP Address Being Used                  :
# Domain                                          :
# Name Server                                     :
# CAPWAP Path MTU                                 : 1485
# Capwap Active Window Size                       : 1
# Telnet State                                    : Disabled
# CPU Type                                        :  ARMv7 Processor rev 1 (v7l)
# Memory Type                                     : DDR3
# Memory Size                                     : 1028096 KB
# SSH State                                       : Enabled
# Cisco AP Location                               : default location
# Site Tag Name                                   : b8
# RF Tag Name                                     : Custom-RF
# Policy Tag Name                                 : b1_policy_tag
# AP join Profile                                 : APG_b18
# Flex Profile                                    : default-flex-profile
# AP Filter name                                  : b8
# Primary Cisco Controller Name                   : b7-wl-ewlc1
# Primary Cisco Controller IP Address             : 10.6.4.17
# Secondary Cisco Controller Name                 : b8-wl-wlc3
# Secondary Cisco Controller IP Address           : 10.6.7.16
# Tertiary Cisco Controller Name                  : b3-wl-wlc3
# Tertiary Cisco Controller IP Address            : 10.6.4.17
# Administrative State                            : Enabled
# Operation State                                 : Registered
# NAT External IP Address                         : 10.10.5.12
# AP Certificate type                             : Manufacturer Installed Certificate
# AP Mode                                         : Local
# AP VLAN tagging state                           : Disabled
# AP VLAN tag                                     : 0
# CAPWAP Preferred mode                           : IPv4
# CAPWAP UDP-Lite                                 : Not Configured
# AP Submode                                      : Not Configured
# Office Extend Mode                              : Disabled
# Dhcp Server                                     : Disabled
# Remote AP Debug                                 : Disabled
# Logging Trap Severity Level                     : information
# Logging Syslog facility                         : kern
# Software Version                                : 17.3.1.9
# Boot Version                                    : 1.1.2.4
# Mini IOS Version                                : 0.0.0.0
# Stats Reporting Period                          : 0
# LED State                                       : Enabled
# LED Flash State                                 : Enabled
# LED Flash Timer                                 : 0
# MDNS Group Id                                   : 0
# MDNS Rule Name                                  :
# PoE Pre-Standard Switch                         : Disabled
# PoE Power Injector MAC Address                  : Disabled
# Power Type/Mode                                 : PoE/Full Power
# Number of Slots                                 : 3
# AP Model                                        : AIR-AP4800-D-K9
# IOS Version                                     : 17.3.1.9
# Reset Button                                    : Disabled
# AP Serial Number                                : FGL2102AZZZ
# Management Frame Validation                     : Capable
# Management Frame Protection                     : Capable
# AP User Name                                    : admin
# AP 802.1X User Mode                             : Global
# AP 802.1X User Name                             : Not Configured
# Cisco AP System Logging Host                    : 10.16.19.6
# Cisco AP Secured Logging TLS mode               : Disabled
# AP Up Time                                      : 3 days 9 hours 44 minutes 18 seconds
# AP CAPWAP Up Time                               : 3 days 9 hours 37 minutes 20 seconds
# Join Date and Time                              : 08/14/2020 19:48:09
# Join Taken Time                                 : 6 minutes 57 seconds
# Join Priority                                   : 1
# AP Link Latency                                 : Disable
# AP Lag Configuration Status                     : Disabled
# Lag Support for AP                              : Yes
# Rogue Detection                                 : Enabled
# Rogue Containment auto-rate                     : Disabled
# Rogue Containment of standalone flexconnect APs : Disabled
# Rogue Detection Report Interval                 : 10
# Rogue AP minimum RSSI                           : -70
# Rogue AP minimum transient time                 : 0
# AP TCP MSS Adjust                               : Enabled
# AP TCP MSS Size                                 : 1250
# AP IPv6 TCP MSS Adjust                          : Enabled
# AP IPv6 TCP MSS Size                            : 1250
# Hyperlocation Admin Status                      : Disabled
# Retransmit count                                : 5
# Retransmit interval                             : 3
# Fabric status                                   : Disabled
# FIPS status                                     : Disabled
# WLANCC status                                   : Disabled
# USB Module Type                                 : USB Module
# USB Module State                                : Enabled
# USB Operational State                           : Disabled
# USB Override                                    : Disabled
# GAS rate limit Admin status                     : Disabled
# WPA3 Capability                                 : Enabled
# EWC-AP Capability                               : Disabled
# AWIPS Capability                                : Enabled
# Proxy Hostname                                  : Not Configured
# Proxy Port                                      : Not Configured
# Proxy NO_PROXY list                             : Not Configured
# GRPC server status                              : Disabled
# Unencrypted Data Keep Alive                     : Enabled
# Local DHCP Server                               : Disabled
# Traffic Distribution Statistics Capability      : Enabled
# Dual DFS Statistics                             : Disabled
#
# Cisco AP Name   : b8-01-cap2
# =================================================
#
# Cisco AP Identifier                             : 70b3.1736.220e
# Country Code                                    : IN
# Regulatory Domain Allowed by Country            : 802.11bg:-A   802.11a:-DN
# AP Country Code                                 : IN  - India
# AP Regulatory Domain
#   Slot 0                                        : -D
#   Slot 1                                        : -D
# MAC Address                                     : 70b3.1788.aaaa
# IP Address Configuration                        : DHCP
# IP Address                                      : 10.10.5.22
# IP Netmask                                      : 255.255.254.0
# Gateway IP Address                              : 10.10.5.1
# Fallback IP Address Being Used                  :
# Domain                                          :
# Name Server                                     :
# CAPWAP Path MTU                                 : 1485
# Capwap Active Window Size                       : 1
# Telnet State                                    : Disabled
# CPU Type                                        :  ARMv7 Processor rev 1 (v7l)
# Memory Type                                     : DDR3
# Memory Size                                     : 1028096 KB
# SSH State                                       : Enabled
# Cisco AP Location                               : default location
# Site Tag Name                                   : b8
# RF Tag Name                                     : Custom-RF
# Policy Tag Name                                 : b8_policy_tag
# AP join Profile                                 : APG_bgl8
# Flex Profile                                    : default-flex-profile
# AP Filter name                                  : b8
# Primary Cisco Controller Name                   : b17-wl-ewlc1
# Primary Cisco Controller IP Address             : 10.6.4.17
# Secondary Cisco Controller Name                 : b7-wl-wlc3
# Secondary Cisco Controller IP Address           : 10.6.4.16
# Tertiary Cisco Controller Name                  : b1-wl-wlc3
# Tertiary Cisco Controller IP Address            : 10.6.4.12
# Administrative State                            : Enabled
# Operation State                                 : Registered
# NAT External IP Address                         : 10.10.5.22
# AP Certificate type                             : Manufacturer Installed Certificate
# AP Mode                                         : Local
# AP VLAN tagging state                           : Disabled
# AP VLAN tag                                     : 0
# CAPWAP Preferred mode                           : IPv4
# CAPWAP UDP-Lite                                 : Not Configured
# AP Submode                                      : Not Configured
# Office Extend Mode                              : Disabled
# Dhcp Server                                     : Disabled
# Remote AP Debug                                 : Disabled
# Logging Trap Severity Level                     : information
# Logging Syslog facility                         : kern
# Software Version                                : 17.3.1.9
# Boot Version                                    : 1.1.2.4
# Mini IOS Version                                : 0.0.0.0
# Stats Reporting Period                          : 0
# LED State                                       : Enabled
# LED Flash State                                 : Enabled
# LED Flash Timer                                 : 0
# MDNS Group Id                                   : 0
# MDNS Rule Name                                  :
# PoE Pre-Standard Switch                         : Disabled
# PoE Power Injector MAC Address                  : Disabled
# Power Type/Mode                                 : PoE/Full Power
# Number of Slots                                 : 3
# AP Model                                        : AIR-AP4800-D-K9
# IOS Version                                     : 17.3.1.9
# Reset Button                                    : Disabled
# AP Serial Number                                : FGL2AA4BA78Z
# Management Frame Validation                     : Capable
# Management Frame Protection                     : Capable
# AP User Name                                    : admin
# AP 802.1X User Mode                             : Global
# AP 802.1X User Name                             : Not Configured
# Cisco AP System Logging Host                    : 10.16.19.6
# Cisco AP Secured Logging TLS mode               : Disabled
# AP Up Time                                      : 3 days 9 hours 44 minutes 17 seconds
# AP CAPWAP Up Time                               : 3 days 9 hours 37 minutes 16 seconds
# Join Date and Time                              : 08/14/2020 19:48:13
# Join Taken Time                                 : 7 minutes 0 second
# Join Priority                                   : 1
# AP Link Latency                                 : Disable
# AP Lag Configuration Status                     : Disabled
# Lag Support for AP                              : Yes
# Rogue Detection                                 : Enabled
# Rogue Containment auto-rate                     : Disabled
# Rogue Containment of standalone flexconnect APs : Disabled
# Rogue Detection Report Interval                 : 10
# Rogue AP minimum RSSI                           : -70
# Rogue AP minimum transient time                 : 0
# AP TCP MSS Adjust                               : Enabled
# AP TCP MSS Size                                 : 1250
# AP IPv6 TCP MSS Adjust                          : Enabled
# AP IPv6 TCP MSS Size                            : 1250
# Hyperlocation Admin Status                      : Disabled
# Retransmit count                                : 5
# Retransmit interval                             : 3
# Fabric status                                   : Disabled
# FIPS status                                     : Disabled
# WLANCC status                                   : Disabled
# USB Module Type                                 : USB Module
# USB Module State                                : Enabled
# USB Operational State                           : Disabled
# USB Override                                    : Disabled
# GAS rate limit Admin status                     : Disabled
# WPA3 Capability                                 : Enabled
# EWC-AP Capability                               : Disabled
# AWIPS Capability                                : Enabled
# Proxy Hostname                                  : Not Configured
# Proxy Port                                      : Not Configured
# Proxy NO_PROXY list                             : Not Configured
# GRPC server status                              : Disabled
# Unencrypted Data Keep Alive                     : Enabled
# Local DHCP Server                               : Disabled
# Traffic Distribution Statistics Capability      : Enabled
# Dual DFS Statistics                             : Disabled
#
#
# Cisco AP Name   : b8-1-cap3
# =================================================
#
# Cisco AP Identifier                             : f4db.e2b4.2046
# Country Code                                    : IN
# Regulatory Domain Allowed by Country            : 802.11bg:-A   802.11a:-DN
# AP Country Code                                 : IN  - India
# AP Regulatory Domain
#   Slot 0                                        : -D
#   Slot 1                                        : -D
# MAC Address                                     : f4db.6e83.e878
# IP Address Configuration                        : DHCP
# IP Address                                      : 10.10.55.12
# IP Netmask                                      : 255.255.254.0
# Gateway IP Address                              : 10.105.54.1
# Fallback IP Address Being Used                  :
# Domain                                          :
# Name Server                                     :
# CAPWAP Path MTU                                 : 1485
# Capwap Active Window Size                       : 1
# Telnet State                                    : Disabled
# CPU Type                                        :  ARMv7 Processor rev 1 (v7l)
# Memory Type                                     : DDR3
# Memory Size                                     : 1028096 KB
# SSH State                                       : Enabled
# Cisco AP Location                               : default location
# Site Tag Name                                   : b8
# RF Tag Name                                     : Custom-RF
# Policy Tag Name                                 : b8_policy_tag
# AP join Profile                                 : APG_b8
# Flex Profile                                    : default-flex-profile
# AP Filter name                                  : b8
# Primary Cisco Controller Name                   : b7-wl-ewlc1
# Primary Cisco Controller IP Address             : 10.6.4.17
# Secondary Cisco Controller Name                 : b7-wl-wlc3
# Secondary Cisco Controller IP Address           : 10.6.4.16
# Tertiary Cisco Controller Name                  : b3-wl-wlc3
# Tertiary Cisco Controller IP Address            : 10.64.7.12
# Administrative State                            : Enabled
# Operation State                                 : Registered
# NAT External IP Address                         : 10.10.5.18
# AP Certificate type                             : Manufacturer Installed Certificate
# AP Mode                                         : Local
# AP VLAN tagging state                           : Disabled
# AP VLAN tag                                     : 0
# CAPWAP Preferred mode                           : IPv4
# CAPWAP UDP-Lite                                 : Not Configured
# AP Submode                                      : Not Configured
# Office Extend Mode                              : Disabled
# Dhcp Server                                     : Disabled
# Remote AP Debug                                 : Disabled
# Logging Trap Severity Level                     : information
# Logging Syslog facility                         : kern
# Software Version                                : 17.3.1.9
# Boot Version                                    : 1.1.2.4
# Mini IOS Version                                : 0.0.0.0
# Stats Reporting Period                          : 0
# LED State                                       : Enabled
# LED Flash State                                 : Enabled
# LED Flash Timer                                 : 0
# MDNS Group Id                                   : 0
# MDNS Rule Name                                  :
# PoE Pre-Standard Switch                         : Disabled
# PoE Power Injector MAC Address                  : Disabled
# Power Type/Mode                                 : PoE/Full Power
# Number of Slots                                 : 3
# AP Model                                        : AIR-AP4800-D-K9
# IOS Version                                     : 17.3.1.9
# Reset Button                                    : Disabled
# AP Serial Number                                : FGL2302A7AZ
# Management Frame Validation                     : Capable
# Management Frame Protection                     : Capable
# AP User Name                                    : admin
# AP 802.1X User Mode                             : Global
# AP 802.1X User Name                             : Not Configured
# Cisco AP System Logging Host                    : 10.16.12.6
# Cisco AP Secured Logging TLS mode               : Disabled
# AP Up Time                                      : 3 days 9 hours 44 minutes 17 seconds
# AP CAPWAP Up Time                               : 3 days 9 hours 39 minutes 22 seconds
# Join Date and Time                              : 08/14/2020 19:46:07
# Join Taken Time                                 : 4 minutes 54 seconds
# Join Priority                                   : 1
# AP Link Latency                                 : Disable
# AP Lag Configuration Status                     : Disabled
# Lag Support for AP                              : Yes
# Rogue Detection                                 : Enabled
# Rogue Containment auto-rate                     : Disabled
# Rogue Containment of standalone flexconnect APs : Disabled
# Rogue Detection Report Interval                 : 10
# Rogue AP minimum RSSI                           : -70
# Rogue AP minimum transient time                 : 0
# AP TCP MSS Adjust                               : Enabled
# AP TCP MSS Size                                 : 1250
# AP IPv6 TCP MSS Adjust                          : Enabled
# AP IPv6 TCP MSS Size                            : 1250
# Hyperlocation Admin Status                      : Disabled
# Retransmit count                                : 5
# Retransmit interval                             : 3
# Fabric status                                   : Disabled
# FIPS status                                     : Disabled
# WLANCC status                                   : Disabled
# USB Module Type                                 : USB Module
# USB Module State                                : Enabled
# USB Operational State                           : Disabled
# USB Override                                    : Disabled
# GAS rate limit Admin status                     : Disabled
# WPA3 Capability                                 : Enabled
# EWC-AP Capability                               : Disabled
# AWIPS Capability                                : Enabled
# Proxy Hostname                                  : Not Configured
# Proxy Port                                      : Not Configured
# Proxy NO_PROXY list                             : Not Configured
# GRPC server status                              : Disabled
# Unencrypted Data Keep Alive                     : Enabled
# Local DHCP Server                               : Disabled
# Traffic Distribution Statistics Capability      : Enabled
# Dual DFS Statistics                             : Disabled
#
# Cisco AP Name   : b8-1-cap4
# =================================================
#
# Cisco AP Identifier                             : 70b3.1745.2750
# Country Code                                    : IN
# Regulatory Domain Allowed by Country            : 802.11bg:-A   802.11a:-DN
# AP Country Code                                 : IN  - India
# AP Regulatory Domain
#   Slot 0                                        : -A
#   Slot 1                                        : -D
# MAC Address                                     : 70b3.1728.b7a8
# IP Address Configuration                        : DHCP
# IP Address                                      : 10.10.5.17
# IP Netmask                                      : 255.255.254.0
# Gateway IP Address                              : 10.10.5.1
# Fallback IP Address Being Used                  :
# Domain                                          :
# Name Server                                     :
# CAPWAP Path MTU                                 : 1485
# Capwap Active Window Size                       : 1
# Telnet State                                    : Disabled
# CPU Type                                        :  ARMv7 Processor rev 1 (v7l)
# Memory Type                                     : DDR3
# Memory Size                                     : 1028096 KB
# SSH State                                       : Enabled
# Cisco AP Location                               : default location
# Site Tag Name                                   : b8
# RF Tag Name                                     : Custom-RF
# Policy Tag Name                                 : b8_policy_tag
# AP join Profile                                 : APG_b8
# Flex Profile                                    : default-flex-profile
# AP Filter name                                  : b8
# Primary Cisco Controller Name                   : b7-wl-ewlc1
# Primary Cisco Controller IP Address             : 10.6.4.17
# Secondary Cisco Controller Name                 : b7-wl-wlc3
# Secondary Cisco Controller IP Address           : 10.6.4.16
# Tertiary Cisco Controller Name                  : b3-wl-wlc3
# Tertiary Cisco Controller IP Address            : 10.6.7.72
# Administrative State                            : Enabled
# Operation State                                 : Registered
# NAT External IP Address                         : 10.10.5.73
# AP Certificate type                             : Manufacturer Installed Certificate
# AP Mode                                         : Local
# AP VLAN tagging state                           : Disabled
# AP VLAN tag                                     : 0
# CAPWAP Preferred mode                           : IPv4
# CAPWAP UDP-Lite                                 : Not Configured
# AP Submode                                      : Not Configured
# Office Extend Mode                              : Disabled
# Dhcp Server                                     : Disabled
# Remote AP Debug                                 : Disabled
# Logging Trap Severity Level                     : information
# Logging Syslog facility                         : kern
# Software Version                                : 17.3.1.9
# Boot Version                                    : 1.1.2.4
# Mini IOS Version                                : 0.0.0.0
# Stats Reporting Period                          : 0
# LED State                                       : Enabled
# LED Flash State                                 : Enabled
# LED Flash Timer                                 : 0
# MDNS Group Id                                   : 0
# MDNS Rule Name                                  :
# PoE Pre-Standard Switch                         : Disabled
# PoE Power Injector MAC Address                  : Disabled
# Power Type/Mode                                 : PoE/Full Power
# Number of Slots                                 : 3
# AP Model                                        : AIR-AP4800-D-K9
# IOS Version                                     : 17.3.1.9
# Reset Button                                    : Disabled
# AP Serial Number                                : FGL342A0082
# Management Frame Validation                     : Capable
# Management Frame Protection                     : Capable
# AP User Name                                    : admin
# AP 802.1X User Mode                             : Global
# AP 802.1X User Name                             : Not Configured
# Cisco AP System Logging Host                    : 10.10.12.6
# Cisco AP Secured Logging TLS mode               : Disabled
# AP Up Time                                      : 3 days 9 hours 44 minutes 21 seconds
# AP CAPWAP Up Time                               : 3 days 9 hours 39 minutes 30 seconds
# Join Date and Time                              : 08/14/2020 19:45:59
# Join Taken Time                                 : 4 minutes 50 seconds
# Join Priority                                   : 1
# AP Link Latency                                 : Disable
# AP Lag Configuration Status                     : Disabled
# Lag Support for AP                              : Yes
# Rogue Detection                                 : Enabled
# Rogue Containment auto-rate                     : Disabled
# Rogue Containment of standalone flexconnect APs : Disabled
# Rogue Detection Report Interval                 : 10
# Rogue AP minimum RSSI                           : -70
# Rogue AP minimum transient time                 : 0
# AP TCP MSS Adjust                               : Enabled
# AP TCP MSS Size                                 : 1250
# AP IPv6 TCP MSS Adjust                          : Enabled
# AP IPv6 TCP MSS Size                            : 1250
# Hyperlocation Admin Status                      : Disabled
# Retransmit count                                : 5
# Retransmit interval                             : 3
# Fabric status                                   : Disabled
# FIPS status                                     : Disabled
# WLANCC status                                   : Disabled
# USB Module Type                                 : USB Module
# USB Module State                                : Enabled
# USB Operational State                           : Disabled
# USB Override                                    : Disabled
# GAS rate limit Admin status                     : Disabled
# WPA3 Capability                                 : Enabled
# EWC-AP Capability                               : Disabled
# AWIPS Capability                                : Enabled
# Proxy Hostname                                  : Not Configured
# Proxy Port                                      : Not Configured
# Proxy NO_PROXY list                             : Not Configured
# GRPC server status                              : Disabled
# Unencrypted Data Keep Alive                     : Enabled
# Local DHCP Server                               : Disabled
# Traffic Distribution Statistics Capability      : Enabled
# Dual DFS Statistics                             : Disabled

        regex_patterns = {
            'ap_config_general': re.compile(r"^(?P<key>.*)\s+:(?P<value>.*)$")
        }

        remove_lines = ('====', 'AP Regulatory')

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        def match_regex(line, regex_patterns):
            groups = {}
            for capture, pattern in regex_patterns.items():
                if pattern.match(line):
                    match = pattern.match(line)
                    groups = match.groupdict()
            return groups

        out_filter = filter_lines(raw_output=out, remove_lines=remove_lines)
        ap_name_key = ''

        for line in out_filter:
            # This output will capture the key values with the ':' as the delimeter
            captured_groups = match_regex(line=line, regex_patterns=regex_patterns)
            if captured_groups:
                # Normalize the key to replace spaces and hyphens with underscores
                k = captured_groups['key'].strip().replace(' ', '_').replace('-', '_').lower()
                v = captured_groups['value'].strip()
                # Change strings to integers if possible
                if v.isdigit():
                    v = int(v)
                else:
                    try:
                        # Change strings to float if possible
                        v = float(v)
                    except ValueError:
                        # if the value is not an int or float, leave it as a string.
                        pass
                # if there was a match, captured_groups should be populated with the groups.
                if captured_groups:
                    if not ap_config_general_dict.get('ap_config_general_info', {}):
                        ap_config_general_dict['ap_config_general_info'] = {}
                    # define the cisco_ap_name as the main key
                    if k == 'cisco_ap_name':
                        ap_name_key = v
                        ap_config_general_dict['ap_config_general_info'][ap_name_key] = {}
                    else:
                        ap_config_general_dict['ap_config_general_info'][ap_name_key].update({k: v})

        return ap_config_general_dict

