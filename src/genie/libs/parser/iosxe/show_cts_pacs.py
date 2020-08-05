import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ==================
# Schema for:
#  * 'show cts pacs'
# ==================
class ShowCtsPacsSchema(MetaParser):
    """Schema for show cts pacs."""

    schema = {
        "cts_pacs_info": {
            "aid": str,
            "pac_type": str,
            "iid": str,
            "aid_info": str,
            "lifetime": {
                "date": str,
                "time": str,
                "time_zone": str
            },
            "pac_opaque": str,
            "refresh_timer": str
        }
    }


# ==================
# Parser for:
#  * 'show cts pacs'
# ==================
class ShowCtsPacs(ShowCtsPacsSchema):
    """Parser for show cts pacs"""

    cli_command = ['show cts pacs']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output


        cts_pacs_dict = {}

        aid_capture = re.compile(r"^AID:\s+(?P<aid>\S+)", re.MULTILINE)
        pac_type_capture = re.compile(r"^PAC-type\s=\s(?P<pac_type>.*$)", re.MULTILINE)
        iid_capture = re.compile(r"^I-ID:\s+(?P<iid>\S+)", re.MULTILINE)
        aid_info_capture = re.compile(r"^A-ID-Info:\s+(?P<aid_info>.*$)", re.MULTILINE)
        credential_lifetime_capture = re.compile(
            r"^Credential\s+Lifetime:\s+(?P<time>\d+:\d+:\d+)\s+(?P<time_zone>\S+)\s+(?P<day>\S+)\s+(?P<month>\S+)\s+(?P<date>\d+)\s+(?P<year>\d+)",
            re.MULTILINE)
        pac_opaque_capture = re.compile(r"^PAC-Opaque:\s+(?P<pac_opaque>.*$)", re.MULTILINE)
        refresh_timer_capture = re.compile(r"^Refresh\s+timer\s+is\s+set\s+for\s+(?P<refresh_timer>\S+)", re.MULTILINE)

        remove_lines = ('PAC-Info:')

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # print(clean_line)
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)

        for line in out:
            aid_match = aid_capture.match(line)
            if aid_match:
                groups = aid_match.groupdict()
                aid = groups['aid']
                if not cts_pacs_dict.get('cts_pacs_info', {}):
                    cts_pacs_dict['cts_pacs_info'] = {}
                cts_pacs_dict['cts_pacs_info']['aid'] = aid
                continue
            pac_type_match = pac_type_capture.match(line)
            if pac_type_match:
                groups = pac_type_match.groupdict()
                pac_type = groups['pac_type']
                cts_pacs_dict['cts_pacs_info']['pac_type'] = pac_type
                continue
            iid_match = iid_capture.match(line)
            if iid_match:
                groups = iid_match.groupdict()
                iid = groups['iid']
                cts_pacs_dict['cts_pacs_info']['iid'] = iid
                continue
            aid_info_match = aid_info_capture.match(line)
            if aid_info_match:
                groups = aid_info_match.groupdict()
                aid_info = groups['aid_info']
                cts_pacs_dict['cts_pacs_info']['aid_info'] = aid_info
                continue
            credential_lifetime_match = credential_lifetime_capture.match(line)
            if credential_lifetime_match:
                groups = credential_lifetime_match.groupdict()
                time = groups['time']
                time_zone = groups['time_zone']
                day = groups['day']
                month = groups['month']
                date = groups['date']
                year = groups['year']
                full_date = f"{day}, {month}/{date}/{year}"
                cts_pacs_dict['cts_pacs_info'].update(
                    {'lifetime': {'date': full_date, 'time': time, 'time_zone': time_zone}})
                continue
            pac_opaque_match = pac_opaque_capture.match(line)
            if pac_opaque_match:
                groups = pac_opaque_match.groupdict()
                pac_opaque = groups['pac_opaque']
                cts_pacs_dict['cts_pacs_info']['pac_opaque'] = pac_opaque
                continue
            refresh_timer_match = refresh_timer_capture.match(line)
            if refresh_timer_match:
                groups = refresh_timer_match.groupdict()
                refresh_timer = groups['refresh_timer']
                cts_pacs_dict['cts_pacs_info']['refresh_timer'] = refresh_timer
                continue

        return cts_pacs_dict

