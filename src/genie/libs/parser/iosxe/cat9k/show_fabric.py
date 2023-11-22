import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ====================
# Schema for:
#  * 'show fabric ap summary'
# ====================
class ShowFabricApSummarySchema(MetaParser):
    """Schema for show fabric ap summary."""

    schema = {
        "fabric_ap_count": int,
        "ap_name": {
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

        # Number of Fabric AP : 2
        p1 = re.compile(r"^Number\s+of\s+Fabric\s+AP\s:\s+(?P<fabric_ap_count>\d+)")

        # AP0029.C2DE.65B0        2      1852I     0029.c2de.65b0  0029.c2df.d9e0  default location    US    112.201.2.152   Registered
        p2 = re.compile(
            r"^(?P<ap_name>\S+)\s+(?P<slots>\d+)\s+(?P<ap_model>\S+)\s+(?P<ethernet_mac>\S+)\s+(?P<radio_mac>\S+)\s+(?P<location>.*)\s+(?P<country>\S+)\s+(?P<ip_address>\d+\.\d+\.\d+\.\d+)\s+(?P<state>(Registered))")

        fabric_ap_dict = {}
        fabric_ret_dict = {}

        for line in output.splitlines():
            line = line.rstrip()

            # Number of Fabric AP : 2 
            m1 = p1.match(line)
            if m1:
                fabric_ap_count = p1.match(line)
                groups = fabric_ap_count.groupdict()
                fabric_ap_count = int(groups['fabric_ap_count'])
                fabric_ret_dict['fabric_ap_count'] = fabric_ap_count

            # AP0029.C2DE.65B0     2     1852I     0029.c2de.65b0  0029.c2df.d9e0  default location    US    112.201.2.152   Registered
            m2 = p2.match(line)
            if m2:
                groups = m2.groupdict()
                fabric_ap_dict = fabric_ret_dict.setdefault('ap_name', {}).setdefault(groups['ap_name'], {})
                fabric_ap_dict.update({
                    'slots': groups['slots'],
                    'ap_model': groups['ap_model'],
                    'ethernet_mac': groups['ethernet_mac'],
                    'radio_mac': groups['radio_mac'],
                    'location': groups['location'].strip(),
                    'country': groups['country'],
                    'ip_address': groups['ip_address'],
                    'state': groups['state']
                })

        return fabric_ret_dict
