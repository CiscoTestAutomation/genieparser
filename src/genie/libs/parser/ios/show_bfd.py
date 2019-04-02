'''show_bfd.py
IOS parser for the following show command
	* show bfd neighbors details
	* show bfd neighbors client <client> details
'''

# import iosxe parser
from genie.libs.parser.iosxe.show_bfd import ShowBfdNeighborsDetails as \
											 ShowBfdNeighborsDetails_iosxe


class ShowBfdNeighborsDetails(ShowBfdNeighborsDetails_iosxe):
    """
    IOS parser for the following show command
	  'show bfd neighbors details'
	  'show bfd neighbors client <client> details'
	"""
    pass
