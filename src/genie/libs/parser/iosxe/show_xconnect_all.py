"""show_xconnect_all.py

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


class ShowXconnectAllSchema(MetaParser):
    """Schema for show xconnect all"""
    schema = {
        'interface': {
            Any(): {
                'state': {
                    Any(): {
                        'Segment 1 State': str,
                        'Segment 2': str,
                        Optional('Segment 2 State'): str,
                        },
                     }
                }
            }
        }

class ShowXconnectAll(ShowXconnectAllSchema):
    """Parser for show xconnect all"""

    cli_command = 'show xconnect all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # IA pri   ac Gi0/0/1:10(Ethernet)         DN mpls 10.239.6.2:684955608         DN
            p1 = re.compile(
                r'^\s*(?P<xc>\S+)\s+(?P<st>\S+)\s+(?P<segment_1>(.*\)))\s+(?P<s1>\S+)\s+(?P<segment_2>\S+[^\S]\S+)\s+(?P<s2>\S+)\s*$')
            m = p1.match(line)

            if m:
                segment_1 = m.groupdict()['segment_1']
                xc_state = m.groupdict()['st']

                ret_dict.setdefault('interface', {}).setdefault(segment_1, {}).setdefault('state',
                                                                                                        {}).setdefault(
                    xc_state, {})

                for key in ret_dict['interface'][segment_1]['state']:
                    if key == 'pri':
                        ret_dict['interface'][segment_1]['state'][xc_state]['Segment 1 State'] = \
                        m.groupdict()['s1']
                        ret_dict['interface'][segment_1]['state'][xc_state]['Segment 2'] = m.groupdict()[
                            'segment_2']
                        ret_dict['interface'][segment_1]['state'][xc_state]['Segment 2 State'] = \
                        m.groupdict()['s2']

                    elif key == 'sec':
                        ret_dict['interface'][segment_1]['state'][xc_state]['Segment 1 State'] = \
                        m.groupdict()['s1']
                        ret_dict['interface'][segment_1]['state'][xc_state]['Segment 2'] = m.groupdict()[
                            'segment_2']
                        ret_dict['interface'][segment_1]['state'][xc_state]['Segment 2 State'] = \
                        m.groupdict()['s2']
                continue

        return ret_dict