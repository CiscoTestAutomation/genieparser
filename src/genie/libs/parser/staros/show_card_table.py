"""starOS implementation of show_card_table.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowCardTableSchema(MetaParser):
    """Schema for show card table"""

    schema = {
        'card_table': {
            Any():{
                'TYPE': str,
                'STATE': str,
                'SPOF': str
            },
        }
    }


class ShowCardTable(ShowCardTableSchema):
    """Parser for show card table"""

    cli_command = 'show card table'

    """
Slot         Card Type                               Oper State     SPOF  Attach
-----------  --------------------------------------  -------------  ----  ------
 1: DPC      Data Processing Card 2                  Active         No          
 2: DPC      Data Processing Card 2                  Active         No          
 3: DPC      Data Processing Card 2                  Active         No          
 4: DPC      Data Processing Card 2                  Standby        -           
 5: MMIO     Management & 20x10Gb I/O Card           Active         No          
 6: MMIO     Management & 20x10Gb I/O Card           Standby        -           
 7: DPC      Data Processing Card 2                  Active         No          
 8: DPC      Data Processing Card 2                  Active         No          
 9: DPC      Data Processing Card 2                  Active         No          
10: DPC      Data Processing Card 2                  Active         No          
11: SSC      System Status Card                      Active         No          
12: SSC      System Status Card                      Active         No          
13: FSC      None                                    -              -           
14: FSC      Fabric & 1x400GB Storage Card           Active         No          
15: FSC      Fabric & 1x400GB Storage Card           Active         No          
16: FSC      Fabric & 1x400GB Storage Card           Active         No          
17: FSC      Fabric & 1x400GB Storage Card           Active         No   
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        card_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'((?P<slot>\d+):\s\w+\s+(?P<card_type>.*?\  )\s+(?P<state>\w+|.)\s+(?P<spof>\w+|.))')
        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'card_table' not in card_dict:
                    result_dict = card_dict.setdefault('card_table',{})
                slot = m.groupdict()['slot']
                card_type = m.groupdict()['card_type']
                state = m.groupdict()['state']
                spof = m.groupdict()['spof']

                result_dict[slot] = {}
                result_dict[slot]['TYPE'] = card_type
                result_dict[slot]['STATE'] = state
                result_dict[slot]['SPOF'] = spof
                continue

        return card_dict