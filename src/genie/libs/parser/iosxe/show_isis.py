"""show_isis.py

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional, \
                                               Or, \
                                               And, \
                                               Default, \
                                               Use

"""show isis neighbors"""

class ShowIsisNeighborSchema(MetaParser):
    """Schema for show isis neighbor"""
    schema = {
        'isis': {
            Any(): {
                'neighbors': {
                    Any(): {
                        'circuit_id': str,
                        'holdtime': str,
                        'interface': str,
                        'ip_address': str,
                        'state': str,
                        'type': str,
                        },
                     }
                }
            }
        }

class ShowIsisNeighbor(ShowIsisNeighborSchema):
    """Parser for show isis neighbor"""

    cli_command = 'show isis neighbor'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # Tag isis_net:
            p1 = re.compile(r'^\s*Tag\s+(?P<isis_name>\S+)\s*:\s*$')
            m = p1.match(line)
            if m:
                isis_name = m.groupdict()['isis_name']
                continue

            # LAB-9001-2      L1   Te0/0/26      10.239.7.29     UP    27       00
            p2 = re.compile(
                r'^\s*(?P<system_id>\S+)\s+(?P<type>\S+)\s+(?P<interface>\S+)\s+(?P<ip_address>\S+)\s+(?P<state>(UP|DOWN)+)\s+(?P<holdtime>\S+)\s+(?P<circuit_id>\S+)\s*$')
            m = p2.match(line)
            if m:
                system_id = m.groupdict()['system_id']
                ret_dict.setdefault('isis', {}).setdefault(isis_name, {}).setdefault('neighbors',
                                                                                                {}).setdefault(
                    system_id, {})
                ret_dict['isis'][isis_name]['neighbors'][system_id]['type'] = m.groupdict()['type']
                ret_dict['isis'][isis_name]['neighbors'][system_id]['interface'] = m.groupdict()['interface']
                ret_dict['isis'][isis_name]['neighbors'][system_id]['ip_address'] = m.groupdict()[
                    'ip_address']
                ret_dict['isis'][isis_name]['neighbors'][system_id]['state'] = m.groupdict()['state']
                ret_dict['isis'][isis_name]['neighbors'][system_id]['holdtime'] = m.groupdict()['holdtime']
                ret_dict['isis'][isis_name]['neighbors'][system_id]['circuit_id'] = m.groupdict()[
                    'circuit_id']
                continue

        return ret_dict