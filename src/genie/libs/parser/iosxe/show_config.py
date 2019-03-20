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
                    Optional('user_debug_info'): int
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
        
        # Owner PID : 543
        p1 = re.compile(r'^\s*Owner +PID +: +(?P<owner_pid>\d+)$')
        # TTY number : 2
        p2 = re.compile(r'^\s*TTY +number +: +(?P<tty_number>\d+)$')
        # TTY username : Test1
        p3 = re.compile(r'^\s*TTY +username +: +(?P<tty_username>\S+)$')
        # User debug info : CLI Session Lock

        p4 = re.compile(r'^\s*User +debug +info +: '\
		'+(?P<user_debug_info>(\w+ *)+)$')
        # Look Active time (in Sec) : 63
        p5 = re.compile(r'^\s*Lock +Active +time +\(in +Sec\) +: '\
                '+(?P<lock_active_time_in_sec>\d+)$')
        # Parser Configure Lock
        p6 = re.compile(r'^\s*Parser +Configure +Lock$')
        # Owner PID         : 10
        p7 = re.compile(r'^\s*Owner +PID +: +(?P<owner_pid>\d+)$')
        # User              : User1
        p8 = re.compile(r'^\s*User +: +(?P<user>\S+)$')
        # TTY               : 3
        p9 = re.compile(r'^\s*TTY +: +(?P<tty>\d+)$')
        # Type              : EXCLUSIVE
        p10 = re.compile(r'^\s*Type +: +(?P<type>\S+)$')
        # State             : LOCKED
        p11 = re.compile(r'^\s*State +: +(?P<state>\S+)$')
        # Class             : Exposed
        p12 = re.compile(r'^\s*Class +: +(?P<class_name>\S+)$')
        # Count             : 0
        p13 = re.compile(r'^\s*Count +: +(?P<count>\d+)$')
        # Pending Requests  : 0
        p14 = re.compile(r'^\s*Pending +Requests +: '\
		'+(?P<pending_requests>\d+)$')
        # User debug info   : 0
        p15 = re.compile(r'^\s*User +debug +info +: '\
		'+(?P<user_debug_info>\d+)$')

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
                m = p7.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock = ret_dict.\
                        setdefault('parser_configure_lock',{}).\
                        setdefault('owner_pid',{}).setdefault( \
                        int(group['owner_pid']),{})
                    continue
                
                # User                  : User1
                m = p8.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'user' : group['user']})
                    continue
                
                # TTY                   : 3
                m = p9.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'tty' : int(group['tty'])})
                    continue
                
                # Type                  : Exclusive
                m = p10.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'type' : group['type']})
                    continue
                
                # State                 : Locked
                m = p11.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'state' : group['state']})
                    continue
                
                # Class                 : Exposed
                m = p12.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'class' : \
                        group['class_name']})
                    continue
                
                # Count                 : 0
                m = p13.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'count' : 
                        int(group['count'])})
                    continue
                
                # Pending Requests      : 0
                m = p14.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'pending_requests' : 
                        int(group['pending_requests'])})
                    continue
                
                # User debug info       : 0
                m = p15.match(line)
                if m:
                    group = m.groupdict()
                    parser_configure_lock.update({'user_debug_info' :  
                        int(group['user_debug_info'])})
                    continue

        return ret_dict
        
