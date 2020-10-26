import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =======================================
# Schema for:
#  * 'show telemetry internal connection'
# =======================================
class ShowTelemetryInternalConnectionSchema(MetaParser):
    """Schema for show telemetry internal connection."""

    schema = {
        
    }


# =======================================
# Parser for:
#  * 'show telemetry internal connection'
# =======================================
class ShowTelemetryInternalConnection(ShowTelemetryInternalConnectionSchema):
    """Parser for show telemetry internal connection"""

    cli_command = ['show telemetry internal connection']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
