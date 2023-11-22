'''show_issu.py

IOSXE parsers for the following show commands:
   * show issu state detail
   * show issu rollback-timer
   * show issu clients
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                               Default, Use

# Genie Libs
from genie.libs.parser.utils.common import Common


# ====================================
#  Schema for 'show issu state detail'
# ====================================
class ShowIssuStateDetailSchema(MetaParser):

    """Schema for show issu state detail"""

    schema = {
        'slot':
            {Any():
                {
                Optional('issu_in_progress'): bool,
                Optional('loadversion_time'): str,
                Optional('context'): str,
                Optional('last_operation'): str,
                Optional('rollback_state'): str,
                Optional('rollback_time'): str,
                Optional('rollback_reason'): str,
                Optional('original_rollback_image'): str,
                Optional('running_image'): str,
                Optional('operating_mode'): str,
                Optional('terminal_state_reached'): bool,
                Optional('runversion_executed'): bool,
                Optional('boot_variable'): str,
                Optional('primary_version'): str,
                Optional('secondary_version'): str,
                Optional('variable_store'): str,
                Optional('issu_state'): str,
                Optional('rp_state'): str,
                Optional('current_status'): str,
                Optional('previous_operation'): str,
                Optional('system_check'): {
                    Optional('platform_issu_support'): str,
                    Optional('standby_online'): str,
                    Optional('autoboot_enabled'): str,
                    Optional('sso_mode'): str,
                    Optional('install_boot'): str,
                    Optional('valid_boot_media'): str,
                    Optional('opertional_mode'): str,
                },
            },
        },
    }

# ====================================
#  Parser for 'show issu state detail'
# ====================================
class ShowIssuStateDetail(ShowIssuStateDetailSchema):

    """Parser for show issu state detail"""

    cli_command = ['show issu state detail']

    def cli(self,output=None):
        if output is None:
            # Execute command to get output from device
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init parsed dict
        ret_dict = {}
        slot_info = False
        default_slot = 'R0'

        # Compile regexp patterns

        # Finished local lock acquisition on R0
        p0 = re.compile(r'^Finished +local +lock +acquisition'
                         ' +on +(switch *)?(?P<slot>(\S+))$')

        # No ISSU operation is in progress
        p1 = re.compile(r'^No +ISSU +operation +is +in +progress$')

        # Slot being modified: R1
        p2 = re.compile(r'^Slot +being +modified: +(?P<slot>(\S+))$')
        
        # Loadversion time: 20180430 19:13:51 on vty 0
        p3 = re.compile(r'^Loadversion +time: +(?P<date>(\S+))'
                         ' +(?P<time>(\S+))(?: +on +(?P<context>.*))?$')

        # Last operation: loadversion
        p4 = re.compile(r'^Last +operation:'
            ' (?P<last>(loadversion|runversion|acceptversion|commitversion))$')

        # Rollback: automatic, remaining time before rollback: 00:35:58
        p5_1 = re.compile(r'^Rollback: +(?P<state>(automatic)), +remaining +time'
                           ' +before +rollback: +(?P<time>(\S+))$')

        # Rollback: inactive, timer canceled by acceptversion
        p5_2 = re.compile(r'^Rollback: +(?P<state>(inactive)), +(?P<reason>.*)$')

        # Original (rollback) image: harddisk:asr1000rpx86-universalk9.16.08.01sprd1.SPA.bin
        p6 = re.compile(r'^Original +\(rollback\) +image: +(?P<orig_image>(\S+))$')

        # Running image: harddisk:asr1000rpx86-universalk9.BLD_V168_1_THROTTLE_LATEST_20180426_165658_V16_8_0_265.SSA.bin
        p7 = re.compile(r'^Running +image: +(?P<run_image>(\S+))$')

        # Operating mode: sso, terminal state not reached
        p8 = re.compile(r'^Operating +mode: +(?P<mode>(\S+)), +terminal +state'
                         ' +(?P<terminal_state>(reached|not reached))$')

        # Notes: runversion executed, active RP is being provisioned
        p9 = re.compile(r'^Notes: +runversion +executed, +active +RP +is +being'
                         ' +provisioned$')

        # Slot = 1
        p10 = re.compile(r'Slot\s*=\s*(?P<slot>\d+)')

        # RP State = Active
        p11 = re.compile(r'RP\s+State\s*=\s*(?P<state>.+)')

        # ISSU State = Init
        p12 = re.compile(r'ISSU\s+State\s*=\s*(?P<issu_state>.+)')

        # Boot Variable = bootdisk:,1;
        p13 = re.compile(r'Boot\s+Variable\s*=\s*(?P<boot_variable>.+)')

        # Operating Mode = sso
        p14 = re.compile(r'Operating\s+Mode\s*=\s*(?P<operating_mode>.+)')

        # Primary Version = N/A
        p15 = re.compile(r'Primary\s+Version\s*=\s*(?P<primary_version>.+)')

        # Secondary Version = N/A
        p16 = re.compile(r'Secondary\s+Version\s*=\s*(?P<secondary_version>.+)')

        # Current Version = bootdisk:s2t54-adventerprisek9-mz.SPA.151-1.SY.bin
        p17 = re.compile(r'Current\s+Version\s*=\s*(?P<current_version>.+)')

        # Variable Store = PrstVbl
        p18 = re.compile(r'Variable\s+Store\s*=\s*(?P<variable_store>.+)')

        # Current ISSU Status: Disabled
        p19 = re.compile(r'^Current +ISSU +Status: +(?P<current_status>(\S+))$')
        
        # Previous ISSU Operation: N/A
        p20 = re.compile(r'^Previous +ISSU +Operation: +(?P<previous_operation>(\S+))$')

        # System Check                        Status
        p21 = re.compile(r'^System +Check +Status$')

        # Platform ISSU Support               No
        p22 = re.compile(r'^Platform +ISSU +Support +(?P<platform_issu_support>(\S+))$')

        # Standby Online                      No
        p23 = re.compile(r'^Standby +Online +(?P<standby_online>(\S+))$')

        # Autoboot Enabled                    Yes
        p24 = re.compile(r'^Autoboot +Enabled +(?P<autoboot_enabled>(\S+))$')

        # SSO Mode                            No
        p25 = re.compile(r'^SSO +Mode +(?P<sso_mode>(\S+))$')

        # Install Boot                        No
        p26 = re.compile(r'^Install +Boot +(?P<install_boot>(\S+))$')

        # Valid Boot Media                    Yes
        p27 = re.compile(r'^Valid +Boot +Media +(?P<valid_boot_media>(\S+))$')

        # Operational Mode                    HA-REMOTE
        p28 = re.compile(r'^Operational +Mode +(?P<opertional_mode>(\S+))$')

        # Parse all lines
        for line in out.splitlines():
            line = line.strip()
            
            # Finished local lock acquisition on R0
            # p0 = re.compile(r'^Finished +local +lock +acquisition'
            #                  ' +on +(?P<slot>(\S+))$')
            m = p0.match(line)
            if m:
                slot = m.groupdict()['slot']
                slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {})
                slot_dict['issu_in_progress'] = False
                slot_info = True
                continue

            # No ISSU operation is in progress
            # p1 = re.compile(r'^No ISSU operation is in progress$')
            m = p1.match(line)
            if m:
                if slot_info is False:
                    slot_dict = ret_dict.setdefault('slot', {}).setdefault(default_slot, {})
                    slot_info = True
                if 'slot' in ret_dict:
                    slot_dict['issu_in_progress'] = False
                continue

            # Slot being modified: R1
            # p2 = re.compile(r'^Slot +being +modified: +(?P<slot>(\S+))$')
            m = p2.match(line)
            if m:
                modified_slot = m.groupdict()['slot']
                if slot == modified_slot:
                    slot_dict['issu_in_progress'] = True
                    slot_dict['runversion_executed'] = False
                continue

            # Loadversion time: 20180430 19:13:51 on vty 0
            # p3 = re.compile(r'^Loadversion +time: +(?P<date>(\S+))'
            #                  ' +(?P<time>(\S+))(?: +on +(?P<context>.*))?$')
            m = p3.match(line)
            if m:
                group = m.groupdict()
                slot_dict['loadversion_time'] = group['date'] + ' ' + group['time']
                slot_dict['context'] = group['context']
                continue

            # Last operation: loadversion
            # p4 = re.compile(r'^Last +operation:'
            # ' (?P<last>(loadversion|runversion|acceptversion|commitversion))$')
            m = p4.match(line)
            if m:
                slot_dict['last_operation'] = m.groupdict()['last']
                continue

            # Rollback: automatic, remaining time before rollback: 00:35:58
            # p5_1 = re.compile(r'^Rollback: +(?P<state>(automatic)), +remaining +time'
            #                    ' +before +rollback: +(?P<rollback_time>(\S+))$')
            m = p5_1.match(line)
            if m:
                group = m.groupdict()
                slot_dict['rollback_state'] = group['state']
                slot_dict['rollback_time'] = group['time']
                continue

            # Rollback: inactive, timer canceled by acceptversion
            # p5_2 = re.compile(r'^Rollback: +(?P<state>(inactive)),'
            #                ' +(?P<reason>[a-zA-Z0-9\s+])$')
            m = p5_2.match(line)
            if m:
                group = m.groupdict()
                slot_dict['rollback_state'] = group['state']
                slot_dict['rollback_reason'] = group['reason']
                continue

            # Original (rollback) image: harddisk:asr1000rpx86-universalk9.16.08.01sprd1.SPA.bin
            # p6 = re.compile(r'^Original +\(rollback\) +image: +(?P<image>(\S+))$')
            m = p6.match(line)
            if m:
                slot_dict['original_rollback_image'] = m.groupdict()['orig_image']
                continue

            # Running image: harddisk:asr1000rpx86-universalk9.BLD_V168_1_THROTTLE_LATEST_20180426_165658_V16_8_0_265.SSA.bin
            # p7 = re.compile(r'^Running +image: +(?P<run_image>(\S+))$')
            m = p7.match(line)
            if m:
                slot_dict['running_image'] = m.groupdict()['run_image']
                continue

            # Operating mode: sso, terminal state not reached
            # p8 = re.compile(r'^Operating +mode: +(?P<mode>(\S+)), +terminal +state'
            #                  ' +(?P<terminal_state>(reached|not reached))$')
            m = p8.match(line)
            if m:
                slot_dict['operating_mode'] = m.groupdict()['mode']
                if 'not' in m.groupdict()['terminal_state']:
                    slot_dict['terminal_state_reached'] = False
                else:
                    slot_dict['terminal_state_reached'] = True
                continue

            # Notes: runversion executed, active RP is being provisioned
            # p9 = re.compile(r'^Notes: +runversion +executed, +active +RP +is +being'
            #              ' +provisioned$')
            m = p9.match(line)
            if m:
                slot_dict['runversion_executed'] = True
                continue

            # Slot = 1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                slot = 'R{}'.format(group['slot'])
                slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {})
                continue

            # RP State = Active
            m = p11.match(line)
            if m:
                group = m.groupdict()
                state = group['state']
                slot_dict['rp_state'] = state
                continue

            # ISSU State = Init
            m = p12.match(line)
            if m:                
                group = m.groupdict()
                issu_state = group['issu_state']
                slot_dict['issu_state'] = issu_state
                continue
            # Boot Variable = bootdisk:,1;
            m = p13.match(line)
            if m:                
                group = m.groupdict()
                boot_variable = group['boot_variable']
                slot_dict['boot_variable'] = boot_variable
                continue

            # Operating Mode = sso
            m = p14.match(line)
            if m:                
                group = m.groupdict()
                operating_mode = group['operating_mode']
                slot_dict['operating_mode'] = operating_mode
                continue

            # Primary Version = N/A
            m = p15.match(line)
            if m:                
                group = m.groupdict()
                primary_version = group['primary_version']
                slot_dict['primary_version'] = primary_version
                continue

            # Secondary Version = N/A
            m = p16.match(line)
            if m:                
                
                group = m.groupdict()
                secondary_version = group['secondary_version']
                slot_dict['secondary_version'] = secondary_version
                continue

            # Current Version = bootdisk:s2t54-adventerprisek9-mz.SPA.151-1.SY.bin
            m = p17.match(line)
            if m:
                group = m.groupdict()
                current_version = group['current_version']
                slot_dict['running_image'] = current_version
                continue
            
            # Variable Store = PrstVbl
            m = p18.match(line)
            if m:
                group = m.groupdict()                
                variable_store = group['variable_store']
                slot_dict['variable_store'] = variable_store
                continue

            # Current ISSU Status: Disabled
            # p19 = re.compile(r'^Current +ISSU +Status: +(?P<current_status>(\S+))$')
            m = p19.match(line)
            if m:
                if slot_info is False:
                    slot_dict = ret_dict.setdefault('slot', {}).setdefault(default_slot, {})
                    slot_info = True
                current_status = m.groupdict()['current_status']
                slot_dict['current_status'] = current_status
                continue

            # Previous ISSU Operation: N/A
            # p20 = re.compile(r'^Previous +ISSU +Operation: +(?P<previous_operation>([\S\/]+))$')
            m = p20.match(line)
            if m:
                previous_operation = m.groupdict()['previous_operation']
                slot_dict['previous_operation'] = previous_operation
                continue

            # System Check                        Status
            # p21 = re.compile(r'^System +Check +Status$')
            m = p21.match(line)
            if m:
                slot_dict.setdefault('system_check', {})
                continue

            # Platform ISSU Support               No
            # p22 = re.compile(r'^Platform +ISSU +Support +(?P<platform_issu_support>(\S+))$')
            m = p22.match(line)
            if m:
                platform_issu_support = m.groupdict()['platform_issu_support']
                slot_dict['system_check']['platform_issu_support'] = platform_issu_support
                continue

            # Standby Online                      No
            # p23 = re.compile(r'^Standby +Online +(?P<standby_online>(\S+))$')
            m = p23.match(line)
            if m:
                standby_online = m.groupdict()['standby_online']
                slot_dict['system_check']['standby_online'] = standby_online
                continue

            # Autoboot Enabled                    Yes
            # p24 = re.compile(r'^Autoboot +Enabled +(?P<autoboot_enabled>(\S+))$')
            m = p24.match(line)
            if m:
                autoboot_enabled = m.groupdict()['autoboot_enabled']
                slot_dict['system_check']['autoboot_enabled'] = autoboot_enabled
                continue

            # SSO Mode                            No
            # p25 = re.compile(r'^SSO +Mode +(?P<sso_mode>(\S+))$')
            m = p25.match(line)
            if m:
                sso_mode = m.groupdict()['sso_mode']
                slot_dict['system_check']['sso_mode'] = sso_mode
                continue

            # Install Boot                        No
            # p26 = re.compile(r'^Install +Boot +(?P<install_boot>(\S+))$')
            m = p26.match(line)
            if m:
                install_boot = m.groupdict()['install_boot']
                slot_dict['system_check']['install_boot'] = install_boot
                continue

            # Valid Boot Media                    Yes
            # p27 = re.compile(r'^Valid +Boot +Media +(?P<valid_boot_media>(\S+))$')
            m = p27.match(line)
            if m:
                valid_boot_media = m.groupdict()['valid_boot_media']
                slot_dict['system_check']['valid_boot_media'] = valid_boot_media
                continue

            # Operational Mode                    HA-REMOTE 
            #p28 = re.compile(r'^Operational +Mode +(?P<opertional_mode>(\S+))$')
            m = p28.match(line)
            if m:
                opertional_mode = m.groupdict()['opertional_mode']
                slot_dict['system_check']['opertional_mode'] = opertional_mode
                continue

        return ret_dict


# ======================================
#  Schema for 'show issu rollback-timer'
# ======================================
class ShowIssuRollbackTimerSchema(MetaParser):

    """Schema for show issu rollback-timer"""

    schema = {
        'rollback_timer_state': str,
        Optional('rollback_timer_reason'): str,
        Optional('rollback_timer_time'): str,
        }

# ======================================
#  Parser for 'show issu rollback-timer'
# ======================================
class ShowIssuRollbackTimer(ShowIssuRollbackTimerSchema):

    """Parser for show issu rollback-timer"""

    cli_command = ['show issu rollback-timer']

    def cli(self,output=None):

        if output is None:
            # Execute command to get output from device
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init parsed dict
        ret_dict = {}

        # Compile regexp patterns

        # Rollback: inactive, no ISSU operation is in progress
        # Rollback: inactive, timer canceled by acceptversion
        p1 = re.compile(r'^Rollback: +(?P<state>(\S+)), +(?P<reason>.*)$')

        # Rollback Process State = Not in progress
        p2 = re.compile(r'Rollback\s+Process\s+State\s*=\s*(?P<state>.+)')

        # Configured Rollback Time = 00:45:00
        p3 = re.compile(r'Configured\s+Rollback\s+Time\s*=\s*(?P<rollback_time>.+)')

        # Parse all lines
        for line in out.splitlines():
            line = line.strip()

            # Rollback: inactive, no ISSU operation is in progress
            # Rollback: inactive, timer canceled by acceptversion
            # p1 = re.compile(r'^Rollback: +(?P<state>(\S+)), +(?P<reason>.*)$')
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rollback_timer_state'] = group['state']
                ret_dict['rollback_timer_reason'] = group['reason']
                continue

            # Rollback Process State = Not in progress
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rollback_timer_state'] = group['state']
                continue

            # Configured Rollback Time = 00:45:00
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rollback_timer_time'] = group['rollback_time']                
                continue

        return ret_dict


class ShowIssuClientsSchema(MetaParser):
    """Schema for show issu clients"""
    schema = {
        'issu_clients':
            {Any():
                {
                'client_id': int,
                'client_name': str,
                'entity_count': int,
                },
            'base_client_name': list,
        },
    }


class ShowIssuClients(ShowIssuClientsSchema):
    """Parser for show issu rollback-timer"""

    cli_command = ['show issu clients']

    def cli(self,output=None):
        if output is None:
            # Execute command to get output from device
            out = self.device.execute(self.cli_command[0])

        # Init parsed dict
        ret_dict = {}
        #ret_dict['base_client_name'] =[]
        

        # Compile regexp patterns
        # Client_ID = 2, Client_Name = ISSU Proto client,  Entity_Count = 1
        p0 = re.compile(r'^Client_ID += +(?P<client_id>\d+), +Client_Name += +(?P<client_name>[\w ]+), +Entity_Count += +(?P<entity_count>\d+)$')

        #Base Clients:
        p1 = re.compile(r'^Base +Clients:$')

        # Client_Name = ISSU Proto client
        p2 = re.compile(r'^Client_Name += +(?P<base_client_name>[\w ]+)$')

        # Parse all lines
        for line in out.splitlines():
            line = line.strip()
            
            # Client_ID = 2, Client_Name = ISSU Proto client,  Entity_Count = 1
            #p0 = re.compile(r'^\s+Client_ID += +(?P<client_id>\d+), +Client_Name += +(?P<client_name>[\w ]+), +Entity_Count += +(?P<entity_count>\d+)'$)
            m = p0.match(line)
            if m:
                group = m.groupdict()
                issu_clients_dict = ret_dict.setdefault('issu_clients', {}).setdefault(int(group['client_id']), {})
                issu_clients_dict.update({'client_id': int(group['client_id'])})
                issu_clients_dict.update({'client_name': group['client_name']})
                issu_clients_dict.update({'entity_count': int(group['entity_count'])})
                continue

            #Base Clients:
            #p1 = re.compile(r'^Base +Clients:$')
            m = p1.match(line)
            if m:
                group = m.groupdict()
                continue

            # Client_Name = ISSU Proto client
            #p2 = re.compile(r'^\s+Client_Name += +(?P<base_client_name>[\w ]+)$')
            m = p2.match(line)
            if m:
                group = m.groupdict()
                base_clients_dict = ret_dict.setdefault('issu_clients', {}).setdefault('base_client_name', [])
                base_clients_dict.append(group['base_client_name'])
                continue
        return ret_dict
