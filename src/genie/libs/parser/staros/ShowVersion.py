"""
* 'show version'
"""

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional


# ===========================================
# Schema for 'show version'
# ===========================================

class ShowVersionUPFSchema(MetaParser):
    """Schema for "show version" """

    schema = {
        "Image Version:": str,
        "Image Build Number": str,
        "Image Description": str,
        "Image Date": str,
        "Boot Image": str,
        "Source Commit ID": str,
    }


# ===========================================
# Parser for 'show version'
# ===========================================


class ShowVersionUPF(ShowVersionUPFSchema):
    """Parser for "show version" """

    cli_command = "show version"

    def cli(self, output = None):
        if output is None:
            output = self.device.execute(self.cli_command)
        parsed_dict = {}
	
	# regex to capture key-value pairs, key is labeled as "type" and value is labeled as "value"
        p1 = re.compile(r"^\s*(?P<type>.*):\s+(?P<value>.*)$")

        for line in output.splitlines():
            line = line.strip()
	    # Image Version:                  21.15.47
	    # Image Build Number:             76955
	    # Image Description:              Deployment_Build
	    # Image Date:                     Wed Aug  5 08:42:44 EDT 2020
	    # Boot Image:                     /flash/asr5500-21.15.47.bin.SPA
	    # Source Commit ID:               883f89545a52f845b399d711b7d16d8bcf90be0d
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                parsed_dict[group["type"].lower().replace(" ", "_")] = group["value"]
        
        return parsed_dict
    
