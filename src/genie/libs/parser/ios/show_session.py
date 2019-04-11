"""show_session.py

"""
import re

from genie.metaparser import MetaParser

# import iosxe parser
from genie.libs.parser.iosxe.show_session import ShowLine as ShowLine_iosxe,\
                                                 ShowUsers as ShowUsers_iosxe


class ShowLine(ShowLine_iosxe):
    """Parser for show line"""
    pass


class ShowUsers(ShowUsers_iosxe):
    """Parser for show users"""
    pass