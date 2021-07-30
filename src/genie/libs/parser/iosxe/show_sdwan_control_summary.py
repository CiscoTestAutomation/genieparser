'''
* 'show sdwan control summary'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
from genie import parsergen


# ===========================================
# Schema for 'show sdwan control summary'
# ===========================================
class ShowSdwanControlSummarySchema(MetaParser):

    """ Schema for "show sdwan control summary" """

    schema = {
        "summary": int,
        "vbond_counts": int,
        "vmanage_counts": int,
        "vsmart_counts": int,
    }


# ===========================================
# Parser for 'show sdwan control summary'
# ===========================================
class ShowSdwanControlSummary(ShowSdwanControlSummarySchema):

    """ Parser for "show sdwan control summary" """

    cli_command = 'show sdwan control summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # sh sdwan control summary
        #  control summary 0
        #   vbond_counts   0
        #   vmanage_counts 1
        #   vsmart_counts  6

        p1 = re.compile(r"(?P<key>\w+)\s+(?P<value>\d+)")

        for line in out.splitlines():
            line = line.strip()
            m = p1.search(line)
            if m:
                groups = m.groupdict()
                key = groups["key"].lower()

                try:
                    value = int(groups["value"])
                except ValueError:
                    value = groups["value"]

                parsed_dict.update({key: value})

        return parsed_dict
