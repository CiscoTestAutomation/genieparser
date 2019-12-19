"""
 c7600 implementation of show_platform.py
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import iosxe parser
from genie.libs.parser.ios.cat6k.show_platform import ShowVersion as ShowVersion_cat6k


class ShowVersion(ShowVersion_cat6k):
    """
    parser for command: show version
    """
    pass

