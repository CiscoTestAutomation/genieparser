"""show_vlan.py

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
#  schema for show vlan
# ====================================================
class ShowVlanSchema(MetaParser):
    """Schema for show vlan"""
    schema = {
        'vlans':{
            Any():{
                Optional('vlan_id'): str,
                Optional('name'): str,
                Optional('status'): str,
                Optional('voice'): str,
                Optional('jumbo'): str,
               
                    }
                },
            }

# ====================================================
#  parser for show vlan
# ====================================================
class ShowVlan(ShowVlanSchema):
    """Parser for show vlan"""
    cli_command = 'show vlan'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

#   This matches the report portion of the show vlan command.

        p0 = re.compile(r'(\s+([a-zA-Z]+\s+)+)-\s+([a-zA-Z]+( [a-zA-Z]+)+)([a-zA-Z]+(\s+[a-zA-Z]+)+)\s+:\s+([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?\s+[a-zA-Z]+\s[a-zA-Z]+\s:\s[a-zA-Z]+_([a-zA-Z]+(\s+[a-zA-Z]+)+) :\s+')

#   VLAN ID Name                             | Status     Voice Jumbo
#   ------- -------------------------------- + ---------- ----- -----
#   1       DEFAULT_VLAN                     | Port-based No    No
#   2       VLAN2_DATA_192.168.2.0           | Port-based No    No
#   82      VLAN82_VOICE_192.168.82.0        | Port-based No    No
#   101     VLAN101_Security_192.168.101.0   | Port-based No    No
#   2001    VLAN2001_MGT_192.168.255.0       | Port-based No    No
        p1 = re.compile(r'\s+(?P<vlan_id>[0-9]+)\s+(?P<name>(?=\S).*(?<=\S))\s+\|\s+(?P<status>(Port-based|active|suspended(.*)lshut|(.*)unsup)+)?\s+(?P<voice>(Yes|No))\s+(?P<jumbo>(Yes|No))?$')

        vlan_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

#   VLAN ID Name                             | Status     Voice Jumbo
#   ------- -------------------------------- + ---------- ----- -----
#   1       DEFAULT_VLAN                     | Port-based No    No
#   2       VLAN2_DATA_192.168.2.0           | Port-based No    No
#   82      VLAN82_VOICE_192.168.82.0        | Port-based No    No
#   101     VLAN101_Security_192.168.101.0   | Port-based No    No
#   2001    VLAN2001_MGT_192.168.255.0       | Port-based No    No

            m = p1.match(line)
            if m:
                vlan_id = m.groupdict()['vlan_id']
                if 'vlans' not in vlan_dict:
                    vlan_dict['vlans'] = {}

                if vlan_id not in vlan_dict:
                    vlan_dict['vlans'][vlan_id] = {}

                vlan_dict['vlans'][vlan_id]['vlan_id'] = vlan_id
                vlan_dict['vlans'][vlan_id]['name'] = m.groupdict()['name']
                if 'act/unsup' in m.groupdict()['status']:
                    status = 'unsupport'
                elif 'suspend' in m.groupdict()['status']:
                    status = 'suspend'

                elif 'shut' in m.groupdict()['status']:
                    status = 'shutdown'
                    vlan_dict['vlans'][vlan_id]['shutdown'] = True
                else:
                    status = m.groupdict()['status']
                vlan_dict['vlans'][vlan_id]['status'] = status
                vlan_dict['vlans'][vlan_id]['voice'] = m.groupdict()['voice']
                vlan_dict['vlans'][vlan_id]['jumbo'] = m.groupdict()['jumbo']

        return vlan_dict
