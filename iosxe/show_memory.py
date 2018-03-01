"""show_memory.py

"""
# python
import re

# metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use


class ShowMemoryStatisticsSchema(MetaParser):
    """Schema for show memory statistics"""
    schema = {
        Optional('tracekey'): str,
        'name': {
            Any(): {
                'head': str,
                'total': int,
                'used': int,
                'free': int,
                'lowest': int,
                'largest': int,
            }
        }
    }


class ShowMemoryStatistics(ShowMemoryStatisticsSchema):
    """Parser for show memory statistics"""

    def cli(self):
        out = self.device.execute('show memory statistics')

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<name>\S+) +(?P<head>\w+) +(?P<total>\d+) +'
                         '(?P<used>\d+) +(?P<free>\d+) +'
                         '(?P<lowest>\d+) +(?P<largest>\d+)$')

        p2 = re.compile(r'^Tracekey *: +(?P<tracekey>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            #                 Head    Total(b)     Used(b)     Free(b)   Lowest(b)  Largest(b)
            # Processor  FF86F21010   856541768   355116168   501425600   499097976   501041348
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group.pop('name').lower()
                name_dict = ret_dict.setdefault('name', {}).setdefault(name, {})
                name_dict['head'] = group.pop('head')
                name_dict.update({k:int(v) for k, v in group.items()})
                continue

            # Tracekey : 1#f8e3c2db7822c04e58ce2bd2fc7e476a
            m = p2.match(line)
            if m:
                ret_dict['tracekey'] = m.groupdict()['tracekey']
                continue
        return ret_dict


class ShowProcessesCpuSortedSchema(MetaParser):
    """Schema for show processes cpu sorted
                  show processes cpu sorted <1min|5min|5sec>
                  show processes cpu sorted | include <WORD>
                  show processes cpu sorted <1min|5min|5sec> | include <WORD>"""
    schema = {
        'five_sec_cpu_low': int,
        'five_sec_cpu_high': int,
        'one_min_cpu': int,
        'five_min_cpu': int,
        Optional('zero_cpu_processes'): list,
        Optional('nonzero_cpu_processes'): list,
        Optional('sort'): {
            Any(): {
                'runtime': int,
                'invoked': int,
                'usecs': int,
                'five_sec_cpu': float,
                'one_min_cpu': float,
                'five_min_cpu': float,
                'tty': int,
                'pid': int,
                'process': str
            }
        }
    }


class ShowProcessesCpuSorted(ShowProcessesCpuSortedSchema):
    """Parser for show processes cpu sorted
                  show processes cpu sorted <1min|5min|5sec>
                  show processes cpu sorted | include <WORD>
                  show processes cpu sorted <1min|5min|5sec> | include <WORD>"""

    def cli(self, sort_time='', key_word=''):
        assert sort_time in ['1min', '5min', '5sec', ''], "Not one from 1min 5min 5sec"
        cmd = 'show processes cpu sorted'
        if sort_time:
            cmd += ' ' + sort_time
        if key_word:
            cmd += ' | ' + key_word

        out = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}
        zero_cpu_processes = []
        nonzero_cpu_processes = []
        index = 0

        # initial regexp pattern
        p1 = re.compile(r'^CPU +utilization +for +five +seconds: +'
                         '(?P<five_sec_cpu_high>\d+)\%\/(?P<five_sec_cpu_low>\d+)\%;'
                         ' +one +minute: +(?P<one_min_cpu>\d+)\%;'
                         ' +five +minutes: +(?P<five_min_cpu>\d+)\%$')

        p2 = re.compile(r'^(?P<pid>\d+) +(?P<runtime>\d+) +(?P<invoked>\d+) +(?P<usecs>\d+) +'
                         '(?P<five_sec_cpu>[\d\.]+)\% +(?P<one_min_cpu>[\d\.]+)\% +'
                         '(?P<five_min_cpu>[\d\.]+)\% +(?P<tty>\d+) +'
                         '(?P<process>[\w\-\/\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            # CPU utilization for five seconds: 5%/1%; one minute: 6%; five minutes: 6%
            m = p1.match(line)
            if m:
                ret_dict.update({k:int(v) for k, v in m.groupdict().items()})
                continue

            # PID Runtime(ms)     Invoked      uSecs   5Sec   1Min   5Min TTY Process 
            # 539     6061647    89951558         67  0.31%  0.36%  0.38%   0 HSRP Common 
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index += 1
                sort_dict = ret_dict.setdefault('sort', {}).setdefault(index, {})
                sort_dict['process'] = group['process']
                sort_dict.update({k:int(v) for k, v in group.items() 
                    if k in ['runtime', 'invoked', 'usecs', 'tty', 'pid']})
                sort_dict.update({k:float(v) for k, v in group.items() 
                    if k in ['five_sec_cpu', 'one_min_cpu', 'five_min_cpu']})
                if float(group['five_sec_cpu']) or \
                   float(group['one_min_cpu']) or \
                   float(group['five_min_cpu']):
                    nonzero_cpu_processes.append(group['process'])
                else:
                    zero_cpu_processes.append(group['process'])
                continue
        ret_dict.setdefault('zero_cpu_processes', zero_cpu_processes) if zero_cpu_processes else None
        ret_dict.setdefault('nonzero_cpu_processes', nonzero_cpu_processes) if nonzero_cpu_processes else None
        return ret_dict
