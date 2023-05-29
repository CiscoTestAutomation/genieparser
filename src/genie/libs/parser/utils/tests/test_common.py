import unittest

from genie.libs.parser.utils.common import Common


class TestCommon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.common = Common()

    def test_interface_converter(self):
        name = self.common.convert_intf_name('Fa1')
        self.assertEqual(name, 'FastEthernet1')

    def test_interface_converter_ignore_case(self):
        name = self.common.convert_intf_name('fa1', ignore_case=True)
        self.assertEqual(name, 'FastEthernet1')
