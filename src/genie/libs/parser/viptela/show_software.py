# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import genie.parsergen as pg

import re


# ===========================================
# Schema for 'show control connections'
# ===========================================


class ShowSoftwareSchema(MetaParser):
    """ Schema for "show control connections" """

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
# Parser for 'show software'
# ===========================================


class ShowSoftware(ShowSoftwareSchema):
    """ Parser for "show control connections" """

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

