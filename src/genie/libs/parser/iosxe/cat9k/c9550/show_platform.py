import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

from genie.libs.parser.iosxe.cat9k.c9350.show_platform import(
   ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema as ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema_C9550,
   ShowPlatformSoftwareFedActiveAclInfoDbDetail as ShowPlatformSoftwareFedActiveAclInfoDbDetail_C9550,
   ShowPlatformTcamUtilizationSchema as ShowPlatformTcamUtilizationSchema_C9550,
   ShowPlatformTcamUtilization as ShowPlatformTcamUtilization_C9550,
   ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear as ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear_C9550,
   ShowPlatformHardwareFedQosSchedulerSdkInterface as ShowPlatformHardwareFedQosSchedulerSdkInterface_C9550,
   ShowPlatformHardwareFedSwitchQosQueueStatsInterface as ShowPlatformHardwareFedSwitchQosQueueStatsInterface_C9550
)

from genie.libs.parser.iosxe.cat9k.c9500.show_platform import(
   ShowPlatformHardwareChassisPowerSupplyDetailAllSchema as ShowPlatformHardwareChassisPowerSupplyDetailAllSchema_C9550,
   ShowPlatformHardwareChassisPowerSupplyDetailAll as ShowPlatformHardwareChassisPowerSupplyDetailAll_C9550
)

from genie.libs.parser.iosxe.cat9k.c9610.show_platform import(
   ShowPlatformHardwareAuthenticationStatusSchema as ShowPlatformHardwareAuthenticationStatusSchema_C9610,
   ShowPlatformHardwareAuthenticationStatus as ShowPlatformHardwareAuthenticationStatus_C9610
)

class ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema(ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema_C9550):
    ...


# ==========================================================
#  Parser for 'ShowPlatformSoftwareFedActiveAclInfoDbDetail'
# ==========================================================
class ShowPlatformSoftwareFedActiveAclInfoDbDetail(ShowPlatformSoftwareFedActiveAclInfoDbDetail_C9550):
    ...

class ShowPlatformTcamUtilizationSchema(ShowPlatformTcamUtilizationSchema_C9550):
    ...


# ==========================================================
#  Parser for 'ShowPlatformTcamUtilization'
# ==========================================================
class ShowPlatformTcamUtilization(ShowPlatformTcamUtilization_C9550):
    ...

class ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear(ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear_C9550):
    ...

class ShowPlatformHardwareFedQosSchedulerSdkInterface(ShowPlatformHardwareFedQosSchedulerSdkInterface_C9550):
    ...

class ShowPlatformHardwareFedQosSchedulerSdkInterface(ShowPlatformHardwareFedQosSchedulerSdkInterface_C9550):
    ...

class ShowPlatformHardwareChassisPowerSupplyDetailAll(ShowPlatformHardwareChassisPowerSupplyDetailAll_C9550):
    ...

class ShowPlatformHardwareAuthenticationStatusSchema(ShowPlatformHardwareAuthenticationStatusSchema_C9610):
    """Schema for show platform hardware authentication status."""

    ...


# ==========================================================
#  Parser for 'show platform hardware authentication status'
# ==========================================================
class ShowPlatformHardwareAuthenticationStatus(ShowPlatformHardwareAuthenticationStatus_C9610):
    """Parser for show platform hardware authentication status."""

    ...


class ShowPlatformHardwareFedSwitchQosQueueStatsInterface(ShowPlatformHardwareFedSwitchQosQueueStatsInterface_C9550):
    """Parser for show platform hardware fed {switch} {switch_var} qos queue stats interface {interface}"""
    ...

class ShowPlatformHardwareChassisFantrayDetailSchema(MetaParser):
    """Schema for show platform hardware chassis fantray detail"""
    
    schema = {
        'fantrays': {
            Any(): {
                'inlet_rpm': int,
                'outlet_rpm': int,
                'pwm_percentage': int
            }
        }
    }

# ==========================================================
#  Parser for 'ShowPlatformHardwareChassisFantrayDetail'
# ==========================================================
class ShowPlatformHardwareChassisFantrayDetail(ShowPlatformHardwareChassisFantrayDetailSchema):
    """Parser for show platform hardware chassis fantray detail
    """

    cli_command = ['show platform hardware chassis fantray detail', 
                   'show platform hardware chassis fantray detail switch {switch_mode}']

    def cli(self, switch_mode="",output=None):
        if output is None:
            if switch_mode:
                output = self.device.execute(self.cli_command[1].format(switch_mode=switch_mode))
            else:
                output = self.device.execute(self.cli_command[0])

        # Initialize return dictionary
        ret_dict = {}

        # FT1:
        # Inlet:4031 RPM, Outlet:5203 RPM, PWM:30%
        p1 = re.compile(r'^(?P<fantray>FT\d+):$')
        p2 = re.compile(r'^Inlet:(?P<inlet_rpm>\d+)\s+RPM,\s+Outlet:(?P<outlet_rpm>\d+)\s+RPM,\s+PWM:(?P<pwm>\d+)%$')

        current_fantray = None

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Match fantray identifier (FT1:, FT2:, etc.)
            m = p1.match(line)
            if m:
                current_fantray = m.groupdict()['fantray']
                if 'fantrays' not in ret_dict:
                    ret_dict['fantrays'] = {}
                ret_dict['fantrays'][current_fantray] = {}
                continue

            # Match RPM and PWM data
            m = p2.match(line)
            if m and current_fantray:
                group = m.groupdict()
                ret_dict['fantrays'][current_fantray].update({
                    'inlet_rpm': int(group['inlet_rpm']),
                    'outlet_rpm': int(group['outlet_rpm']),
                    'pwm_percentage': int(group['pwm'])
                })
                continue

        return ret_dict

class ShowEnvironmentAllSchema(MetaParser):
    """Schema for show environment all"""

    schema = {
        Optional("critical_alarms"): int,
        Optional("major_alarms"): int,
        Optional("minor_alarms"): int,
        "sensor_list": {
            Any(): {
                "location": {
                    Any(): {
                        "sensor": {
                            Any(): {
                                "state": str,
                                "reading": str,
                                Optional("threshold"): {
                                    "minor": int,
                                    "major": int,
                                    "critical": int,
                                    "shutdown": int,
                                    "unit": str,
                                },
                            }
                        }
                    }
                }
            }
        },
        Optional("switch"): {
            Any(): {
                "power_supply": {
                    Any(): {
                        "model_no": str,
                        "type": str,
                        "capacity": str,
                        "status": str,
                        "fan_1_state": str,
                        "fan_2_state": str,
                    }
                },
                "fan": {
                    Any(): {
                        "status": str,
                        "fan_1_state": str,
                        "fan_2_state": str,
                    }
                },
            }
        },
        Optional("power_supply"): {
            Any(): {
                "model_no": str,
                "type": str,
                "capacity": str,
                "status": str,
                "fan_1_state": str,
                "fan_2_state": str,
            }
        },
        Optional("fan"): {
            Any(): {
                "status": str,
                "fan_1_state": str,
                "fan_2_state": str,
            }
        },
    }


class ShowEnvironmentAll(ShowEnvironmentAllSchema):
    """Parser for show environment all"""

    cli_command = "show environment all"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        current_switch = None
        sensor_list = None

        # Number of Critical alarms:  0
        p1 = re.compile(
            r"^Number of (?P<severity>Critical|Major|Minor) alarms:\s+(?P<count>\d+)$"
        )
        # Sensor List:  Environmental Monitoring
        p2 = re.compile(r"^Sensor List:\s+(?P<sensor_list>.+)$")
        # Switch:1
        p3 = re.compile(r"^Switch:\s*(?P<switch>\d+)$")
        # Temp: CPU board  R0  Normal  33  Celsius  (52,57,62,67)(Celsius)
        p4 = re.compile(
            r"^(?P<sensor_name>.+?)\s+(?P<location>\S+)\s+"
            r"(?P<state>\S+)\s+(?P<reading>\d+(?:\.\d+)?\s+\S+)\s+"
            r"(?:(?:\(\s*(?P<minor>\d+)\s*,\s*(?P<major>\d+)\s*,\s*"
            r"(?P<critical>\d+)\s*,\s*(?P<shutdown>\d+)\s*\)\s*"
            r"\((?P<threshold_unit>\S+)\))|na)$"
        )
        # PS1  C9K-PWR-750WAC  ac  n.a.  bad-input  n.a.  n.a.
        p5 = re.compile(
            r"^(?P<supply>PS\d+)\s+(?P<model_no>\S+)\s+(?P<type>\S+)\s+"
            r"(?P<capacity>\d+\s+\S+|n\.a\.)\s+(?P<status>\S+)\s+"
            r"(?P<fan_1_state>\S+)\s+(?P<fan_2_state>\S+)$"
        )
        # FT1  active  good  good
        p6 = re.compile(
            r"^(?P<tray>FT\d+)\s+(?P<status>\S+)\s+"
            r"(?P<fan_1_state>\S+)\s+(?P<fan_2_state>\S+)$"
        )

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Number of Critical alarms:  0
            m = p1.match(line)
            if m:
                severity = m.group("severity").lower()
                ret_dict[f"{severity}_alarms"] = int(m.group("count"))
                continue

            # Sensor List:  Environmental Monitoring
            m = p2.match(line)
            if m:
                sensor_list = ret_dict.setdefault("sensor_list", {}).setdefault(
                    m.group("sensor_list"), {}
                )
                continue

            # Switch:1
            m = p3.match(line)
            if m:
                current_switch = m.group("switch")
                ret_dict.setdefault("switch", {}).setdefault(current_switch, {})
                continue

            # Temp: CPU board  R0  Normal  33  Celsius  (52,57,62,67)(Celsius)
            m = p4.match(line)
            if m and sensor_list is not None:
                group = m.groupdict()
                sensor = sensor_list.setdefault("location", {}).setdefault(
                    group["location"], {}
                ).setdefault("sensor", {}).setdefault(group["sensor_name"].strip(), {})
                sensor["state"] = group["state"]
                sensor["reading"] = " ".join(group["reading"].split())
                if group["minor"] is not None:
                    sensor["threshold"] = {
                        "minor": int(group["minor"]),
                        "major": int(group["major"]),
                        "critical": int(group["critical"]),
                        "shutdown": int(group["shutdown"]),
                        "unit": group["threshold_unit"],
                    }
                continue

            # PS1  C9K-PWR-750WAC  ac  n.a.  bad-input  n.a.  n.a.
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if current_switch is None:
                    power_supply = ret_dict.setdefault("power_supply", {})
                else:
                    power_supply = ret_dict["switch"].setdefault(
                        current_switch, {}
                    ).setdefault("power_supply", {})
                power_supply[group.pop("supply")] = group
                continue

            # FT1  active  good  good
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if current_switch is None:
                    fan = ret_dict.setdefault("fan", {})
                else:
                    fan = ret_dict["switch"].setdefault(current_switch, {}).setdefault(
                        "fan", {}
                    )
                fan[group.pop("tray")] = group

        return ret_dict
