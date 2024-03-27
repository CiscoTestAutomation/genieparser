''' show_terminal.py
IOSXR parsers for the following show commands:
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
        "baud_rate": {
            "tx": int,
            "rx": int
        },
        "template": str,
        "capabilities": str,
        "parity": str,
        "stopbits": int,
        "databits": int,
        "allowed_transport": ListOf(str)
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
        p0 = re.compile(r'^Line "(?P<line>.*?)", Location "(?P<location>.*?)", Type "(?P<type>.*?)"$')

        # Length: 0 lines, Width: 0 columns
        p1 = re.compile(r'^Length: (?P<length>\d+) lines, Width: (?P<width>\d+) columns$')

        # Baud rate (TX/RX) is 9600/9600, no parity, 1 stopbits, 8 databits
        p2 = re.compile(r'^Baud rate \(TX\/RX\) is (?P<baud_rate>\d+), '
                        r'"(?P<parity>\w+)" Parity, (?P<stopbits>\d) stopbits, (?P<databits>\w+) databits$')

        # Template: console
        p3 = re.compile(r'^Template: (?P<template>\w+)$')

        # Capabilities: Timestamp Enabled
        p4 = re.compile(r'Capabilities: (?P<capabilities>[\w\s]+)')

        # Allowed transports are none.
        p5 = re.compile(r'^Allowed transports are (?P<allowed_transport>[\w\s]+)\.?\s*$')

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
                baud_rate.update({"tx": int(m.groupdict()['baud_rate'])})
                baud_rate.update({"rx": int(m.groupdict()['baud_rate'])})
                ret_dict.setdefault("parity", m.groupdict()['parity'])
                ret_dict.setdefault("stopbits", int(m.groupdict()['stopbits']))
                ret_dict.setdefault("databits", int(m.groupdict()['databits']))

            # Template: console
            m = p3.match(line)
            if m:
                ret_dict.setdefault("template", m.groupdict()['template'])

            # Capabilities: Timestamp Enabled
            m = p4.match(line)
            if m:
                ret_dict.setdefault("capabilities", m.groupdict()['capabilities'])

            # Allowed transports are none.
            m = p5.match(line)
            if m:
                allowed_transport = m.groupdict()['allowed_transport']
                if allowed_transport:
                    ret_dict.setdefault("allowed_transport", allowed_transport.split())

        return ret_dict