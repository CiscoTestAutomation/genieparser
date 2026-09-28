"""show_uac.py

Revision 1 of IOSXE parsers for the following show commands:

    * 'show uac uplink'
    * 'show uac uplink db'
    * 'show uac active-port'
    * 'show uac active-vlan'

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

from genie.libs.parser.utils.common import Common


class ShowUACUplinkSchema(MetaParser):
    """Schema for:
    * 'show uac uplink'
    """

    schema = {
        "autoconfig_status": str,
        Optional("ipv4"): {
            "interface": str,
            Optional("configured_interface"): str,
            "config_in_progress": bool,
            Optional("ip_address"): str,
            Optional("type"): str,
            Optional("svi"): str,
            Optional("port_used"): str,
            Optional("gw_ip"): str,
            Optional("gw_mac"): str,
            Optional("score"): int,
        },
        Optional("ipv6"): {
            "interface": str,
            Optional("configured_interface"): str,
            "config_in_progress": bool,
            Optional("ip_address"): str,
            Optional("type"): str,
            Optional("svi"): str,
            Optional("port_used"): str,
            Optional("gw_ip"): str,
            Optional("gw_mac"): str,
            Optional("score"): int,
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
        p1 = re.compile(r"^Configured IPv4 Uplink interface: ([^(]+?)\s*(?=\(|$)")
        # Configured IPv6 Uplink interface: Vlan 1 (Default)
        p2 = re.compile(r"^Configured IPv6 Uplink interface: ([^(]+?)\s*(?=\(|$)")
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

        current_section = None

        for line in out.splitlines():
            line = line.strip()

            # Uplink Autoconfig: Enable
            m = p0.match(line)
            if m:
                parsed_dict["autoconfig_status"] = m.group(1)
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
                current_section = "ipv4"
                parsed_dict.setdefault(current_section, {})
                interface_name = m.group(1).strip()
                if interface_name.endswith("*"):
                    interface_name = interface_name[:-1].strip()
                    parsed_dict[current_section]["config_in_progress"] = True
                else:
                    parsed_dict[current_section]["config_in_progress"] = False

                parsed_dict[current_section]["interface"] = Common.convert_intf_name(
                    interface_name
                )
                continue

            # Uplink IPv6 interface: Vlan 92
            m = p4.match(line)
            if m:
                current_section = "ipv6"
                parsed_dict.setdefault(current_section, {})
                interface_name = m.group(1).strip()
                if interface_name.endswith("*"):
                    interface_name = interface_name[:-1].strip()
                    parsed_dict[current_section]["config_in_progress"] = True
                else:
                    parsed_dict[current_section]["config_in_progress"] = False

                parsed_dict[current_section]["interface"] = Common.convert_intf_name(
                    interface_name
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
            Optional("ping_pass_count"): int,
            Optional("gw_arp_pass_count"): int,
        },
        Optional("ipv4_preferred_uplink"): {
            "interface": str,
            Optional("ping_pass_count"): int,
            Optional("gw_arp_pass_count"): int,
        },
        Optional("ipv6_uplink"): {
            "interface": str,
            Optional("ping_pass_count"): int,
            Optional("gw_arp_pass_count"): int,
        },
        Optional("ipv6_preferred_uplink"): {
            "interface": str,
            Optional("ping_pass_count"): int,
            Optional("gw_arp_pass_count"): int,
        },
        Optional("interfaces"): {
            Optional("ipv4"): {
                Any(): {
                    "score": int,
                    "state": str,
                    "ip_address": str,
                    "subnet_mask": str,
                    "gateway": str,
                    "gw_probe": str,
                    "gw_probe_fail": int,
                    Optional("allowed"): int,
                },
            },
            Optional("ipv6"): {
                Any(): {
                    "score": int,
                    "state": str,
                    "ipv6_address": str,
                    "prefix": str,
                    "gateway": str,
                    "gw_probe": str,
                    "gw_probe_fail": int,
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

        # Uplink Autoconfig: Enable
        p0 = re.compile(r"^Uplink Autoconfig: (\w+)$")
        # Uplink Allow-list enforce: IPv4:No  IPv6:No
        p1 = re.compile(
            r"^Uplink Allow-list enforce: IPv4:(?P<ipv4>\w+)\s+IPv6:(?P<ipv6>\w+)$"
        )
        # ipv4 uplink : Vlan 91
        p2 = re.compile(r"^ipv4 uplink\s*:\s*(.+)$", re.IGNORECASE)
        # ipv4 preferred uplink : Vlan 1
        p3 = re.compile(r"^ipv4 preferred uplink\s*:\s*(.+)$", re.IGNORECASE)
        # ipv6 uplink : None
        p4 = re.compile(r"^ipv6 uplink\s*:\s*(.+)$", re.IGNORECASE)
        # ipv6 preferred uplink : Vlan 1
        p5 = re.compile(r"^ipv6 preferred uplink\s*:\s*(.+)$", re.IGNORECASE)
        # Ping Pass Count: 69
        p6 = re.compile(r"^Ping Pass Count:\s*(\d+)$", re.IGNORECASE)
        # GW ARP Pass Count:3
        p7 = re.compile(r"^GW ARP Pass Count:\s*(\d+)$", re.IGNORECASE)
        # IfName      Score  State  IPAddress Subnet/Prefix Gateway GWProbe GWProbeFail Allowed
        p8 = re.compile(
            r"^IfName\s+Score\s+State\s+IPAddress\s+Subnet/Prefix\s+Gateway\s+GWProbe\s+GWProbeFail\s+Allowed",
            re.IGNORECASE,
        )
        # IfName      Score  State  IPv6Address Prefix Gateway GWProbe GWProbeFail Allowed
        p9 = re.compile(
            r"^IfName\s+Score\s+State\s+IPv6Address\s+Prefix\s+Gateway\s+GWProbe\s+GWProbeFail\s+Allowed",
            re.IGNORECASE,
        )

        current_section = None
        ipv4_interfaces = {}
        ipv6_interfaces = {}

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # Uplink Autoconfig: Enable
            m = p0.match(line)
            if m:
                parsed_dict["autoconfig_status"] = m.group(1)
                continue

            # Uplink Allow-list enforce: IPv4:No  IPv6:No
            m = p1.match(line)
            if m:
                parsed_dict["uplink_allow_list_enforce"] = {
                    "ipv4": True if m.group("ipv4") == "Yes" else False,
                    "ipv6": True if m.group("ipv6") == "Yes" else False,
                }
                continue

            # ipv4 preferred uplink : Vlan 1
            m = p3.match(line)
            if m:
                parsed_dict["ipv4_preferred_uplink"] = {
                    "interface": Common.convert_intf_name(m.group(1).strip()),
                }
                current_section = "ipv4_preferred_uplink"
                continue

            # ipv4 uplink : Vlan 91
            m = p2.match(line)
            if m and "Preferred" not in line:
                parsed_dict["ipv4_uplink"] = {
                    "interface": Common.convert_intf_name(m.group(1).strip()),
                }
                current_section = "ipv4_uplink"
                continue

            # ipv6 preferred uplink : Vlan 1
            m = p5.match(line)
            if m:
                parsed_dict["ipv6_preferred_uplink"] = {
                    "interface": Common.convert_intf_name(m.group(1).strip()),
                }
                current_section = "ipv6_preferred_uplink"
                continue

            # ipv6 uplink : None
            m = p4.match(line)
            if m and "Preferred" not in line:
                parsed_dict["ipv6_uplink"] = {
                    "interface": Common.convert_intf_name(m.group(1).strip()),
                }
                current_section = "ipv6_uplink"
                continue

            # Ping Pass Count: 69
            m = p6.match(line)
            if m and current_section:
                parsed_dict[current_section]["ping_pass_count"] = int(m.group(1))
                continue

            # GW ARP Pass Count:3
            m = p7.match(line)
            if m and current_section:
                parsed_dict[current_section]["gw_arp_pass_count"] = int(m.group(1))
                continue

            # IfName      Score  State  IPAddress Subnet/Prefix Gateway GWProbe GWProbeFail Allowed
            m = p8.match(line)
            if m:
                current_section = "ipv4_interfaces"
                continue

            # IfName      Score  State  IPv6Address Prefix Gateway GWProbe GWProbeFail Allowed
            m = p9.match(line)
            if m:
                current_section = "ipv6_interfaces"
                continue

            if current_section == "ipv4_interfaces":
                parts = line.split()
                if len(parts) >= 9:
                    interface_name = Common.convert_intf_name(parts[0])
                    ipv4_interfaces[interface_name] = {
                        "score": int(parts[1]),
                        "state": parts[2],
                        "ip_address": parts[3],
                        "subnet_mask": parts[4],
                        "gateway": parts[5],
                        "gw_probe": parts[6],
                        "gw_probe_fail": int(parts[7]),
                    }
                    if len(parts) >= 9:
                        ipv4_interfaces[interface_name]["allowed"] = int(parts[8])
                    continue

            if current_section == "ipv6_interfaces":
                parts = line.split()
                if len(parts) >= 9:
                    interface_name = Common.convert_intf_name(parts[0])
                    ipv6_interfaces[interface_name] = {
                        "score": int(parts[1]),
                        "state": parts[2],
                        "ipv6_address": parts[3],
                        "prefix": parts[4],
                        "gateway": parts[5],
                        "gw_probe": parts[6],
                        "gw_probe_fail": int(parts[7]),
                    }
                    if len(parts) >= 9:
                        ipv6_interfaces[interface_name]["allowed"] = int(parts[8])
                    continue

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
            Any(): {
                "uid": int,
                "state": str,
                "l2": str,
                "created": str,
                "initialized": str,
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

        # Uplink Autoconfig: Enable
        p0 = re.compile(r"^Uplink Autoconfig: (\w+)$")
        # Vlan1       1      DONE       Up   No       Yes          (1,0)     (11,0)   (1,0)  (0,0)   (8,0)  (1,1)
        p1 = re.compile(
            r"^(?P<intf>\S+)\s+(?P<uid>\d+)\s+(?P<state>\S+)\s+(?P<l2>\S+)\s+"
            r"(?P<created>\S+)\s+(?P<initialized>\S+)\s+"
            r"\(\s*(?P<ip_assign1>\d+)\s*,\s*(?P<ip_assign2>\d+)\s*\)\s+"
            r"\(\s*(?P<ip_state1>\d+)\s*,\s*(?P<ip_state2>\d+)\s*\)\s+"
            r"\(\s*(?P<route1>\d+)\s*,\s*(?P<route2>\d+)\s*\)\s+"
            r"\(\s*(?P<static1>\d+)\s*,\s*(?P<static2>\d+)\s*\)\s+"
            r"\(\s*(?P<score1>\d+)\s*,\s*(?P<score2>\d+)\s*\)\s+"
            r"\(\s*(?P<allowed1>\d+)\s*,\s*(?P<allowed2>\d+)\s*\)$"
        )

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # Uplink Autoconfig: Enable
            m = p0.match(line)
            if m:
                parsed_dict["autoconfig_status"] = m.group(1)
                continue

            # Vlan1       1      DONE       Up   No       Yes          (1,0)     (11,0)   (1,0)  (0,0)   (8,0)  (1,1)
            m = p1.match(line)
            if m:
                interface_name = Common.convert_intf_name(m.group("intf"))
                interfaces[interface_name] = {
                    "uid": int(m.group("uid")),
                    "state": m.group("state"),
                    "l2": m.group("l2"),
                    "created": m.group("created"),
                    "initialized": m.group("initialized"),
                    "ip_assign": (
                        int(m.group("ip_assign1")),
                        int(m.group("ip_assign2")),
                    ),
                    "ip_state": (
                        int(m.group("ip_state1")),
                        int(m.group("ip_state2")),
                    ),
                    "route": (
                        int(m.group("route1")),
                        int(m.group("route2")),
                    ),
                    "static": (
                        int(m.group("static1")),
                        int(m.group("static2")),
                    ),
                    "score": (
                        int(m.group("score1")),
                        int(m.group("score2")),
                    ),
                    "allowed": (
                        int(m.group("allowed1")),
                        int(m.group("allowed2")),
                    ),
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
            Any(): {
                "state": str,
                "l2": str,
                "created": str,
                "initialized": str,
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

        # Uplink Autoconfig: Enable
        p0 = re.compile(r"^Uplink Autoconfig: (\w+)$")
        # 1        DONE       Up   No        Yes          (1,0)     (11,0)   (1,0)  (0,0)   (8,0)  (1,1)
        p1 = re.compile(
            r"^(?P<vlan>\S+)\s+(?P<state>\S+)\s+(?P<l2>\S+)\s+(?P<created>\S+)\s+"
            r"(?P<initialized>\S+)\s+\(\s*(?P<ip_assign1>\d+)\s*,\s*(?P<ip_assign2>\d+)\s*\)\s+"
            r"\(\s*(?P<ip_state1>\d+)\s*,\s*(?P<ip_state2>\d+)\s*\)\s+"
            r"\(\s*(?P<route1>\d+)\s*,\s*(?P<route2>\d+)\s*\)\s+"
            r"\(\s*(?P<static1>\d+)\s*,\s*(?P<static2>\d+)\s*\)\s+"
            r"\(\s*(?P<score1>\d+)\s*,\s*(?P<score2>\d+)\s*\)\s+"
            r"\(\s*(?P<allowed1>\d+)\s*,\s*(?P<allowed2>\d+)\s*\)$"
        )

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # Uplink Autoconfig: Enable
            m = p0.match(line)
            if m:
                parsed_dict["autoconfig_status"] = m.group(1)
                continue

            # 1        DONE       Up   No        Yes          (1,0)     (11,0)   (1,0)  (0,0)   (8,0)  (1,1)
            m = p1.match(line)
            if m:
                raw_vlan = m.group("vlan")
                # The CLI can emit bare vlan IDs (e.g. "1") – normalize to the
                # interface-style label to match expectations (e.g. "Vlan1").
                if not raw_vlan.lower().startswith("vlan"):
                    raw_vlan = f"Vlan{raw_vlan}"
                vlan_name = Common.convert_intf_name(raw_vlan)
                vlans[vlan_name] = {
                    "state": m.group("state"),
                    "l2": m.group("l2"),
                    "created": m.group("created"),
                    "initialized": m.group("initialized"),
                    "ip_assign": (
                        int(m.group("ip_assign1")),
                        int(m.group("ip_assign2")),
                    ),
                    "ip_state": (
                        int(m.group("ip_state1")),
                        int(m.group("ip_state2")),
                    ),
                    "route": (
                        int(m.group("route1")),
                        int(m.group("route2")),
                    ),
                    "static": (
                        int(m.group("static1")),
                        int(m.group("static2")),
                    ),
                    "score": (
                        int(m.group("score1")),
                        int(m.group("score2")),
                    ),
                    "allowed": (
                        int(m.group("allowed1")),
                        int(m.group("allowed2")),
                    ),
                }
                continue

        if vlans:
            parsed_dict["vlans"] = vlans

        return parsed_dict
