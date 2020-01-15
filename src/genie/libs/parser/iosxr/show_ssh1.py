# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowSSHHistorySchema(MetaParser):
    #Schema for show SSH History
    schema = {'Incomming Sessions':
        {'id':
            {Any():
                {'chan': int,
                 'pty' : str,
                 'location':str,
                 'userid':str,
                 'host':str,
                 'ver':str,
                 'authentication':str,
                 'connection_type':str
                 }
            }
        }
    }
# The parser class inherits from the schema class
class ShowSSHHistory(ShowSSHHistorySchema):
    '''Parser for "show ssh history"'''
    cli_command = 'show ssh history'

     # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # Initializes the Python dictionary variable    
        parsed_dict = {}

        # Defines the regex for the lines of device output, which is
        # 1        1    vty0    0/RP0/CPU0      admin     172.16.1.254          v2  key-intr       Command-Line-Interface
        p1 = re.compile(r'(?P<id>\d+) +(?P<chan>\d+) +(?P<pty>\S+) +(?P<location>\S+) +(?P<userid>\S+) +(?P<host>\S+) +(?P<ver>\S+) +(?P<authentication>\S+) +(?P<connection_type>\S+)')
        p2 = re.compile(r'(Incoming\s)')
         # Defines the "for" loop, to pattern match each line of output
        for line in out.splitlines():
            line = line.strip()
            
            
            
            m = p2.match(line)
            if m:
                direction_dict = parsed_dict.setdefault('Incomming Sessions',{})
            
            
            m = p1.match(line)
            # Processes the matched patterns for the lines of output
            if m:
                group = m.groupdict()
                id = int(group['id'])
                group_dict =direction_dict.setdefault('id',{}).\
                    setdefault(id,{})
                group_dict['chan'] = int(group['chan'])
                group_dict['pty'] = group['pty']
                group_dict['location'] = group['location']
                group_dict['userid'] = group['userid']
                group_dict['host'] = group['host']
                group_dict['ver'] = group['ver']
                group_dict['authentication'] = group['authentication']
                group_dict['connection_type'] = group['connection_type']
                continue
            
                
        
        return parsed_dict
                

            
