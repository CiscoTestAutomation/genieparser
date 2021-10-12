import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any
# import parser utils
from genie.libs.parser.utils.common import Common


# ==============================================
# Parser for 'show glbp brief'
# ==============================================

class ShowGlbpBriefSchema(MetaParser):
    """
    Schema for 'show glbp brief'
    """

    schema = {
        'interfaces': {
            Any(): {
                'forwarder': {
                    Any(): {
                        'grp': str,
                        'state': str,
                        'pri': str,
                        'address': str,
                        'active_router': str,
                        'standby_router': str
                    },
                }
            },
        }
    }


# ==========================================================
#  Parser for show glbp brief
# ==========================================================
class ShowGlbpBrief(ShowGlbpBriefSchema):

    cli_command = 'show glbp brief'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        #Vl220       1    -   100 Standby  122.1.1.254     122.1.1.1       local
        p1 = re.compile(
            r'(?P<interface>\S+)\s+(?P<grp>\d+)\s+(?P<fwd>\S+)\s+(?P<pri>\S+)\s+(?P<state>\S+)\s+(?P<address>\S+)\s+(?P<active_router>\S+)\s+(?P<standby_router>\S+)')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()

                grp = group['grp']
                fwd = group['fwd']
                pri = group['pri']
                address = group['address']
                active_router = group['active_router']
                standby_router = group['standby_router']
                interface = group['interface']
                state = group['state']

                glbp_dict = ret_dict.setdefault('interfaces', {})
                fwd_dict = glbp_dict.setdefault(interface, {})
                intf_dict = fwd_dict.setdefault('forwarder', {})

                intf_dict[fwd] = {}
                intf_dict[fwd]['grp'] = grp
                intf_dict[fwd]['state'] = state
                intf_dict[fwd]['pri'] = pri
                intf_dict[fwd]['address'] = address
                intf_dict[fwd]['active_router'] = active_router
                intf_dict[fwd]['standby_router'] = standby_router

        return ret_dict
