''' show_ospf.py

IOSXE parsers for the following show commands:

    * show ospf interface brief

'''

# Python
import re
import xmltodict
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.utils.common import Common

# ============================
# Schema for:
#   * 'show ospf interface brief'
class ShowOspfInterfaceBriefSchema(MetaParser):
    schema= {
        'interfaces': {
            Any(): {
                'state': str,
                'area': str,
                'dr_id': str,
                'bdr_id': str,
                'nbrs': int
            }
        }
    }

class ShowOspfInterfaceBrief(ShowOspfInterfaceBriefSchema):
    cli_command = 'show ospf interface brief'

    def cli(self):

        out = self.device.execute(self.cli_command)

        # Init vars
        ret_dict = {}
        # ge-0/0/2.0    BDR    0.0.0.1    2.2.2.2    4.4.4.4     5
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<state>\S+) '
            '+(?P<area>\S+) +(?P<dr_id>\S+) +(?P<bdr_id>\S+) +(?P<nbrs>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            # ge-0/0/2.0    BDR    0.0.0.1    2.2.2.2    4.4.4.4     5
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_dict = ret_dict.setdefault('interfaces', {}).\
                    setdefault(group['interface'], {})
                intf_dict.update({'state' : group['state']})
                intf_dict.update({'area' : group['area']})
                intf_dict.update({'dr_id' : group['dr_id']})
                intf_dict.update({'bdr_id' : group['bdr_id']})
                intf_dict.update({'nbrs' : int(group['nbrs'])})
                continue

        return ret_dict