"""show_acl.py
   supported commands:
     *  show access-lists
"""
# import iosxe parser
from genie.libs.parser.iosxe.show_acl import ShowAccessLists as ShowAccessLists_iosxe


class ShowAccessLists(ShowAccessLists_iosxe):
    """Parser for show access-lists"""
    pass