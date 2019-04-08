# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_ospf
from genie.libs.parser.iosxr.show_lldp import ShowLldp, ShowLldpEntry, \
                                   ShowLldpNeighborsDetail, \
                                   ShowLldpTraffic, \
                                   ShowLldpInterface


class test_show_lldp(unittest.TestCase):
    dev = Device(name='d')
    empty_output = {'execute.return_value': '      '}
    golden_parsed_output = {}
    golden_output = {'execute.return_value': '''\
    '''}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldp(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldp(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

class test_show_lldp_entry(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {}
    golden_output = {'execute.return_value': '''\
     '''}
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpEntry(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(entry='GigabitEthernet1/0/19')

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpEntry(device=self.dev_c3850)
        parsed_output = obj.parse(entry='*')
        self.assertEqual(parsed_output,self.golden_parsed_output)

class test_show_lldp_neighbor_detail(unittest.TestCase):
    dev = Device(name='empty')
    empty_output = {'execute.return_value': '      '}
    golden_parsed_output = {}
    golden_output = {'execute.return_value': '''\
    '''}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowLldpNeighborsDetail(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowLldpNeighborsDetail(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

class test_show_lldp_traffic(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {}
    golden_output = {'execute.return_value': '''\
    '''}
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpTraffic(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpTraffic(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

class test_show_lldp_interface(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {}
    golden_output = {'execute.return_value': '''\
    '''}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowLldpInterface(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowLldpInterface(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()