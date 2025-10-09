"""
show_igmp.py

IOSXE parsers for the following show commands:

    * show ip igmp snooping groups
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
from genie.libs.parser.utils.common import Common
from genie.parsergen import oper_fill_tabular


# ========================================================
# Parser for 'show ip igmp snooping groups'
# ========================================================

class ShowIpIgmpSnoopingGroupsSchema(MetaParser):
    """
    Schema for 'show ip igmp snooping groups'
    """

    schema = {
        'igmp_groups': {
            Any(): {
                Optional('vlan_id'): str,
                Optional('type'): str,
                Optional('version'): str,
                Optional('port'): str
            },
        }
    }

class ShowIpIgmpSnoopingGroups(ShowIpIgmpSnoopingGroupsSchema):
    """
    Parser for 'show ip igmp snooping groups'
    """
    cli_command = 'show ip igmp snooping groups'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        igmp_dict = {}

        # 12        224.0.1.40               I           v2          Po92
        p1 = re.compile(r'^(?P<vlan_id>\d+) +(?P<group_ip>[\d\.]+) +(?P<type>\w+) +(?P<version>\w+) +(?P<port>[\S,\s]+)$')

        # 12        225.0.0.1                S                       Po92
        p1_0 = re.compile(r'^(?P<vlan_id>\d+) +(?P<group_ip>[\d\.]+) +(?P<type>\w+) +(?P<port>[\S,\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            # 12        224.0.1.40               I           v2          Po92
            m = p1.match(line)
            if m:
                group = m.groupdict()
                igmp_dict.setdefault('igmp_groups', {}).setdefault(group.pop('group_ip'), group)
                continue

            # 12        225.0.0.1                S                       Po92
            m = p1_0.match(line)
            if m:
                group = m.groupdict()
                igmp_dict.setdefault('igmp_groups', {}).setdefault(group.pop('group_ip'), group)
                continue

        return igmp_dict
