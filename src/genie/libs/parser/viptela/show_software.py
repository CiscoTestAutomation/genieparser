'''
* 'show software | tab'
'''
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import genie.parsergen as pg
import re

# ===========================================
# Schema for 'show software | tab'
# ===========================================


class ShowSoftwaretabSchema(MetaParser):
    """ Schema for "show software | tab" """

    schema = {
        'version':{
            str: {
                'active': str,
                'confirmed': str,
                'default': str,
                'previous': str,
                'timestamp': str,
            }
        }
    }
# ===========================================
# Parser for 'show software | tab'
# ===========================================

class ShowSoftwaretab(ShowSoftwaretabSchema):
    """ Parser for "show software | tab" """

    cli_command = "show software | tab"

    def cli(self, output=None):
        parsed_dict = {}
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # VERSION         ACTIVE  DEFAULT  PREVIOUS  CONFIRMED  TIMESTAMP
        # ---------------------------------------------------------------------------------
        # 99.99.999-4499  false   false    true      -          2020-06-01T03:30:46-00:00
        # 99.99.999-4542  false   false    false     -          2020-06-18T06:30:30-00:00
        # 99.99.999-4567  true    true     false     auto       2020-07-06T01:51:18-00:00
        if out:
            out = pg.oper_fill_tabular(device_output=out,
                                    header_fields=["VERSION", "ACTIVE", "DEFAULT", "PREVIOUS", "CONFIRMED", "TIMESTAMP"],
                                    label_fields=["version", "active", "default", "previous", "confirmed", "timestamp"],
                                    index=[0])
            return_dict = out.entries
            version_dict ={}
            for keys in return_dict.keys() :
                dict1={}
                del return_dict[keys]['version']
                version_dict[keys] = return_dict[keys]
            parsed_dict['version'] = version_dict
        return parsed_dict