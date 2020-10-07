import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =====================================
# Schema for:
#  * 'show avc sd-service info summary'
# =====================================
class ShowAvcSdServiceInfoSummarySchema(MetaParser):
    """Schema for show avc sd-service info summary."""

    schema = {
        
    }


# =====================================
# Parser for:
#  * 'show avc sd-service info summary'
# =====================================
class ShowAvcSdServiceInfoSummary(ShowAvcSdServiceInfoSummarySchema):
    """Parser for show avc sd-service info summary"""

    cli_command = ['show avc sd-service info summary']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
