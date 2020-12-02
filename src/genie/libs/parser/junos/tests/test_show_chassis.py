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
                                                 ShowChassisAlarms

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
                        "chassis-re-disk-module": [{
                            "description": "Hard Disk",
                            "disk-size": "27649",
                            "model": "VMware Virtual IDE Har",
                            "name": "cd0",
                            "serial-number": "00000000000000000001"
                        }],
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
                                "chassis-sub-sub-module": [{
                                    "description": "Virtual",
                                    "name": "PIC 0",
                                    "part-number": "BUILTIN",
                                    "serial-number": "BUILTIN"
                                }],
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

    golden_output_2 = {'execute.return_value':'''
    > show chassis hardware detail
        Hardware inventory:
        Item             Version  Part number  Serial number     Description
        Chassis                                JN125D903AFJ      MX2020
        Midplane         REV 64   750-040240   ABAC9716          Lower Backplane
        Midplane 1       REV 06   711-032386   ABAC9742          Upper Backplane
        PMP 1            REV 01   711-051408   ACAJ5284          Upper Power Midplane
        PMP 0            REV 01   711-051406   ACAJ5165          Lower Power Midplane
        FPM Board        REV 13   760-040242   ABDD0194          Front Panel Display
        PSM 0            REV 04   740-050037   1EDB5270035       DC 52V Power Supply Module
        PSM 1            REV 04   740-050037   1EDB527003C       DC 52V Power Supply Module
        PSM 2            REV 04   740-050037   1EDB52202SM       DC 52V Power Supply Module
        PSM 3            REV 04   740-050037   1EDB527002J       DC 52V Power Supply Module
        PSM 4            REV 04   740-050037   1EDB527002L       DC 52V Power Supply Module
        PSM 5            REV 04   740-050037   1EDB52202PZ       DC 52V Power Supply Module
        PSM 6            REV 04   740-050037   1EDB52202ZD       DC 52V Power Supply Module
        PSM 7            REV 04   740-050037   1EDB527002N       DC 52V Power Supply Module
        PSM 8            REV 04   740-050037   1EDB527002S       DC 52V Power Supply Module
        PSM 9            REV 04   740-050037   1EDB5270010       DC 52V Power Supply Module
        PSM 10           REV 04   740-050037   1EDB52202XW       DC 52V Power Supply Module
        PSM 11           REV 04   740-050037   1EDB527002P       DC 52V Power Supply Module
        PSM 12           REV 04   740-050037   1EDB52202VJ       DC 52V Power Supply Module
        PSM 13           REV 04   740-050037   1EDB527001V       DC 52V Power Supply Module
        PSM 14           REV 04   740-050037   1EDB52202K3       DC 52V Power Supply Module
        PSM 15           REV 04   740-050037   1EDB527001L       DC 52V Power Supply Module
        PSM 16           REV 04   740-050037   1EDB527001P       DC 52V Power Supply Module
        PSM 17           REV 04   740-050037   1EDB52202PM       DC 52V Power Supply Module
        PDM 0            REV 01   740-050036   1EFD3390141       DC Power Dist Module
        PDM 1            REV 01   740-050036   1EFD3390149       DC Power Dist Module
        PDM 2            REV 01   740-050036   1EFD3390162       DC Power Dist Module
        PDM 3            REV 01   740-050036   1EFD3390136       DC Power Dist Module
        Routing Engine 0 REV 01   740-052100   9009237267        RE-S-1800x4
        ad0    3919 MB  604784               000060095234B000018D Compact Flash
        ad1   28496 MB  StorFly - VSFA18PI032G- P1T12003591504100303 Disk 1
        usb0 (addr 1)  EHCI root hub 0       Intel             uhub0
        usb0 (addr 2)  product 0x0020 32     vendor 0x8087     uhub1
        DIMM 0         VL33B1G63F-K9SQ-KC DIE REV-0 PCB REV-0  MFR ID-ce80
        DIMM 1         VL33B1G63F-K9SQ-KC DIE REV-0 PCB REV-0  MFR ID-ce80
        DIMM 2         VL33B1G63F-K9SQ-KC DIE REV-0 PCB REV-0  MFR ID-ce80
        DIMM 3         VL33B1G63F-K9SQ-KC DIE REV-0 PCB REV-0  MFR ID-ce80
        Routing Engine 1 REV 01   740-052100   9009237474        RE-S-1800x4
        ad0    3919 MB  604784               000060095234B00001BA Compact Flash
        ad1   28496 MB  StorFly - VSFA18PI032G- P1T05003591504080057 Disk 1
        CB 0             REV 10   750-051985   CAFC0322          Control Board
        CB 1             REV 10   750-051985   CAFC0337          Control Board
        SPMB 0           REV 04   711-041855   ABDC5673          PMB Board
        SPMB 1           REV 04   711-041855   ABDA9007          PMB Board
        SFB 0            REV 06   711-044466   ABCY8621          Switch Fabric Board
        SFB 1            REV 07   711-044466   ABDB4626          Switch Fabric Board
        SFB 2            REV 06   711-044466   ABCZ9595          Switch Fabric Board
        SFB 3            REV 07   711-044466   ABDB4637          Switch Fabric Board
        SFB 4            REV 07   711-044466   ABDC6281          Switch Fabric Board
        SFB 5            REV 06   711-044466   ABCZ9386          Switch Fabric Board
        SFB 6            REV 07   711-044466   ABDC6286          Switch Fabric Board
        SFB 7            REV 07   711-044466   ABDC6495          Switch Fabric Board
        FPC 0            REV 72   750-044130   ABDF7568          MPC6E 3D
        CPU            REV 12   711-045719   ABDF7304          RMPC PMB
        MIC 0          REV 19   750-049457   ABDJ2346          2X100GE CFP2 OTN
            PIC 0                 BUILTIN      BUILTIN           2X100GE CFP2 OTN
            Xcvr 0     REV 01   740-052504   UW811XC           CFP2-100G-LR4
            Xcvr 1     REV 01   740-052504   UW70304           CFP2-100G-LR4
        MIC 1          REV 28   750-046532   ABDG0526          24X10GE SFPP
            PIC 1                 BUILTIN      BUILTIN           24X10GE SFPP
            Xcvr 0     REV 01   740-031981   F7G2011247        SFP+-10G-LR
            Xcvr 1     REV 01   740-031981   F7J2018525        SFP+-10G-LR
            Xcvr 2     REV 01   740-031981   F7G2011211        SFP+-10G-LR
            Xcvr 3     REV 01   740-031981   F7J2018541        SFP+-10G-LR
            Xcvr 4     REV 01   740-031981   F7G2011226        SFP+-10G-LR
            Xcvr 5     REV 01   740-031981   F7G2011277        SFP+-10G-LR
            Xcvr 6     REV 01   740-031981   F7G2011182        SFP+-10G-LR
            Xcvr 7     REV 01   740-031981   F7J2018422        SFP+-10G-LR
            Xcvr 8     REV 01   740-031981   F7J2018446        SFP+-10G-LR
            Xcvr 9     REV 01   740-031981   F7J2018443        SFP+-10G-LR
            Xcvr 10    REV 01   740-031981   F7G2011165        SFP+-10G-LR
            Xcvr 11    REV 01   740-031981   F7G2011263        SFP+-10G-LR
            Xcvr 12    REV 01   740-031981   F7G2011283        SFP+-10G-LR
            Xcvr 13    REV 01   740-031981   F7J2018424        SFP+-10G-LR
            Xcvr 14    REV 01   740-031981   F7G2011224        SFP+-10G-LR
            Xcvr 15    REV 01   740-031981   F7J2018502        SFP+-10G-LR
            Xcvr 16    REV 01   740-031981   F7G2011200        SFP+-10G-LR
            Xcvr 17    REV 01   740-031981   F7J2018495        SFP+-10G-LR
            Xcvr 18    REV 01   740-031981   F7J2018435        SFP+-10G-LR
            Xcvr 19    REV 01   740-031981   F7J2018430        SFP+-10G-LR
            Xcvr 20    REV 01   740-021309   XN74D671039       SFP+-10G-LR
            Xcvr 21    REV 01   740-021309   XN74D671041       SFP+-10G-LR
            Xcvr 22    REV 01   740-031983   UTQ1D19           SFP+-10G-ER
            Xcvr 23    REV 01   740-031983   UTQ1D2P           SFP+-10G-ER
        XLM 0          REV 14   711-046638   ABDF2862          MPC6E XL
        XLM 1          REV 14   711-046638   ABDF2893          MPC6E XL
        FPC 9            REV 19   750-038491   CAFC4523          MPCE Type 2 3D
        CPU            REV 06   711-038484   CAEY2214          MPCE PMB 2G
        MIC 0          REV 19   750-043688   CAET3123          MS-MIC-16G
            PIC 0                 BUILTIN      BUILTIN           MS-MIC-16G
        MIC 1          REV 11   750-049846   CAFA6278          3D 20x 1GE(LAN)-E,SFP
            PIC 2                 BUILTIN      BUILTIN           10x 1GE(LAN) -E  SFP
            Xcvr 0     REV 01   740-031850   AC1522SA10E       SFP-LX10
            Xcvr 1     REV 01   740-031850   AC1522SA10T       SFP-LX10
            Xcvr 2     REV 01   740-031850   AC1522SA10P       SFP-LX10
            Xcvr 3     REV 01   740-031850   AC1522SA10Q       SFP-LX10
            Xcvr 4     REV 01   740-011783   P950PWN           SFP-LX10
            Xcvr 5              NON-JNPR     AGM1049Q4E4       SFP-T
            Xcvr 6     REV 01   740-031850   AC1522SA10J       SFP-LX10
            Xcvr 7     REV 01   740-031850   AC1522SA10W       SFP-LX10
            Xcvr 8              NON-JNPR     AGM1708211W       SFP-T
            Xcvr 9     REV 01   740-031850   AC1522SA10H       SFP-LX10
            PIC 3                 BUILTIN      BUILTIN           10x 1GE(LAN) -E  SFP
            Xcvr 0     REV 01   740-031850   AC1522SA10G       SFP-LX10
            Xcvr 1     REV 01   740-031850   AC1522SA10M       SFP-LX10
            Xcvr 2              NON-JNPR     00000MTC101600GS  SFP-T
            Xcvr 3     REV 02   740-013111   B133802           SFP-T
            Xcvr 4     REV 01   740-031850   AC1522SA10U       SFP-LX10
            Xcvr 5              NON-JNPR     AGM1120Q5E5       SFP-T
            Xcvr 6     REV 01   740-031850   AC1522SA10Z       SFP-LX10
            Xcvr 7     REV 01   740-031850   AC1522SA10K       SFP-LX10
            Xcvr 8     l*       NON-JNPR     AGM17082139       SFP-T
            Xcvr 9     }        NON-JNPR     AGM1708212S       SFP-T
        ADC 9            REV 21   750-043596   ABDC2129          Adapter Card
        Fan Tray 0       REV 01   760-052467   ACAY4748          172mm FanTray - 6 Fans
        Fan Tray 1       REV 01   760-052467   ACAY4731          172mm FanTray - 6 Fans
        Fan Tray 2       REV 01   760-052467   ACAY4747          172mm FanTray - 6 Fans
        Fan Tray 3       REV 01   760-052467   ACAY4754          172mm FanTray - 6 Fans
    
    '''}

    golden_parsed_output_2 = {'chassis-inventory': {'chassis': {'@junos:style': 'inventory',
                                   'chassis-module': [{'description': 'Lower '
                                                                      'Backplane',
                                                       'name': 'Midplane',
                                                       'part-number': '750-040240',
                                                       'serial-number': 'ABAC9716',
                                                       'version': 'REV 64'},
                                                      {'description': 'Upper '
                                                                      'Backplane',
                                                       'name': 'Midplane 1',
                                                       'part-number': '711-032386',
                                                       'serial-number': 'ABAC9742',
                                                       'version': 'REV 06'},
                                                      {'description': 'Upper '
                                                                      'Power '
                                                                      'Midplane',
                                                       'name': 'PMP 1',
                                                       'part-number': '711-051408',
                                                       'serial-number': 'ACAJ5284',
                                                       'version': 'REV 01'},
                                                      {'description': 'Lower '
                                                                      'Power '
                                                                      'Midplane',
                                                       'name': 'PMP 0',
                                                       'part-number': '711-051406',
                                                       'serial-number': 'ACAJ5165',
                                                       'version': 'REV 01'},
                                                      {'description': 'Front '
                                                                      'Panel '
                                                                      'Display',
                                                       'name': 'FPM Board',
                                                       'part-number': '760-040242',
                                                       'serial-number': 'ABDD0194',
                                                       'version': 'REV 13'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 0',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB5270035',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 1',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB527003C',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 2',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB52202SM',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 3',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB527002J',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 4',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB527002L',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 5',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB52202PZ',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 6',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB52202ZD',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 7',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB527002N',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 8',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB527002S',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 9',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB5270010',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 10',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB52202XW',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 11',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB527002P',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 12',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB52202VJ',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 13',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB527001V',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 14',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB52202K3',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 15',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB527001L',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 16',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB527001P',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC 52V '
                                                                      'Power '
                                                                      'Supply '
                                                                      'Module',
                                                       'name': 'PSM 17',
                                                       'part-number': '740-050037',
                                                       'serial-number': '1EDB52202PM',
                                                       'version': 'REV 04'},
                                                      {'description': 'DC '
                                                                      'Power '
                                                                      'Dist '
                                                                      'Module',
                                                       'name': 'PDM 0',
                                                       'part-number': '740-050036',
                                                       'serial-number': '1EFD3390141',
                                                       'version': 'REV 01'},
                                                      {'description': 'DC '
                                                                      'Power '
                                                                      'Dist '
                                                                      'Module',
                                                       'name': 'PDM 1',
                                                       'part-number': '740-050036',
                                                       'serial-number': '1EFD3390149',
                                                       'version': 'REV 01'},
                                                      {'description': 'DC '
                                                                      'Power '
                                                                      'Dist '
                                                                      'Module',
                                                       'name': 'PDM 2',
                                                       'part-number': '740-050036',
                                                       'serial-number': '1EFD3390162',
                                                       'version': 'REV 01'},
                                                      {'description': 'DC '
                                                                      'Power '
                                                                      'Dist '
                                                                      'Module',
                                                       'name': 'PDM 3',
                                                       'part-number': '740-050036',
                                                       'serial-number': '1EFD3390136',
                                                       'version': 'REV 01'},
                                                      {'chassis-re-dimm-module': [{'die-rev': 'DIE '
                                                                                              'REV-0',
                                                                                   'mfr-id': 'MFR '
                                                                                             'ID-ce80',
                                                                                   'name': 'DIMM '
                                                                                           '0',
                                                                                   'part-number': 'VL33B1G63F-K9SQ-KC',
                                                                                   'pcb-rev': 'PCB '
                                                                                              'REV-0'},
                                                                                  {'die-rev': 'DIE '
                                                                                              'REV-0',
                                                                                   'mfr-id': 'MFR '
                                                                                             'ID-ce80',
                                                                                   'name': 'DIMM '
                                                                                           '1',
                                                                                   'part-number': 'VL33B1G63F-K9SQ-KC',
                                                                                   'pcb-rev': 'PCB '
                                                                                              'REV-0'},
                                                                                  {'die-rev': 'DIE '
                                                                                              'REV-0',
                                                                                   'mfr-id': 'MFR '
                                                                                             'ID-ce80',
                                                                                   'name': 'DIMM '
                                                                                           '2',
                                                                                   'part-number': 'VL33B1G63F-K9SQ-KC',
                                                                                   'pcb-rev': 'PCB '
                                                                                              'REV-0'},
                                                                                  {'die-rev': 'DIE '
                                                                                              'REV-0',
                                                                                   'mfr-id': 'MFR '
                                                                                             'ID-ce80',
                                                                                   'name': 'DIMM '
                                                                                           '3',
                                                                                   'part-number': 'VL33B1G63F-K9SQ-KC',
                                                                                   'pcb-rev': 'PCB '
                                                                                              'REV-0'}],
                                                       'chassis-re-disk-module': [{'description': 'Compact '
                                                                                                  'Flash',
                                                                                   'disk-size': '3919',
                                                                                   'model': '604784',
                                                                                   'name': 'ad0',
                                                                                   'serial-number': '000060095234B000018D'},
                                                                                  {'description': 'Disk '
                                                                                                  '1',
                                                                                   'disk-size': '28496',
                                                                                   'model': 'StorFly '
                                                                                            '- '
                                                                                            'VSFA18PI032G-',
                                                                                   'name': 'ad1',
                                                                                   'serial-number': 'P1T12003591504100303'}],
                                                       'chassis-re-usb-module': [{'description': 'uhub0',
                                                                                  'name': 'usb0 '
                                                                                          '(addr '
                                                                                          '1)',
                                                                                  'product': 'EHCI '
                                                                                             'root '
                                                                                             'hub',
                                                                                  'product-number': '0',
                                                                                  'vendor': 'Intel'},
                                                                                 {'description': 'uhub1',
                                                                                  'name': 'usb0 '
                                                                                          '(addr '
                                                                                          '2)',
                                                                                  'product': 'product '
                                                                                             '0x0020',
                                                                                  'product-number': '32',
                                                                                  'vendor': 'vendor '
                                                                                            '0x8087'}],
                                                       'description': 'RE-S-1800x4',
                                                       'name': 'Routing Engine '
                                                               '0',
                                                       'part-number': '740-052100',
                                                       'serial-number': '9009237267',
                                                       'version': 'REV 01'},
                                                      {'chassis-re-disk-module': [{'description': 'Compact '
                                                                                                  'Flash',
                                                                                   'disk-size': '3919',
                                                                                   'model': '604784',
                                                                                   'name': 'ad0',
                                                                                   'serial-number': '000060095234B00001BA'},
                                                                                  {'description': 'Disk '
                                                                                                  '1',
                                                                                   'disk-size': '28496',
                                                                                   'model': 'StorFly '
                                                                                            '- '
                                                                                            'VSFA18PI032G-',
                                                                                   'name': 'ad1',
                                                                                   'serial-number': 'P1T05003591504080057'}],
                                                       'description': 'RE-S-1800x4',
                                                       'name': 'Routing Engine '
                                                               '1',
                                                       'part-number': '740-052100',
                                                       'serial-number': '9009237474',
                                                       'version': 'REV 01'},
                                                      {'description': 'Control '
                                                                      'Board',
                                                       'name': 'CB 0',
                                                       'part-number': '750-051985',
                                                       'serial-number': 'CAFC0322',
                                                       'version': 'REV 10'},
                                                      {'description': 'Control '
                                                                      'Board',
                                                       'name': 'CB 1',
                                                       'part-number': '750-051985',
                                                       'serial-number': 'CAFC0337',
                                                       'version': 'REV 10'},
                                                      {'description': 'PMB '
                                                                      'Board',
                                                       'name': 'SPMB 0',
                                                       'part-number': '711-041855',
                                                       'serial-number': 'ABDC5673',
                                                       'version': 'REV 04'},
                                                      {'description': 'PMB '
                                                                      'Board',
                                                       'name': 'SPMB 1',
                                                       'part-number': '711-041855',
                                                       'serial-number': 'ABDA9007',
                                                       'version': 'REV 04'},
                                                      {'description': 'Switch '
                                                                      'Fabric '
                                                                      'Board',
                                                       'name': 'SFB 0',
                                                       'part-number': '711-044466',
                                                       'serial-number': 'ABCY8621',
                                                       'version': 'REV 06'},
                                                      {'description': 'Switch '
                                                                      'Fabric '
                                                                      'Board',
                                                       'name': 'SFB 1',
                                                       'part-number': '711-044466',
                                                       'serial-number': 'ABDB4626',
                                                       'version': 'REV 07'},
                                                      {'description': 'Switch '
                                                                      'Fabric '
                                                                      'Board',
                                                       'name': 'SFB 2',
                                                       'part-number': '711-044466',
                                                       'serial-number': 'ABCZ9595',
                                                       'version': 'REV 06'},
                                                      {'description': 'Switch '
                                                                      'Fabric '
                                                                      'Board',
                                                       'name': 'SFB 3',
                                                       'part-number': '711-044466',
                                                       'serial-number': 'ABDB4637',
                                                       'version': 'REV 07'},
                                                      {'description': 'Switch '
                                                                      'Fabric '
                                                                      'Board',
                                                       'name': 'SFB 4',
                                                       'part-number': '711-044466',
                                                       'serial-number': 'ABDC6281',
                                                       'version': 'REV 07'},
                                                      {'description': 'Switch '
                                                                      'Fabric '
                                                                      'Board',
                                                       'name': 'SFB 5',
                                                       'part-number': '711-044466',
                                                       'serial-number': 'ABCZ9386',
                                                       'version': 'REV 06'},
                                                      {'description': 'Switch '
                                                                      'Fabric '
                                                                      'Board',
                                                       'name': 'SFB 6',
                                                       'part-number': '711-044466',
                                                       'serial-number': 'ABDC6286',
                                                       'version': 'REV 07'},
                                                      {'description': 'Switch '
                                                                      'Fabric '
                                                                      'Board',
                                                       'name': 'SFB 7',
                                                       'part-number': '711-044466',
                                                       'serial-number': 'ABDC6495',
                                                       'version': 'REV 07'},
                                                      {'chassis-sub-module': [{'description': 'RMPC '
                                                                                              'PMB',
                                                                               'name': 'CPU',
                                                                               'part-number': '711-045719',
                                                                               'serial-number': 'ABDF7304',
                                                                               'version': 'REV '
                                                                                          '12'},
                                                                              {'chassis-sub-sub-module': [{'chassis-sub-sub-sub-module': [{'description': 'CFP2-100G-LR4',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '0',
                                                                                                                                           'part-number': '740-052504',
                                                                                                                                           'serial-number': 'UW811XC',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'CFP2-100G-LR4',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '1',
                                                                                                                                           'part-number': '740-052504',
                                                                                                                                           'serial-number': 'UW70304',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'}],
                                                                                                           'description': '2X100GE '
                                                                                                                          'CFP2 '
                                                                                                                          'OTN',
                                                                                                           'name': 'PIC '
                                                                                                                   '0',
                                                                                                           'part-number': 'BUILTIN',
                                                                                                           'serial-number': 'BUILTIN'}],
                                                                               'description': '2X100GE '
                                                                                              'CFP2 '
                                                                                              'OTN',
                                                                               'name': 'MIC '
                                                                                       '0',
                                                                               'part-number': '750-049457',
                                                                               'serial-number': 'ABDJ2346',
                                                                               'version': 'REV '
                                                                                          '19'},
                                                                              {'chassis-sub-sub-module': [{'chassis-sub-sub-sub-module': [{'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '0',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7G2011247',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '1',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7J2018525',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '2',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7G2011211',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '3',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7J2018541',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '4',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7G2011226',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '5',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7G2011277',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '6',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7G2011182',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '7',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7J2018422',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '8',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7J2018446',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '9',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7J2018443',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '10',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7G2011165',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '11',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7G2011263',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '12',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7G2011283',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '13',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7J2018424',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '14',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7G2011224',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '15',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7J2018502',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '16',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7G2011200',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '17',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7J2018495',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '18',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7J2018435',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '19',
                                                                                                                                           'part-number': '740-031981',
                                                                                                                                           'serial-number': 'F7J2018430',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '20',
                                                                                                                                           'part-number': '740-021309',
                                                                                                                                           'serial-number': 'XN74D671039',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-LR',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '21',
                                                                                                                                           'part-number': '740-021309',
                                                                                                                                           'serial-number': 'XN74D671041',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-ER',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '22',
                                                                                                                                           'part-number': '740-031983',
                                                                                                                                           'serial-number': 'UTQ1D19',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP+-10G-ER',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '23',
                                                                                                                                           'part-number': '740-031983',
                                                                                                                                           'serial-number': 'UTQ1D2P',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'}],
                                                                                                           'description': '24X10GE '
                                                                                                                          'SFPP',
                                                                                                           'name': 'PIC '
                                                                                                                   '1',
                                                                                                           'part-number': 'BUILTIN',
                                                                                                           'serial-number': 'BUILTIN'}],
                                                                               'description': '24X10GE '
                                                                                              'SFPP',
                                                                               'name': 'MIC '
                                                                                       '1',
                                                                               'part-number': '750-046532',
                                                                               'serial-number': 'ABDG0526',
                                                                               'version': 'REV '
                                                                                          '28'},
                                                                              {'description': 'MPC6E '
                                                                                              'XL',
                                                                               'name': 'XLM '
                                                                                       '0',
                                                                               'part-number': '711-046638',
                                                                               'serial-number': 'ABDF2862',
                                                                               'version': 'REV '
                                                                                          '14'},
                                                                              {'description': 'MPC6E '
                                                                                              'XL',
                                                                               'name': 'XLM '
                                                                                       '1',
                                                                               'part-number': '711-046638',
                                                                               'serial-number': 'ABDF2893',
                                                                               'version': 'REV '
                                                                                          '14'}],
                                                       'description': 'MPC6E '
                                                                      '3D',
                                                       'name': 'FPC 0',
                                                       'part-number': '750-044130',
                                                       'serial-number': 'ABDF7568',
                                                       'version': 'REV 72'},
                                                      {'chassis-sub-module': [{'description': 'MPCE '
                                                                                              'PMB '
                                                                                              '2G',
                                                                               'name': 'CPU',
                                                                               'part-number': '711-038484',
                                                                               'serial-number': 'CAEY2214',
                                                                               'version': 'REV '
                                                                                          '06'},
                                                                              {'chassis-sub-sub-module': [{'description': 'MS-MIC-16G',
                                                                                                           'name': 'PIC '
                                                                                                                   '0',
                                                                                                           'part-number': 'BUILTIN',
                                                                                                           'serial-number': 'BUILTIN'}],
                                                                               'description': 'MS-MIC-16G',
                                                                               'name': 'MIC '
                                                                                       '0',
                                                                               'part-number': '750-043688',
                                                                               'serial-number': 'CAET3123',
                                                                               'version': 'REV '
                                                                                          '19'},
                                                                              {'chassis-sub-sub-module': [{'chassis-sub-sub-sub-module': [{'description': 'SFP-LX10',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '0',
                                                                                                                                           'part-number': '740-031850',
                                                                                                                                           'serial-number': 'AC1522SA10E',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP-LX10',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '1',
                                                                                                                                           'part-number': '740-031850',
                                                                                                                                           'serial-number': 'AC1522SA10T',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP-LX10',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '2',
                                                                                                                                           'part-number': '740-031850',
                                                                                                                                           'serial-number': 'AC1522SA10P',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP-LX10',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '3',
                                                                                                                                           'part-number': '740-031850',
                                                                                                                                           'serial-number': 'AC1522SA10Q',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP-LX10',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '4',
                                                                                                                                           'part-number': '740-011783',
                                                                                                                                           'serial-number': 'P950PWN',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP-T',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '5',
                                                                                                                                           'part-number': 'NON-JNPR',
                                                                                                                                           'serial-number': 'AGM1049Q4E4'},
                                                                                                                                          {'description': 'SFP-LX10',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '6',
                                                                                                                                           'part-number': '740-031850',
                                                                                                                                           'serial-number': 'AC1522SA10J',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP-LX10',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '7',
                                                                                                                                           'part-number': '740-031850',
                                                                                                                                           'serial-number': 'AC1522SA10W',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP-T',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '8',
                                                                                                                                           'part-number': 'NON-JNPR',
                                                                                                                                           'serial-number': 'AGM1708211W'},
                                                                                                                                          {'description': 'SFP-LX10',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '9',
                                                                                                                                           'part-number': '740-031850',
                                                                                                                                           'serial-number': 'AC1522SA10H',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'}],
                                                                                                           'description': '10x '
                                                                                                                          '1GE(LAN) '
                                                                                                                          '-E  '
                                                                                                                          'SFP',
                                                                                                           'name': 'PIC '
                                                                                                                   '2',
                                                                                                           'part-number': 'BUILTIN',
                                                                                                           'serial-number': 'BUILTIN'},
                                                                                                          {'chassis-sub-sub-sub-module': [{'description': 'SFP-LX10',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '0',
                                                                                                                                           'part-number': '740-031850',
                                                                                                                                           'serial-number': 'AC1522SA10G',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP-LX10',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '1',
                                                                                                                                           'part-number': '740-031850',
                                                                                                                                           'serial-number': 'AC1522SA10M',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP-T',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '2',
                                                                                                                                           'part-number': 'NON-JNPR',
                                                                                                                                           'serial-number': '00000MTC101600GS'},
                                                                                                                                          {'description': 'SFP-T',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '3',
                                                                                                                                           'part-number': '740-013111',
                                                                                                                                           'serial-number': 'B133802',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '02'},
                                                                                                                                          {'description': 'SFP-LX10',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '4',
                                                                                                                                           'part-number': '740-031850',
                                                                                                                                           'serial-number': 'AC1522SA10U',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP-T',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '5',
                                                                                                                                           'part-number': 'NON-JNPR',
                                                                                                                                           'serial-number': 'AGM1120Q5E5'},
                                                                                                                                          {'description': 'SFP-LX10',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '6',
                                                                                                                                           'part-number': '740-031850',
                                                                                                                                           'serial-number': 'AC1522SA10Z',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP-LX10',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '7',
                                                                                                                                           'part-number': '740-031850',
                                                                                                                                           'serial-number': 'AC1522SA10K',
                                                                                                                                           'version': 'REV '
                                                                                                                                                      '01'},
                                                                                                                                          {'description': 'SFP-T',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '8',
                                                                                                                                           'part-number': 'NON-JNPR',
                                                                                                                                           'serial-number': 'AGM17082139',
                                                                                                                                           'version': 'l*'},
                                                                                                                                          {'description': 'SFP-T',
                                                                                                                                           'name': 'Xcvr '
                                                                                                                                                   '9',
                                                                                                                                           'part-number': 'NON-JNPR',
                                                                                                                                           'serial-number': 'AGM1708212S',
                                                                                                                                           'version': '}'}],
                                                                                                           'description': '10x '
                                                                                                                          '1GE(LAN) '
                                                                                                                          '-E  '
                                                                                                                          'SFP',
                                                                                                           'name': 'PIC '
                                                                                                                   '3',
                                                                                                           'part-number': 'BUILTIN',
                                                                                                           'serial-number': 'BUILTIN'}],
                                                                               'description': '3D '
                                                                                              '20x '
                                                                                              '1GE(LAN)-E,SFP',
                                                                               'name': 'MIC '
                                                                                       '1',
                                                                               'part-number': '750-049846',
                                                                               'serial-number': 'CAFA6278',
                                                                               'version': 'REV '
                                                                                          '11'}],
                                                       'description': 'MPCE '
                                                                      'Type 2 '
                                                                      '3D',
                                                       'name': 'FPC 9',
                                                       'part-number': '750-038491',
                                                       'serial-number': 'CAFC4523',
                                                       'version': 'REV 19'},
                                                      {'description': 'Adapter '
                                                                      'Card',
                                                       'name': 'ADC 9',
                                                       'part-number': '750-043596',
                                                       'serial-number': 'ABDC2129',
                                                       'version': 'REV 21'},
                                                      {'description': '172mm '
                                                                      'FanTray '
                                                                      '- 6 '
                                                                      'Fans',
                                                       'name': 'Fan Tray 0',
                                                       'part-number': '760-052467',
                                                       'serial-number': 'ACAY4748',
                                                       'version': 'REV 01'},
                                                      {'description': '172mm '
                                                                      'FanTray '
                                                                      '- 6 '
                                                                      'Fans',
                                                       'name': 'Fan Tray 1',
                                                       'part-number': '760-052467',
                                                       'serial-number': 'ACAY4731',
                                                       'version': 'REV 01'},
                                                      {'description': '172mm '
                                                                      'FanTray '
                                                                      '- 6 '
                                                                      'Fans',
                                                       'name': 'Fan Tray 2',
                                                       'part-number': '760-052467',
                                                       'serial-number': 'ACAY4747',
                                                       'version': 'REV 01'},
                                                      {'description': '172mm '
                                                                      'FanTray '
                                                                      '- 6 '
                                                                      'Fans',
                                                       'name': 'Fan Tray 3',
                                                       'part-number': '760-052467',
                                                       'serial-number': 'ACAY4754',
                                                       'version': 'REV 01'}],
                                   'description': 'MX2020',
                                   'name': 'Chassis',
                                   'serial-number': 'JN125D903AFJ'}}}
    

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

    def test_golden2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowChassisHardwareDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)        


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

    golden_parsed_output = {'chassis-inventory': {'chassis': {'@junos:style': 'inventory',
                                   'chassis-module': [{'name': 'Midplane'},
                                                      {'chassis-re-disk-module': [{'description': 'Hard '
                                                                                                  'Disk',
                                                                                   'disk-size': '27649',
                                                                                   'model': 'VMware '
                                                                                            'Virtual '
                                                                                            'IDE '
                                                                                            'Har',
                                                                                   'name': 'cd0',
                                                                                   'serial-number': '00000000000000000001'}],
                                                       'description': 'RE-VMX',
                                                       'name': 'Routing Engine '
                                                               '0'},
                                                      {'description': 'VMX SCB',
                                                       'name': 'CB 0'},
                                                      {'chassis-sub-module': [{'name': 'CPU',
                                                                               'part-number': 'RIOT-LITE',
                                                                               'serial-number': 'BUILTIN',
                                                                               'version': 'Rev. '
                                                                                          '1.0'},
                                                                              {'chassis-sub-sub-module': [{'description': 'Virtual',
                                                                                                           'name': 'PIC '
                                                                                                                   '0',
                                                                                                           'part-number': 'BUILTIN',
                                                                                                           'serial-number': 'BUILTIN'}],
                                                                               'description': 'Virtual',
                                                                               'name': 'MIC '
                                                                                       '0'}],
                                                       'description': 'Virtual '
                                                                      'FPC',
                                                       'name': 'FPC 0'}],
                                   'description': 'VMX',
                                   'name': 'Chassis',
                                   'serial-number': 'VM5D4C6B3599'}}}
                                   
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



if __name__ == '__main__':
    unittest.main()