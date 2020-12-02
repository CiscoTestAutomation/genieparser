import unittest
from unittest.mock import Mock

from pyats.topology import loader, Device
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_chassis import ShowChassisFpcDetail,\
                                                 ShowChassisEnvironmentRoutingEngine,\
                                                 ShowChassisFirmware,\
                                                 ShowChassisFirmwareNoForwarding,\
                                                 ShowChassisFpc,\
                                                 ShowChassisRoutingEngine,\
                                                 ShowChassisRoutingEngineNoForwarding,\
                                                 ShowChassisHardware,\
                                                 ShowChassisHardwareDetail,\
                                                 ShowChassisHardwareDetailNoForwarding,\
                                                 ShowChassisHardwareExtensive,\
                                                 ShowChassisHardwareExtensiveNoForwarding,\
                                                 ShowChassisEnvironment,\
                                                 ShowChassisAlarms,\
                                                 ShowChassisFabricSummary,\
                                                 ShowChassisFabricPlane

class TestShowChassisFpcDetail(unittest.TestCase):
    """ Unit tests for:
            * show chassis fpc detail
    """

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show chassis fpc detail
        Slot 0 information:
        State                               Online    
        Temperature                      Testing
        Total CPU DRAM                  511 MB
        Total RLDRAM                     10 MB
        Total DDR DRAM                    0 MB
        FIPS Capable                        False 
        FIPS Mode                           False 
        Start time                          2019-08-29 09:09:16 UTC
        Uptime                              208 days, 22 hours, 50 minutes, 26 seconds
    '''}

    golden_parsed_output = {
        "fpc-information": {
        "fpc": {
            "fips-capable": "False",
            "fips-mode": "False",
            "memory-ddr-dram-size": "0",
            "memory-dram-size": "511",
            "memory-rldram-size": "10",
            "slot": "0",
            "start-time": {
                "#text": "2019-08-29 09:09:16 UTC"
            },
            "state": "Online",
            "temperature": {
                "#text": "Testing"
            },
            "up-time": {
                "#text": "208 days, 22 hours, 50 minutes, 26 seconds"
            }
        }
    }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisFpcDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisFpcDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowChassisEnvironmentRoutingEngine(unittest.TestCase):
    """ Unit tests for:
            * show chassis environment routing-engine
    """

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show chassis environment routing-engine
        Routing Engine 0 status:
        State                      Online Master
    '''}

    golden_parsed_output = {
        "environment-component-information": {
            "environment-component-item": {
                "name": "Routing Engine 0",
                "state": "Online Master"
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisEnvironmentRoutingEngine(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisEnvironmentRoutingEngine(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

class TestShowChassisFirmware(unittest.TestCase):
    """ Unit tests for:
            * show chassis firmware
    """

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': 
    ''' show chassis firmware
        Part                     Type       Version
        FPC 0                    ROM        PC Bios                                    
                                O/S        Version 19.2R1.8 by builder on 2019-06-21 17:52:23 UTC
    '''}

    golden_parsed_output = {
        "firmware-information": {
            "chassis": {
                "chassis-module": {
                    "firmware": [
                        {
                            "firmware-version": "PC Bios",
                            "type": "ROM"
                        },
                        {
                            "firmware-version": "Version 19.2R1.8 by builder on 2019-06-21 17:52:23 UTC",
                            "type": "O/S"
                        }
                    ],
                    "name": "FPC 0"
                }
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisFirmware(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisFirmware(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowChassisFirmwareNoForwarding(unittest.TestCase):
    """ Unit tests for:
            * show chassis firmware no-forwarding
    """

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': 
    ''' show chassis firmware no-forwarding
        Part                     Type       Version
        FPC 0                    ROM        PC Bios                                    
                                O/S        Version 19.2R1.8 by builder on 2019-06-21 17:52:23 UTC
    '''}

    golden_parsed_output = {
        "firmware-information": {
            "chassis": {
                "chassis-module": {
                    "firmware": [
                        {
                            "firmware-version": "PC Bios",
                            "type": "ROM"
                        },
                        {
                            "firmware-version": "Version 19.2R1.8 by builder on 2019-06-21 17:52:23 UTC",
                            "type": "O/S"
                        }
                    ],
                    "name": "FPC 0"
                }
            }
        }
        
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisFirmwareNoForwarding(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisFirmwareNoForwarding(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowChassisHardware(unittest.TestCase):

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': 
    ''' show chassis hardware
        Hardware inventory:
        Item             Version  Part number  Serial number     Description
        Chassis                                VM5D4C6B3599      VMX
        Midplane        
        Routing Engine 0                                         RE-VMX
        CB 0                                                     VMX SCB
        FPC 0                                                    Virtual FPC
          CPU            Rev. 1.0 RIOT-LITE    BUILTIN          
          MIC 0                                                  Virtual
            PIC 0                 BUILTIN      BUILTIN           Virtual
    '''}

    golden_parsed_output = {
        "chassis-inventory": {
            "chassis": {
                "@junos:style": "inventory",
                "chassis-module": [
                    {
                        "name": "Midplane"
                    },
                    {
                        "description": "RE-VMX",
                        "name": "Routing Engine 0"
                    },
                    {
                        "description": "VMX SCB",
                        "name": "CB 0"
                    },
                    {
                        "chassis-sub-module": [
                            {
                                "name": "CPU",
                                "part-number": "RIOT-LITE",
                                "serial-number": "BUILTIN",
                                "version": "Rev. 1.0"
                            },
                            {
                                "chassis-sub-sub-module": {
                                    "description": "Virtual",
                                    "name": "PIC 0",
                                    "part-number": "BUILTIN",
                                    "serial-number": "BUILTIN"
                                },
                                "description": "Virtual",
                                "name": "MIC 0"
                            }
                        ],
                        "description": "Virtual FPC",
                        "name": "FPC 0"
                    }
                ],
                "description": "VMX",
                "name": "Chassis",
                "serial-number": "VM5D4C6B3599"
            }
    }
        
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisHardware(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisHardware(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowChassisHardwareDetail(unittest.TestCase):

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': 
    ''' show chassis hardware detail
        Hardware inventory:
        Item             Version  Part number  Serial number     Description
        Chassis                                VM5D4C6B3599      VMX
        Midplane        
        Routing Engine 0                                         RE-VMX
          cd0   27649 MB  VMware Virtual IDE Har 00000000000000000001 Hard Disk
        CB 0                                                     VMX SCB
        FPC 0                                                    Virtual FPC
          CPU            Rev. 1.0 RIOT-LITE    BUILTIN          
          MIC 0                                                  Virtual
            PIC 0                 BUILTIN      BUILTIN           Virtual
    '''}

    golden_parsed_output = {
        "chassis-inventory": {
            "chassis": {
                "@junos:style": "inventory",
                "chassis-module": [
                    {
                        "name": "Midplane"
                    },
                    {
                        "chassis-re-disk-module": {
                            "description": "Hard Disk",
                            "disk-size": "27649",
                            "model": "VMware Virtual IDE Har",
                            "name": "cd0",
                            "serial-number": "00000000000000000001"
                        },
                        "description": "RE-VMX",
                        "name": "Routing Engine 0"
                    },
                    {
                        "description": "VMX SCB",
                        "name": "CB 0"
                    },
                    {
                        "chassis-sub-module": [
                            {
                                "name": "CPU",
                                "part-number": "RIOT-LITE",
                                "serial-number": "BUILTIN",
                                "version": "Rev. 1.0"
                            },
                            {
                                "chassis-sub-sub-module": {
                                    "description": "Virtual",
                                    "name": "PIC 0",
                                    "part-number": "BUILTIN",
                                    "serial-number": "BUILTIN"
                                },
                                "description": "Virtual",
                                "name": "MIC 0"
                            }
                        ],
                        "description": "Virtual FPC",
                        "name": "FPC 0"
                    }
                ],
                "description": "VMX",
                "name": "Chassis",
                "serial-number": "VM5D4C6B3599"
            }
        }
        
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisHardwareDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisHardwareDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowChassisHardwareDetailNoForwarding(unittest.TestCase):

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': 
    ''' show chassis hardware detail no-forwarding
        Hardware inventory:
        Item             Version  Part number  Serial number     Description
        Chassis                                VM5D4C6B3599      VMX
        Midplane        
        Routing Engine 0                                         RE-VMX
          cd0   27649 MB  VMware Virtual IDE Har 00000000000000000001 Hard Disk
        CB 0                                                     VMX SCB
        FPC 0                                                    Virtual FPC
          CPU            Rev. 1.0 RIOT-LITE    BUILTIN          
          MIC 0                                                  Virtual
            PIC 0                 BUILTIN      BUILTIN           Virtual
    '''}

    golden_parsed_output = {
        "chassis-inventory": {
            "chassis": {
                "@junos:style": "inventory",
                "chassis-module": [
                    {
                        "name": "Midplane"
                    },
                    {
                        "chassis-re-disk-module": {
                            "description": "Hard Disk",
                            "disk-size": "27649",
                            "model": "VMware Virtual IDE Har",
                            "name": "cd0",
                            "serial-number": "00000000000000000001"
                        },
                        "description": "RE-VMX",
                        "name": "Routing Engine 0"
                    },
                    {
                        "description": "VMX SCB",
                        "name": "CB 0"
                    },
                    {
                        "chassis-sub-module": [
                            {
                                "name": "CPU",
                                "part-number": "RIOT-LITE",
                                "serial-number": "BUILTIN",
                                "version": "Rev. 1.0"
                            },
                            {
                                "chassis-sub-sub-module": {
                                    "description": "Virtual",
                                    "name": "PIC 0",
                                    "part-number": "BUILTIN",
                                    "serial-number": "BUILTIN"
                                },
                                "description": "Virtual",
                                "name": "MIC 0"
                            }
                        ],
                        "description": "Virtual FPC",
                        "name": "FPC 0"
                    }
                ],
                "description": "VMX",
                "name": "Chassis",
                "serial-number": "VM5D4C6B3599"
            }
        }
        
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisHardwareDetailNoForwarding(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisHardwareDetailNoForwarding(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

class TestShowChassisHardwareExtensive(unittest.TestCase):

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': 
    ''' show chassis hardware extensive
        Hardware inventory:
        Item             Version  Part number  Serial number     Description
        Chassis                                VM5D4C6B3599      VMX
        Jedec Code:   0x7fb0            EEPROM Version:    0x02
                                        S/N:               VM5D4C6B3599
        Assembly ID:  0x0567            Assembly Version:  00.00
        Date:         00-00-0000        Assembly Flags:    0x00
        ID: VMX                        
        Board Information Record:
        Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        I2C Hex Data:
        Address 0x00: 7f b0 02 ff 05 67 00 00 00 00 00 00 00 00 00 00
        Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x20: 56 4d 35 44 34 43 36 42 33 35 39 39 00 00 00 00
        Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Midplane        
        Routing Engine 0                                         RE-VMX
        Jedec Code:   0x0000            EEPROM Version:    0x00
        Assembly ID:  0x0bab            Assembly Version:  00.00
        Date:         00-00-0000        Assembly Flags:    0x00
        ID: RE-VMX                     
        Board Information Record:
        Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        I2C Hex Data:
        Address 0x00: 00 00 00 00 0b ab 00 00 00 00 00 00 00 00 00 00
        Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        cd0   27649 MB  VMware Virtual IDE Har 00000000000000000001 Hard Disk
        CB 0                                                     VMX SCB
        Jedec Code:   0x7fb0            EEPROM Version:    0x00
        Assembly ID:  0x0bb5            Assembly Version:  00.00
        Date:         00-00-0000        Assembly Flags:    0x00
        ID: VMX SCB                            
        Board Information Record:
        Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        I2C Hex Data:
        Address 0x00: 7f b0 00 00 0b b5 00 00 00 00 00 00 00 00 00 00
        Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        FPC 0                                                    Virtual FPC
        Jedec Code:   0x7fb0            EEPROM Version:    0x00
        Assembly ID:  0x0baa            Assembly Version:  00.00
        Date:         00-00-0000        Assembly Flags:    0x00
        ID: Virtual FPC                
        Board Information Record:
        Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        I2C Hex Data:
        Address 0x00: 7f b0 00 00 0b aa 00 00 00 00 00 00 00 00 00 00
        Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        CPU            Rev. 1.0 RIOT-LITE    BUILTIN          
        Jedec Code:   0x7fb0            EEPROM Version:    0x02
        P/N:          RIOT-LITE         S/N:               BUILTIN
        Assembly ID:  0xfa4e            Assembly Version:  01.00
        Date:         08-18-2013        Assembly Flags:    0x01
        Version:      Rev. 1.0
        Board Information Record:
        Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        I2C Hex Data:
        Address 0x00: 7f b0 02 00 fa 4e 01 00 52 65 76 2e 20 31 2e 30
        Address 0x10: 00 00 00 00 52 49 4f 54 2d 4c 49 54 45 00 00 00
        Address 0x20: 42 55 49 4c 54 49 4e 00 00 00 00 00 01 12 08 07
        Address 0x30: dd 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        MIC 0                                                  Virtual
        Jedec Code:   0x0000            EEPROM Version:    0x00
        Assembly ID:  0x0a7d            Assembly Version:  00.00
        Date:         00-00-0000        Assembly Flags:    0x00
        ID: Virtual                    
        Board Information Record:
        Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        I2C Hex Data:
        Address 0x00: 00 00 00 00 0a 7d 00 00 00 00 00 00 00 00 00 00
        Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x70: 00 00 00 00 00 00 00 00 27 41 0f 08 83 80 f0 86
            PIC 0                 BUILTIN      BUILTIN           Virtual
    '''}

    golden_parsed_output = {
        "chassis-inventory": {
            "chassis": {
                "@junos:style": "inventory",
                "chassis-module": [
                    {
                        "name": "Midplane"
                    },
                    {
                        "chassis-re-disk-module": {
                            "description": "Hard Disk",
                            "disk-size": "27649",
                            "model": "VMware Virtual IDE Har",
                            "name": "cd0",
                            "serial-number": "00000000000000000001"
                        },
                        "description": "RE-VMX",
                        "i2c-information": {
                            "assembly-flags": "0x00",
                            "assembly-identifier": "0x0bab",
                            "assembly-version": "00.00",
                            "board-information-record": "Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                            "eeprom-version": "0x00",
                            "i2c-data": [
                                "Address 0x00: 00 00 00 00 0b ab 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                            ],
                            "i2c-identifier": "RE-VMX",
                            "i2c-version": None,
                            "jedec-code": "0x0000",
                            "manufacture-date": "00-00-0000",
                            "part-number": None,
                            "serial-number": None
                        },
                        "name": "Routing Engine 0"
                    },
                    {
                        "description": "VMX SCB",
                        "i2c-information": {
                            "assembly-flags": "0x00",
                            "assembly-identifier": "0x0bb5",
                            "assembly-version": "00.00",
                            "board-information-record": "Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                            "eeprom-version": "0x00",
                            "i2c-data": [
                                "Address 0x00: 7f b0 00 00 0b b5 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                            ],
                            "i2c-identifier": "VMX SCB",
                            "i2c-version": None,
                            "jedec-code": "0x7fb0",
                            "manufacture-date": "00-00-0000",
                            "part-number": None,
                            "serial-number": None
                        },
                        "name": "CB 0"
                    },
                    {
                        "chassis-sub-module": [
                            {
                                "chassis-sub-sub-module": {
                                    "description": "Virtual",
                                    "name": "PIC 0",
                                    "part-number": "BUILTIN",
                                    "serial-number": "BUILTIN"
                                },
                                "description": "Virtual",
                                "i2c-information": {
                                    "assembly-flags": "0x00",
                                    "assembly-identifier": "0x0a7d",
                                    "assembly-version": "00.00",
                                    "board-information-record": "Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                    "eeprom-version": "0x00",
                                    "i2c-data": [
                                        "Address 0x00: 00 00 00 00 0a 7d 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x70: 00 00 00 00 00 00 00 00 27 41 0f 08 83 80 f0 86"
                                    ],
                                    "i2c-identifier": "Virtual",
                                    "i2c-version": None,
                                    "jedec-code": "0x0000",
                                    "manufacture-date": "00-00-0000",
                                    "part-number": None,
                                    "serial-number": None
                                },
                                "name": "MIC 0"
                            },
                            {
                                "i2c-information": {
                                    "assembly-flags": "0x01",
                                    "assembly-identifier": "0xfa4e",
                                    "assembly-version": "01.00",
                                    "board-information-record": "Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                    "eeprom-version": "0x02",
                                    "i2c-data": [
                                        "Address 0x00: 7f b0 02 00 fa 4e 01 00 52 65 76 2e 20 31 2e 30",
                                        "Address 0x10: 00 00 00 00 52 49 4f 54 2d 4c 49 54 45 00 00 00",
                                        "Address 0x20: 42 55 49 4c 54 49 4e 00 00 00 00 00 01 12 08 07",
                                        "Address 0x30: dd 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                                    ],
                                    "i2c-identifier": None,
                                    "i2c-version": "Rev. 1.0",
                                    "jedec-code": "0x7fb0",
                                    "manufacture-date": "08-18-2013",
                                    "part-number": None,
                                    "serial-number": "BUILTIN"
                                },
                                "name": "CPU",
                                "part-number": "RIOT-LITE",
                                "serial-number": "BUILTIN",
                                "version": "Rev. 1.0"
                            }
                        ],
                        "description": "Virtual FPC",
                        "i2c-information": {
                            "assembly-flags": "0x00",
                            "assembly-identifier": "0x0baa",
                            "assembly-version": "00.00",
                            "board-information-record": "Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                            "eeprom-version": "0x00",
                            "i2c-data": [
                                "Address 0x00: 7f b0 00 00 0b aa 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                            ],
                            "i2c-identifier": "Virtual FPC",
                            "i2c-version": None,
                            "jedec-code": "0x7fb0",
                            "manufacture-date": "00-00-0000",
                            "part-number": None,
                            "serial-number": None
                        },
                        "name": "FPC 0"
                    }
                ],
                "description": "VMX",
                "i2c-information": {
                    "assembly-flags": "0x00",
                    "assembly-identifier": "0x0567",
                    "assembly-version": "00.00",
                    "board-information-record": "Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                    "eeprom-version": "0x02",
                    "i2c-data": [
                        "Address 0x00: 7f b0 02 ff 05 67 00 00 00 00 00 00 00 00 00 00",
                        "Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                        "Address 0x20: 56 4d 35 44 34 43 36 42 33 35 39 39 00 00 00 00",
                        "Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                        "Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                        "Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                        "Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                        "Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                    ],
                    "i2c-identifier": "VMX",
                    "i2c-version": None,
                    "jedec-code": "0x7fb0",
                    "manufacture-date": "00-00-0000",
                    "part-number": None,
                    "serial-number": "VM5D4C6B3599"
                },
                "name": "Chassis",
                "serial-number": "VM5D4C6B3599"
            }
        }
        
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisHardwareExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisHardwareExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowChassisHardwareExtensiveNoForwarding(unittest.TestCase):

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': 
    ''' show chassis hardware extensive no-forwarding
        Hardware inventory:
        Item             Version  Part number  Serial number     Description
        Chassis                                VM5D4C6B3599      VMX
        Jedec Code:   0x7fb0            EEPROM Version:    0x02
                                        S/N:               VM5D4C6B3599
        Assembly ID:  0x0567            Assembly Version:  00.00
        Date:         00-00-0000        Assembly Flags:    0x00
        ID: VMX                        
        Board Information Record:
        Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        I2C Hex Data:
        Address 0x00: 7f b0 02 ff 05 67 00 00 00 00 00 00 00 00 00 00
        Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x20: 56 4d 35 44 34 43 36 42 33 35 39 39 00 00 00 00
        Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Midplane        
        Routing Engine 0                                         RE-VMX
        Jedec Code:   0x0000            EEPROM Version:    0x00
        Assembly ID:  0x0bab            Assembly Version:  00.00
        Date:         00-00-0000        Assembly Flags:    0x00
        ID: RE-VMX                     
        Board Information Record:
        Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        I2C Hex Data:
        Address 0x00: 00 00 00 00 0b ab 00 00 00 00 00 00 00 00 00 00
        Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        cd0   27649 MB  VMware Virtual IDE Har 00000000000000000001 Hard Disk
        CB 0                                                     VMX SCB
        Jedec Code:   0x7fb0            EEPROM Version:    0x00
        Assembly ID:  0x0bb5            Assembly Version:  00.00
        Date:         00-00-0000        Assembly Flags:    0x00
        ID: VMX SCB                            
        Board Information Record:
        Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        I2C Hex Data:
        Address 0x00: 7f b0 00 00 0b b5 00 00 00 00 00 00 00 00 00 00
        Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        FPC 0                                                    Virtual FPC
        Jedec Code:   0x7fb0            EEPROM Version:    0x00
        Assembly ID:  0x0baa            Assembly Version:  00.00
        Date:         00-00-0000        Assembly Flags:    0x00
        ID: Virtual FPC                
        Board Information Record:
        Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        I2C Hex Data:
        Address 0x00: 7f b0 00 00 0b aa 00 00 00 00 00 00 00 00 00 00
        Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        CPU            Rev. 1.0 RIOT-LITE    BUILTIN          
        Jedec Code:   0x7fb0            EEPROM Version:    0x02
        P/N:          RIOT-LITE         S/N:               BUILTIN
        Assembly ID:  0xfa4e            Assembly Version:  01.00
        Date:         08-18-2013        Assembly Flags:    0x01
        Version:      Rev. 1.0
        Board Information Record:
        Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        I2C Hex Data:
        Address 0x00: 7f b0 02 00 fa 4e 01 00 52 65 76 2e 20 31 2e 30
        Address 0x10: 00 00 00 00 52 49 4f 54 2d 4c 49 54 45 00 00 00
        Address 0x20: 42 55 49 4c 54 49 4e 00 00 00 00 00 01 12 08 07
        Address 0x30: dd 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        MIC 0                                                  Virtual
        Jedec Code:   0x0000            EEPROM Version:    0x00
        Assembly ID:  0x0a7d            Assembly Version:  00.00
        Date:         00-00-0000        Assembly Flags:    0x00
        ID: Virtual                    
        Board Information Record:
        Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        I2C Hex Data:
        Address 0x00: 00 00 00 00 0a 7d 00 00 00 00 00 00 00 00 00 00
        Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        Address 0x70: 00 00 00 00 00 00 00 00 27 41 0f 08 83 80 f0 86
            PIC 0                 BUILTIN      BUILTIN           Virtual
    '''}

    golden_parsed_output = {
        "chassis-inventory": {
            "chassis": {
                "@junos:style": "inventory",
                "chassis-module": [
                    {
                        "name": "Midplane"
                    },
                    {
                        "chassis-re-disk-module": {
                            "description": "Hard Disk",
                            "disk-size": "27649",
                            "model": "VMware Virtual IDE Har",
                            "name": "cd0",
                            "serial-number": "00000000000000000001"
                        },
                        "description": "RE-VMX",
                        "i2c-information": {
                            "assembly-flags": "0x00",
                            "assembly-identifier": "0x0bab",
                            "assembly-version": "00.00",
                            "board-information-record": "Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                            "eeprom-version": "0x00",
                            "i2c-data": [
                                "Address 0x00: 00 00 00 00 0b ab 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                            ],
                            "i2c-identifier": "RE-VMX",
                            "i2c-version": None,
                            "jedec-code": "0x0000",
                            "manufacture-date": "00-00-0000",
                            "part-number": None,
                            "serial-number": None
                        },
                        "name": "Routing Engine 0"
                    },
                    {
                        "description": "VMX SCB",
                        "i2c-information": {
                            "assembly-flags": "0x00",
                            "assembly-identifier": "0x0bb5",
                            "assembly-version": "00.00",
                            "board-information-record": "Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                            "eeprom-version": "0x00",
                            "i2c-data": [
                                "Address 0x00: 7f b0 00 00 0b b5 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                            ],
                            "i2c-identifier": "VMX SCB",
                            "i2c-version": None,
                            "jedec-code": "0x7fb0",
                            "manufacture-date": "00-00-0000",
                            "part-number": None,
                            "serial-number": None
                        },
                        "name": "CB 0"
                    },
                    {
                        "chassis-sub-module": [
                            {
                                "chassis-sub-sub-module": {
                                    "description": "Virtual",
                                    "name": "PIC 0",
                                    "part-number": "BUILTIN",
                                    "serial-number": "BUILTIN"
                                },
                                "description": "Virtual",
                                "i2c-information": {
                                    "assembly-flags": "0x00",
                                    "assembly-identifier": "0x0a7d",
                                    "assembly-version": "00.00",
                                    "board-information-record": "Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                    "eeprom-version": "0x00",
                                    "i2c-data": [
                                        "Address 0x00: 00 00 00 00 0a 7d 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x70: 00 00 00 00 00 00 00 00 27 41 0f 08 83 80 f0 86"
                                    ],
                                    "i2c-identifier": "Virtual",
                                    "i2c-version": None,
                                    "jedec-code": "0x0000",
                                    "manufacture-date": "00-00-0000",
                                    "part-number": None,
                                    "serial-number": None
                                },
                                "name": "MIC 0"
                            },
                            {
                                "i2c-information": {
                                    "assembly-flags": "0x01",
                                    "assembly-identifier": "0xfa4e",
                                    "assembly-version": "01.00",
                                    "board-information-record": "Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                    "eeprom-version": "0x02",
                                    "i2c-data": [
                                        "Address 0x00: 7f b0 02 00 fa 4e 01 00 52 65 76 2e 20 31 2e 30",
                                        "Address 0x10: 00 00 00 00 52 49 4f 54 2d 4c 49 54 45 00 00 00",
                                        "Address 0x20: 42 55 49 4c 54 49 4e 00 00 00 00 00 01 12 08 07",
                                        "Address 0x30: dd 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                        "Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                                    ],
                                    "i2c-identifier": None,
                                    "i2c-version": "Rev. 1.0",
                                    "jedec-code": "0x7fb0",
                                    "manufacture-date": "08-18-2013",
                                    "part-number": None,
                                    "serial-number": "BUILTIN"
                                },
                                "name": "CPU",
                                "part-number": "RIOT-LITE",
                                "serial-number": "BUILTIN",
                                "version": "Rev. 1.0"
                            }
                        ],
                        "description": "Virtual FPC",
                        "i2c-information": {
                            "assembly-flags": "0x00",
                            "assembly-identifier": "0x0baa",
                            "assembly-version": "00.00",
                            "board-information-record": "Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                            "eeprom-version": "0x00",
                            "i2c-data": [
                                "Address 0x00: 7f b0 00 00 0b aa 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                                "Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                            ],
                            "i2c-identifier": "Virtual FPC",
                            "i2c-version": None,
                            "jedec-code": "0x7fb0",
                            "manufacture-date": "00-00-0000",
                            "part-number": None,
                            "serial-number": None
                        },
                        "name": "FPC 0"
                    }
            ],
            "description": "VMX",
            "i2c-information": {
                "assembly-flags": "0x00",
                "assembly-identifier": "0x0567",
                "assembly-version": "00.00",
                "board-information-record": "Address 0x00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                "eeprom-version": "0x02",
                "i2c-data": [
                    "Address 0x00: 7f b0 02 ff 05 67 00 00 00 00 00 00 00 00 00 00",
                    "Address 0x10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                    "Address 0x20: 56 4d 35 44 34 43 36 42 33 35 39 39 00 00 00 00",
                    "Address 0x30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                    "Address 0x40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                    "Address 0x50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                    "Address 0x60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                    "Address 0x70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
                ],
                "i2c-identifier": "VMX",
                "i2c-version": None,
                "jedec-code": "0x7fb0",
                "manufacture-date": "00-00-0000",
                "part-number": None,
                "serial-number": "VM5D4C6B3599"
            },
            "name": "Chassis",
            "serial-number": "VM5D4C6B3599"
        }
    }
        
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisHardwareExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisHardwareExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
   


class TestShowChassisFpc(unittest.TestCase):
    """ Unit tests for:
            * show chassis fpc
    """
    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': ''' show chassis fpc
                     Temp  CPU Utilization (%)   CPU Utilization (%)  Memory    Utilization (%)
        Slot State            (C)  Total  Interrupt      1min   5min   15min  DRAM (MB) Heap     Buffer
        0  Online           Testing   3         0        2      2      2    511        31          0
        1  Empty           
        2  Empty           
        3  Empty           
        4  Empty           
        5  Empty           
        6  Empty           
        7  Empty           
        8  Empty           
        9  Empty           
        10  Empty           
        11  Empty
    '''}

    golden_parsed_output = {
        "fpc-information": {
            "fpc": [
                {
                    "cpu-15min-avg": "2",
                    "cpu-1min-avg": "2",
                    "cpu-5min-avg": "2",
                    "cpu-interrupt": "0",
                    "cpu-total": "3",
                    "memory-buffer-utilization": "0",
                    "memory-dram-size": "511",
                    "memory-heap-utilization": "31",
                    "slot": "0",
                    "state": "Online",
                    "temperature": {
                        "#text": "Testing"
                    }
                },
                {
                    "slot": "1",
                    "state": "Empty"
                },
                {
                    "slot": "2",
                    "state": "Empty"
                },
                {
                    "slot": "3",
                    "state": "Empty"
                },
                {
                    "slot": "4",
                    "state": "Empty"
                },
                {
                    "slot": "5",
                    "state": "Empty"
                },
                {
                    "slot": "6",
                    "state": "Empty"
                },
                {
                    "slot": "7",
                    "state": "Empty"
                },
                {
                    "slot": "8",
                    "state": "Empty"
                },
                {
                    "slot": "9",
                    "state": "Empty"
                },
                {
                    "slot": "10",
                    "state": "Empty"
                },
                {
                    "slot": "11",
                    "state": "Empty"
                }
            ]
        }
    }
    
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisFpc(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisFpc(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowChassisRoutingEngine(unittest.TestCase):
    """ Unit tests for:
            * show chassis routing-engine
    """
    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': 
    ''' show chassis routing-engine
        Routing Engine status:
        Slot 0:
            Current state                  Master
            Election priority              Master (default)
            DRAM                      2002 MB (2048 MB installed)
            Memory utilization          19 percent
            5 sec CPU utilization:
            User                       1 percent
            Background                 0 percent
            Kernel                     1 percent
            Interrupt                  0 percent
            Idle                      98 percent
            1 min CPU utilization:
            User                       1 percent
            Background                 0 percent
            Kernel                     1 percent
            Interrupt                  0 percent
            Idle                      98 percent
            5 min CPU utilization:
            User                       1 percent
            Background                 0 percent
            Kernel                     1 percent
            Interrupt                  0 percent
            Idle                      98 percent
            15 min CPU utilization:
            User                       1 percent
            Background                 0 percent
            Kernel                     1 percent
            Interrupt                  0 percent
            Idle                      98 percent
            Model                          RE-VMX
            Start time                     2019-08-29 09:02:22 UTC
            Uptime                         208 days, 23 hours, 14 minutes, 9 seconds
            Last reboot reason             Router rebooted after a normal shutdown.
            Load averages:                 1 minute   5 minute  15 minute
                                            0.72       0.46       0.40
    '''}

    golden_parsed_output = {
        "route-engine-information": {
            "route-engine": [{
                "cpu-background-15min": "0",
                "cpu-background-1min": "0",
                "cpu-background-5min": "0",
                "cpu-background-5sec": "0",
                "cpu-idle-15min": "98",
                "cpu-idle-1min": "98",
                "cpu-idle-5min": "98",
                "cpu-idle-5sec": "98",
                "cpu-interrupt-15min": "0",
                "cpu-interrupt-1min": "0",
                "cpu-interrupt-5min": "0",
                "cpu-interrupt-5sec": "0",
                "cpu-system-15min": "1",
                "cpu-system-1min": "1",
                "cpu-system-5min": "1",
                "cpu-system-5sec": "1",
                "cpu-user-15min": "1",
                "cpu-user-1min": "1",
                "cpu-user-5min": "1",
                "cpu-user-5sec": "1",
                "last-reboot-reason": "Router rebooted after a normal shutdown.",
                "load-average-fifteen": "0.40",
                "load-average-five": "0.46",
                "load-average-one": "0.72",
                "mastership-priority": "Master (default)",
                "mastership-state": "Master",
                "memory-buffer-utilization": "19",
                "memory-dram-size": "2002 MB",
                "memory-installed-size": "(2048 MB installed)",
                "model": "RE-VMX",
                "slot": "0",
                "start-time": {
                    "#text": "2019-08-29 09:02:22 UTC"
                },
                "up-time": {
                    "#text": "208 days, 23 hours, 14 minutes, 9 seconds"
                }
                }
            ]
        }
        
    }

    golden_output2 = {'execute.return_value': 
    ''' show chassis routing-engine
        Routing Engine status:
        Slot 0:
            Current state                  Master
            Election priority              Master (default)
            Temperature                 42 degrees C / 107 degrees F
            CPU temperature             38 degrees C / 100 degrees F
            DRAM                      32733 MB (32768 MB installed)
            Memory utilization          19 percent
            CPU utilization:
            User                       3 percent
            Background                 0 percent
            Kernel                    11 percent
            Interrupt                  4 percent
            Idle                      82 percent
            Model                          RE-S-1800x4
            Serial ID                      9009237267
            Start time                     2020-07-16 13:36:25 EST
            Uptime                         5 days, 3 hours, 24 minutes, 13 seconds
            Last reboot reason             Router rebooted after a normal shutdown.
            Load averages:                 1 minute   5 minute  15 minute
                                            0.22       0.26       0.23
        Routing Engine status:
        Slot 1:
            Current state                  Backup
            Election priority              Backup (default)
            Temperature                 39 degrees C / 102 degrees F
            CPU temperature             34 degrees C / 93 degrees F
            DRAM                      32733 MB (32768 MB installed)
            Memory utilization           8 percent
            CPU utilization:
            User                       0 percent
            Background                 0 percent
            Kernel                     0 percent
            Interrupt                  0 percent
            Idle                      99 percent
            Model                          RE-S-1800x4
            Serial ID                      9009237474
            Start time                     2020-07-16 13:36:22 EST
            Uptime                         5 days, 3 hours, 23 minutes, 59 seconds
            Last reboot reason             Router rebooted after a normal shutdown.
            Load averages:                 1 minute   5 minute  15 minute
                                            0.00       0.00       0.00
                                            
        {master}
    '''}

    golden_parsed_output2 = {
        "route-engine-information": {
            "route-engine": [
                {
                    "cpu-background": "0",
                    "cpu-idle": "82",
                    "cpu-interrupt": "4",
                    "cpu-system": "11",
                    "cpu-user": "3",
                    "last-reboot-reason": "Router rebooted after a normal shutdown.",
                    "load-average-fifteen": "0.23",
                    "load-average-five": "0.26",
                    "load-average-one": "0.22",
                    "mastership-priority": "Master (default)",
                    "mastership-state": "Master",
                    "memory-buffer-utilization": "19",
                    "memory-dram-size": "32733 MB",
                    "memory-installed-size": "(32768 MB installed)",
                    "model": "RE-S-1800x4",
                    "serial-number": "9009237267",
                    "slot": "0",
                    "start-time": {
                        "#text": "2020-07-16 13:36:25 EST"
                    },
                    "temperature": {
                        "#text": "42 degrees C / 107 degrees F"
                    },
                    "up-time": {
                        "#text": "5 days, 3 hours, 24 minutes, 13 seconds"
                    }
                },
                {
                    "cpu-background": "0",
                    "cpu-idle": "99",
                    "cpu-interrupt": "0",
                    "cpu-system": "0",
                    "cpu-user": "0",
                    "last-reboot-reason": "Router rebooted after a normal shutdown.",
                    "load-average-fifteen": "0.00",
                    "load-average-five": "0.00",
                    "load-average-one": "0.00",
                    "mastership-priority": "Backup (default)",
                    "mastership-state": "Backup",
                    "memory-buffer-utilization": "8",
                    "memory-dram-size": "32733 MB",
                    "memory-installed-size": "(32768 MB installed)",
                    "model": "RE-S-1800x4",
                    "serial-number": "9009237474",
                    "slot": "1",
                    "start-time": {
                        "#text": "2020-07-16 13:36:22 EST"
                    },
                    "temperature": {
                        "#text": "39 degrees C / 102 degrees F"
                    },
                    "up-time": {
                        "#text": "5 days, 3 hours, 23 minutes, 59 seconds"
                    }
                }
            ],
            "re-state": "{master}"
        }
        
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisRoutingEngine(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisRoutingEngine(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowChassisRoutingEngine(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

class TestShowChassisRoutingEngineNoForwarding(unittest.TestCase):
    """ Unit tests for:
            * show chassis routing-engine no-forwarding
    """
    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': 
    ''' show chassis routing-engine no-forwarding
        Routing Engine status:
        Slot 0:
            Current state                  Master
            Election priority              Master (default)
            DRAM                      2002 MB (2048 MB installed)
            Memory utilization          19 percent
            5 sec CPU utilization:
            User                       0 percent
            Background                 0 percent
            Kernel                     1 percent
            Interrupt                  0 percent
            Idle                      99 percent
            1 min CPU utilization:
            User                       1 percent
            Background                 0 percent
            Kernel                     1 percent
            Interrupt                  0 percent
            Idle                      98 percent
            5 min CPU utilization:
            User                       1 percent
            Background                 0 percent
            Kernel                     1 percent
            Interrupt                  0 percent
            Idle                      98 percent
            15 min CPU utilization:
            User                       1 percent
            Background                 0 percent
            Kernel                     1 percent
            Interrupt                  0 percent
            Idle                      98 percent
            Model                          RE-VMX
            Start time                     2019-08-29 09:02:22 UTC
            Uptime                         208 days, 23 hours, 15 minutes, 9 seconds
            Last reboot reason             Router rebooted after a normal shutdown.
            Load averages:                 1 minute   5 minute  15 minute
                                            0.48       0.44       0.40
    '''}

    golden_parsed_output = {
        "route-engine-information": {
            "route-engine": [{
                "cpu-background-15min": "0",
                "cpu-background-1min": "0",
                "cpu-background-5min": "0",
                "cpu-background-5sec": "0",
                "cpu-idle-15min": "98",
                "cpu-idle-1min": "98",
                "cpu-idle-5min": "98",
                "cpu-idle-5sec": "99",
                "cpu-interrupt-15min": "0",
                "cpu-interrupt-1min": "0",
                "cpu-interrupt-5min": "0",
                "cpu-interrupt-5sec": "0",
                "cpu-system-15min": "1",
                "cpu-system-1min": "1",
                "cpu-system-5min": "1",
                "cpu-system-5sec": "1",
                "cpu-user-15min": "1",
                "cpu-user-1min": "1",
                "cpu-user-5min": "1",
                "cpu-user-5sec": "0",
                "last-reboot-reason": "Router rebooted after a normal shutdown.",
                "load-average-fifteen": "0.40",
                "load-average-five": "0.44",
                "load-average-one": "0.48",
                "mastership-priority": "Master (default)",
                "mastership-state": "Master",
                "memory-buffer-utilization": "19",
                "memory-dram-size": "2002 MB",
                "memory-installed-size": "(2048 MB installed)",
                "model": "RE-VMX",
                "slot": "0",
                "start-time": {
                    "#text": "2019-08-29 09:02:22 UTC"
                },
                "up-time": {
                    "#text": "208 days, 23 hours, 15 minutes, 9 seconds"
                }
            }
            ]
            }
        
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisRoutingEngineNoForwarding(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisRoutingEngineNoForwarding(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowChassisEnvironment(unittest.TestCase):
    """ Unit tests for:
            * show chassis environment
    """
    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
      Class Item                           Status     Measurement
      Temp  PSM 0                          OK         25 degrees C / 77 degrees F
            PSM 1                          OK         24 degrees C / 75 degrees F
            PSM 2                          OK         24 degrees C / 75 degrees F
            PSM 3                          OK         23 degrees C / 73 degrees F
            PSM 4                          Check
            PSM 5                          Check
            PSM 6                          Check
            PSM 7                          Check
            PSM 8                          Check
            PSM 9                          OK         29 degrees C / 84 degrees F
            PSM 10                         OK         30 degrees C / 86 degrees F
            PSM 11                         OK         30 degrees C / 86 degrees F
            PSM 12                         Check
            PSM 13                         Check
            PSM 14                         Check
            PSM 15                         Check
            PSM 16                         Check
            PSM 17                         Check
            PDM 0                          OK
            PDM 1                          OK
            PDM 2                          OK
            PDM 3                          OK
            CB 0 IntakeA-Zone0             OK         39 degrees C / 102 degrees F
            CB 0 IntakeB-Zone1             OK         36 degrees C / 96 degrees F
            CB 0 IntakeC-Zone0             OK         51 degrees C / 123 degrees F
            CB 0 ExhaustA-Zone0            OK         40 degrees C / 104 degrees F
            CB 0 ExhaustB-Zone1            OK         35 degrees C / 95 degrees F
            CB 0 TCBC-Zone0                OK         45 degrees C / 113 degrees F
            CB 1 IntakeA-Zone0             OK         29 degrees C / 84 degrees F
            CB 1 IntakeB-Zone1             OK         32 degrees C / 89 degrees F
            CB 1 IntakeC-Zone0             OK         33 degrees C / 91 degrees F
            CB 1 ExhaustA-Zone0            OK         32 degrees C / 89 degrees F
            CB 1 ExhaustB-Zone1            OK         32 degrees C / 89 degrees F
            CB 1 TCBC-Zone0                OK         39 degrees C / 102 degrees F
            SPMB 0 Intake                  OK         35 degrees C / 95 degrees F
            SPMB 1 Intake                  OK         33 degrees C / 91 degrees F
            Routing Engine 0               OK         43 degrees C / 109 degrees F
            Routing Engine 0 CPU           OK         39 degrees C / 102 degrees F
            Routing Engine 1               OK         40 degrees C / 104 degrees F
            Routing Engine 1 CPU           OK         35 degrees C / 95 degrees F
            SFB 0 Intake-Zone0             OK         37 degrees C / 98 degrees F
            SFB 0 Exhaust-Zone1            OK         45 degrees C / 113 degrees F
            SFB 0 IntakeA-Zone0            OK         32 degrees C / 89 degrees F
            SFB 0 IntakeB-Zone1            OK         34 degrees C / 93 degrees F
            SFB 0 Exhaust-Zone0            OK         36 degrees C / 96 degrees F
            SFB 0 SFB-XF2-Zone1            OK         63 degrees C / 145 degrees F
            SFB 0 SFB-XF1-Zone0            OK         55 degrees C / 131 degrees F
            SFB 0 SFB-XF0-Zone0            OK         52 degrees C / 125 degrees F
            SFB 1 Intake-Zone0             OK         35 degrees C / 95 degrees F
            SFB 1 Exhaust-Zone1            OK         42 degrees C / 107 degrees F
            SFB 1 IntakeA-Zone0            OK         29 degrees C / 84 degrees F
            SFB 1 IntakeB-Zone1            OK         32 degrees C / 89 degrees F
            SFB 1 Exhaust-Zone0            OK         34 degrees C / 93 degrees F
            SFB 1 SFB-XF2-Zone1            OK         63 degrees C / 145 degrees F
            SFB 1 SFB-XF1-Zone0            OK         53 degrees C / 127 degrees F
            SFB 1 SFB-XF0-Zone0            OK         50 degrees C / 122 degrees F
            SFB 2 Intake-Zone0             OK         35 degrees C / 95 degrees F
            SFB 2 Exhaust-Zone1            OK         42 degrees C / 107 degrees F
            SFB 2 IntakeA-Zone0            OK         30 degrees C / 86 degrees F
            SFB 2 IntakeB-Zone1            OK         32 degrees C / 89 degrees F
            SFB 2 Exhaust-Zone0            OK         34 degrees C / 93 degrees F
            SFB 2 SFB-XF2-Zone1            OK         60 degrees C / 140 degrees F
            SFB 2 SFB-XF1-Zone0            OK         53 degrees C / 127 degrees F
            SFB 2 SFB-XF0-Zone0            OK         56 degrees C / 132 degrees F
            SFB 3 Intake-Zone0             OK         35 degrees C / 95 degrees F
            SFB 3 Exhaust-Zone1            OK         42 degrees C / 107 degrees F
            SFB 3 IntakeA-Zone0            OK         29 degrees C / 84 degrees F
            SFB 3 IntakeB-Zone1            OK         32 degrees C / 89 degrees F
            SFB 3 Exhaust-Zone0            OK         34 degrees C / 93 degrees F
            SFB 3 SFB-XF2-Zone1            OK         61 degrees C / 141 degrees F
            SFB 3 SFB-XF1-Zone0            OK         53 degrees C / 127 degrees F
            SFB 3 SFB-XF0-Zone0            OK         50 degrees C / 122 degrees F
            SFB 4 Intake-Zone0             OK         34 degrees C / 93 degrees F
            SFB 4 Exhaust-Zone1            OK         42 degrees C / 107 degrees F
            SFB 4 IntakeA-Zone0            OK         29 degrees C / 84 degrees F
            SFB 4 IntakeB-Zone1            OK         32 degrees C / 89 degrees F
            SFB 4 Exhaust-Zone0            OK         34 degrees C / 93 degrees F
            SFB 4 SFB-XF2-Zone1            OK         64 degrees C / 147 degrees F
            SFB 4 SFB-XF1-Zone0            OK         53 degrees C / 127 degrees F
            SFB 4 SFB-XF0-Zone0            OK         50 degrees C / 122 degrees F
            SFB 5 Intake-Zone0             OK         34 degrees C / 93 degrees F
            SFB 5 Exhaust-Zone1            OK         41 degrees C / 105 degrees F
            SFB 5 IntakeA-Zone0            OK         29 degrees C / 84 degrees F
            SFB 5 IntakeB-Zone1            OK         31 degrees C / 87 degrees F
            SFB 5 Exhaust-Zone0            OK         34 degrees C / 93 degrees F
            SFB 5 SFB-XF2-Zone1            OK         63 degrees C / 145 degrees F
            SFB 5 SFB-XF1-Zone0            OK         53 degrees C / 127 degrees F
            SFB 5 SFB-XF0-Zone0            OK         50 degrees C / 122 degrees F
            SFB 6 Intake-Zone0             OK         34 degrees C / 93 degrees F
            SFB 6 Exhaust-Zone1            OK         42 degrees C / 107 degrees F
            SFB 6 IntakeA-Zone0            OK         29 degrees C / 84 degrees F
            SFB 6 IntakeB-Zone1            OK         32 degrees C / 89 degrees F
            SFB 6 Exhaust-Zone0            OK         34 degrees C / 93 degrees F
            SFB 6 SFB-XF2-Zone1            OK         62 degrees C / 143 degrees F
            SFB 6 SFB-XF1-Zone0            OK         53 degrees C / 127 degrees F
            SFB 6 SFB-XF0-Zone0            OK         49 degrees C / 120 degrees F
            SFB 7 Intake-Zone0             OK         35 degrees C / 95 degrees F
            SFB 7 Exhaust-Zone1            OK         43 degrees C / 109 degrees F
            SFB 7 IntakeA-Zone0            OK         31 degrees C / 87 degrees F
            SFB 7 IntakeB-Zone1            OK         32 degrees C / 89 degrees F
            SFB 7 Exhaust-Zone0            OK         35 degrees C / 95 degrees F
            SFB 7 SFB-XF2-Zone1            OK         65 degrees C / 149 degrees F
            SFB 7 SFB-XF1-Zone0            OK         56 degrees C / 132 degrees F
            SFB 7 SFB-XF0-Zone0            OK         52 degrees C / 125 degrees F
            FPC 0 Intake                   OK         29 degrees C / 84 degrees F
            FPC 0 Exhaust A                OK         53 degrees C / 127 degrees F
            FPC 0 Exhaust B                OK         54 degrees C / 129 degrees F
            FPC 0 XL 0 TSen                OK         50 degrees C / 122 degrees F
            FPC 0 XL 0 Chip                OK         63 degrees C / 145 degrees F
            FPC 0 XL 0 XR2 0 TSen          OK         50 degrees C / 122 degrees F
            FPC 0 XL 0 XR2 0 Chip          OK         80 degrees C / 176 degrees F
            FPC 0 XL 0 XR2 1 TSen          OK         50 degrees C / 122 degrees F
            FPC 0 XL 0 XR2 1 Chip          OK         80 degrees C / 176 degrees F
            FPC 0 XL 1 TSen                OK         36 degrees C / 96 degrees F
            FPC 0 XL 1 Chip                OK         44 degrees C / 111 degrees F
            FPC 0 XL 1 XR2 0 TSen          OK         36 degrees C / 96 degrees F
            FPC 0 XL 1 XR2 0 Chip          OK         60 degrees C / 140 degrees F
            FPC 0 XL 1 XR2 1 TSen          OK         36 degrees C / 96 degrees F
            FPC 0 XL 1 XR2 1 Chip          OK         59 degrees C / 138 degrees F
            FPC 0 XM 0 TSen                OK         52 degrees C / 125 degrees F
            FPC 0 XM 0 Chip                OK         62 degrees C / 143 degrees F
            FPC 0 XM 1 TSen                OK         52 degrees C / 125 degrees F
            FPC 0 XM 1 Chip                OK         57 degrees C / 134 degrees F
            FPC 0 XM 2 TSen                OK         52 degrees C / 125 degrees F
            FPC 0 XM 2 Chip                OK         51 degrees C / 123 degrees F
            FPC 0 XM 3 TSen                OK         52 degrees C / 125 degrees F
            FPC 0 XM 3 Chip                OK         45 degrees C / 113 degrees F
            FPC 0 PCIe Switch TSen         OK         52 degrees C / 125 degrees F
            FPC 0 PCIe Switch Chip         OK         30 degrees C / 86 degrees F
            FPC 9 Intake                   OK         31 degrees C / 87 degrees F
            FPC 9 Exhaust A                OK         48 degrees C / 118 degrees F
            FPC 9 Exhaust B                OK         41 degrees C / 105 degrees F
            FPC 9 LU 0 TCAM TSen           OK         46 degrees C / 114 degrees F
            FPC 9 LU 0 TCAM Chip           OK         55 degrees C / 131 degrees F
            FPC 9 LU 0 TSen                OK         46 degrees C / 114 degrees F
            FPC 9 LU 0 Chip                OK         55 degrees C / 131 degrees F
            FPC 9 MQ 0 TSen                OK         46 degrees C / 114 degrees F
            FPC 9 MQ 0 Chip                OK         57 degrees C / 134 degrees F
            FPC 9 LU 1 TCAM TSen           OK         41 degrees C / 105 degrees F
            FPC 9 LU 1 TCAM Chip           OK         46 degrees C / 114 degrees F
            FPC 9 LU 1 TSen                OK         41 degrees C / 105 degrees F
            FPC 9 LU 1 Chip                OK         47 degrees C / 116 degrees F
            FPC 9 MQ 1 TSen                OK         41 degrees C / 105 degrees F
            FPC 9 MQ 1 Chip                OK         47 degrees C / 116 degrees F
            ADC 9 Intake                   OK         32 degrees C / 89 degrees F
            ADC 9 Exhaust                  OK         42 degrees C / 107 degrees F
            ADC 9 ADC-XF1                  OK         49 degrees C / 120 degrees F
            ADC 9 ADC-XF0                  OK         59 degrees C / 138 degrees F
      Fans  Fan Tray 0 Fan 1               OK         2760 RPM
            Fan Tray 0 Fan 2               OK         2520 RPM
            Fan Tray 0 Fan 3               OK         2520 RPM
            Fan Tray 0 Fan 4               OK         2640 RPM
            Fan Tray 0 Fan 5               OK         2640 RPM
            Fan Tray 0 Fan 6               OK         2640 RPM
            Fan Tray 1 Fan 1               OK         2520 RPM
            Fan Tray 1 Fan 2               OK         2640 RPM
            Fan Tray 1 Fan 3               OK         2520 RPM
            Fan Tray 1 Fan 4               OK         2640 RPM
            Fan Tray 1 Fan 5               OK         2520 RPM
            Fan Tray 1 Fan 6               OK         2640 RPM
            Fan Tray 2 Fan 1               OK         2640 RPM
            Fan Tray 2 Fan 2               OK         2640 RPM
            Fan Tray 2 Fan 3               OK         2520 RPM
            Fan Tray 2 Fan 4               OK         2640 RPM
            Fan Tray 2 Fan 5               OK         2520 RPM
            Fan Tray 2 Fan 6               OK         2640 RPM
            Fan Tray 3 Fan 1               OK         2520 RPM
            Fan Tray 3 Fan 2               OK         2400 RPM
            Fan Tray 3 Fan 3               OK         2520 RPM
            Fan Tray 3 Fan 4               OK         2520 RPM
            Fan Tray 3 Fan 5               OK         2640 RPM
            Fan Tray 3 Fan 6               OK         2520 RPM    
    '''}

    golden_parsed_output = {'environment-information': {'environment-item': [{'class': 'Temp',
                                                   'name': 'PSM 0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '25 '
                                                                            'degrees '      
                                                                            'C '
                                                                            '/ '
                                                                            '77 '
                                                                            'degrees '      
                                                                            'F',
                                                                   '@junos:celsius': '25'}},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '24 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '75 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '24'}},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 2',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '24 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '75 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '24'}},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 3',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '23 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '73 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '23'}},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 4',
                                                   'status': 'Check'},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 5',
                                                   'status': 'Check'},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 6',
                                                   'status': 'Check'},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 7',
                                                   'status': 'Check'},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 8',
                                                   'status': 'Check'},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 9',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '29 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '84 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '29'}},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 10',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '30 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '86 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '30'}},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 11',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '30 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '86 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '30'}},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 12',
                                                   'status': 'Check'},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 13',
                                                   'status': 'Check'},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 14',
                                                   'status': 'Check'},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 15',
                                                   'status': 'Check'},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 16',
                                                   'status': 'Check'},
                                                  {'class': 'Temp',
                                                   'name': 'PSM 17',
                                                   'status': 'Check'},
                                                  {'class': 'Temp',
                                                   'name': 'PDM 0',
                                                   'status': 'OK'},
                                                  {'class': 'Temp',
                                                   'name': 'PDM 1',
                                                   'status': 'OK'},
                                                  {'class': 'Temp',
                                                   'name': 'PDM 2',
                                                   'status': 'OK'},
                                                  {'class': 'Temp',
                                                   'name': 'PDM 3',
                                                   'status': 'OK'},
                                                  {'class': 'Temp',
                                                   'name': 'CB 0 IntakeA-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '39 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '102 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '39'}},
                                                  {'class': 'Temp',
                                                   'name': 'CB 0 IntakeB-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '36 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '96 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '36'}},
                                                  {'class': 'Temp',
                                                   'name': 'CB 0 IntakeC-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '51 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '123 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '51'}},
                                                  {'class': 'Temp',
                                                   'name': 'CB 0 '
                                                           'ExhaustA-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '40 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '104 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '40'}},
                                                  {'class': 'Temp',
                                                   'name': 'CB 0 '
                                                           'ExhaustB-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '35 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '95 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '35'}},
                                                  {'class': 'Temp',
                                                   'name': 'CB 0 TCBC-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '45 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '113 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '45'}},
                                                  {'class': 'Temp',
                                                   'name': 'CB 1 IntakeA-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '29 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '84 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '29'}},
                                                  {'class': 'Temp',
                                                   'name': 'CB 1 IntakeB-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '32 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '89 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '32'}},
                                                  {'class': 'Temp',
                                                   'name': 'CB 1 IntakeC-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '33 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '91 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '33'}},
                                                  {'class': 'Temp',
                                                   'name': 'CB 1 '
                                                           'ExhaustA-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '32 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '89 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '32'}},
                                                  {'class': 'Temp',
                                                   'name': 'CB 1 '
                                                           'ExhaustB-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '32 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '89 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '32'}},
                                                  {'class': 'Temp',
                                                   'name': 'CB 1 TCBC-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '39 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '102 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '39'}},
                                                  {'class': 'Temp',
                                                   'name': 'SPMB 0 Intake',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '35 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '95 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '35'}},
                                                  {'class': 'Temp',
                                                   'name': 'SPMB 1 Intake',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '33 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '91 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '33'}},
                                                  {'class': 'Temp',
                                                   'name': 'Routing Engine 0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '43 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '109 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '43'}},
                                                  {'class': 'Temp',
                                                   'name': 'Routing Engine 0 '
                                                           'CPU',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '39 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '102 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '39'}},
                                                  {'class': 'Temp',
                                                   'name': 'Routing Engine 1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '40 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '104 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '40'}},
                                                  {'class': 'Temp',
                                                   'name': 'Routing Engine 1 '
                                                           'CPU',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '35 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '95 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '35'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 0 Intake-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '37 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '98 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '37'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 0 '
                                                           'Exhaust-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '45 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '113 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '45'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 0 '
                                                           'IntakeA-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '32 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '89 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '32'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 0 '
                                                           'IntakeB-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '34 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '93 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '34'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 0 '
                                                           'Exhaust-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '36 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '96 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '36'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 0 '
                                                           'SFB-XF2-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '63 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '145 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '63'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 0 '
                                                           'SFB-XF1-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '55 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '131 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '55'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 0 '
                                                           'SFB-XF0-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '52 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '125 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '52'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 1 Intake-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '35 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '95 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '35'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 1 '
                                                           'Exhaust-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '42 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '107 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '42'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 1 '
                                                           'IntakeA-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '29 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '84 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '29'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 1 '
                                                           'IntakeB-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '32 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '89 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '32'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 1 '
                                                           'Exhaust-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '34 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '93 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '34'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 1 '
                                                           'SFB-XF2-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '63 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '145 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '63'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 1 '
                                                           'SFB-XF1-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '53 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '127 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '53'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 1 '
                                                           'SFB-XF0-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '50 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '122 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '50'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 2 Intake-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '35 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '95 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '35'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 2 '
                                                           'Exhaust-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '42 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '107 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '42'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 2 '
                                                           'IntakeA-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '30 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '86 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '30'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 2 '
                                                           'IntakeB-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '32 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '89 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '32'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 2 '
                                                           'Exhaust-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '34 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '93 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '34'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 2 '
                                                           'SFB-XF2-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '60 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '140 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '60'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 2 '
                                                           'SFB-XF1-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '53 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '127 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '53'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 2 '
                                                           'SFB-XF0-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '56 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '132 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '56'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 3 Intake-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '35 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '95 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '35'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 3 '
                                                           'Exhaust-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '42 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '107 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '42'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 3 '
                                                           'IntakeA-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '29 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '84 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '29'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 3 '
                                                           'IntakeB-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '32 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '89 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '32'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 3 '
                                                           'Exhaust-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '34 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '93 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '34'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 3 '
                                                           'SFB-XF2-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '61 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '141 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '61'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 3 '
                                                           'SFB-XF1-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '53 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '127 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '53'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 3 '
                                                           'SFB-XF0-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '50 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '122 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '50'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 4 Intake-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '34 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '93 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '34'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 4 '
                                                           'Exhaust-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '42 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '107 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '42'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 4 '
                                                           'IntakeA-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '29 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '84 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '29'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 4 '
                                                           'IntakeB-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '32 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '89 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '32'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 4 '
                                                           'Exhaust-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '34 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '93 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '34'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 4 '
                                                           'SFB-XF2-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '64 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '147 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '64'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 4 '
                                                           'SFB-XF1-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '53 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '127 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '53'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 4 '
                                                           'SFB-XF0-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '50 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '122 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '50'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 5 Intake-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '34 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '93 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '34'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 5 '
                                                           'Exhaust-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '41 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '105 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '41'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 5 '
                                                           'IntakeA-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '29 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '84 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '29'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 5 '
                                                           'IntakeB-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '31 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '87 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '31'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 5 '
                                                           'Exhaust-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '34 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '93 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '34'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 5 '
                                                           'SFB-XF2-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '63 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '145 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '63'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 5 '
                                                           'SFB-XF1-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '53 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '127 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '53'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 5 '
                                                           'SFB-XF0-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '50 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '122 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '50'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 6 Intake-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '34 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '93 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '34'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 6 '
                                                           'Exhaust-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '42 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '107 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '42'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 6 '
                                                           'IntakeA-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '29 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '84 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '29'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 6 '
                                                           'IntakeB-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '32 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '89 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '32'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 6 '
                                                           'Exhaust-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '34 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '93 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '34'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 6 '
                                                           'SFB-XF2-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '62 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '143 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '62'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 6 '
                                                           'SFB-XF1-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '53 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '127 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '53'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 6 '
                                                           'SFB-XF0-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '49 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '120 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '49'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 7 Intake-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '35 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '95 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '35'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 7 '
                                                           'Exhaust-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '43 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '109 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '43'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 7 '
                                                           'IntakeA-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '31 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '87 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '31'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 7 '
                                                           'IntakeB-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '32 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '89 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '32'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 7 '
                                                           'Exhaust-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '35 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '95 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '35'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 7 '
                                                           'SFB-XF2-Zone1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '65 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '149 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '65'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 7 '
                                                           'SFB-XF1-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '56 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '132 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '56'}},
                                                  {'class': 'Temp',
                                                   'name': 'SFB 7 '
                                                           'SFB-XF0-Zone0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '52 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '125 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '52'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 Intake',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '29 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '84 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '29'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 Exhaust A',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '53 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '127 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '53'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 Exhaust B',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '54 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '129 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '54'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XL 0 TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '50 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '122 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '50'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XL 0 Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '63 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '145 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '63'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XL 0 XR2 0 '
                                                           'TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '50 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '122 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '50'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XL 0 XR2 0 '
                                                           'Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '80 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '176 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '80'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XL 0 XR2 1 '
                                                           'TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '50 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '122 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '50'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XL 0 XR2 1 '
                                                           'Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '80 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '176 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '80'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XL 1 TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '36 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '96 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '36'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XL 1 Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '44 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '111 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '44'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XL 1 XR2 0 '
                                                           'TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '36 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '96 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '36'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XL 1 XR2 0 '
                                                           'Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '60 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '140 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '60'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XL 1 XR2 1 '
                                                           'TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '36 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '96 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '36'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XL 1 XR2 1 '
                                                           'Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '59 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '138 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '59'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XM 0 TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '52 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '125 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '52'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XM 0 Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '62 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '143 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '62'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XM 1 TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '52 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '125 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '52'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XM 1 Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '57 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '134 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '57'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XM 2 TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '52 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '125 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '52'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XM 2 Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '51 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '123 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '51'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XM 3 TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '52 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '125 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '52'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 XM 3 Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '45 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '113 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '45'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 PCIe Switch '
                                                           'TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '52 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '125 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '52'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 0 PCIe Switch '
                                                           'Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '30 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '86 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '30'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 Intake',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '31 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '87 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '31'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 Exhaust A',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '48 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '118 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '48'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 Exhaust B',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '41 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '105 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '41'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 LU 0 TCAM '
                                                           'TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '46 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '114 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '46'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 LU 0 TCAM '
                                                           'Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '55 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '131 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '55'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 LU 0 TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '46 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '114 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '46'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 LU 0 Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '55 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '131 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '55'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 MQ 0 TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '46 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '114 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '46'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 MQ 0 Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '57 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '134 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '57'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 LU 1 TCAM '
                                                           'TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '41 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '105 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '41'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 LU 1 TCAM '
                                                           'Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '46 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '114 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '46'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 LU 1 TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '41 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '105 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '41'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 LU 1 Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '47 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '116 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '47'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 MQ 1 TSen',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '41 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '105 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '41'}},
                                                  {'class': 'Temp',
                                                   'name': 'FPC 9 MQ 1 Chip',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '47 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '116 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '47'}},
                                                  {'class': 'Temp',
                                                   'name': 'ADC 9 Intake',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '32 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '89 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '32'}},
                                                  {'class': 'Temp',
                                                   'name': 'ADC 9 Exhaust',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '42 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '107 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '42'}},
                                                  {'class': 'Temp',
                                                   'name': 'ADC 9 ADC-XF1',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '49 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '120 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '49'}},
                                                  {'class': 'Temp',
                                                   'name': 'ADC 9 ADC-XF0',
                                                   'status': 'OK',
                                                   'temperature': {'#text': '59 '
                                                                            'degrees '
                                                                            'C '
                                                                            '/ '
                                                                            '138 '
                                                                            'degrees '
                                                                            'F',
                                                                   '@junos:celsius': '59'}},
                                                  {'class': 'Fans',
                                                   'comment': '2760 RPM',
                                                   'name': 'Fan Tray 0 Fan 1',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2520 RPM',
                                                   'name': 'Fan Tray 0 Fan 2',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2520 RPM',
                                                   'name': 'Fan Tray 0 Fan 3',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2640 RPM',
                                                   'name': 'Fan Tray 0 Fan 4',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2640 RPM',
                                                   'name': 'Fan Tray 0 Fan 5',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2640 RPM',
                                                   'name': 'Fan Tray 0 Fan 6',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2520 RPM',
                                                   'name': 'Fan Tray 1 Fan 1',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2640 RPM',
                                                   'name': 'Fan Tray 1 Fan 2',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2520 RPM',
                                                   'name': 'Fan Tray 1 Fan 3',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2640 RPM',
                                                   'name': 'Fan Tray 1 Fan 4',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2520 RPM',
                                                   'name': 'Fan Tray 1 Fan 5',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2640 RPM',
                                                   'name': 'Fan Tray 1 Fan 6',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2640 RPM',
                                                   'name': 'Fan Tray 2 Fan 1',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2640 RPM',
                                                   'name': 'Fan Tray 2 Fan 2',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2520 RPM',
                                                   'name': 'Fan Tray 2 Fan 3',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2640 RPM',
                                                   'name': 'Fan Tray 2 Fan 4',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2520 RPM',
                                                   'name': 'Fan Tray 2 Fan 5',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2640 RPM',
                                                   'name': 'Fan Tray 2 Fan 6',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2520 RPM',
                                                   'name': 'Fan Tray 3 Fan 1',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2400 RPM',
                                                   'name': 'Fan Tray 3 Fan 2',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2520 RPM',
                                                   'name': 'Fan Tray 3 Fan 3',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2520 RPM',
                                                   'name': 'Fan Tray 3 Fan 4',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2640 RPM',
                                                   'name': 'Fan Tray 3 Fan 5',
                                                   'status': 'OK'},
                                                  {'class': 'Fans',
                                                   'comment': '2520 RPM',
                                                   'name': 'Fan Tray 3 Fan 6',
                                                   'status': 'OK'}]}}
    
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisEnvironment(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisEnvironment(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowChassisAlarms(unittest.TestCase):
    """Unit test for show chassis alarms"""
    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value':'''
        1 alarms currently active
        Alarm time               Class  Description
        2020-07-16 13:38:21 EST  Major  PSM 15 Not OK    
    '''}

    golden_parsed_output =  {
        "alarm-information": {
            "alarm-detail": {
                "alarm-class": "Major",
                "alarm-description": "PSM 15 Not OK",
                "alarm-short-description": "PSM 15 Not OK",
                "alarm-time": {
                    "#text": "2020-07-16 13:38:21 EST",
                },
                "alarm-type": "Chassis"
            },
            "alarm-summary": {
                "active-alarm-count": "1"
            }
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisAlarms(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisAlarms(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)    


class TestShowChassisFabricSummary(unittest.TestCase):
    """Unit test for show chassis Fabric Summary"""
    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value':'''
        show chassis fabric summary
        Plane   State    Uptime
        0      Online   34 days, 18 hours, 43 minutes, 48 seconds
        1      Online   34 days, 18 hours, 43 minutes, 47 seconds
        2      Online   34 days, 18 hours, 43 minutes, 48 seconds
        3      Online   34 days, 18 hours, 43 minutes, 47 seconds
        4      Spare    34 days, 18 hours, 43 minutes, 47 seconds
        5      Spare    34 days, 18 hours, 43 minutes, 46 seconds
        6      Spare    34 days, 18 hours, 43 minutes, 46 seconds
        7      Spare    34 days, 18 hours, 43 minutes, 46 seconds   
    '''}

    golden_parsed_output =  {
        "fm-state-information": {
            "fm-state-item": [
                {
                    "plane-slot": "0",
                    "state": "Online",
                    "up-time": "34 days, 18 hours, 43 minutes, 48 seconds"
                },
                {
                    "plane-slot": "1",
                    "state": "Online",
                    "up-time": "34 days, 18 hours, 43 minutes, 47 seconds"
                },
                {
                    "plane-slot": "2",
                    "state": "Online",
                    "up-time": "34 days, 18 hours, 43 minutes, 48 seconds"
                },
                {
                    "plane-slot": "3",
                    "state": "Online",
                    "up-time": "34 days, 18 hours, 43 minutes, 47 seconds"
                },
                {
                    "plane-slot": "4",
                    "state": "Spare",
                    "up-time": "34 days, 18 hours, 43 minutes, 47 seconds"
                },
                {
                    "plane-slot": "5",
                    "state": "Spare",
                    "up-time": "34 days, 18 hours, 43 minutes, 46 seconds"
                },
                {
                    "plane-slot": "6",
                    "state": "Spare",
                    "up-time": "34 days, 18 hours, 43 minutes, 46 seconds"
                },
                {
                    "plane-slot": "7",
                    "state": "Spare",
                    "up-time": "34 days, 18 hours, 43 minutes, 46 seconds"
                }
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisFabricSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisFabricSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output) 


class TestShowChassisFabricPlane(unittest.TestCase):
    """Unit test for show chassis Fabric Plane"""
    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value':'''
        show chassis fabric plane
        Fabric management PLANE state
        Plane 0
        Plane state: ACTIVE
            FPC 0
                PFE 0 :Links ok
                PFE 1 :Links ok
            FPC 1
                PFE 0 :Links ok
                PFE 1 :Links ok
        Plane 1
        Plane state: ACTIVE
            FPC 0
                PFE 0 :Links ok
                PFE 1 :Links ok
            FPC 1
                PFE 0 :Links ok
                PFE 1 :Links ok
        Plane 2
        Plane state: ACTIVE
            FPC 0
                PFE 0 :Links ok
                PFE 1 :Links ok
            FPC 1
                PFE 0 :Links ok
                PFE 1 :Links ok
        Plane 3
        Plane state: ACTIVE
            FPC 0
                PFE 0 :Links ok
                PFE 1 :Links ok
            FPC 1
                PFE 0 :Links ok
                PFE 1 :Links ok
        Plane 4
        Plane state: SPARE
            FPC 0
                PFE 0 :Links ok
                PFE 1 :Links ok
            FPC 1
                PFE 0 :Links ok
                PFE 1 :Links ok
        Plane 5
        Plane state: SPARE
            FPC 0
                PFE 0 :Links ok
                PFE 1 :Links ok
            FPC 1
                PFE 0 :Links ok
                PFE 1 :Links ok
        Plane 6
        Plane state: SPARE
            FPC 0
                PFE 0 :Links ok
                PFE 1 :Links ok
            FPC 1
                PFE 0 :Links ok
                PFE 1 :Links ok
        Plane 7
        Plane state: SPARE
            FPC 0
                PFE 0 :Links ok
                PFE 1 :Links ok
            FPC 1
                PFE 0 :Links ok
                PFE 1 :Links ok  
    '''}

    golden_parsed_output =  {
        "fm-plane-state-information": {
            "fmp-plane": [
                {
                    "fru-name": [
                        "FPC",
                        "FPC"
                    ],
                    "fru-slot": [
                        "0",
                        "1"
                    ],
                    "pfe-link-status": [
                        "Links ok",
                        "Links ok",
                        "Links ok",
                        "Links ok"
                    ],
                    "pfe-slot": [
                        "0",
                        "1",
                        "0",
                        "1"
                    ],
                    "slot": "0",
                    "state": "ACTIVE"
                },
                {
                    "fru-name": [
                        "FPC",
                        "FPC"
                    ],
                    "fru-slot": [
                        "0",
                        "1"
                    ],
                    "pfe-link-status": [
                        "Links ok",
                        "Links ok",
                        "Links ok",
                        "Links ok"
                    ],
                    "pfe-slot": [
                        "0",
                        "1",
                        "0",
                        "1"
                    ],
                    "slot": "1",
                    "state": "ACTIVE"
                },
                {
                    "fru-name": [
                        "FPC",
                        "FPC"
                    ],
                    "fru-slot": [
                        "0",
                        "1"
                    ],
                    "pfe-link-status": [
                        "Links ok",
                        "Links ok",
                        "Links ok",
                        "Links ok"
                    ],
                    "pfe-slot": [
                        "0",
                        "1",
                        "0",
                        "1"
                    ],
                    "slot": "2",
                    "state": "ACTIVE"
                },
                {
                    "fru-name": [
                        "FPC",
                        "FPC"
                    ],
                    "fru-slot": [
                        "0",
                        "1"
                    ],
                    "pfe-link-status": [
                        "Links ok",
                        "Links ok",
                        "Links ok",
                        "Links ok"
                    ],
                    "pfe-slot": [
                        "0",
                        "1",
                        "0",
                        "1"
                    ],
                    "slot": "3",
                    "state": "ACTIVE"
                },
                {
                    "fru-name": [
                        "FPC",
                        "FPC"
                    ],
                    "fru-slot": [
                        "0",
                        "1"
                    ],
                    "pfe-link-status": [
                        "Links ok",
                        "Links ok",
                        "Links ok",
                        "Links ok"
                    ],
                    "pfe-slot": [
                        "0",
                        "1",
                        "0",
                        "1"
                    ],
                    "slot": "4",
                    "state": "SPARE"
                },
                {
                    "fru-name": [
                        "FPC",
                        "FPC"
                    ],
                    "fru-slot": [
                        "0",
                        "1"
                    ],
                    "pfe-link-status": [
                        "Links ok",
                        "Links ok",
                        "Links ok",
                        "Links ok"
                    ],
                    "pfe-slot": [
                        "0",
                        "1",
                        "0",
                        "1"
                    ],
                    "slot": "5",
                    "state": "SPARE"
                },
                {
                    "fru-name": [
                        "FPC",
                        "FPC"
                    ],
                    "fru-slot": [
                        "0",
                        "1"
                    ],
                    "pfe-link-status": [
                        "Links ok",
                        "Links ok",
                        "Links ok",
                        "Links ok"
                    ],
                    "pfe-slot": [
                        "0",
                        "1",
                        "0",
                        "1"
                    ],
                    "slot": "6",
                    "state": "SPARE"
                },
                {
                    "fru-name": [
                        "FPC",
                        "FPC"
                    ],
                    "fru-slot": [
                        "0",
                        "1"
                    ],
                    "pfe-link-status": [
                        "Links ok",
                        "Links ok",
                        "Links ok",
                        "Links ok"
                    ],
                    "pfe-slot": [
                        "0",
                        "1",
                        "0",
                        "1"
                    ],
                    "slot": "7",
                    "state": "SPARE"
                }
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowChassisFabricPlane(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowChassisFabricPlane(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)



if __name__ == '__main__':
    unittest.main()