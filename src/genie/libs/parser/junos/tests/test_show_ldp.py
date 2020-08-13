# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_ldp import (ShowLDPSession,
                                             ShowLdpNeighbor,
                                             ShowLdpSessionIpaddressDetail,
                                             ShowLdpDatabaseSessionIpaddress,
                                             ShowLDPInterface,ShowLDPInterfaceDetail,
                                             ShowLDPOverview)


# =================================
# Unit test for 'show ldp session'
# =================================
class TestShowLDPSession(unittest.TestCase):
    '''unit test for "show ldp session'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'ldp-session-information': {
            'ldp-session': [{
                'ldp-neighbor-address': '10.34.2.250',
                'ldp-session-state': 'Operational',
                'ldp-connection-state': 'Open',
                'ldp-remaining-time': '26',
                'ldp-session-adv-mode': 'DU'
            }]
        }
    }

    golden_output = {
        'execute.return_value':
        '''
          Address                           State       Connection  Hold time  Adv. Mode
        10.34.2.250                        Operational Open          26         DU
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLDPSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLDPSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# =================================
# Unit test for 'show ldp neighbor'
# =================================
class TestShowLdpNeighbor(unittest.TestCase):
    '''unit test for "show ldp neighbor '''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'ldp-neighbor-information':
        {'ldp-neighbor': [
            {'interface-name': 'ge-0/0/0.0',
             'ldp-label-space-id': '10.34.2.250:0',
             'ldp-neighbor-address': '10.169.14.158',
             'ldp-remaining-time': '14'
             }
        ]
        }
    }

    golden_output = {
        'execute.return_value':
        '''
          show ldp neighbor
        Address                             Interface       Label space ID     Hold time
        10.169.14.158                      ge-0/0/0.0      10.34.2.250:0       14
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLdpNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLdpNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# =================================
# Unit test for 'show ldp database session ipaddress'
# =================================
class TestShowLdpDatabaseSessionIpaddress(unittest.TestCase):
    '''unit test for "show ldp database session ipaddress'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "ldp-database-information": {
            "ldp-database": [
                {
                    "ldp-binding": [
                        {
                            "ldp-label": "3",
                            "ldp-prefix": "10.34.2.250/32"
                        },
                        {
                            "ldp-label": "16",
                            "ldp-prefix": "10.169.14.240/32"
                        }
                    ],
                    "ldp-database-type": "Input label database",
                    "ldp-label-received": "2",
                    "ldp-session-id": "10.169.14.240:0--10.34.2.250:0"
                },
                {
                    "ldp-binding": [
                        {
                            "ldp-label": "16",
                            "ldp-prefix": "10.34.2.250/32"
                        },
                        {
                            "ldp-label": "3",
                            "ldp-prefix": "10.169.14.240/32"
                        }
                    ],
                    "ldp-database-type": "Output label database",
                    "ldp-label-advertised": "2",
                    "ldp-session-id": "10.169.14.240:0--10.34.2.250:0"
                }
            ]
        }
    }

    golden_output = {
        'execute.return_value':
        '''
          show ldp database 10.34.2.250 
        Input label database, 10.169.14.240:0--10.34.2.250:0
        Labels received: 2
        Label     Prefix
            3      10.34.2.250/32
            16      10.169.14.240/32

        Output label database, 10.169.14.240:0--10.34.2.250:0
        Labels advertised: 2
        Label     Prefix
            16      10.34.2.250/32
            3      10.169.14.240/32
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLdpDatabaseSessionIpaddress(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLdpDatabaseSessionIpaddress(device=self.device)
        parsed_output = obj.parse(ipaddress='10.34.2.250')
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ===============================================
# Unit test for 'show ldp interface {interface}'
# ===============================================


class TestShowLDPInterface(unittest.TestCase):
    '''unit test for "show ldp interface {interface}'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "ldp-interface-information": {
            "ldp-interface": {
                "interface-name": "ge-0/0/0.0",
                "ldp-interface-local-address": "10.1.2.2",
                "ldp-label-space-id": "100.2.14.100:0",
                "ldp-neighbor-count": "1",
                "ldp-next-hello": "3"
            }
        }
    }

    golden_output = {
        'execute.return_value':
        '''
            show ldp interface ge-0/0/0.0
            Interface          Address                          Label space ID   Nbr   Next
                                                                                count  hello
            ge-0/0/0.0         10.1.2.2                   100.2.14.100:0  1      3
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLDPInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(interface='ge-0/0/0.0')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLDPInterface(device=self.device)
        parsed_output = obj.parse(interface='ge-0/0/0.0')
        self.assertEqual(parsed_output, self.golden_parsed_output)

# =====================================================
# Unit test for 'show ldp interface {interface} detail'
# =====================================================


class TestShowLDPInterfaceDetail(unittest.TestCase):
    '''unit test for "show ldp interface {interface} detail'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "ldp-interface-information": {
            "ldp-interface": {
                "interface-name": "ge-0/0/0.0",
                "ldp-interface-local-address": "10.1.2.2",
                "ldp-label-space-id": "100.2.14.100:0",
                "ldp-neighbor-count": "1",
                "ldp-next-hello": "1",
                "ldp-transport-address": "100.2.14.100",
                "ldp-hello-interval": "5",
                "ldp-holdtime": "15",
            }
        }
    }

    golden_output = {
        'execute.return_value':
        '''
            show ldp interface ge-0/0/0.0 detail
            Interface          Address                          Label space ID   Nbr   Next
                                                                                count  hello
            ge-0/0/0.0         10.1.2.2                   100.2.14.100:0  1      1
            Hello interval: 5, Hold time: 15, Transport address: 100.2.14.100
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLDPInterfaceDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(interface='ge-0/0/0.0')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLDPInterfaceDetail(device=self.device)
        parsed_output = obj.parse(interface='ge-0/0/0.0')
        self.assertEqual(parsed_output, self.golden_parsed_output)

# =================================
# Unit test for 'show ldp overview'
# =================================


class TestShowLDPOverview(unittest.TestCase):
    '''unit test for "show ldp overview'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ldp overview
        Instance: master
        Reference count: 2
        Router ID: 100.2.14.100
        LDP inet: enabled
        Transport preference: IPv4
        Message id: 4
        Configuration sequence: 1
        Deaggregate: disabled
        Explicit null: disabled
        IPv6 tunneling: disabled
        Strict targeted hellos: disabled
        Loopback if added: no
        Route preference: 9
        Unicast transit LSP chaining: disabled
        P2MP transit LSP chaining: disabled
        Transit LSP statistics based on route statistics: disabled
        LDP route acknowledgement: enabled
        BGP export: enabled
        LDP mtu discovery: disabled
        LDP SR Mapping Client: disabled
        Capabilities enabled: none
        Egress FEC capabilities enabled: entropy-label-capability
        Downstream unsolicited Sessions:
            Operational: 1
            Retention: liberal
            Control: ordered
        Auto targeted sessions:
            Auto targeted: disabled
            Dynamic tunnel session count: 0
        P2MP:
            Recursive route: disabled
            No rsvp tunneling: disabled
        Timers:
            Keepalive interval: 10, Keepalive timeout: 30
            Link hello interval: 5, Link hello hold time: 15
            Targeted hello interval: 15, Targeted hello hold time: 45
            Label withdraw delay: 60, Make before break timeout: 30
            Make before break switchover delay: 3
            Link protection timeout: 120
        Graceful restart:
            Restart: disabled, Helper: enabled, Restart in process: false
            Reconnect time: 60000, Max neighbor reconnect time: 120000
            Recovery time: 160000, Max neighbor recovery time: 240000
        Traffic Engineering:
            Bgp igp: disabled
            Both ribs: disabled
            Mpls forwarding: disabled
        IGP:
            Tracking igp metric: disabled
            Sync session up delay: 10
        Session protection:
            Session protection: disabled
            Session protection timeout: 0
        Interface addresses advertising:
            10.1.2.2
        LDP Job:
            Read job time quantum: 1000, Write job time quantum: 1000
            Read job loop quantum: 100, Write job loop quantum: 100
            Backup inbound read job time quantum: 1000, Backup outbound read job time quantum: 1000
            Backup inbound read job loop quantum: 100, Backup outbound read job loop quantum: 100
        Label allocation:
            Current number of LDP labels allocated: 1
            Total number of LDP labels allocated: 1
            Total number of LDP labels freed: 0
            Total number of LDP label allocation failure: 0
            Current number of labels allocated by all protocols: 0
    '''}

    golden_parsed_output = {
        'ldp-overview-information': {
            'ldp-overview': {
                'ldp-auto-targeted-session': {
                    'ldp-auto-targeted-dyn-tun-ses-count': 0,
                    'ldp-auto-targeted-session-enabled': 'disabled'
                },
                'ldp-bgp-export': 'enabled',
                'ldp-configuration-sequence': 1,
                'ldp-deaggregate': 'disabled',
                'ldp-explicit-null': 'disabled',
                'ldp-gr-overview': {
                    'ldp-gr-helper': 'enabled',
                    'ldp-gr-max-neighbor-reconnect-time': 120000,
                    'ldp-gr-max-neighbor-recovery-time': 240000,
                    'ldp-gr-reconnect-time': 60000,
                    'ldp-gr-recovery-time': 160000,
                    'ldp-gr-restart': 'disabled',
                    'ldp-gr-restarting': 'false'
                },
                'ldp-igp-overview': {
                    'ldp-igp-sync-session-up-delay': 10,
                    'ldp-tracking-igp-metric': 'disabled'
                },
                'ldp-inet': 'enabled',
                'ldp-instance-capability': {
                    'ldp-capability': 'none'
                },
                'ldp-instance-egress-fec-capability': {
                    'ldp-egress-fec-capability': 'entropy-label-capability'
                },
                'ldp-instance-name': 'master',
                'ldp-interface-address': {
                    'interface-address': '10.1.2.2'
                },
                'ldp-ipv6-tunneling': 'disabled',
                'ldp-job-overview': {
                    'ldp-inbound-read-job-loop-quantum': 100,
                    'ldp-inbound-read-job-time-quantum': 1000,
                    'ldp-outbound-read-job-loop-quantum': 100,
                    'ldp-outbound-read-job-time-quantum': 1000,
                    'ldp-read-job-loop-quantum': 100,
                    'ldp-read-job-time-quantum': 1000,
                    'ldp-write-job-loop-quantum': 100,
                    'ldp-write-job-time-quantum': 1000
                },
                'ldp-label-allocation': {
                    'ldp-global-label-current-allocs': 0,
                    'ldp-label-alloc-failure': 0,
                    'ldp-label-current-allocs': 1,
                    'ldp-label-total-allocs': 1,
                    'ldp-label-total-frees': 0
                },
                'ldp-loopback-if-added': 'no',
                'ldp-message-id': 4,
                'ldp-mtu-discovery': 'disabled',
                'ldp-p2mp': {
                    'ldp-p2mp-no-rsvp-tunneling-enabled': 'disabled',
                    'ldp-p2mp-recursive-route-enabled': 'disabled'
                },
                'ldp-p2mp-transit-lsp-chaining': 'disabled',
                'ldp-reference-count': 2,
                'ldp-route-acknowledgement': 'enabled',
                'ldp-route-preference': 9,
                'ldp-router-id': '100.2.14.100',
                'ldp-session-count': {
                    'ldp-control-mode': 'ordered',
                    'ldp-retention-mode': 'liberal',
                    'ldp-session-operational': 1
                },
                'ldp-session-protect-overview': {
                    'ldp-session-protect': 'disabled',
                    'ldp-session-protect-timeout': 0
                },
                'ldp-sr-mapping-client': 'disabled',
                'ldp-strict-targeted-hellos': 'disabled',
                'ldp-te-overview': {
                    'ldp-te-bgp-igp': 'disabled',
                    'ldp-te-both-ribs': 'disabled',
                    'ldp-te-mpls-forwarding': 'disabled'
                },
                'ldp-timer-overview': {
                    'ldp-instance-keepalive-interval': 10,
                    'ldp-instance-keepalive-timeout': 30,
                    'ldp-instance-label-withdraw-delay': 60,
                    'ldp-instance-link-hello-hold-time': 15,
                    'ldp-instance-link-hello-interval': 5,
                    'ldp-instance-link-protection-timeout': 120,
                    'ldp-instance-make-before-break-switchover-delay': 3,
                    'ldp-instance-make-before-break-timeout': 30,
                    'ldp-instance-targeted-hello-hold-time': 45,
                    'ldp-instance-targeted-hello-interval': 15
                },
                'ldp-transit-lsp-route-stats': 'disabled',
                'ldp-transport-preference': 'IPv4',
                'ldp-unicast-transit-lsp-chaining': 'disabled'
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
        show ldp overview 
        Instance: master
        Router ID: 100.2.14.100
        Message id: 345
        Configuration sequence: 1
        Deaggregate: disabled
        Explicit null: disabled
        IPv6 tunneling: disabled
        Strict targeted hellos: disabled
        Loopback if added: no
        Route preference: 9
        Unicast transit LSP chaining: disabled
        P2MP transit LSP chaining: disabled
        Transit LSP statistics based on route statistics: disabled
        Capabilities enabled: none
        Protocol modes:
            Distribution: unsolicited
            Retention: liberal
            Control: ordered
        Sessions:
            Operational: 1
        Timers:
            Keepalive interval: 10, Keepalive timeout: 30
            Link hello interval: 5, Link hello hold time: 15
            Targeted hello interval: 15, Targeted hello hold time: 45
            Label withdraw delay: 60
        Graceful restart:
            Restart: enabled, Helper: enabled, Restart in process: false
            Reconnect time: 60000, Max neighbor reconnect time: 120000
            Recovery time: 160000, Max neighbor recovery time: 240000
        Traffic Engineering:
            Bgp igp: disabled
            Both ribs: disabled
            Mpls forwarding: disabled
        IGP:
            Tracking igp metric: disabled
            Sync session up delay: 10
        Session protection:
            Session protection: disabled
            Session protecton timeout: 0
        Interface addresses advertising:
            10.1.2.2
    '''}

    golden_parsed_output_2 = {
        'ldp-overview-information': {
            'ldp-overview': {
                'ldp-configuration-sequence': 1,
                'ldp-deaggregate': 'disabled',
                'ldp-explicit-null': 'disabled',
                'ldp-gr-overview': {
                    'ldp-gr-helper': 'enabled',
                    'ldp-gr-max-neighbor-reconnect-time': 120000,
                    'ldp-gr-max-neighbor-recovery-time': 240000,
                    'ldp-gr-reconnect-time': 60000,
                    'ldp-gr-recovery-time': 160000,
                    'ldp-gr-restart': 'enabled',
                    'ldp-gr-restarting': 'false'
                },
                'ldp-igp-overview': {
                    'ldp-igp-sync-session-up-delay': 10,
                    'ldp-tracking-igp-metric': 'disabled'
                },
                'ldp-instance-capability': {
                    'ldp-capability': 'none'
                },
                'ldp-instance-name': 'master',
                'ldp-interface-address': {
                    'interface-address': '10.1.2.2'
                },
                'ldp-ipv6-tunneling': 'disabled',
                'ldp-loopback-if-added': 'no',
                'ldp-message-id': 345,
                'ldp-p2mp-transit-lsp-chaining': 'disabled',
                'ldp-protocol-modes': {
                    'ldp-control-mode': 'ordered',
                    'ldp-distribution-mode': 'unsolicited',
                    'ldp-retention-mode': 'liberal'
                },
                'ldp-route-preference': 9,
                'ldp-router-id': '100.2.14.100',
                'ldp-session-count': {
                    'ldp-session-operational': 1
                },
                'ldp-session-protect-overview': {
                    'ldp-session-protect': 'disabled',
                    'ldp-session-protect-timeout': 0
                },
                'ldp-strict-targeted-hellos': 'disabled',
                'ldp-te-overview': {
                    'ldp-te-bgp-igp': 'disabled',
                    'ldp-te-both-ribs': 'disabled',
                    'ldp-te-mpls-forwarding': 'disabled'
                },
                'ldp-timer-overview': {
                    'ldp-instance-keepalive-interval': 10,
                    'ldp-instance-keepalive-timeout': 30,
                    'ldp-instance-label-withdraw-delay': 60,
                    'ldp-instance-link-hello-hold-time': 15,
                    'ldp-instance-link-hello-interval': 5,
                    'ldp-instance-targeted-hello-hold-time': 45,
                    'ldp-instance-targeted-hello-interval': 15
                },
                'ldp-transit-lsp-route-stats': 'disabled',
                'ldp-unicast-transit-lsp-chaining': 'disabled'
            }
        }
    }

    golden_output_3 = {'execute.return_value': '''
        show ldp overview 
        Instance: master
        Reference count: 2
        Router ID: 100.2.14.100
        LDP inet: enabled
        Transport preference: IPv4
        Message id: 4
        Configuration sequence: 1
        Deaggregate: disabled
        Explicit null: disabled
        IPv6 tunneling: disabled
        Strict targeted hellos: disabled
        Loopback if added: no
        Route preference: 9
        Unicast transit LSP chaining: disabled
        P2MP transit LSP chaining: disabled
        Transit LSP statistics based on route statistics: disabled
        LDP route acknowledgement: enabled
        BGP export: enabled
        LDP mtu discovery: disabled
        LDP SR Mapping Client: disabled
        Capabilities enabled: none
        Egress FEC capabilities enabled: entropy-label-capability
        Downstream unsolicited Sessions:
            Operational: 1
            Retention: liberal
            Control: ordered
        Auto targeted sessions:
            Auto targeted: disabled
            Dynamic tunnel session count: 0
        P2MP:
            Recursive route: disabled
            No rsvp tunneling: disabled
        Timers:
            Keepalive interval: 10, Keepalive timeout: 30
            Link hello interval: 5, Link hello hold time: 15
            Targeted hello interval: 15, Targeted hello hold time: 45
            Label withdraw delay: 60, Make before break timeout: 30
            Make before break switchover delay: 3
            Link protection timeout: 120
        Graceful restart:
            Restart: disabled, Helper: enabled, Restart in process: false
            Reconnect time: 60000, Max neighbor reconnect time: 120000
            Recovery time: 160000, Max neighbor recovery time: 240000
        Traffic Engineering:
            Bgp igp: disabled
            Both ribs: disabled
            Mpls forwarding: disabled
        IGP:
            Tracking igp metric: disabled
            Sync session up delay: 10
        Session protection:
            Session protection: disabled
            Session protection timeout: 0
        Interface addresses advertising:
            10.1.2.2
        LDP Job:
            Read job time quantum: 1000, Write job time quantum: 1000
            Read job loop quantum: 100, Write job loop quantum: 100
            Backup inbound read job time quantum: 1000, Backup outbound read job time quantum: 1000
            Backup inbound read job loop quantum: 100, Backup outbound read job loop quantum: 100
        Label allocation:
            Current number of LDP labels allocated: 1
            Total number of LDP labels allocated: 1
            Total number of LDP labels freed: 0
            Total number of LDP label allocation failure: 0
            Current number of labels allocated by all protocols: 0    
    '''}

    golden_parsed_output_3 = {
        'ldp-overview-information': {
            'ldp-overview': {
                'ldp-auto-targeted-session': {
                    'ldp-auto-targeted-dyn-tun-ses-count': 0,
                    'ldp-auto-targeted-session-enabled': 'disabled'
                },
                'ldp-bgp-export': 'enabled',
                'ldp-configuration-sequence': 1,
                'ldp-deaggregate': 'disabled',
                'ldp-explicit-null': 'disabled',
                'ldp-gr-overview': {
                    'ldp-gr-helper': 'enabled',
                    'ldp-gr-max-neighbor-reconnect-time': 120000,
                    'ldp-gr-max-neighbor-recovery-time': 240000,
                    'ldp-gr-reconnect-time': 60000,
                    'ldp-gr-recovery-time': 160000,
                    'ldp-gr-restart': 'disabled',
                    'ldp-gr-restarting': 'false'
                },
                'ldp-igp-overview': {
                    'ldp-igp-sync-session-up-delay': 10,
                    'ldp-tracking-igp-metric': 'disabled'
                },
                'ldp-inet': 'enabled',
                'ldp-instance-capability': {
                    'ldp-capability': 'none'
                },
                'ldp-instance-egress-fec-capability': {
                    'ldp-egress-fec-capability': 'entropy-label-capability'
                },
                'ldp-instance-name': 'master',
                'ldp-interface-address': {
                    'interface-address': '10.1.2.2'
                },
                'ldp-ipv6-tunneling': 'disabled',
                'ldp-job-overview': {
                    'ldp-inbound-read-job-loop-quantum': 100,
                    'ldp-inbound-read-job-time-quantum': 1000,
                    'ldp-outbound-read-job-loop-quantum': 100,
                    'ldp-outbound-read-job-time-quantum': 1000,
                    'ldp-read-job-loop-quantum': 100,
                    'ldp-read-job-time-quantum': 1000,
                    'ldp-write-job-loop-quantum': 100,
                    'ldp-write-job-time-quantum': 1000
                },
                'ldp-label-allocation': {
                    'ldp-global-label-current-allocs': 0,
                    'ldp-label-alloc-failure': 0,
                    'ldp-label-current-allocs': 1,
                    'ldp-label-total-allocs': 1,
                    'ldp-label-total-frees': 0
                },
                'ldp-loopback-if-added': 'no',
                'ldp-message-id': 4,
                'ldp-mtu-discovery': 'disabled',
                'ldp-p2mp': {
                    'ldp-p2mp-no-rsvp-tunneling-enabled': 'disabled',
                    'ldp-p2mp-recursive-route-enabled': 'disabled'
                },
                'ldp-p2mp-transit-lsp-chaining': 'disabled',
                'ldp-reference-count': 2,
                'ldp-route-acknowledgement': 'enabled',
                'ldp-route-preference': 9,
                'ldp-router-id': '100.2.14.100',
                'ldp-session-count': {
                    'ldp-control-mode': 'ordered',
                    'ldp-retention-mode': 'liberal',
                    'ldp-session-operational': 1
                },
                'ldp-session-protect-overview': {
                    'ldp-session-protect': 'disabled',
                    'ldp-session-protect-timeout': 0
                },
                'ldp-sr-mapping-client': 'disabled',
                'ldp-strict-targeted-hellos': 'disabled',
                'ldp-te-overview': {
                    'ldp-te-bgp-igp': 'disabled',
                    'ldp-te-both-ribs': 'disabled',
                    'ldp-te-mpls-forwarding': 'disabled'
                },
                'ldp-timer-overview': {
                    'ldp-instance-keepalive-interval': 10,
                    'ldp-instance-keepalive-timeout': 30,
                    'ldp-instance-label-withdraw-delay': 60,
                    'ldp-instance-link-hello-hold-time': 15,
                    'ldp-instance-link-hello-interval': 5,
                    'ldp-instance-link-protection-timeout': 120,
                    'ldp-instance-make-before-break-switchover-delay': 3,
                    'ldp-instance-make-before-break-timeout': 30,
                    'ldp-instance-targeted-hello-hold-time': 45,
                    'ldp-instance-targeted-hello-interval': 15
                },
                'ldp-transit-lsp-route-stats': 'disabled',
                'ldp-transport-preference': 'IPv4',
                'ldp-unicast-transit-lsp-chaining': 'disabled'
            }
        }
    }

    golden_output_4 = {'execute.return_value': '''
        show ldp overview 
        Instance: master
        Reference count: 2
        Router ID: 100.2.14.100
        LDP inet: enabled
        Transport preference: IPv4
        Message id: 4
        Configuration sequence: 1
        Deaggregate: disabled
        Explicit null: disabled
        IPv6 tunneling: disabled
        Strict targeted hellos: disabled
        Loopback if added: no
        Route preference: 9
        Unicast transit LSP chaining: disabled
        P2MP transit LSP chaining: disabled
        Transit LSP statistics based on route statistics: disabled
        LDP route acknowledgement: enabled
        BGP export: enabled
        LDP mtu discovery: disabled
        LDP SR Mapping Client: disabled
        Capabilities enabled: none
        Egress FEC capabilities enabled: entropy-label-capability
        Downstream unsolicited Sessions:
            Nonexistent: 1
            Retention: liberal
            Control: ordered
        Auto targeted sessions:
            Auto targeted: disabled
            Dynamic tunnel session count: 0
        P2MP:
            Recursive route: disabled
            No rsvp tunneling: disabled
        Timers:
            Keepalive interval: 10, Keepalive timeout: 30
            Link hello interval: 5, Link hello hold time: 15
            Targeted hello interval: 15, Targeted hello hold time: 45
            Label withdraw delay: 60, Make before break timeout: 30
            Make before break switchover delay: 3
            Link protection timeout: 120
        Graceful restart:
            Restart: disabled, Helper: enabled, Restart in process: false
            Reconnect time: 60000, Max neighbor reconnect time: 120000
            Recovery time: 160000, Max neighbor recovery time: 240000
        Traffic Engineering:
            Bgp igp: disabled
            Both ribs: disabled
            Mpls forwarding: disabled
        IGP:
            Tracking igp metric: disabled
            Sync session up delay: 10
        Session protection:
            Session protection: disabled
            Session protection timeout: 0
        Interface addresses advertising:
            10.1.2.2
        LDP Job:
            Read job time quantum: 1000, Write job time quantum: 1000
            Read job loop quantum: 100, Write job loop quantum: 100
            Backup inbound read job time quantum: 1000, Backup outbound read job time quantum: 1000
            Backup inbound read job loop quantum: 100, Backup outbound read job loop quantum: 100
        Label allocation:
            Current number of LDP labels allocated: 0
            Total number of LDP labels allocated: 0
            Total number of LDP labels freed: 0
            Total number of LDP label allocation failure: 0
            Current number of labels allocated by all protocols: 0
    '''}

    golden_parsed_output_4 = {
        'ldp-overview-information': {
            'ldp-overview': {
                'ldp-auto-targeted-session': {
                    'ldp-auto-targeted-dyn-tun-ses-count': 0,
                    'ldp-auto-targeted-session-enabled': 'disabled'
                },
                'ldp-bgp-export': 'enabled',
                'ldp-configuration-sequence': 1,
                'ldp-deaggregate': 'disabled',
                'ldp-explicit-null': 'disabled',
                'ldp-gr-overview': {
                    'ldp-gr-helper': 'enabled',
                    'ldp-gr-max-neighbor-reconnect-time': 120000,
                    'ldp-gr-max-neighbor-recovery-time': 240000,
                    'ldp-gr-reconnect-time': 60000,
                    'ldp-gr-recovery-time': 160000,
                    'ldp-gr-restart': 'disabled',
                    'ldp-gr-restarting': 'false'
                },
                'ldp-igp-overview': {
                    'ldp-igp-sync-session-up-delay': 10,
                    'ldp-tracking-igp-metric': 'disabled'
                },
                'ldp-inet': 'enabled',
                'ldp-instance-capability': {
                    'ldp-capability': 'none'
                },
                'ldp-instance-egress-fec-capability': {
                    'ldp-egress-fec-capability': 'entropy-label-capability'
                },
                'ldp-instance-name': 'master',
                'ldp-interface-address': {
                    'interface-address': '10.1.2.2'
                },
                'ldp-ipv6-tunneling': 'disabled',
                'ldp-job-overview': {
                    'ldp-inbound-read-job-loop-quantum': 100,
                    'ldp-inbound-read-job-time-quantum': 1000,
                    'ldp-outbound-read-job-loop-quantum': 100,
                    'ldp-outbound-read-job-time-quantum': 1000,
                    'ldp-read-job-loop-quantum': 100,
                    'ldp-read-job-time-quantum': 1000,
                    'ldp-write-job-loop-quantum': 100,
                    'ldp-write-job-time-quantum': 1000
                },
                'ldp-label-allocation': {
                    'ldp-global-label-current-allocs': 0,
                    'ldp-label-alloc-failure': 0,
                    'ldp-label-current-allocs': 0,
                    'ldp-label-total-allocs': 0,
                    'ldp-label-total-frees': 0
                },
                'ldp-loopback-if-added': 'no',
                'ldp-message-id': 4,
                'ldp-mtu-discovery': 'disabled',
                'ldp-p2mp': {
                    'ldp-p2mp-no-rsvp-tunneling-enabled': 'disabled',
                    'ldp-p2mp-recursive-route-enabled': 'disabled'
                },
                'ldp-p2mp-transit-lsp-chaining': 'disabled',
                'ldp-reference-count': 2,
                'ldp-route-acknowledgement': 'enabled',
                'ldp-route-preference': 9,
                'ldp-router-id': '100.2.14.100',
                'ldp-session-count': {
                    'ldp-control-mode': 'ordered',
                    'ldp-retention-mode': 'liberal',
                    'ldp-session-nonexistent': 1
                },
                'ldp-session-protect-overview': {
                    'ldp-session-protect': 'disabled',
                    'ldp-session-protect-timeout': 0
                },
                'ldp-sr-mapping-client': 'disabled',
                'ldp-strict-targeted-hellos': 'disabled',
                'ldp-te-overview': {
                    'ldp-te-bgp-igp': 'disabled',
                    'ldp-te-both-ribs': 'disabled',
                    'ldp-te-mpls-forwarding': 'disabled'
                },
                'ldp-timer-overview': {
                    'ldp-instance-keepalive-interval': 10,
                    'ldp-instance-keepalive-timeout': 30,
                    'ldp-instance-label-withdraw-delay': 60,
                    'ldp-instance-link-hello-hold-time': 15,
                    'ldp-instance-link-hello-interval': 5,
                    'ldp-instance-link-protection-timeout': 120,
                    'ldp-instance-make-before-break-switchover-delay': 3,
                    'ldp-instance-make-before-break-timeout': 30,
                    'ldp-instance-targeted-hello-hold-time': 45,
                    'ldp-instance-targeted-hello-interval': 15
                },
                'ldp-transit-lsp-route-stats': 'disabled',
                'ldp-transport-preference': 'IPv4',
                'ldp-unicast-transit-lsp-chaining': 'disabled'
            }
        }
    }

    golden_output_5 = {'execute.return_value': '''
        show ldp overview 
        Instance: master
        Router ID: 100.2.1.100
        Message id: 4
        Configuration sequence: 1
        Deaggregate: disabled
        Explicit null: disabled
        IPv6 tunneling: disabled
        Strict targeted hellos: disabled
        Loopback if added: no
        Route preference: 9
        Unicast transit LSP chaining: disabled
        P2MP transit LSP chaining: disabled
        Transit LSP statistics based on route statistics: disabled
        Capabilities enabled: none
        Protocol modes:
            Distribution: unsolicited
            Retention: liberal
            Control: ordered
        Sessions:
            Connecting: 1
        Timers:
            Keepalive interval: 10, Keepalive timeout: 30
            Link hello interval: 5, Link hello hold time: 15
            Targeted hello interval: 15, Targeted hello hold time: 45
            Label withdraw delay: 60
        Graceful restart:
            Restart: enabled, Helper: enabled, Restart in process: false
            Reconnect time: 60000, Max neighbor reconnect time: 120000
            Recovery time: 160000, Max neighbor recovery time: 240000
        Traffic Engineering:
            Bgp igp: disabled
            Both ribs: disabled
            Mpls forwarding: disabled
        IGP:
            Tracking igp metric: disabled
            Sync session up delay: 10
        Session protection:
            Session protection: disabled
            Session protecton timeout: 0
        Interface addresses advertising:
            10.1.2.2
    '''}

    golden_parsed_output_5 = {
        'ldp-overview-information': {
            'ldp-overview': {
                'ldp-configuration-sequence': 1,
                'ldp-deaggregate': 'disabled',
                'ldp-explicit-null': 'disabled',
                'ldp-gr-overview': {
                    'ldp-gr-helper': 'enabled',
                    'ldp-gr-max-neighbor-reconnect-time': 120000,
                    'ldp-gr-max-neighbor-recovery-time': 240000,
                    'ldp-gr-reconnect-time': 60000,
                    'ldp-gr-recovery-time': 160000,
                    'ldp-gr-restart': 'enabled',
                    'ldp-gr-restarting': 'false'
                },
                'ldp-igp-overview': {
                    'ldp-igp-sync-session-up-delay': 10,
                    'ldp-tracking-igp-metric': 'disabled'
                },
                'ldp-instance-capability': {
                    'ldp-capability': 'none'
                },
                'ldp-instance-name': 'master',
                'ldp-interface-address': {
                    'interface-address': '10.1.2.2'
                },
                'ldp-ipv6-tunneling': 'disabled',
                'ldp-loopback-if-added': 'no',
                'ldp-message-id': 4,
                'ldp-p2mp-transit-lsp-chaining': 'disabled',
                'ldp-protocol-modes': {
                    'ldp-control-mode': 'ordered',
                    'ldp-distribution-mode': 'unsolicited',
                    'ldp-retention-mode': 'liberal'
                },
                'ldp-route-preference': 9,
                'ldp-router-id': '100.2.1.100',
                'ldp-session-count': {
                    'ldp-session-connecting': 1
                },
                'ldp-session-protect-overview': {
                    'ldp-session-protect': 'disabled',
                    'ldp-session-protect-timeout': 0
                },
                'ldp-strict-targeted-hellos': 'disabled',
                'ldp-te-overview': {
                    'ldp-te-bgp-igp': 'disabled',
                    'ldp-te-both-ribs': 'disabled',
                    'ldp-te-mpls-forwarding': 'disabled'
                },
                'ldp-timer-overview': {
                    'ldp-instance-keepalive-interval': 10,
                    'ldp-instance-keepalive-timeout': 30,
                    'ldp-instance-label-withdraw-delay': 60,
                    'ldp-instance-link-hello-hold-time': 15,
                    'ldp-instance-link-hello-interval': 5,
                    'ldp-instance-targeted-hello-hold-time': 45,
                    'ldp-instance-targeted-hello-interval': 15
                },
                'ldp-transit-lsp-route-stats': 'disabled',
                'ldp-unicast-transit-lsp-chaining': 'disabled'
            }
        }
    }

    golden_parsed_output_6 = {
        "ldp-overview-information": {
        "ldp-overview": {
            "ldp-auto-targeted-session": {
                "ldp-auto-targeted-dyn-tun-ses-count": 0,
                "ldp-auto-targeted-session-enabled": "disabled"
            },
            "ldp-bgp-export": "enabled",
            "ldp-configuration-sequence": 2,
            "ldp-control-mode": "ordered",
            "ldp-deaggregate": "disabled",
            "ldp-explicit-null": "disabled",
            "ldp-gr-overview": {
                "ldp-gr-helper": "enabled",
                "ldp-gr-max-neighbor-reconnect-time": 120000,
                "ldp-gr-max-neighbor-recovery-time": 240000,
                "ldp-gr-reconnect-time": 60000,
                "ldp-gr-recovery-time": 160000,
                "ldp-gr-restart": "enabled",
                "ldp-gr-restarting": "false"
            },
            "ldp-igp-overview": {
                "ldp-igp-sync-session-up-delay": 10,
                "ldp-tracking-igp-metric": "disabled"
            },
            "ldp-inet": "enabled",
            "ldp-instance-capability": {
                "ldp-capability": "none"
            },
            "ldp-instance-egress-fec-capability": {
                "ldp-egress-fec-capability": "entropy-label-capability"
            },
            "ldp-instance-name": "master",
            "ldp-interface-address": {
                "interface-address": "106.187.14.157"
            },
            "ldp-ipv6-tunneling": "disabled",
            "ldp-job-overview": {
                "ldp-inbound-read-job-loop-quantum": 100,
                "ldp-inbound-read-job-time-quantum": 1000,
                "ldp-outbound-read-job-loop-quantum": 100,
                "ldp-outbound-read-job-time-quantum": 1000,
                "ldp-read-job-loop-quantum": 100,
                "ldp-read-job-time-quantum": 1000,
                "ldp-write-job-loop-quantum": 100,
                "ldp-write-job-time-quantum": 1000
            },
            "ldp-label-allocation": {
                "ldp-global-label-current-allocs": 0,
                "ldp-label-alloc-failure": 0,
                "ldp-label-current-allocs": 3,
                "ldp-label-total-allocs": 7,
                "ldp-label-total-frees": 4
            },
            "ldp-loopback-if-added": "no",
            "ldp-message-id": 10,
            "ldp-mtu-discovery": "disabled",
            "ldp-p2mp": {
                "ldp-p2mp-no-rsvp-tunneling-enabled": "disabled",
                "ldp-p2mp-recursive-route-enabled": "disabled"
            },
            "ldp-p2mp-transit-lsp-chaining": "disabled",
            "ldp-reference-count": 3,
            "ldp-retention-mode": "liberal",
            "ldp-route-acknowledgement": "enabled",
            "ldp-route-preference": 9,
            "ldp-router-id": "106.187.14.240",
            "ldp-session-count": {
                "ldp-control-mode": "ordered",
                "ldp-retention-mode": "liberal",
                "ldp-session-nonexistent": 1
            },
            "ldp-session-operational": 1,
            "ldp-session-protect-overview": {
                "ldp-session-protect": "disabled",
                "ldp-session-protect-timeout": 0
            },
            "ldp-sr-mapping-client": "disabled",
            "ldp-strict-targeted-hellos": "disabled",
            "ldp-te-overview": {
                "ldp-te-bgp-igp": "disabled",
                "ldp-te-both-ribs": "disabled",
                "ldp-te-mpls-forwarding": "disabled"
            },
            "ldp-timer-overview": {
                "ldp-instance-keepalive-interval": 10,
                "ldp-instance-keepalive-timeout": 30,
                "ldp-instance-label-withdraw-delay": 60,
                "ldp-instance-link-hello-hold-time": 15,
                "ldp-instance-link-hello-interval": 5,
                "ldp-instance-link-protection-timeout": 120,
                "ldp-instance-make-before-break-switchover-delay": 3,
                "ldp-instance-make-before-break-timeout": 30,
                "ldp-instance-targeted-hello-hold-time": 45,
                "ldp-instance-targeted-hello-interval": 15
            },
            "ldp-transit-lsp-route-stats": "disabled",
            "ldp-transport-preference": "IPv4",
            "ldp-unicast-transit-lsp-chaining": "disabled"
        }
    }
    }

    golden_output_6 = {'execute.return_value': '''
        show ldp overview 
        Instance: master
        Reference count: 3
        Router ID: 106.187.14.240
        LDP inet: enabled
        Transport preference: IPv4
        Message id: 10
        Configuration sequence: 2
        Deaggregate: disabled
        Explicit null: disabled
        IPv6 tunneling: disabled
        Strict targeted hellos: disabled
        Loopback if added: no
        Route preference: 9
        Unicast transit LSP chaining: disabled
        P2MP transit LSP chaining: disabled
        Transit LSP statistics based on route statistics: disabled
        LDP route acknowledgement: enabled
        BGP export: enabled
        LDP mtu discovery: disabled
        LDP SR Mapping Client: disabled
        Capabilities enabled: none
        Egress FEC capabilities enabled: entropy-label-capability
        Downstream unsolicited Sessions:
            Nonexistent: 1
            Retention: liberal
            Control: ordered
            Operational: 1
            Retention: liberal
            Control: ordered
        Auto targeted sessions:
            Auto targeted: disabled
            Dynamic tunnel session count: 0
        P2MP:
            Recursive route: disabled
            No rsvp tunneling: disabled
        Timers:
            Keepalive interval: 10, Keepalive timeout: 30
            Link hello interval: 5, Link hello hold time: 15
            Targeted hello interval: 15, Targeted hello hold time: 45
            Label withdraw delay: 60, Make before break timeout: 30
            Make before break switchover delay: 3
            Link protection timeout: 120
        Graceful restart:
            Restart: enabled, Helper: enabled, Restart in process: false
            Reconnect time: 60000, Max neighbor reconnect time: 120000
            Recovery time: 160000, Max neighbor recovery time: 240000
        Traffic Engineering:
            Bgp igp: disabled
            Both ribs: disabled
            Mpls forwarding: disabled
        IGP:
            Tracking igp metric: disabled
            Sync session up delay: 10
        Session protection:
            Session protection: disabled
            Session protection timeout: 0
        Interface addresses advertising:
            106.187.14.121
            106.187.14.157
        LDP Job:
            Read job time quantum: 1000, Write job time quantum: 1000
            Read job loop quantum: 100, Write job loop quantum: 100
            Backup inbound read job time quantum: 1000, Backup outbound read job time quantum: 1000
            Backup inbound read job loop quantum: 100, Backup outbound read job loop quantum: 100
        Label allocation:
            Current number of LDP labels allocated: 3
            Total number of LDP labels allocated: 7
            Total number of LDP labels freed: 4
            Total number of LDP label allocation failure: 0
            Current number of labels allocated by all protocols: 0
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLDPOverview(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLDPOverview(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowLDPOverview(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowLDPOverview(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.device = Mock(**self.golden_output_4)
        obj = ShowLDPOverview(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_golden_5(self):
        self.device = Mock(**self.golden_output_5)
        obj = ShowLDPOverview(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_5)

    def test_golden_6(self):
        self.device = Mock(**self.golden_output_6)
        obj = ShowLDPOverview(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_6)


# =================================
# Unit test for 'show ldp session {ipaddress} detail'
# =================================
class TestShowLDPSessionIpaddressDetail(unittest.TestCase):
    '''unit test for "show ldp session {ipaddress} detail'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "ldp-session-information": {
        "ldp-session": {
            "ldp-connection-state": "Open",
            "ldp-graceful-restart-local": "disabled",
            "ldp-graceful-restart-remote": "disabled",
            "ldp-holdtime": "30",
            "ldp-keepalive-interval": "10",
            "ldp-keepalive-time": "3",
            "ldp-local-address": "59.128.2.250",
            "ldp-local-helper-mode": "enabled",
            "ldp-local-label-adv-mode": "Downstream unsolicited",
            "ldp-local-maximum-reconnect": "120000",
            "ldp-local-maximum-recovery": "240000",
            "ldp-mtu-discovery": "disabled",
            "ldp-neg-label-adv-mode": "Downstream unsolicited",
            "ldp-neighbor-address": "106.187.14.240",
            "ldp-neighbor-count": "1",
            "ldp-neighbor-types": {
                "ldp-neighbor-type": "discovered"
            },
            "ldp-remaining-time": "23",
            "ldp-remote-address": "106.187.14.240",
            "ldp-remote-helper-mode": "enabled",
            "ldp-remote-label-adv-mode": "Downstream unsolicited",
            "ldp-retry-interval": "1",
            "ldp-session-address": {
                "interface-address": "106.187.14.157"
            },
            "ldp-session-capabilities-advertised": {
                "ldp-capability": "none"
            },
            "ldp-session-capabilities-received": {
                "ldp-capability": "none"
            },
            "ldp-session-flags": {
                "ldp-session-flag": "none"
            },
            "ldp-session-id": "59.128.2.250:0--106.187.14.240:0",
            "ldp-session-max-pdu": "4096",
            "ldp-session-nsr-state": "Not in sync",
            "ldp-session-protection": {
                "ldp-session-protection-state": "disabled"
            },
            "ldp-session-role": "Passive",
            "ldp-session-state": "Operational",
            "ldp-up-time": "00:00:47"
        }
    }
    }

    golden_output = {
        'execute.return_value':
        '''
        show ldp session 106.187.14.240 detail
          Address: 106.187.14.240, State: Operational, Connection: Open, Hold time: 23
            Session ID: 59.128.2.250:0--106.187.14.240:0
            Next keepalive in 3 seconds
            Passive, Maximum PDU: 4096, Hold time: 30, Neighbor count: 1
            Neighbor types: discovered
            Keepalive interval: 10, Connect retry interval: 1
            Local address: 59.128.2.250, Remote address: 106.187.14.240
            Up for 00:00:47
            Capabilities advertised: none
            Capabilities received: none
            Protection: disabled
            Session flags: none
            Local - Restart: disabled, Helper mode: enabled
            Remote - Restart: disabled, Helper mode: enabled
            Local maximum neighbor reconnect time: 120000 msec
            Local maximum neighbor recovery time: 240000 msec
            Local Label Advertisement mode: Downstream unsolicited
            Remote Label Advertisement mode: Downstream unsolicited
            Negotiated Label Advertisement mode: Downstream unsolicited
            MTU discovery: disabled
            Nonstop routing state: Not in sync
            Next-hop addresses received:
                106.187.14.157
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLdpSessionIpaddressDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(ipaddress='106.187.14.240')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLdpSessionIpaddressDetail(device=self.device)
        parsed_output = obj.parse(ipaddress='106.187.14.240')
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
