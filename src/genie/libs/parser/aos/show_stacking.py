"""show_stacking.py

"""
import re
import logging

from genie.metaparser import MetaParser
from genie.libs.parser.utils.common import Common
from genie.metaparser.util.schemaengine import Any, Optional


logger = logging.getLogger(__name__)


def regexp(expression):
    def match(value):
        if re.match(expression,value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                              %(value, expression))
    return match

# ====================================================
#  schema for show stacking
# ====================================================
class ShowStackingSchema(MetaParser):
    """Schema for show stacking"""
    schema = {
        'id':{
            Any():{
                Optional('id'): str,
                Optional('mac'): str,
                Optional('model'): str,
                Optional('pri'): str,
                Optional('status'): str,
               
                    }
                },
            }

# ====================================================
#  parser for show stacking
# ====================================================
class ShowStacking(ShowStackingSchema):
    """Parser for show stacking"""
    cli_command = 'show stacking'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

#   This matches the report portion of the show stacking command.

   
# This is the payload.
# ID  Mac Address       Model                                 Pri Status
# --- ----------------- ------------------------------------- --- ---------------
# 1  123456-123456     Aruba JL076A 3810M-40G-8SR-PoE+-1-... 255 Commander
# 2  123456-123654     Aruba JL076A 3810M-40G-8SR-PoE+-1-... 128 Standby

        p0 = re.compile(r'\s+(?P<id>[0-9]+)\s+(?P<mac>[0-9a-f]+-[0-9a-f]+)\s+(?P<model>.+|\s+)?\s(?P<pri>[0-9]+)\s+(?P<status>(Commander|Standby|Member))?$')

        id_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

# This is the payload.
# ID  Mac Address       Model                                 Pri Status
# --- ----------------- ------------------------------------- --- ---------------
# 1  123456-123456     Aruba JL076A 3810M-40G-8SR-PoE+-1-... 255 Commander
# 2  123456-123654     Aruba JL076A 3810M-40G-8SR-PoE+-1-... 128 Standby

            m = p0.match(line)
            if m:
                id = m.groupdict()['id']
                if 'id' not in id_dict:
                    id_dict['id'] = {}

                if id not in id_dict:
                    id_dict['id'][id] = {}

                id_dict['id'][id]['id'] = id
                id_dict['id'][id]['mac'] = m.groupdict()['mac']
                id_dict['id'][id]['model'] = m.groupdict()['model']
                id_dict['id'][id]['pri'] = m.groupdict()['pri']
                id_dict['id'][id]['status'] = m.groupdict()['status']

        return id_dict
