"""
IOS Parsers for the following show commands:
    * show redundancy application group {group_id}
    * show redundancy application group all
"""
# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

from genie.libs.parser.iosxe.show_redundancy \
    import ShowRedundancyApplicationGroup as ShowRedundancyApplicationGroup_iosxe


class ShowRedundancyApplicationGroup(ShowRedundancyApplicationGroup_iosxe):
    """
    Parser for:
        * show redundancy application group {group_id}
        * show redundancy application group all
    """
    pass
