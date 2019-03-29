'''show_service.py
IOS parser for the following show command
	* show service-group state
	* show service-group stats
'''

# import iosxe parser
from genie.libs.parser.iosxe.show_service import ShowServiceGroupState as \
											 ShowServiceGroupState_iosxe, \
											 ShowServiceGroupStats as \
											 ShowServiceGroupStats_iosxe


class ShowServiceGroupState(ShowServiceGroupState_iosxe):
    '''Parser for show service-group state'''
    pass

class ShowServiceGroupStats(ShowServiceGroupStats_iosxe):
    '''Parser for show service-group stats'''
    pass