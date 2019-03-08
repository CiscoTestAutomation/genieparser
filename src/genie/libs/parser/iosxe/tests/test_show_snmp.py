
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# iosxe show_snmp
from genie.libs.parser.iosxe.show_snmp import ShowSnmpMib


# =============================
# Unit test for 'show snmp mib'
# =============================
class test_show_snmp_mib(unittest.TestCase):

    '''Unit test for "show snmp mib" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {}

    golden_output1 = {'execute.return_value': '''