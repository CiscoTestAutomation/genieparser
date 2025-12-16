"""show_uac.py

IOSXE parsers for the following show commands:

    * 'show uac uplink'
    * 'show uac uplink db'
    * 'show uac active-port'
    * 'show uac active-vlan'

"""

# Python
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowUACUplinkSchema(MetaParser):
    """Schema for:
    * 'show uac uplink'
    """

    schema = {
        "autoconfig_status": str,
        Optional("ipv4"): {
            "interface": str,
            "configured_interface": str,
            "config_in_progress": bool,
            Optional("ip_address"): str,
            Optional("type"): str,
            Optional("svi"): str,
            Optional("port_used"): str,
            Optional("gw_ip"): str,
            Optional("gw_mac"): str,
            Optional("score"): int,
            Optional('vrf'): str,
        },
        Optional("ipv6"): {
            "interface": str,
            "configured_interface": str,
            "config_in_progress": bool,
            Optional("ip_address"): str,
            Optional("type"): str,
            Optional("svi"): str,
            Optional("port_used"): str,
            Optional("gw_ip"): str,
            Optional("gw_mac"): str,
            Optional("score"): int,
            Optional('vrf'): str,
        },
        Optional("uplink_reachable"): str,
    }


class ShowUACUplink(ShowUACUplinkSchema):
    """Parser for show uac uplink"""

    cli_command = "show uac uplink"

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}

        # Regex patterns to match the output lines
        # Uplink Autoconfig: Enable
        p0 = re.compile(r"^Uplink Autoconfig: (\w+)$")
        
        # Configured IPv4 Uplink interface: Vlan 91
        p1 = re.compile(
            r"^Configured IPv4 Uplink interface: ([^(]+?)\s*(?=\(|$)"
        )
        # Configured IPv6 Uplink interface: Vlan 1 (Default)
        p2 = re.compile(
            r"^Configured IPv6 Uplink interface: ([^(]+?)\s*(?=\(|$)"
        )
        # Uplink IPv4 interface: Vlan 92
        p3 = re.compile(r"^Uplink IPv4 interface:\s*(.+)$")
        # Uplink IPv6 interface: Vlan 92
        p4 = re.compile(r"^Uplink IPv6 interface:\s*(.+)$")
        # IP Address: 92.92.92.181/255.255.255.0
        p5 = re.compile(r"^IP Address: ([^\s]+)$")
        # Type:       DHCP
        p6 = re.compile(r"^Type:\s+(\w+)$")
        # SVI:        Configured
        p7 = re.compile(r"^SVI:\s+(\w+)$")
        # Port Used:  GigabitEthernet1/0/2
        p8 = re.compile(r"^Port Used:\s+(.*)$")
        # GW IP:      92.92.92.1
        p9 = re.compile(r"^GW IP:\s+([^\s]+)$")
        # GW MAC:     6c6c.d3d0.5cc2
        p10 = re.compile(r"^GW MAC:\s+([^\s]+)$")
        # Score:      3
        p11 = re.compile(r"^Score:\s+(\d+)$")
        # Uplink Reachable: IPv4
        p12 = re.compile(r"^Uplink Reachable: (.+)$")

        #Uplink Allow-list enforce: IPv4:No  IPv6:No
        p13 = re.compile(r"Uplink Allow-list enforce: IPv4:(\w+)$  IPv6:(\w+)$")


        current_section = None

        for line in out.splitlines():
            line = line.strip()

            # Uplink Autoconfig: Enable
            m = p0.match(line)
            if m:
                parsed_dict["autoconfig_status"] = m.group(1)
                continue

            #Uplink Allow-list enforce: IPv4:No  IPv6:No
            m = p13.match(line)
            if m:
                parsed_dict['uplink_allow_list_enforce'] = {}
                parsed_dict['uplink_allow_list_enforce']['ipv4'] = m.group(1)
                parsed_dict['uplink_allow_list_enforce']['ipv6'] = m.group(2)
                continue


            # Configured IPv4 Uplink interface: Vlan 91
            m = p1.match(line)
            if m:
                current_section = "ipv4"
                parsed_dict[current_section] = {}
                parsed_dict[current_section]["configured_interface"] = (
                    Common.convert_intf_name(m.group(1).strip())
                )
                continue

            # Configured IPv6 Uplink interface: Vlan 1 (Default)
            m = p2.match(line)
            if m:
                current_section = "ipv6"
                parsed_dict[current_section] = {}
                parsed_dict[current_section]["configured_interface"] = (
                    Common.convert_intf_name(m.group(1).strip())
                )
                continue

            # Uplink IPv4 interface: Vlan 92
            m = p3.match(line)
            if m:
                interface_name = m.group(1).strip()
                if interface_name.endswith("*"):
                    interface_name = interface_name[:-1].strip()
                    parsed_dict[current_section]["config_in_progress"] = True
                else:
                    parsed_dict[current_section]["config_in_progress"] = False

                parsed_dict[current_section]["interface"] = (
                    Common.convert_intf_name(interface_name)
                )
                continue

            # Uplink IPv6 interface: Vlan 92
            m = p4.match(line)
            if m:
                interface_name = m.group(1).strip()
                if interface_name.endswith("*"):
                    interface_name = interface_name[:-1].strip()
                    parsed_dict[current_section]["config_in_progress"] = True
                else:
                    parsed_dict[current_section]["config_in_progress"] = False

                parsed_dict[current_section]["interface"] = (
                    Common.convert_intf_name(interface_name)
                )
                continue

            # IP Address: 92.92.92.181/255.255.255.0
            m = p5.match(line)
            if m:
                parsed_dict[current_section]["ip_address"] = m.group(1).strip()
                continue

            # Type:       DHCP
            m = p6.match(line)
            if m:
                parsed_dict[current_section]["type"] = m.group(1).strip()
                continue

            # SVI:        Configured
            m = p7.match(line)
            if m:
                parsed_dict[current_section]["svi"] = m.group(1).strip()
                continue

            # Port Used:  GigabitEthernet1/0/2
            m = p8.match(line)
            if m:
                parsed_dict[current_section]["port_used"] = m.group(1).strip()
                continue

            # GW IP:      92.92.92.1
            m = p9.match(line)
            if m:
                parsed_dict[current_section]["gw_ip"] = m.group(1).strip()
                continue

            # GW MAC:     6c6c.d3d0.5cc2
            m = p10.match(line)
            if m:
                parsed_dict[current_section]["gw_mac"] = m.group(1).strip()
                continue

            # Score:      3
            m = p11.match(line)
            if m:
                parsed_dict[current_section]["score"] = int(m.group(1).strip())
                continue

            # Uplink Reachable: IPv4
            m = p12.match(line)
            if m:
                parsed_dict["uplink_reachable"] = m.group(1).strip()
                continue

        return parsed_dict


class ShowUACUplinkDBSchema(MetaParser):
    """Schema for:
    * 'show uac uplink db'
    """

    schema = {
        "autoconfig_status": str,
        Optional("uplink_allow_list_enforce"): {
            "ipv4": bool,
            "ipv6": bool,
        },
        Optional("ipv4_uplink"): {
            "interface": str,
            "ping_pass_count": int,
            "gw_arp_pass_count": int,
        },
        Optional("ipv4_preferred_uplink"): {
            "interface": str,
            "ping_pass_count": int,
            "gw_arp_pass_count": int,
        },
        Optional("ipv6_uplink"): {
            "interface": str,
            "ping_pass_count": int,
            "gw_arp_pass_count": int,
        },
        Optional("ipv6_preferred_uplink"): {
            "interface": str,
            "ping_pass_count": int,
            "gw_arp_pass_count": int,
        },
        Optional("interfaces"): {
            Optional("ipv4"): {
                Any(): {  # Interface name
                    "score": int,
                    "state": int,
                    "ip_address": str,
                    "subnet_mask": str,
                    "arp_fail": int,
                    "ping_fail": int,
                    "gw_probe": str,
                    "ping": str,
                    "rescore": int,
                    Optional("allowed"): int,
                },
            },
            Optional("ipv6"): {
                Any(): {  # Interface name
                    "score": int,
                    "state": int,
                    "ipv6_address": str,
                    "prefix": str,
                    "arp_fail": int,
                    "ping_fail": int,
                    "gw_probe": str,
                    "ping": str,
                    "rescore": int,
                    Optional("allowed"): int,
                },
            },
        },
    }


class ShowUACUplinkDB(ShowUACUplinkDBSchema):
    """Parser for show uac uplink db"""

    cli_command = "show uac uplink db"

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}

        # Regex patterns to match the output lines
        # Uplink Autoconfig: Enable
        p0 = re.compile(r"^Uplink Autoconfig: (\w+)$")
        # Uplink Allow-list enforce: IPv4:No  IPv6:No
        p1 = re.compile(r"^Uplink Allow-list enforce: IPv4:(?P<ipv4>\w+)\s+IPv6:(?P<ipv6>\w+)$")
        # IPV4 Uplink: Vlan 91 (case insensitive)
        p2 = re.compile(r"^ipv4 uplink: (.+)$", re.IGNORECASE)
        # IPv4 Preferred Uplink: Vlan 1 (case insensitive)
        p3 = re.compile(r"^ipv4 preferred uplink: (.+)$", re.IGNORECASE)
        # IPV6 Uplink: None (case insensitive)
        p4 = re.compile(r"^ipv6 uplink: (.+)$", re.IGNORECASE)
        # IPv6 Preferred Uplink: Vlan 1 (case insensitive)
        p5 = re.compile(r"^ipv6 preferred uplink: (.+)$", re.IGNORECASE)
        # Ping Pass Count: 69
        p6 = re.compile(r"^Ping Pass Count:\s*(\d+)$")
        # GW ARP Pass Count:3
        p7 = re.compile(r"^GW ARP Pass Count:\s*(\d+)$")
        # IfName      Score  State  IPAddress
        p8 = re.compile(
            r"^IfName\s+Score\s+State\s+IPAddress"
        )
        # IfName      Score  State  IPv6Address
        p9 = re.compile(
            r"^IfName\s+Score\s+State\s+IPv6Address"
        )
        # Vlan91 3 11 91.91.91.176 255.255.255.0 0 0 FCCF0DC 10347E28 0
        p10 = re.compile(
            r"^(\S+)\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\d+)$"
        )
        p11 = re.compile(
            r"^(\S+)\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\d+)$"
        )

        current_section = None
        ipv4_interfaces = {}
        ipv6_interfaces = {}

        # Process each line
        for line in out.splitlines():
            line = line.strip()

            # Uplink Autoconfig: Enable
            m = p0.match(line)
            if m:
                parsed_dict["autoconfig_status"] = m.group(1)
                continue

            # Uplink Allow-list enforce: IPv4:No  IPv6:No
            m = p1.match(line)
            if m:
                parsed_dict["uplink_allow_list_enforce"] = {
                    "ipv4": True if m.group('ipv4') == 'Yes' else False,
                    "ipv6": True if m.group('ipv6') == 'Yes' else False,
                }
                continue

            # IPv4 Preferred Uplink: Vlan 1 (check this first)
            m = p3.match(line)
            if m:
                parsed_dict["ipv4_preferred_uplink"] = {
                    "interface": Common.convert_intf_name(m.group(1)),
                    "ping_pass_count": 0,
                    "gw_arp_pass_count": 0,
                }
                current_section = "ipv4_preferred_uplink"
                continue

            # IPV4 Uplink: Vlan 91 (check after preferred)
            m = p2.match(line)
            if m and "Preferred" not in line:
                parsed_dict["ipv4_uplink"] = {
                    "interface": Common.convert_intf_name(m.group(1)),
                    "ping_pass_count": 0,
                    "gw_arp_pass_count": 0,
                }
                current_section = "ipv4_uplink"
                continue

            # IPv6 Preferred Uplink: Vlan 1 (check this first)
            m = p5.match(line)
            if m:
                parsed_dict["ipv6_preferred_uplink"] = {
                    "interface": Common.convert_intf_name(m.group(1)),
                    "ping_pass_count": 0,
                    "gw_arp_pass_count": 0,
                }
                current_section = "ipv6_preferred_uplink"
                continue

            # IPV6 Uplink: None (check after preferred)
            m = p4.match(line)
            if m and "Preferred" not in line:
                parsed_dict["ipv6_uplink"] = {
                    "interface": Common.convert_intf_name(m.group(1)),
                    "ping_pass_count": 0,
                    "gw_arp_pass_count": 0,
                }
                current_section = "ipv6_uplink"
                continue

            # Ping Pass Count: 69
            m = p6.match(line)
            if m:
                if current_section in ["ipv4_uplink", "ipv6_uplink", "ipv4_preferred_uplink", "ipv6_preferred_uplink"]:
                    parsed_dict[current_section]["ping_pass_count"] = int(
                        m.group(1)
                    )
                continue

            # GW ARP Pass Count:3
            m = p7.match(line)
            if m:
                if current_section in ["ipv4_uplink", "ipv6_uplink", "ipv4_preferred_uplink", "ipv6_preferred_uplink"]:
                    parsed_dict[current_section]["gw_arp_pass_count"] = int(
                        m.group(1)
                    )
                continue

            # IfName      Score  State  IPAddress
            m = p8.match(line)
            if m:
                current_section = "ipv4_interfaces"
                continue

            # IfName      Score  State  IPv6Address
            m = p9.match(line)
            if m:
                current_section = "ipv6_interfaces"
                continue

            if current_section == "ipv4_interfaces" and line.strip():
                # Vlan91 3 11 91.91.91.176 255.255.255.0 0 0 FCCF0DC 10347E28 0
                m = p10.match(line) or p11.match(line)
                if m:
                    groups = m.groups()
                    interface_name = Common.convert_intf_name(groups[0])
                    ipv4_interfaces[interface_name] = {
                        "score": int(groups[1]),
                        "state": int(groups[2]),
                        "ip_address": groups[3],
                        "subnet_mask": groups[4],
                        "arp_fail": int(groups[5]),
                        "ping_fail": int(groups[6]),
                        "gw_probe": groups[7],
                        "ping": groups[8],
                        "rescore": int(groups[9]),
                    }
                    if len(groups) > 10:
                        ipv4_interfaces[interface_name]['allowed'] = int(groups[10])
                    continue

            # IPv6 interface entries
            if current_section == "ipv6_interfaces" and line.strip():
                # Vlan91 3 11 91.91.91.176 255.255.255.0 0 0 FCCF0DC 10347E28 0
                m = p10.match(line) or p11.match(line)
                if m:
                    groups = m.groups()
                    interface_name = Common.convert_intf_name(groups[0])
                    ipv6_interfaces[interface_name] = {
                        "score": int(groups[1]),
                        "state": int(groups[2]),
                        "ipv6_address": groups[3],
                        "prefix": groups[4],
                        "arp_fail": int(groups[5]),
                        "ping_fail": int(groups[6]),
                        "gw_probe": groups[7],
                        "ping": groups[8],
                        "rescore": int(groups[9]),
                    }
                    if len(groups) > 10:
                        ipv6_interfaces[interface_name]['allowed'] = int(groups[10])
                    continue

        # Add interfaces to parsed_dict if they exist
        if ipv4_interfaces or ipv6_interfaces:
            parsed_dict["interfaces"] = {}
            if ipv4_interfaces:
                parsed_dict["interfaces"]["ipv4"] = ipv4_interfaces
            if ipv6_interfaces:
                parsed_dict["interfaces"]["ipv6"] = ipv6_interfaces

        return parsed_dict

class ShowUACActivePortSchema(MetaParser):
    """Schema for:
    * 'show uac active-port'
    """

    schema = {
        "autoconfig_status": str,
        Optional("interfaces"): {
            Any(): {  # Interface name
                "uid": int,
                "state": int,
                "l2": str,
                "created": str,
                "svi": str,
                "ip_assign": tuple,
                "ip_state": tuple,
                "route": tuple,
                "static": tuple,
                "score": tuple,
                Optional("allowed"): tuple,
            }
        },
    }


class ShowUACActivePort(ShowUACActivePortSchema):
    """Parser for show uac active-port"""

    cli_command = "show uac active-port"

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}
        interfaces = {}

        # Regex patterns to match the output lines
        # Uplink Autoconfig: Enable
        p0 = re.compile(r"^Uplink Autoconfig: (\w+)$")
        # Vlan1          1      3  Up   No       Yes  ( 0   0)  ( 0  0)  (0 0)  (0  0)  (0 0)
        p1 = re.compile(
            r"^(\S+)\s+(\d+)\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+\(\s*(\d+)\s+(\d+)\)\s+\(\s*(\d+)\s+(\d+)\)\s+\((\d+)\s+(\d+)\)\s+\((\d+)\s+(\d+)\)\s+\((\d+)\s+(\d+)\)(((\s+))(\((\d+)\s+(\d+)\)))?$"
        )

        for line in out.splitlines():
            line = line.strip()

            # Uplink Autoconfig: Enable
            m = p0.match(line)
            if m:
                parsed_dict["autoconfig_status"] = m.group(1)
                continue

            # Vlan1          1      3  Up   No       Yes  ( 0   0)  ( 0  0)  (0 0)  (0  0)  (0 0)
            m = p1.match(line)
            if m:
                interface_name = Common.convert_intf_name(m.group(1))
                uid = int(m.group(2))
                state = int(m.group(3))
                l2 = m.group(4)
                created = m.group(5)
                svi = m.group(6)

                ip_assign = (int(m.group(7)), int(m.group(8)))
                ip_state = (int(m.group(9)), int(m.group(10)))
                route = (int(m.group(11)), int(m.group(12)))
                static = (int(m.group(13)), int(m.group(14)))
                score = (int(m.group(15)), int(m.group(16)))
                if m.group(21) and m.group(22):
                    allowed = (int(m.group(21)), int(m.group(22)))
                    interfaces[interface_name] = {
                        "uid": uid,
                        "state": state,
                        "l2": l2,
                        "created": created,
                        "svi": svi,
                        "ip_assign": ip_assign,
                        "ip_state": ip_state,
                        "route": route,
                        "static": static,
                        "score": score,
                        "allowed": allowed,
                    }
                else:

                    interfaces[interface_name] = {
                        "uid": uid,
                        "state": state,
                        "l2": l2,
                        "created": created,
                        "svi": svi,
                        "ip_assign": ip_assign,
                        "ip_state": ip_state,
                        "route": route,
                        "static": static,
                        "score": score,
                    }
                continue

        if interfaces:
            parsed_dict["interfaces"] = interfaces

        return parsed_dict


class ShowUACActiveVlanSchema(MetaParser):
    """Schema for:
    * 'show uac active-vlan'
    """

    schema = {
        "autoconfig_status": str,
        Optional("vlans"): {
            Any(): {  # Vlan ID
                "state": int,
                "l2": str,
                "created": str,
                "svi": str,
                "ip_assign": tuple,
                "ip_state": tuple,
                "route": tuple,
                "static": tuple,
                "score": tuple,
                Optional("allowed"): tuple,
            }
        },
    }


class ShowUACActiveVlan(ShowUACActiveVlanSchema):
    """Parser for show uac active-vlan"""

    cli_command = "show uac active-vlan"

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}
        vlans = {}

        # Regex patterns to match the output lines
        # Uplink Autoconfig: Enable
        p0 = re.compile(r"^Uplink Autoconfig: (\w+)$")
        #      1      3  Up   No       Yes  ( 0   0)  ( 0  0)  (0 0)  (0  0)  (0 0)
        p1 = re.compile(
            r"^(\d+)\s+\s+(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+\(\s*(\d+)\s+(\d+)\)\s+\(\s*(\d+)\s+(\d+)\)\s+\((\d+)\s+(\d+)\)\s+\((\d+)\s+(\d+)\)\s+\((\d+)\s+(\d+)\)(((\s+))(\((\d+)\s+(\d+)\)))?$"
        )

        for line in out.splitlines():
            line = line.strip()

            # Uplink Autoconfig: Enable
            m = p0.match(line)
            if m:
                parsed_dict["autoconfig_status"] = m.group(1)
                continue

            #      1      3  Up   No       Yes  ( 0   0)  ( 0  0)  (0 0)  (0  0)  (0 0)
            m = p1.match(line)
            if m:
                interface_name = Common.convert_intf_name(m.group(1))
                state = int(m.group(2))
                l2 = m.group(3)
                created = m.group(4)
                svi = m.group(5)

                ip_assign = (int(m.group(6)), int(m.group(7)))
                ip_state = (int(m.group(8)), int(m.group(9)))
                route = (int(m.group(10)), int(m.group(11)))
                static = (int(m.group(12)), int(m.group(13)))
                score = (int(m.group(14)), int(m.group(15)))
                if m.group(20) and m.group(21):
                    allowed = (int(m.group(20)), int(m.group(21)))
                    vlans[interface_name] = {
                        "state": state,
                        "l2": l2,
                        "created": created,
                        "svi": svi,
                        "ip_assign": ip_assign,
                        "ip_state": ip_state,
                        "route": route,
                        "static": static,
                        "score": score,
                        "allowed": allowed,
                    }
                else:
                    # Add the interface data to the parsed_dict
                    vlans[interface_name] = {
                        "state": state,
                        "l2": l2,
                        "created": created,
                        "svi": svi,
                        "ip_assign": ip_assign,
                        "ip_state": ip_state,
                        "route": route,
                        "static": static,
                        "score": score,
                    }
                continue

        if vlans:
            parsed_dict["vlans"] = vlans

        return parsed_dict
