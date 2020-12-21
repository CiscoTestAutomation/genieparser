
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
from genie.libs.parser.dellos6.show_mac_address_table import ShowMacAddressTable


class test_show_mac_address_table(unittest.TestCase):
    '''Unit test for "show mac address-table" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}
    golden_parsed_output_brief = {
    'macs': {
        'F8B1.5683.8734': {
            'vlan': '20',
            'type': 'Management',
            'port': 'Vl20'
        },
        '0005.CDFA.3F30': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        },
        '0EFC.476B.D1E2': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        },
        '1865.90DF.E791': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        },
        '18C0.4D24.01DE': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        },
        '2424.0E68.4CC7': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        },
        '5897.BDAB.2E0A': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        },
        '5897.BDAB.2E56': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        },
        '6003.08BF.028C': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        },
        'AA43.2D3F.4223': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        },
        'C0D2.F389.D1E0': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        },
        'C61D.4667.C243': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        },
        'D003.4BEC.DF57': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        },
        'E007.1BFE.571A': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        },
        'E063.DA81.0C57': {
            'vlan': '20',
            'type': 'Dynamic',
            'port': 'Gi1/0/1'
        }
    }
}

    golden_output_brief = {'execute.return_value': '''
    Aging time is 300 Sec

    Vlan     Mac Address           Type        Port
    -------- --------------------- ----------- ---------------------
    1        F8B1.5683.8734        Management  Vl1
    20       0005.CDFA.3F30        Dynamic     Gi1/0/1
    20       0EFC.476B.D1E2        Dynamic     Gi1/0/1
    20       1865.90DF.E791        Dynamic     Gi1/0/1
    20       18C0.4D24.01DE        Dynamic     Gi1/0/1
    20       5897.BDAB.2E0A        Dynamic     Gi1/0/1
    20       5897.BDAB.2E56        Dynamic     Gi1/0/1
    20       6003.08BF.028C        Dynamic     Gi1/0/1
    20       AA43.2D3F.4223        Dynamic     Gi1/0/1
    20       C0D2.F389.D1E0        Dynamic     Gi1/0/1
    20       C61D.4667.C243        Dynamic     Gi1/0/1
    20       D003.4BEC.DF57        Dynamic     Gi1/0/1
    20       E007.1BFE.571A        Dynamic     Gi1/0/1
    20       E063.DA81.0C57        Dynamic     Gi1/0/1
    20       F8B1.5683.8734        Management  Vl20

    Total MAC Addresses in use: 15
    '''}

    def test_show_mac_address_table(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowMacAddressTable(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)

if __name__ == '__main__':
    unittest.main()