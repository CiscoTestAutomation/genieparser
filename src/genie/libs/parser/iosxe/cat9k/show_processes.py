''' show_processes.py

IOSXE parser for the following show command:
    * show processes platform | count {process}
    * show processes platform | include {process}
'''

import re
# Metaparser
from genie.metaparser import MetaParser


# ====================
# Schema for:
#  * 'show processes platform | count <process>'
# ====================
class ShowProcessesPlatformCProcessSchema(MetaParser):
    """Schema for show processes platform | count <process>"""

    schema = {
        "number_of_matching_lines": int
    }


# ====================
# Parser for:
#  * 'show processes platform | count <process>'
# ====================
class ShowProcessesPlatformCProcess(ShowProcessesPlatformCProcessSchema):
    """Schema for show processes platform | count <process>"""

    # Number of lines which match regexp = 1

    cli_command = "show processes platform | count {process}"

    def cli(self, process="", output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(process=process))

        # initial return dictionary
        ret_dict = {}

        # Number of lines which match regexp = 1

        p1 = re.compile(r"^Number\s+of\s+lines\s+which\s+match\s+regexp\s=\s+(?P<number_of_matching_lines>\d+)")

        for line in output.splitlines():
            line = line.strip()

            # Number of lines which match regexp = 1
            m1 = p1.match(line)
            if m1:
                number_of_matching_lines = p1.match(line)
                groups = number_of_matching_lines.groupdict()
                number_of_matching_lines = int(groups['number_of_matching_lines'])
                ret_dict['number_of_matching_lines'] = number_of_matching_lines

        return ret_dict


# ====================
# Schema for:
#  * 'show processes platform | include <process>'
# ====================
class ShowProcessesPlatformIProcessSchema(MetaParser):
    """Schema for show processes platform | include <process>"""

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
    """Schema for show processes platform | include <process>"""

    # Pid	PPid  Status		Size  Name
    # 1229	 848  S		   347160  wncd_0

    cli_command = "show processes platform | include {process}"

    def cli(self, process="wncd", output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(process=process))

        # initial return dictionary
        processes_platform_ret_dict = {}

        # Pid	PPid  Status		Size  Name
        p1 = re.compile(r"^(?P<pid>\S+)\s+(?P<ppid>\S+)\s+(?P<status>\S+)\s+(?P<size>\S+)\s+(?P<name>\S+)")

        for line in output.splitlines():
            line = line.strip()

            # 1229	 848  S		   347160  wncd_0
            m1 = p1.match(line)
            if m1:
                groups = m1.groupdict()
                processes_platform_dict = processes_platform_ret_dict.setdefault('pid', {}).setdefault(groups['pid'],{})
                processes_platform_dict.update({
                    'ppid': groups['ppid'],
                    'status': groups['status'],
                    'size': groups['size'],
                    'name': groups['name']
                })
        return processes_platform_ret_dict
