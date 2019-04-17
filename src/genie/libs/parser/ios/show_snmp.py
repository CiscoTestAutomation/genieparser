''' show_snmp.py

IOSXE parsers for the following show commands:
    * show snmp mib
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser

# import iosxe parser
from genie.libs.parser.iosxe.show_snmp import ShowSnmpMib as ShowSnmpMib_iosxe

# ==========================
# Parser for 'show snmp mib'
# ==========================
class ShowSnmpMib(ShowSnmpMib_iosxe):
    ''' Parser for "show snmp mib" '''
    pass