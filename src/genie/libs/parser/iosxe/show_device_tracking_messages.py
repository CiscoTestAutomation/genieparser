import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# ==================================
# Schema for:
#  * 'show device-tracking messages'
# ==================================
class ShowIPV6DestinationGuardPolicySchema(MetaParser):
    schema = {
        
    }

# ==================================
# Parser for:
#  * 'show device-tracking messages'
# ==================================
class ShowIPV6DestinationGuardPolicyParser(ShowIPV6DestinationGuardPolicySchema):
    cli_command = 'show device-tracking messages'