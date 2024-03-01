"""show_interfaces_brief.py

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
#  schema for show interfaces brief
# ====================================================
class ShowInterfacesBriefSchema(MetaParser):
    """Schema for show interfaces brief"""
    schema = {
        'port':{
            Any():{
                Optional('port'): str,
                Optional('type'): str,
                Optional('intrusion'): str,
                Optional('enabled'): str,
                Optional('status'): str,
                Optional('mode'): str,
                Optional('mdiMode'): str,
                Optional('flowControl'): str,
                Optional('bcastLimit'): str,
               
                    }
                },
            }

# ====================================================
#  parser for show Interfaces Brief
# ====================================================
class ShowInterfacesBrief(ShowInterfacesBriefSchema):
    """Parser for show interfaces brief"""
    cli_command = 'show interfaces brief'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

#  Status and Counters - Port Status

#                           | Intrusion                           MDI  Flow Bcast
#   Port         Type       | Alert     Enabled Status Mode       Mode Ctrl Limit
#   ------------ ---------- + --------- ------- ------ ---------- ---- ---- -----
#   1/1          100/1000T  | No        Yes     Up     1000FDx    MDI  off  0
#   1/2          100/1000T  | No        Yes     Up     1000FDx    MDI  off  0
#   1/3          100/1000T  | No        Yes     Up     1000FDx    MDI  off  0
#   1/4          100/1000T  | No        Yes     Up     1000FDx    MDI  off  0
#   1/5          100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/6          100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/7          100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/8          100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/9          100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/10         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/11         100/1000T  | No        Yes     Up     100FDx     MDIX off  0
#   1/12         100/1000T  | No        Yes     Down   1000FDx    NA   off  0
#   1/13         100/1000T  | No        Yes     Up     100FDx     MDIX off  0
#   1/14         100/1000T  | No        Yes     Up     100FDx     MDIX off  0
#   1/15         100/1000T  | No        Yes     Up     100FDx     MDIX off  0
#   1/16         100/1000T  | No        Yes     Up     100FDx     MDIX off  0
#   1/17         100/1000T  | No        Yes     Up     100FDx     MDIX off  0
#   1/18         100/1000T  | No        Yes     Up     100FDx     MDIX off  0
#   1/19         100/1000T  | No        Yes     Up     100FDx     MDIX off  0
#   1/20         100/1000T  | No        Yes     Up     100FDx     MDI  off  0
#   1/21         100/1000T  | No        Yes     Up     100FDx     MDIX off  0
#   1/22         100/1000T  | No        Yes     Up     100FDx     MDIX off  0
#   1/23         100/1000T  | No        Yes     Up     1000FDx    MDIX off  0
#   1/24         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/25         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/26         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/27         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/28         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/29         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/30         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/31         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/32         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/33         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/34         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/35         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/36         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/37         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/38         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/39         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/40         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/41         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/42         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/43         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/44         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/45         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/46         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/47         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/48         100/1000T  | No        Yes     Down   1000FDx    Auto off  0
#   1/A1                    | No        Yes     Down   .               off  0
#   1/A2                    | No        Yes     Down   .               off  0
#   1/A3-Trk1    SFP+SR     | No        Yes     Up     10GigFD    NA   off  0
#   1/A4-Trk1    SFP+SR     | No        Yes     Up     10GigFD    NA   off  0

        p0 = re.compile(r'\s+(?P<port>(\S+[^ ]?))?\s\s+?(?P<type>(\S+|(\s+)))?\s\s+\|\s(?P<intrusion>(Yes|No))?\s+(?P<enabled>(Yes|No))?\s+(?P<status>Up|Down|)?\s+(?P<mode>([0-9A-Za-z]+|\.\s\s\s\s\s\s))?\s\s+?(?P<mdiMode>(MDI|Auto|MDIX|NA|\s\s))?\s+(?P<flowControl>(on|off))?\s+(?P<bcastLimit>([0-9]+))?$')

        interfaces_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p0.match(line)
            if m:
                interfaces = m.groupdict()['port']
                if 'port' not in interfaces_dict:
                    interfaces_dict['port'] = {}

                if interfaces not in interfaces_dict:
                    interfaces_dict['port'][interfaces] = {}

                interfaces_dict['port'][interfaces]['port'] = interfaces
                interfaces_dict['port'][interfaces]['type'] = m.groupdict()['type']
                interfaces_dict['port'][interfaces]['intrusion'] = m.groupdict()['intrusion']
                interfaces_dict['port'][interfaces]['enabled'] = m.groupdict()['enabled']
                interfaces_dict['port'][interfaces]['status'] = m.groupdict()['status']
                interfaces_dict['port'][interfaces]['mode'] = m.groupdict()['mode']
                interfaces_dict['port'][interfaces]['mdiMode'] = m.groupdict()['mdiMode']
                interfaces_dict['port'][interfaces]['flowControl'] = m.groupdict()['flowControl']
                interfaces_dict['port'][interfaces]['bcastLimit'] = m.groupdict()['bcastLimit']

        return interfaces_dict
