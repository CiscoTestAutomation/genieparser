"""show_system.py

"""
import re

from genie.metaparser import MetaParser

# import iosxe parser
from genie.libs.parser.iosxe.show_system import ShowClock as ShowClock_iosxe


class ShowClock(ShowClock_iosxe):
    """Parser for show clock"""
    pass