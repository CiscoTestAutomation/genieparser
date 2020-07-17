# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device, loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.junos.show_mpls import (
    ShowMPLSLSPNameDetail, ShowMPLSLSPNameExtensive)


class TestShowMPLSLSPNameDetail(unittest.TestCase):
    """ Unit test for:
        * show mpls lsp name {name} detail
    """
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {
        'execute.return_value':
        """Ingress LSP: 0 sessions
        Total 0 displayed, Up 0, Down 0

        Egress LSP: 0 sessions
        Total 0 displayed, Up 0, Down 0

        Transit LSP: 30 sessions

        10.49.194.125
        From: 10.49.194.127, LSPstate: Up, ActiveRoute: 0
        LSPname: test_lsp_01, LSPpath: Primary
        Suggested label received: -, Suggested label sent: -
        Recovery label received: -, Recovery label sent: 44
        Resv style: 1 FF, Label in: 46, Label out: 44
        Time left:  138, Since: Tue Jun 30 07:22:02 2020
        Tspec: rate 0bps size 0bps peak Infbps m 20 M 1500
        Port number: sender 1 receiver 50088 protocol 0
        PATH rcvfrom: 10.169.14.157 (ge-0/0/0.0) 1 pkts
        Adspec: received MTU 1500 sent MTU 1500
        PATH sentto: 192.168.145.218 (ge-0/0/1.1) 1 pkts
        RESV rcvfrom: 192.168.145.218 (ge-0/0/1.1) 1 pkts, Entropy label: Yes
        Explct route: 192.168.145.218 10.49.194.65 10.49.194.66
        10.49.194.123
        Record route: 10.49.194.2 10.169.14.157 <self> 192.168.145.218
        10.49.194.66 10.49.194.12
        255.255.255.255 10.4.1.1 10.1.8.8 10.64.64.64
        Total 1 displayed, Up 1, Down 0"""
    }

    golden_parsed_output_1 = {
        'mpls-lsp-information': {
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
                'rsvp-session': {
                    'destination-address':
                    '10.49.194.125',
                    'source-address':
                    '10.49.194.127',
                    'lsp-state':
                    'Up',
                    'route-count':
                    '0',
                    'name':
                    'test_lsp_01',
                    'lsp-path-type':
                    'Primary',
                    'suggested-label-in':
                    '-',
                    'suggested-label-out':
                    '-',
                    'recovery-label-in':
                    '-',
                    'recovery-label-out':
                    '44',
                    'rsb-count':
                    '1',
                    'resv-style':
                    'FF',
                    'label-in':
                    '46',
                    'label-out':
                    '44',
                    'psb-lifetime':
                    '138',
                    'psb-creation-time':
                    'Tue Jun 30 07:22:02 2020',
                    'sender-tspec':
                    'rate 0bps size 0bps peak Infbps m 20 M 1500',
                    'lsp-id':
                    '1',
                    'tunnel-id':
                    '50088',
                    'proto-id':
                    '0',
                    'packet-information': [{
                        'heading': 'PATH',
                        'previous-hop': '10.169.14.157',
                        'interface-name': '(ge-0/0/0.0)',
                        'count': '1'
                    }, {
                        'heading': 'PATH',
                        'next-hop': '192.168.145.218',
                        'interface-name': '(ge-0/0/1.1)',
                        'count': '1'
                    }, {
                        'heading': 'RESV',
                        'previous-hop': '192.168.145.218',
                        'interface-name': '(ge-0/0/1.1)',
                        'count': '1',
                        'entropy-label': 'Yes'
                    }],
                    'adspec':
                    'received MTU 1500 sent MTU 1500',
                    'explicit-route': {
                        'explicit-route-element': [{
                            'address': '192.168.145.218'
                        }, {
                            'address': '10.49.194.65'
                        }, {
                            'address': '10.49.194.66'
                        }, {
                            'address': '10.49.194.123'
                        }]
                    },
                    'record-route': {
                        'record-route-element': [{
                            'address': '10.49.194.2'
                        }, {
                            'address': '10.169.14.157'
                        }, {
                            'address': '<self>'
                        }, {
                            'address': '192.168.145.218'
                        }, {
                            'address': '10.49.194.66'
                        }, {
                            'address': '10.49.194.12'
                        }, {
                            'address': '255.255.255.255'
                        }, {
                            'address': '10.4.1.1'
                        }, {
                            'address': '10.1.8.8'
                        }, {
                            'address': '10.64.64.64'
                        }]
                    }
                },
                'display-count': '1',
                'up-count': '1',
                'down-count': '0'
            }]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMPLSLSPNameDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(name='test_lsp_01')

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowMPLSLSPNameDetail(device=self.device)
        parsed_output = obj.parse(name='test_lsp_01')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


class TestShowMPLSLSPNameExtensive(unittest.TestCase):
    """
    Unit test for:
        * show mpls lsp name {name} extensive
    """
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': '''
    Ingress LSP: 0 sessions
    Total 0 displayed, Up 0, Down 0

    Egress LSP: 0 sessions
    Total 0 displayed, Up 0, Down 0

    Transit LSP: 30 sessions

    10.49.194.125
      From: 10.49.194.127, LSPstate: Up, ActiveRoute: 0
      LSPname: test_lsp_01, LSPpath: Primary
      Suggested label received: -, Suggested label sent: -
      Recovery label received: -, Recovery label sent: 44
      Resv style: 1 FF, Label in: 46, Label out: 44
      Time left:  146, Since: Tue Jun 30 07:22:02 2020
      Tspec: rate 0bps size 0bps peak Infbps m 20 M 1500
      Port number: sender 1 receiver 50088 protocol 0
      Enhanced FRR: Disabled (Upstream), Reason: Compatibility, Refresh: 30 secs
      Enhanced FRR: Disabled (Downstream), Reason: Compatibility, Refresh: 30 secs
      PATH rcvfrom: 10.169.14.157 (ge-0/0/0.0) 1 pkts
           incoming message handle: P-8/1, Message ID: 23, Epoch: 385353
      Adspec: received MTU 1500 sent MTU 1500
      PATH sentto: 192.168.145.218 (ge-0/0/1.1) 1 pkts
           outgoing message state: refreshing, Message ID: 23, Epoch: 385318
      RESV rcvfrom: 192.168.145.218 (ge-0/0/1.1) 1 pkts, Entropy label: Yes
           incoming message handle: R-59/1, Message ID: 74, Epoch: 385436
      RESV
           outgoing message state: refreshing, Message ID: 74, Epoch: 385318
      Explct route: 192.168.145.218 10.49.194.65 10.49.194.66
      Record route: 10.49.194.2 10.169.14.157 <self> 192.168.145.218 10.49.194.66
    Total 1 displayed, Up 1, Down 0
    '''}

    golden_parsed_output_1 = {
        "mpls-lsp-information": {
            "rsvp-session-data": [
                {
                    "count": "0",
                    "display-count": "0",
                    "down-count": "0",
                    "session-type": "Ingress",
                    "up-count": "0"
                },
                {
                    "count": "0",
                    "display-count": "0",
                    "down-count": "0",
                    "session-type": "Egress",
                    "up-count": "0"
                },
                {
                    "count": "30",
                    "display-count": "1",
                    "down-count": "0",
                    "rsvp-session": {
                        "adspec": "received MTU 1500 sent MTU 1500",
                        "destination-address": "10.49.194.125",
                        "explicit-route": {
                            "explicit-route-element": [
                                {
                                    "address": "192.168.145.218"
                                },
                                {
                                    "address": "10.49.194.65"
                                },
                                {
                                    "address": "10.49.194.66"
                                }
                            ]
                        },
                        "label-in": "46",
                        "label-out": "44",
                        "lsp-id": "1",
                        "lsp-path-type": "Primary",
                        "lsp-state": "Up",
                        "name": "test_lsp_01",
                        "packet-information": [
                            {
                                'heading': 'PATH',
                                "count": "1",
                                "in-epoch": "385353",
                                "in-message-handle": "P-8/1",
                                "in-message-id": "23",
                                "interface-name": "ge-0/0/0.0",
                                "previous-hop": "10.169.14.157"
                            },
                            {
                                'heading': 'PATH',
                                "count": "1",
                                "interface-name": "ge-0/0/1.1",
                                "next-hop": "192.168.145.218",
                                "out-epoch": "385318",
                                "out-message-id": "23",
                                "out-message-state": "refreshing"
                            },
                            {
                                'heading': 'RESV',
                                "count": "1",
                                "entropy-label": "Yes",
                                "in-epoch": "385436",
                                "in-message-handle": "R-59/1",
                                "in-message-id": "74",
                                "interface-name": "ge-0/0/1.1",
                                "previous-hop": "192.168.145.218"
                            },
                            {
                                'heading': 'RESV',
                                "out-epoch": "385318",
                                "out-message-id": "74",
                                "out-message-state": "refreshing"
                            }
                        ],
                        "proto-id": "0",
                        "psb-creation-time": "Tue Jun 30 07:22:02 2020",
                        "psb-lifetime": "146",
                        "record-route": {
                            "address": [
                                "10.49.194.2",
                                "10.169.14.157",
                                "192.168.145.218",
                                "10.49.194.66"
                            ],
                        },
                        "recovery-label-in": "-",
                        "recovery-label-out": "44",
                        "resv-style": "FF",
                        "route-count": "0",
                        "rsb-count": "1",
                        "rsvp-lsp-enh-local-prot-downstream": {
                            "rsvp-lsp-enh-local-prot-refresh-interval": "30 secs",
                            "rsvp-lsp-enh-lp-downstream-status": "Disabled"
                        },
                        "rsvp-lsp-enh-local-prot-upstream": {
                            "rsvp-lsp-enh-local-prot-refresh-interval": "30 secs",
                            "rsvp-lsp-enh-lp-upstream-status": "Disabled"
                        },
                        "sender-tspec": "rate 0bps size 0bps peak Infbps m 20 M 1500",
                        "source-address": "10.49.194.127",
                        "suggested-label-in": "-",
                        "suggested-label-out": "-",
                        "tunnel-id": "50088"
                    },
                    "session-type": "Transit",
                    "up-count": "1"
                }
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMPLSLSPNameExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(name='test_lsp_01')

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowMPLSLSPNameExtensive(device=self.device)
        parsed_output = obj.parse(name='test_lsp_01')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


if __name__ == '__main__':
    unittest.main()
