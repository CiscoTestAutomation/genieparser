''' show_terminal.py
IOSXE parsers for the following show commands:
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
        "line": str,
        "location": str,
        "type": str,
        "length": int,
        "width": int,
        "baud_rate":{
            "tx": int,
            "rx": int
        },
        "parity": str,
        "stopbits": int,
        "databits": int,
        "status": ListOf(str),
        "input_transport": ListOf(str),
        "output_transport": ListOf(str)
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

        # Line 0, Location: "", Type: ""
        p0 = re.compile(r'^Line (?P<line>\w+), Location: "(?P<location>.*?)", Type: "(?P<type>.*?)"$')

        # Length: 0 lines, Width: 0 columns
        p1 = re.compile(r'^Length: (?P<length>\d+) lines, Width: (?P<width>\d+) columns$')

        # Baud rate (TX/RX) is 9600/9600, no parity, 1 stopbits, 8 databits
        p2 = re.compile(r'^Baud rate \(TX\/RX\) is (?P<tx>\d+)\/(?P<rx>\d+), '
                        r'(?P<parity>\w+) parity, (?P<stopbits>\d) stopbits, (?P<databits>\w+) databits$')

        # Status: PSI Enabled, Ready, Active, Automore On
        p3 = re.compile(r'^Status: (?P<status>.*?)$')

        # Allowed input transports are none
        p4 = re.compile(r'^Allowed input transports are (?P<input_transport>[\w\s]+)\.?\s*$')

        # Allowed output transports are pad telnet rlogin ssh.
        p5 = re.compile(r'^Allowed output transports are (?P<output_transport>[\w\s]+)\.?\s*$')

        for line in output.splitlines():
            line = line.strip()

            # Line 0, Location: "", Type: ""
            m = p0.match(line)
            if m:
                ret_dict.setdefault("line", m.groupdict()["line"])
                ret_dict.setdefault("location", m.groupdict()["location"])
                ret_dict.setdefault("type", m.groupdict()["type"])

            # Length: 0 lines, Width: 0 columns
            m = p1.match(line)
            if m:
                ret_dict.setdefault("length", int(m.groupdict()['length']))
                ret_dict.setdefault("width", int(m.groupdict()['width']))

            # Baud rate (TX/RX) is 9600/9600, no parity, 1 stopbits, 8 databits
            m = p2.match(line)
            if m:
                baud_rate = ret_dict.setdefault("baud_rate", {})
                baud_rate.update({"tx": int(m.groupdict()['tx'])})
                baud_rate.update({"rx": int(m.groupdict()['rx'])})
                ret_dict.setdefault("parity", m.groupdict()['parity'])
                ret_dict.setdefault("stopbits", int(m.groupdict()['stopbits']))
                ret_dict.setdefault("databits", int(m.groupdict()['databits']))

            # Status: PSI Enabled, Ready, Active, Automore On
            m = p3.match(line)
            if m:
                status = m.groupdict()['status']
                if status:
                    ret_dict.setdefault("status", status.split(", "))

            # Allowed input transports are none
            m = p4.match(line)
            if m:
                input_transport = m.groupdict()['input_transport']
                if input_transport:
                    ret_dict.setdefault("input_transport", input_transport.split())

            # Allowed output transports are pad telnet rlogin ssh.
            m = p5.match(line)
            if m:
                output_transport = m.groupdict()['output_transport']
                if output_transport:
                    ret_dict.setdefault("output_transport", output_transport.split())

        return ret_dict