''' show_config.py
IOSXE parsers for the following show command
    * show configuration lock
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                            Optional, \
                                            Any

# ==================================================
# Parser for 'show configuration lock'
# ==================================================
class ShowConfigurationLockSchema(MetaParser):
    """
    Schema for show configuration lock
    """
    
    schema = {
        Optional('config_session_lock'): {
            Optional('owner_pid'): {
                Any(): {
                    'tty_number': int,
                    'tty_username': str,
                    'user_debug_info': str,
                    'lock_active_time_in_sec': int,
                }
            }
        },
        Optional('parser_configure_lock'): {
            Optional('owner_pid'): {
                Any(): {
                    Optional('user'): str,
                    Optional('tty'): int,
                    Optional('type'): str,
                    Optional('state'): str,
                    Optional('class'): str,
                    Optional('count'): int,
                    Optional('pending_requests'): int,
                    Optional('user_debug_info'): str,
                    Optional('session_idle_state'): str,
                    Optional('num_of_exec_cmds_executed'): int,
                    Optional('num_of_exec_cmds_blocked'): int,
                    Optional('config_wait_for_show_completion'): str,
                    Optional('remote_ip_address'): str,
                    Optional('lock_active_time_in_sec'): int,
                    Optional('lock_expiration_timer_in_sec'): int,
                }
            }
        }
    }


class ShowConfigurationLock(ShowConfigurationLockSchema):
    """ Parser for show configuration lock"""
    
    cli_command = 'show configuration lock'

    def cli(self,output=None):
        if output is None:
            # execute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output
    
        # initial variables
        ret_dict = {}
        
        parser_lock_found = False
        
        # Owner PID : -1
        # Owner PID : 543
        # Owner PID :10
        p1 = re.compile(r'^\s*Owner +PID +: *(?P<owner_pid>(\-)?\d+)$')
        # TTY number : 2
        p2 = re.compile(r'^\s*TTY +number +: +(?P<tty_number>\d+)$')
        # TTY username : Test1
        p3 = re.compile(r'^\s*TTY +username +: +(?P<tty_username>\S+)$')
        # User debug info : CLI Session Lock

        p4 = re.compile(r'^\s*User +debug +info +: '\
		'+(?P<user_debug_info>(\w+ *)+)$')
        # Look Active time (in Sec) : 63
        p5 = re.compile(r'^\s*Lock +(a|A)ctive +time +\(in +Sec\) +: '\
                '+(?P<lock_active_time_in_sec>\d+)$')
        # Parser Configure Lock
        p6 = re.compile(r'^\s*Parser +Configure +Lock$')
        
        # User              : User1
        # User:User1
        p7 = re.compile(r'^\s*User *: *(?P<user>\S+)$')
        # TTY               : 3
        # TTY:3
        p8 = re.compile(r'^\s*TTY *: *(?P<tty>(\-)?\d+)$')
        # Type              : EXCLUSIVE
        # Type:EXCLUSIVE
        p9 = re.compile(r'^\s*Type *: *(?P<type>[\w\W]+)$')
        # State             : LOCKED
        # State:LOCKED
        p10 = re.compile(r'^\s*State *: *(?P<state>\S+)$')
        # Class             : Exposed
        # Class:Exposed
        p11 = re.compile(r'^\s*Class *: *(?P<class_name>\S+)$')
        # Count             : 0
        # Count:0
        p12 = re.compile(r'^\s*Count *: *(?P<count>\d+)$')
        # Pending Requests  : 0
        # Pending Requests:0
        p13 = re.compile(r'^\s*Pending +Requests *: '\
		'*(?P<pending_requests>\d+)$')
        # User debug info   : 0
        # User debug info:0
        p14 = re.compile(r'^\s*User +debug +info *: '\
		'*(?P<user_debug_info>[\w\W]+)$')
        # Session idle state : TRUE
        p15 = re.compile(r'^Session +idle +state *: *(?P<session_idle_state>[\w]+)$')
        # No of exec cmds getting executed : 0
        p16 = re.compile(r'^No +of +exec +cmds +getting +executed *: *(?P<num_of_exec_cmds_executed>\d+)$')
        # No of exec cmds blocked : 0
        p17 = re.compile(r'^No +of +exec +cmds +blocked *: *(?P<num_of_exec_cmds_blocked>\d+)$')
        # Config wait for show completion : FALSE
        p18 = re.compile(r'^Config +wait +for +show +completion *: *(?P<config_wait_for_show_completion>[\w]+)$')
        # Remote ip address : Unknown
        p19 = re.compile(r'^Remote +ip +address *: *(?P<remote_ip_address>[\w]+)$')
        # Lock Expiration timer (in Sec) : 593
        p20 = re.compile(r'^Lock +Expiration +timer +\(in +Sec\) *: *(?P<lock_expiration_timer_in_sec>[\w]+)$')

        for line in out.splitlines():
            line = line.strip()
        
            if not parser_lock_found:
                # Owner PID : 513
                m = p1.match(line)
                if m:
                    group = m.groupdict()
                    config_session_lock = ret_dict.\
                        setdefault('config_session_lock',{}).\
                        setdefault('owner_pid',{}).\
                        setdefault(int(group['owner_pid']),{})
                    continue
                
                # TTY number : 2
                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    config_session_lock.update({'tty_number' : 
                        int(group['tty_number'])})
                    continue
                
                # TTY username : Test1
                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    config_session_lock.update({'tty_username' : 
                        group['tty_username']})
                    continue
                
                # User debug info : CLI Session Lock
                m = p4.match(line)
                if m:
                    group = m.groupdict()
                    config_session_lock.update({'user_debug_info' : 
                        group['user_debug_info']})
                    continue
                
                # Lock Active time (in Sec) : 63
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    config_session_lock.update({'lock_active_time_in_sec' : 
			             int(group['lock_active_time_in_sec'])})
                    continue
                
                # Parser Configure Lock
                m = p6.match(line)
                if m:
                    parser_lock_found = True
                    continue
            else:
                # Owner PID             : 10
                m = p1.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock = ret_dict.\
                        setdefault('parser_configure_lock',{}).\
                        setdefault('owner_pid',{}).setdefault( \
                        int(group['owner_pid']),{})
                    continue
                
                # User                  : User1
                m = p7.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'user' : group['user']})
                    continue
                
                # TTY                   : 3
                m = p8.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'tty' : int(group['tty'])})
                    continue
                
                # Type                  : Exclusive
                m = p9.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'type' : group['type']})
                    continue
                
                # State                 : Locked
                m = p10.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'state' : group['state']})
                    continue
                
                # Class                 : Exposed
                m = p11.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'class' : \
                        group['class_name']})
                    continue
                
                # Count                 : 0
                m = p12.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'count' : 
                        int(group['count'])})
                    continue
                
                # Pending Requests      : 0
                m = p13.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'pending_requests' : 
                        int(group['pending_requests'])})
                    continue
                
                # User debug info       : 0
                m = p14.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'user_debug_info' :  
                        group['user_debug_info']})
                    continue

                # Session idle state : TRUE
                m = p15.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'session_idle_state' : 
                         group['session_idle_state']})
                    continue

                # No of exec cmds getting executed : 0
                m = p16.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'num_of_exec_cmds_executed' : 
                         int(group['num_of_exec_cmds_executed'])})
                    continue

                # No of exec cmds blocked : 0
                m = p17.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'num_of_exec_cmds_blocked' : 
                         int(group['num_of_exec_cmds_blocked'])})
                    continue

                # Config wait for show completion : FALSE
                m = p18.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'config_wait_for_show_completion' : 
                         group['config_wait_for_show_completion']})
                    continue

                # Remote ip address : Unknown
                m = p19.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'remote_ip_address' : 
                         group['remote_ip_address']})
                    continue

                # Lock Expiration timer (in Sec) : 593
                m = p20.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'lock_expiration_timer_in_sec' : 
                         int(group['lock_expiration_timer_in_sec'])})
                    continue

                # Lock Active time (in Sec) : 63
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'lock_active_time_in_sec' : 
                         int(group['lock_active_time_in_sec'])})
                    continue


        return ret_dict
        
