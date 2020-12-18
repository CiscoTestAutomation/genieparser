
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.nxos.aci.show_firmware import (ShowFirmwareUpgradeStatus,
                                                      ShowFirmwareUpgradeStatusControllerGroup,
                                                      ShowFirmwareRepository)


class TestShowFirmwareUpgradeStatus(unittest.TestCase):
    dev = Device(name='aci')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': """\
 Pod         Node        Current-Firmware      Target-Firmware       Status                     Upgrade-Progress(%)
 ----------  ----------  --------------------  --------------------  -------------------------  --------------------
 1           1           apic-4.2(4o)                                success                    100
 1           101         unknown               unknown               node unreachable           -
 1           102         n9000-14.2(4q)                              not scheduled              0
 1           201         unknown               unknown               node unreachable           -
    """}

    golden_parsed_output = {
        'node': {
            1: {
                'pod': 1,
                'current_firmware': 'apic-4.2(4o)',
                'status': 'success',
                'upgrade_progress_percentage': 100
            },
            101: {
                'pod': 1,
                'current_firmware': 'unknown',
                'target_firmware': 'unknown',
                'status': 'node unreachable'
            },
            102: {
                'pod': 1,
                'current_firmware': 'n9000-14.2(4q)',
                'status': 'not scheduled',
                'upgrade_progress_percentage': 0
            },
            201: {
                'pod': 1,
                'current_firmware': 'unknown',
                'target_firmware': 'unknown',
                'status': 'node unreachable'
            }
        }
    }


    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowFirmwareUpgradeStatus(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowFirmwareUpgradeStatus(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowFirmwareUpgradeStatusSwitchGroup(unittest.TestCase):
    dev = Device(name='aci')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': """\
  Pod         Node        Current-Firmware      Target-Firmware       Status                     Upgrade-Progress(%)   Download-Status            Download-Progress(%)
 ----------  ----------  --------------------  --------------------  -------------------------  --------------------  -------------------------  --------------------
 1           101         n9000-15.0(0.138)     n9000-15.0(0.144)     upgrade in progress        45                    downloaded                 100                 
 1           107         n9000-15.0(0.138)     n9000-15.0(0.144)     waiting in queue           0                     downloaded                 100                 
 1           108         n9000-15.0(0.138)     n9000-15.0(0.144)     upgrade in progress        45                    downloaded                 100                 
 1           112         n9000-15.0(0.138)     n9000-15.0(0.144)     upgrade in progress        45                    downloaded                 100                 
 1           113         n9000-15.0(0.138)     n9000-15.0(0.144)     upgrade in progress        45                    downloaded       
    """}

    golden_parsed_output = {
        'node': {
            101: {
                'pod': 1,
                'current_firmware': 'n9000-15.0(0.138)',
                'status': 'upgrade in progress',
                'target_firmware': 'n9000-15.0(0.144)',
                'upgrade_progress_percentage': 45,
                'download_status': 'downloaded',
                'download_progress_percentage': 100
            },
            107: {
                'pod': 1,
                'current_firmware': 'n9000-15.0(0.138)',
                'status': 'waiting in queue',
                'target_firmware': 'n9000-15.0(0.144)',
                'upgrade_progress_percentage': 0,
                'download_status': 'downloaded',
                'download_progress_percentage': 100
            },
            108: {
                'pod': 1,
                'current_firmware': 'n9000-15.0(0.138)',
                'status': 'upgrade in progress',
                'target_firmware': 'n9000-15.0(0.144)',
                'upgrade_progress_percentage': 45,
                'download_status': 'downloaded',
                'download_progress_percentage': 100
            },
            112: {
                'pod': 1,
                'current_firmware': 'n9000-15.0(0.138)',
                'status': 'upgrade in progress',
                'target_firmware': 'n9000-15.0(0.144)',
                'upgrade_progress_percentage': 45,
                'download_status': 'downloaded',
                'download_progress_percentage': 100
            },
            113: {
                'pod': 1,
                'current_firmware': 'n9000-15.0(0.138)',
                'status': 'upgrade in progress',
                'target_firmware': 'n9000-15.0(0.144)',
                'upgrade_progress_percentage': 45
            }
        }
    }



    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowFirmwareUpgradeStatus(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse(switch_group='group1')

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowFirmwareUpgradeStatus(device=self.dev)
        parsed_output = obj.parse(switch_group='group1')
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowFirmwareUpgradeStatusControllerGroup(unittest.TestCase):
    dev = Device(name='aci')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': """\
 Pod         Node        Current-Firmware      Target-Firmware       Status                     Upgrade-Progress(%)     Last-Firmware-Install-Date
 ----------  ----------  --------------------  --------------------  -------------------------  --------------------  ------------------------------
 1           1           apic-5.0(1k)          apic-5.0(1k)          success                    100                   2020-11-17T18:43:57.000+00:00
"""}

    golden_parsed_output = {
        'node': {
            1: {
                'pod': 1,
                'current_firmware': 'apic-5.0(1k)',
                'status': 'success',
                'target_firmware': 'apic-5.0(1k)',
                'upgrade_progress_percentage': 100,
                'last_firmware_install_date': '2020-11-17T18:43:57.000+00:00'
            }
        }
    }


    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowFirmwareUpgradeStatusControllerGroup(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowFirmwareUpgradeStatusControllerGroup(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowFirmwareUpgradeStatusSwitchGroup(unittest.TestCase):
    dev = Device(name='aci')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': """\
 Name                                      Type        Version        Size(MB)
 ----------------------------------------  ----------  -------------  ----------
 aci-catalog-dk9.70.8.2.bin                catalog     70.8(2)        0.129
 aci-apic-dk9.5.0.1k.bin                   controller  5.0(1k)        6266.102
 aci-catalog-dk9.70.7.4.bin                catalog     70.7(4)        0.128"""}

    golden_parsed_output = {
        'name': {
            'aci-catalog-dk9.70.8.2.bin': {
                'version': {
                    '70.8(2)': {
                        'type': 'catalog',
                        'size': 0.129
                    }
                }
            },
            'aci-apic-dk9.5.0.1k.bin': {
                'version': {
                    '5.0(1k)': {
                        'type': 'controller',
                        'size': 6266.102
                    }
                }
            },
            'aci-catalog-dk9.70.7.4.bin': {
                'version': {
                    '70.7(4)': {
                        'type': 'catalog',
                        'size': 0.128
                    }
                }
            }
        }
    }



    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowFirmwareRepository(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowFirmwareRepository(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()