'''show_platform.py

IOSXE C9500-32QC parsers for the following show commands:
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


class ShowInventorySchema(ShowInventorySchema_XE):
    ...


# ============================
#  Parser for 'show inventory'
# ============================
class ShowInventory(ShowInventory_XE):
    ...
