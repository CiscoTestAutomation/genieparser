# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device, loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.junos.show_rsvp import (ShowRSVPNeighbor,
                                               ShowRSVPNeighborDetail,
                                               ShowRSVPSession,
                                               )


class TestShowRSVPNeighbor(unittest.TestCase):
    device = Device(name='aName')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': """
    show rsvp neighbor
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

class TestShowRSVPNeighborDetail(unittest.TestCase):
    device = Device(name='aName')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': """
        show rsvp neighbor detail
        RSVP neighbor: 4 learned
        Address: 10.34.3.252 status: Down (Node neighbor)
        Last changed time: 27:54, Idle: 27:55 sec, Up cnt: 0, Down cnt: 0
        Message received: 0
        Hello: sent 187, received: 0, interval: 9 sec
        Remote instance: 0x0, Local instance: 0xf81317e
        Refresh reduction:  not operational
            Remote end: disabled, Ack-extension: disabled
        Enhanced FRR: Disabled

        Address: 10.169.14.240 status: Down (Node neighbor)
        Last changed time: 46:15, Idle: 46:15 sec, Up cnt: 0, Down cnt: 0
        Message received: 0
        Hello: sent 309, received: 0, interval: 9 sec
        Remote instance: 0x0, Local instance: 0x1a61c152
        Refresh reduction:  not operational
            Remote end: disabled, Ack-extension: disabled
        Enhanced FRR: Disabled

        Address: 10.169.14.157 via: ge-0/0/0.0 status: Up
        Last changed time: 46:15, Idle: 0 sec, Up cnt: 1, Down cnt: 0
        Message received: 695
        Hello: sent 310, received: 309, interval: 9 sec
        Remote instance: 0xe6740271, Local instance: 0xb6ab962a
        Refresh reduction:  operational
            Remote end: enabled, Ack-extension: enabled
        Enhanced FRR: Enabled
            LSPs (total 30): Phop 30, PPhop 0, Nhop 0, NNhop 0

        Address: 192.168.145.218 via: ge-0/0/1.1 status: Up
        Last changed time: 27:57, Idle: 0 sec, Up cnt: 1, Down cnt: 0
        Message received: 557
        Hello: sent 183, received: 183, interval: 9 sec
        Remote instance: 0xa1a75540, Local instance: 0x41ad0a42
        Refresh reduction:  operational
            Remote end: enabled, Ack-extension: enabled
        Enhanced FRR: Enabled
            LSPs (total 30): Phop 0, PPhop 0, Nhop 30, NNhop 0"""}

    golden_parsed_output_1 = {
        'rsvp-neighbor-information': {
            'rsvp-neighbor': [{
                'hello-interval': '9',
                'hellos-received': '0',
                'hellos-sent': '187',
                'last-changed-time': '27:54',
                'messages-received': '0',
                'neighbor-down-count': '0',
                'neighbor-idle': '27:55',
                'neighbor-up-count': '0',
                'rsvp-nbr-enh-local-protection': {
                'rsvp-nbr-enh-lp-status': 'Disabled'
                },
                'rsvp-neighbor-address': '10.34.3.252',
                'rsvp-neighbor-local-instance': '0xf81317e',
                'rsvp-neighbor-node': True,
                'rsvp-neighbor-remote-instance': '0x0',
                'rsvp-neighbor-status': 'Down',
                'rsvp-refresh-reduct-ack-status': 'disabled',
                'rsvp-refresh-reduct-remote-status': 'disabled',
                'rsvp-refresh-reduct-status': 'not '
                'operational'
            },
            {
                'hello-interval': '9',
                'hellos-received': '0',
                'hellos-sent': '309',
                'last-changed-time': '46:15',
                'messages-received': '0',
                'neighbor-down-count': '0',
                'neighbor-idle': '46:15',
                'neighbor-up-count': '0',
                'rsvp-nbr-enh-local-protection': {
                'rsvp-nbr-enh-lp-status': 'Disabled'
                },
                'rsvp-neighbor-address': '10.169.14.240',
                'rsvp-neighbor-local-instance': '0x1a61c152',
                'rsvp-neighbor-node': True,
                'rsvp-neighbor-remote-instance': '0x0',
                'rsvp-neighbor-status': 'Down',
                'rsvp-refresh-reduct-ack-status': 'disabled',
                'rsvp-refresh-reduct-remote-status': 'disabled',
                'rsvp-refresh-reduct-status': 'not '
                'operational'
            },
            {
                'hello-interval': '9',
                'hellos-received': '309',
                'hellos-sent': '310',
                'last-changed-time': '46:15',
                'messages-received': '695',
                'neighbor-down-count': '0',
                'neighbor-idle': '0',
                'neighbor-up-count': '1',
                'rsvp-nbr-enh-local-protection': {
                'rsvp-nbr-enh-lp-nhop-lsp-count': '0',
                'rsvp-nbr-enh-lp-nnhop-lsp-count': '0',
                'rsvp-nbr-enh-lp-phop-lsp-count': '30',
                'rsvp-nbr-enh-lp-pphop-lsp-count': '0',
                'rsvp-nbr-enh-lp-status': 'Enabled',
                'rsvp-nbr-enh-lp-total-lsp-count': '30'
                },
                'rsvp-neighbor-address': '10.169.14.157',
                'rsvp-neighbor-interface': 'ge-0/0/0.0',
                'rsvp-neighbor-local-instance': '0xb6ab962a',
                'rsvp-neighbor-node': True,
                'rsvp-neighbor-remote-instance': '0xe6740271',
                'rsvp-neighbor-status': 'Up',
                'rsvp-refresh-reduct-ack-status': 'enabled',
                'rsvp-refresh-reduct-remote-status': 'enabled',
                'rsvp-refresh-reduct-status': 'operational'
            },
            {
                'hello-interval': '9',
                'hellos-received': '183',
                'hellos-sent': '183',
                'last-changed-time': '27:57',
                'messages-received': '557',
                'neighbor-down-count': '0',
                'neighbor-idle': '0',
                'neighbor-up-count': '1',
                'rsvp-nbr-enh-local-protection': {
                'rsvp-nbr-enh-lp-nhop-lsp-count': '30',
                'rsvp-nbr-enh-lp-nnhop-lsp-count': '0',
                'rsvp-nbr-enh-lp-phop-lsp-count': '0',
                'rsvp-nbr-enh-lp-pphop-lsp-count': '0',
                'rsvp-nbr-enh-lp-status': 'Enabled',
                'rsvp-nbr-enh-lp-total-lsp-count': '30'
                },
                'rsvp-neighbor-address': '192.168.145.218',
                'rsvp-neighbor-interface': 'ge-0/0/1.1',
                'rsvp-neighbor-local-instance': '0x41ad0a42',
                'rsvp-neighbor-node': True,
                'rsvp-neighbor-remote-instance': '0xa1a75540',
                'rsvp-neighbor-status': 'Up',
                'rsvp-refresh-reduct-ack-status': 'enabled',
                'rsvp-refresh-reduct-remote-status': 'enabled',
                'rsvp-refresh-reduct-status': 'operational'
            }
            ],
            'rsvp-neighbor-count': '4'
        }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRSVPNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowRSVPNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

class TestShowRSVPSession(unittest.TestCase):
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
        10.49.194.125   10.49.194.127   Up       0  1 FF      46       44 test_lsp_01
        10.49.194.125   10.49.194.127   Up       0  1 FF      37       35 test_lsp_02
        10.49.194.125   10.49.194.127   Up       0  1 FF      28       26 test_lsp_03
        10.49.194.125   10.49.194.127   Up       0  1 FF      20       18 test_lsp_04
        10.49.194.125   10.49.194.127   Up       0  1 FF      26       24 test_lsp_05
        10.49.194.125   10.49.194.127   Up       0  1 FF      30       28 test_lsp_06
        10.49.194.125   10.49.194.127   Up       0  1 FF      19       17 test_lsp_07
        10.49.194.125   10.49.194.127   Up       0  1 FF      21       19 test_lsp_08
        10.49.194.125   10.49.194.127   Up       0  1 FF      39       37 test_lsp_09
        10.49.194.125   10.49.194.127   Up       0  1 FF      45       43 test_lsp_10
        10.49.194.125   10.49.194.127   Up       0  1 FF      23       21 test_lsp_11
        10.49.194.125   10.49.194.127   Up       0  1 FF      36       34 test_lsp_12
        10.49.194.125   10.49.194.127   Up       0  1 FF      42       40 test_lsp_13
        10.49.194.125   10.49.194.127   Up       0  1 FF      47       45 test_lsp_14
        10.49.194.125   10.49.194.127   Up       0  1 FF      18       16 test_lsp_15
        10.49.194.125   10.49.194.127   Up       0  1 FF      40       38 test_lsp_16
        10.49.194.125   10.49.194.127   Up       0  1 FF      22       20 test_lsp_17
        10.49.194.125   10.49.194.127   Up       0  1 FF      31       29 test_lsp_18
        10.49.194.125   10.49.194.127   Up       0  1 FF      41       39 test_lsp_19
        10.49.194.125   10.49.194.127   Up       0  1 FF      24       22 test_lsp_20
        10.49.194.125   10.49.194.127   Up       0  1 FF      32       30 test_lsp_21
        10.49.194.125   10.49.194.127   Up       0  1 FF      33       31 test_lsp_22
        10.49.194.125   10.49.194.127   Up       0  1 FF      34       32 test_lsp_23
        10.49.194.125   10.49.194.127   Up       0  1 FF      38       36 test_lsp_24
        10.49.194.125   10.49.194.127   Up       0  1 FF      43       41 test_lsp_25
        10.49.194.125   10.49.194.127   Up       0  1 FF      29       27 test_lsp_26
        10.49.194.125   10.49.194.127   Up       0  1 FF      44       42 test_lsp_27
        10.49.194.125   10.49.194.127   Up       0  1 FF      27       25 test_lsp_28
        10.49.194.125   10.49.194.127   Up       0  1 FF      25       23 test_lsp_29
        10.49.194.125   10.49.194.127   Up       0  1 FF      35       33 test_lsp_30
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
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '46',
                'label-out': '44',
                'name': 'test_lsp_01'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '37',
                'label-out': '35',
                'name': 'test_lsp_02'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '28',
                'label-out': '26',
                'name': 'test_lsp_03'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '20',
                'label-out': '18',
                'name': 'test_lsp_04'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '26',
                'label-out': '24',
                'name': 'test_lsp_05'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '30',
                'label-out': '28',
                'name': 'test_lsp_06'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '19',
                'label-out': '17',
                'name': 'test_lsp_07'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '21',
                'label-out': '19',
                'name': 'test_lsp_08'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '39',
                'label-out': '37',
                'name': 'test_lsp_09'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '45',
                'label-out': '43',
                'name': 'test_lsp_10'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '23',
                'label-out': '21',
                'name': 'test_lsp_11'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '36',
                'label-out': '34',
                'name': 'test_lsp_12'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '42',
                'label-out': '40',
                'name': 'test_lsp_13'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '47',
                'label-out': '45',
                'name': 'test_lsp_14'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '18',
                'label-out': '16',
                'name': 'test_lsp_15'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '40',
                'label-out': '38',
                'name': 'test_lsp_16'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '22',
                'label-out': '20',
                'name': 'test_lsp_17'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '31',
                'label-out': '29',
                'name': 'test_lsp_18'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '41',
                'label-out': '39',
                'name': 'test_lsp_19'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '24',
                'label-out': '22',
                'name': 'test_lsp_20'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '32',
                'label-out': '30',
                'name': 'test_lsp_21'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '33',
                'label-out': '31',
                'name': 'test_lsp_22'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '34',
                'label-out': '32',
                'name': 'test_lsp_23'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '38',
                'label-out': '36',
                'name': 'test_lsp_24'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '43',
                'label-out': '41',
                'name': 'test_lsp_25'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '29',
                'label-out': '27',
                'name': 'test_lsp_26'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '44',
                'label-out': '42',
                'name': 'test_lsp_27'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '27',
                'label-out': '25',
                'name': 'test_lsp_28'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
                'lsp-state': 'Up',
                'route-count': '0',
                'rsb-count': '1',
                'resv-style': 'FF',
                'label-in': '25',
                'label-out': '23',
                'name': 'test_lsp_29'
            }, {
                'destination-address': '10.49.194.125',
                'source-address': '10.49.194.127',
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