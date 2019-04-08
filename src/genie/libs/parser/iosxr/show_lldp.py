"""show_spanning_tree.py
   supported commands:
     *  show lldp
     *  show lldp entry [<WORD>|*]
     *  show lldp interface [<WORD>]
     *  show lldp neighbors detail
     *  show lldp traffic
"""
import re

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

class ShowLldpSchema(MetaParser):
    """Schema for show lldp"""
    schema = {
        
    }


class ShowLldp(ShowLldpSchema):
    """Parser for show lldp"""

    cli_command = 'show lldp'

    def cli(self, output=None):
    	ret_dict = {}
    	return ret_dict

class ShowLldpEntrySchema(MetaParser):
    """Schema for show lldp entry [<WORD>|*]"""
    schema = {}

class ShowLldpEntry(ShowLldpEntrySchema):
    """Parser for show lldp entry [<WORD>|*]"""

    cli_command = 'show lldp entry {entry}'

    def cli(self, entry='*',output=None):
    	ret_dict = {}
    	return ret_dict

class ShowLldpNeighborsDetail(ShowLldpEntry):
    '''Parser for show lldp neighbors detail'''
    CMD = 'show lldp neighbors detail'

class ShowLldpTrafficSchema(MetaParser):
    """Schema for show lldp traffic"""
    schema = {}

class ShowLldpTraffic(ShowLldpTrafficSchema):
    """Parser for show lldp traffic"""

    cli_command = 'show lldp traffic'

    def cli(self,output=None):
    	ret_dict = {}
    	return ret_dict

class ShowLldpInterfaceSchema(MetaParser):
    """Schema for show lldp interface [<WORD>]"""
    schema = {}

class ShowLldpInterface(ShowLldpInterfaceSchema):
    """Parser for show lldp interface [<WORD>]"""

    cli_command = ['show lldp interface {interface}','show lldp interface']

    def cli(self, interface='',output=None):

    	ret_dict = {}
    	return ret_dict