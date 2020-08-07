# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import genie.parsergen as pg
import re


# ===========================================
# Schema for 'show software | tab'
# ===========================================


class ShowVersionSchema(MetaParser):
    """ Schema for "show version" """

    schema = {
        'VERSION': str
    }
# ===========================================
# Parser for 'show version'
# ===========================================

class ShowVersion(ShowVersionSchema):
    """ Parser for "show version" """

    cli_command = "show version"

    def cli(self, output=None):
        parsed_dict = {}
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # srp_vedge# show version
        # 99.99.999-4567
        if out:
            for line in out.splitlines():
                line = line.strip()
                p1 = re.compile('^(?P<value>[\d\w/\.\:\-]+)$')
                m = p1.match(line)
                if m:
                    groups = m.groupdict()
                    parsed_dict.update({'VERSION': (groups['value'])})
        return parsed_dict