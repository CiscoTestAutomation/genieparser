# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import genie.parsergen as pg
import re


# ===========================================
# Schema for 'show software'
# ===========================================


class ShowSoftwareSchema(MetaParser):
    """ Schema for "show software" """

    schema = {
        Any():{
            'ACTIVE': str,
            'CONFIRMED': str,
            'DEFAULT': str,
            'PREVIOUS': str,
            'TIMESTAMP': str,
            'VERSION': str
        }
    }


# ===========================================
# Parser for 'show software | tab'
# ===========================================


class ShowSoftwaretab(ShowSoftwareSchema):
    """ Parser for "show software | tab" """

    cli_command = "show software | tab"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # VERSION         ACTIVE  DEFAULT  PREVIOUS  CONFIRMED  TIMESTAMP
        # ---------------------------------------------------------------------------------
        # 99.99.999-4499  false   false    true      -          2020-06-01T03:30:46-00:00
        # 99.99.999-4542  false   false    false     -          2020-06-18T06:30:30-00:00
        # 99.99.999-4567  true    true     false     auto       2020-07-06T01:51:18-00:00

        out = pg.oper_fill_tabular(self.device,
                                   show_command=self.cli_command,
                                   header_fields=
                                   ["VERSION", "ACTIVE", "DEFAULT", "PREVIOUS", "CONFIRMED", "TIMESTAMP"],
                                   index=[0])
        parsed_dict = out.entries

        return parsed_dict


class ShowSoftware(ShowSoftwareSchema):
    """ Parser for "show software" """

    cli_command = "show software"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # software 99.99.999-4499
        #  active    false
        #  default   false
        #  previous  true
        #  timestamp 2020-06-01T03:30:46-00:00
        # software 99.99.999-4542
        #  active    false
        #  default   false
        #  previous  false
        #  timestamp 2020-06-18T06:30:30-00:00
        # software 99.99.999-4567
        #  active    true
        #  default   true
        #  previous  false
        #  confirmed auto
        #  timestamp 2020-07-06T01:51:18-00:00

        p1 = re.compile(r'(?P<key>[\w\/\.\-]+) +(?P<value>[\d\w\/\.\:\-]+)$')

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace('-', '_').lower()
                parsed_dict.update({key: (groups['value'])})

        print(parsed_dict)
        return parsed_dict