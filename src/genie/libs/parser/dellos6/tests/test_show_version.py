
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# iosxe show_ospf
from genie.libs.parser.dellos6.show_version import ShowVersion


class test_show_version(unittest.TestCase):
    '''Unit test for "show ip ospf interface brief" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}
    golden_parsed_output_brief = {    
    'version': {
        'machine_dsc': 'Dell Networking Switch',
        'model': 'N1548',
        'machine_type': 'Dell Networking N1548',
        'serial': 'CN0V143P2829856D0183A00',
        'manufacturer': '0xbc00',
        'bia': 'F8B1.5683.8731',
        'sys_obj_id': '1.3.6.1.4.1.674.10895.3065',
        'soc_ver': 'BCM56150_A0',
        'hw_ver': '2',
        'cpld_ver': '16',
        'versioning': {
            'unit': '1',
            'active_ver': '6.3.2.4',
            'backup_ver': '6.2.5.3',
            'curr_act_ver': '6.3.2.4',
            'next_act_ver': '6.3.2.4'
        }
    }
}

    golden_output_brief = {'execute.return_value': '''
    Machine Description............... Dell Networking Switch
    System Model ID................... N1548
    Machine Type...................... Dell Networking N1548
    Serial Number..................... CN0V143P2829856D0183A00
    Manufacturer...................... 0xbc00
    Burned In MAC Address............. F8B1.5683.8731
    System Object ID.................. 1.3.6.1.4.1.674.10895.3065
    SOC Version....................... BCM56150_A0
    HW Version........................ 2
    CPLD Version...................... 16

    unit active      backup      current-active next-active
    ---- ----------- ----------- -------------- --------------
    1    6.3.2.4     6.2.5.3     6.3.2.4        6.3.2.4
    '''}

    def test_show_version(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowVersion(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)

if __name__ == '__main__':
    unittest.main()