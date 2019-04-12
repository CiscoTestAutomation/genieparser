'''show_issu.py

IOSXE parsers for the following show commands:
   * show issu state detail
   * show issu rollback-timer
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
                {'issu_in_progress': bool,
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
                },
            },
        }

# ====================================
#  Parser for 'show issu state detail'
# ====================================
class ShowIssuStateDetail(ShowIssuStateDetailSchema):

    """Parser for show issu state detail"""

    cli_command = 'show issu state detail'

    def cli(self,output=None):
        if output is None:
            # Execute command to get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init parsed dict
        ret_dict = {}

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
                continue

            # No ISSU operation is in progress
            # p1 = re.compile(r'^No ISSU operation is in progress$')
            m = p1.match(line)
            if m:
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

        return ret_dict


# ======================================
#  Schema for 'show issu rollback-timer'
# ======================================
class ShowIssuRollbackTimerSchema(MetaParser):

    """Schema for show issu rollback-timer"""

    schema = {
        'rollback_timer_state': str,
        'rollback_timer_reason': str,
        }

# ======================================
#  Parser for 'show issu rollback-timer'
# ======================================
class ShowIssuRollbackTimer(ShowIssuRollbackTimerSchema):

    """Parser for show issu rollback-timer"""

    cli_command = 'show issu rollback-timer'

    def cli(self,output=None):
        if output is None:
            # Execute command to get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init parsed dict
        ret_dict = {}

        # Compile regexp patterns

        # Rollback: inactive, no ISSU operation is in progress
        # Rollback: inactive, timer canceled by acceptversion
        p1 = re.compile(r'^Rollback: +(?P<state>(\S+)), +(?P<reason>.*)$')


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

        return ret_dict
