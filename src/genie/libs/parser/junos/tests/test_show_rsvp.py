# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device, loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.junos.show_rsvp import (ShowRSVPNeighbor,
                                                )


class test_show_rsvp_neighbor(unittest.TestCase):
    device = Device(name='aName')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': """
    kddi@sr_hktGCS002> show rsvp neighbor
    RSVP neighbor: 4 learned
    Address            Idle Up/Dn LastChange HelloInt HelloTx/Rx MsgRcvd
    10.34.3.252      15:55  0/0       15:52        9   106/0    0
    10.169.14.240    34:15  0/0       34:13        9   229/0    0
    10.169.14.157        0  1/0       34:13        9   230/229  333
    192.168.145.218       0  1/0       15:55        9   105/105  197"""}

    golden_parsed_output_1 = {
        'rsvp-neighbor-information': {
            'rsvp-neighbor-count': '4',
            'rsvp-neighbor': [{
                'rsvp-neighbor-address': '10.34.3.252',
                'neighbor-idle': '15:55',
                'neighbor-up-count': '0',
                'neighbor-down-count': '0',
                'last-changed-time': '15:52',
                'hello-interval': '9',
                'hellos-sent': '106',
                'hellos-received': '0',
                'messages-received': '0'
                }, {
                'rsvp-neighbor-address': '10.169.14.240',
                'neighbor-idle': '34:15',
                'neighbor-up-count': '0',
                'neighbor-down-count': '0',
                'last-changed-time': '34:13',
                'hello-interval': '9',
                'hellos-sent': '229',
                'hellos-received': '0',
                'messages-received': '0'
                }, {
                'rsvp-neighbor-address': '10.169.14.157',
                'neighbor-idle': '0',
                'neighbor-up-count': '1',
                'neighbor-down-count': '0',
                'last-changed-time': '34:13',
                'hello-interval': '9',
                'hellos-sent': '230',
                'hellos-received': '229',
                'messages-received': '333'
                }, {
                'rsvp-neighbor-address': '192.168.145.218',
                'neighbor-idle': '0',
                'neighbor-up-count': '1',
                'neighbor-down-count': '0',
                'last-changed-time': '15:55',
                'hello-interval': '9',
                'hellos-sent': '105',
                'hellos-received': '105',
                'messages-received': '197'
            }]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRSVPNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowRSVPNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


if __name__ == '__main__':
    unittest.main()