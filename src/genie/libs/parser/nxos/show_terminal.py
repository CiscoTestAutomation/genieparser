''' show_terminal.py
NXOS parsers for the following show commands:
    * show terminal
'''

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Optional, ListOf

# =============================================
# Schema for 'show terminal'
# =============================================

class ShowTerminalSchema(MetaParser):

    """
    Schema for show terminal
    """

    schema = {
        "tty": str,
        "type": str,
        "length": int,
        "width": int,
        "session_timeout": str,
        "event_manager": str,
        "redirection_mode": str,
        "accounting_log_all": str,
        "vlan_mutex": int,
        "vlan_batch": str
    }

# =============================================
# Parser for 'show terminal'
# =============================================

class ShowTerminal(ShowTerminalSchema):

    """
    Parser for show terminal
    """

    cli_command = 'show terminal'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # TTY: /dev/ttyS0 Type: "vt102"
        p0 = re.compile(r'^TTY: (?P<tty>[\/\w]+) Type: "(?P<type>\w+)"$')

        # Length: 0 lines, Width: 0 columns
        p1 = re.compile(r'^Length: (?P<length>\d+) lines, Width: (?P<width>\d+) columns$')

        # Session Timeout: 0 minutes
        p2 = re.compile(r'^Session Timeout: (?P<session_timeout>[\w\s]+)$')

        # Event Manager CLI event bypass: no
        p3 = re.compile(r'^Event Manager CLI event bypass: (?P<event_manager>\w+)$')

        # Redirection mode: ascii
        p4 = re.compile(r'^Redirection mode: (?P<redirection_mode>\w+)$')

        # Accounting log all commands (including show commands): no
        p5 = re.compile(r'^Accounting log all commands \(including show commands\): '
                        r'(?P<accounting_log_all>\w+)$')

        # Vlan mutex value: 1
        p6 = re.compile(r'^Vlan mutex value: (?P<vlan_mutex>\d+)$')

        # Vlan batch mode: yes
        p7 = re.compile(r'^Vlan batch mode: (?P<vlan_batch>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # Line 0, Location: "", Type: ""
            m = p0.match(line)
            if m:
                ret_dict.setdefault("tty", m.groupdict()["tty"])
                ret_dict.setdefault("type", m.groupdict()["type"])

            # Length: 0 lines, Width: 0 columns
            m = p1.match(line)
            if m:
                ret_dict.setdefault("length", int(m.groupdict()['length']))
                ret_dict.setdefault("width", int(m.groupdict()['width']))

            # Session Timeout: 0 minutes
            m = p2.match(line)
            if m:
                ret_dict.setdefault("session_timeout", m.groupdict()["session_timeout"])

            # Event Manager CLI event bypass: no
            m = p3.match(line)
            if m:
                ret_dict.setdefault("event_manager", m.groupdict()["event_manager"])

            # Redirection mode: ascii
            m = p4.match(line)
            if m:
                ret_dict.setdefault("redirection_mode", m.groupdict()['redirection_mode'])

            # Accounting log all commands (including show commands): no
            m = p5.match(line)
            if m:
                ret_dict.setdefault("accounting_log_all", m.groupdict()['accounting_log_all'])

            # Vlan mutex value: 1
            m = p6.match(line)
            if m:
                ret_dict.setdefault("vlan_mutex", int(m.groupdict()['vlan_mutex']))

            # Vlan batch mode: yes
            m = p7.match(line)
            if m:
                ret_dict.setdefault("vlan_batch", m.groupdict()['vlan_batch'])

        return ret_dict