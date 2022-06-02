""" show_network.py

AireOS parser for the following command:
    * 'show network summary'

"""

from queue import PriorityQueue
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ======================
# Schema for:
#  * 'show network summary'
# ======================

class ShowNetworkSummarySchema(MetaParser):
    """Schema for show network summary"""

    schema = {
        'rf_network_name': str,
        'ipv4_ap_mode': str
    }

# ======================
# Parser for:
#  * 'show network summary'
# ======================

class ShowNetworkSummary(ShowNetworkSummarySchema):
    """ Parser for show network summary"""

    cli_command = 'show network summary'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        parsed_dict = {}

        #RF-Network Name............................. Decentralized2-Corp
        #IPv4 AP Multicast/Broadcast Mode............ Unicast

        rf_network_name_capture = re.compile(r"^RF-Network\sName\.+\s(?P<network_name>\S+)$")
        ipv4_ap_mode_capture = re.compile(r"^IPv4 AP Multicast\/Broadcast Mode\.+\s(?P<ap_mode>.*)$")

        for line in out.splitlines():
            line = line.strip()

            if rf_network_name_capture.match(line):
                match = rf_network_name_capture.match(line)
                parsed_dict.update({"rf_network_name": match.group("network_name")})
                continue
            elif ipv4_ap_mode_capture.match(line):
                match = ipv4_ap_mode_capture.match(line)
                parsed_dict.update({"ipv4_ap_mode": match.group("ap_mode")})
                continue

        return parsed_dict
        

