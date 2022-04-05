'''show_cable_tdr_interface.py
IOSXE parser for the following show command
	* show cable tdr interface {interface}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, ListOf, \
        Optional, And, Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common

# =================================================
# Schema for:
#   * 'show cable tdr interface {interface}'
# ==================================================
class ShowCableTdrIntSchema(MetaParser):
    schema = {
        Any(): {
            'interface': str,
            'speed': str,
            'date': str,
            'time': str,
            'pairs': {
                Any() : {
                    'length': int,
                    'tolerance': int,
                    'remote_pair': str,
                    'status': str,
               }
           }
        }
    }

class ShowCableTdrInterface(ShowCableTdrIntSchema):
    """
    Parser for:
            show cable tdr interface {interface}
    """

    cli_command = 'show cable tdr interface {interface}'

    def cli(self, interface=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        # initial return dictionary
        tdr_dict = {}

        # TDR test last run on: January 09 16:19:29
        p1 = re.compile(r'^TDR +test +last +run +on: +(?P<date>\w+ \d+) +(?P<time>\d+:\d+:\d+)$')

        # Gi1/0/1   auto  Pair A     0    +/- 1  meters N/A         Open
        p2 = re.compile(r'^(?P<interface>\w\w\d\/\d\/\d+)\s+(?P<speed>auto|100M|1000M)'
                '\s+Pair (?P<local_pair>A)     (?P<pair_length>\d+)\s+\+\/\- (?P<pair_tolerance>\d+)\s+meters '
                '(?P<pair_remote>N\/A|Pair A|Pair B|Pair C|Pair D)\s+(?P<pair_status>.*$)')

        #                 Pair B     1    +/- 1  meters N/A         Open
        #                 Pair C     0    +/- 1  meters N/A         Open
        #                 Pair D     1    +/- 1  meters N/A         Open
        p3 = re.compile(r'Pair +(?P<local_pair>B|C|D)\s+(?P<pair_length>\d+)\s+\+\/\- (?P<pair_tolerance>\d+)\s+meters'
                ' +(?P<pair_remote>N\/A|Pair A|Pair B|Pair C|Pair D)\s+(?P<pair_status>.*$)')

        for line in output.splitlines():
            line = line.strip()

            # TDR test last run on: January 09 16:19:29
            m = p1.match(line)
            if m:
                date_performed = m.groupdict()['date']
                time_performed = m.groupdict()['time']
                continue

            # Gi1/0/1   auto  Pair A     0    +/- 1  meters N/A         Open
            m = p2.match(line)
            if m:
                interface = m.groupdict()['interface']
                group = m.groupdict()
                tdr_dict[interface] = {}
                tdr_dict[interface]['interface'] = m.groupdict()['interface']
                tdr_dict[interface]['speed'] = m.groupdict()['speed']

                tdr_dict[interface]['date'] = date_performed
                tdr_dict[interface]['time'] = time_performed

                tdr_dict[interface].setdefault('pairs', {})

                pair = m.groupdict()['local_pair']
                tdr_dict[interface]['pairs'][pair] = {}
                tdr_dict[interface]['pairs'][pair]['length'] = int(m.groupdict()['pair_length'])
                tdr_dict[interface]['pairs'][pair]['tolerance'] = int(m.groupdict()['pair_tolerance'])
                tdr_dict[interface]['pairs'][pair]['remote_pair'] = m.groupdict()['pair_remote']
                tdr_dict[interface]['pairs'][pair]['status'] = m.groupdict()['pair_status']
                continue

            #                 Pair B     1    +/- 1  meters N/A         Open
            #                 Pair C     0    +/- 1  meters N/A         Open
            #                 Pair D     1    +/- 1  meters N/A         Open
            m = p3.match(line)
            if m:
                pair = m.groupdict()['local_pair']
                tdr_dict[interface]['pairs'][pair] = {}
                tdr_dict[interface]['pairs'][pair]['length'] = int(m.groupdict()['pair_length'])
                tdr_dict[interface]['pairs'][pair]['tolerance'] = int(m.groupdict()['pair_tolerance'])
                tdr_dict[interface]['pairs'][pair]['remote_pair'] = m.groupdict()['pair_remote']
                tdr_dict[interface]['pairs'][pair]['status'] = m.groupdict()['pair_status']
                continue

        return(tdr_dict)
