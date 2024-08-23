""" show_advanced.py

AireOS parser for the following commands:
    * 'show advanced 802.11a summary'
    * 'show advanced 802.11b summary'


"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ======================
# Schema for:
#  * 'show advanced 802.11a summary'
# ======================
class ShowAdvanced80211aSummarySchema(MetaParser):
    """Schema for show advanced 802.11a summary"""

    schema = {
        "advanced_802.11a_summary": {
            str: {
                "mac_address": str,
                "slot": int,
                "admin_status": str,
                "operational_status": str,
                "channel": str,
                "tx_power": str,
                "bss_color": str
            }
        }
    }

# ====================
# Parser for:
#  * 'show advanced 802.11a summary'
# ====================
class ShowAdvanced80211aSummary(ShowAdvanced80211aSummarySchema):
    """Parser for show advanced 802.11a summary"""

    cli_command = 'show advanced 802.11a summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        advanced_summary_dict = {}

        #Member RRM Information
        #AP Name                          MAC Address       Slot Admin    Oper        Channel            TxPower       BSS Color
        #-------------------------------- ----------------- ---- -------- ----------- ------------------ ------------- ----------
        #VCH-477337-RAVSNG-FL01-009       78:72:5d:2a:12:f0  1   ENABLED  UP          (157,161)*         *4/8 (14 dBm) N/A      
        #VCH-477337-RAVSNG-FL02-009       78:72:5d:ad:06:30  1   ENABLED  UP          (56,52)*           *3/6 (11 dBm) N/A      
        #VCH-477337-RAVSNG-FL03-006       78:72:5d:d0:79:c0  1   ENABLED  UP          (157,161)*         *5/8 (11 dBm) N/A      

        #VCH-477337-RAVSNG-FL01-009       78:72:5d:2a:12:f0  1   ENABLED  UP          (157,161)*         *4/8 (14 dBm) N/A  
        ap_info_capture = re.compile(
            r"^(?P<ap_name>\S+)\s+(?P<mac_address>\S+)\s+"
            "(?P<slot>\d+)\s+(?P<admin_status>\S+)\s+(?P<operational_status>\S+)\s+"
            "(?P<channel>\S+)\s+(?P<tx_power>.*)\s+(?P<bss_color>\S+)$")

        remove_lines = ("Member ", "AP Name", "--------")

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

        advanced_summary_data = {}

        for line in out_filter:
            #VCH-477337-RAVSNG-FL01-009       78:72:5d:2a:12:f0  1   ENABLED  UP          (157,161)*         *4/8 (14 dBm) N/A  
            if ap_info_capture.match(line):
                ap_info_capture_match = ap_info_capture.match(line)
                groups = ap_info_capture_match.groupdict()
                ap_name = ''
                for k,v in groups.items():
                    if k == 'ap_name':
                        ap_name = v
                    else:
                        if k == "slot" and v.isdigit():
                            v = int(v)
                        if not advanced_summary_dict.get("advanced_802.11a_summary", {}):
                            advanced_summary_dict["advanced_802.11a_summary"] = {}
                        advanced_summary_dict["advanced_802.11a_summary"][ap_name] = {}
                        advanced_summary_data.update({k: v})
                advanced_summary_dict["advanced_802.11a_summary"][ap_name].update(advanced_summary_data)
                advanced_summary_data = {}
                continue

        return advanced_summary_dict

# ======================
# Schema for:
#  * 'show advanced 802.11b summary'
# ======================
class ShowAdvanced80211bSummarySchema(MetaParser):
    """Schema for show advanced 802.11b summary"""

    schema = {
        "advanced_802.11b_summary": {
            str: {
                "mac_address": str,
                "slot": int,
                "admin_status": str,
                "operational_status": str,
                "channel": str,
                "tx_power": str,
                "bss_color": str
            }
        }
    }

# ====================
# Parser for:
#  * 'show advanced 802.11b summary'
# ====================
class ShowAdvanced80211bSummary(ShowAdvanced80211bSummarySchema):
    """Parser for show advanced 802.11b summary"""

    cli_command = 'show advanced 802.11b summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        advanced_summary_dict = {}

        #Member RRM Information
        #AP Name                          MAC Address       Slot Admin    Oper        Channel            TxPower       BSS Color
        #-------------------------------- ----------------- ---- -------- ----------- ------------------ ------------- ----------
        #VCH-477337-RAVSNG-FL01-009       78:72:5d:2a:12:f0  1   ENABLED  UP          (157,161)*         *4/8 (14 dBm) N/A      
        #VCH-477337-RAVSNG-FL02-009       78:72:5d:ad:06:30  1   ENABLED  UP          (56,52)*           *3/6 (11 dBm) N/A      
        #VCH-477337-RAVSNG-FL03-006       78:72:5d:d0:79:c0  1   ENABLED  UP          (157,161)*         *5/8 (11 dBm) N/A      

        #VCH-477337-RAVSNG-FL01-009       78:72:5d:2a:12:f0  1   ENABLED  UP          (157,161)*         *4/8 (14 dBm) N/A  
        ap_info_capture = re.compile(
            r"^(?P<ap_name>\S+)\s+(?P<mac_address>\S+)\s+"
            "(?P<slot>\d+)\s+(?P<admin_status>\S+)\s+(?P<operational_status>\S+)\s+"
            "(?P<channel>\S+)\s+(?P<tx_power>.*)\s+(?P<bss_color>\S+)$")

        remove_lines = ("Member ", "AP Name", "--------")

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

        advanced_summary_data = {}

        for line in out_filter:
            #VCH-477337-RAVSNG-FL01-009       78:72:5d:2a:12:f0  1   ENABLED  UP          (157,161)*         *4/8 (14 dBm) N/A  
            if ap_info_capture.match(line):
                ap_info_capture_match = ap_info_capture.match(line)
                groups = ap_info_capture_match.groupdict()
                ap_name = ''
                for k,v in groups.items():
                    if k == 'ap_name':
                        ap_name = v
                    else:
                        if k == "slot" and v.isdigit():
                            v = int(v)
                        if not advanced_summary_dict.get("advanced_802.11b_summary", {}):
                            advanced_summary_dict["advanced_802.11b_summary"] = {}
                        advanced_summary_dict["advanced_802.11b_summary"][ap_name] = {}
                        advanced_summary_data.update({k: v})
                advanced_summary_dict["advanced_802.11b_summary"][ap_name].update(advanced_summary_data)
                advanced_summary_data = {}
                continue

        return advanced_summary_dict




