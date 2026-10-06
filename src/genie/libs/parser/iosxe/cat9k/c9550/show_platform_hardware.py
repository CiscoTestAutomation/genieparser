"""show_platform_hardware.py

    * 'show platform hardware voltage margin rp active'
"""

import re

from genie.libs.parser.iosxe.show_platform_hardware import (
    ShowPlatformHardwareVoltageMarginSwitchSchema as
    ShowPlatformHardwareVoltageMarginRpActiveSchema,
)


class ShowPlatformHardwareVoltageMarginRpActive(
    ShowPlatformHardwareVoltageMarginRpActiveSchema
):
    """Parser for show platform hardware voltage margin rp active"""

    cli_command = "show platform hardware voltage margin rp active"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # max chnl 16
        p1 = re.compile(r"^max chnl\s+(?P<max_channels>\d+)$")

        # 0  CPU_P3P3V_S5  3296.87  3300.00  -4.50  -0.09  4.50  0
        p2 = re.compile(
            r"^(?P<channel>\d+)\s+(?P<rail_name>\S+)\s+"
            r"(?P<voltage_in_mv>-?\d+(?:\.\d+)?)\s+"
            r"(?P<nominal_voltage>-?\d+(?:\.\d+)?)\s+"
            r"(?P<min_margin>-?\d+(?:\.\d+)?)\s+"
            r"(?P<percentage_change>-?\d+(?:\.\d+)?)\s+"
            r"(?P<max_margin>-?\d+(?:\.\d+)?)\s+"
            r"(?P<monitor>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # max chnl 16
            m = p1.match(line)
            if m:
                ret_dict["max_channels"] = int(m.group("max_channels"))
                continue

            # 0  CPU_P3P3V_S5  3296.87  3300.00  -4.50  -0.09  4.50  0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                channel = ret_dict.setdefault("channels", {}).setdefault(
                    int(group.pop("channel")), {}
                )
                channel.update(
                    {
                        "rail_name": group["rail_name"],
                        "voltage_in_mv": float(group["voltage_in_mv"]),
                        "nominal_voltage": float(group["nominal_voltage"]),
                        "min_margin": float(group["min_margin"]),
                        "percentage_change": float(group["percentage_change"]),
                        "max_margin": float(group["max_margin"]),
                        "monitor": int(group["monitor"]),
                    }
                )
                continue

        return ret_dict
