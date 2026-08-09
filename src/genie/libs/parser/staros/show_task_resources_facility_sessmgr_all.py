"""starOS implementation of show_version.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowtaskResources(MetaParser):
    """Schema for show task resources facility sessmgr all"""

    schema = {
        'task_table': {
            Any(): {
                'Facility': str,
                'CPU': str,
                'CPU Used': str,
                'CPU Allc': str,
                'Memory Used': str,
                'Memory Allc': str,
                'Files Used': str,
                'Files Allc': str,
                'Session Used': str,
                'Session Allc': str,
                'Status': str,                
            },
        }    
    }


class Showtask(ShowtaskResources):
    """Parser for show task resources facility sessmgr all"""

    cli_command = 'show task resources facility sessmgr all'

    """
                   task   cputime        memory     files      sessions
 cpu facility      inst  used  allc   used  alloc used allc  used  allc S status
----------------------- ----------- ------------- --------- ------------- ------
 1/0 sessmgr       5010 0.17%   50% 126.9M 270.0M   28  500    --    -- S   good
 1/0 sessmgr          4 0.40%  100% 213.7M 900.0M   32  500     0 12000 I   good
 1/0 sessmgr         39 0.42%  100% 213.4M 900.0M   30  500     0 12000 I   good
 1/0 sessmgr         60 0.38%  100% 213.7M 900.0M   30  500     0 12000 I   good
 1/0 sessmgr         69 0.43%  100% 213.7M 900.0M   30  500     0 12000 I   good
 1/0 sessmgr         93 0.42%  100% 213.7M 900.0M   30  500     0 12000 I   good
 1/0 sessmgr        104 0.37%  100% 213.4M 900.0M   28  500     0 12000 I   good
 1/0 sessmgr        135 0.42%  100% 213.7M 900.0M   26  500     0 12000 I   good
 1/0 sessmgr        156 0.44%  100% 213.7M 900.0M   25  500     0 12000 I   good
 1/0 sessmgr        191 0.44%  100% 213.7M 900.0M   26  500     0 12000 I   good
 1/0 sessmgr        202 0.40%  100% 213.7M 900.0M   26  500     0 12000 I   good
 1/0 sessmgr        225 0.38%  100% 213.7M 900.0M   26  500     0 12000 I   good
 1/0 sessmgr        268 0.41%  100% 213.7M 900.0M   24  500     0 12000 I   good
 1/0 sessmgr        276 0.41%  100% 213.7M 900.0M   24  500     0 12000 I   good
 1/0 sessmgr        289 0.38%  100% 213.7M 900.0M   23  500     0 12000 I   good
 1/0 sessmgr        300 0.42%  100% 213.7M 900.0M   23  500     0 12000 I   good
 1/0 sessmgr        309 0.42%  100% 213.9M 900.0M   27  500     0 12000 I   good
     """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        task_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'^(?P<CPU>\d+.\d+)\s(?P<facility>\w+)\s+(?P<instance>\d+)\s+(?P<cpu_used>\d+.\d+%|\d+%)\s+(?P<cpu_allc>\d+%)\s+(?P<mem_used>\d+.\d+M)\s+(?P<mem_allc>\d+.\d+M)\s+(?P<file_used>\d+)\s+(?P<file_allc>\d+)\s+(?P<sess_used>\d+|..)\s+(?P<sess_allc>\d+|..)\s+(\w)\s+(?P<status>\w+)')
        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'task_table' not in task_dict:
                    result_dict = task_dict.setdefault('task_table',{})
                instance = m.groupdict()['instance']
                facility = m.groupdict()['facility']
                CPU = m.groupdict()['CPU']
                cpu_used = m.groupdict()['cpu_used']
                cpu_allc = m.groupdict()['cpu_allc']
                mem_used = m.groupdict()['mem_used']
                mem_allc = m.groupdict()['mem_allc']
                file_used = m.groupdict()['file_used']
                file_allc = m.groupdict()['file_allc']
                sess_used = m.groupdict()['sess_used']
                sess_allc = m.groupdict()['sess_allc']
                status = m.groupdict()['status']
                
                result_dict[instance] = {}
                result_dict[instance]['Facility'] = facility
                result_dict[instance]['CPU'] = CPU
                result_dict[instance]['CPU Used'] = cpu_used
                result_dict[instance]['CPU Allc'] = cpu_allc
                result_dict[instance]['Memory Used'] = mem_used
                result_dict[instance]['Memory Allc'] = mem_allc     
                result_dict[instance]['Files Used'] = file_used
                result_dict[instance]['Files Allc'] = file_allc
                result_dict[instance]['Session Used'] = sess_used
                result_dict[instance]['Session Allc'] = sess_allc
                result_dict[instance]['Status'] = status         
                continue

        return task_dict