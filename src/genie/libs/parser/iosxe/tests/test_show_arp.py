# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_arp import ShowArp


# ============================================
# Parser for 'show arp [vrf <WORD>] <WROD>'
# ============================================
class test_show_arp(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "address": {
            "201.0.12.2": {
               "type": "ARPA",
               "mac": "3820.5672.fc51",
               "age": "29",
               "protocol": "Internet",
               "address": "201.0.12.2",
               "interface": "Vlan100"
            },
            "201.0.12.1": {
               "type": "ARPA",
               "protocol": "Internet",
               "address": "201.0.12.1",
               "mac": "58bf.eab6.2f51",
               "interface": "Vlan100"
            },
            "201.0.14.1": {
               "type": "ARPA",
               "protocol": "Internet",
               "address": "201.0.14.1",
               "mac": "58bf.eab6.2f62",
               "interface": "Vlan200"
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Protocol  Address          Age (min)  Hardware Addr   Type   Interface
        Internet  201.0.12.1              -   58bf.eab6.2f51  ARPA   Vlan100
        Internet  201.0.12.2             29   3820.5672.fc51  ARPA   Vlan100
        Internet  201.0.14.1              -   58bf.eab6.2f62  ARPA   Vlan200
    '''}
    
    golden_parsed_output_1 = {
        "address": {
            "10.1.18.1": {
               "type": "ARPA",
               "mac": "0012.7f57.ac80",
               "age": "45",
               "protocol": "Internet",
               "address": "10.1.18.1",
               "interface": "GigabitEthernet0/0"
            },
            "10.1.18.122": {
               "type": "ARPA",
               "protocol": "Internet",
               "address": "10.1.18.122",
               "mac": "58bf.eab6.2f00",
               "interface": "GigabitEthernet0/0"
            },
            "10.1.18.13": {
               "type": "ARPA",
               "mac": "00b0.c215.441d",
               "age": "142",
               "protocol": "Internet",
               "address": "10.1.18.13",
               "interface": "GigabitEthernet0/0"
            },
            "10.1.18.254": {
               "type": "ARPA",
               "mac": "5cf3.fc25.ab76",
               "age": "247",
               "protocol": "Internet",
               "address": "10.1.18.254",
               "interface": "GigabitEthernet0/0"
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''\
        Protocol  Address          Age (min)  Hardware Addr   Type   Interface
        Internet  10.1.18.122             -   58bf.eab6.2f00  ARPA   GigabitEthernet0/0
        Internet  10.1.18.1              45   0012.7f57.ac80  ARPA   GigabitEthernet0/0
        Internet  10.1.18.13            142   00b0.c215.441d  ARPA   GigabitEthernet0/0
        Internet  10.1.18.254           247   5cf3.fc25.ab76  ARPA   GigabitEthernet0/0

    '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowArp(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowArp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowArp(device=self.device)
        parsed_output = obj.parse(vrf='Mgmt-vrf', intf_or_ip='GigabitEthernet0/0')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)


if __name__ == '__main__':
    unittest.main()