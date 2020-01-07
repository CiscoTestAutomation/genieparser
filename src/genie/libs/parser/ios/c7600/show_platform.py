"""
 c7600 implementation of show_platform.py
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import cat6k parser
from genie.libs.parser.ios.cat6k.show_platform import (Dir as Dir_cat6k,
                                                       ShowVersion as ShowVersion_cat6k,
                                                       ShowRedundancy as ShowRedundancy_cat6k,
                                                       ShowInventory as ShowInventory_cat6k,
                                                       ShowModule as ShowModule_cat6k)

class ShowVersion(ShowVersion_cat6k):
    """
    parser for command: show version
    """
    pass

class Dir(Dir_cat6k):
    """
    parser for command: dir
    """
    pass

class ShowRedundancy(ShowRedundancy_cat6k):
    """
    Parser for command:
        * show redundancy
    """
    pass

class ShowInventory(ShowInventory_cat6k):
    """
    Parser for command:
        * show inventory
    """
    pass

class ShowModule(ShowModule_cat6k):
    """
    Parser for command:
        * show module
    """
    pass