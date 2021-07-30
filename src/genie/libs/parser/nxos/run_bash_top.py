"""run_bash_top.py

NXOS parsers for the following show commands:
    * run bash & top -n 1
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

class RunBashTopSchema(MetaParser):
    """ Schema for
            * run bash & top -n 1
    """

    schema = {
        'time': str,
        'up': str,
        'user': int,
        'load_average': {
            'one_min': float,
            'five_mins': float,
            'fifteen_mins': float,
        },
        'tasks': {
            'total': int,
            'running': int,
            'sleeping': int,
            'stopped': int,
            'zombie': int,
        },
        'cpus': {
            'us': float,
            'sy': float,
            'ni': float,
            'id': float,
            'wa': float,
            'hi': float,
            'si': float,
            'st': float,
        },
        'mib_mem': {
            'total': float,
            'free': float,
            'used': float,
            'buff_cache': float,
        },
        'mib_swap': {
            'total': float,
            'free': float,
            'used': float,
            'avail_mem': float,
        },
        'pids': {
            int: {
                'user': str,
                'pr': int,
                'ni': int,
                'virt': int,
                'res': int,
                'shr': int,
                's': str,
                'cpu_percent': float,
                'mem_percent': float,
                'time': str,
                'command': str,
            }
        }
    }

class RunBashTop(RunBashTopSchema):

    """ parser for
        * run bash & top -n 1
    """

    cli_command = 'top -n 1'

    def cli(self,
            output=None):

        if not output:
            with self.device.bash_console():
                out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # top - 15:39:21 up 3 days, 21:35,  1 user,  load average: 0.69, 1.11, 1.21
        # top - 19:10:21 up 18 min,  2 users,  load average: 6.11, 3.33, 2.27
        p1 = re.compile(
            r'^\s*top\s+-\s+(?P<time>\S+)\s+up\s+(?P<up>.*),\s+(?P<user>\d)\s+user(s)?,\s+load\s+average:\s+(?P<one_min>\d+\.\d+),\s+(?P<five_mins>\d+\.\d+),\s+(?P<fifteen_mins>\d+\.\d+)'
        )

        # Tasks: 187 total,   2 running, 185 sleeping,   0 stopped,   0 zombie
        p2 = re.compile(
            r'^\s*Tasks:\s+(?P<total>\d+)\s+total,\s+(?P<running>\d+)\s+running,\s+(?P<sleeping>\d+)\s+sleeping,\s+(?P<stopped>\d+)\s+stopped,\s+(?P<zombie>\d+)\s+zombie'
        )

        # %Cpu(s):  2.9 us, 11.8 sy,  0.0 ni, 76.5 id,  0.0 wa,  5.9 hi,  2.9 si,  0.0 st
        p3 = re.compile(
            r'^\s*%Cpu\(s\):\s+(?P<us>\d+\.\d+)\s+us,\s+(?P<sy>\d+\.\d+)\s+sy,\s+(?P<ni>\d+\.\d+)\s+ni,\s+(?P<id>\d+\.\d+)\s+id,\s+(?P<wa>\d+\.\d+)\s+wa,\s+(?P<hi>\d+\.\d+)\s+hi,\s+(?P<si>\d+\.\d+)\s+si,\s+(?P<st>\d+\.\d+)\s+st'
        )

        # MiB Mem :   5735.5 total,   1039.1 free,   2568.2 used,   2128.2 buff/cache
        p4 = re.compile(
            r'^\s*MiB\s+Mem\s+:\s+(?P<total>\d+\.\d+)\s+total,\s+(?P<free>\d+\.\d+)\s+free,\s+(?P<used>\d+\.\d+)\s+used,\s+(?P<buff_cache>\d+\.\d+)\s+buff/cache'
        )

        # MiB Swap:      0.0 total,      0.0 free,      0.0 used.   1473.4 avail Mem
        p5 = re.compile(
            r'^\s*MiB\s+Swap(\s+)*:\s+(?P<total>\d+\.\d+)\s+total,\s+(?P<free>\d+\.\d+)\s+free,\s+(?P<used>\d+\.\d+)\s+used(\.|,)\s+(?P<avail_mem>\d+\.\d+)\s+avail\s+Mem'
        )

        #   PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
        #  1530 root      20   0  697668  79708  46992 S   6.7   1.4  80:09.11 svc_ifc_eventmg
        p6 = re.compile(
            r'^\s*(?P<pid>\d+)\s+(?P<user>\S+)\s+(?P<pr>\d+)\s+(?P<ni>\d+)\s+(?P<virt>\d+)\s+(?P<res>\d+)\s+(?P<shr>\d+)\s+(?P<s>\S+)\s+(?P<cpu_percent>\d+\.\d+)\s+(?P<mem_percent>\d+\.\d+)\s+(?P<time>\S+)\s+(?P<command>.*)'
        )

        top_dict = {}
        for line in out.splitlines():
            line = line.replace('\x0f', '').strip()

            # top - 15:39:21 up 3 days, 21:35,  1 user,  load average: 0.69, 1.11, 1.21
            m = p1.match(line)
            if m:
                group = m.groupdict()
                for k,v in group.items():
                    if k in ['user']:
                        ret_dict[k] = int(v)
                    elif k in ['one_min', 'five_mins', 'fifteen_mins']:
                        ret_dict.setdefault('load_average', {}).setdefault(k, float(v))
                    else:
                        ret_dict[k] = v
            
            # Tasks: 187 total,   2 running, 185 sleeping,   0 stopped,   0 zombie
            m = p2.match(line)
            if m:
                group = m.groupdict()
                for k,v in group.items():
                    ret_dict.setdefault('tasks', {}).setdefault(k, int(v))

            # %Cpu(s):  2.9 us, 11.8 sy,  0.0 ni, 76.5 id,  0.0 wa,  5.9 hi,  2.9 si,  0.0 st
            m = p3.match(line)
            if m:
                group = m.groupdict()
                for k,v in group.items():
                    ret_dict.setdefault('cpus', {}).setdefault(k, float(v))

            # MiB Mem :   5735.5 total,   1039.1 free,   2568.2 used,   2128.2 buff/cache
            m = p4.match(line)
            if m:
                group = m.groupdict()
                for k,v in group.items():
                    ret_dict.setdefault('mib_mem', {}).setdefault(k, float(v))

            # MiB Swap:      0.0 total,      0.0 free,      0.0 used.   1473.4 avail Mem
            m = p5.match(line)
            if m:
                group = m.groupdict()
                for k,v in group.items():
                    ret_dict.setdefault('mib_swap', {}).setdefault(k, float(v))

            #  1530 root      20   0  697668  79708  46992 S   6.7   1.4  80:09.11 svc_ifc_eventmg
            m = p6.match(line)
            if m:
                group = m.groupdict()
                pid = int(group.pop('pid'))
                top_dict = ret_dict.setdefault('pids', {}).setdefault(pid, {})
                for k, v in group.items():
                    if k in ['user', 's', 'time', 'command']:
                        top_dict.update({k: v})
                    elif k in ['cpu_percent', 'mem_percent']:
                        top_dict.update({k: float(v)})
                    else:
                        top_dict.update({k: int(v)})
                continue

        return ret_dict