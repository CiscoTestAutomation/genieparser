import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =============================
# Schema for:
#  * 'show running-config wlan'
# =============================
class ShowRunningConfigWlanSchema(MetaParser):
    """Schema for show running-config wlan."""

    schema = {
        
    }


# =============================
# Parser for:
#  * 'show running-config wlan'
# =============================
class ShowRunningConfigWlan(ShowRunningConfigWlanSchema):
    """Parser for show running-config wlan"""

    cli_command = ['show running-config wlan']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
