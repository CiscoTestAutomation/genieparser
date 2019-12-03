"""show_access_session.py
   supported commands:
     * show access-session
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser

# import parser utils
from genie.libs.parser.utils.common import Common

# import iosxe parser
from genie.libs.parser.iosxe.show_access_session import ShowAccessSession as ShowAccessSession_iosxe, \
                ShowAccessSessionInterfaceDetails as ShowAuthenticationSessionsInterfaceDetails_iosxe


class ShowAccessSession(ShowAccessSession_iosxe):
    """Parser for show access-session"""
    pass
    
class ShowAccessSessionInterfaceDetails(ShowAuthenticationSessionsInterfaceDetails_iosxe):
    '''
        Parser for the following show commands:
            * show access-session interface {interface} details
    '''
    pass
