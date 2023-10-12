''' show_awips.py

IOSXE parsers for the following show commands:
    * show awips status {mac_address}
'''

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any


# =====================================
# Schema for:
#  * 'show awips status {mac_address}'
# =====================================
class ShowAwipsStatusSchema(MetaParser):
    """Schema for show awips status"""

    schema = {
        Any(): {
            'awips_status': str,
            'forensic_status': str,
            'alarm_message_count': str
        }
    }


# =====================================
# Parser for:
#  * 'show awips status {mac_address}'
# =====================================
class ShowAwipsStatus(ShowAwipsStatusSchema):
    """Parser for show awips status {mac_address}"""

    cli_command = "show awips status {mac_address}"

    def cli(self, mac_address, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mac_address=mac_address))

        ret_dict = {}
        p1 = re.compile(
            # 1416.9d57.b280  ENABLED               CONFIG_NOT_ENABLED                  21965
            r'(?P<radio_mac>(([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4}))\s+(?P<awips_status>(\w+))\s+(?P<forensic_status>(\w+))\s+(?P<alarm_message_count>\d+)\s*')

        for line in output.splitlines():
            line = line.strip()

            # 002c.c8b6.4d40  ENABLED               ENABLED                    709
            m = p1.match(line)
            if m:
                rgx_dict = m.groupdict()
                radio_mac = rgx_dict.get('radio_mac')
                ap_dict = ret_dict.setdefault(radio_mac, dict())
                rgx_dict.pop('radio_mac')
                ap_dict.update(rgx_dict)
                continue
        return ret_dict
