'''show_bfd.py
IOS parser for the following show command
	* show bfd neighbors details
	* show bfd neighbors client <client> details
	* show bfd internal
'''

# import iosxe parser
from genie.libs.parser.iosxe.show_bfd import ShowBfdNeighborsDetails as \
											 ShowBfdNeighborsDetails_iosxe

from genie.libs.parser.iosxe.show_bfd import ShowBfdInternal as \
											 ShowBfdInternal_iosxe


class ShowBfdNeighborsDetails(ShowBfdNeighborsDetails_iosxe):
    """
    IOS parser for the following show command
	  'show bfd neighbors details'
	  'show bfd neighbors client <client> details'
	"""
    pass


class ShowBfdInternal(ShowBfdInternal_iosxe):
    """
    IOS parser for the following show command
	  'show bfd internal'
	"""
    pass