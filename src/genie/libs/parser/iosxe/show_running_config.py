import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =============================
# Schema for:
#  * 'show running-config wlan'
# =============================
class ShowRunningConfigWlanSchema(MetaParser):
    """Schema for show running-config wlan."""

    schema = {
        "profile_name": {
            Any(): {
                "config": list,
                "ssid": str,
                "wlan_id": int,
            },
        },
    }


# =============================
# Parser for:
#  * 'show running-config wlan'
# =============================
class ShowRunningConfigWlan(ShowRunningConfigWlanSchema):
    """Parser for show running-config wlan"""

    cli_command = "show running-config wlan"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)

        else:
            out = output

        wlan_capture = re.compile(
            r"^wlan\s(?P<profile_name>\S+)\s(?P<wlan_id>\d+)\s(?P<ssid>\S+)"
        )

        config_group = []

        wlan_info_obj = {}

        for line in out.splitlines():
            line = line.strip()

            if wlan_capture.match(line):
                match = wlan_capture.match(line)
                group = match.groupdict()

                group["wlan_id"] = int(group["wlan_id"])

                # pull a key from dict to use as new_key
                new_key = "profile_name"
                new_group = {group[new_key]: {}}
                group.update({"config": []})

                # update then pop new_key from the dict
                new_group[group[new_key]].update(group)
                new_group[group[new_key]].pop(new_key)

                # initialize then update the dict
                if not wlan_info_obj.get(new_key):
                    wlan_info_obj[new_key] = {}

                wlan_info_obj[new_key].update(new_group)

                # grab key and set config_group for each new_key value
                config_group = wlan_info_obj[new_key][group[new_key]]["config"]

            else:
                config_group.append(line)

        return wlan_info_obj
