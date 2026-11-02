'''

IOSXE parsers for the following show commands:
    * acm log
    * acm log confirm-commit
    * acm log merge
    * acm log replace
    * acm log save
    * acm log <1-50>

'''
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ====================
# Schema for:
#  * 'acm configlet status'
# ====================
class AcmConfigletStatusSchema(MetaParser):
    """Schema for 'acm configlet status'."""
    schema = {
        'configlets': {
            Any(): {
                'terminal': str,
                Optional('user'): str,
                'cli_count': int,
                'configlet_data': list
            }
        }
    }

class AcmConfigletStatus(AcmConfigletStatusSchema):
    cli_command = 'acm configlet status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        if not output.strip():
            return {}  # <-- This is the key fix

        configlets = {}
        current_name = None

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            if line.startswith("Configlet Name"):
                current_name = line.split(":", 1)[1].strip()
                configlets[current_name] = {
                    'terminal': '',
                    'cli_count': 0,
                    'configlet_data': []
                }

            elif line.startswith("Terminal, User") and current_name:
                parts = line.split(":", 1)[1].split(",")
                configlets[current_name]['terminal'] = parts[0].strip()
                if len(parts) > 1 and parts[1].strip():
                    configlets[current_name]['user'] = parts[1].strip()

            elif line.startswith("CLI Count") and current_name:
                try:
                    configlets[current_name]['cli_count'] = int(line.split(":", 1)[1].strip())
                except ValueError:
                    configlets[current_name]['cli_count'] = 0  # default fallback

            elif re.match(r'^\d+\s+.+', line) and current_name:
                cmd = re.sub(r'^\d+\s+', '', line)
                configlets[current_name]['configlet_data'].append(cmd)

        return {'configlets': configlets}
        
# ====================
# Schema for:
#  * 'acm merge <configlet_file> validate'
# ====================
class AcmMergeValidateSchema(MetaParser):
    """Schema for acm merge <configlet_file> validate."""
    schema = {
        Optional("configlet_file_name"): str,
        Optional("validation_status"): str,
        Optional("validation_time"): str,
        Optional("failed_command"): str,
        Optional("failed_reason"): str,
        Optional("platform_status"): str,
        Optional("invalid_file"): str
    }


class AcmMergeValidate(AcmMergeValidateSchema):
    """Parser for acm merge <configlet_file> validate"""

    cli_command = 'acm merge {configlet_file} validate'

    def cli(self, configlet_file='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(configlet_file=configlet_file))

        ret_dict = {}
        failed_command_lines = []
        failed_reason_lines = []
        state = None
        failed_reason_check = False

        # Old format patterns
        p_old_configlet = re.compile(r'^Validatating +the +configlet (?P<configlet_file>\S+)$')
        p_old_status = re.compile(r'^Validation +(?P<validation_status>success|failed)$', re.IGNORECASE)
        p_old_time = re.compile(r'^Validation +Time: (?P<validation_time>[\w\s]+)$')
        p_old_failed_cmd = re.compile(r'^Failed +command: (?P<failed_command>.*)$')
        p_old_failed_reason = re.compile(r'^Failed +reason:$')
        p_old_reason_detail = re.compile(r'(?P<failed_reason>[\S\s]+)$')
        p_old_platform = re.compile(r'^Validation +on +platform (?P<platform_status>not supported)$')
        p_old_invalid_file = re.compile(r'^%Error: +Invalid file: (?P<invalid_file>\S+)$')

        # New format patterns
        p_new_configlet = re.compile(r'^Config +Validation +of +Configlet: +(?P<configlet_file>\S+)$')
        p_new_status = re.compile(r'^Status\s*:\s*(?P<validation_status>\w+)$', re.IGNORECASE)
        p_new_time = re.compile(r'^Time\s*:\s*(?P<validation_time>\d+ +msec)$')
        p_new_failed_cmd = re.compile(r'^Failed +command:')
        p_new_failed_reason = re.compile(r'^Failed +reason:')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Old format parsing
            m = p_old_configlet.match(line)
            if m:
                ret_dict['configlet_file_name'] = m.group('configlet_file')
                continue

            m = p_old_status.match(line)
            if m:
                ret_dict['validation_status'] = m.group('validation_status').lower()
                continue

            m = p_old_time.match(line)
            if m:
                ret_dict['validation_time'] = m.group('validation_time')
                continue

            m = p_old_failed_cmd.match(line)
            if m:
                ret_dict['failed_command'] = m.group('failed_command')
                continue

            m = p_old_failed_reason.match(line)
            if m:
                failed_reason_check = True
                continue

            m = p_old_reason_detail.match(line)
            if m and failed_reason_check:
                ret_dict['failed_reason'] = m.group('failed_reason')
                failed_reason_check = False
                continue

            m = p_old_platform.match(line)
            if m:
                ret_dict['platform_status'] = m.group('platform_status')
                continue

            m = p_old_invalid_file.match(line)
            if m:
                ret_dict['invalid_file'] = m.group('invalid_file')
                continue

            # New format parsing
            m = p_new_configlet.match(line)
            if m:
                ret_dict['configlet_file_name'] = m.group('configlet_file')
                continue

            m = p_new_status.match(line)
            if m:
                ret_dict['validation_status'] = m.group('validation_status').lower()
                continue

            m = p_new_time.match(line)
            if m:
                ret_dict['validation_time'] = m.group('validation_time')
                continue

            if p_new_failed_cmd.match(line):
                state = 'failed_command'
                continue

            if p_new_failed_reason.match(line):
                state = 'failed_reason'
                continue

            # Collecting failed command or reason (new format)
            if state == 'failed_command' and line.startswith((' ', '\t')):
                failed_command_lines.append(line.strip())
                continue

            if state == 'failed_reason' and line.startswith((' ', '\t')):
                failed_reason_lines.append(line.strip())
                continue

        if failed_command_lines:
            ret_dict['failed_command'] = ' '.join(failed_command_lines)

        if failed_reason_lines:
            ret_dict['failed_reason'] = '\n'.join(failed_reason_lines)

        return ret_dict
    
class ACMLogSchema(MetaParser):
    """Schema for ACM log message"""
    schema = {
        'sno': {
            Any(): {
                'event': str,
                'result': str,
                Optional('username'): str,
                'timestamp': str,
                Optional('target_config'): str
            },
        },
    }


class AcmLog(ACMLogSchema):
    """Parser for 'acm log'"""

    cli_command = ['acm log']

    def cli(self, command='', output=None):
        if output is None:
            if command:
                out = self.device.execute(command)
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        if not out.strip() or 'Sno' not in out:
            return {}

        # Sno  Event  Result   Username   Time(M/D H:M:S)  Target-config
        p1 = re.compile(
            r'^(?P<sno>\d+)\s+'
            r'(?P<event>\S+)\s+'
            r'(?P<result>\S+)\s+'
            r'(?P<username>\S*)\s+'
            r'(?P<timestamp>\d{2}/\d{2}\s\d{2}:\d{2}:\d{2})\s*'
            r'(?P<target_config>\S*)$'
        )

        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()
            if not line or line.startswith("Sno") or line.startswith("~~~"):
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                sno = int(group['sno'])
                ret_dict.setdefault('sno', {})[sno] = {
                    'event': group['event'],
                    'result': group['result'],
                    'timestamp': group['timestamp']
                }
                if group['username']:
                    ret_dict['sno'][sno]['username'] = group['username']
                if group['target_config']:
                    ret_dict['sno'][sno]['target_config'] = group['target_config']

        return ret_dict
        
class ACMLogIndexNumberSchema(MetaParser):
    """Schema for ACM log {index number}"""
    schema = {
        'user_name': str,
        'event_name': str,
        'result': str,
        'event_time': str,
        'target_config': str,
        Optional('net_config_location'): str,
        Optional('net_config'): list,
        Optional('summary'): {
            'operation': str,
            'result': str
        },
    }


class ACMLogIndexNumber(ACMLogIndexNumberSchema):
    """Parser for ACM log {index number}"""

    cli_command = ['acm log {index_number}']

    def cli(self, index_number='', output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0].format(index_number=index_number))
        else:
            out = output

        ret_dict = {}
        net_config_lines = []
        summary = {}
        state = None

        # Define regex patterns
        p1 = re.compile(r'^User\s+Name\s*:\s*(?P<user_name>.*)$')
        p2 = re.compile(r'^Event\s*:\s*(?P<event>.+)$')
        p3 = re.compile(r'^Result\s*:\s*(?P<result>.+)$')
        p4 = re.compile(r'^Time\s+of\s+Event\s*:\s*(?P<event_time>.+)$')
        p5 = re.compile(r'^Target\s+config\s*:\s*(?P<target_config>.+)$')
        p6 = re.compile(r'^Net-Config\s+Location\s*:\s*(?P<flash>.+)$')
        p7 = re.compile(r'^Net-Config:$')
        p8 = re.compile(r'^![-]+$')
        p9 = re.compile(r'^!\s*(?P<key>[^:]+)\s*:\s*(?P<value>.+)$')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            if state == 'net_config':
                # Summary section not always exists, so we stop on empty line or known boundary
                if p8.match(line):
                    state = 'summary'
                    continue
                elif p9.match(line):
                    state = 'summary'
                    m = p9.match(line)
                    group = m.groupdict()
                    summary[group['key'].strip().lower()] = group['value'].strip()
                    continue
                else:
                    net_config_lines.append(line)
                    continue

            if state == 'summary':
                m = p9.match(line)
                if m:
                    group = m.groupdict()
                    summary[group['key'].strip().lower()] = group['value'].strip()
                continue

            # Header fields
            m = p1.match(line)
            if m:
                ret_dict['user_name'] = m.group('user_name')
                continue
            m = p2.match(line)
            if m:
                ret_dict['event_name'] = m.group('event')
                continue
            m = p3.match(line)
            if m:
                ret_dict['result'] = m.group('result')
                continue
            m = p4.match(line)
            if m:
                ret_dict['event_time'] = m.group('event_time')
                continue
            m = p5.match(line)
            if m:
                ret_dict['target_config'] = m.group('target_config')
                continue
            m = p6.match(line)
            if m:
                ret_dict['net_config_location'] = m.group('flash')
                continue
            if p7.match(line):
                state = 'net_config'
                continue

        # Final assignments
        if net_config_lines:
            ret_dict['net_config'] = net_config_lines
        if summary:
            ret_dict['summary'] = {}
            if 'operation' in summary:
                ret_dict['summary']['operation'] = summary['operation']
            if 'result' in summary:
                ret_dict['summary']['result'] = summary['result']

        return ret_dict

class ACMMergeSchema(MetaParser):
    schema = {
        Optional("validation_stage"): {
            "status": str,
            "time": str
        },
        Optional("apply_stage"): {
            "status": str,
            "time": str
        },
        Optional("config_merge_status"): str,
        Optional("configlet"): str,
        Optional("confirm_commit_timeout"): int,
        Optional("error"): str   # <-- allow error
    }

class AcmMerge(ACMMergeSchema):
    """Parser for 'acm merge <configlet>' or with optional timeout"""

    cli_command = ['acm merge {configlet}', 'acm merge {configlet} timeout {timeout}']

    def cli(self, configlet='', timeout='', output=None):
        if output is None:
            if timeout:
                cmd = self.cli_command[1].format(configlet=configlet, timeout=timeout)
            else:
                cmd = self.cli_command[0].format(configlet=configlet)
            output = self.device.execute(cmd)
        if not output.strip():
            return {}


        ret_dict = {}
        lines = output.splitlines()
        current_stage = None

        # Config Merge of Configlet: test_config.cfg
        p1 = re.compile(r'^Config Merge of Configlet:\s*(?P<configlet>\S+)')

        # Status : Success
        p2 = re.compile(r'^Status\s*:\s*(?P<status>\S+)')

        # Time : 1234 msec
        p3 = re.compile(r'^Time\s*:\s*(?P<time>\d+)\s*msec')

        # Config Merge Status: Success
        p4 = re.compile(r'^Config Merge Status:\s*(?P<status>\S+)')

        # Started confirm commit timer for 10 minutes
        p5 = re.compile(r'^Started confirm commit timer for\s+(?P<minutes>\d+)\s+minutes')

        # Error: File doesn't exist
        p6 = re.compile(r'^Error: File doesn\'t exist')        

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Ignore syslog/prompt
            if line.startswith("*") or line.startswith("%") or line.endswith("#"):
                continue

            # Handle file not found / error case
            m = p6.match(line)
            if m:
                ret_dict['configlet'] = configlet
                ret_dict['config_merge_status'] = "Failed"
                ret_dict['error'] = line   # optional: keep full error message
                return ret_dict  # exit early

            # Configlet URL
            m = p1.match(line)
            if m:
                ret_dict['configlet'] = m.group('configlet')
                continue

            # Validation or Apply stage headers
            if 'Validation Stage' in line:
                current_stage = 'validation_stage'
                ret_dict.setdefault(current_stage, {})
                continue
            elif 'Apply Stage' in line:
                current_stage = 'apply_stage'
                ret_dict.setdefault(current_stage, {})
                continue

            # Status within current stage
            m = p2.match(line)
            if m and current_stage:
                ret_dict[current_stage]['status'] = m.group('status')
                continue

            # Time within current stage
            m = p3.match(line)
            if m and current_stage:
                ret_dict[current_stage]['time'] = f"{m.group('time')} msec"
                continue

            # Merge Status
            m = p4.match(line)
            if m:
                ret_dict['config_merge_status'] = m.group('status')
                continue

            # Confirm Commit Timer
            m = p5.match(line)
            if m:
                ret_dict['confirm_commit_timeout'] = int(m.group('minutes'))
                continue

        # Ensure config_merge_status always set
        if 'config_merge_status' not in ret_dict:
            ret_dict['config_merge_status'] = "Failed"

        return ret_dict
            
class ACMRollbackSchema(MetaParser):
    schema = {
        Optional("target"): str,
        Optional("validation"): {
            "status": str,
            "time_ms": int
        },
        Optional("apply"): {
            "status": str,
            "time_ms": int
        },
        Optional("net_diff"): str,
        Optional("rollback_status"): str,
        Optional("no_diff"): bool,
        Optional("error"): str,     # <-- add this
        Optional("details"): str    # <-- add this
    }

class AcmRollback(ACMRollbackSchema):
    """Parser for 'acm rollback <id>'"""

    cli_command = ['acm rollback {rollback_id}']

    def cli(self, rollback_id='', output=None):
        if output is None:
            cmd = self.cli_command[0].format(rollback_id=rollback_id)
            try:
                output = self.device.execute(cmd)
            except Exception as e:
                # Handle Unicon SubCommandFailure or InvalidCommandError
                error_msg = str(e)
                return {
                    "target": rollback_id,
                    "rollback_status": "Failed",
                    "error": "Invalid input or unsupported rollback ID",
                    "details": error_msg
                }

        if not output.strip():
            return {}

        ret_dict = {}
        current_stage = None
        lines = output.splitlines()

        # Config Rollback to Target : rollback_config.txt
        p1 = re.compile(r'^Config Rollback to Target\s*:\s*(?P<target>\S+)')

        # Status : Success
        p2 = re.compile(r'^Status\s*:\s*(?P<status>\S+)')

        # Time : 1423 msec
        p3 = re.compile(r'^Time\s*:\s*(?P<time>\d+)\s*msec')

        # Config Net-Diff: net_diff_output.txt
        p4 = re.compile(r'^Config Net-Diff:\s*(?P<net_diff>\S+)')

        # Config Rollback Status: Failed
        p5 = re.compile(r'^Config Rollback Status:\s*(?P<status>\S+)')        
        
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Ignore syslog/prompt
            if line.startswith("*") or line.startswith("%") or line.endswith("#"):
                if "Invalid input" in line:
                    ret_dict["target"] = rollback_id
                    ret_dict["rollback_status"] = "Failed"
                    ret_dict["error"] = line
                continue

            # Target line
            m = p1.match(line)
            if m:
                ret_dict['target'] = m.group('target')
                continue

            # No diff case
            if 'Config diff empty. No Diff to Validate/Apply' in line:
                ret_dict['no_diff'] = True
                continue

            # Identify stages
            if 'Validation Stage' in line:
                current_stage = 'validation'
                ret_dict.setdefault(current_stage, {})
                continue
            if 'Apply Stage' in line:
                current_stage = 'apply'
                ret_dict.setdefault(current_stage, {})
                continue

            # Status
            m = p2.match(line)
            if m and current_stage:
                ret_dict[current_stage]['status'] = m.group('status')
                continue

            # Time
            m = p3.match(line)
            if m and current_stage:
                ret_dict[current_stage]['time_ms'] = int(m.group('time'))
                continue

            # Config Net-Diff
            m = p4.match(line)
            if m:
                ret_dict['net_diff'] = m.group('net_diff')
                continue

            # Rollback Status
            m = p5.match(line)
            if m:
                ret_dict['rollback_status'] = m.group('status')

        # If rollback_status not found, default to Failed
        if 'rollback_status' not in ret_dict:
            ret_dict['rollback_status'] = "Failed"

        return ret_dict
            
class ACMReplaceSchema(MetaParser):
    schema = {
        Optional("target"): str,
        Optional("validation_stage"): {
            "status": str,
            "time_ms": int,
            Optional("failed_command"): str,
            Optional("failed_reason"): str,
        },
        Optional("apply_stage"): {
            "status": str,
            "time_ms": int
        },
        Optional("net_diff"): str,
        "replace_status": str,
        Optional("timeout_min"): int,
        Optional("error"): str   # <-- Add this for error cases
    }

class AcmReplace(ACMReplaceSchema):
    """Parser for 'acm replace <source>'"""
    
    cli_command = [
        'acm replace {source} timeout {timeout}',
        'acm replace {source}'
    ]

    def cli(self, source='', timeout=None, output=None):
        if output is None:
            if timeout:
                cmd = self.cli_command[0].format(source=source, timeout=timeout)
            else:
                cmd = self.cli_command[1].format(source=source)
            output = self.device.execute(cmd)
        if not output.strip():
            return {}

        ret_dict = {}
        lines = output.splitlines()
        current_stage = None

        # Config Replace to Target: target_config.cfg
        p1 = re.compile(r'^Config Replace to Target:\s*(?P<target>\S+)')

        # Status : Success
        p2 = re.compile(r'^Status\s*:\s*(?P<status>\S+)')

        # Time : 1234 msec
        p3 = re.compile(r'^Time\s*:\s*(?P<time>\d+)\s*msec')

        # no interface GigabitEthernet0/0/0
        p4 = re.compile(r'^no\s+.*')

        # Config Net-Diff: some_diff_id
        p5 = re.compile(r'^Config Net-Diff:\s*(?P<net_diff>\S+)')

        # Config Replace Status: Success
        p6 = re.compile(r'^Config Replace Status:\s*(?P<status>\S+)')

        # Started confirm commit timer for 10 minutes
        p7 = re.compile(r'^Started confirm commit timer for\s+(?P<timeout>\d+)\s+minutes')
       
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Ignore syslog/prompt noise
            if line.startswith("*") or line.startswith("%") or line.endswith("#"):
                continue

            # Target
            m = p1.match(line)
            if m:
                ret_dict['target'] = m.group('target')
                continue

            # Handle file not found / error case
            if line.startswith("Error: File doesn't exist"):
                ret_dict['replace_status'] = "Failed"
                ret_dict['error'] = line   # optional, keep error message
                return ret_dict  # exit early since nothing else will be parsed

            # Validation Stage
            if 'Validation Stage' in line:
                current_stage = 'validation_stage'
                ret_dict.setdefault(current_stage, {})
                continue

            # Apply Stage
            if 'Apply Stage' in line:
                current_stage = 'apply_stage'
                ret_dict.setdefault(current_stage, {})
                continue

            # Status
            m = p2.match(line)
            if m and current_stage:
                ret_dict[current_stage]['status'] = m.group('status')
                continue

            # Time
            m = p3.match(line)
            if m and current_stage:
                ret_dict[current_stage]['time_ms'] = int(m.group('time'))
                continue

            # Failed Command
            if 'Failed Command:' in line:
                current_stage = 'validation_stage'
                continue
            m = p4.match(line)
            if m and current_stage == 'validation_stage':
                ret_dict[current_stage]['failed_command'] = m.group(0)
                continue

            # Failed Reason
            if 'Failed Reason:' in line:
                continue
            if current_stage == 'validation_stage' and ('%' in line or 'Remove' in line):
                prev_reason = ret_dict[current_stage].get('failed_reason', '')
                ret_dict[current_stage]['failed_reason'] = (
                    (prev_reason + '\n' + line).strip() if prev_reason else line
                )
                continue

            # Config Net-Diff
            m = p5.match(line)
            if m:
                ret_dict['net_diff'] = m.group('net_diff')
                continue

            # Replace Status
            m = p6.match(line)
            if m:
                ret_dict['replace_status'] = m.group('status')
                continue

            # Timeout
            m = p7.match(line)
            if m:
                ret_dict['timeout_min'] = int(m.group('timeout'))

        # Ensure replace_status is always set (default to Failed if missing)
        if 'replace_status' not in ret_dict:
            ret_dict['replace_status'] = "Failed"

        return ret_dict
                
class ShowAcmRulesSchema(MetaParser):
    """Schema for show acm rules"""
    schema = {
        "rules": {
            int: {
                "match_mode": str,
                "command": str,
                "action": str
            }
        }
    }

class ShowAcmRules(ShowAcmRulesSchema):
    """Parser for show acm rules"""

    cli_command = 'show acm rules'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        rules_dict = {}
        rule_index = 1
        
        # match mode mdt-subscription-mode command no update-policy
        # match mode mdt-subscription-mode command no stream
        p1 = re.compile(r'^match mode (?P<match_mode>\S+) command (?P<command>.*)$')

        # action skip
        p2 = re.compile(r'^action (?P<action>\S+)$')

        current_rule = {}

        for line in output.splitlines():
            line = line.strip()
            
            # match mode mdt-subscription-mode command no update-policy
            # match mode mdt-subscription-mode command no stream
            m = p1.match(line)
            if m:
                group = m.groupdict()  # Use named groups for clarity
                current_rule = {
                    "match_mode": group["match_mode"],
                    "command": group["command"]
                }
                continue
            
            # action skip
            m = p2.match(line)
            if m and current_rule:
                current_rule["action"] = m.group("action")
                rules_dict[rule_index] = current_rule
                rule_index += 1
                current_rule = {}

        if rules_dict:
            ret_dict["rules"] = rules_dict

        return ret_dict

class AcmReplaceValidateSchema(MetaParser):
    """Schema for 'acm replace <configlet_file> validate'."""

    schema = {
        "target": str,
        "validation": {
            "status": str,
            "time_ms": int
        }
    }


class AcmReplaceValidate(AcmReplaceValidateSchema):
    """Parser for 'acm replace <configlet_file> validate'."""

    cli_command = 'acm replace {configlet_file} validate'

    def cli(self, configlet_file='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(configlet_file=configlet_file))

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Config Validation to Target: flash:day1
            m = re.match(r'^Config Validation to Target:\s+(?P<target>\S+)', line)
            if m:
                ret_dict['target'] = m.group('target')
                continue

            # Status : Success
            m = re.match(r'^Status\s*:\s*(?P<status>\S+)', line)
            if m:
                ret_dict.setdefault('validation', {})['status'] = m.group('status')
                continue

            # Time   : 483 msec
            m = re.match(r'^Time\s*:\s*(?P<time>\d+)\s*msec', line)
            if m:
                ret_dict.setdefault('validation', {})['time_ms'] = int(m.group('time'))
                continue

        return ret_dict