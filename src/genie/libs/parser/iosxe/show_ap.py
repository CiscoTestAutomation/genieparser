import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ====================
# Schema for:
#  * 'show ap summary'
# ====================
class ShowApSummarySchema(MetaParser):
    """Schema for show ap summary."""

    schema = {
        "ap_neighbor_count": int,
        "ap_name": {
            str: {
                "slots_count": int,
                "ap_model": str,
                "ethernet_mac": str,
                "radio_mac": str,
                "location": str,
                "ap_ip_address": str,
                "state": str
            }
        }
    }


# ====================
# Parser for:
#  * 'show ap summary'
# ====================
class ShowApSummary(ShowApSummarySchema):
    """Parser for show ap summary"""

    cli_command = 'show ap summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ap_summary_dict = {}
        # Number of APs: 149
        #
        # AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State
        # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # a121-cap22                       2      9130AXI   a4b2.3291.9b28  2c57.4119.a060  Fab A  UK          10.6.33.106                               Registered
        # a132-cap15                       2      9130AXI   a4b2.3291.2244  2c57.4120.d2a0  Fab A  UK          10.6.32.146                               Registered
        # a111-cap27                       2      9130AXI   a4b2.3291.225c  2c57.4120.d360  Fab A  UK          10.6.32.118.                              Registered
        # a112-cap11                       2      9130AXI   a4b2.3291.22d0  2c57.4120.d700  Fab A  UK          10.6.33.160                               Registered
        # a112-cap10                       2      9130AXI   a4b2.3291.2420  2c57.4120.b180  Fab A  UK          10.6.33.102                               Registered
        # a112-cap17                       2      9130AXI   a4b2.3291.2434  2c57.4120.b220  Fab A  UK          10.6.32.203                               Registered
        # a112-cap14                       2      9130AXI   a4b2.3291.2438  2c57.4120.b240  Fab A  UK          10.6.32.202                               Registered
        # a122-cap09                       2      9130AXI   a4b2.3291.2450  2c57.4120.b300  Fab A  UK          10.6.33.133                               Registered
        # a131-cap43                       2      9130AXI   a4b2.3291.2454  2c57.4120.b320  Fab A  UK          10.6.33.93                                Registered
        # a122-cap08                       2      9130AXI   a4b2.3291.2458  2c57.4120.b340  Fab A  UK          10.6.32.166                               Registered

        # Number of APs: 149
        ap_neighbor_count_capture = re.compile(r"^Number\s+of\s+APs:\s+(?P<ap_neighbor_count>\d+)")
        # a121-cap22                       2      9130AXI   a4b2.3291.9b28  2c57.4119.a060  Fab A  UK          10.6.33.106                               Registered
        ap_neighbor_info_capture = re.compile(
            r"^(?P<ap_name>\S+)\s+(?P<slots_count>\d+)\s+(?P<ap_model>\S+)\s+(?P<ethernet_mac>\S+)\s+(?P<radio_mac>\S+)(?P<location>.*)\s+(?P<ap_ip_address>\d+\.\d+\.\d+\.\d+)\s+(?P<state>(Registered))")

        remove_lines = ('AP Name', '----')

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

        ap_summary_data = {}

        for line in out_filter:
            # Number of APs: 149
            if ap_neighbor_count_capture.match(line):
                ap_neighbor_count_match = ap_neighbor_count_capture.match(line)
                groups = ap_neighbor_count_match.groupdict()
                ap_neighbor_count = int(groups['ap_neighbor_count'])
                ap_summary_dict['ap_neighbor_count'] = ap_neighbor_count
            # a121-cap22                       2      9130AXI   a4b2.3291.9b28  2c57.4119.a060  Fab A  UK          10.6.33.106                               Registered
            elif ap_neighbor_info_capture.match(line):
                ap_neighbor_info_match = ap_neighbor_info_capture.match(line)
                groups = ap_neighbor_info_match.groupdict()
                # ap name is the key to place all the ap neighbor info
                ap_name = ''
                # Loop over all regex matches found
                for k, v in groups.items():
                    # If the key value is ap_name, update the outer ap_name variable with the ap_name regex match
                    if k == 'ap_name':
                        ap_name = v
                    else:
                        # ap_model can sometimes be a digit e.g., '4800'. This needs to be a string.
                        if k != 'ap_model' and v.isdigit():
                            v = int(v)
                        elif str(v):
                            # The location value can be any value as a string but need to strip the whitespace
                            v = v.strip()
                        if not ap_summary_dict.get("ap_name", {}):
                            ap_summary_dict["ap_name"] = {}
                        ap_summary_dict['ap_name'][ap_name] = {}
                        ap_summary_data.update({k: v})
                ap_summary_dict['ap_name'][ap_name].update(ap_summary_data)
                ap_summary_data = {}
                continue

        return ap_summary_dict

