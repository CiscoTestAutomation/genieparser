"""IOSXE C9250 parser for the following command:

* ``show switch stack-ports summary``
"""

import re

from genie.libs.parser.iosxe.cat9k.c9350 import show_switch as c9350


class ShowSwitchStackPortSummarySchema(
    c9350.ShowSwitchStackPortSummarySchema
):
    """Schema for C9250 ``show switch stack-ports summary`` output."""

    pass


class ShowSwitchStackPortSummary(ShowSwitchStackPortSummarySchema):
    """Parser for ``show switch stack-ports summary`` on C9250."""

    cli_command = ["show switch stack-ports summary"]

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        ret_dict = {}

        # 1/1  OK  2/2  50cm      Yes  Yes  Yes  1  No
        # 1/1  OK  2/2  No Cable  Yes  Yes  Yes  1  No
        p1 = re.compile(
            r"^(?P<stackport_id>\S+)\s+"
            r"(?P<port_status>\S+)\s+"
            r"(?P<neighbor>\S+)\s+"
            r"(?P<cable_length>.+?)\s+"
            r"(?P<link_ok>Yes|No)\s+"
            r"(?P<link_active>Yes|No)\s+"
            r"(?P<sync_ok>Yes|No)\s+"
            r"(?P<link_changes_count>\d+)\s+"
            r"(?P<in_loopback>Yes|No)$"
        )

        for line in output.splitlines():
            match = p1.match(line.strip())
            if not match:
                continue

            values = match.groupdict()
            stackport_dict = ret_dict.setdefault("stackports", {}).setdefault(
                values["stackport_id"], {}
            )
            stackport_dict.update(
                {
                    "port_status": values["port_status"],
                    "neighbor": values["neighbor"],
                    "cable_length": values["cable_length"],
                    "link_ok": values["link_ok"],
                    "link_active": values["link_active"],
                    "sync_ok": values["sync_ok"],
                    "link_changes_count": int(values["link_changes_count"]),
                    "in_loopback": values["in_loopback"],
                }
            )

        return ret_dict
