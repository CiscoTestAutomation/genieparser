# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device, loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.junos.show_rsvp import (ShowRSVPNeighbor,
                                               ShowRSVPNeighborDetail,)


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

class test_show_rsvp_neighbor_detail(unittest.TestCase):
    device = Device(name='aName')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': """
        RSVP neighbor: 4 learned
        Address: 59.128.3.252 status: Down (Node neighbor)
        Last changed time: 27:54, Idle: 27:55 sec, Up cnt: 0, Down cnt: 0
        Message received: 0
        Hello: sent 187, received: 0, interval: 9 sec
        Remote instance: 0x0, Local instance: 0xf81317e
        Refresh reduction:  not operational
            Remote end: disabled, Ack-extension: disabled
        Enhanced FRR: Disabled

        Address: 106.187.14.240 status: Down (Node neighbor)
        Last changed time: 46:15, Idle: 46:15 sec, Up cnt: 0, Down cnt: 0
        Message received: 0
        Hello: sent 309, received: 0, interval: 9 sec
        Remote instance: 0x0, Local instance: 0x1a61c152
        Refresh reduction:  not operational
            Remote end: disabled, Ack-extension: disabled
        Enhanced FRR: Disabled

        Address: 106.187.14.157 via: ge-0/0/0.0 status: Up
        Last changed time: 46:15, Idle: 0 sec, Up cnt: 1, Down cnt: 0
        Message received: 695
        Hello: sent 310, received: 309, interval: 9 sec
        Remote instance: 0xe6740271, Local instance: 0xb6ab962a
        Refresh reduction:  operational
            Remote end: enabled, Ack-extension: enabled
        Enhanced FRR: Enabled
            LSPs (total 30): Phop 30, PPhop 0, Nhop 0, NNhop 0

        Address: 203.181.106.218 via: ge-0/0/1.1 status: Up
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
                'rsvp-neighbor-address': '59.128.3.252',
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
                'rsvp-neighbor-address': '106.187.14.240',
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
                'rsvp-neighbor-address': '106.187.14.157',
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
                'rsvp-neighbor-address': '203.181.106.218',
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

if __name__ == '__main__':
    unittest.main()