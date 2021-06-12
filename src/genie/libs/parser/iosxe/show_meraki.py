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
                     'switch_num': int,
                     'pid': str,
                     'serial_number': str,
                     'meraki_sn': str,
                     'mac_addr': str,
                     'conversion_status': str, 
                     'current_mode': str   }, }, },
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
#        4       C9300-48TX FJC2311T0AJ N/A             5cbc.4812.3479   N/A                C9K-C


        p1 = re.compile ( r'^(?P<switch_num>\d+)(?P<pid>\s+\w+\d+\-\d+\w+)(?P<serial_number>\s+[a-zA-Z0-9]+)(?P<meraki_sn>\s+[a-zA-Z0-9\/\-]*)(?P<mac_addr>\s+[a-zA-Z0-9\.]*)(?P<conversion_status>\s+[a-zA-Z0-9\s\/\-]+)(?P<current_mode>\s+[a-zA-Z0-9\-]+)')

        parsed_dict = {}
        switch_id_index = 1
        for line in out.splitlines():
            line = line.strip()
            result = p1.match(line)
            device_dict = parsed_dict.setdefault('meraki', {}) \
                        .setdefault('switch', {}).setdefault(switch_id_index, {})

            if result:

                switch_id_index += 1

                group = result.groupdict()
                device_dict['switch_num'] = int(group['switch_num'])
                device_dict['pid'] = group['pid'].strip()
                device_dict['serial_number'] = group['serial_number'].strip()
                device_dict['meraki_sn'] = group['meraki_sn'].strip()
                device_dict['mac_addr'] = group['mac_addr'].strip()
                device_dict['conversion_status'] = group['conversion_status'].strip()
                device_dict['current_mode'] = group['current_mode'].strip()
                continue

        return parsed_dict

