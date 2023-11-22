'''
IOSXE parsers for the following show commands: 
show_beacon_all.py
'''
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any,Optional


class ShowBeaconAllSchema(MetaParser):
    """
    Schema for show beacon all
    """
    schema = {
        'switch': {
            Any(): {
                'beacon_status': str,
            },
        },
        Optional('power_supply'): {
            Any():{
                'power_supply_beacon_status': str,
            },
        },
        Optional('fantray_beacon_status'): str
    }

class ShowBeaconAll(ShowBeaconAllSchema):
    """ Parser for Schema for show beacon all status"""

    cli_command = "show beacon all"

    def cli(self,output=None): 
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}

        # Slot#           Beacon Status
        # ---------------------------------
        # 1                  OFF
        # *2                  OFF

        p1_0 = re.compile(r'^\w+#\s+Beacon\s+Status$')
        p1_1 = re.compile('^[*]?(?P<switch_number>\d+)\s+(?P<beacon_status>\w+)$')

        # Power-Supply#   Beacon Status
        # ---------------------------------
         # 1                  OFF
        p2_0 = re.compile(r'Power-Supply#\s+Beacon\s+Status$')
        p2_1 = re.compile('^(?P<power_supply>\d+)\s+(?P<power_supply_beacon_status>\w+)$')

        #FANTRAY BEACON:     OFF
        p3 = re.compile('^FANTRAY BEACON:\s+(?P<fantray_beacon_status>\w+)$')


        for line in output.splitlines():
            line = line.strip()

            # Slot#           Beacon Status
            # ---------------------------------
            # 1                  OFF
            # *2                  OFF
            m = p1_0.match(line)
            if m:
                active_table = 1
                continue

            m = p2_0.match(line)
            if m:
                active_table = 2
                continue

            m = p1_1.match(line)

            if m and active_table == 1:
                group = m.groupdict()
                switch_dict = ret_dict.setdefault('switch', {}).setdefault(m.groupdict()['switch_number'], {})
                switch_dict['beacon_status'] = m.groupdict()['beacon_status']
                continue

            # Power-Supply#   Beacon Status
            # ---------------------------------
             # 1                  OFF
            m = p2_1.match(line)
            if m and active_table == 2:
               group = m.groupdict()
               power_dict = ret_dict.setdefault('power_supply',{})
               power_supply_dict = power_dict.setdefault(int(group['power_supply']),{})
               power_supply_dict.update({  
                    'power_supply_beacon_status' : str(group['power_supply_beacon_status']),
                })

               continue


            m = p3.match(line)
            if m:
               group = m.groupdict()
               ret_dict.update({'fantray_beacon_status': group['fantray_beacon_status']})
               continue


        return ret_dict        
