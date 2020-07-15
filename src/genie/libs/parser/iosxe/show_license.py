''' show_license.py

IOS parsers for the following show commands:
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

        p1 = re.compile(r"Index\s+(?P<id>\d+)\s+Feature:\s+(?P<feature>\S+)", re.MULTILINE)
        p2 = re.compile(r"\s+Period\s+left:\s+(?P<period_left>(Life\s+time|Not\s+Activated))", re.MULTILINE)
        p3 = re.compile(r"\s+Period\s+Used:\s+(?P<period_minutes>\d+)\s+minute\s+(?P<period_seconds>\d+)\s+second",
                        re.MULTILINE)
        p4 = re.compile(r"\s+License\s+Type:\s+(?P<license_type>(Permanent|EvalRightToUse))", re.MULTILINE)
        p5 = re.compile(
            r"\s+License\s+Count:\s+((?P<count_in_use>\d+)/(?P<count_violation>\d+)\s+\(In-use/Violation\)|(?P<count>)\S+)",
            re.MULTILINE)
        p6 = re.compile(r"\s+License\s+Priority:\s+(?P<license_priority>\S+)", re.MULTILINE)
        p7 = re.compile(
            r"\s+License\s+State:\s+(?P<license_state>(Active,\s+Not\s+in\s+Use,\s+EULA\s+not\s+accepted|Active,\s+In\s+Use))",
            re.MULTILINE)

        matches = [p1, p2, p3, p4, p5, p6, p7]

        # initial variables
        ret_dict = {}
        # Index 1 Feature: appxk9
        #         Period left: Life time
        #         License Type: Permanent
        #         License State: Active, In Use
        #         License Count: Non-Counted
        #         License Priority: Medium

        group_id = ''

        for line in out.splitlines():
            for match in matches:
                m = match.match(line)
                if m:
                    if not ret_dict.get('licenses'):
                        ret_dict.update({'licenses': {}})
                    groups = m.groupdict()
                    if groups.get('id'):
                        group_id = int(groups['id'])
                        ret_dict['licenses'].update({group_id: {'feature': groups['feature']}})
                    else:
                        for k, v in groups.items():
                            if k and v:
                                try:
                                    ret_dict['licenses'][group_id].update({k: int(v)})
                                except ValueError:
                                    ret_dict['licenses'][group_id].update({k: v})
        return ret_dict
