"""show_vrf.py

NXOS parsers for the following show commands:
    * 'show running-config'
"""

# Python
import re
import xmltodict

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common



# ================================================================================
#  Schema for "Parser for show running-config | sec '^advertise evpn multicast'"
# =================================================================================
class ShowRunningConfigTrmSchema(MetaParser):
    """Schema for show running-config | sec '^advertise evpn multicast'"""

    schema = {
             Optional('advertise_evpn_multicast'): bool,
    }


# =================================================================================
#  Schema for "Parser for show running-config | sec '^advertise evpn multicast'"
# =================================================================================
class ShowRunningConfigTrm(ShowRunningConfigTrmSchema):
    """Parser for show running-config | sec '^advertise evpn multicast'"""

    def cli(self):
        result_dict = {}

        # advertise evpn multicast
        p1 = re.compile(r'^advertise +evpn +multicast$')

        cmd = "show running-config | sec '^advertise evpn multicast'"
        out = self.device.execute(cmd)

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                result_dict.update({'advertise_evpn_multicast': True})
                continue

        return result_dict