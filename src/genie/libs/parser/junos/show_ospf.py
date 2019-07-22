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
#   * 'show ospf interface brief instance master'
class ShowOspfInterfaceBriefSchema(MetaParser):
    schema= {
        'instance':{
            Any(): {
                'areas': {
                    Any(): {
                        'interfaces': {
                            Any(): {
                                'state': str,
                                'dr_id': str,
                                'bdr_id': str,
                                'nbrs_count': int,
                            }
                        }
                    }
                }
            }
        }
    }

class ShowOspfInterfaceBrief(ShowOspfInterfaceBriefSchema):
    cli_command = [
        'show ospf interface brief instance {instance}',
        'show ospf interface brief']

    def cli(self, instance=None, output=None):
        if output is None:
            if instance:
                out = self.device.execute(self.cli_command[0].format(instance=instance))
            else:
                instance='master'
                out = self.device.execute(self.cli_command[1])
        else:
            out = output

        # Init vars
        ret_dict = {}
        # ge-0/0/2.0    BDR    0.0.0.1    2.2.2.2    4.4.4.4     5
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<state>\S+) '
            '+(?P<area>\S+) +(?P<dr_id>\S+) +(?P<bdr_id>\S+) +(?P<nbrs_count>\d+)$')
        
        for line in out.splitlines():
            line = line.strip()
            
            # ge-0/0/2.0    BDR    0.0.0.1    2.2.2.2    4.4.4.4     5
            m = p1.match(line)
            if m:
                group = m.groupdict()
                area = group['area']
                intf_dict = ret_dict.setdefault('instance', {}).\
                    setdefault(instance, {}).\
                    setdefault('areas', {}).\
                    setdefault(area, {}).\
                    setdefault('interfaces', {}).\
                    setdefault(group['interface'], {})

                intf_dict.update({'state' : group['state']})
                intf_dict.update({'dr_id' : group['dr_id']})
                intf_dict.update({'bdr_id' : group['bdr_id']})
                intf_dict.update({'nbrs_count' : int(group['nbrs_count'])})
                continue

        return ret_dict