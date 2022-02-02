import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.libs.parser.iosxr.show_tacacs import ShowTacacs


class test_show_tacacs(unittest.TestCase):
    ''' Unit test for "show tacacs" '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}
    golden_parsed_output_brief = {
        "server": {
            "127.0.0.1/24": {
                "vrf": "default",
                "server_type": "private",
                "opens": "123543",
                "closes": "123543",
                "aborts": "592",
                "errors": "0",
                "packets_in": "134396",
                "packets_out": "134421",
                "status": "up",
                "single_connect": "false",
                "family": "IPv4"
            }
        }
    }

    golden_output_brief = {'execute.return_value': '''
Wed Feb  2 09:06:41.714 CET

Server: 127.0.0.1/24 vrf=default [private]
        opens=123543 closes=123543 aborts=592 errors=0
        packets in=134396 packets out=134421
        status=up single-connect=false family=IPv4

    '''
    }

    def test_show_tacas(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowTacacs(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)


if __name__ == '__main__':
    unittest.main()
