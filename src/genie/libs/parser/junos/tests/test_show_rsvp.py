# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device, loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.junos.show_rsvp import (ShowRSVPNeighbor,
                                               ShowRSVPSession,
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

class test_show_rsvp_neighbor(unittest.TestCase):
    device = Device(name='aName')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': """
        show rsvp session
        Ingress RSVP: 0 sessions
        Total 0 displayed, Up 0, Down 0

        Egress RSVP: 0 sessions
        Total 0 displayed, Up 0, Down 0

        Transit RSVP: 30 sessions
        To              From            State   Rt Style Labelin Labelout LSPname
        27.85.194.125   27.85.194.127   Up       0  1 FF      46       44 test_lsp_01
        27.85.194.125   27.85.194.127   Up       0  1 FF      37       35 test_lsp_02
        27.85.194.125   27.85.194.127   Up       0  1 FF      28       26 test_lsp_03
        27.85.194.125   27.85.194.127   Up       0  1 FF      20       18 test_lsp_04
        27.85.194.125   27.85.194.127   Up       0  1 FF      26       24 test_lsp_05
        27.85.194.125   27.85.194.127   Up       0  1 FF      30       28 test_lsp_06
        27.85.194.125   27.85.194.127   Up       0  1 FF      19       17 test_lsp_07
        27.85.194.125   27.85.194.127   Up       0  1 FF      21       19 test_lsp_08
        27.85.194.125   27.85.194.127   Up       0  1 FF      39       37 test_lsp_09
        27.85.194.125   27.85.194.127   Up       0  1 FF      45       43 test_lsp_10
        27.85.194.125   27.85.194.127   Up       0  1 FF      23       21 test_lsp_11
        27.85.194.125   27.85.194.127   Up       0  1 FF      36       34 test_lsp_12
        27.85.194.125   27.85.194.127   Up       0  1 FF      42       40 test_lsp_13
        27.85.194.125   27.85.194.127   Up       0  1 FF      47       45 test_lsp_14
        27.85.194.125   27.85.194.127   Up       0  1 FF      18       16 test_lsp_15
        27.85.194.125   27.85.194.127   Up       0  1 FF      40       38 test_lsp_16
        27.85.194.125   27.85.194.127   Up       0  1 FF      22       20 test_lsp_17
        27.85.194.125   27.85.194.127   Up       0  1 FF      31       29 test_lsp_18
        27.85.194.125   27.85.194.127   Up       0  1 FF      41       39 test_lsp_19
        27.85.194.125   27.85.194.127   Up       0  1 FF      24       22 test_lsp_20
        27.85.194.125   27.85.194.127   Up       0  1 FF      32       30 test_lsp_21
        27.85.194.125   27.85.194.127   Up       0  1 FF      33       31 test_lsp_22
        27.85.194.125   27.85.194.127   Up       0  1 FF      34       32 test_lsp_23
        27.85.194.125   27.85.194.127   Up       0  1 FF      38       36 test_lsp_24
        27.85.194.125   27.85.194.127   Up       0  1 FF      43       41 test_lsp_25
        27.85.194.125   27.85.194.127   Up       0  1 FF      29       27 test_lsp_26
        27.85.194.125   27.85.194.127   Up       0  1 FF      44       42 test_lsp_27
        27.85.194.125   27.85.194.127   Up       0  1 FF      27       25 test_lsp_28
        27.85.194.125   27.85.194.127   Up       0  1 FF      25       23 test_lsp_29
        27.85.194.125   27.85.194.127   Up       0  1 FF      35       33 test_lsp_30
        Total 30 displayed, Up 30, Down 0"""}

    golden_parsed_output_1 = {
        'rsvp-session-information': {
            'rsvp-session-data': [{
            'session-type': 'Ingress',
            'count': '0',
            'display-count': '0',
            'up-count': '0',
            'down-count': '0'
            }, {
            'session-type': 'Egress',
            'count': '0',
            'display-count': '0',
            'up-count': '0',
            'down-count': '0'
            }, {
            'session-type': 'Transit',
            'count': '30',
            'rsvp-session': [{
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '46',
                'label-out': '44',
                'name': 'test_lsp_01'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '37',
                'label-out': '35',
                'name': 'test_lsp_02'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '28',
                'label-out': '26',
                'name': 'test_lsp_03'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '20',
                'label-out': '18',
                'name': 'test_lsp_04'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '26',
                'label-out': '24',
                'name': 'test_lsp_05'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '30',
                'label-out': '28',
                'name': 'test_lsp_06'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '19',
                'label-out': '17',
                'name': 'test_lsp_07'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '21',
                'label-out': '19',
                'name': 'test_lsp_08'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '39',
                'label-out': '37',
                'name': 'test_lsp_09'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '45',
                'label-out': '43',
                'name': 'test_lsp_10'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '23',
                'label-out': '21',
                'name': 'test_lsp_11'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '36',
                'label-out': '34',
                'name': 'test_lsp_12'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '42',
                'label-out': '40',
                'name': 'test_lsp_13'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '47',
                'label-out': '45',
                'name': 'test_lsp_14'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '18',
                'label-out': '16',
                'name': 'test_lsp_15'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '40',
                'label-out': '38',
                'name': 'test_lsp_16'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '22',
                'label-out': '20',
                'name': 'test_lsp_17'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '31',
                'label-out': '29',
                'name': 'test_lsp_18'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '41',
                'label-out': '39',
                'name': 'test_lsp_19'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '24',
                'label-out': '22',
                'name': 'test_lsp_20'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '32',
                'label-out': '30',
                'name': 'test_lsp_21'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '33',
                'label-out': '31',
                'name': 'test_lsp_22'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '34',
                'label-out': '32',
                'name': 'test_lsp_23'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '38',
                'label-out': '36',
                'name': 'test_lsp_24'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '43',
                'label-out': '41',
                'name': 'test_lsp_25'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '29',
                'label-out': '27',
                'name': 'test_lsp_26'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '44',
                'label-out': '42',
                'name': 'test_lsp_27'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '27',
                'label-out': '25',
                'name': 'test_lsp_28'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '25',
                'label-out': '23',
                'name': 'test_lsp_29'
            }, {
                'destination-address': '27.85.194.125',
                'source-address': '27.85.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '35',
                'label-out': '33',
                'name': 'test_lsp_30'
            }],
            'display-count': '30',
            'up-count': '30',
            'down-count': '0'
            }]
        }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRSVPSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowRSVPSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


if __name__ == '__main__':
    unittest.main()