import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_ap import ShowApConfigGeneral


# ======================================
# Unit test for 'show ap config general'
# ======================================
class TestShowApConfigGeneral(unittest.TestCase):
    """Unit test for 'show ap config general'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
        "ap_config_general_info": {
            "bg-1-cap1": {
                "cisco_ap_identifier": "70b3.d278.e03e",
                "country_code": "IN",
                "regulatory_domain_allowed_by_country": "802.11bg:-A   802.11a:-DN",
                "ap_country_code": "IN  - India",
                "slot_0": "-A",
                "slot_1": "-D",
                "mac_address": "70b3.1711.acbb",
                "ip_address_configuration": "DHCP",
                "ip_address": "10.10.5.14",
                "ip_netmask": "255.255.254.0",
                "gateway_ip_address": "10.10.5.1",
                "capwap_path_mtu": 1485,
                "capwap_active_window_size": 1,
                "telnet_state": "Disabled",
                "cpu_type": "ARMv7 Processor rev 1 (v7l)",
                "memory_type": "DDR3",
                "memory_size": "1028096 KB",
                "ssh_state": "Enabled",
                "cisco_ap_location": "default location",
                "site_tag_name": "b8",
                "rf_tag_name": "Custom-RF",
                "policy_tag_name": "b1_policy_tag",
                "ap_join_profile": "APG_b18",
                "flex_profile": "default-flex-profile",
                "ap_filter_name": "b8",
                "primary_cisco_controller_name": "b7-wl-ewlc1",
                "primary_cisco_controller_ip_address": "10.6.4.17",
                "secondary_cisco_controller_name": "b8-wl-wlc3",
                "secondary_cisco_controller_ip_address": "10.6.7.16",
                "tertiary_cisco_controller_name": "b3-wl-wlc3",
                "tertiary_cisco_controller_ip_address": "10.6.4.17",
                "administrative_state": "Enabled",
                "operation_state": "Registered",
                "nat_external_ip_address": "10.10.5.12",
                "ap_certificate_type": "Manufacturer Installed Certificate",
                "ap_mode": "Local",
                "ap_vlan_tagging_state": "Disabled",
                "ap_vlan_tag": 0,
                "capwap_preferred_mode": "IPv4",
                "capwap_udp_lite": "Not Configured",
                "ap_submode": "Not Configured",
                "office_extend_mode": "Disabled",
                "dhcp_server": "Disabled",
                "remote_ap_debug": "Disabled",
                "logging_trap_severity_level": "information",
                "logging_syslog_facility": "kern",
                "software_version": "17.3.1.9",
                "boot_version": "1.1.2.4",
                "mini_ios_version": "0.0.0.0",
                "stats_reporting_period": 0,
                "led_state": "Enabled",
                "led_flash_state": "Enabled",
                "led_flash_timer": 0,
                "mdns_group_id": 0,
                "poe_pre_standard_switch": "Disabled",
                "poe_power_injector_mac_address": "Disabled",
                "power_type_mode": "PoE/Full Power",
                "number_of_slots": 3,
                "ap_model": "AIR-AP4800-D-K9",
                "ios_version": "17.3.1.9",
                "reset_button": "Disabled",
                "ap_serial_number": "FGL2102AZZZ",
                "management_frame_validation": "Capable",
                "management_frame_protection": "Capable",
                "ap_user_name": "admin",
                "ap_802_1x_user_mode": "Global",
                "ap_802_1x_user_name": "Not Configured",
                "cisco_ap_system_logging_host": "10.16.19.6",
                "cisco_ap_secured_logging_tls_mode": "Disabled",
                "ap_up_time": "3 days 9 hours 44 minutes 18 seconds",
                "ap_capwap_up_time": "3 days 9 hours 37 minutes 20 seconds",
                "join_date_and_time": "08/14/2020 19:48:09",
                "join_taken_time": "6 minutes 57 seconds",
                "join_priority": 1,
                "ap_link_latency": "Disable",
                "ap_lag_configuration_status": "Disabled",
                "lag_support_for_ap": "Yes",
                "rogue_detection": "Enabled",
                "rogue_containment_auto_rate": "Disabled",
                "rogue_containment_of_standalone_flexconnect_aps": "Disabled",
                "rogue_detection_report_interval": 10,
                "rogue_ap_minimum_rssi": -70.0,
                "rogue_ap_minimum_transient_time": 0,
                "ap_tcp_mss_adjust": "Enabled",
                "ap_tcp_mss_size": 1250,
                "ap_ipv6_tcp_mss_adjust": "Enabled",
                "ap_ipv6_tcp_mss_size": 1250,
                "hyperlocation_admin_status": "Disabled",
                "retransmit_count": 5,
                "retransmit_interval": 3,
                "fabric_status": "Disabled",
                "fips_status": "Disabled",
                "wlancc_status": "Disabled",
                "usb_module_type": "USB Module",
                "usb_module_state": "Enabled",
                "usb_operational_state": "Disabled",
                "usb_override": "Disabled",
                "gas_rate_limit_admin_status": "Disabled",
                "wpa3_capability": "Enabled",
                "ewc_ap_capability": "Disabled",
                "awips_capability": "Enabled",
                "proxy_hostname": "Not Configured",
                "proxy_port": "Not Configured",
                "proxy_no_proxy_list": "Not Configured",
                "grpc_server_status": "Disabled",
                "unencrypted_data_keep_alive": "Enabled",
                "local_dhcp_server": "Disabled",
                "traffic_distribution_statistics_capability": "Enabled",
                "dual_dfs_statistics": "Disabled"
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
Cisco AP Name   : bg-1-cap1
=================================================

Cisco AP Identifier                             : 70b3.d278.e03e
Country Code                                    : IN
Regulatory Domain Allowed by Country            : 802.11bg:-A   802.11a:-DN
AP Country Code                                 : IN  - India
AP Regulatory Domain
  Slot 0                                        : -A
  Slot 1                                        : -D
MAC Address                                     : 70b3.1711.acbb
IP Address Configuration                        : DHCP
IP Address                                      : 10.10.5.14
IP Netmask                                      : 255.255.254.0
Gateway IP Address                              : 10.10.5.1
Fallback IP Address Being Used                  : 
Domain                                          : 
Name Server                                     : 
CAPWAP Path MTU                                 : 1485
Capwap Active Window Size                       : 1
Telnet State                                    : Disabled
CPU Type                                        :  ARMv7 Processor rev 1 (v7l)
Memory Type                                     : DDR3
Memory Size                                     : 1028096 KB
SSH State                                       : Enabled
Cisco AP Location                               : default location
Site Tag Name                                   : b8
RF Tag Name                                     : Custom-RF
Policy Tag Name                                 : b1_policy_tag
AP join Profile                                 : APG_b18
Flex Profile                                    : default-flex-profile
AP Filter name                                  : b8
Primary Cisco Controller Name                   : b7-wl-ewlc1
Primary Cisco Controller IP Address             : 10.6.4.17
Secondary Cisco Controller Name                 : b8-wl-wlc3
Secondary Cisco Controller IP Address           : 10.6.7.16
Tertiary Cisco Controller Name                  : b3-wl-wlc3
Tertiary Cisco Controller IP Address            : 10.6.4.17
Administrative State                            : Enabled
Operation State                                 : Registered
NAT External IP Address                         : 10.10.5.12
AP Certificate type                             : Manufacturer Installed Certificate
AP Mode                                         : Local
AP VLAN tagging state                           : Disabled
AP VLAN tag                                     : 0
CAPWAP Preferred mode                           : IPv4
CAPWAP UDP-Lite                                 : Not Configured
AP Submode                                      : Not Configured
Office Extend Mode                              : Disabled
Dhcp Server                                     : Disabled
Remote AP Debug                                 : Disabled
Logging Trap Severity Level                     : information
Logging Syslog facility                         : kern
Software Version                                : 17.3.1.9
Boot Version                                    : 1.1.2.4
Mini IOS Version                                : 0.0.0.0
Stats Reporting Period                          : 0
LED State                                       : Enabled
LED Flash State                                 : Enabled
LED Flash Timer                                 : 0
MDNS Group Id                                   : 0
MDNS Rule Name                                  : 
PoE Pre-Standard Switch                         : Disabled
PoE Power Injector MAC Address                  : Disabled
Power Type/Mode                                 : PoE/Full Power
Number of Slots                                 : 3
AP Model                                        : AIR-AP4800-D-K9
IOS Version                                     : 17.3.1.9
Reset Button                                    : Disabled
AP Serial Number                                : FGL2102AZZZ
Management Frame Validation                     : Capable
Management Frame Protection                     : Capable
AP User Name                                    : admin
AP 802.1X User Mode                             : Global
AP 802.1X User Name                             : Not Configured
Cisco AP System Logging Host                    : 10.16.19.6
Cisco AP Secured Logging TLS mode               : Disabled
AP Up Time                                      : 3 days 9 hours 44 minutes 18 seconds 
AP CAPWAP Up Time                               : 3 days 9 hours 37 minutes 20 seconds 
Join Date and Time                              : 08/14/2020 19:48:09
Join Taken Time                                 : 6 minutes 57 seconds 
Join Priority                                   : 1
AP Link Latency                                 : Disable
AP Lag Configuration Status                     : Disabled
Lag Support for AP                              : Yes
Rogue Detection                                 : Enabled
Rogue Containment auto-rate                     : Disabled
Rogue Containment of standalone flexconnect APs : Disabled
Rogue Detection Report Interval                 : 10
Rogue AP minimum RSSI                           : -70
Rogue AP minimum transient time                 : 0
AP TCP MSS Adjust                               : Enabled
AP TCP MSS Size                                 : 1250
AP IPv6 TCP MSS Adjust                          : Enabled
AP IPv6 TCP MSS Size                            : 1250
Hyperlocation Admin Status                      : Disabled
Retransmit count                                : 5
Retransmit interval                             : 3
Fabric status                                   : Disabled
FIPS status                                     : Disabled
WLANCC status                                   : Disabled
USB Module Type                                 : USB Module
USB Module State                                : Enabled
USB Operational State                           : Disabled
USB Override                                    : Disabled
GAS rate limit Admin status                     : Disabled
WPA3 Capability                                 : Enabled
EWC-AP Capability                               : Disabled
AWIPS Capability                                : Enabled
Proxy Hostname                                  : Not Configured
Proxy Port                                      : Not Configured
Proxy NO_PROXY list                             : Not Configured
GRPC server status                              : Disabled
Unencrypted Data Keep Alive                     : Enabled
Local DHCP Server                               : Disabled
Traffic Distribution Statistics Capability      : Enabled
Dual DFS Statistics                             : Disabled

    '''}

    def test_show_ap_config_general_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowApConfigGeneral(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ap_config_general_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowApConfigGeneral(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
