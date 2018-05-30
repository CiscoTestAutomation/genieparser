"""show_system.py

NXOS parsers for the following show commands:
    * 'show system internal sysmgr service name <WORD>'
    * 'show system internal l2fwder Mac'
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

    def cli(self, process):
        cmd = 'show system internal sysmgr service name {}'.format(process)
        out = self.device.execute(cmd)
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Service "bfdc" ("bfdc", 3):
            # Service "__inst_012__isis" ("isis", 61):
            # Service "feature-mgr" ("feature-mgr", 135):
            p1 = re.compile(r'^Service +\"(?P<inst>[\w\-]+)\" *'
                             '\(\"(?P<process_name>[\w\-]+)\", *'
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

                # initial for each process
                pid = sap = restart_count = previous_pid = None
                last_restart_date = reboot_state = last_terminate_reason = None
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
                else:
                    pid = None
                if m.groupdict()['sap']:
                    sap = int(m.groupdict()['sap'])
                else:
                    sap = None
                continue

            # State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Tue Mar 26 17:31:06 2013).
            # State: SRV_STATE_HAP_FAILED [unstable] (entered at time Thu Oct 26 13:46:32 2017).
            p3 = re.compile(r'^State: *(?P<state>[\w\s\[\]]+) *'
                             '\(entered +at +time +'
                             '(?P<state_start_date>[\w\s\:]+)\).$')
            m = p3.match(line)
            if m:
                state = m.groupdict()['state'].strip()
                state_start_date = m.groupdict()['state_start_date']
                continue

            # Restart count: 1
            p4 = re.compile(r'^Restart +count: +(?P<restart_count>\d+)$')
            m = p4.match(line)
            if m:
                if m.groupdict()['restart_count']:
                    restart_count = int(m.groupdict()['restart_count'])
                else:
                    restart_count = None
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

    def cli(self):
        cmd = 'show system internal l2fwder Mac'
        out = self.device.execute(cmd)
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # G  1008    5e01.8000.0007    static   -          F     F   sup-eth1(R)
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