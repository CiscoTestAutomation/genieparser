'''  show_meraki.py

IOSXE parsers for the following show command:

    * 'show meraki'

'''

# Python
import re

# Metaparser
from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowMerakiSchema(MetaParser):

    """ Schema for:
        * 'show meraki'
        CLI:

    	                   Serial                      MAC             Conversion         Current    

	Switch#.  PID      Number      Meraki SN       Addr             Status             Mode           
 	---------------------------------------------------------------------------------------

	1       C9300-24T  FJC2311T0DA Q5EE-DJYN-CRGR  4cbc.4812.3550   Registered         C9K-C

	2       C9300-24U  FJC1527A0BC N/A             4cbc.4812.2881   ACT2 write failed  C9K-C

	3       C9300-48UX FJC2317T0DT Q3EA-AZYP-WDFH  4cbc.4812.2501   Registered         C9K-C         

	4       C9300-48TX FJC2311T0AJ N/A             5cbc.4812.3479   Timeout            C9K-C

    """ 

    schema = {
        'meraki':
            {Optional('switch'):
                {Any():
                     {
                     Optional('switch_no'): str,
                     Optional('PID'): str,
                     Optional('Serial_Number'): str,
                     Optional('Meraki_SN'): str,
                     Optional('Mac_Addr'): str,
                     Optional('Conversion_Status'): str, 
                     Optional('Current_Mode'): str   }, }, },
    }


# ================================
# Parser for 'show meraki'
# ================================
class ShowMeraki(ShowMerakiSchema):

    cli_command = 'show meraki'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


#        1       C9300-24T  FJC2311T0DA Q5EE-DJYN-CRGR  4cbc.4812.3550   Registered         C9K-C

#        2       C9300-24U  FJC1527A0BC N/A             4cbc.4812.2881   ACT2 write failed  C9K-C

#        3       C9300-48UX FJC2317T0DT Q3EA-AZYP-WDFH  4cbc.4812.2501   Registered         C9K-C

#        4       C9300-48TX FJC2311T0AJ N/A             5cbc.4812.3479   Timeout            C9K-C



        p1 = re.compile ( r'^(?P<switch_no>\d+)(?P<PID>\s+\w+\d+\-\d+\w+)(?P<Serial_Number>\s+[a-zA-Z0-9]+)(?P<Meraki_SN>\s+[a-zA-Z0-9\/\-]+)(?P<Mac_Addr>\s+[a-zA-Z0-9\.]+)(?P<Conversion_Status>\s+[a-zA-Z0-9\s]+)(?P<Current_Mode>\s+[a-zA-Z0-9\-]+)')

        parsed_dict = {}
        switch_id_index = 1
        for line in out.splitlines():
            line = line.strip()
            print("result after splitting the line :",line)
            result = p1.match(line)
            device_dict = parsed_dict.setdefault('meraki', {}) \
                        .setdefault('switch', {}).setdefault(switch_id_index, {})

            if result:

                switch_id_index += 1

                group = result.groupdict()
                device_dict['switch_no'] = group['switch_no'].strip()
                device_dict['PID'] = group['PID'].strip()
                device_dict['Serial_Number'] = group['Serial_Number'].strip()
                device_dict['Meraki_SN'] = group['Meraki_SN'].strip()
                device_dict['Mac_Addr'] = group['Mac_Addr'].strip()
                device_dict['Conversion_Status'] = group['Conversion_Status'].strip()
                device_dict['Current_Mode'] = group['Current_Mode'].strip()
                continue

        return parsed_dict

