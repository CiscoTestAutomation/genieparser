'''show_cable_tdr_interface.py
IOSXE parser for the following show command
	* show cable tdr interface {interface}
'''

# Python
import re
# import unittest

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
            Optional('interface'): str,
            Optional('speed'): str,
            Optional('date'): str,
            Optional('time'): str,
            'pairs': {
                Any() : {
                    Optional('length'): int,
                    Optional('tolerance'): int,
                    Optional('remote_pair'): str,
                    Optional('status'): str,
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
            if interface:
                output = self.device.execute(self.cli_command.format(interface=interface))
        else:
            output = output

        # initial return dictionary
        tdr_dict = {}

        # TDR test last run on: January 09 16:19:29
        #
        # Interface Speed Local pair Pair length        Remote pair Pair status
        # --------- ----- ---------- ------------------ ----------- --------------------
        # Gi1/0/1   auto  Pair A     0    +/- 1  meters N/A         Open
        #                 Pair B     1    +/- 1  meters N/A         Open
        #                 Pair C     0    +/- 1  meters N/A         Open
        #                 Pair D     1    +/- 1  meters N/A         Open

        # TDR test last run on: January 09 16:19:29
        p1 = re.compile(r'^TDR +test +last +run +on: +(?P<date>\w+ \d+) +(?P<time>\d+:\d+:\d+)$')

        # Gi1/0/1   auto  Pair A     0    +/- 1  meters N/A         Open
        p2 = re.compile(r'^(?P<interface>\w\w\d\/\d\/\d+)\s+(?P<speed>auto|100M|1000M)'
                '\s+Pair A     (?P<pair_a_length>\d+)\s+\+\/\- (?P<pair_a_tolerance>\d+)\s+meters '
                '(?P<pair_a_remote>N\/A|Pair A|Pair B|Pair C|Pair D)\s+(?P<pair_a_status>.*$)')

        #                 Pair B     1    +/- 1  meters N/A         Open
        p3 = re.compile(r'Pair +B\s+(?P<pair_b_length>\d+)\s+\+\/\- (?P<pair_b_tolerance>\d+)\s+meters'
                ' +(?P<pair_b_remote>N\/A|Pair A|Pair B|Pair C|Pair D)\s+(?P<pair_b_status>.*$)')


        #                 Pair C     0    +/- 1  meters N/A         Open
        p4 = re.compile(r'Pair +C\s+(?P<pair_c_length>\d+)\s+\+\/\- (?P<pair_c_tolerance>\d+)\s+meters'
                ' +(?P<pair_c_remote>N\/A|Pair A|Pair B|Pair C|Pair D)\s+(?P<pair_c_status>.*$)')

        #                 Pair D     1    +/- 1  meters N/A         Open
        p5 = re.compile(r'Pair +D\s+(?P<pair_d_length>\d+)\s+\+\/\- (?P<pair_d_tolerance>\d+)\s+meters'
                ' +(?P<pair_d_remote>N\/A|Pair A|Pair B|Pair C|Pair D)\s+(?P<pair_d_status>.*$)')

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
                tdr_dict[interface] = {}
                tdr_dict[interface]['interface'] = m.groupdict()['interface']
                tdr_dict[interface]['speed'] = m.groupdict()['speed']

                tdr_dict[interface]['date'] = date_performed
                tdr_dict[interface]['time'] = time_performed

                tdr_dict[interface]['pair_a'] = {}
                tdr_dict[interface]['pair_a']['length'] = int(m.groupdict()['pair_a_length'])
                tdr_dict[interface]['pair_a']['tolerance'] = int(m.groupdict()['pair_a_tolerance'])
                tdr_dict[interface]['pair_a']['remote_pair'] = m.groupdict()['pair_a_remote']
                tdr_dict[interface]['pair_a']['status'] = m.groupdict()['pair_a_status']

                continue

            #                 Pair B     1    +/- 1  meters N/A         Open
            m = p3.match(line)
            if m:
                tdr_dict[interface]['pair_b'] = {}
                tdr_dict[interface]['pair_b']['length'] = int(m.groupdict()['pair_b_length'])
                tdr_dict[interface]['pair_b']['tolerance'] = int(m.groupdict()['pair_b_tolerance'])
                tdr_dict[interface]['pair_b']['remote_pair'] = m.groupdict()['pair_b_remote']
                tdr_dict[interface]['pair_b']['status'] = m.groupdict()['pair_b_status']
                continue

            #                 Pair C     0    +/- 1  meters N/A         Open
            m = p4.match(line)
            if m:
                tdr_dict[interface]['pair_c'] = {}
                tdr_dict[interface]['pair_c']['length'] = int(m.groupdict()['pair_c_length'])
                tdr_dict[interface]['pair_c']['tolerance'] = int(m.groupdict()['pair_c_tolerance'])
                tdr_dict[interface]['pair_c']['remote_pair'] = m.groupdict()['pair_c_remote']
                tdr_dict[interface]['pair_c']['status'] = m.groupdict()['pair_c_status']
                continue

            m = p5.match(line)
            if m:
                tdr_dict[interface]['pair_d'] = {}
                tdr_dict[interface]['pair_d']['length'] = int(m.groupdict()['pair_d_length'])
                tdr_dict[interface]['pair_d']['tolerance'] = int(m.groupdict()['pair_d_tolerance'])
                tdr_dict[interface]['pair_d']['remote_pair'] = m.groupdict()['pair_d_remote']
                tdr_dict[interface]['pair_d']['status'] = m.groupdict()['pair_d_status']
                continue

        return(tdr_dict)
