"""show_platform_hardware_fed.py

    * show platform hardware fed switch active npu slot 1 port 41 link_status
    * show platform hardware fed active npu slot 1 port 2 link_status
    * show platform hardware fed switch active qos queue config interface AppGigabitEthernet 2/0/2
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, ListOf
from genie.libs.parser.utils.common import Common


def _normalize_key(key):
    """Convert CLI labels to parser keys."""
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", key.lower())).strip("_")


def _parse_braced_list(value, convert_int=False):
    """Parse values such as {F,F,F} or {0}."""
    values = []
    for item in value.strip("{}").split(","):
        item = item.strip()
        if not item:
            continue
        if convert_int and item.isdigit():
            values.append(int(item))
        else:
            values.append(item)
    return values


def _parse_csv_list(value):
    """Parse comma-separated CLI values into a list."""
    values = []
    for item in value.split(","):
        item = item.strip()
        if item:
            values.append(item)
    return values


class ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatusSchema(MetaParser):
    """Schema for show platform hardware fed switch active npu slot 1 port 41 link_status"""

    schema = {
        "mac_port_details": {
            "link_state": int,
            "pcs_status": int,
            "high_ber": int,
            Optional("am_lock"): ListOf(str),
            Optional("mac_pcs_lanes"): ListOf(int),
            Optional("get_link_management_enabled"): str,
            Optional("get_serdes_continuous_tuning_enabled"): str,
            Optional("get_tune_status"): str,
            Optional("get_an_enabled"): str,
            Optional("get_loopback_mode"): str,
            Optional("get_state"): str,
            Optional("get_speed"): str,
            Optional("state_transitions"): ListOf(
                {
                    "state": str,
                    "count": int,
                }
            ),
        },
        Optional("mib_counters"): {
            Any(): int,
        },
        Optional("port"): int,
        Optional("slot"): int,
        Optional("cmd"): str,
        Optional("rc"): str,
        Optional("reason"): str,
    }


class ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatus(
    ShowPlatformHardwareFedSwitchActiveNpuSlotPortLinkstatusSchema
):
    """Parser for show platform hardware fed switch active npu slot 1 port 41 link_status

    Supports standalone and SVL command forms.
    """

    cli_command = "show platform hardware fed switch {mode} npu slot 1 port {port_num} link_status"

    def cli(self, port_num, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode, port_num=port_num))

        ret_dict = {}
        current_section = None

        # MAC PORT DETAILS
        p1 = re.compile(r"^MAC +PORT +DETAILS$")

        # link_state: 0 pcs_status: 0  high_ber: 0
        p2 = re.compile(
            r"^link_state: +(?P<link_state>\d+) +"
            r"pcs_status: +(?P<pcs_status>\d+) +"
            r"high_ber: +(?P<high_ber>\d+)$"
        )

        # am_lock       = {F,F,F,F}
        # mac_pcs_lanes = {0}
        p3 = re.compile(r"^(?P<key>am_lock|mac_pcs_lanes) *= *(?P<value>\{.*\})$")

        # get_state = TUNING
        p4 = re.compile(r"^(?P<key>get_[\w_]+) *= *(?P<value>.+)$")

        # INACTIVE(2), garbage(4), ACTIVE(8),
        p5 = re.compile(r"(?P<state>[A-Za-z_]+)\((?P<count>\d+)\)")

        # MIB counters
        p6 = re.compile(r"^MIB +counters$")

        # TX legal frames counter : 1
        p7 = re.compile(r"^(?P<key>.+) +: +(?P<value>\d+)$")

        # Port = 41 Slot = 1 cmd = (port_diag unit 0 port 40 slot 0) rc = 0x0 reason = success
        p8 = re.compile(
            r"^Port *= *(?P<port>\d+)"
            r"(?: +Slot *= *(?P<slot>\d+))?"
            r" +cmd *= *\((?P<cmd>[^)]+)\)"
            r" +rc *= *(?P<rc>\S+)"
            r" +(?:rsn|reason) *= *(?P<reason>\S+)$"
        )

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # MAC PORT DETAILS
            m = p1.match(line)
            if m:
                current_section = "mac_port_details"
                ret_dict.setdefault(current_section, {})
                continue

            # link_state: 0 pcs_status: 0  high_ber: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                mac_dict = ret_dict.setdefault("mac_port_details", {})
                mac_dict["link_state"] = int(group["link_state"])
                mac_dict["pcs_status"] = int(group["pcs_status"])
                mac_dict["high_ber"] = int(group["high_ber"])
                continue

            # am_lock       = {F,F,F,F}
            # mac_pcs_lanes = {0}
            m = p3.match(line)
            if m:
                group = m.groupdict()
                mac_dict = ret_dict.setdefault("mac_port_details", {})
                key = group["key"]
                mac_dict[key] = _parse_braced_list(
                    group["value"], convert_int=(key == "mac_pcs_lanes")
                )
                continue

            # get_state = TUNING
            m = p4.match(line)
            if m:
                group = m.groupdict()
                mac_dict = ret_dict.setdefault("mac_port_details", {})
                mac_dict[group["key"]] = group["value"].strip()
                continue

            # INACTIVE(2), garbage(4), ACTIVE(8),
            state_matches = p5.findall(line)
            if state_matches:
                mac_dict = ret_dict.setdefault("mac_port_details", {})
                mac_dict["state_transitions"] = [
                    {"state": state, "count": int(count)}
                    for state, count in state_matches
                ]
                continue

            # MIB counters
            m = p6.match(line)
            if m:
                current_section = "mib_counters"
                ret_dict.setdefault(current_section, {})
                continue

            # TX legal frames counter : 1
            m = p7.match(line)
            if m and current_section == "mib_counters":
                group = m.groupdict()
                mib_dict = ret_dict.setdefault("mib_counters", {})
                mib_dict[_normalize_key(group["key"].strip())] = int(group["value"])
                continue

            # Port = 41 Slot = 1 cmd = (port_diag unit 0 port 40 slot 0) rc = 0x0 reason = success
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict["port"] = int(group["port"])
                if group.get("slot"):
                    ret_dict["slot"] = int(group["slot"])
                ret_dict["cmd"] = group["cmd"]
                ret_dict["rc"] = group["rc"]
                ret_dict["reason"] = group["reason"]
                current_section = None
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchQosQueueConfigSchema(MetaParser):
    """Schema for show platform hardware fed switch active qos queue config interface"""

    schema = {
        "interface": {
            Any(): {
                "interface_id": str,
                "voq_id": str,
                "voq_oid": str,
                "voq_set_size": str,
                "base_voq_id": str,
                "base_vsc_ids": ListOf(str),
                "voq_state": str,
                "voq_flush": str,
                "is_empty": str,
                "profile_oid": {
                    Any(): {
                        "profile_id": str,
                        "device_id": str,
                        "cgm_type": str,
                        "profile_reference_count": str,
                        "is_reserved": str,
                        "for_speeds": str,
                        "associated_voq_offsets": ListOf(str),
                        "hbm_enabled": str,
                        Optional("hbm_block_size"): str,
                        Optional("q_block_size"): str,
                        Optional("red_enabled"): str,
                        Optional("fcn_enabled"): str,
                        Optional("queue_user_config"): {
                            Optional("q_limit_bytes"): str,
                            Optional("q_limit_hbm_blocks"): str,
                            Optional("red_ema_coefficient"): str,
                            Optional("red_flag"): {
                                Any(): {
                                    Optional("minimum"): str,
                                    Optional("maximum"): str,
                                    Optional("minimum_hbm_blocks"): str,
                                    Optional("maximum_hbm_blocks"): str,
                                    Optional("maximum_probability"): str,
                                }
                            },
                        },
                        Optional("queue_hw_values"): {
                            Optional("red_ema_coefficient"): str,
                            Optional("red_action"): str,
                            Optional("red_drop_thresholds"): ListOf(str),
                            Optional("red_flag"): {
                                Any(): {
                                    Optional("red_drop_probabilities"): ListOf(str),
                                }
                            },
                            Optional("hbm_free_thresholds"): ListOf(str),
                            Optional("hbm_voq_age_thresholds"): ListOf(str),
                            Optional("hbm_voq_thresholds"): ListOf(str),
                        },
                    }
                },
            }
        }
    }


class ShowPlatformHardwareFedSwitchQosQueueConfig(
    ShowPlatformHardwareFedSwitchQosQueueConfigSchema
):
    """Parser for show platform hardware fed switch active qos queue config interface"""

    cli_command = "show platform hardware fed switch {mode} qos queue config interface {interface}"

    def cli(self, interface, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode, interface=interface))

        # Interface : AppGigabitEthernet2/0/2 (0x4F1)
        p1 = re.compile(
            r"^Interface\s+:\s+(?P<interface>.+?)\s+\((?P<interface_id>\S+)\)$"
        )

        # VOQ OID        : 3760(0xEB0)
        p2 = re.compile(
            r"^VOQ OID\s+:\s+(?P<voq_oid>\S+)\((?P<voq_id>\S+)\)$"
        )

        # VOQ Set Size   : 8
        p3 = re.compile(r"^VOQ Set Size\s+:\s+(?P<value>\S+)$")

        # Base VOQ ID    : 20160
        p4 = re.compile(r"^Base VOQ ID\s+:\s+(?P<value>\S+)$")

        # Base VSC IDs   : 1408, 1472, 0
        p5 = re.compile(r"^Base VSC IDs\s+:\s+(?P<value>[\d,\s]+)$")

        # VOQ State      : Active
        p6 = re.compile(r"^VOQ State\s+:\s+(?P<value>\S+)$")

        # VOQ Flush      : Flush not active
        p7 = re.compile(r"^VOQ Flush\s+:\s+(?P<value>.+)$")

        # Is Empty       : Yes
        p8 = re.compile(r"^Is Empty\s+:\s+(?P<value>.+)$")

        # Profile OID            : 342(0x156)
        p9 = re.compile(
            r"^Profile OID\s+:\s+(?P<profile_oid>\d+)\((?P<profile_id>\S+)\)$"
        )

        # Device ID              : 0
        p10 = re.compile(r"^Device ID\s+:\s+(?P<value>\d+)$")

        # CGM Type               : Unicast
        p11 = re.compile(r"^CGM Type\s+:\s+(?P<value>\S+)$")

        # Profile reference count: 216
        p12 = re.compile(
            r"^Profile reference count\s*:\s+(?P<value>\d+)$"
        )

        # Is Reserved            : Yes
        p13 = re.compile(r"^Is Reserved\s+:\s+(?P<value>.+)$")

        # For speeds             : 10000000000
        p14 = re.compile(r"^For speeds\s+:\s+(?P<value>\d+)$")

        # Associated VOQ Offsets : 0, 1, 2, 3, 4, 5, 6, 7
        p15 = re.compile(
            r"^Associated VOQ Offsets\s+:\s+(?P<value>[\d,\s]+)$"
        )

        # HBM Enabled            : Disabled
        p16 = re.compile(r"^HBM Enabled\s+:\s+(?P<value>\S+)$")

        # HBM Block Size         : 6144
        # Q   Block Size         : 384
        p17 = re.compile(
            r"^(?P<name>HBM\s+Block\s+Size|Q\s+Block\s+Size)\s+:\s+(?P<value>\d+)$"
        )

        # RED Enabled            : Enabled
        p18 = re.compile(r"^RED Enabled\s+:\s+(?P<value>\S+)$")

        # FCN Enabled            : Disabled
        p19 = re.compile(r"^FCN Enabled\s+:\s+(?P<value>\S+)$")

        # Queue User Config      :
        p20 = re.compile(r"^Queue User Config\s+:$")

        # Q-Limit(Bytes    )    : 98304
        # Q-Limit(HBM Blocks)    : 1220
        p21 = re.compile(
            r"^Q-Limit\((?P<unit>[^)]+)\)\s+:\s+(?P<value>\d+)$"
        )

        # RED EMA Coefficient    : 1.000000
        p22 = re.compile(
            r"^RED EMA Coefficient\s+:\s+(?P<value>[\d.]+)$"
        )

        # RED Green :
        p23 = re.compile(r"^RED\s+(?P<red_flag>\S+)\s+:$")

        # Minimum              : 0
        p24 = re.compile(r"^Minimum\s+:\s+(?P<value>\d+)$")

        # Minium(HBM BLOCKS)   : 0
        p25 = re.compile(
            r"^Mini(?:mum|um)\(HBM BLOCKS\)\s*:\s*(?P<value>\d+)$"
        )

        # Maximum              : 98304
        p26 = re.compile(r"^Maximum\s+:\s+(?P<value>\d+)$")

        # Maximum(HBM BLOCKS)  : 1220
        p27 = re.compile(
            r"^Maximum\(HBM BLOCKS\)\s*:\s*(?P<value>\d+)$"
        )

        # Maximum Probability  : 0
        p28 = re.compile(
            r"^Maximum Probability\s*:\s*(?P<value>\d+)$"
        )

        # Queue H/W Values       :
        p29 = re.compile(r"^Queue H/W Values\s+:$")

        # RED Action                     : Drop
        p30 = re.compile(r"^RED Action\s+:\s+(?P<value>\S+)$")

        # RED Drop thresholds            : 0, 1220, 1220
        p31 = re.compile(
            r"^RED Drop thresholds\s+:\s*(?P<value>[\w\s,.]*)$"
        )

        # RED Drop Probabilities[Green]  : 0.000000, 0.000000
        p32 = re.compile(
            r"^RED Drop Probabilities\[(?P<red_flag>\S+)\]\s+:\s+(?P<value>[\w\s,.]+)$"
        )

        # HBM Free Thresholds            : 10000, 20000
        p33 = re.compile(
            r"^HBM Free Thresholds\s+:\s+(?P<value>[\w\s,.]+)$"
        )

        # HBM VOQ Age Thresholds         : 1, 2
        p34 = re.compile(
            r"^HBM VOQ Age Thresholds\s+:\s+(?P<value>[\w\s,.]+)$"
        )

        # HBM VOQ Thresholds             : 96, 992
        p35 = re.compile(
            r"^HBM VOQ Thresholds\s+:\s+(?P<value>[\w\s,.]+)$"
        )

        ret_dict = {}
        int_dict = None
        profile_dict = None
        queue_config_dict = None
        queue_hw_dict = None
        red_dict = None
        current_section = None

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_name = Common.convert_intf_name(group["interface"])
                int_dict = ret_dict.setdefault("interface", {}).setdefault(
                    interface_name, {}
                )
                int_dict["interface_id"] = group["interface_id"]
                continue

            m = p2.match(line)
            if m:
                int_dict["voq_oid"] = m.groupdict()["voq_oid"]
                int_dict["voq_id"] = m.groupdict()["voq_id"]
                continue

            m = p3.match(line)
            if m:
                int_dict["voq_set_size"] = m.groupdict()["value"]
                continue

            m = p4.match(line)
            if m:
                int_dict["base_voq_id"] = m.groupdict()["value"]
                continue

            m = p5.match(line)
            if m:
                int_dict["base_vsc_ids"] = _parse_csv_list(m.groupdict()["value"])
                continue

            m = p6.match(line)
            if m:
                int_dict["voq_state"] = m.groupdict()["value"]
                continue

            m = p7.match(line)
            if m:
                int_dict["voq_flush"] = m.groupdict()["value"]
                continue

            m = p8.match(line)
            if m:
                int_dict["is_empty"] = m.groupdict()["value"]
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                profile_dict = int_dict.setdefault("profile_oid", {}).setdefault(
                    group["profile_oid"], {}
                )
                profile_dict["profile_id"] = group["profile_id"]
                queue_config_dict = None
                queue_hw_dict = None
                red_dict = None
                current_section = None
                continue

            m = p10.match(line)
            if m:
                profile_dict["device_id"] = m.groupdict()["value"]
                continue

            m = p11.match(line)
            if m:
                profile_dict["cgm_type"] = m.groupdict()["value"]
                continue

            m = p12.match(line)
            if m:
                profile_dict["profile_reference_count"] = m.groupdict()["value"]
                continue

            m = p13.match(line)
            if m:
                profile_dict["is_reserved"] = m.groupdict()["value"]
                continue

            m = p14.match(line)
            if m:
                profile_dict["for_speeds"] = m.groupdict()["value"]
                continue

            m = p15.match(line)
            if m:
                profile_dict["associated_voq_offsets"] = _parse_csv_list(
                    m.groupdict()["value"]
                )
                continue

            m = p16.match(line)
            if m:
                profile_dict["hbm_enabled"] = m.groupdict()["value"]
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                key = "hbm_block_size"
                if group["name"].startswith("Q"):
                    key = "q_block_size"
                profile_dict[key] = group["value"]
                continue

            m = p18.match(line)
            if m:
                profile_dict["red_enabled"] = m.groupdict()["value"]
                continue

            m = p19.match(line)
            if m:
                profile_dict["fcn_enabled"] = m.groupdict()["value"]
                continue

            m = p20.match(line)
            if m:
                queue_config_dict = profile_dict.setdefault("queue_user_config", {})
                current_section = "queue_user_config"
                red_dict = None
                continue

            m = p21.match(line)
            if m:
                group = m.groupdict()
                unit = group["unit"].strip().lower()
                key = "q_limit_hbm_blocks"
                if unit.startswith("bytes"):
                    key = "q_limit_bytes"
                queue_config_dict[key] = group["value"]
                continue

            m = p22.match(line)
            if m:
                if current_section == "queue_hw_values":
                    queue_hw_dict["red_ema_coefficient"] = m.groupdict()["value"]
                else:
                    queue_config_dict["red_ema_coefficient"] = m.groupdict()["value"]
                continue

            m = p23.match(line)
            if m:
                queue_config_dict = profile_dict.setdefault("queue_user_config", {})
                red_dict = queue_config_dict.setdefault("red_flag", {}).setdefault(
                    m.groupdict()["red_flag"], {}
                )
                current_section = "queue_user_config"
                continue

            m = p24.match(line)
            if m:
                red_dict["minimum"] = m.groupdict()["value"]
                continue

            m = p25.match(line)
            if m:
                red_dict["minimum_hbm_blocks"] = m.groupdict()["value"]
                continue

            m = p26.match(line)
            if m:
                red_dict["maximum"] = m.groupdict()["value"]
                continue

            m = p27.match(line)
            if m:
                red_dict["maximum_hbm_blocks"] = m.groupdict()["value"]
                continue

            m = p28.match(line)
            if m:
                red_dict["maximum_probability"] = m.groupdict()["value"]
                continue

            m = p29.match(line)
            if m:
                queue_hw_dict = profile_dict.setdefault("queue_hw_values", {})
                current_section = "queue_hw_values"
                red_dict = None
                continue

            m = p30.match(line)
            if m:
                queue_hw_dict["red_action"] = m.groupdict()["value"]
                continue

            m = p31.match(line)
            if m:
                queue_hw_dict["red_drop_thresholds"] = _parse_csv_list(
                    m.groupdict()["value"]
                )
                continue

            m = p32.match(line)
            if m:
                group = m.groupdict()
                queue_hw_dict.setdefault("red_flag", {}).setdefault(
                    group["red_flag"], {}
                )["red_drop_probabilities"] = _parse_csv_list(group["value"])
                continue

            m = p33.match(line)
            if m:
                queue_hw_dict["hbm_free_thresholds"] = _parse_csv_list(
                    m.groupdict()["value"]
                )
                continue

            m = p34.match(line)
            if m:
                queue_hw_dict["hbm_voq_age_thresholds"] = _parse_csv_list(
                    m.groupdict()["value"]
                )
                continue

            m = p35.match(line)
            if m:
                queue_hw_dict["hbm_voq_thresholds"] = _parse_csv_list(
                    m.groupdict()["value"]
                )
                continue

        return ret_dict
