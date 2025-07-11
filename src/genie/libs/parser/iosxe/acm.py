'''

IOSXE parsers for the following show commands:
    * acm log
    * acm log confirm-commit
    * acm log merge
    * acm log replace
    * acm log save
    * acm log <1-50>

'''
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ====================
# Schema for:
#  * 'acm configlet status'
# ====================
class AcmConfigletStatusSchema(MetaParser):
    """Schema for acm configlet status."""

    schema = {
        "configlet_file": str,
        "terminal": str,
        "user": str,
        "count": str,
        "configlet_data": {
            str: str
            }
        }

# ====================
# Parser for:
#  * 'acm configlet status'
# ====================
class AcmConfigletStatus(AcmConfigletStatusSchema):
    """Parser for acm configlet status"""

    # Configlet Name      : flash:configletfile1
    # Terminal, User      : TTY0, campus
    # CLI Count           : 99
    # Configlet Data      : 
    # 2   vlan 40
    # 3   name OFFICE:FACILITIES
    # 4   vlan 15
    # 5   name IMAGING-WIRED
    # 6   vlan 400
    # 7   name OFFICE:GUEST-DATA-1
    # 8   vlan 16
    # 9   name IMAGING-WIRELESS
    # 10  vlan 301
    # 11  name OFFICE:EMPLOYEE-DEV-1
 
    cli_command = 'acm configlet status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
    		
    	# Configlet Name      : flash:configletfile1
        p1 = re.compile(r'^Configlet Name \s+: (?P<file>\S+)$')

        # Terminal, User      : TTY0, campus
        p2 = re.compile(r'^Terminal, User \s+: (?P<terminal>\w+)\, +(?P<user>\w+)$')

        # CLI Count           : 99
        p3 = re.compile(r'^CLI Count \s+: (?P<count>\d+)$')

        # Configlet Data      : 
        p4 = re.compile(r'^Configlet Data+ \s+:$')

        # 10  vlan 301
        # 11  name OFFICE:EMPLOYEE-DEV-1
        # 97  storm-control broadcast level 20.00
        p5 = re.compile(r'^(?P<index_number>\d+)\s+(?P<config_data>.*)$')
                                
        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

    	    # Configlet Name      : flash:configletfile1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['configlet_file']=group['file']
                continue
            
            # Terminal, User      : TTY0, campus
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['terminal']=group['terminal']
                ret_dict['user']=group['user']
                continue
            
            # CLI Count           : 99
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['count']=group['count']
                continue
            
            # Configlet Data      : 
            m = p4.match(line)
            if m:
                group = m.groupdict()
                config_dict = ret_dict.setdefault('configlet_data',{})
                continue
            
            # 10  vlan 301
            # 11  name OFFICE:EMPLOYEE-DEV-1
            # 97  storm-control broadcast level 20.00
            m = p5.match(line)
            if m:
                group = m.groupdict()
                config_dict[group["index_number"]]=group['config_data']
                continue

        return ret_dict

# ====================
# Schema for:
#  * 'acm merge <configlet_file> validate'
# ====================
class AcmMergeValidateSchema(MetaParser):
    """Schema for acm merge <configlet_file> validate."""

    schema = {
        Optional("configlet_file_name"): str,
        Optional("validation_status"): str,
        Optional("validation_time"): str,
        Optional("failed_command"): str,
        Optional("failed_reason"): str,
        Optional("platform_status"): str,
        Optional("invalid_file"): str
        }

# ====================
# Parser for:
#  * 'acm merge <configlet_file> validate'
# ====================
class AcmMergeValidate(AcmMergeValidateSchema):
    """Parser for acm merge <configlet_file> validate"""

    # Validatating the configlet demo
    #     Validation failed
    #     Validation Time: 253 msec

    #     Failed command: hostname 1234
    #     Failed reason: 
    # % Hostname contains one or more illegal characters. 
 
    cli_command = 'acm merge {configlet_file} validate'

    def cli(self, configlet_file='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(configlet_file=configlet_file))
    	
        # Validatating the configlet demo
        p1 = re.compile(r'^Validatating +the +configlet (?P<configlet_file>\S+)$')

        # Validation failed
        p2 = re.compile(r'^Validation +(?P<validation_status>success|failed)$')

        # Validation Time: 253 msec
        p3 = re.compile(r'^Validation +Time: (?P<validation_time>[\w\s]+)$')

        # Failed command: hostname 1234
        p4 = re.compile(r'^Failed +command: (?P<failed_command>.*)$')

        # Failed reason: 
        p5 = re.compile(r'^Failed +reason:$')
    
        # % Hostname contains one or more illegal characters. 
        p6 = re.compile(r'(?P<failed_reason>[\S\s]+)$')

        # Validation on platform not supported   #Negative scenario
        p7 = re.compile(r'^Validation +on +platform (?P<platform_status>not supported)$')

        # %Error: Invalid file: flash:empty_file.cfg    #Negative scenario
        p8 = re.compile(r'^%Error: +Invalid file: (?P<invalid_file>\S+)$')

        failed_reason_check = False
        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            
            # Validatating the configlet demo
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['configlet_file_name'] = group['configlet_file']
                continue
            
            # Validation failed
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['validation_status'] = group['validation_status']
                continue
            
            # Validation Time: 253 msec
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['validation_time'] = group['validation_time']
                continue
            
            # Failed command: hostname 1234
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['failed_command'] = group['failed_command']
                continue
            
            # Failed reason: 
            m = p5.match(line)
            if m:
                failed_reason_check = True
                continue
            
            # % Hostname contains one or more illegal characters.
            m = p6.match(line)
            if m and failed_reason_check:
                group = m.groupdict()
                ret_dict['failed_reason'] = group['failed_reason']
                continue

            # Validation on platform not supported    #Negative scenario
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict['platform_status'] = group['platform_status']
                continue
            
            # %Error: Invalid file: flash:empty_file.cfg    #Negative scenario
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict['invalid_file'] = group['invalid_file']
                continue

        return ret_dict 

class ACMLogSchema(MetaParser):
    """Schema for ACM log message"""
    schema = {
        'sno': {
            Any(): {
                'event': str,
                'result': str,
                'username': str,
                'timestamp': str,
                Optional('target_config'): str
            },
        },
    }


class AcmLog(ACMLogSchema):
    """Parser for ACM log"""

    cli_command = ['acm log', 'acm log {command}']

    def cli(self, command='', output=None):

        if output is None:
            if command:
                out = self.device.execute(self.cli_command[1].format(command=command))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        #Sno  Event  Result   Username   Time(M/D H:M:S)  Target-config
        p1 = re.compile(r'^(?P<sno>\d+)\s+'r'(?P<event>\S+)\s+'r'(?P<result>\S+)\s+'r'(?P<username>\S+)\s+'r'(?P<timestamp>\d{2}/\d{2}\s\d{2}:\d{2}:\d{2})\s*'r'(?P<target_config>\S*)$')
        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            #Sno  Event Result   Username   Time(M/D H:M:S)  Target-config
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sno = int(group['sno'])
                sno_dict = ret_dict.setdefault('sno', {})
                log_dict = sno_dict.setdefault(sno, {})
                log_dict['event'] = group['event']
                log_dict['result'] = group['result']
                log_dict['username'] = group['username']
                log_dict['timestamp'] = group['timestamp']
                if group['target_config']:
                    log_dict['target_config'] = group['target_config']

        return ret_dict

class ACMLogIndexNumberSchema(MetaParser):
    """Schema for ACM log {index number}"""
    schema = {
      'user_name': str,                  
      'event_name': str,                 
      'result': str,                     
      'event_time': str,                 
      'target_config': str,            
      Optional('net_config_location'): str,       
      Optional('net_config'): list,          
      Optional('summary'): {                      
          'operation': str,             
          'result': str                 
        },
    }

class ACMLogIndexNumber(ACMLogIndexNumberSchema):
    """Parser for ACM log {index number}"""
     
    cli_command = ['acm log {index_number}']

    def cli(self, index_number='', output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0].format(index_number=index_number))
        else:
            out = output

        ret_dict = {}
        net_config_lines = []
        summary = {}
        state = None  

        #User Name : campus
        p1 = re.compile(r'^User\s+Name\s*:\s*(?P<user_name>.+)$')
        #Event : ROLLBACK
        p2 = re.compile(r'^Event\s*:\s*(?P<event>.+)$')
        #Result : Success
        p3 = re.compile(r'^Result\s*:\s*(?P<result>.+)$')
        #Time of Event : 2025/05/15 18:11:11.340 UTC
        p4 = re.compile(r'^Time\s+of\s+Event\s*:\s*(?P<event_time>.+)$')
        #Target config : flash:checkpoint1
        p5 = re.compile(r'^Target\s+config\s*:\s*(?P<target_config>.+)$')
        #Net-Config Location: flash:acm/acm_cfg_ROLLBACK_diff_3956321471.cfg
        p6 = re.compile(r'^Net-Config\s+Location\s*:\s*(?P<flash>.+)$')
        #Net-Config:
        p7 = re.compile(r'^Net-Config:$')
        #!----------------------
        p8 = re.compile(r'^![-]+$')
        #! Operation : ROLLBACK"
        p9 = re.compile(r'^!\s*(?P<key>[^:]+)\s*:\s*(?P<value>.+)$')


        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            #User Name : campus
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['user_name'] = group['user_name']
                continue

            #Event : ROLLBACK
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['event_name'] = group['event']
                continue

            #Result : Success
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['result'] = group['result']
                continue

            #Time of Event : 2025/05/15 18:11:11.340 UTC
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['event_time'] = group['event_time']
                continue

            #Target config : flash:checkpoint1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict['target_config'] = group['target_config']
                continue

            #Net-Config Location: flash:acm/acm_cfg_ROLLBACK_diff_3956321471.cfg
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict['net_config_location'] = group['flash']
                continue
            
            #Net-Config:
            if p7.match(line):
                state = 'net_config'
                continue
            
            # Handle lines in the "Net-Config" section
            if state == 'net_config':
                # Matches "!----------------------" (end of "Net-Config" section and transition to summary)
                if p8.match(line):
                    ret_dict['net_config'] = net_config_lines
                    net_config_lines = []
                    state = 'summary'  # Transition to parsing the summary section
                    continue
                # Collect lines in the "Net-Config" section
                net_config_lines.append(line)
                continue
            
            # Handle lines in the "summary" section
            if state == 'summary':
                # Matches summary key-value pairs, e.g., "! Operation : ROLLBACK"
                m = p9.match(line)
                if m:
                    group = m.groupdict()
                    summary[group['key'].strip().lower()] = group['value'].strip()
                    continue
            
        # Add parsed summary data to the result dictionary
        if summary:
            ret_dict['summary'] = {}
            # Extract "operation" from summary if present
            if 'operation' in summary:
                ret_dict['summary']['operation'] = summary['operation']
            # Extract "result" from summary if present
            if 'result' in summary:
                ret_dict['summary']['result'] = summary['result']

        return ret_dict
