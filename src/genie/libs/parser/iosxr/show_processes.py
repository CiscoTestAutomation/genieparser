'''
IOSXR parsers for the following commands:
    * show processes
    * show processes {process}
    * show processes location {location}
    * show processes {process} location {location}
    * show processes cpu
    * show processes blocked
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

class ShowProcessesSchema(MetaParser):
    ''' Schema for commands:
        * show processes 
        * show processes {process}
        * show processes location {location}
        * show processes {process} location {location}
    '''
    schema = {
        'job_id': {
            Any(): {
                Optional('pid'): int,
                Optional('process_name'): str,
                Optional('executable_path'): str,
                Optional('instance'): int,
                Optional('version_id'): str,
                Optional('respawn'): str,
                Optional('respawn_count'): int,
                Optional('last_started'): str,
                Optional('process_state'): str,
                Optional('package_state'): str,
                Optional('started_on_config'): str,
                Optional('process_group'): str,
                Optional('core'): str,
                Optional('registered_item'): str,
                Optional('max_core'): int,
                Optional('level'): int,
                Optional('mandatory'): str,
                Optional('placement'): str,
                Optional('startup_path'): str,
                Optional('ready'): str,
                Optional('available'): str,
                Optional('process_cpu_time'): {
                    'user': float,
                    'kernel': float,
                    'total': float,
                },
                Optional('tid'): {
                    Any(): {
                        'stack': str,
                        'pri': int,
                        'state': str,
                        'name': str,
                        'rt_pri': int,
                    }
                }
            }
        }
    }

class ShowProcesses(ShowProcessesSchema):
    ''' Parser for:
        * 'show processes'
        * 'show processes {process}'
        * 'show processes location {location}'
        * 'show processes {process} location {location}'
    '''

    cli_command = ['show processes',
                   'show processes {process}',
                   'show processes location {location}',
                   'show processes {process} location {location}'
                   ]

    def cli(self, process=None, location=None, output=None):

        if output is None:
            if process and location:
                output = self.device.execute(self.cli_command[3].format(process=process, location=location))
            elif process:
                output = self.device.execute(self.cli_command[1].format(process=process))
            elif location:
                output = self.device.execute(self.cli_command[2].format(location=location))
            else:
                output = self.device.execute(self.cli_command[0])

        parsed_output = {}

        # Job Id: 1011
        r1 = re.compile(r'Job\s+Id\s*:\s*(?P<job_id>\d+)')

        # PID: 22464
        r2 = re.compile(r'PID\s*:\s*(?P<pid>\d+)')

        # Process name: isis
        r3 = re.compile(r'Process\s+name\s*:\s+(?P<process_name>\S+)')

        # Executable path: /opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/bin/isis
        r4 = re.compile(r'Executable\s+path\s*:\s*(?P<executable_path>\S+)')

        # Instance #: 1
        r5 = re.compile(r'Instance\s+\#\s*:\s*(?P<instance_number>\d+)')

        # Version ID: 00.00.0000
        r6 = re.compile(r'Version\s+ID\s*:\s*(?P<version_id>\S+)')

        # Respawn: ON
        r7 = re.compile(r'Respawn\s*:\s*(?P<respawn>(ON|OFF))')

        # Respawn count: 1
        r8 = re.compile(r'Respawn\s+count\s*:\s*(?P<respawn_count>\d+)')

        # Last started: Wed Jan 30 20:43:04 2019
        r9 = re.compile(r'Last\s+started\s*:\s*(?P<last_started>.+)')

        # Process state: Run
        r10 = re.compile(r'Process\s+state\s*:\s*(?P<process_state>.+)')

        # Package state: Normal
        r11 = re.compile(r'Package\s+state\s*:\s*(?P<package_state>.+)')

        # Started on config: cfg/gl/isis/instance/test/ord_A/running
        r12 = re.compile(r'Started\s+on\s+config\s*:\s*'
                          r'(?P<started_on_config>\S+)')

        # Process group: v4-routing
        r13 = re.compile(r'Process\s+group\s*:\s*(?P<process_group>\S+)')

        # core: COPY
        r14 = re.compile(r'core\s*:\s*(?P<core>\S+)')

        # Max. core: 0
        r15 = re.compile(r'Max\.\s+core\s*:\s*(?P<max_core>\d+)')

        # Level: 14
        r23 = re.compile(r'Level\s*:\s*(?P<level>\d+)')

        # Mandatory: ON
        r24 = re.compile(r'Mandatory\s*:\s*(?P<mandatory>(ON|OFF))')

        # Placement: Placeable
        r16 = re.compile(r'Placement\s*:\s*(?P<placement>.+)')

        # startup_path: /opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/startup/isis.startup
        r17 = re.compile(r'startup\_path\s*:\s*(?P<startup_path>\S+)')

        # Ready: 1.804s
        r18 = re.compile(r'Ready\s*:\s*(?P<ready>.+)')

        # Available: 1.892s
        r19 = re.compile(r'Available\s*:\s*(?P<available>.+)')

        # Process cpu time: 2.690 user, 0.640 kernel, 3.330 total
        r20 = re.compile(r'Process\s+cpu\s+time\s*:\s*(?P<cpu_time_user>\S+)'
                          r'\s+user,\s+(?P<cpu_time_kernel>\S+)\s+kernel,\s+'
                          r'(?P<cpu_time_total>\S+)\s+total')

        #Registered item(s): cfg/gl/isis/instance/.*/ord_A/
        r21 = re.compile(r'Registered\s+item\(s\)\s*:\s*(?P<registered_item>.+)')

        # JID    TID   Stack  pri  state        NAME             rt_pri
        # 1011   22511    0K  20   Sleeping     Decision         0
        # 1011   22512    0K  20   Sleeping     TE               0
        # 1011   22513    0K  20   Sleeping     MIB Traps        0
        # 1011   22514    0K  20   Sleeping     Protect Infra    0
        # 1011   22494    0K  20   Sleeping     telemetry_evtli  0
        # 1011   22487    0K  20   Sleeping     lspv_lib ISIS    0
        r22 = re.compile(r'(?P<jid>\d+)\s+(?P<tid>\d+)\s+(?P<stack>\S+)\s+'
                          r'(?P<pri>\d+)\s+(?P<state>\S+)\s+\s'
                          r'(?P<name>[\sa-zA-Z\_\-\.]+)\s+(?P<rt_pri>\d+)')

        for line in output.splitlines():
            line = line.strip()

            # Job Id: 1011
            result = r1.match(line)
            if result:
                group = result.groupdict()
                job_id = group['job_id']
                job_dict = parsed_output\
                    .setdefault('job_id', {})\
                    .setdefault(job_id, {})\

                continue

            # PID: 22464
            result = r2.match(line)
            if result:
                group = result.groupdict()
                pid = int(group['pid'])
                job_dict['pid'] = pid

                continue

            # Process name: isis
            result = r3.match(line)
            if result:
                group = result.groupdict()
                process_name = group['process_name']
                job_dict['process_name'] = process_name

                continue

            # Executable path: /opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/bin/isis
            result = r4.match(line)
            if result:
                group = result.groupdict()
                executable_path = group['executable_path']
                job_dict['executable_path'] = executable_path

                continue

            # Instance #: 1
            result = r5.match(line)
            if result:
                group = result.groupdict()
                instance_number = int(group['instance_number'])
                job_dict['instance'] = instance_number

                continue

            # Version ID: 00.00.0000
            result = r6.match(line)
            if result:
                group = result.groupdict()
                version_id = group['version_id']
                job_dict['version_id'] = version_id

                continue

            # Respawn: ON
            result = r7.match(line)
            if result:
                group = result.groupdict()
                respawn = group['respawn']
                job_dict['respawn'] = respawn

                continue

            # Respawn count: 1
            result = r8.match(line)
            if result:
                group = result.groupdict()
                respawn_count = int(group['respawn_count'])
                job_dict['respawn_count'] = respawn_count

                continue

            # Last started: Wed Jan 30 20:43:04 2019
            result = r9.match(line)
            if result:
                group = result.groupdict()
                last_started = group['last_started']
                job_dict['last_started'] = last_started

                continue

            # Process state: Run
            result = r10.match(line)
            if result:
                group = result.groupdict()
                process_state = group['process_state']
                job_dict['process_state'] = process_state

                continue

            # Package state: Normal
            result = r11.match(line)
            if result:
                group = result.groupdict()
                package_state = group['package_state']
                job_dict['package_state'] = package_state

                continue

            # Started on config: cfg/gl/isis/instance/test/ord_A/running
            result = r12.match(line)
            if result:
                group = result.groupdict()
                started_on_config = group['started_on_config']
                job_dict['started_on_config'] = started_on_config

                continue

            # Process group: v4-routing
            result = r13.match(line)
            if result:
                group = result.groupdict()
                process_group = group['process_group']
                job_dict['process_group'] = process_group

                continue

            # core: COPY
            result = r14.match(line)
            if result:
                group = result.groupdict()
                core = group['core']
                job_dict['core'] = core

                continue

            # Max. core: 0
            result = r15.match(line)
            if result:
                group = result.groupdict()
                max_core = int(group['max_core'])
                job_dict['max_core'] = max_core

                continue

            # Level: 14
            result = r23.match(line)
            if result:
                group = result.groupdict()
                level = int(group['level'])
                job_dict['level'] = level

                continue

            # Mandatory: ON
            result = r24.match(line)
            if result:
                group = result.groupdict()
                mandatory = group['mandatory']
                job_dict['mandatory'] = mandatory

                continue

            # Placement: Placeable
            result = r16.match(line)
            if result:
                group = result.groupdict()
                placement = group['placement']
                job_dict['placement'] = placement

                continue

            # startup_path: /opt/cisco/XR/packages/xrv9k-isis-10.9.0.0-r651/rp/startup/isis.startup
            result = r17.match(line)
            if result:
                group = result.groupdict()
                startup_path = group['startup_path']
                job_dict['startup_path'] = startup_path

                continue

            # Ready: 1.804s
            result = r18.match(line)
            if result:
                group = result.groupdict()
                ready = group['ready']
                job_dict['ready'] = ready

                continue

            # Available: 1.892s
            result = r19.match(line)
            if result:
                group = result.groupdict()
                available = group['available']
                job_dict['available'] = available

                continue

            # Process cpu time: 2.690 user, 0.640 kernel, 3.330 total
            result = r20.match(line)
            if result:
                group = result.groupdict()
                cpu_time_user = float(group['cpu_time_user'])
                cpu_time_kernel = float(group['cpu_time_kernel'])
                cpu_time_total = float(group['cpu_time_total'])
                process_cpu_time_dict = job_dict\
                    .setdefault('process_cpu_time', {})
                process_cpu_time_dict['user'] = cpu_time_user
                process_cpu_time_dict['kernel'] = cpu_time_kernel
                process_cpu_time_dict['total'] = cpu_time_total

                continue

            # Registered item(s): cfg/gl/isis/instance/.*/ord_A/
            result = r21.match(line)
            if result:
                group = result.groupdict()
                registered_item = group['registered_item']
                job_dict['registered_item'] = registered_item

                continue

            # JID    TID   Stack  pri  state        NAME             rt_pri
            # 1011   22511    0K  20   Sleeping     Decision         0
            # 1011   22512    0K  20   Sleeping     TE               0
            # 1011   22513    0K  20   Sleeping     MIB Traps        0
            # 1011   22514    0K  20   Sleeping     Protect Infra    0
            # 1011   22494    0K  20   Sleeping     telemetry_evtli  0
            # 1011   22487    0K  20   Sleeping     lspv_lib ISIS    0
            result = r22.match(line)
            if result:
                group = result.groupdict()
                jid = group['jid']
                tid = int(group['tid'])
                stack = group['stack']
                pri = int(group['pri'])
                state = group['state']
                name = group['name'].strip()
                rt_pri = int(group['rt_pri'])
                processes_dict = parsed_output\
                    .setdefault('job_id', {})\
                    .setdefault(jid, {})\
                    .setdefault('tid', {})\
                    .setdefault(tid, {})
                processes_dict['stack'] = stack
                processes_dict['pri'] = pri
                processes_dict['state'] = state
                processes_dict['name'] = name
                processes_dict['rt_pri'] = rt_pri

                continue

        return parsed_output


class ShowProcessesCpuSchema(MetaParser):
    """
    Schema for show processes cpu
    """
    schema = {
        'location': {
            Any(): {
                Optional('one_min_cpu'): int,
                Optional('five_min_cpu'): int,
                Optional('fifteen_min_cpu'): int,
                Optional('index'): {
                    Any(): {
                        'one_min_cpu': int,
                        'five_min_cpu': int,
                        'fifteen_min_cpu': int,
                        'pid': int,
                        'process': str
                    }
                }
            }
        }
    }


class ShowProcessesCpu(ShowProcessesCpuSchema):
    """
    Parser for show processes cpu
    """

    cli_command = ['show processes cpu']
    exclude = ['one_min_cpu', 'five_min_cpu', 'fifteen_min_cpu', 'index']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
            
        # initial return dictionary
        ret_dict = {}
        index = 0

        # ---- node0_RP0_CPU0 ----
        p1 = re.compile(r'^----\s+(?P<location>\S+)\s+----$')

        # CPU utilization for one minute: 0%; five minutes: 0%; fifteen minutes: 0%
        p2 = re.compile(
            r'^CPU\s+utilization\s+for\s+one\s+minute:\s+(?P<one_min_cpu>\d+)\%;\s+five\s+minutes:\s+(?P<five_min_cpu>\d+)\%;\s+fifteen\s+minutes:\s+(?P<fifteen_min_cpu>\d+)%$'
        )

        # 1        0%      0%       0% init
        p3 = re.compile(
            r'^(?P<pid>\d+)\s+(?P<one_min_cpu>\d+)%\s+(?P<five_min_cpu>\d+)%\s+(?P<fifteen_min_cpu>\d+)%\s+(?P<process>\S+)$'
        )

        for line in out.splitlines():
            line = line.strip()

            # ---- node0_RP0_CPU0 ----
            m = p1.match(line)
            if m:
                location = m.groupdict()['location']
                ret_dict.setdefault('location', {}).setdefault(location, {})
                continue

            # CPU utilization for one minute: 0%; five minutes: 0%; fifteen minutes: 0%
            m = p2.match(line)
            if m:
                ret_dict.setdefault('location', {})
                if not ret_dict['location']:
                    location = 'CPU'

                ret_dict.setdefault('location', {}).setdefault(location, {})

                ret_dict['location'][location].update(
                    {k: int(v)
                     for k, v in m.groupdict().items()})
                continue

            # 1        0%      0%       0% init
            m = p3.match(line)
            if m:
                index += 1
                for k, v in m.groupdict().items():
                    if k in [
                            'pid', 'one_min_cpu', 'five_min_cpu',
                            'fifteen_min_cpu'
                    ]:
                        ret_dict['location'][location].setdefault(
                            'index', {}).setdefault(index,
                                                    {}).update({k: int(v)})
                    else:
                        ret_dict['location'][location].setdefault(
                            'index', {}).setdefault(index, {}).update({k: v})
                continue

        return ret_dict


class ShowProcessesBlockedSchema(MetaParser):
    """
    Schema for 'show processes blocked'
    """

    schema = {
        'jid': {
            Any(): {
                'pid': int,
                'process_name': str,
                'tid': {
                    Any(): {
                        'state': str,
                        'time_in_state': str,
                        'blocked_on': str,
                    }
                }
            }
        }
    }


class ShowProcessesBlocked(ShowProcessesBlockedSchema):
    """
    Parser for 'show processes blocked'

    Thu May  1 03:40:06.214 UTC
    Jid       Pid Tid          ProcessName        State   TimeInState    Blocked-on
    122     13635 47914         pm_collector        Reply 0000:00:00.0005    7321 sysdb_mc
    122     13635 47910         pm_collector        Reply 0000:00:00.0005    7321 sysdb_mc
    206     11833 11963              lpts_fm        Reply 0017:08:12.0626    9035 lpts_pa
    """

    cli_command = ['show processes blocked']

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        #   Jid       Pid Tid          ProcessName        State   TimeInState    Blocked-on
        #   193     10985 11144              lpts_fm        Reply 0003:27:24.0579    8532 lpts_pa
        p1 = re.compile(
            r'^(\s+)?(?P<jid>\d+)'
            r'\s+(?P<pid>\d+)'
            r'\s+(?P<tid>\d+)'
            r'\s+(?P<process_name>\w+)'
            r'\s+(?P<state>\w+)'
            r'\s+(?P<time_in_state>[\d:.\w]+)'
            r'\s+(?P<blocked_on>\d+\s+\w+)'
            )

        # Initial return dictionary
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            #  193     10985 11144              lpts_fm        Reply 0003:27:24.0579    8532 lpts_pa
            m = p1.match(line)
            if m:
                group = m.groupdict()

                jid_dict = ret_dict.setdefault('jid', {}).setdefault(int(group['jid']), {})
                jid_dict['pid'] = int(group['pid'])
                jid_dict['process_name'] = group['process_name']

                tid_dict = jid_dict.setdefault('tid', {}).setdefault(int(group['tid']), {})
                tid_dict['state'] = group['state']
                tid_dict['time_in_state'] = group['time_in_state']
                tid_dict['blocked_on'] = group['blocked_on']

        return ret_dict