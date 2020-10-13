import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


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
        print(show_wireless_fabric_summary_dict)
        return show_wireless_fabric_summary_dict


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
#  * 'show wireless client summary'
# =================================
class ShowWirelessClientSummary(ShowWirelessClientSummarySchema):
    """Parser for show wireless client summary"""

    cli_command = 'show wireless client summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

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

        for line in out.splitlines():
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

