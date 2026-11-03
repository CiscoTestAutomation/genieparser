"""show_nxsecure.py

NXOS parsers for the following show commands:
    * show nxsecure status
    * show nxsecure policy status
    * show nxsecure log {policy_id}
    * show nxsecure packages
    * show nxsecure logfiles
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf


# ====================================================================
# Schema for 'show nxsecure status'
# ====================================================================
class ShowNxsecureStatusSchema(MetaParser):
    """Schema for show nxsecure status"""

    schema = {
        'tetragon_agent_status': str,
    }


# ====================================================================
# Parser for 'show nxsecure status'
# ====================================================================
class ShowNxsecureStatus(ShowNxsecureStatusSchema):
    """Parser for show nxsecure status"""

    cli_command = 'show nxsecure status'

    def cli(self, command='', output=None):
        if output is None:
            output = self.device.execute(command or self.cli_command)

        ret_dict = {}

        # Tetragon Agent Status: Running
        p1 = re.compile(r'^Tetragon +Agent +Status: +(?P<tetragon_agent_status>\S+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Tetragon Agent Status: Running
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({
                    'tetragon_agent_status': groups['tetragon_agent_status'],
                })
                continue

        return ret_dict


# ====================================================================
# Schema for 'show nxsecure packages'
# ====================================================================
class ShowNxsecurePackagesSchema(MetaParser):
    """Schema for show nxsecure packages"""

    schema = {
        'packages': ListOf(str),
    }


# ====================================================================
# Parser for 'show nxsecure packages'
# ====================================================================
class ShowNxsecurePackages(ShowNxsecurePackagesSchema):
    """Parser for show nxsecure packages"""

    cli_command = 'show nxsecure packages'

    def cli(self, command='', output=None):
        if output is None:
            output = self.device.execute(command or self.cli_command)

        ret_dict = {}

        # Package List:
        p1 = re.compile(r'^Package +List:$')

        # lp00037.lps-mplsoam-fec-v1.lps
        p2 = re.compile(r'^(?P<package>\S+\.(?:lps|rpm|shd|pkg|bin)(?:\.\S+)?)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Package List:
            m = p1.match(line)
            if m:
                continue

            # lp00037.lps-mplsoam-fec-v1.lps
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.setdefault('packages', []).append(groups['package'])
                continue

        return ret_dict


# ====================================================================
# Schema for 'show nxsecure logfiles'
# ====================================================================
class ShowNxsecureLogfilesSchema(MetaParser):
    """Schema for show nxsecure logfiles"""

    schema = {
        'logfiles': ListOf(str),
    }


# ====================================================================
# Parser for 'show nxsecure logfiles'
# ====================================================================
class ShowNxsecureLogfiles(ShowNxsecureLogfilesSchema):
    """Parser for show nxsecure logfiles"""

    cli_command = 'show nxsecure logfiles'

    def cli(self, command='', output=None):
        if output is None:
            output = self.device.execute(command or self.cli_command)

        ret_dict = {}

        # tetragon.log
        p1 = re.compile(r'^(?P<logfile>\S+\.(?:log|tar\.gz))$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # tetragon.log
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.setdefault('logfiles', []).append(groups['logfile'])
                continue

        return ret_dict


# ====================================================================
# Schema for 'show nxsecure log {policy_id}'
# ====================================================================
class ShowNxsecureLogSchema(MetaParser):
    """Schema for show nxsecure log {policy_id}"""

    schema = {
        'policy_id': str,
        'policy_name': str,
        'policy_severity': str,
        'policy_event': str,
        'event_history': {
            Any(): {
                'time': str,
                'mode': str,
                'process': str,
            }
        }
    }


# ====================================================================
# Parser for 'show nxsecure log {policy_id}'
# ====================================================================
class ShowNxsecureLog(ShowNxsecureLogSchema):
    """Parser for show nxsecure log {policy_id}"""

    cli_command = 'show nxsecure log {policy_id}'

    def cli(self, command='', output=None, **kwargs):
        if output is None:
            output = self.device.execute(command)

        ret_dict = {}

        # Policy Id       : lp00003
        p1 = re.compile(r'^Policy +Id +: +(?P<policy_id>\S+)$')

        # Policy Name     : infra-2-ptrace
        p2 = re.compile(r'^Policy +Name +: +(?P<policy_name>[^\r\n]+)$')

        # Policy Severity : INFO
        p3 = re.compile(r'^Policy +Severity +: +(?P<policy_severity>\S+)$')

        # Policy Event    : Process attempted to perform ptrace operations
        # without sufficient privileges
        p4 = re.compile(r'^Policy +Event +: +(?P<policy_event>[^\r\n]+)$')

        # Policy Event History(last 20 events):
        p5 = re.compile(r'^Policy +Event +History\(last +20 +events\):$')

        # SNo         Time                               Mode          Process
        p6 = re.compile(r'^SNo +Time +Mode +Process$')

        # 1 07:40:51.318 UTC Thu Sep 17 2026 monitor /usr/bin/strace
        p7 = re.compile(r'^(?P<sno>\d+) +(?P<time>\d{2}:\d{2}:\d{2}\.\d{3} +\S+ +\S+ +\S+ +\d{1,2} +\d{4}) +(?P<mode>\S+) +(?P<process>[^\r\n]+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Policy Id       : lp00003
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({'policy_id': groups['policy_id']})
                continue

            # Policy Name     : infra-2-ptrace
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({'policy_name': groups['policy_name']})
                continue

            # Policy Severity : INFO
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({
                    'policy_severity': groups['policy_severity'],
                })
                continue

            # Policy Event    : Process attempted to perform ptrace operations
            # without sufficient privileges
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({'policy_event': groups['policy_event']})
                continue

            # Policy Event History(last 20 events):
            m = p5.match(line)
            if m:
                continue

            # SNo         Time                               Mode          Process
            m = p6.match(line)
            if m:
                continue

            # 1 07:40:51.318 UTC Thu Sep 17 2026 monitor /usr/bin/strace
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                event_dict = ret_dict.setdefault('event_history', {}).setdefault(
                    int(groups['sno']), {}
                )
                event_dict.update({
                    'time': groups['time'],
                    'mode': groups['mode'],
                    'process': groups['process'],
                })
                continue

        return ret_dict


# ====================================================================
# Schema for 'show nxsecure policy status'
# ====================================================================
class ShowNxsecurePolicyStatusSchema(MetaParser):
    """Schema for show nxsecure policy status"""

    schema = {
        'policies': {
            Any(): {
                'name': str,
                'package': str,
                'original': str,
                'override': str,
                'current': str,
                'hits': int,
            }
        }
    }


# ====================================================================
# Parser for 'show nxsecure policy status'
# ====================================================================
class ShowNxsecurePolicyStatus(ShowNxsecurePolicyStatusSchema):
    """Parser for show nxsecure policy status"""

    cli_command = 'show nxsecure policy status'

    def cli(self, command='', output=None):
        if output is None:
            output = self.device.execute(command or self.cli_command)

        ret_dict = {}

        # Id Name Package Original Override Current Hits
        p1 = re.compile(r'^Id +Name +Package +Original +Override +Current +Hits$')

        # lp10008 lps-heap-out-v1 lp10008.lps-heap-out-v1.lps enforce none enforce 0
        p2 = re.compile(r'^(?P<policy_id>\S+) +(?P<name>\S+) +(?P<package>\S+) +(?P<original>\S+) +(?P<override>\S+) +(?P<current>\S+) +(?P<hits>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Id Name Package Original Override Current Hits
            m = p1.match(line)
            if m:
                continue

            # lp10008 lps-heap-out-v1 lp10008.lps-heap-out-v1.lps enforce none enforce 0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                policy_dict = ret_dict.setdefault('policies', {}).setdefault(
                    groups['policy_id'], {}
                )
                policy_dict.update({
                    'name': groups['name'],
                    'package': groups['package'],
                    'original': groups['original'],
                    'override': groups['override'],
                    'current': groups['current'],
                    'hits': int(groups['hits']),
                })
                continue

        return ret_dict
