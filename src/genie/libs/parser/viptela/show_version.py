'''
* 'show version'
'''
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import genie.parsergen as pg
import re


# ===========================================
# Schema for 'show version'
# ===========================================


class ShowVersionSchema(MetaParser):
    """ Schema for "show version" """

    schema = {
        'version': str
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
        if out:
            # 99.99.999-4567
            p1 = re.compile('^(?P<value>[\d\w/\.\:\-]+)$')
            for line in out.splitlines():
                line = line.strip()
                m = p1.match(line)
                if m:
                    groups = m.groupdict()
                    parsed_dict.update({'version': (groups['value'])})
        return parsed_dict