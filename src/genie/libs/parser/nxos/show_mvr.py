"""show_mvr.py

NXOS parsers for the following show commands:
    * show mvr groups
    * show mvr interface
    * show mvr members
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf, Optional

# Parser utils
from genie.libs.parser.utils.common import Common


class ShowMvrGroupsSchema(MetaParser):
    """Schema for show mvr groups"""

    schema = {
        'groups': {
            Any(): {
                'group_end': str,
                Optional('count'): int,
                Optional('mask'): str,
                'mvr_vlan': int,
                'global_default_mvr_vlan': bool,
                Optional('interface'): str,
            },
        },
    }


class ShowMvrGroups(ShowMvrGroupsSchema):
    """Parser for show mvr groups"""

    cli_command = 'show mvr groups'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # * - Global default MVR VLAN.
        p1 = re.compile(r'^\* +- +Global +default +MVR +VLAN\.$')

        # Group start    Group end       Count  MVR-VLAN Interface
        p2 = re.compile(
            r'^Group +start +Group +end +Count +MVR-VLAN +Interface$'
        )

        # Mask
        p3 = re.compile(r'^Mask$')

        # -------------  --------------- ------ -------- -----------
        p4 = re.compile(r'^-+ +-+ +-+ +-+ +-+$')

        # 228.1.2.240    228.1.2.255     /28     101
        # 230.1.1.1      230.1.1.4        4     *100
        # 225.1.3.1      225.1.3.1        1     *100     Eth1/10
        p5 = re.compile(
            r'^(?P<group_start>(?:\d{1,3}\.){3}\d{1,3}) +'
            r'(?P<group_end>(?:\d{1,3}\.){3}\d{1,3}) +'
            r'(?P<count_mask>/\d+|\d+) +'
            r'(?P<global_default>\*)?(?P<mvr_vlan>\d+)'
            r'(?: +(?P<interface>[\w./-]+))?$'
        )

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # * - Global default MVR VLAN.
            m = p1.match(line)
            if m:
                continue

            # Group start    Group end       Count  MVR-VLAN Interface
            m = p2.match(line)
            if m:
                continue

            # Mask
            m = p3.match(line)
            if m:
                continue

            # -------------  --------------- ------ -------- -----------
            m = p4.match(line)
            if m:
                continue

            # 228.1.2.240    228.1.2.255     /28     101
            # 230.1.1.1      230.1.1.4        4     *100
            # 225.1.3.1      225.1.3.1        1     *100     Eth1/10
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                group_dict = ret_dict.setdefault('groups', {}) \
                    .setdefault(groups['group_start'], {})

                count_mask = groups['count_mask']
                if count_mask.startswith('/'):
                    group_dict['mask'] = count_mask
                else:
                    group_dict['count'] = int(count_mask)

                group_dict.update({
                    'group_end': groups['group_end'],
                    'mvr_vlan': int(groups['mvr_vlan']),
                    'global_default_mvr_vlan': bool(
                        groups['global_default']
                    ),
                })

                if groups['interface']:
                    group_dict['interface'] = Common.convert_intf_name(
                        groups['interface']
                    )
                continue

        return ret_dict


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


# ==================================================
# Schema for 'show mvr members'
# ==================================================
class ShowMvrMembersSchema(MetaParser):
    """Schema for show mvr members"""

    schema = {
        'vlans': {
            Any(): {
                'groups': {
                    Any(): {
                        'status': str,
                        'members': ListOf(str),
                    },
                },
            },
        },
    }


# ==================================================
# Parser for 'show mvr members'
# ==================================================
class ShowMvrMembers(ShowMvrMembersSchema):
    """Parser for show mvr members"""

    cli_command = 'show mvr members'

    def cli(self, command='', output=None):
        if output is None:
            command = command or self.cli_command
            output = self.device.execute(command)

        ret_dict = {}

        # MVR-VLAN  Group Address  Status   Members
        p1 = re.compile(r'^MVR-VLAN +Group +Address +Status +Members$')

        # 100       230.1.1.1     ACTIVE    Po201 Po202 Po203 Po205 Po206
        p2 = re.compile(
            r'^(?P<mvr_vlan>\d+) +(?P<group_address>\S+) +'
            r'(?P<status>\S+) +(?P<members>[\w\.\/\-:\s]+)$'
        )

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # MVR-VLAN  Group Address  Status   Members
            m = p1.match(line)
            if m:
                continue

            # 100       230.1.1.1     ACTIVE    Po201 Po202 Po203 Po205 Po206
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                mvr_vlan = int(groups['mvr_vlan'])
                group_address = groups['group_address']
                members = [
                    Common.convert_intf_name(member)
                    for member in groups['members'].split()
                ]

                group_dict = ret_dict.setdefault('vlans', {}) \
                    .setdefault(mvr_vlan, {}) \
                    .setdefault('groups', {}) \
                    .setdefault(group_address, {})
                group_dict.update({
                    'status': groups['status'],
                    'members': members,
                })
                continue

        return ret_dict
