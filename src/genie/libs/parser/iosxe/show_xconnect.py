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
        'segment_1': {
            Any(): {
                's1': str,
                'segment_2': {
                    Any(): {
                        's2': str,
                        'xc': str,
                        'st': str,
                    }
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
            # UP pri mpls 2.2.2.2:888                  UP   ac Gi3:9(Ethernet)              UP
            # -- pri  vfi sample-vfi                   UP unkn Invalid Segment              --
            # UP pri   bd 300                          UP  vfi sample-vfi                   UP
            p1 = re.compile(
                r'^\s*(?P<xc>(UP|DN|AD|IA|SB|HS|RV|NH|\-\-))\s+(?P<st>(pri|sec))\s+(?P<segment1>.*)\s+(?P<s1>(UP|DN|AD|IA|SB|HS|RV|NH|\-\-))\s+(?P<segment2>.*)\s+(?P<s2>(UP|DN|AD|IA|SB|HS|RV|NH|\-\-))')
            m = p1.match(line)

            if m:
                xc, st, segment_1, s1, segment_2, s2 = m.groupdict().values()
                segment_1 = segment_1.rstrip()
                segment_2 = segment_2.rstrip()
                ret_dict.setdefault('segment_1', {}).setdefault(segment_1, {}).setdefault('segment_2', {}).setdefault(segment_2, {})
                ret_dict['segment_1'][segment_1]['s1'] = s1
                ret_dict['segment_1'][segment_1]['segment_2'][segment_2]['s2'] = s2
                ret_dict['segment_1'][segment_1]['segment_2'][segment_2]['xc'] = xc
                ret_dict['segment_1'][segment_1]['segment_2'][segment_2]['st'] = st

        return ret_dict