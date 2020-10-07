import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =======================================
# Schema for:
#  * 'show redundancy switchover history'
# =======================================
class ShowRedundancySwitchoverHistorySchema(MetaParser):
    """Schema for show redundancy switchover history."""

    schema = {
        
    }


# =======================================
# Parser for:
#  * 'show redundancy switchover history'
# =======================================
class ShowRedundancySwitchoverHistory(ShowRedundancySwitchoverHistorySchema):
    """Parser for show redundancy switchover history"""

    cli_command = ['show redundancy switchover history']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
