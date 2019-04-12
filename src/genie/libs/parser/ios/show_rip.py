'''
show_rip.py
    *  show ip rip database
'''

# python
import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, Optional

# import iosxe parser
from genie.libs.parser.iosxe.show_rip import \
    ShowIpRipDatabase as ShowIpRipDatabase_iosxe, \
    ShowIpv6Rip as ShowIpv6Rip_iosxe, \
    ShowIpv6RipDatabase as ShowIpv6RipDatabase_iosxe

class ShowIpRipDatabase(ShowIpRipDatabase_iosxe):
    """Parser for :
        show ip rip database
        show ip rip database vrf {vrf}
    """
    pass

class ShowIpv6RipDatabase(ShowIpv6RipDatabase_iosxe):
	"""Parser for :
       show ipv6 rip database
       show ipv6 rip database vrf {vrf}
       """
	pass
	
class ShowIpv6Rip(ShowIpv6Rip_iosxe):
	"""Parser for :
       show ipv6 rip
       show ipv6 rip vrf {vrf}"""
	pass

