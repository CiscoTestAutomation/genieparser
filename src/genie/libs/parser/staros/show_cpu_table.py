"""starOS implementation of show_cpu_table.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowCpuTableSchema(MetaParser):
    """Schema for show version"""

    schema = {
        'cpu_table': {
            Any(): {
            'state': str,
            'load now': str,
            'load 5min': str,
            'load 15min': str,
            'cpu now': str,
            'cpu 5min': str,
            'cpu 15min': str,
            'mem now': str,
            'mem 5min': str,
            'mem 15min': str,
            'mem total': str,
            },
        }     
    }


class ShowCpuTable(ShowCpuTableSchema):
    """Parser for show cpu table"""

    cli_command = 'show cpu table'

    """
             --------Load--------  ------CPU-Usage-----  ---------Memory--------
 cpu  state     now   5min  15min     now   5min  15min    now  5min 15min total
----  -----  ------ ------ ------  ------ ------ ------  ----- ----- ----- -----
 1/0  Actve    3.51   2.90   2.57    1.1%   1.1%   0.9%  7035M 7034M 7032M 8192M
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        cpu_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'^((?P<cpu_id>\d+.\d+)\s+(?P<state>\S+)\s+(?P<load_now>\d+.\d+)\s+(?P<load_5min>\d+.\d+)\s+(?P<load_15min>\d+.\d+)\s+(?P<CPU_now>\d+.\d+%)\s+(?P<CPU_5min>\d+.\d+%)\s+(?P<CPU_15min>\d+.\d+%)\s+(?P<Mem_now>\d+.\d+(M|G))\s+(?P<Mem_5min>\d+.\d+(M|G))\s+(?P<Mem_15min>\d+.\d+(M|G))\s+(?P<Mem_total>\d+.\d+(M|G)))')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'cpu_table' not in cpu_dict:
                    result_dict = cpu_dict.setdefault('cpu_table',{})
                cpu = m.groupdict()['cpu_id']    
                state = m.groupdict()['state']
                load_now = m.groupdict()['load_now']
                load_5min = m.groupdict()['load_5min']
                load_15min = m.groupdict()['load_5min']
                CPU_now = m.groupdict()['CPU_now']
                CPU_5min = m.groupdict()['CPU_5min']
                CPU_15min = m.groupdict()['CPU_15min']
                Mem_now = m.groupdict()['Mem_now']
                Mem_5min = m.groupdict()['Mem_5min']
                Mem_15min = m.groupdict()['Mem_15min']
                Mem_total = m.groupdict()['Mem_total']

                result_dict[cpu] = {}
                result_dict[cpu]['state'] = state
                result_dict[cpu]['load now'] = load_now
                result_dict[cpu]['load 5min'] = load_5min
                result_dict[cpu]['load 15min'] = load_15min
                result_dict[cpu]['cpu now'] = CPU_now
                result_dict[cpu]['cpu 5min'] = CPU_5min
                result_dict[cpu]['cpu 15min'] = CPU_15min
                result_dict[cpu]['mem now'] = Mem_now
                result_dict[cpu]['mem 5min'] = Mem_5min
                result_dict[cpu]['mem 15min'] = Mem_15min
                result_dict[cpu]['mem total'] = Mem_total
                continue

        return cpu_dict