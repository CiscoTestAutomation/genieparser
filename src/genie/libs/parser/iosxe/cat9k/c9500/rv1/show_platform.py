'''show_platform.py

IOSXE c9500 parsers for the following show commands:
   * show inventory
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

from genie.libs.parser.iosxe.rv1.show_platform import (
    ShowInventorySchema as ShowInventorySchema_XE,
    ShowInventory as ShowInventory_XE)

from genie.libs.parser.iosxe.show_platform import (
    ShowPlatformSchema as ShowPlatformSchema_RV1,
    ShowPlatform as ShowPlatform_RV1)


class ShowInventorySchema(ShowInventorySchema_XE):
    ...


# ============================
#  Parser for 'show inventory'
# ============================
class ShowInventory(ShowInventory_XE):
    ...


class ShowPlatformSchema(ShowPlatformSchema_RV1):
    ...

# ============================
#  Parser for 'show inventory'
# ============================

class ShowPlatform(ShowPlatform_RV1):
    ...