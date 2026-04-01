"""show_xconnect.py

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
            line = line.strip()

            # XC ST  Segment 1                         S1 Segment 2                         S2
            # ------+---------------------------------+--+---------------------------------+--
            # IA pri   ac Gi0/0/1:10(Ethernet)         DN mpls 10.239.6.2:684955608         DN
            # UP pri mpls 10.16.2.2:888                  UP   ac Gi3:9(Ethernet)              UP
            # -- pri  vfi sample-vfi                   UP unkn Invalid Segment              --
            # UP pri   bd 300                          UP  vfi sample-vfi                   UP
            p1 = re.compile(r'^(?P<xc>(UP|DN|AD|IA|SB|HS|RV|NH|\-\-))\s+(?P<st>(pri|sec))\s+(?P<segment1>.*)\s+(?P<s1>(UP|DN|AD|IA|SB|HS|RV|NH|\-\-))\s+(?P<segment2>.*)\s+(?P<s2>(UP|DN|AD|IA|SB|HS|RV|NH|\-\-))')
            m = p1.match(line)
            if m:
                group = m.groupdict()
                segment_1 = group['segment1'].strip()
                segment_2 = group['segment2'].strip()
                # segment_1
                sg1_dict = ret_dict.setdefault('segment_1', {}).\
                                      setdefault(segment_1, {})
                sg1_dict['s1'] = group['s1'].strip()
                # segment_2
                sg2_dict = sg1_dict.setdefault('segment_2', {}).\
                                    setdefault(segment_2, {})
                sg2_dict['s2'] = group['s2'].strip()
                sg2_dict['xc'] = group['xc'].strip()
                sg2_dict['st'] = group['st'].strip()

        return ret_dict


class ShowXconnectInterfaceSchema(MetaParser):
    """Schema for show xconnect interface {interface}"""
    schema = {
        'segment_1': {
            Any(): {
                's1': str,
                Optional('segment_2'): {
                    Any(): {
                        's2': str,
                        'xc': str,
                        'st': str,
                    }
                }
            }
        }
    }


class ShowXconnectInterface(ShowXconnectInterfaceSchema):
    """Parser for show xconnect interface {interface}"""

    cli_command = 'show xconnect interface {interface}'

    def cli(self, interface, output=None):
        if output is None:
            cmd = self.cli_command.format(interface=interface)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Match xconnect entries with segment1 and segment2:
            # UP pri   ac Gi0/0/0:8(Ethernet)          UP l2tp 100.3.1.1:101                UP
            # Format: <XC_STATE> <PRIORITY> <SEGMENT1> <S1_STATE> <SEGMENT2> <S2_STATE>
            p1 = re.compile(r'^(?P<xc>(?:UP|DN|AD|IA|SB|HS|RV|NH|--))\s+'
                            r'(?P<st>(?:pri|sec))\s+'
                            r'(?P<segment1>.*?)\s+'
                            r'(?P<s1>(?:UP|DN|AD|IA|SB|HS|RV|NH|--))\s+'
                            r'(?P<segment2>.*?)\s+'
                            r'(?P<s2>(?:UP|DN|AD|IA|SB|HS|RV|NH|--))$')

            # Match xconnect entries with only segment1:
            # SB sec   bd 400                          
            # Format: <XC_STATE> <PRIORITY> <SEGMENT1>
            p2 = re.compile(r'^(?P<xc>(?:UP|DN|AD|IA|SB|HS|RV|NH|--))\s+'
                            r'(?P<st>(?:pri|sec))\s+'
                            r'(?P<segment1>.*?)\s*$')

            m1 = p1.match(line)
            m2 = p2.match(line)

            if m1:
                group = m1.groupdict()
                segment_1 = group['segment1'].strip()
                segment_2 = group['segment2'].strip()
                
                # segment_1
                sg1_dict = ret_dict.setdefault('segment_1', {}).\
                                      setdefault(segment_1, {})
                sg1_dict['s1'] = group['s1'].strip()
                
                # segment_2 
                sg2_dict = sg1_dict.setdefault('segment_2', {}).\
                                    setdefault(segment_2, {})
                sg2_dict['s2'] = group['s2'].strip()
                sg2_dict['xc'] = group['xc'].strip()
                sg2_dict['st'] = group['st'].strip()

            elif m2:
                group = m2.groupdict()
                segment_1 = group['segment1'].strip()
                
                # segment_1 only (no segment_2)
                sg1_dict = ret_dict.setdefault('segment_1', {}).\
                                      setdefault(segment_1, {})
                sg1_dict['s1'] = group['xc'].strip()  # For entries with no segment 2, s1 is the XC state

        return ret_dict
