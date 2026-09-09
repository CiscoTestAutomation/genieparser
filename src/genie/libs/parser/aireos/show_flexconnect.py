""" show_flexconnect.py

AireOS parser for the following command:
    * 'show flexconnect group summary'

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

class ShowFlexconnectGroupSummarySchema(MetaParser):
    """Schema for show flexconnect group  summary"""

    schema = {
        "groups_count": int,
        "group_name":  {
            str: {
                "no_of_aps": int
            }
        }
    }

# ====================
# Parser for:
#  * 'show flexconnect group summary'
# ====================
class ShowFlexconnectGroupSummary(ShowFlexconnectGroupSummarySchema):
    """Parser for show flexconnect group summary"""

    cli_command = 'show flexconnect group summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        flexconnect_group_summary_dict = {}
        #FlexConnect Group Summary: Count: 69
        #Group Name            # Aps
        #--------------------  --------
        #
        #FC-AP-Goup-SUPINJ                 13   
        #FC-AP-Group-1001WB                7    
        #FC-AP-Group-1367WB                3    
        #FC-AP-Group-312MA                 7    
        #default-flex-group                0    

        #FlexConnect Group Summary: Count: 69
        flexconnect_group_count_capture = re.compile(r"FlexConnect\s+Group\s+Summary:\sCount:\s+(?P<groups_count>\d+)$")

        #default-flex-group                0
        group_info_capture = re.compile(r"^(?P<group_name>\S+)\s+(?P<no_of_aps>\d+)$")

        remove_lines=('Group Name', '------' )

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

        group_data = {}

        for line in out_filter:
            #FlexConnect Group Summary: Count: 69
            if flexconnect_group_count_capture.match(line):
                flexconnect_group_count = flexconnect_group_count_capture.match(line)
                groups = flexconnect_group_count.groupdict()
                groups_count = int(groups['groups_count'])
                flexconnect_group_summary_dict['groups_count'] = groups_count
            #default-flex-group                0
            elif group_info_capture.match(line):
                group_info_capture_match = group_info_capture.match(line)
                groups =  group_info_capture_match.groupdict()
                group_name = ''
                for k,v in groups.items():
                    if k == 'group_name':
                        group_name = v
                    else: 
                        if k == 'no_of_aps' and v.isdigit():
                            v = int(v)
                        if not flexconnect_group_summary_dict.get('group_name', {}):
                            flexconnect_group_summary_dict['group_name'] = {}
                        flexconnect_group_summary_dict['group_name'][group_name] = {}
                        group_data.update({k:v})
                flexconnect_group_summary_dict['group_name'][group_name].update(group_data)
                group_data = {}
                continue
        
        return flexconnect_group_summary_dict

