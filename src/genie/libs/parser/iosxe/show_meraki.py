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
from genie.metaparser.util.schemaengine import (Schema, Any, Optional, Or, And, Default, Use)

# import parser utils
from genie.libs.parser.utils.common import Common


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

# ================
# Schema for:
#  * 'show meraki compatibility'
# ================
class ShowMerakiCompatibilitySchema(MetaParser):
    "Schema for meraki compatibility"
    schema = {
        'compatibility_check': {
            Any(): {
                'status':str
            },
        },
        'switch': {
            Any():{
                'skus':str,
                'compatibility': str,
                'bootloader_version': str,
                'compatibility':str
            },  
        },
        'compatible_skus': {
            'all_skus':list
        },
        'compatible_nms': {
            'all_nms':list
        },
    }
# ================
# Parser for:
#  * 'show meraki compatibility'
# ===============

class ShowMerakiCompatibility(ShowMerakiCompatibilitySchema):
    cli_command = 'show meraki compatibility'

    def cli(self,output=None):
        if output is None:
            #get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output
        meraki_dict = {}

        #Boot Mode INSTALL - Compatible
        #Stackwise Virtual Disabled - Compatible    
        p1 = re.compile(r'^(?!Compatibility Check )(?P<name>[\w+\s]+) *'
                         '(?P<status>[\-+\s+\w]+)$')

        #1 C9300-48UN - Compatible 17.06.03 - Incompatible N/A

        p2 = re.compile(r'^(?P<switch_num>\d+) +'
                r'(?P<skus>(\w+\-+\w+)) +'
                r'(?P<compatibility>(\W+\w+\s)*)'
                r'(?P<bootloader_version>((\d+\.+\d+\.+\d+))*)')

        #Compatible SKUs: C9300-24P, C9300-24T, C9300-24U, C9300-24UX, C9300-48P, C9300-48T, C9300-48U, C9300-48UN, C9300-48UX

        p3 = re.compile(r'^Compatible SKUs:\s(?P<compatible_skus>(\w+.*))$')

        #Compatible NMs : C9300-NM-2Q, C9300-NM-8X

        p4 = re.compile(r'^Compatible NMs\s:\s(?P<compatible_nms>(\w+.*))$')
        for line in out.splitlines():
            line = line.strip()
           
            #Boot Mode INSTALL - Compatible
            #Stackwise Virtual Disabled - Compatible   
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group.pop('name')
                name_dict = meraki_dict.setdefault('compatibility_check', {}).setdefault(name, {})
                name_dict.update(
                    {k:v for k, v in group.items()})
                continue
            #1 C9300-48UN - Compatible 17.06.03 - Incompatible N/A
            m = p2.match(line)
            if m:
                group = m.groupdict()
                num = group.pop('switch_num')
                switch_dict = meraki_dict.setdefault('switch', {}).setdefault(num, {})
                switch_dict.update(
                    {k:v for k, v in group.items()})
                continue
            
            #Compatible SKUs: C9300-24P, C9300-24T, C9300-24U, C9300-24UX, C9300-48P, C9300-48T, C9300-48U, C9300-48UN, C9300-48UX
            m = p3.match(line)
            if m:
                group = m.groupdict()
                compatible_skus_dict = meraki_dict.setdefault('compatible_skus', {})
                all_skus_dict = compatible_skus_dict.setdefault('all_skus', [])
                for x in group['compatible_skus'].split(', '):
                    all_skus_dict.append(x)
                continue
            
            #Compatible NMs : C9300-NM-2Q, C9300-NM-8X
            m = p4.match(line)
            if m:
                group = m.groupdict()
                compatible_nms_dict = meraki_dict.setdefault('compatible_nms', {})
                all_nms_dict = compatible_nms_dict.setdefault('all_nms', [])
                for x in group['compatible_nms'].split(', '):
                    all_nms_dict.append(x)
                continue

        return meraki_dict
