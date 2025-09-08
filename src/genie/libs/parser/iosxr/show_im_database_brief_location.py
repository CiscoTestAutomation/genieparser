''' show_im_database_brief_location.py

IOSXR parsers for the following show commands:

    * show im database brief location {location}
    * show im database brief location all
'''

# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any


# =======================================================
# Schema for 'show im database brief location {location}'
# =======================================================
class ShowImDatabaseBriefLocationSchema(MetaParser):
    '''Schema for:
        * show im database brief location {location}
        * show im database brief location all
    '''

    schema = {
        Any(): {
            Any(): {
                'handle': str,
                'state': str,
                'mtu': str,
                '#p': int,
                '#c': int,
                'views': str,
                }
            },
        }


# =======================================================
# Parser for 'show im database brief location {location}'
# =======================================================
class ShowImDatabaseBriefLocation(ShowImDatabaseBriefLocationSchema):
    '''Parser for:
        * show im database brief location {location}
        * show im database brief location all
    '''

    cli_command = "show im database brief location {location}"

    def cli(self, location='all', output=None):

        # Execute command
        if output is None:
            out = self.device.execute(self.cli_command.format(location=location))
        else:
            out = output

        # Init
        parsed_dict = {}

        # Node 0/RP0/CPU0 (0x2000)
        # Node 0/2/CPU0 (0x200)
        # Get just the node name (e.g., 0/RP0/CPU0 or 0/2/CPU0)
        p1 = re.compile(r'^Node +(?P<node>(\d+/(?:RP\d+|\d+)/CPU\d+)) \(0x[0-9A-Fa-f]+\)$')

        # 0x08000008 FI0/2/CPU0             up          8000 12 13 GDP|LDP|L3P|OWN
        # 0x08000068 Op0/2/0/25             down           -  0  0 GDP|LDP|L3P|OWN
        # 0x08000218 FH0/2/0/29             shutdown    1514  2  3 GDP|LDP|L3P|OWN
        # 0x7c000010 PT0/RP1/CPU0/0         N/A         1514  1  1 GDP
        # 0x7800000c Nu0                    up          1500  1  1 UL|GDP|LDP|G3P|L3P|OWN
        p2 = re.compile(r'(?P<handle>^0x[0-9A-Fa-f]+)\s+'
                        r'(?P<name>\S+)\s+'
                        r'(?P<state>up|down|shutdown|N/A)\s+'
                        r'(?P<mtu>\d+|[\-]+)\s+'
                        r'(?P<p>\d+)\s+'
                        r'(?P<c>\d+)\s+'
                        r'(?P<views>.*)$')

        for line in out.splitlines():
            line = line.strip()

            # Node 0/RP0/CPU0 (0x2000)
            # Node 0/2/CPU0 (0x200)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                node = group['node']

                im_node_dict = parsed_dict.setdefault(node, {})
                continue

            # 0x08000008 FI0/2/CPU0             up          8000 12 13 GDP|LDP|L3P|OWN
            # 0x08000068 Op0/2/0/25             down           -  0  0 GDP|LDP|L3P|OWN
            # 0x08000218 FH0/2/0/29             shutdown    1514  2  3 GDP|LDP|L3P|OWN
            # 0x7c000010 PT0/RP1/CPU0/0         N/A         1514  1  1 GDP
            # 0x7800000c Nu0                    up          1500  1  1 UL|GDP|LDP|G3P|L3P|OWN
            m = p2.match(line)
            if m:
                group = m.groupdict()
                name_dict = im_node_dict.setdefault(group['name'], {})
                name_dict['handle'] = group['handle']
                name_dict['state'] = group['state']
                name_dict['mtu'] = group['mtu']
                name_dict['#p'] = int(group['p'])
                name_dict['#c'] = int(group['c'])
                name_dict['views'] = group['views']

        return parsed_dict
