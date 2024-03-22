import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional


# ====================
# Schema for:
#  * 'show fabric ap summary'
# ====================
class ShowFabricApSummarySchema(MetaParser):
    """Schema for show fabric ap summary."""

    schema = {
        "fabric_ap_count": int,
        Optional("ap_name"): {
            str: {
                "slots": str,
                "ap_model": str,
                "ethernet_mac": str,
                "radio_mac": str,
                "location": str,
                "country": str,
                "ip_address": str,
                "state": str
            }
        }
    }


# ====================
# Parser for:
#  * 'show fabric ap summary'
# ====================
class ShowFabricApSummary(ShowFabricApSummarySchema):
    """Parser for show fabric ap summary"""

    # Number of Fabric AP : 2

    # AP Name            Slots   AP Model  Ethernet MAC    Radio MAC       Location               Country    IP Address      State
    # -----------------------------------------------------------------------------------------------------------------------------------
    # AP0029.C2DE.65B0    2      1852I     0029.c2de.65b0  0029.c2df.d9e0  default location         US       112.201.2.152   Registered
    # AP78BC.1AB3.8318    2      3802I     78bc.1ab3.8318  5c5a.c78d.a2e0  default location         US       112.201.2.153   Registered

    cli_command = 'show fabric ap summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        # Number of Fabric AP : 2
        p1 = re.compile(r"^Number\sof\sFabric\sAP\s:\s+(?P<fabric_ap_count>\d+)")

        # AP0029.C2DE.65B0        2      1852I     0029.c2de.65b0  0029.c2df.d9e0  default location    US    112.201.2.152   Registered
        # AP-E1-C8A0              3      C9124AXE-B       488b.0a76.1a64  488b.0a78.c8a0  Global/Ecublens/Buil     US       2001:10b1::9    Registered

        p2 = re.compile(r"^(?P<ap_name>\S+)\s+(?P<slots>\d+)\s+(?P<ap_model>\S+)\s+(?P<ethernet_mac>(([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4}))\s+(?P<radio_mac>(([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4}))\s+(?P<location>([\w\s\/-]+))\s+(?P<country>([A-Z]{2}))\s+(?P<ip_address>((\d{1,3}\.){3}\d{1,3}|([a-fA-F\d]{1,4}:*:?){1,7}[a-fA-F\d]{1,4}))\s+(?P<state>(\w+))")

        for line in output.splitlines():
            line = line.strip()

            # Number of Fabric AP : 2
            m = p1.match(line)
            if m:
                fabric_ap_count = int(m.groupdict().get('fabric_ap_count'))
                ret_dict['fabric_ap_count'] = fabric_ap_count
                continue
            # AP0029.C2DE.65B0     2     1852I     0029.c2de.65b0  0029.c2df.d9e0  default location    US    112.201.2.152   Registered
            m = p2.match(line)
            if m:
                ap_name_dict = ret_dict.setdefault('ap_name', {})
                rgx_dict = m.groupdict()
                ap_name = rgx_dict.get('ap_name')
                ap_dict = ap_name_dict.setdefault(ap_name, {})
                rgx_dict.pop('ap_name')
                ap_dict.update({key: value.strip() for key, value in rgx_dict.items()})
                continue
        return ret_dict
