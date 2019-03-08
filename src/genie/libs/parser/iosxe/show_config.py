''' show_config.py
IOSXE parsers for the following show command
    * show configuration lock
'''

# Python

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema


# ==================================================
# Parser for 'show configuration lock
# ==================================================

class ShowConfigurationLockSchema(MetaParser):
    """
    Schema for show configuration lock
    """
    
    schema = {'owner': {
                    'owner_pid': int,
                    'tty_number': int,
                    'tty_username': str,
                    'user_debug_info': str,
                    'lock_active_time_in_sec': int
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
        
            
        # Owner PID         : 578
        p1 = re.compile(r'^\s*Owner +PID +: *(?P<owner_pid>\d+)$')
        
        # TTY number        : 2
        p2 = re.compile(r'^\s*TTY +number +: *(?P<tty_number>\d+)$')
        
        # TTY username      : testuser
        p3 = re.compile(r'^\s*TTY +username +: *(?P<tty_username>.*)$')

        # User debug info   : CLI Session Lock
        p4 = re.compile(r'^\s*User +debug +info +: *(?P<user_debug_info>.*)$')

        # Lock Active time (in Sec)
        p5 = re.compile(r'^\s*Lock +Active +time +\( *in +Sec *\) +: *(?P<lock_active_time_in_sec>\d+)')

        for line in out.splitlines():
            line = line.strip()
        
            m = p1.match(line)
            if m:
                group = m.groupdict()
                owner_dict = ret_dict.setdefault('owner',{})
                owner_dict.update({'owner_pid':int(group['owner_pid'])})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                owner_dict.update({'tty_number':int(group['tty_number'])})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                owner_dict.update({'tty_username':str(group['tty_username'])})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                owner_dict.update({'user_debug_info':str(group['user_debug_info'])})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                owner_dict.update({'lock_active_time_in_sec':int(group['lock_active_time_in_sec'])})
                continue

        return ret_dict
        
