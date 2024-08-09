"""starOS implementation of show port table.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowPortSchema(MetaParser):
    """Schema for show port table"""

    schema = {
        'port_table': {
            Any(): {
                'Role': str,
                'Type': str,
                'Admin': str,
                'Operation': str,
                'Link': str,
                'State': str,
                'Pair': str,
                'Redundant': str
            },
        }    
    }


class ShowPort(ShowPortSchema):
    """Parser for show port table"""

    cli_command = 'show port table'

    """
Port  Role Type                      Admin    Oper Link State    Pair  Redundant
----- ---- ------------------------  -------- ---- ---- -------  ----- ---------
5/1  Mgmt 1000 Ethernet             Enabled  Up   Up   Active    6/1  L2 Link  
5/2  Mgmt 1000 Ethernet             Disabled Down Down Active    6/2  L2 Link  
5/3  Mgmt RS232 Serial Console      Enabled  Down Down Active    6/3  L2 Link  
5/10 Srvc 10G Ethernet              Enabled  -    Up   -         6/10 LA+  5/10
5/11 Srvc 10G Ethernet              Enabled  -    Up   -         6/11 LA+  5/11
5/12 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/12 LA+  5/10
5/13 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/13 LA+  5/11
5/14 Srvc 10G Ethernet              Disabled Down Down Active    6/14 L2 Link  
5/15 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/15 LA+  5/10
5/16 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/16 LA+  5/11
5/17 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/17 LA+  5/10
5/18 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/18 LA+  5/11
5/19 Srvc 10G Ethernet              Disabled Down Down Active    6/19 L2 Link  
5/20 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/20 LA+  5/10
5/21 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/21 LA+  5/11
5/22 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/22 LA+  5/10
5/23 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/23 LA+  5/11
5/24 Srvc 10G Ethernet              Disabled Down Down Active    6/24 L2 Link  
5/25 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/25 LA+  5/10
5/26 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/26 LA+  5/11
5/27 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/27 LA+  5/10
5/28 Srvc 10G Ethernet              Enabled  Up   Up   Active    6/28 LA+  5/11
5/29 Srvc 10G Ethernet              Disabled Down Down Active    6/29 L2 Link  
6/1  Mgmt 1000 Ethernet             Enabled  Down Up   Standby   5/1  L2 Link  
6/2  Mgmt 1000 Ethernet             Disabled Down Down Standby   5/2  L2 Link  
6/3  Mgmt RS232 Serial Console      Enabled  Down Down Standby   5/3  L2 Link  
6/10 Srvc 10G Ethernet              Enabled  -    Up   -         5/10 LA+  5/10
6/11 Srvc 10G Ethernet              Enabled  -    Up   -         5/11 LA+  5/11
6/12 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/12 LA+  5/10
6/13 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/13 LA+  5/11
6/14 Srvc 10G Ethernet              Disabled Down Down Standby   5/14 L2 Link  
6/15 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/15 LA+  5/10
6/16 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/16 LA+  5/11
6/17 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/17 LA+  5/10
6/18 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/18 LA+  5/11
6/19 Srvc 10G Ethernet              Disabled Down Down Standby   5/19 L2 Link  
6/20 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/20 LA+  5/10
6/21 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/21 LA+  5/11
6/22 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/22 LA+  5/10
6/23 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/23 LA+  5/11
6/24 Srvc 10G Ethernet              Disabled Down Down Standby   5/24 L2 Link  
6/25 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/25 LA+  5/10
6/26 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/26 LA+  5/11
6/27 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/27 LA+  5/10
6/28 Srvc 10G Ethernet              Enabled  Up   Up   Active    5/28 LA+  5/11   
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        port_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'^(?P<port>\d+.\d+)\s+(?P<role>\w+)\s(?P<type>.*?)\s{3}\s+(?P<admin>\w+)\s+(?P<oper>\w+|-)\s+(?P<link>\w+|-)\s+(?P<state>\w+|-)\s+(?P<pair>\d+.\d+)\s+(?P<redundant>.*?)\s')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'port_table' not in port_dict:
                    result_dict = port_dict.setdefault('port_table',{})
                port = m.groupdict()['port']
                role = m.groupdict()['role']
                type = m.groupdict()['type']
                admin = m.groupdict()['admin']
                oper = m.groupdict()['oper']
                link = m.groupdict()['link']
                state = m.groupdict()['state']
                pair = m.groupdict()['pair']
                redundant = m.groupdict()['redundant']
                result_dict[port] = {}
                result_dict[port]['Role'] = role
                result_dict[port]['Type'] = type
                result_dict[port]['Admin'] = admin
                result_dict[port]['Operation'] = oper
                result_dict[port]['Link'] = link
                result_dict[port]['State'] = state   
                result_dict[port]['Pair'] = pair
                result_dict[port]['Redundant'] = redundant              
                continue

        return port_dict