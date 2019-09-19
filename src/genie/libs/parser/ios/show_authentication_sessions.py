''' show_authentication_sessions.py

IOS parsers for the following show commands:
    * show authentication sessions
    * show authentication sessions interface {interface}
    * show authentication sessions interface {interface} details

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common

# import iosxe parser
from genie.libs.parser.iosxe.show_authentication_sessions import \
						ShowAuthenticationSessionsInterfaceDetails as \
						ShowAuthenticationSessionsInterfaceDetails_iosxe, \
						ShowAuthenticationSessions as ShowAuthenticationSessions_iosxe



class ShowAuthenticationSessions(ShowAuthenticationSessions_iosxe):
	'''
		IOS parsers for the following show commands:
	    		* show authentication sessions
	'''
	pass

class ShowAuthenticationSessionsInterface(ShowAuthenticationSessionsInterfaceDetails_iosxe):
	'''
		IOS parsers for the following show commands:
	    	* show authentication sessions interface {interfaces}
	'''
	pass


