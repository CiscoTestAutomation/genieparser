''' show_proc_mem.py

IOSXE parser for the following show command:
    * show processes memory platform sorted
    * show processes platform | count {process}
    * show processes platform | include {process}
    * show processes cpu platform DP
    * show processes cpu platform CP
    * show processes cpu platform SP
'''

import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional


# ==================================================
# Schema for 'show processes memory platform sorted'
# ==================================================
class ShowProcessesMemoryPlatformSortedSchema(MetaParser):

    ''' Schema for "show processes memory platform sorted" '''

    schema = {
        'system_memory':
            {Optional('total'): str,
             Optional('used'): str,
             Optional('free'): str,
             Optional('lowest'): str,
             'per_process_memory':
                {Any():
                    {'pid': int,
                     'text': int,
                     'data': int,
                     'stack': int,
                     'dynamic': int,
                     'RSS': int
                     },
                 },
             },
    }


# ==================================================
# Parser for 'show processes memory platform sorted'
# ==================================================
class ShowProcessesMemoryPlatformSorted(ShowProcessesMemoryPlatformSortedSchema):

    ''' Parser for "show processes memory platform sorted" '''

    cli_command = 'show processes memory platform sorted'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        parsed_dict = {}
        if out:
            mem_dict = parsed_dict.setdefault('system_memory', {})
            procmem_dict = mem_dict.setdefault('per_process_memory', {})

        # System memory: 7703908K total, 3863776K used, 3840132K free,
        p1 = re.compile(r'System +memory: +(?P<total>(\d+\w?)) +total,'
                        r' +(?P<used>(\d+\w?)) +used,'
                        r' +(?P<free>(\d+\w?)) +free,')

        # Lowest: 3707912K
        p2 = re.compile(r'Lowest: (?P<lowest>(\d+\w?))')

        #    Pid    Text      Data   Stack   Dynamic       RSS              Name
        # ----------------------------------------------------------------------
        #  16994  233305    887872     136       388    887872   linux_iosd-imag
        p3 = re.compile(r'(?P<pid>(\d+))(\s+)(?P<text>(\d+))(\s+)(?P<data>(\d+))'
                        r'(\s+)(?P<stack>(\d+))(\s+)(?P<dynamic>(\d+))'
                        r'(\s+)(?P<RSS>(\d+))(\s+)(?P<name>([\w-])+)')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                mem_dict['total'] = str(group['total'])
                mem_dict['used'] = str(group['used'])
                mem_dict['free'] = str(group['free'])
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                mem_dict['lowest'] = str(group['lowest'])
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                name = str(group['name'])
                one_proc_dict = procmem_dict.setdefault(name, {})
                one_proc_dict['pid'] = int(group['pid'])
                one_proc_dict['text'] = int(group['text'])
                one_proc_dict['data'] = int(group['data'])
                one_proc_dict['stack'] = int(group['stack'])
                one_proc_dict['dynamic'] = int(group['dynamic'])
                one_proc_dict['RSS'] = int(group['RSS'])
                continue

        return parsed_dict


# ====================
# Schema for:
#  * 'show processes platform | count <process>'
# ====================
class ShowProcessesPlatformCProcessSchema(MetaParser):

    ''' Schema for "show processes platform | count <process>" '''

    schema = {
        "number_of_matching_lines": int
    }


# ====================
# Parser for:
#  * 'show processes platform | count <process>'
# ====================
class ShowProcessesPlatformCProcess(ShowProcessesPlatformCProcessSchema):

    ''' Parser for "show processes platform | count <process>" '''

    # Number of lines which match regexp = 1
    cli_command = "show processes platform | count {process}"

    def cli(self, process=None, output=None):

        if output is None:
            output = self.device.execute(
                self.cli_command.format(process=process))

        # initial return dictionary
        ret_dict = {}

        # Number of lines which match regexp = 1
        p1 = re.compile(
            r"^Number\s+of\s+lines\s+which\s+match\s+regexp\s=\s+(?P<number_of_matching_lines>\d+)")
        for line in output.splitlines():
            line = line.strip()

            # Number of lines which match regexp = 1
            m1 = p1.match(line)
            if m1:
                number_of_matching_lines = p1.match(line)
                groups = number_of_matching_lines.groupdict()
                number_of_matching_lines = int(
                    groups['number_of_matching_lines'])
                ret_dict['number_of_matching_lines'] = number_of_matching_lines

        return ret_dict


# ====================
# Schema for:
#  * 'show processes platform | include <process>'
# ====================
class ShowProcessesPlatformIProcessSchema(MetaParser):

    ''' Schema for "show processes platform | include <process>" '''

    schema = {
        "pid": {
            str: {
                "ppid": str,
                "status": str,
                "size": str,
                "name": str
            }
        }
    }


# ====================
# Parser for:
#  * 'show processes platform | include <process>'
# ====================
class ShowProcessesPlatformIProcess(ShowProcessesPlatformIProcessSchema):

    ''' Parser for "show processes platform | include <process>" '''

    # Pid	PPid  Status		Size  Name
    # 1229	 848  S		   347160  wncd_0
    cli_command = "show processes platform | include {process}"

    def cli(self, process=None, output=None):

        if output is None:
            output = self.device.execute(
                self.cli_command.format(process=process))

        # initial return dictionary
        processes_platform_ret_dict = {}

        # Pid	PPid  Status		Size  Name
        p1 = re.compile(
            r"^(?P<pid>\S+)\s+(?P<ppid>\S+)\s+(?P<status>\S+)\s+(?P<size>\S+)\s+(?P<name>\S+)")

        for line in output.splitlines():
            line = line.strip()

            # 1229	 848  S		   347160  wncd_0
            m1 = p1.match(line)
            if m1:
                groups = m1.groupdict()
                processes_platform_dict = processes_platform_ret_dict.setdefault(
                    'pid', {}).setdefault(groups['pid'], {})
                processes_platform_dict.update({
                    'ppid': groups['ppid'],
                    'status': groups['status'],
                    'size': groups['size'],
                    'name': groups['name']
                })
        return processes_platform_ret_dict


class ShowProcessesCpuPlatformPorfileSchema(MetaParser):
    """Schema for show processes cpu platform profile {profile_name}"""
    schema = {
        'cpu_utilization': {
            'cpu_util_five_secs': str,
            'cpu_util_one_min': str,
            'cpu_util_five_min': str,
            Optional('core'): {
                Any(): {
                    'core_cpu_util_five_secs': str,
                    'core_cpu_util_one_min': str,
                    'core_cpu_util_five_min': str,
                },
            }
        },
        Optional('plane_process_utilization'): {
            'cpu_util_five_secs': str,
            'cpu_util_one_min': str,
            'cpu_util_five_min': str,
        },
        Optional('pid'): {
            Any(): {
                'ppid': int,
                'five_sec': str,
                'one_min': str,
                'five_min': str,
                'status': str,
                'size': int,
                'name': str,
            },
        }
    }


class ShowProcessesCpuPlatformProfile(ShowProcessesCpuPlatformPorfileSchema):
    """Parser for show processes cpu platform profile {profile_name}"""

    cli_command = 'show processes cpu platform profile {profile_name}'

    def cli(self, profile_name, output=None):

        assert profile_name in ['DP', 'CP',
                                'SP'], "Not one from 'DP' 'CP' 'SP'"

        if output is None:
            cmd = self.cli_command.format(profile_name=profile_name)
            out = self.device.execute(cmd, timeout=300)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern

        # CPU utilization for five seconds: 43%, one minute: 44%, five minutes: 44%
        p1 = re.compile(
            r'^CPU +utilization +for +five +seconds: +(?P<cpu_util_five_secs>[\d\%]+),'
            r' +one +minute: +(?P<cpu_util_one_min>[\d\%]+),'
            r' +five +minutes: +(?P<cpu_util_five_min>[\d\%]+)'
        )

        # Core 0: CPU utilization for five seconds:  6%, one minute: 11%, five minutes: 11%
        p2 = re.compile(
            r'^(?P<core>[\w\s]+): +CPU +utilization +for'
            r' +five +seconds: +(?P<core_cpu_util_five_secs>\d+\%+),'
            r' +one +minute: +(?P<core_cpu_util_one_min>[\d+\%]+),'
            r' +five +minutes: +(?P<core_cpu_util_five_min>[\d+\%]+)'
        )

        # Data plane process utilization for five seconds: 43%, one minute: 44%, five minutes: 44%
        p3 = re.compile(
            r'^(Data|Control|Service) +plane +process +utilization +for +five +seconds: +(?P<cpu_util_five_secs>[\d\%]+),'
            r' +one +minute: +(?P<cpu_util_one_min>[\d\%]+),'
            r' +five +minutes: +(?P<cpu_util_five_min>[\d\%]+)'
        )

        # 21188   21176    599%    600%    599%  R           478632  ucode_pkt_PPE0
        p4 = re.compile(
            r'^(?P<pid>\d+) +(?P<ppid>\d+)'
            r' +(?P<five_sec>[\d\%]+) +(?P<one_min>[\d\%]+)'
            r' +(?P<five_min>[\d\%]+) +(?P<status>[\w]+)'
            r' +(?P<size>\d+) +(?P<name>.*)'
        )

        for line in out.splitlines():
            line = line.strip()

            # CPU utilization for five seconds:  2%, one minute:  5%, five minutes: 22%
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('cpu_utilization', {})
                ret_dict['cpu_utilization'].update(
                    {k: str(v) for k, v in group.items()})
                continue

            # Core 0: CPU utilization for five seconds:  2%, one minute:  8%, five minutes: 18%
            m = p2.match(line)
            if m:
                group = m.groupdict()
                core = group.pop('core')
                if 'cpu_utilization' not in ret_dict:
                    ret_dict.setdefault('cpu_utilization', {})
                ret_dict['cpu_utilization'].setdefault(
                    'core', {}).setdefault(core, {})
                ret_dict['cpu_utilization']['core'][core].update(
                    {k: str(v) for k, v in group.items()})
                continue

            # Data plane process utilization for five seconds:  2%, one minute:  5%, five minutes: 22%
            # Control plane process utilization for five seconds:  2%, one minute:  5%, five minutes: 22%
            # Service plane process utilization for five seconds:  2%, one minute:  5%, five minutes: 22%
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('plane_process_utilization', {})
                ret_dict['plane_process_utilization'].update(
                    {k: str(v) for k, v in group.items()})
                continue

            # Pid    PPid    5Sec    1Min    5Min  Status        Size  Name
            # 1       0      0%      0%      0%  S          1863680  init
            m = p4.match(line)
            if m:
                group = m.groupdict()
                pid = group['pid']
                ret_dict.setdefault('pid', {}).setdefault(pid, {})
                ret_dict['pid'][pid]['ppid'] = int(group['ppid'])
                ret_dict['pid'][pid]['five_sec'] = group['five_sec']
                ret_dict['pid'][pid]['one_min'] = group['one_min']
                ret_dict['pid'][pid]['five_min'] = group['five_min']
                ret_dict['pid'][pid]['status'] = group['status']
                ret_dict['pid'][pid]['size'] = int(group['size'])
                ret_dict['pid'][pid]['name'] = group['name']
                continue

        return ret_dict
