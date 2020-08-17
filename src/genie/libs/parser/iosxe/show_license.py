''' show_license.py

IOSXE parsers for the following show commands:
    * show license
'''

# Python

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =================
# Schema for:
#  * 'show license'
# =================

class ShowLicenseSchema(MetaParser):
    """Schema for show license."""

    schema = {
        'licenses': {
            int: {
                'feature': str,
                'period_left': str,
                Optional('period_minutes'): int,
                Optional('period_seconds'): int,
                'license_type': str,
                'license_state': str,
                Optional('count_in_use'): int,
                Optional('count_violation'): int,
                Optional('count'): str,
                'license_priority': str

            }
        }
    }



# =================
# Parser for:
#  * 'show license'
# =================
class ShowLicense(ShowLicenseSchema):
    """Parser for show license"""

    cli_command = 'show license'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Index 1 Feature: appxk9
        p1 = re.compile(r"Index\s+(?P<id>\d+)\s+Feature:\s+(?P<feature>\S+)")
        #         Period left: Life time
        p2 = re.compile(r"\s+(?P<period_left>(Life\s+time|Not\s+Activated))")
        # 	        Period Used: 0  minute  0  second
        p3 = re.compile(r"\s+(?P<period_minutes>\d+)\s+minute\s+(?P<period_seconds>\d+)\s+second")
        #         License Type: Permanent
        p4 = re.compile(r"\s+(?P<license_type>(Permanent|EvalRightToUse))")
        #         License State: Active, In Use
        p5 = re.compile(r"\s+((?P<count_in_use>\d+)/(?P<count_violation>\d+)\s+\(In-use/Violation\)|(?P<count>\S+))")
        #         License Priority: None
        p6 = re.compile(r"\s+(?P<license_priority>\S+)")
        #         License State: Active, Not in Use, EULA not accepted
        p7 = re.compile(r"\s+(?P<license_state>(Active,\s+Not\s+in\s+Use,\s+EULA\s+not\s+accepted|Active,\s+In\s+Use))")

        regex_map = {
            "Period left": p2,
            "Period Used": p3,
            "License Type": p4,
            "License Count": p5,
            "License Priority": p6,
            "License State": p7,
        }

        # initial variables
        license_dict = {}
        # Index 1 Feature: appxk9
        #         Period left: Life time
        #         License Type: Permanent
        #         License State: Active, In Use
        #         License Count: Non-Counted
        #         License Priority: Medium

        for line in out.splitlines():
            line_strip = line.strip()
            if not line_strip.startswith("Index"):
                try:
                    data_type, value = line_strip.split(":", 1)
                    regex = regex_map.get(data_type)
                except ValueError:
                    continue
            else:
                match = p1.match(line_strip)
                # Index 1 Feature: appxk9
                groups = match.groupdict()
                group_id = int(groups['id'])
                license_dict.update({group_id: {'feature': groups['feature']}})
                continue

            if regex:
                match = regex.match(value)
                groups = match.groupdict()
                for k, v in groups.items():
                    if v is None:
                        continue
                    if v.isdigit():
                        v = int(v)
                    license_dict[group_id].update({k: v})

        if license_dict:
            return {"licenses": license_dict}
        else:
            return {}
