"""show_system.py

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional, \
                                               Or, \
                                               And, \
                                               Default, \
                                               Use

# import iosxe parser
from genie.libs.parser.iosxe.show_system import ShowClock as ShowClock_iosxe


class ShowClock(ShowClock_iosxe):
    """Parser for show clock"""
    pass