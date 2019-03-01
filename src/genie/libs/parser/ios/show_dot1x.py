"""show_dot1x.py
   supported commands:
     *  show dot1x
     *  show dot1x all details
     *  show dot1x all statistics
     *  show dot1x all summary
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common

from genie.libs.parser.iosxe.show_dot1x import ShowDot1xAllCount as ShowDot1xAllCount_iosxe,\
                                               ShowDot1xAllDetail as ShowDot1xAllDetail_iosxe,\
                                               ShowDot1x as ShowDot1x_iosxe,\
                                               ShowDot1xAllSummary as ShowDot1xAllSummary_iosxe


class ShowDot1xAllDetail(ShowDot1xAllDetail_iosxe):
    """Parser for show dot1x all details"""
    pass

class ShowDot1x(ShowDot1x_iosxe):
    """Parser for show dot1x"""
    pass


class ShowDot1xAllSummary(ShowDot1xAllSummary_iosxe):
    """Parser for show dot1x all summary"""

    pass

class ShowDot1xAllCount(ShowDot1xAllCount_iosxe):
    """Parser for show dot1x all count"""

    pass