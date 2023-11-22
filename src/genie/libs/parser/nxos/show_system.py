"""show_system.py

NXOS parsers for the following show commands:
    * 'show system internal sysmgr service name <WORD>'
    * 'show system internal l2fwder Mac'
    * 'show system internal processes memory'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


# ====================================================================
# Schema for 'show system internal sysmgr service name <process>'
# ====================================================================
class ShowSystemInternalSysmgrServiceNameSchema(MetaParser):    
    """Schema for show system internal sysmgr service name <process>"""
    schema = {'instance':
                {Any():
                    {'tag':
                        {Any():
                            {'process_name': str,
                             'internal_id': int,
                             'uuid': str,
                             'state': str,
                             'plugin_id': str,
                             'state_start_date': str,
                             Optional('last_restart_date'): str,
                             Optional('pid'): int,
                             Optional('previous_pid'): int,
                             Optional('sap'): int,
                             Optional('restart_count'): int,
                             Optional('reboot_state'): str,
                             Optional('last_terminate_reason'): str}
                        },
                    }
                },
            }

class ShowSystemInternalSysmgrServiceName(
    ShowSystemInternalSysmgrServiceNameSchema):
    """Parser for show system internal sysmgr service name <process>"""

    cli_command = 'show system internal sysmgr service name {process}'

    def cli(self, process,output=None):
        if process:
            cmd = self.cli_command.format(process=process)
        else:
            cmd = ""
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # Service "bfdc" ("bfdc", 3):
        # Service "__inst_012__isis" ("isis", 61):
        # Service "feature-mgr" ("feature-mgr", 135):
        p1 = re.compile(r'^Service +\"(?P<inst>[\w\-]+)\" *'
                         '\(\"(?P<process_name>[\w\-]+)\", *'
                         '(?P<internal_id>\d+)\):$')

        # UUID = 0x2C7, PID = 6547, SAP = 1008
        # UUID = 0x59D, PID = 5418, no SAP
        # UUID = 0x42000118, -- Currently not running --
        p2 = re.compile(r'^UUID *= *(?P<uuid>\w+), *'
                         '((PID *= *(?P<pid>\d+), *'
                         '(SAP *= *(?P<sap>\d+)|no SAP))'
                         '|(-- Currently not running --))$')

        # State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Tue Mar 26 17:31:06 2013).
        # State: SRV_STATE_HAP_FAILED [unstable] (entered at time Thu Oct 26 13:46:32 2017).
        p3 = re.compile(r'^State: *(?P<state>[\w\s\[\]]+) *'
                         '\(entered +at +time +'
                         '(?P<state_start_date>[\w\s\:]+)\).$')

        # Restart count: 1
        p4 = re.compile(r'^Restart +count: +(?P<restart_count>\d+)$')

        # Time of last restart: Sat Jul  1 14:49:10 2017.
        p5 = re.compile(r'^Time +of +last +restart: +'
                         '(?P<last_restart_date>[\w\s\:]+).$')

        # The service never crashed since the last reboot.
        # The service has never been started since the last reboot.
        p6 = re.compile(r'The service never crashed since the last reboot.')

        # Previous PID: 2176
        p7 = re.compile(r'^Previous +PID: +(?P<previous_pid>\d+)$')

        # Reason of last termination: SYSMGR_DEATH_REASON_FAILURE_SIGNAL
        p8 = re.compile(r'^Reason +of +last +termination: +'
                         '(?P<last_terminate_reason>\w+)$')

        # Plugin ID: 0
        p9 = re.compile(r'^Plugin +ID: +(?P<plugin_id>\d+)$')

        # Tag = N/A
        # Tag = 100
        # Tag = l3vpn
        p10 = re.compile(r'^Tag *= *(?P<tag>(N\/A)|(\S+))$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                if 'instance' not in ret_dict:
                    ret_dict['instance'] = {}

                inst = m.groupdict()['inst']
                if inst not in ret_dict['instance']:
                    ret_dict['instance'][inst] = {}
                process_name = m.groupdict()['process_name']
                internal_id = int(m.groupdict()['internal_id'])

                # initial for each process
                pid = sap = restart_count = previous_pid = None
                last_restart_date = reboot_state = last_terminate_reason = None
                continue

            m = p2.match(line)
            if m:
                uuid = m.groupdict()['uuid']
                if m.groupdict()['pid']:
                    pid = int(m.groupdict()['pid'])
                else:
                    pid = None
                if m.groupdict()['sap']:
                    sap = int(m.groupdict()['sap'])
                else:
                    sap = None
                continue

            m = p3.match(line)
            if m:
                state = m.groupdict()['state'].strip()
                state_start_date = m.groupdict()['state_start_date']
                continue

            m = p4.match(line)
            if m:
                if m.groupdict()['restart_count']:
                    restart_count = int(m.groupdict()['restart_count'])
                else:
                    restart_count = None
                continue

            m = p5.match(line)
            if m:
                last_restart_date = m.groupdict()['last_restart_date']
                continue

            m = p6.match(line)
            if m:
                reboot_state = 'never_crashed'
                continue

            p6_1 = re.compile(r'The service has never been started since the last reboot.')
            m = p6_1.match(line)
            if m:
                reboot_state = 'never_started'
                continue

            m = p7.match(line)
            if m:
                previous_pid = int(m.groupdict()['previous_pid'])
                continue

            m = p8.match(line)
            if m:
                last_terminate_reason = m.groupdict()['last_terminate_reason']
                continue

            m = p9.match(line)
            if m:
                plugin_id = m.groupdict()['plugin_id']
                ret_dict['instance'][inst]['tag'][tag]['plugin_id'] = plugin_id
                continue

            m = p10.match(line)
            if m:
                tag = m.groupdict()['tag']
                if 'tag' not in ret_dict['instance'][inst]:
                    ret_dict['instance'][inst]['tag'] = {}
                if tag not in ret_dict['instance'][inst]['tag']:
                    ret_dict['instance'][inst]['tag'][tag] = {}

                if 'process_name':
                    ret_dict['instance'][inst]['tag'][tag]['process_name'] = process_name
                if 'internal_id':
                    ret_dict['instance'][inst]['tag'][tag]['internal_id'] = internal_id
                if 'uuid':
                    ret_dict['instance'][inst]['tag'][tag]['uuid'] = uuid
                if 'state':
                    ret_dict['instance'][inst]['tag'][tag]['state'] = state                    
                if 'state_start_date':
                    ret_dict['instance'][inst]['tag'][tag]['state_start_date'] = state_start_date

                if last_restart_date:
                    ret_dict['instance'][inst]['tag'][tag]\
                        ['last_restart_date'] = last_restart_date 

                if pid:
                    ret_dict['instance'][inst]['tag'][tag]['pid'] = pid 

                if previous_pid:
                    ret_dict['instance'][inst]['tag'][tag]\
                        ['previous_pid'] = previous_pid 

                if sap:
                    ret_dict['instance'][inst]['tag'][tag]['sap'] = sap 

                if restart_count:
                    ret_dict['instance'][inst]['tag'][tag]\
                        ['restart_count'] = restart_count

                if reboot_state:
                    ret_dict['instance'][inst]['tag'][tag]\
                        ['reboot_state'] = reboot_state

                if last_terminate_reason:
                    ret_dict['instance'][inst]['tag'][tag]\
                        ['last_terminate_reason'] = last_terminate_reason
                continue
        return ret_dict

# ====================================================================
# Schema for 'show system internal l2fwder Mac'
# ====================================================================
class ShowSystemInternalL2fwderMacSchema(MetaParser):    
    """Schema for show system internal l2fwder Mac"""

    schema = {'vlans':
                {Any():
                    {'mac_addresses':
                        {Any():
                            {'mac_type': str,
                             'mac_aging_time': str,
                             'entry': str,
                             'secure': str,
                             'ntfy': str,
                             'ports': str,
                            }
                        },
                    }
                },
            }

# ====================================================================
# Parser for 'show system internal l2fwder Mac'
# ====================================================================
class ShowSystemInternalL2fwderMac(ShowSystemInternalL2fwderMacSchema):
    """Parser for show system internal l2fwder Mac"""

    cli_command = 'show system internal l2fwder Mac'

    def cli(self,output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # G  1008    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
            p1 = re.compile(r'^\s*(?P<entry>[A-Z\*\(\+\)]+) +(?P<vlan>[0-9]+) '
                '+(?P<mac_address>[0-9a-z\.]+) +(?P<mac_type>[a-z]+) '
                '+(?P<age>[0-9\-\:]+) +(?P<secure>[A-Z]+) +(?P<ntfy>[A-Z]+) '
                '+(?P<ports>[a-zA-Z0-9\-\(\)\s\.\/]+)$')
            m = p1.match(line)
            if m:

                vlan = str(m.groupdict()['vlan'])
                mac_address = str(m.groupdict()['mac_address'])

                if 'vlans' not in ret_dict:
                    ret_dict['vlans'] = {}
                if vlan not in ret_dict['vlans']:
                    ret_dict['vlans'][vlan] = {}
                if 'mac_addresses' not in ret_dict['vlans'][vlan]:
                    ret_dict['vlans'][vlan]['mac_addresses'] = {}

                ret_dict['vlans'][vlan]['mac_addresses'][mac_address] = {}

                ret_dict['vlans'][vlan]['mac_addresses'][mac_address]['mac_type'] = \
                    str(m.groupdict()['mac_type'])
                ret_dict['vlans'][vlan]['mac_addresses'][mac_address]['mac_aging_time'] = \
                    str(m.groupdict()['age'])
                ret_dict['vlans'][vlan]['mac_addresses'][mac_address]['entry'] = \
                    str(m.groupdict()['entry'])
                ret_dict['vlans'][vlan]['mac_addresses'][mac_address]['secure'] = \
                    str(m.groupdict()['secure'])
                ret_dict['vlans'][vlan]['mac_addresses'][mac_address]['ntfy'] = \
                    str(m.groupdict()['ntfy'])
                ret_dict['vlans'][vlan]['mac_addresses'][mac_address]['ports'] = \
                    str(m.groupdict()['ports'])

                continue

        return ret_dict


class ShowSystemInternalKernelMeminfoSchema(MetaParser):
    """
    Schema for show system internal kernel meminfo
    """
    schema = {
        'mem': {
            'memtotal_kb': int,
            'memfree_kb': int,
            'memavailable_kb': int,
        },
        'buffers_kb': int,
        'cached_kb': int,
        'active': {
            'active_kb': int,
            'inactive_kb': int,
            'active(anon)_kb': int,
            'inactive(anon)_kb': int,
            'active(file)_kb': int,
            'inactive(file)_kb': int,
        },
        'unevictable_kb': int,
        'mlocked_kb': int,
        'swap': {
            'swapcached_kb': int,
            'swaptotal_kb': int,
            'swapfree_kb': int,
        },
        'dirty_kb': int,
        'writeback_kb': int,
        'anonpages_kb': int,
        'mapped_kb': int,
        'shmem_kb': int,
        'slab_kb': int,
        'sreclaimable_kb': int,
        'sunreclaim_kb': int,
        'kernelstack_kb': int,
        'pagetables_kb': int,
        'nfs_unstable_kb': int,
        'bounce_kb': int,
        'writebacktmp_kb': int,
        'commitlimit_kb': int,
        'committed_as_kb': int,
        'vmalloc': {
            'vmalloctotal_kb': int,
            'vmallocused_kb': int,
            'vmallocchunk_kb': int,
        },
        'hardwarecorrupted_kb': int,
        'hugepages': {
            'hugepages_total': int,
            'hugepages_free': int,
            'hugepages_rsvd': int,
            'hugepages_surp': int,
            'hugepagesize_kb': int,
        },
        'directmap4k_kb': int,
        'directmap2m_kb': int,
    }


class ShowSystemInternalKernelMeminfo(ShowSystemInternalKernelMeminfoSchema):
    """
    Parser for show system internal kernel meminfo
    """

    cli_command = 'show system internal system internal kernel meminfo'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # MemTotal:        5873172 kB
        p1 = re.compile(r'(?P<mem_type>Mem.+):\s+(?P<amount>\d+)\skB$')

        # Active(file):     236740 kB
        p2 = re.compile(r'(?i)(?P<active_state>[in]*active.*):\s+(?P<amount>\d+)\skB$')

        # SwapTotal:             0 kB
        p3 = re.compile(r'(?P<swap_type>Swap.+):\s+(?P<amount>\d+)\skB$')

        # VmallocChunk:   34359477316 kB
        p4 = re.compile(r'(?P<vmalloc_type>Vmalloc.+):\s+(?P<amount>\d+)\skB$')

        # HugePages_Surp:        0
        p5 = re.compile(r'(?P<hugepages_type>Huge.+):\s+(?P<amount>\d+)$')

        # Hugepagesize:       2048 kB
        p6 = re.compile(r'(?P<hugepages_type>Huge.+):\s+(?P<amount>\d+)\s+kB$')

        # Buffers:           38212 kB
        p7 = re.compile(r'(?P<key>.+):\s+(?P<amount>\d+)(\skB)?$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # MemTotal:        5873172 kB
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mem_dict = ret_dict.setdefault('mem', {})

                key = group['mem_type'].lower() + '_kb'
                mem_dict[key] = int(group['amount'])
                continue

            # Active(file):     236740 kB
            m = p2.match(line)
            if m:
                group = m.groupdict()
                active_dict = ret_dict.setdefault('active', {})

                key = group['active_state'].lower() + '_kb'
                active_dict[key] = int(group['amount'])
                continue

            # SwapTotal:             0 kB
            m = p3.match(line)
            if m:
                group = m.groupdict()
                swap_dict = ret_dict.setdefault('swap', {})

                key = group['swap_type'].lower() + '_kb'
                swap_dict[key] = int(group['amount'])
                continue

            # VmallocChunk:   34359477316 kB
            m = p4.match(line)
            if m:
                group = m.groupdict()
                vmalloc_dict = ret_dict.setdefault('vmalloc', {})

                key = group['vmalloc_type'].lower() + '_kb'
                vmalloc_dict[key] = int(group['amount'])
                continue

            # HugePages_Surp:        0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                hugepages_dict = ret_dict.setdefault('hugepages', {})

                key = group['hugepages_type'].lower()
                hugepages_dict[key] = int(group['amount'])
                continue

            # Hugepagesize:       2048 kB
            m = p6.match(line)
            if m:
                group = m.groupdict()
                hugepages_dict = ret_dict.setdefault('hugepages', {})

                key = group['hugepages_type'].lower() + '_kb'
                hugepages_dict[key] = int(group['amount'])
                continue

            # Buffers:           38212 kB
            m = p7.match(line)
            if m:
                group = m.groupdict()

                key = group['key'].lower() + '_kb'
                ret_dict[key] = int(group['amount'])
                continue

        return ret_dict


class ShowSystemResourcesSchema(MetaParser):
    """
    Schema for show system resources
    """

    schema = {
        'load_avg': {
            'load_avg_1min': float,
            'load_avg_5min': float,
            'load_avg_15min': float,
        },
        'processes': {
            'processes_total': int,
            'processes_running': int,
        },
        'cpu_state': {
            'cpu_state_user': float,
            'cpu_state_kernel': float,
            'cpu_state_idle': float,
            'cpus': {
                Any(): {
                    'cpu_state_user': float,
                    'cpu_state_kernel': float,
                    'cpu_state_idle': float,
                }
            }
        },
        'memory_usage': {
            'memory_usage_total_kb': int,
            'memory_usage_used_kb': int,
            'memory_usage_free_kb': int,
        },
        'kernel': {
            'kernel_vmalloc_total_kb': int,
            'kernel_vmalloc_free_kb': int,
            'kernel_buffers_kb': int,
            'kernel_cached_kb': int,
        },
        'current_memory_status': str,
    }


class ShowSystemResources(ShowSystemResourcesSchema):
    """
    Parser for show system resources
    """

    cli_command = 'show system resources'

    def cli(self, output=None):
        # execute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Load average:   1 minute: 0.34   5 minutes: 0.40   15 minutes: 0.66
        p1 = re.compile(r'^Load average\s*:\s+1 minute:\s+(?P<minute_one>[\d\.]+)\s+5 minutes:\s+'
                        r'(?P<minute_five>\d+\.\d+)\s+15 minutes:\s+(?P<minute_fifteen>\d+\.\d+)$')

        # Processes   :   901 total, 2 running
        p2 = re.compile(r'^Processes\s*:\s+(?P<processes_total>\d+)\s+total,\s+'
                        r'(?P<processes_running>\d+)\s+running$')

        # CPU states  :   2.11% user,   11.64% kernel,   86.24% idle
        #         CPU0 states  :   3.33% user,   12.22% kernel,   84.44% idle
        p3 = re.compile(r'^CPU(?P<cpu_num>\d*)\s+states\s+:\s+(?P<user>\d+\.\d+)%\s+user,\s+'
                        r'(?P<kernel>[\d+\.]+)%\s+kernel,\s+(?P<idle>\d+\.\d+)%\s+idle$')

        # Memory usage:   5873172K total,   4189652K used,   1683520K free
        p4 = re.compile(r'^Memory usage\s*:\s+(?P<total>\d+)K total,\s+'
                        r'(?P<used>\d+)K used,\s+(?P<free>\d+)K free$')

        # Kernel vmalloc:   0K total,   0K free
        p5 = re.compile(r'^Kernel vmalloc\s*:\s+(?P<total>\d+)'
                        r'K total,\s+(?P<free>\d+)K free$')

        # Kernel buffers:   144876K Used
        p6 = re.compile(r'^Kernel buffers\s*:\s+(?P<buffers>\d+)K Used$')

        # Kernel cached :   2296916K Used
        p7 = re.compile(r'^Kernel cached\s*:\s+(?P<cached>\d+)K Used$')

        # Current memory status: OK
        p8 = re.compile(r'^Current memory status\s*:\s+(?P<status>\w+)$')

        ret_dict = {}

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            # Load average:   1 minute: 0.34   5 minutes: 0.40   15 minutes: 0.66
            m = p1.match(line)
            if m:
                group = m.groupdict()

                load_avg_dict = ret_dict.setdefault('load_avg', {})

                load_avg_dict["load_avg_1min"] = float(group['minute_one'])
                load_avg_dict["load_avg_5min"] = float(group['minute_five'])
                load_avg_dict["load_avg_15min"] = float(group['minute_five'])
                continue

            # Processes   :   901 total, 2 running
            m = p2.match(line)
            if m:
                group = m.groupdict()

                processes_dict = ret_dict.setdefault('processes', {})
                processes_dict["processes_total"] = int(group['processes_total'])
                processes_dict["processes_running"] = int(group['processes_running'])
                continue

            # CPU states  :   2.11% user,   11.64% kernel,   86.24% idle
            #        CPU0 states  :   3.33% user,   12.22% kernel,   84.44% idle
            m = p3.match(line)
            if m:
                group = m.groupdict()

                cpu_state_dict = ret_dict.setdefault('cpu_state', {})

                if group['cpu_num']:
                    cpu_id_dict = cpu_state_dict.setdefault(
                        'cpus', {}).setdefault(int(group['cpu_num']), {})
                    cpu_id_dict['cpu_state_user'] = float(group['user'])
                    cpu_id_dict['cpu_state_kernel'] = float(group['kernel'])
                    cpu_id_dict['cpu_state_idle'] = float(group['idle'])
                    continue

                cpu_state_dict['cpu_state_user'] = float(group['user'])
                cpu_state_dict['cpu_state_kernel'] = float(group['kernel'])
                cpu_state_dict['cpu_state_idle'] = float(group['idle'])
                continue

            # Memory usage:   5873172K total,   4189652K used,   1683520K free
            m = p4.match(line)
            if m:
                group = m.groupdict()

                memory_usage_dict = ret_dict.setdefault('memory_usage', {})

                memory_usage_dict['memory_usage_total_kb'] = int(group['total'])
                memory_usage_dict['memory_usage_used_kb'] = int(group['used'])
                memory_usage_dict['memory_usage_free_kb'] = int(group['free'])
                continue

            # Kernel vmalloc:   0K total,   0K free
            m = p5.match(line)
            if m:
                group = m.groupdict()

                kernel_dict = ret_dict.setdefault('kernel', {})
                kernel_dict['kernel_vmalloc_total_kb'] = int(group['total'])
                kernel_dict['kernel_vmalloc_free_kb'] = int(group['free'])
                continue

            # Kernel buffers:   144876K Used
            m = p6.match(line)
            if m:
                group = m.groupdict()

                kernel_dict = ret_dict.setdefault('kernel', {})
                kernel_dict['kernel_buffers_kb'] = int(group['buffers'])
                continue

            # Kernel cached :   2296916K Used
            m = p7.match(line)
            if m:
                group = m.groupdict()

                kernel_dict = ret_dict.setdefault('kernel', {})
                kernel_dict['kernel_cached_kb'] = int(group['cached'])
                continue

            # Current memory status: OK
            m = p8.match(line)
            if m:
                ret_dict["current_memory_status"] = m.groupdict()['status']
                continue

        return ret_dict


class ShowSystemInternalProcessesMemorySchema(MetaParser):
    """
    Schema for show system internal processes memory
    """

    schema = {
        'pid':
            {
                Any():
                    {
                        'stat': str,
                        'time': str,
                        'majflt': int,
                        'trs': int,
                        'rss': int,
                        'vsz': int,
                        'mem_percent': float,
                        'command': str,
                        'tty': str
                    }
            }
    }


class ShowSystemInternalProcessesMemory(ShowSystemInternalProcessesMemorySchema):
    """
    Parser for show system internal processes memory
    """
    cli_command = "show system internal processes memory"

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # 7482 ?        Ssl  00:05:05    158    0 219576 1053628  3.7 /opt/mtx/bin/grpc -i 2626 -I
        # 27344 pts/0    Sl+  00:00:20      0   63 117180 709928  1.9 /isan/bin/vsh.bin
        p1 = re.compile(
            r'^(?P<pid>\d+)\s+(?P<tty>\S+)\s+(?P<stat>\S+)\s+(?P<time>[\d:]+)\s+(?P<majflt>\d+)\s+(?P<trs>\d+)\s+'
            r'(?P<rss>\d+)\s+(?P<vsz>\d+)\s+(?P<mem_percent>[\d.]+)\s+(?P<command>.+$)')

        ret_dict = {}

        for line in out.splitlines():
            stripped_line = line.strip()

            # 27344 pts/0    Sl+  00:00:20      0   63 117180 709928  1.9 /isan/bin/vsh.bin
            # 7482 ?        Ssl  00:05:05    158    0 219576 1053628  3.7 /opt/mtx/bin/grpc -i 2626 -I
            m = p1.match(stripped_line)
            if m:

                group = m.groupdict()

                pid = int(group['pid'])

                pid_dict = ret_dict.setdefault('pid', {}).setdefault(pid, {})

                pid_dict['stat'] = group['stat']
                pid_dict['majflt'] = int(group['majflt'])
                pid_dict['trs'] = int(group['trs'])
                pid_dict['rss'] = int(group['rss'])
                pid_dict['vsz'] = int(group['vsz'])
                pid_dict['mem_percent'] = float(group['mem_percent'])
                pid_dict['command'] = group['command']
                pid_dict['tty'] = group['tty']
                pid_dict['time'] = group['time']

        return ret_dict
