""" show_interface.py

AireOS parser for the following command:
    * 'show interface summary'

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ======================
# Schema for:
#  * 'show interface summary'
# ======================
class ShowInterfaceSummarySchema(MetaParser):
    """Schema for show interface summary"""

    schema = {
        "interface_count": int,
        "interface_name": {
            str: {
                "port_type": int,
                "vlan_id": str,
                "type": str,
                "ip_address": str,
                "ap_mgr": str,
                "guest": str
            }
        }
    }

# ====================
# Parser for:
#  * 'show ap summary'
# ====================
class ShowInterfaceSummary(ShowInterfaceSummarySchema):
    """Parser for show interface summary"""

    cli_command = 'show interface summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        int_summary_dict = {}

        #Number of Interfaces.......................... 17

        #Interface Name                   Port Vlan Id  IP Address      Type    Ap Mgr Guest
        #-------------------------------- ---- -------- --------------- ------- ------ -----
        #management                       LAG  3001      172.23.89.35    Static  Yes    No   
        #redundancy-management            LAG  3001      172.23.89.34    Static  No     No   
        #redundancy-port                  -    untagged 169.254.89.34   Static  No     No   
        #non-routable-interface           LAG  2081      192.0.2.129     Dynamic No     No   
        #phsa-lab-cw-dc-ssid-subnet-1     LAG  3101      10.251.1.250    Dynamic No     No   
        #phsa-lab-cw-dc-ssid-subnet-10    LAG  3110      10.251.10.250   Dynamic No     No 

        #Number of Interfaces.......................... 17
        int_count_capture = re.compile(r"^Number\s+of\s+Interfaces\.+ +(?P<int_count>\d+)$")

        #management                       LAG  3001      172.23.89.35    Static  Yes    No   
        int_info_capture = re.compile(
            r"^((?P<int_name>)\S+)\s+(?P<port_type>\S+)\s+(?P<vlan_id>\d+)\s+"
            "(?P<ip_address>\S+)\s+(?P<int_type>\S+)\s+(?P<ap_mgr>\S+)\s+(?P<guest>\S+)\s+$")
        
        remove_lines = ('Interface Name', '------')

            # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines  

        out_filter = filter_lines(raw_output=out, remove_lines=remove_lines)   

        int_summary_data = {}

        for line in out_filter:
            #Number of Interfaces.......................... 17
            if int_count_capture.match(line):
                int_count_match = int_count_capture.match(line)
                groups = int_count_match.groupdict()
                int_count = int(groups['int_count'])
                int_summary_dict['int_count'] = int_count
            #management                       LAG  3001      172.23.89.35    Static  Yes    No   
            elif int_info_capture.match(line):
                int_info_capture_match = int_info_capture.match(line)
                groups = int_info_capture_match.groupdict()
                # interface name is the key to place all the corresponding info
                int_name = ''
                # Loop over all regex matches found
                for k,v in groups.items():
                    if k == 'int_name':
                        int_name = v
                    else:
                        if k != 'vlan_id' and v.isdigit():
                            v = int(v)
                        elif str(v):
                            v = v.strip()
                        if not int_summary_dict.get("int_name", {}):
                            int_summary_dict["int_name"] = {}
                        int_summary_dict['int_name'][int_name] = {}
                        int_summary_data.update({k: v})
                int_summary_dict['int_name'][int_name].update(int_summary_data)
                int_summary_data = {}
                continue

        return int_summary_dict
