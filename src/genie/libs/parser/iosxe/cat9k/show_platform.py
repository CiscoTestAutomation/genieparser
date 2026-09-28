'''show_platform.py

IOSXE Cat9k parsers for the following show commands:
    * show platform software process slot sw {chassis} r0 monitor |
      count {process}
    * show platform software process slot sw {chassis} r0 monitor |
      include {process}
    * show platform software process database resource-manager switch
      {switch_id} r0 summary
'''

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
import re


# ====================
# Schema for:
#  * 'show platform software process slot sw standby r0 monitor | count <process>'
# ====================


class ShowPlatformSoftCProcessSchema(MetaParser):
    """Schema for show platform software process slot sw standby r0 monitor | count <process>"""

    schema = {
        "number_of_matching_lines": int
    }


# ====================
# Parser for:
#  * 'show platform software process slot sw standby r0 monitor | count <process>'
# ====================


class ShowPlatformSoftCProcess(ShowPlatformSoftCProcessSchema):
    """Schema for show platform software process slot sw standby r0 monitor| count <process>"""

    # Number of lines which match regexp = 1

    cli_command = "show platform software process slot sw {chassis} r0 monitor | count {process}"

    def cli(self, process="", chassis="active", output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(process=process, chassis=chassis))

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
#  * 'show platform software process slot sw standby r0 monitor | include <process>'
# ====================


class ShowPlatformSoftIProcessSchema(MetaParser):
    """Schema for show platform software process slot sw standby r0 monitor | include <process>"""

    schema = {
        "pid": {
            str: {
                "user": str,
                "pr": str,
                "ni": str,
                "virt": str,
                "res": str,
                "shr": str,
                "s": str,
                "cpu": str,
                "mem": str,
                "time": str,
                "cmd": str
            }
        }
    }


# ====================


# Parser for:
#  * 'show platform software process slot sw standby r0 monitor | include <process>'
# ====================


class ShowPlatformSoftIProcess(ShowPlatformSoftIProcessSchema):
    """Schema for show platform software process slot sw standby r0 monitor| include <process>"""

    # PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    # 26855 root      20   0 1842228 240864 206380 S   0.0   3.1   0:20.22 wncd_0

    cli_command = "show platform software process slot sw {chassis} r0 monitor | include {process}"

    def cli(self, process="wncd", chassis="active", output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(process=process, chassis=chassis))

        # initial return dictionary
        platform_software_dict = {}
        platform_software_ret_dict = {}

        # PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
        p1 = re.compile(
            r'^(?P<pid>\S+)\s+(?P<user>\S+)\s+(?P<pr>\S+)\s+(?P<ni>\S+)\s+(?P<virt>\S+)\s+(?P<res>\S+)\s+(?P<shr>\S+)\s+(?P<s>\S+)\s+(?P<cpu>\S+)\s+(?P<mem>\S+)\s+(?P<time>\S+)\s+(?P<cmd>\S+)')

        for line in output.splitlines():
            line = line.strip()

            # 26855 root      20   0 1842228 240864 206380 S   0.0   3.1   0:20.22 wncd_0
            m1 = p1.match(line)
            if m1:
                groups = m1.groupdict()
                platform_software_dict = platform_software_ret_dict.setdefault('pid', {}).setdefault(groups['pid'], {})
                platform_software_dict.update({
                    'user': groups['user'],
                    'pr': groups['pr'],
                    'ni': groups['ni'],
                    'virt': groups['virt'],
                    'res': groups['res'],
                    'shr': groups['shr'],
                    's': groups['s'],
                    'cpu': groups['cpu'],
                    'mem': groups['mem'],
                    'time': groups['time'],
                    'cmd': groups['cmd']
                })
        return platform_software_ret_dict


# ====================
# Schema for:
#  * 'show platform software process database resource-manager switch
#    {switch_id} r0 summary'
# ====================


class ShowPlatformSoftwareProcessDatabaseResourceManagerSwitchR0SummarySchema(
        MetaParser):
    """Schema for show platform software process database resource-manager
    switch {switch_id} r0 summary.
    """

    schema = {
        "database": str,
        "tables": {
            Any(): {
                "table_oid_id": str,
                "records": int,
                "current_state": str,
                "table_types": {
                    Any(): {
                        "table_oid_source": str,
                        "mode": str,
                    }
                },
            }
        },
    }


# ====================
# Parser for:
#  * 'show platform software process database resource-manager switch
#    {switch_id} r0 summary'
# ====================


class ShowPlatformSoftwareProcessDatabaseResourceManagerSwitchR0Summary(
        ShowPlatformSoftwareProcessDatabaseResourceManagerSwitchR0SummarySchema
):
    """Parser for show platform software process database resource-manager
    switch {switch_id} r0 summary.
    """

    cli_command = (
        "show platform software process database resource-manager "
        "switch {switch_id} r0 summary"
    )

    def cli(self, switch_id, output=None):
        if output is None:
            command = self.cli_command.format(switch_id=switch_id)
            output = self.device.execute(command)

        ret_dict = {}
        current_table = None

        # Database: LEABA_RM_DB
        p1 = re.compile(r"^Database:\s+(?P<database>\S+)$")

        # table rms_RM_RSC_L2_AC_PORT_ta
        #   0x096884c32c1dcefbdf7c8a7d383f8658  575  en
        p2 = re.compile(
            r"^table\s+(?P<table_name>\S+)\s+"
            r"(?P<table_oid_id>0x[0-9a-fA-F]+)\s+"
            r"(?P<records>\d+)\s+(?P<current_state>\S+)$"
        )

        # rms_RM_RSC_L2_AC_PORT_table
        #   0x00000000000000000000000000000000  expl
        p3 = re.compile(
            r"^(?P<table_type>\S+)\s+"
            r"(?P<table_oid_source>0x[0-9a-fA-F]+)\s+"
            r"(?P<mode>\S+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Database: LEABA_RM_DB
            match = p1.match(line)
            if match:
                ret_dict["database"] = match.group("database")
                continue

            # table rms_RM_RSC_L2_AC_PORT_ta
            #   0x096884c32c1dcefbdf7c8a7d383f8658  575  en
            match = p2.match(line)
            if match:
                groups = match.groupdict()
                current_table = ret_dict.setdefault("tables", {}).setdefault(
                    groups["table_name"], {}
                )
                current_table.update({
                    "table_oid_id": groups["table_oid_id"].lower(),
                    "records": int(groups["records"]),
                    "current_state": groups["current_state"],
                })
                continue

            # rms_RM_RSC_L2_AC_PORT_table
            #   0x00000000000000000000000000000000  expl
            match = p3.match(line)
            if match and current_table is not None:
                groups = match.groupdict()
                table_types = current_table.setdefault("table_types", {})
                table_type = table_types.setdefault(groups["table_type"], {})
                table_type.update({
                    "table_oid_source": groups["table_oid_source"].lower(),
                    "mode": groups["mode"],
                })
                continue

        return ret_dict
