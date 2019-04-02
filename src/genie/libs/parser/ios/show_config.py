''' show_config.py

IOS parsers for the following show commands:
    * show configuration lock
'''

# import iosxe parser
from genie.libs.parser.iosxe.show_config import ShowConfigurationLock as \
												ShowConfigurationLock_iosxe


class ShowConfigurationLock(ShowConfigurationLock_iosxe):
    """ Parser for show configuration lock """
    pass
