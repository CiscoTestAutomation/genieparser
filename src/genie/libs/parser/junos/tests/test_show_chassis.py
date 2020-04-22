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
                                                 ShowChassisRoutingEngineNoForwarding

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


class TestShowChassisFpc(unittest.TestCase):
    """ Unit tests for:
            * show chassis fpc
    """

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': 
    ''' show chassis fpc
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
            "route-engine": {
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
            "route-engine": {
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

if __name__ == '__main__':
    unittest.main()