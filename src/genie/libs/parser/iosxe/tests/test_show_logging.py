# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

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
            "Jun  5 05:09:30.838 EST: %IP-4-DUPADDR: Duplicate address 172.16.1.216 on GigabitEthernet1, sourced by 5e00.80ff.0606",
            "Jun  5 05:10:36.839 EST: %IP-4-DUPADDR: Duplicate address 172.16.1.216 on GigabitEthernet1, sourced by 5e00.80ff.0606",
            "Jun  5 05:10:59.519 EST: %SYS-5-CONFIG_I: Configured from console by cisco on console",
            "Jun  5 05:11:04.626 EST: Rollback:Acquired Configuration lock.",
            "Jun  5 05:11:04.626 EST: %SYS-5-CONFIG_R: Config Replace is Done",
            "Jun  5 05:11:14.115 EST: Rollback:Acquired Configuration lock.",
            "Jun  5 05:11:14.115 EST: %SYS-5-CONFIG_R: Config Replace is Done"
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
        Jun  5 05:09:30.838 EST: %IP-4-DUPADDR: Duplicate address 172.16.1.216 on GigabitEthernet1, sourced by 5e00.80ff.0606
        Jun  5 05:10:36.839 EST: %IP-4-DUPADDR: Duplicate address 172.16.1.216 on GigabitEthernet1, sourced by 5e00.80ff.0606
        Jun  5 05:10:59.519 EST: %SYS-5-CONFIG_I: Configured from console by cisco on console
        Jun  5 05:11:04.626 EST: Rollback:Acquired Configuration lock.
        Jun  5 05:11:04.626 EST: %SYS-5-CONFIG_R: Config Replace is Done
        Jun  5 05:11:14.115 EST: Rollback:Acquired Configuration lock.
        Jun  5 05:11:14.115 EST: %SYS-5-CONFIG_R: Config Replace is Done
        '''}

    golden_parsed_output_2 = {
        "logs": [
            "Jun  5 05:11:04.626 EST: Rollback:Acquired Configuration lock.",
            "Jun  5 05:11:14.115 EST: Rollback:Acquired Configuration lock."
        ]
    }

    golden_output_2 = {'execute.return_value': '''
        Jun  5 05:11:04.626 EST: Rollback:Acquired Configuration lock.
        Jun  5 05:11:14.115 EST: Rollback:Acquired Configuration lock.
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

    def test_show_logging_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowLogging(device=self.device)
        parsed_output = obj.parse(include='Rollback')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


if __name__ == '__main__':
    unittest.main()
