from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

# ====================================================
# Schema for 'show hsrp internal event-history debugs'
# ====================================================
class ShowHsrpEventHistoryDebugsSchema(MetaParser):
    
    ''' Schema for "show hsrp internal event-history debugs" '''
   
    schema = {  
        "debug_logs":{
            Any():{
                 'date' : str,
                 'time' : str,
                 'proc_name' : str,
                 'pid' : str, 
                 'debug_msg' : str
            } 
        }       
    }

import re

# ====================================================
# Parser for 'show hsrp internal event-history debugs'
# ====================================================
class ShowHsrpEventHistoryDebugs(ShowHsrpEventHistoryDebugsSchema):

    ''' Parser for "show hsrp internal event-history debugs"'''

    cli_command = 'show hsrp internal event-history debugs'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
            if(len(out)==0):
                event_history_debugs_dict={}
                return  event_history_debugs_dict
        else:
            out = output
        
        event_history_debugs_dict={}
        result_dict={}

        p1 = re.compile(r'^\[(?P<log_num>\d+)\]\s+(?P<date>\d{4} (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-9]{1,2}) (?P<time>[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}\.[0-9]{6}) \[(?P<proc_name>.+)\] E_DEBUG\s+\[(?P<pid>\d+)\]:\[\d+\]:\s*(?P<debug_msg>.+)$')

        for line in out.splitlines():
            line = line.strip()

          
            m = p1.match(line)
            if m:
                if 'debug_logs' not in event_history_debugs_dict:
                    result_dict = event_history_debugs_dict.setdefault('debug_logs',{})
                log_num = m.groupdict()['log_num']
                date = m.groupdict()['date']
                time = m.groupdict()['time']
                proc_name = m.groupdict()['proc_name']
                pid = m.groupdict()['pid']
                debug_msg = m.groupdict()['debug_msg']
                
                result_dict[log_num] = {}
                result_dict[log_num]['date'] = date
                result_dict[log_num]['time'] = time
                result_dict[log_num]['proc_name'] = proc_name
                result_dict[log_num]['pid'] = pid
                result_dict[log_num]['debug_msg'] = debug_msg
                continue

        return event_history_debugs_dict



        
    
