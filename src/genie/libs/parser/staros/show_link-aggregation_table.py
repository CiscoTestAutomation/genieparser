"""starOS implementation of show_link-aggregation_table.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowTableSchema(MetaParser):
    """Schema for show link-aggregation table"""

    schema = {
        'link-aggregation_table': {
            Any(): {
                'GRP': str,
                'TYPES': str,
                'ADMIN': str,
                'OPER': str,
                'LINK': str,
                'STATE': str,
                'PAIR': str,
                'REDUNDANT': str
            },
        }    
    }


class ShowTable(ShowTableSchema):
    """Parser for show link-aggregation table"""

    cli_command = 'show link-aggregation table'

    """
    Grp  Port   Type                      Admin    Oper Link State    Pair  Redundant
    ---- -----  ------------------------  -------- ---- ---- -------  ----- ---------
    232   5/10  10G Ethernet              Enabled  -    Up   -         6/10 LA+  5/10
    232   5/12  10G Ethernet              Enabled  Up   Up   Active    6/12 LA+  5/10
    232   5/15  10G Ethernet              Enabled  Up   Up   Active    6/15 LA+  5/10
    232   5/17  10G Ethernet              Enabled  Up   Up   Active    6/17 LA+  5/10
    232   5/20  10G Ethernet              Enabled  Up   Up   Active    6/20 LA+  5/10
    232   5/22  10G Ethernet              Enabled  Up   Up   Active    6/22 LA+  5/10
    232   5/25  10G Ethernet              Enabled  Up   Up   Active    6/25 LA+  5/10
    232   5/27  10G Ethernet              Enabled  Up   Up   Active    6/27 LA+  5/10
    232   6/10  10G Ethernet              Enabled  -    Up   -         5/10 LA+  5/10
    232   6/12  10G Ethernet              Enabled  Up   Up   Active    5/12 LA+  5/10
    232   6/15  10G Ethernet              Enabled  Up   Up   Active    5/15 LA+  5/10
    232   6/17  10G Ethernet              Enabled  Up   Up   Active    5/17 LA+  5/10
    232   6/20  10G Ethernet              Enabled  Up   Up   Active    5/20 LA+  5/10
    232   6/22  10G Ethernet              Enabled  Up   Up   Active    5/22 LA+  5/10
    232   6/25  10G Ethernet              Enabled  Up   Up   Active    5/25 LA+  5/10
    232   6/27  10G Ethernet              Enabled  Up   Up   Active    5/27 LA+  5/10
    233   5/11  10G Ethernet              Enabled  -    Up   -         6/11 LA+  5/11
    233   5/13  10G Ethernet              Enabled  Up   Up   Active    6/13 LA+  5/11
    233   5/16  10G Ethernet              Enabled  Up   Up   Active    6/16 LA+  5/11
    233   5/18  10G Ethernet              Enabled  Up   Up   Active    6/18 LA+  5/11
    233   5/21  10G Ethernet              Enabled  Up   Up   Active    6/21 LA+  5/11
    233   5/23  10G Ethernet              Enabled  Up   Up   Active    6/23 LA+  5/11
    233   5/26  10G Ethernet              Enabled  Up   Up   Active    6/26 LA+  5/11
    233   5/28  10G Ethernet              Enabled  Up   Up   Active    6/28 LA+  5/11
    233   6/11  10G Ethernet              Enabled  -    Up   -         5/11 LA+  5/11
    233   6/13  10G Ethernet              Enabled  Up   Up   Active    5/13 LA+  5/11
    233   6/16  10G Ethernet              Enabled  Up   Up   Active    5/16 LA+  5/11
    233   6/18  10G Ethernet              Enabled  Up   Up   Active    5/18 LA+  5/11
    233   6/21  10G Ethernet              Enabled  Up   Up   Active    5/21 LA+  5/11
    233   6/23  10G Ethernet              Enabled  Up   Up   Active    5/23 LA+  5/11
    233   6/26  10G Ethernet              Enabled  Up   Up   Active    5/26 LA+  5/11
    233   6/28  10G Ethernet              Enabled  Up   Up   Active    5/28 LA+  5/11            
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        recovery_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'(?P<grp>^\d..)\s+(?P<port>\d.\d.)\s+(?P<types>\w+\s\w+)\s+(?P<admin>\w+)\s+(?P<oper>\S+)\s+(?P<link>\S+)\s+(?P<state>\S+)\s+(?P<pair>\d.\d.)\s+(?P<redundant>\w+.\s+\d.\d.)')
        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'link-aggregation_table' not in recovery_dict:
                    result_dict = recovery_dict.setdefault('link-aggregation_table',{})
                grp = m.groupdict()['grp']
                port = m.groupdict()['port']
                types = m.groupdict()['types']
                admin = m.groupdict()['admin']
                oper = m.groupdict()['oper']
                link = m.groupdict()['link']
                state = m.groupdict()['state']
                pair = m.groupdict()['pair']
                redundant = m.groupdict()['redundant']
                result_dict[port] = {}
                result_dict[port]['GRP'] = grp
                result_dict[port]['TYPES'] = types
                result_dict[port]['ADMIN'] = admin
                result_dict[port]['OPER'] = oper
                result_dict[port]['LINK'] = link
                result_dict[port]['STATE'] = state 
                result_dict[port]['PAIR'] = pair   
                result_dict[port]['REDUNDANT'] = redundant      
                continue

        return recovery_dict