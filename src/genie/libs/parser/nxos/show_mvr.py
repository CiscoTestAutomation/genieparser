"""show_mvr.py

NXOS parsers for the following show commands:
    * show mvr interface
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf

# Parser utils
from genie.libs.parser.utils.common import Common


# ==================================================
# Schema for 'show mvr interface'
# ==================================================
class ShowMvrInterfaceSchema(MetaParser):
    """Schema for show mvr interface"""

    schema = {
        'interfaces': {
            Any(): {
                'vlan': int,
                'type': str,
                'status': str,
                'mvr_vlans': ListOf(str),
            },
        },
    }


# ==================================================
# Parser for 'show mvr interface'
# ==================================================
class ShowMvrInterface(ShowMvrInterfaceSchema):
    """Parser for show mvr interface"""

    cli_command = 'show mvr interface'

    def cli(self, command='', output=None, **kwargs):
        if output is None:
            command = command or self.cli_command
            output = self.device.execute(command)

        ret_dict = {}

        # Port         VLAN Type      Status    MVR-VLAN
        p1 = re.compile(r'^Port +VLAN +Type +Status +MVR-VLAN$')

        # Po10         100  SOURCE    ACTIVE    100-101
        p2 = re.compile(r'^(?P<interface>\S+) +(?P<vlan>\d+) +'
                        r'(?P<type>\S+) +(?P<status>\S+) +'
                        r'(?P<mvr_vlans>\S+)$')

        # Status INVALID indicates one of the following misconfiguration:
        # a) Interface is not a switchport.
        p3 = re.compile(
            r'^(?:[a-z]\) +[^\r\n]+[.]|Status +INVALID +indicates +one +'
            r'of +the +following +misconfiguration:)$'
        )

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Port         VLAN Type      Status    MVR-VLAN
            m = p1.match(line)
            if m:
                continue

            # Po10         100  SOURCE    ACTIVE    100-101
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                interface = Common.convert_intf_name(groups['interface'])
                interface_dict = ret_dict.setdefault('interfaces', {}) \
                    .setdefault(interface, {})
                interface_dict.update({
                    'vlan': int(groups['vlan']),
                    'type': groups['type'],
                    'status': groups['status'],
                    'mvr_vlans': groups['mvr_vlans'].split(','),
                })
                continue

            # Status INVALID indicates one of the following misconfiguration:
            # a) Interface is not a switchport.
            m = p3.match(line)
            if m:
                continue

        return ret_dict
