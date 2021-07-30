'''  show_meraki.py

IOSXE parsers for the following show command:

    * 'show meraki'
    * 'show meraki switch {switch}'

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowMerakiSchema(MetaParser):
    """ Schema for:
        * 'show meraki'
        * 'show meraki switch {switch}'
    """ 

    schema = {
        'meraki': {
            'switch': {
                Any(): {
                    'switch_num': int,
                    'pid': str,
                    'serial_number': str,
                    'meraki_sn': str,
                    'mac_addr': str,
                    'conversion_status': str, 
                    'current_mode': str   
                }, 
            }, 
        },
    }


class ShowMeraki(ShowMerakiSchema):
    '''Parser for:
        * 'show meraki'
        * 'show meraki switch {switch}'
    '''

    cli_command = ['show meraki', 'show meraki switch {switch}']

    def cli(self, switch = '',output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # 1       C9300-24T  FJC2311T0DA Q5EE-DJYN-CRGR  4cbc.4812.3550   Registered         C9K-C
        # 2       C9300-24U  FJC1527A0BC N/A             4cbc.4812.2881   ACT2 write failed  C9K-C
        # 3       C9300-48UX FJC2317T0DT Q3EA-AZYP-WDFH  4cbc.4812.2501   Registered         C9K-C
        # 4       C9300-48TX FJC2311T0AJ N/A             5cbc.4812.3479   N/A                C9K-C
        p1 = re.compile(r'^(?P<switch_num>\d+)\s+(?P<pid>[\w-]+)\s+(?P<serial_number>[\w]+)\s+(?P<meraki_sn>[\w\/-]+)\s+(?P<mac_addr>[\w\.]+)\s+(?P<conversion_status>[\w\s\/-]+)\s+(?P<current_mode>[\w\-]+)$')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 1       C9300-24T  FJC2311T0DA Q5EE-DJYN-CRGR  4cbc.4812.3550   Registered         C9K-C
            # 2       C9300-24U  FJC1527A0BC N/A             4cbc.4812.2881   ACT2 write failed  C9K-C
            # 3       C9300-48UX FJC2317T0DT Q3EA-AZYP-WDFH  4cbc.4812.2501   Registered         C9K-C
            # 4       C9300-48TX FJC2311T0AJ N/A             5cbc.4812.3479   N/A                C9K-C
            m = p1.match(line)
            if m:
                group = m.groupdict()
                device_dict = parsed_dict.setdefault('meraki', {}) \
                    .setdefault('switch', {}).setdefault(group['switch_num'], {})
                device_dict['switch_num'] = int(group['switch_num'])
                device_dict['pid'] = group['pid']
                device_dict['serial_number'] = group['serial_number']
                device_dict['meraki_sn'] = group['meraki_sn']
                device_dict['mac_addr'] = group['mac_addr']
                device_dict['conversion_status'] = group['conversion_status'].strip()
                device_dict['current_mode'] = group['current_mode']

        return parsed_dict
