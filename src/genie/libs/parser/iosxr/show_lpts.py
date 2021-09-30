''' show_lpts.py

IOSXR parsers for the following show commands:
    * 'show lpts pfib hardware police'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, ListOf

# ==========================
# Parser for 'show lpts pfib hardware police'
# ==========================

class ShowLptsPfibHardwarePoliceSchema(MetaParser):
    """Schema for show lpts pfib hardware police"""
    schema = {
        "lpts_policer_list": {
            Any(): {
                "lpts_policer": ListOf(
                    {
                        "flow_type": str,
                        "policer": str,
                        "type": str,
                        "curr_rate": str,
                        "burst": str,
                        "accepted": str,
                        "dropped": str,
                        "npu": str,
                    },
                )
            }
        }
    }


class ShowLptsPfibHardwarePolice(ShowLptsPfibHardwarePoliceSchema):
    """Parser for show lpts pfib hardware police"""
    cli_command = 'show lpts pfib hardware police'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Node 0/RP0/CPU0:
        p1 = re.compile(r'^(Node)\s(?P<node>[a-zA-Z0-9\/]+)')

        # Fragment               2       np      474       1000      2            0            0
        # OSPF-mc-known          3       np      1559      1000      0            0            0
        # OSPF-mc-default        4       np      1017      1000      0            0            0
        # OSPF-uc-known          5       np      474       1000      0            0            0
        # OSPF-uc-default        6       np      474       1000      0            0            0
        # BFD-default            10      np      7864      1000      75           0            0
        # BFD-MP-known           11      np      7864      1000      0            0            0
        # BGP-known              16      np      16272     1000      120267993    0            0
        p2 = re.compile(r'^(?P<flow_type>[a-zA-Z-]+)\s+(?P<policer>\d+)\s+(?P<type>\S+)\s+(?P<curr_rate>\d+)\s+(?P<burst>\d+)\s+(?P<accepted>\d+)\s+(?P<dropped>\d+)\s+(?P<npu>\d+)$')


        # Init vars
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                # Parse regexp
                group = m.groupdict()
                node = group['node'] or "None"
                lpts_policer_list = ret_dict.setdefault('lpts_policer_list', {})\
                    .setdefault(node, {})\
                    .setdefault('lpts_policer', [])
                continue

            m = p2.match(line)
            if m:
                # Parse regexp
                group = m.groupdict()
                lpts_policer_list.append({k: v for k, v in group.items()})
                continue


        return ret_dict