# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.iosxe.show_logging import ShowLogging

# ==============================================
# Unittest for:
#   * 'show logging'
# ==============================================
class test_show_logging(unittest.TestCase):
    '''Unittest for:
        * 'show logging'
    '''
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        "logs": [
            "Syslog logging: enabled (0 messages dropped, 149 messages rate-limited, 0 flushes, 0 overruns, xml disabled, filtering disabled)",
            "No Active Message Discriminator.",
            "No Inactive Message Discriminator.",
            "Console logging: disabled",
            "Monitor logging: level debugging, 0 messages logged, xml disabled,",
            "filtering disabled",
            "Buffer logging:  level debugging, 481 messages logged, xml disabled,",
            "filtering disabled",
            "Exception Logging: size (4096 bytes)",
            "Count and timestamp logging messages: disabled",
            "Persistent logging: disabled",
            "No active filter modules.",
            "Trap logging: level informational, 478 message lines logged",
            "Logging Source-Interface:       VRF Name:",
            "Log Buffer (4096 bytes):",
            "ate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 14:55:33.426: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 14:56:05.114: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 14:56:37.891: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 14:57:10.121: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 14:57:42.362: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 14:58:14.621: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 14:59:21.114: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:00:26.115: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:01:31.114: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:04:13.337: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:06:21.132: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:10:06.114: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:11:13.113: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:12:19.113: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:12:49.586: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:22:24.383: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:29:42.116: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:30:25.115: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:30:59.116: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:31:29.116: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:32:04.115: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:32:36.115: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:45:54.755: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:49:31.164: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:50:24.117: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:50:56.116: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:51:29.117: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:52:03.118: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 15:52:33.120: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 16:00:07.019: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 16:08:30.412: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 16:09:14.118: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 16:10:12.118: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 16:11:18.118: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000",
            "*Jun  4 16:12:22.118: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000"
        ]
    }

    golden_output_1 = {'execute.return_value': '''
        Syslog logging: enabled (0 messages dropped, 149 messages rate-limited, 0 flushes, 0 overruns, xml disabled, filtering disabled)

        No Active Message Discriminator.

        No Inactive Message Discriminator.

            Console logging: disabled
            Monitor logging: level debugging, 0 messages logged, xml disabled,
                             filtering disabled
            Buffer logging:  level debugging, 481 messages logged, xml disabled,
                            filtering disabled
            Exception Logging: size (4096 bytes)
            Count and timestamp logging messages: disabled
            Persistent logging: disabled

        No active filter modules.

            Trap logging: level informational, 478 message lines logged
                Logging Source-Interface:       VRF Name:

        Log Buffer (4096 bytes):
        ate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 14:55:33.426: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 14:56:05.114: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 14:56:37.891: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 14:57:10.121: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 14:57:42.362: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 14:58:14.621: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 14:59:21.114: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:00:26.115: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:01:31.114: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:04:13.337: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:06:21.132: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:10:06.114: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:11:13.113: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:12:19.113: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:12:49.586: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:22:24.383: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:29:42.116: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:30:25.115: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:30:59.116: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:31:29.116: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:32:04.115: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:32:36.115: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:45:54.755: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:49:31.164: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:50:24.117: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:50:56.116: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:51:29.117: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:52:03.118: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 15:52:33.120: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 16:00:07.019: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 16:08:30.412: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 16:09:14.118: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 16:10:12.118: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 16:11:18.118: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        *Jun  4 16:12:22.118: %IP-4-DUPADDR: Duplicate address 172.16.1.217 on GigabitEthernet1, sourced by 5e00.8007.0000
        '''}

    def test_show_logging_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLogging(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_logging_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowLogging(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


if __name__ == '__main__':
    unittest.main()
