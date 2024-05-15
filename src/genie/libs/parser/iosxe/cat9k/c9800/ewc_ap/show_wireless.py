import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or


# ==========================================
# Schema for:
#  * 'show wireless ewc-ap predownload status'
# ==========================================
class ShowWirelessEwcApPredownloadStatusSchema(MetaParser):
    schema = {
        "predownload_status": str,
        "predownload_error": str
    }


# ==========================================
# Parser for:
#  * 'show wireless ewc-ap predownload status'
# ==========================================
class ShowWirelessEwcApPredownloadStatus(ShowWirelessEwcApPredownloadStatusSchema):
    """Parser for show wireless ewc-ap predownload status"""

    cli_command = 'show wireless ewc-ap predownload status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output = output

        # Predownload Status: None
        p_predownload_status = re.compile(r"Predownload Status:\s+(?P<value>.*)$")

        # Predownload Error: None
        p_predownload_error = re.compile(r"Predownload Error:\s+(?P<value>.*)$")

        return_dict = {}

        for line in output.splitlines():
            line = line.strip()
            if p_predownload_status.match(line):
                # Predownload Status: None
                match = p_predownload_status.match(line)
                return_dict.update({"predownload_status": match.group("value")})
                continue
            elif p_predownload_error.match(line):
                # Predownload Error: None
                match = p_predownload_error.match(line)
                return_dict.update({"predownload_error": match.group("value")})
                continue
        return return_dict

