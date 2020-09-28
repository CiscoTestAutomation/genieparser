import unittest
from unittest.mock import Mock

from pyats.topology import loader, Device
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_firewall import ShowFirewall,\
                                                  ShowFirewallCounterFilter,\
                                                  ShowFirewallLog

class TestShowFirewall(unittest.TestCase):
    """ Unit tests for:
            * show firewall
    """

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show firewall

        Filter: catch_all                                              
        Counters:
        Name                                                Bytes              Packets
        cflow_counter_v4                              28553344730            151730215

        Filter: local-access-control                                   
        Counters:
        Name                                                Bytes              Packets
        fragment-test                                           0                    0
        fragment-test2                                          0                    0
        last_policer                                   1069200810             19016081
        ntp-deny-count                                          0                    0
        telnet-deny-count                                    1316                   23
        traceroute-udp-deny-count                         1385466                 8350
        Policers:
        Name                                                Bytes              Packets
        MINIMUM-RATE-POLICER                              2508396                48164

        Filter: v4_EXT_inbound                                         
        Counters:
        Name                                                Bytes              Packets
        deny-dst-in                                             0                    0
        deny-p-in                                               0                    0
        deny-src-in                                             0                    0

        Filter: v4_toIPVPN_inbound                                     
        Counters:
        Name                                                Bytes              Packets
        cflow_counter_v4                                        0                    0
        deny-dst-in                                             0                    0
        deny-rsvp-in                                            0                    0

        Filter: v6_catch_all                                           
        Counters:
        Name                                                Bytes              Packets
        cflow_counter_v6                              12001013864            149192171

        Filter: v6_local-access-control                                
        Counters:
        Name                                                Bytes              Packets
        traceroute-udp-deny-count                               0                    0
        v6_last_policer                                1061535120              7859252
        Policers:
        Name                                                Bytes              Packets
        MINIMUM-RATE-POLICER                                    0                    0

        Filter: __default_bpdu_filter__
    '''}

    golden_parsed_output = {
        "firewall-information": {
            "filter-information": [
                {
                    "counter": [
                        {
                            "byte-count": "28553344730",
                            "counter-name": "cflow_counter_v4",
                            "packet-count": "151730215"
                        }
                    ],
                    "filter-name": "catch_all"
                },
                {
                    "counter": [
                        {
                            "byte-count": "0",
                            "counter-name": "fragment-test",
                            "packet-count": "0"
                        },
                        {
                            "byte-count": "0",
                            "counter-name": "fragment-test2",
                            "packet-count": "0"
                        },
                        {
                            "byte-count": "1069200810",
                            "counter-name": "last_policer",
                            "packet-count": "19016081"
                        },
                        {
                            "byte-count": "0",
                            "counter-name": "ntp-deny-count",
                            "packet-count": "0"
                        },
                        {
                            "byte-count": "1316",
                            "counter-name": "telnet-deny-count",
                            "packet-count": "23"
                        },
                        {
                            "byte-count": "1385466",
                            "counter-name": "traceroute-udp-deny-count",
                            "packet-count": "8350"
                        }
                    ],
                    "filter-name": "local-access-control",
                    "policer": {
                        "byte-count": "2508396",
                        "packet-count": "48164",
                        "policer-name": "MINIMUM-RATE-POLICER"
                    }
                },
                {
                    "counter": [
                        {
                            "byte-count": "0",
                            "counter-name": "deny-dst-in",
                            "packet-count": "0"
                        },
                        {
                            "byte-count": "0",
                            "counter-name": "deny-p-in",
                            "packet-count": "0"
                        },
                        {
                            "byte-count": "0",
                            "counter-name": "deny-src-in",
                            "packet-count": "0"
                        }
                    ],
                    "filter-name": "v4_EXT_inbound"
                },
                {
                    "counter": [
                        {
                            "byte-count": "0",
                            "counter-name": "cflow_counter_v4",
                            "packet-count": "0"
                        },
                        {
                            "byte-count": "0",
                            "counter-name": "deny-dst-in",
                            "packet-count": "0"
                        },
                        {
                            "byte-count": "0",
                            "counter-name": "deny-rsvp-in",
                            "packet-count": "0"
                        }
                    ],
                    "filter-name": "v4_toIPVPN_inbound"
                },
                {
                    "counter": [
                        {
                            "byte-count": "12001013864",
                            "counter-name": "cflow_counter_v6",
                            "packet-count": "149192171"
                        }
                    ],
                    "filter-name": "v6_catch_all"
                },
                {
                    "counter": [
                        {
                            "byte-count": "0",
                            "counter-name": "traceroute-udp-deny-count",
                            "packet-count": "0"
                        },
                        {
                            "byte-count": "1061535120",
                            "counter-name": "v6_last_policer",
                            "packet-count": "7859252"
                        }
                    ],
                    "filter-name": "v6_local-access-control",
                    "policer": {
                        "byte-count": "0",
                        "packet-count": "0",
                        "policer-name": "MINIMUM-RATE-POLICER"
                    }
                },
                {
                    "filter-name": "__default_bpdu_filter__"
                }
            ]
        }
        
    }

    golden_output_2 = {'execute.return_value': 
    """
        show firewall

        Filter: __default_bpdu_filter__

        Filter: ICMP_ACL_filter
        Counters:
        Name                                                Bytes              Packets
        block                                                   0                    0

        Filter: TCP_ACK-flood_ACL_filter
        Counters:
        Name                                                Bytes              Packets
        block                                                   0                    0

        Filter: TCP_SYN-flood_ACL_filter
        Counters:
        Name                                                Bytes              Packets
        block                                                   0                    0

        Filter: UDP_ACL_filter
        Counters:
        Name                                                Bytes              Packets
        block                                                   0                    0

        Filter: ICMP_ACL_filter_IPv6
        Counters:
        Name                                                Bytes              Packets
        block                                                   0                    0

        Filter: TCP_ACK-flood_ACL_filter_IPv6
        Counters:
        Name                                                Bytes              Packets
        block                                                   0                    0

        Filter: TCP_SYN-flood_ACL_filter_IPv6
        Counters:
        Name                                                Bytes              Packets
        block                                                   0                    0

        Filter: UDP_ACL_filter_IPv6
        Counters:
        Name                                                Bytes              Packets
        block                                                   0                    0"""
        }

    golden_parsed_output_2 = {
        'firewall-information': {
            'filter-information': [{
                'filter-name': '__default_bpdu_filter__'
            },
            {
                'counter': [{
                'byte-count': '0',
                'counter-name': 'block',
                'packet-count': '0'
                }],
                'filter-name': 'ICMP_ACL_filter'
            },
            {
                'counter': [{
                'byte-count': '0',
                'counter-name': 'block',
                'packet-count': '0'
                }],
                'filter-name': 'TCP_ACK-flood_ACL_filter'
            },
            {
                'counter': [{
                'byte-count': '0',
                'counter-name': 'block',
                'packet-count': '0'
                }],
                'filter-name': 'TCP_SYN-flood_ACL_filter'
            },
            {
                'counter': [{
                'byte-count': '0',
                'counter-name': 'block',
                'packet-count': '0'
                }],
                'filter-name': 'UDP_ACL_filter'
            },
            {
                'counter': [{
                'byte-count': '0',
                'counter-name': 'block',
                'packet-count': '0'
                }],
                'filter-name': 'ICMP_ACL_filter_IPv6'
            },
            {
                'counter': [{
                'byte-count': '0',
                'counter-name': 'block',
                'packet-count': '0'
                }],
                'filter-name': 'TCP_ACK-flood_ACL_filter_IPv6'
            },
            {
                'counter': [{
                'byte-count': '0',
                'counter-name': 'block',
                'packet-count': '0'
                }],
                'filter-name': 'TCP_SYN-flood_ACL_filter_IPv6'
            },
            {
                'counter': [{
                'byte-count': '0',
                'counter-name': 'block',
                'packet-count': '0'
                }],
                'filter-name': 'UDP_ACL_filter_IPv6'
            }
            ]
        }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowFirewall(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowFirewall(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowFirewall(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

class TestShowFirewallCounterFilter(unittest.TestCase):
    """ Unit tests for:
            * show firewall counter filter v6_local-access-control v6_last_policer
    """

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show firewall counter filter v6_local-access-control v6_last_policer

        Filter: v6_local-access-control                                
        Counters:
        Name                                                Bytes              Packets
        v6_last_policer                                1061737740              7860915
    '''}

    golden_parsed_output = {
        "firewall-information": {
            "filter-information": {
                "counter": {
                    "byte-count": "1061737740",
                    "counter-name": "v6_last_policer",
                    "packet-count": "7860915"
                },
                "filter-name": "v6_local-access-control"
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowFirewallCounterFilter(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse(filter='v6_local-access-control', counter_name='v6_last_policer')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowFirewallCounterFilter(device=self.device)
        parsed_output = obj.parse(filter='v6_local-access-control', counter_name='v6_last_policer')
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowFirewallLog(unittest.TestCase):
    """ Unit tests for:
            * show firewall log
    """

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show firewall log
        Log :
        Time      Filter    Action Interface     Protocol        Src Addr                         Dest Addr
        10:28:22  pfe       D      ge-0/0/0.0    TCP             10.70.0.2                         10.70.0.1
        10:15:22  pfe       D      ge-0/0/0.0    TCP             10.70.0.2                         10.70.0.1
        10:15:19  pfe       D      ge-0/0/0.0    TCP             10.70.0.2                         10.70.0.1
    '''}

    golden_parsed_output = {
        "firewall-log-information": {
            "log-information": [
                {
                    "action-name": "D",
                    "destination-address": "10.70.0.1",
                    "filter-name": "pfe",
                    "interface-name": "ge-0/0/0.0",
                    "protocol-name": "TCP",
                    "source-address": "10.70.0.2",
                    "time": "10:28:22"
                },
                {
                    "action-name": "D",
                    "destination-address": "10.70.0.1",
                    "filter-name": "pfe",
                    "interface-name": "ge-0/0/0.0",
                    "protocol-name": "TCP",
                    "source-address": "10.70.0.2",
                    "time": "10:15:22"
                },
                {
                    "action-name": "D",
                    "destination-address": "10.70.0.1",
                    "filter-name": "pfe",
                    "interface-name": "ge-0/0/0.0",
                    "protocol-name": "TCP",
                    "source-address": "10.70.0.2",
                    "time": "10:15:19"
                }
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowFirewallLog(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowFirewallLog(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()