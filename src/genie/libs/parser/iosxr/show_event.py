"""
   show_event.py
   IOSXR parsers for the following show commands:
   * show event manager environment 
   * show event manager environment all
   * show event manager policy available 
   * show event manager policy available <type>
   * show event manager policy available user | include <eem_file_name>
   * show event manager policy registered 
   * show event manager policy registered <type>
   * show event manager policy registered user | include <eem_file_name>	
"""

# python
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowEventManagerEnvSchema(MetaParser):
    """Schema for show event manager environment"""
    schema = {
        'event_num': {
            int: {
                'event_name': str,
                'value': str,
            },
        },
    }

class ShowEventManagerEnv(ShowEventManagerEnvSchema):

    """Parser for 
       show event manager environment 
       show event manager environment | include {event_name}
    """

    cli_command = ['show event manager environment','show event manager environment | include {event_name}']

    def cli(self, event_name='', output=None):
        
        if output is None:
            if event_name:
                cmd = self.cli_command[1].format(event_name=event_name)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        #1   _eem_int                      Loopback2                                         
        #2   _eem_event_trigger_log        eem trigger logs jun24     
        p = re.compile(r'^(?P<num>\d+) +(?P<event_name>\w+) +((?P<value>.+))?$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #1   _eem_int                      Loopback2
            #2   _eem_event_trigger_log        eem trigger logs jun24     
            m = p.match(line)
            if m:
                group = m.groupdict()
                event_number = int(group['num'])
                result_dict = ret_dict.setdefault('event_num', {}).setdefault(event_number, {})  
                result_dict['event_name'] = group['event_name']
                result_dict['value'] = group['value']
                continue

        return ret_dict

class ShowEventManagerEnvAll(ShowEventManagerEnv):

    """Parser for
       show event manager environment all
    """

    cli_command = ['show event manager environment all']

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)

		
class ShowEventManagerPolicyAvailableSchema(MetaParser):
    """Schema for show event manager policy available """

    schema = {
        'event_num': {
            int: {
                'type': str,
                'time_created': str,
                'eemfile_name': str,
            }
        }
    }

class ShowEventManagerPolicyAvailable(ShowEventManagerPolicyAvailableSchema):

    """Parser for 
       show event manager policy available 
       show event manager policy available {type}	       
       show event manager policy available {type} | include {eemfile_name}
    """

    cli_command = ['show event manager policy available','show event manager policy available {type}',
                   'show event manager policy available {type} | include {eemfile_name}']

    def cli(self, eemfile_name='',type ='', output=None):
        if output is None:
            if type and eemfile_name:
                cmd = self.cli_command[2].format(eemfile_name=eemfile_name,type=type)
            elif type and not eemfile_name:
                cmd = self.cli_command[1].format(type=type)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

	#1   user      Mon Jun 28 11:52:14 2021      eem_cli_exec_file.tcl                             
        #2   user      Thu Jun 24 09:33:26 2021      eem_int_shut.tcl    
        p = re.compile(r'^(?P<num>\d+) +(?P<type>\w+) +(?P<time_created>.+[^ ]) +(?P<eemfile_name>.+)$')

        ret_dict = {}
        
        for line in output.splitlines():
            line = line.strip()

            #1   user      Mon Jun 28 11:52:14 2021      eem_cli_exec_file.tcl
            m = p.match(line)
            if m:
                group = m.groupdict()
                event_number = int(group['num'])
                result_dict = ret_dict.setdefault('event_num', {}).setdefault(event_number, {})
                result_dict['type'] = group['type']
                result_dict['time_created'] = group['time_created']
                result_dict['eemfile_name'] = group['eemfile_name']
                continue

        return ret_dict


class ShowEventManagerPolicyRegisteredSchema(MetaParser):
    """Schema for show event manager policy registered  """
    
    schema = {
        'policy_num':{
            Any(): {
                'class': str,
                'type': str,
                'event_type': str,
                'trap': str,
                'time_registered': str,
                'eemfile_name': str,
                Optional('pattern_name'): str,
                Optional('nice_value'):int,
                Optional('queue_priority'): str,
                Optional('maxrun'): float,
                Optional('scheduler'): str,
                Optional('secu'): str,
                Optional('persist_time'): int,
                Optional('username'): str,
            }
        }
    }

class ShowEventManagerPolicyRegistered(ShowEventManagerPolicyRegisteredSchema):

    """Parser for 
       show event manager policy registered 
       show event manager policy registered {type}	       
       show event manager policy registered {type} | include {eemfile_name}	      
    """

    cli_command = ['show event manager policy registered','show event manager policy registered {type}',
                   'show event manager policy registered {type} | include {eemfile_name}']

    def cli(self, eemfile_name='',type ='', output=None):
        if output is None:
            if type and eemfile_name:
                cmd = self.cli_command[2].format(eemfile_name=eemfile_name,type=type)
            elif type and not eemfile_name:
                cmd = self.cli_command[1].format(type=type)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)
        
        #1    script    user    syslog              Off   Mon Jun 28 14:55:59 2021  eem_int_shut.tcl
        p1 = re.compile(r'^(?P<num>\d+) + (?P<class>[a-z]+) '
                       r'+ (?P<type>[a-z]+) + (?P<event_type>[a-z\s]+)\s'
                       r'+ (?P<trap>[A-Za-z]+) + (?P<time_registered>[A-Za-z0-9\s\:]+) '
                       r'+ (?P<eemfile_name>[\w\-.]+)?$')

        #  pattern {eem trigger logs jun24}
        #  name {watchtimer} time 180.000
        #  name {crontimer2} cron entry {0-59/2 0-23/1 * * 0-7}
        p2 = re.compile(r'^(?P<pattern_name>[\w\s]+ \{[\w\s]+\}.*)$')

        #  nice 0 queue-priority normal maxrun 100.000 scheduler rp_primary Secu none
        p3 = re.compile(r'^nice +(?P<nice_value>\d+) +queue-priority +(?P<queue_priority>\w+) +maxrun +(?P<maxrun>[\d.]+) '
                        r'+scheduler +(?P<scheduler>[\w\_]+) +Secu +(?P<secu>\w+)$')

        #  persist_time: 3600 seconds,  username: lab
        p4 = re.compile(r'^persist_time: +(?P<persist_time>\d+) seconds,  +username: +(?P<username>\w+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #1    script    user    syslog              Off   Mon Jun 28 14:55:59 2021  eem_int_shut.tcl
            m = p1.match(line)
            if m:
                group = m.groupdict()
                event_number =int(group['num'])

                result_dict = ret_dict.setdefault('policy_num', {}).setdefault(event_number, {})
          
                result_dict['class'] = group['class']
                result_dict['type'] = group['type']
                result_dict['event_type'] = group['event_type']
                result_dict['trap'] = group['trap']
                result_dict['time_registered'] = group['time_registered']
                result_dict['eemfile_name'] = group['eemfile_name']
                continue

            #  pattern {eem trigger jun28}
            #  name {watchtimer} time 180.000
            #  name {crontimer2} cron entry {0-59/2 0-23/1 * * 0-7}
            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_dict['pattern_name'] = group['pattern_name']
                continue

            #  nice 0 queue-priority normal maxrun 100.000 scheduler rp_primary Secu none
            m = p3.match(line)
            if m:
                group = m.groupdict()

                result_dict['nice_value'] = int(group['nice_value'])
                result_dict['queue_priority'] = group['queue_priority']
                result_dict['maxrun'] = float(group['maxrun'])
                result_dict['scheduler'] = group['scheduler']
                result_dict['secu'] = group['secu']
                continue

            #  persist_time: 3600 seconds,  username: lab
            m = p4.match(line)
            if m:
                group = m.groupdict()

                result_dict['persist_time'] = int(group['persist_time'])
                result_dict['username'] = group['username']
                continue

        return ret_dict
