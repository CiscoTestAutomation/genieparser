''' show_logging.py

IOSXE parsers for the following show commands:
    * show logging
    * show logging | include {include}
    * show logging | exclude {exclude}
'''

# import iosxe parser
from genie.libs.parser.iosxe.show_logging import ShowLogging as ShowLogging_iosxe

class ShowLogging(ShowLogging_iosxe):
    '''Parser for:
        * 'show logging'
        * 'show logging | include {include}'
        * 'show logging | exclude {exclude}'
    '''
    pass
