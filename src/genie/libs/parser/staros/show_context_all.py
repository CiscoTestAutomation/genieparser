"""starOS implementation of show_card_table.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowContextAllSchema(MetaParser):
    """Schema for show card table"""

    schema = {
        'context_table':{
            Any():{
                'NAME': str,
                'STATE': str,
            },
        }
    }


class ShowContextAll(ShowContextAllSchema):
    """Parser for show context all"""

    cli_command = 'show context all'

    """
Context Name    ContextID    State     Description
--------------- --------- ----------   ----------------------- 
local           1            Active    
SAEGW           2            Active    
SGi_Internet    3            Active    
SGi_VAS         4            Active    
Ga              5            Active    
Gy              6            Active    
Gx              7            Active    
Lawful_Intercept 8            Active    
SGi_HPPTT       9            Active    
ePDG            10           Active     
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
        p0 = re.compile(r'(^(?P<name>\w+)\s+(?P<id>\d*)\s+(?P<state>\w+))')
        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'context_table' not in card_dict:
                    result_dict = card_dict.setdefault('context_table',{})
                name = m.groupdict()['name']
                idnum = m.groupdict()['id']
                state = m.groupdict()['state']

                result_dict[idnum] = {}
                result_dict[idnum]['NAME'] = name
                result_dict[idnum]['STATE'] = state
                continue

        return card_dict