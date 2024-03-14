"""show_ntp.py

IOSXE parsers for the following show commands:

    * show sntp

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or


# ==============================================
#  Schema for show sntp
# ==============================================
class ShowSntpSchema(MetaParser):
    """Schema for show sntp"""

    schema = {
        'servers': {
                Any(): {
                    'stratum': int,
                    'version': int,
                    'updated': str,
                    'synced': bool
                    },
                },
            }


# ==============================================
#  Parser for show sntp
# ==============================================
class ShowSntp(ShowSntpSchema):
    """Parser for show sntp"""


    cli_command = 'show sntp'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}
        # SNTP server                Stratum   Version    Last Received
        # 192.168.131.58              3           4        15w5d     
        # 192.168.131.59              3           4        15w5d     
        # 172.18.1.10                 16          4        never     
        # 192.168.131.59              3           4        00:01:00      Synced

        p1 = re.compile( r'^(?P<server>[\w\.\:]+) +(?P<stratum>\d+) +(?P<version>\d+) +(?P<updated>[\w\:\.]+) *(?P<status>\w*)$' )

        for line in out.splitlines():
            line = line.strip()
            
            if not line:
                continue

            # 192.168.131.58              3           4        15w5d     
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                server = groups['server']
                if groups['status']:
                    synced = True
                else:
                    synced = False
                peer_dict = ret_dict.setdefault('servers', {}).setdefault(server, {})
                   
                peer_dict.update({
                                  'stratum': int(groups['stratum']),
                                  'version': int(groups['version']),
                                  'updated': groups['updated'],
                                  'synced': synced
                                })

        return ret_dict


