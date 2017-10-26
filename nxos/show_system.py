''' show_system.py

NXOS parsers for the following show commands:
    * 'show system internal sysmgr service name <WORD>'
'''

# Python
import re

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


# ====================================================================
# Parser for 'show system internal sysmgr service name <WORD>'
# ====================================================================
class ShowSystemInternalSysmgrServiceNameSchema(MetaParser):    
    '''Schema for show system internal sysmgr service name <WORD>'''
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
    '''Parser for show system internal sysmgr service name <WORD>'''

    def cli(self, process):
        cmd = 'show system internal sysmgr service name {}'.format(process)
        out = self.device.execute(cmd)
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Service "bfdc" ("bfdc", 3):
            # Service "__inst_012__isis" ("isis", 61):
            p1 = re.compile(r'^Service +\"(?P<inst>\w+)\" *'
                             '\(\"(?P<process_name>\w+)\", *'
                             '(?P<internal_id>\d+)\):$')
            m = p1.match(line)
            if m:
                if 'instance' not in ret_dict:
                    ret_dict['instance'] = {}

                inst = m.groupdict()['inst']
                if inst not in ret_dict['instance']:
                    ret_dict['instance'][inst] = {}
                process_name = m.groupdict()['process_name']
                internal_id = int(m.groupdict()['internal_id'])
                continue

            # UUID = 0x2C7, PID = 6547, SAP = 1008
            # UUID = 0x42000118, -- Currently not running --
            p2 = re.compile(r'^UUID *= *(?P<uuid>\w+), *'
                             '((PID *= *(?P<pid>\d+), *'
                             'SAP *= *(?P<sap>\d+))'
                             '|(-- Currently not running --))$')
            m = p2.match(line)
            if m:
                uuid = m.groupdict()['uuid']
                if m.groupdict()['pid']:
                    pid = int(m.groupdict()['pid'])
                if m.groupdict()['sap']:
                    sap = int(m.groupdict()['sap'])
                continue

            # State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Tue Mar 26 17:31:06 2013).
            p3 = re.compile(r'^State: *(?P<state>\w+) *'
                             '\(entered +at +time +'
                             '(?P<state_start_date>[\w\s\:]+)\).$')
            m = p3.match(line)
            if m:
                state = m.groupdict()['state']
                state_start_date = m.groupdict()['state_start_date']
                continue

            # Restart count: 1
            p4 = re.compile(r'^Restart +count: +(?P<restart_count>\d+)$')
            m = p4.match(line)
            if m:
                if m.groupdict()['restart_count']:
                    restart_count = int(m.groupdict()['restart_count'])
                continue

            # Time of last restart: Sat Jul  1 14:49:10 2017.
            p5 = re.compile(r'^Time +of +last +restart: +'
                             '(?P<last_restart_date>[\w\s\:]+).$')
            m = p5.match(line)
            if m:
                last_restart_date = m.groupdict()['last_restart_date']
                continue

            # The service never crashed since the last reboot.
            # The service has never been started since the last reboot.
            p6 = re.compile(r'The service never crashed since the last reboot.')
            m = p6.match(line)
            if m:
                reboot_state = 'never_crashed'
                continue

            p6_1 = re.compile(r'The service has never been started since the last reboot.')
            m = p6_1.match(line)
            if m:
                reboot_state = 'never_started'
                continue

            # Previous PID: 2176
            p7 = re.compile(r'^Previous +PID: +(?P<previous_pid>\d+)$')
            m = p7.match(line)
            if m:
                if m.groupdict()['previous_pid']:
                    previous_pid = int(m.groupdict()['previous_pid'])
                continue

            # Reason of last termination: SYSMGR_DEATH_REASON_FAILURE_SIGNAL
            p8 = re.compile(r'^Reason +of +last +termination: +'
                             '(?P<last_terminate_reason>\w+)$')
            m = p8.match(line)
            if m:
                last_terminate_reason = m.groupdict()['last_terminate_reason']
                continue

            # Plugin ID: 0
            p9 = re.compile(r'^Plugin +ID: +(?P<plugin_id>\d+)$')
            m = p9.match(line)
            if m:
                plugin_id = m.groupdict()['plugin_id']
                ret_dict['instance'][inst]['tag'][tag]['plugin_id'] = plugin_id
                continue

            # Tag = N/A
            # Tag = 100
            p10 = re.compile(r'^Tag *= *(?P<tag>(N\/A)|(\d+))$')
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

                try:
                    last_restart_date
                except:
                    pass
                else:
                    ret_dict['instance'][inst]['tag'][tag]\
                        ['last_restart_date'] = last_restart_date 
                try:
                    pid
                except:
                    pass
                else:
                    ret_dict['instance'][inst]['tag'][tag]['pid'] = pid 
                try:
                    previous_pid
                except:
                    pass
                else:
                    ret_dict['instance'][inst]['tag'][tag]\
                        ['previous_pid'] = previous_pid 
                try:
                    sap
                except:
                    pass
                else:
                    ret_dict['instance'][inst]['tag'][tag]['sap'] = sap 
                try:
                    restart_count
                except:
                    pass
                else:
                    ret_dict['instance'][inst]['tag'][tag]\
                        ['restart_count'] = restart_count

                try:
                    reboot_state
                except:
                    pass
                else:
                    ret_dict['instance'][inst]['tag'][tag]\
                        ['reboot_state'] = reboot_state
                try:
                    last_terminate_reason
                except:
                    pass
                else:
                    ret_dict['instance'][inst]['tag'][tag]\
                        ['last_terminate_reason'] = last_terminate_reason
                continue
        return ret_dict
