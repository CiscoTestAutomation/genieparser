
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And
from genie.libs.parser.utils.common import Common

# pyATS
from pyats.utils.exceptions import SchemaTypeError

log = logging.getLogger(__name__)

class ShowProcessesCpuPlatformSortedSchema(MetaParser):
    """Schema for show processes cpu platform sorted"""
    schema = {
        Optional('cpu_utilization'): {
            Optional('five_sec_cpu_total'): float,
            Optional('one_min_cpu'): float,
            Optional('five_min_cpu'): float,
            Optional('core'): {
                Any(): {
                    'core_cpu_util_five_secs': float,
                    'core_cpu_util_one_min': float,
                    'core_cpu_util_five_min': float,
                },
            }
        },
        'sort': {
            Any(): {
                'ppid': int,
                'five_sec_cpu': float,
                'one_min_cpu': float,
                'five_min_cpu': float,
                'status': str,
                'size': int,
                'process': str,
            },
        }
    }
    
class ShowProcessesCpuPlatformSorted(ShowProcessesCpuPlatformSortedSchema):
    """Parser for show processes cpu platform sorted"""

    cli_command = ['show processes cpu platform sorted', 'show processes cpu platform sorted | exclude {exclude}']
    exclude = ['five_min_cpu', 'nonzero_cpu_processes', 'zero_cpu_processes', 'invoked',
               'runtime', 'usecs', 'five_sec_cpu', 'one_min_cpu']

    def cli(self, exclude=None, output=None):
        if output is None:
            if exclude:
                self.cli_command = self.cli_command[1].format(exclude=exclude)
            else:
                self.cli_command = self.cli_command[0]
            output = self.device.execute(self.cli_command)
        # initial return dictionary
        ret_dict = {}
        index = 0

        # initial regexp pattern

        # CPU utilization for five seconds: 43%, one minute: 44%, five minutes: 44%
        p1 = re.compile(r'^CPU +utilization +for +five +seconds: +(?P<five_sec_cpu_total>[\d\%]+),'
                        ' +one +minute: +(?P<one_min_cpu>[\d\%]+),'
                        ' +five +minutes: +(?P<five_min_cpu>[\d\%]+)$')

        # Core 0: CPU utilization for five seconds:  6%, one minute: 11%, five minutes: 11%
        p2 = re.compile(r'^(?P<core>[\w\s]+): +CPU +utilization +for'
                        ' +five +seconds: +(?P<core_cpu_util_five_secs>\d+\%+),'
                        ' +one +minute: +(?P<core_cpu_util_one_min>[\d+\%]+),'
                        ' +five +minutes: +(?P<core_cpu_util_five_min>[\d+\%]+)$')

        # 21188   21176    599%    600%    599%  R           478632  ucode_pkt_PPE0
        p3 = re.compile(r'^(?P<pid>\d+) +(?P<ppid>\d+)'
                        ' +(?P<five_sec_cpu>[\d\%]+) +(?P<one_min_cpu>[\d\%]+)'
                        ' +(?P<five_min_cpu>[\d\%]+) +(?P<status>[\w]+)'
                        ' +(?P<size>\d+) +(?P<process>.*)$')

        for line in output.splitlines():
            line = line.strip()

            # CPU utilization for five seconds:  2%, one minute:  5%, five minutes: 22%
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('cpu_utilization', {})
                ret_dict['cpu_utilization']['five_sec_cpu_total'] = float(re.search(r'\d+', group['five_sec_cpu_total']).group())/100
                ret_dict['cpu_utilization']['one_min_cpu'] = float(re.search(r'\d+', group['one_min_cpu']).group())/100
                ret_dict['cpu_utilization']['five_min_cpu'] = float(re.search(r'\d+', group['five_min_cpu']).group())/100
                continue

            # Core 0: CPU utilization for five seconds:  2%, one minute:  8%, five minutes: 18%
            m = p2.match(line)
            if m:
                group = m.groupdict()
                core = group.pop('core')
                if 'cpu_utilization' not in ret_dict:
                    ret_dict.setdefault('cpu_utilization', {})
                ret_dict['cpu_utilization'].setdefault('core', {}).setdefault(core, {})
                ret_dict['cpu_utilization']['core'][core]['core_cpu_util_five_secs'] = float(re.search(r'\d+', group['core_cpu_util_five_secs']).group())/100
                ret_dict['cpu_utilization']['core'][core]['core_cpu_util_one_min'] = float(re.search(r'\d+', group['core_cpu_util_one_min']).group())/100
                ret_dict['cpu_utilization']['core'][core]['core_cpu_util_five_min'] = float(re.search(r'\d+', group['core_cpu_util_five_min']).group())/100

            #    Pid    PPid    5Sec    1Min    5Min  Status        Size  Name
            # --------------------------------------------------------------------------------
            #      1       0      0%      0%      0%  S          1863680  init
            #      2       0      0%      0%      0%  S                0  kthreadd
            #      3       2      0%      0%      0%  S                0  migration/0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('sort', {}).setdefault(index, {})
                ret_dict['sort'][index]['ppid'] = int(group['ppid'])
                ret_dict['sort'][index]['five_sec_cpu'] = float(re.search(r'\d+', group['five_sec_cpu']).group())/100
                ret_dict['sort'][index]['one_min_cpu'] = float(re.search(r'\d+', group['one_min_cpu']).group())/100
                ret_dict['sort'][index]['five_min_cpu'] = float(re.search(r'\d+', group['five_min_cpu']).group())/100
                ret_dict['sort'][index]['status'] = group['status']
                ret_dict['sort'][index]['size'] = int(group['size'])
                ret_dict['sort'][index]['process'] = group['process']
                index += 1
                continue

        return ret_dict