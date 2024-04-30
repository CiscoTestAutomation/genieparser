'''show_issu.py

IOSXE c9500 parsers for the following show commands:
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
                {
                Optional('issu_in_progress'): bool,
                Optional('current_status'): str,
                Optional('previous_operation'): str,
                Optional('system_check'): {
                    Optional('platform_issu_support'): str,
                    Optional('standby_online'): str,
                    Optional('autoboot_enabled'): str,
                    Optional('sso_mode'): str,
                    Optional('install_boot'): str,
                    Optional('valid_boot_media'): str,
                }
            },
        },
    }

# ====================================
#  Parser for 'show issu state detail'
# ====================================
class ShowIssuStateDetail(ShowIssuStateDetailSchema):

    """Parser for show issu state detail"""

    cli_command = ['show issu state detail']

    def cli(self, output=None):

        if output is None:
            # Execute command to get output from device
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init parsed dict
        ret_dict = {}

        # Compile regexp patterns

        # Finished local lock acquisition on R0
        p0 = re.compile(r'^Finished +local +lock +acquisition'
                         ' +on +(?P<slot>(\S+))$')

        # No ISSU operation is in progress
        p1 = re.compile(r'^No +ISSU +operation +is +in +progress$')

        # Current ISSU Status: Disabled
        p2 = re.compile(r'^Current +ISSU +Status: +(?P<current_status>(\S+))$')
        
        # Previous ISSU Operation: N/A
        p3 = re.compile(r'^Previous +ISSU +Operation: +(?P<previous_operation>(\S+))$')

        # System Check                        Status
        p4 = re.compile(r'^System +Check +Status$')

        # Platform ISSU Support               No
        p5 = re.compile(r'^Platform +ISSU +Support +(?P<platform_issu_support>(\S+))$')

        # Standby Online                      No
        p6 = re.compile(r'^Standby +Online +(?P<standby_online>(\S+))$')

        # Autoboot Enabled                    Yes
        p7 = re.compile(r'^Autoboot +Enabled +(?P<autoboot_enabled>(\S+))$')

        # SSO Mode                            No
        p8 = re.compile(r'^SSO +Mode +(?P<sso_mode>(\S+))$')

        # Install Boot                        No
        p9 = re.compile(r'^Install +Boot +(?P<install_boot>(\S+))$')

        # Valid Boot Media                    Yes
        p10 = re.compile(r'^Valid +Boot +Media +(?P<valid_boot_media>(\S+))$')

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

            # Current ISSU Status: Disabled
            # p2 = re.compile(r'^Current +ISSU +Status: +(?P<current_status>(\S+))$')
            m = p2.match(line)
            if m:
                current_status = m.groupdict()['current_status']
                slot_dict['current_status'] = current_status
                continue

            # Previous ISSU Operation: N/A
            # p3 = re.compile(r'^Previous +ISSU +Operation: +(?P<previous_operation>([\S\/]+))$')
            m = p3.match(line)
            if m:
                previous_operation = m.groupdict()['previous_operation']
                slot_dict['previous_operation'] = previous_operation
                continue

            # System Check                        Status
            # p4 = re.compile(r'^System +Check +Status$')
            m = p4.match(line)
            if m:
                slot_dict.setdefault('system_check', {})
                continue

            # Platform ISSU Support               No
            # p5 = re.compile(r'^Platform +ISSU +Support +(?P<platform_issu_support>(\S+))$')
            m = p5.match(line)
            if m:
                platform_issu_support = m.groupdict()['platform_issu_support']
                slot_dict['system_check']['platform_issu_support'] = platform_issu_support
                continue

            # Standby Online                      No
            # p6 = re.compile(r'^Standby +Online +(?P<standby_online>(\S+))$')
            m = p6.match(line)
            if m:
                standby_online = m.groupdict()['standby_online']
                slot_dict['system_check']['standby_online'] = standby_online
                continue

            # Autoboot Enabled                    Yes
            # p7 = re.compile(r'^Autoboot +Enabled +(?P<autoboot_enabled>(\S+))$')
            m = p7.match(line)
            if m:
                autoboot_enabled = m.groupdict()['autoboot_enabled']
                slot_dict['system_check']['autoboot_enabled'] = autoboot_enabled
                continue

            # SSO Mode                            No
            # p8 = re.compile(r'^SSO +Mode +(?P<sso_mode>(\S+))$')
            m = p8.match(line)
            if m:
                sso_mode = m.groupdict()['sso_mode']
                slot_dict['system_check']['sso_mode'] = sso_mode
                continue

            # Install Boot                        No
            # p9 = re.compile(r'^Install +Boot +(?P<install_boot>(\S+))$')
            m = p9.match(line)
            if m:
                install_boot = m.groupdict()['install_boot']
                slot_dict['system_check']['install_boot'] = install_boot
                continue

            # Valid Boot Media                    Yes
            # p10 = re.compile(r'^Valid +Boot +Media +(?P<valid_boot_media>(\S+))$')
            m = p10.match(line)
            if m:
                valid_boot_media = m.groupdict()['valid_boot_media']
                slot_dict['system_check']['valid_boot_media'] = valid_boot_media
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

    def cli(self, output=None):

        if output is None:
            # Execute command to get output from device
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init parsed dict
        ret_dict = {}

        # Compile regexp patterns

        # Rollback: inactive, no ISSU operation is in progress
        p1 = re.compile(r'^Rollback: +(?P<state>(\S+)), +(?P<reason>.*)$')

        # Rollback Process State = Not in progress
        p2 = re.compile(r'Rollback\s+Process\s+State\s*=\s*(?P<state>.+)')

        # Configured Rollback Time = 00:45:00
        p3 = re.compile(r'Configured\s+Rollback\s+Time\s*=\s*(?P<rollback_time>.+)')

        # Parse all lines
        for line in out.splitlines():
            line = line.strip()

            # Rollback: inactive, no ISSU operation is in progress
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
