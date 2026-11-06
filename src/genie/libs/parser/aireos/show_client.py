""" show_client.py

AireOS parser for the following command:
    * 'show client state summary'

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

class ShowClientStateSummarySchema(MetaParser):
    """Schema for show client state summary"""

    schema = {
        "total_clients": int,
        "state":  {
            str: {
                "no_of_clients": int
            }
        }
        
    }


# ====================
# Parser for:
#  * 'show client state summary'
# ====================
class ShowClientStateSummary(ShowClientStateSummarySchema):
    """Parser for show client state summary"""

    cli_command = 'show client state summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        client_state_summary_dict = {}
        #Client State Summary
        #====================
        #
        #State                          Number of Clients   
        #-----                          -----------------   
        #START                                20                  
        #8021X_REQD                           65                  
        #DHCP_REQD                            3                   
        #RUN                                  2137                
        #-----                          -----------------   
        #Total                                2225 

        p_client_info_capture = re.compile(r"^(?P<state>\S+)\s+(?P<no_of_clients>\S+)$")
        p_total_info_capture = re.compile(r"^Total\s+(?P<total_clients>\d+)$")

        remove_lines=('Client state','=====','State','-----')

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

        client_summary_data = {}

        for line in out_filter:
            #Total                                2225 
            if p_total_info_capture.match(line):
                p_total_info_capture_match = p_total_info_capture.match(line)
                groups = p_total_info_capture_match.groupdict()
                total_clients = int(groups['total_clients'])
                client_state_summary_dict['total_clients'] = total_clients
            #START                                20   
            elif p_client_info_capture.match(line):
                p_client_info_capture_match = p_client_info_capture.match(line)
                groups = p_client_info_capture_match.groupdict()
                state = ''
                for k, v in groups.items():
                    if k == 'state':
                        state = v
                    else:
                        if k != 'state' and v.isdigit():
                            v = int(v)
                        if not client_state_summary_dict.get("state",{}):
                            client_state_summary_dict["state"] = {}
                        client_state_summary_dict['state'][state] = {}
                        client_summary_data.update({k: v})
                client_state_summary_dict['state'][state].update(client_summary_data)
                client_summary_data = {}
                continue
        
        return client_state_summary_dict

           
