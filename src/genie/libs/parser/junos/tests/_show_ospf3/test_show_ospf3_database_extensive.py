import unittest
from unittest.mock import Mock

from pyats.topology import loader, Device
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos._show_ospf3.show_ospf3_database_extensive import ShowOspf3DatabaseExtensive

class TestShowOspf3DatabaseExtensive(unittest.TestCase):

    maxDiff = None

    device = Device(name='test-device')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value':
    '''

        show ospf3 database extensive | no-more

            OSPF3 database, Area 0.0.0.8
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Router      0.0.0.0          59.128.2.250     0x800018ed  2504  0xaf2d  56
        bits 0x2, Options 0x33
        Type PointToPoint (1), Metric 5
            Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 59.128.2.251
        Type PointToPoint (1), Metric 100
            Loc-If-Id 3, Nbr-If-Id 4, Nbr-Rtr-Id 106.187.14.240
        Type: PointToPoint, Node ID: 106.187.14.240, Metric: 100, Bidirectional
        Type: PointToPoint, Node ID: 59.128.2.251, Metric: 5, Bidirectional
        Aging timer 00:18:16
        Installed 00:41:38 ago, expires in 00:18:16, sent 00:41:36 ago
        Last changed 2w6d 04:50:31 ago, Change count: 196
        Router      0.0.0.0          59.128.2.251     0x80001841   629  0x1d57  56
        bits 0x2, Options 0x33
        Type PointToPoint (1), Metric 5
            Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 59.128.2.250
        Type PointToPoint (1), Metric 120
            Loc-If-Id 3, Nbr-If-Id 4, Nbr-Rtr-Id 106.187.14.241
        Type: PointToPoint, Node ID: 106.187.14.241, Metric: 120, Bidirectional
        Type: PointToPoint, Node ID: 59.128.2.250, Metric: 5, Bidirectional
        Aging timer 00:49:31
        Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
        Last changed 2w6d 04:10:26 ago, Change count: 208
        Router      0.0.0.0          106.187.14.240   0x80001a0c    53  0x50bb  72
        bits 0x2, Options 0x33
        Type PointToPoint (1), Metric 5
            Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 106.187.14.241
        Type PointToPoint (1), Metric 100
            Loc-If-Id 3, Nbr-If-Id 3, Nbr-Rtr-Id 111.87.5.252
        Type PointToPoint (1), Metric 100
            Loc-If-Id 4, Nbr-If-Id 3, Nbr-Rtr-Id 59.128.2.250
        Type: PointToPoint, Node ID: 59.128.2.250, Metric: 100, Bidirectional
        Type: PointToPoint, Node ID: 111.87.5.252, Metric: 100, Bidirectional
        Type: PointToPoint, Node ID: 106.187.14.241, Metric: 5, Bidirectional
        Aging timer 00:59:06
        Installed 00:00:50 ago, expires in 00:59:07, sent 00:00:48 ago
        Last changed 2w6d 04:50:31 ago, Change count: 341
        Router      0.0.0.0          106.187.14.241   0x800018b7  1356  0x94a3  72
        bits 0x2, Options 0x33
        Type PointToPoint (1), Metric 5
            Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 106.187.14.240
        Type PointToPoint (1), Metric 120
            Loc-If-Id 3, Nbr-If-Id 3, Nbr-Rtr-Id 111.87.5.253
        Type PointToPoint (1), Metric 120
            Loc-If-Id 4, Nbr-If-Id 3, Nbr-Rtr-Id 59.128.2.251
        Type: PointToPoint, Node ID: 59.128.2.251, Metric: 120, Bidirectional
        Type: PointToPoint, Node ID: 111.87.5.253, Metric: 120, Bidirectional
        Type: PointToPoint, Node ID: 106.187.14.240, Metric: 5, Bidirectional
        Aging timer 00:37:23
        Installed 00:22:30 ago, expires in 00:37:24, sent 00:22:28 ago
        Last changed 2w6d 04:10:26 ago, Change count: 280
        Router     *0.0.0.0          111.87.5.252     0x80001890  1010  0xae6c  56
        bits 0x2, Options 0x33
        Type PointToPoint (1), Metric 5
            Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 111.87.5.253
        Type PointToPoint (1), Metric 100
            Loc-If-Id 3, Nbr-If-Id 3, Nbr-Rtr-Id 106.187.14.240
        Type: PointToPoint, Node ID: 106.187.14.240, Metric: 100, Bidirectional
        Type: PointToPoint, Node ID: 111.87.5.253, Metric: 5, Bidirectional
        Gen timer 00:33:09
        Aging timer 00:43:09
        Installed 00:16:50 ago, expires in 00:43:10, sent 00:16:48 ago
        Last changed 3w0d 17:02:09 ago, Change count: 6, Ours
        Router      0.0.0.0          111.87.5.253     0x8000182a  1012  0x8fdc  56
        bits 0x2, Options 0x33
        Type PointToPoint (1), Metric 5
            Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 111.87.5.252
        Type PointToPoint (1), Metric 120
            Loc-If-Id 3, Nbr-If-Id 3, Nbr-Rtr-Id 106.187.14.241
        Type: PointToPoint, Node ID: 106.187.14.241, Metric: 120, Bidirectional
        Type: PointToPoint, Node ID: 111.87.5.252, Metric: 5, Bidirectional
        Aging timer 00:43:07
        Installed 00:16:49 ago, expires in 00:43:08, sent 00:16:48 ago
        Last changed 3w0d 17:02:14 ago, Change count: 181
        IntraArPfx  0.0.0.1          59.128.2.250     0x8000178c  1754  0xc4fc  76
        Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 59.128.2.250
        Prefix-count 3
        Prefix 2001:268:fb80:3e::/64
            Prefix-options 0x0, Metric 5
        Prefix 2001:268:fb8f:29::/64
            Prefix-options 0x0, Metric 100
        Prefix 2001:268:fb80::13/128
            Prefix-options 0x2, Metric 0
        Aging timer 00:30:46
        Installed 00:29:08 ago, expires in 00:30:46, sent 00:29:06 ago
        Last changed 29w5d 21:33:07 ago, Change count: 1
        IntraArPfx  0.0.0.1          59.128.2.251     0x8000178b  1004  0x9e2d  76
        Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 59.128.2.251
        Prefix-count 3
        Prefix 2001:268:fb80:3e::/64
            Prefix-options 0x0, Metric 5
        Prefix 2001:268:fb8f:9::/64
            Prefix-options 0x0, Metric 120
        Prefix 2001:268:fb80::14/128
            Prefix-options 0x2, Metric 0
        Aging timer 00:43:16
        Installed 00:16:35 ago, expires in 00:43:16, sent 00:16:33 ago
        Last changed 29w5d 21:33:07 ago, Change count: 1
        IntraArPfx  0.0.0.1          106.187.14.240   0x80001808  2780  0x6948  88
        Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 106.187.14.240
        Prefix-count 4
        Prefix 2001:268:fb8f:5::/64
            Prefix-options 0x0, Metric 5
        Prefix 2001:268:fb8f:1f::/64
            Prefix-options 0x0, Metric 100
        Prefix 2001:268:fb8f:29::/64
            Prefix-options 0x0, Metric 100
        Prefix 2001:268:fb8f::1/128
            Prefix-options 0x2, Metric 0
        Aging timer 00:13:39
        Installed 00:46:17 ago, expires in 00:13:40, sent 00:46:15 ago
        Last changed 2w6d 04:50:31 ago, Change count: 147
        IntraArPfx  0.0.0.1          106.187.14.241   0x800017e6  1023  0xa81e  88
        Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 106.187.14.241
        Prefix-count 4
        Prefix 2001:268:fb8f:5::/64
            Prefix-options 0x0, Metric 5
        Prefix 2001:268:fb8f:21::/64
            Prefix-options 0x0, Metric 120
        Prefix 2001:268:fb8f:9::/64
            Prefix-options 0x0, Metric 120
        Prefix 2001:268:fb8f::2/128
            Prefix-options 0x2, Metric 0
        Aging timer 00:42:56
        Installed 00:16:57 ago, expires in 00:42:57, sent 00:16:55 ago
        Last changed 2w6d 04:10:26 ago, Change count: 111
        IntraArPfx *0.0.0.1          111.87.5.252     0x8000178a  1510  0x9b24  76
        Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 111.87.5.252
        Prefix-count 3
        Prefix 2001:268:fb90:14::/64
            Prefix-options 0x0, Metric 5
        Prefix 2001:268:fb8f:1f::/64
            Prefix-options 0x0, Metric 100
        Prefix 2001:268:fb90::b/128
            Prefix-options 0x2, Metric 0
        Gen timer 00:24:49
        Aging timer 00:34:49
        Installed 00:25:10 ago, expires in 00:34:50, sent 00:25:08 ago
        Last changed 29w5d 21:40:56 ago, Change count: 2, Ours
        IntraArPfx  0.0.0.1          111.87.5.253     0x80001788   512  0x8820  76
        Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 111.87.5.253
        Prefix-count 3
        Prefix 2001:268:fb90:14::/64
            Prefix-options 0x0, Metric 5
        Prefix 2001:268:fb8f:21::/64
            Prefix-options 0x0, Metric 120
        Prefix 2001:268:fb90::c/128
            Prefix-options 0x2, Metric 0
        Aging timer 00:51:27
        Installed 00:08:29 ago, expires in 00:51:28, sent 00:08:27 ago
        Last changed 29w5d 21:33:18 ago, Change count: 1
            OSPF3 AS SCOPE link state database
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Extern      0.0.0.1          59.128.2.250     0x8000178e  1379  0x3c81  28
        Prefix ::/0
        Prefix-options 0x0, Metric 1, Type 1,
        Aging timer 00:37:01
        Installed 00:22:53 ago, expires in 00:37:01, sent 00:22:51 ago
        Last changed 29w5d 21:03:56 ago, Change count: 1
        Extern      0.0.0.3          59.128.2.250     0x8000178e  1004  0x21bf  44
        Prefix 2001:268:fb8f::2/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:43:16
        Installed 00:16:38 ago, expires in 00:43:16, sent 00:16:36 ago
        Last changed 29w5d 21:03:56 ago, Change count: 1
        Extern      0.0.0.4          59.128.2.250     0x80000246  2880  0xcc71  44
        Prefix 2001:268:fb8f::1/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:12:00
        Installed 00:47:53 ago, expires in 00:12:00, sent 00:47:51 ago
        Last changed 2w6d 04:50:27 ago, Change count: 1
        Extern      0.0.0.1          59.128.2.251     0x80001789  1379  0x4081  28
        Prefix ::/0
        Prefix-options 0x0, Metric 1, Type 1,
        Aging timer 00:37:01
        Installed 00:22:50 ago, expires in 00:37:01, sent 00:22:48 ago
        Last changed 29w5d 21:03:55 ago, Change count: 1
        Extern      0.0.0.2          59.128.2.251     0x80001788  2879  0x17d0  44
        Prefix 2001:268:fb8f::1/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:12:01
        Installed 00:47:50 ago, expires in 00:12:01, sent 00:47:48 ago
        Last changed 29w5d 21:03:55 ago, Change count: 1
        Extern      0.0.0.3          59.128.2.251     0x80000246   254  0xea52  44
        Prefix 2001:268:fb8f::2/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:55:46
        Installed 00:04:05 ago, expires in 00:55:46, sent 00:04:03 ago
        Last changed 2w6d 04:10:22 ago, Change count: 1
        Extern      0.0.0.18         106.187.14.240   0x80000349  1689  0xbddb  28
        Prefix ::/0
        Prefix-options 0x0, Metric 1, Type 1,
        Aging timer 00:31:50
        Installed 00:28:06 ago, expires in 00:31:51, sent 00:28:04 ago
        Last changed 4w1d 01:47:27 ago, Change count: 1
        Extern      0.0.0.19         106.187.14.240   0x8000034d   871  0x3603  44
        Prefix 2001:268:fa00:200::1001/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:45:28
        Installed 00:14:28 ago, expires in 00:45:29, sent 00:14:26 ago
        Last changed 3w3d 02:05:14 ago, Change count: 3
        Extern      0.0.0.22         106.187.14.240   0x800002b9  2235  0xab95  44
        Prefix 2001:268:fb90::b/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:22:45
        Installed 00:37:12 ago, expires in 00:22:45, sent 00:37:10 ago
        Last changed 3w0d 17:02:14 ago, Change count: 1
        Extern      0.0.0.23         106.187.14.240   0x80000247   598  0x7049  44
        Prefix 2001:268:fb80::14/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:50:01
        Installed 00:09:55 ago, expires in 00:50:02, sent 00:09:53 ago
        Last changed 2w6d 04:50:31 ago, Change count: 1
        Extern      0.0.0.24         106.187.14.240   0x80000246  2507  0x4e6c  44
        Prefix 2001:268:fb80::13/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:18:12
        Installed 00:41:44 ago, expires in 00:18:13, sent 00:41:42 ago
        Last changed 2w6d 04:50:25 ago, Change count: 1
        Extern      0.0.0.9          106.187.14.241   0x800002f0  2690  0xd341  44
        Prefix 2001:268:fb90::c/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:15:10
        Installed 00:44:44 ago, expires in 00:15:10, sent 00:44:42 ago
        Last changed 3w2d 03:23:47 ago, Change count: 11
        Extern      0.0.0.10         106.187.14.241   0x80000246   690  0xd4f2  44
        Prefix 2001:268:fb80::13/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:48:30
        Installed 00:11:24 ago, expires in 00:48:30, sent 00:11:22 ago
        Last changed 2w6d 04:10:26 ago, Change count: 1
        Extern      0.0.0.11         106.187.14.241   0x80000246    23  0xe4e0  44
        Prefix 2001:268:fb80::14/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:59:36
        Installed 00:00:17 ago, expires in 00:59:37, sent 00:00:15 ago
        Last changed 2w6d 04:10:20 ago, Change count: 1
        Extern     *0.0.0.1          111.87.5.252     0x8000063f  2010  0x3ff4  44
        Prefix 2001:268:fb8f::1/128
        Prefix-options 0x0, Metric 50, Type 1,
        Gen timer 00:16:29
        Aging timer 00:26:29
        Installed 00:33:30 ago, expires in 00:26:30, sent 00:33:28 ago
        Last changed 3w0d 17:02:14 ago, Change count: 2, Ours
        Extern      0.0.0.1          111.87.5.253     0x80000e1e  2012  0x7dcd  44
        Prefix 2001:268:fb8f::2/128
        Prefix-options 0x0, Metric 50, Type 1,
        Aging timer 00:26:27
        Installed 00:33:29 ago, expires in 00:26:28, sent 00:33:28 ago
        Last changed 3w3d 00:31:13 ago, Change count: 15

            OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.8
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Link       *0.0.0.2          111.87.5.252     0x8000178a   510  0xae5c  56
        fe80::250:56ff:fe8d:c829
        Options 0x33, Priority 128
        Prefix-count 1
        Prefix 2001:268:fb90:14::/64 Prefix-options 0x0
        Gen timer 00:41:29
        Aging timer 00:51:29
        Installed 00:08:30 ago, expires in 00:51:30, sent 00:08:28 ago
        Last changed 29w5d 21:40:56 ago, Change count: 1, Ours
        Link        0.0.0.2          111.87.5.253     0x80001787  2512  0x13d7  56
        fe80::250:56ff:fe8d:53c0
        Options 0x33, Priority 128
        Prefix-count 1
        Prefix 2001:268:fb90:14::/64 Prefix-options 0x0
        Aging timer 00:18:07
        Installed 00:41:49 ago, expires in 00:18:08
        Last changed 29w5d 21:33:17 ago, Change count: 1

            OSPF3 Link-Local database, interface ge-0/0/1.0 Area 0.0.0.8
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Link        0.0.0.3          106.187.14.240   0x8000179e  1144  0xbe92  56
        fe80::250:56ff:fe8d:72bd
        Options 0x33, Priority 128
        Prefix-count 1
        Prefix 2001:268:fb8f:1f::/64 Prefix-options 0x0
        Aging timer 00:40:56
        Installed 00:19:01 ago, expires in 00:40:56, sent 6w2d 02:47:58 ago
        Last changed 29w5d 21:33:04 ago, Change count: 1
        Link       *0.0.0.3          111.87.5.252     0x8000178a    10  0x5e7d  56
        fe80::250:56ff:fe8d:a96c
        Options 0x33, Priority 128
        Prefix-count 1
        Prefix 2001:268:fb8f:1f::/64 Prefix-options 0x0
        Gen timer 00:49:49
        Aging timer 00:59:49
        Installed 00:00:10 ago, expires in 00:59:50, sent 00:00:08 ago
        Last changed 29w5d 21:40:56 ago, Change count: 1, Ours

            OSPF3 Link-Local database, interface lo0.0 Area 0.0.0.8
        Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        Link       *0.0.0.1          111.87.5.252     0x8000178b  2510  0xa440  44
        fe80::250:560f:fc8d:7c08
        Options 0x33, Priority 128
        Prefix-count 0
        Gen timer 00:08:09
        Aging timer 00:18:09
        Installed 00:41:50 ago, expires in 00:18:10
        Last changed 29w5d 21:46:59 ago, Change count: 1, Ours

    '''}

    golden_parsed_output = {'ospf3-database-information': {'ospf3-area-header': {'ospf-area': '0.0.0.8'},
                                'ospf3-database': [{'advertising-router': '59.128.2.250',
                        'age': '2504',
                        'checksum': '0xaf2d',
                        'lsa-id': '0.0.0.0',
                        'lsa-length': '56',
                        'lsa-type': 'Router',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:18:16'},
                                                    'expiration-time': {'#text': '00:18:16'},
                                                    'installation-time': {'#text': '00:41:38'},
                                                    'lsa-change-count': '196',
                                                    'lsa-changed-time': {'#text': '2w6d '
                                                                                    '04:50:31'},
                                                    'send-time': {'#text': '00:41:36'}},
                        'ospf3-router-lsa': {'bits': '0x2',
                                                'ospf3-link': [{'link-intf-id': '2',
                                                                'link-metric': '5',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '2',
                                                                'nbr-rtr-id': '59.128.2.251'},
                                                            {'link-intf-id': '3',
                                                                'link-metric': '100',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '4',
                                                                'nbr-rtr-id': '106.187.14.240'}],
                                                'ospf3-lsa-topology': {'ospf-topology-id': '0',
                                                                    'ospf-topology-name': 'default',
                                                                    'ospf3-lsa-topology-link': [{'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '100',
                                                                                                    'ospf-lsa-topology-link-node-id': '106.187.14.240',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'},
                                                                                                {'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '5',
                                                                                                    'ospf-lsa-topology-link-node-id': '59.128.2.251',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'}]},
                                                'ospf3-options': '0x33'},
                        'sequence-number': '0x800018ed'},
                        {'advertising-router': '59.128.2.251',
                        'age': '629',
                        'checksum': '0x1d57',
                        'lsa-id': '0.0.0.0',
                        'lsa-length': '56',
                        'lsa-type': 'Router',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:49:31'},
                                                    'expiration-time': {'#text': '00:49:31'},
                                                    'installation-time': {'#text': '00:10:20'},
                                                    'lsa-change-count': '208',
                                                    'lsa-changed-time': {'#text': '2w6d '
                                                                                    '04:10:26'},
                                                    'send-time': {'#text': '00:10:18'}},
                        'ospf3-router-lsa': {'bits': '0x2',
                                                'ospf3-link': [{'link-intf-id': '2',
                                                                'link-metric': '5',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '2',
                                                                'nbr-rtr-id': '59.128.2.250'},
                                                            {'link-intf-id': '3',
                                                                'link-metric': '120',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '4',
                                                                'nbr-rtr-id': '106.187.14.241'}],
                                                'ospf3-lsa-topology': {'ospf-topology-id': '0',
                                                                    'ospf-topology-name': 'default',
                                                                    'ospf3-lsa-topology-link': [{'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '120',
                                                                                                    'ospf-lsa-topology-link-node-id': '106.187.14.241',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'},
                                                                                                {'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '5',
                                                                                                    'ospf-lsa-topology-link-node-id': '59.128.2.250',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'}]},
                                                'ospf3-options': '0x33'},
                        'sequence-number': '0x80001841'},
                        {'advertising-router': '106.187.14.240',
                        'age': '53',
                        'checksum': '0x50bb',
                        'lsa-id': '0.0.0.0',
                        'lsa-length': '72',
                        'lsa-type': 'Router',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:59:06'},
                                                    'expiration-time': {'#text': '00:59:07'},
                                                    'installation-time': {'#text': '00:00:50'},
                                                    'lsa-change-count': '341',
                                                    'lsa-changed-time': {'#text': '2w6d '
                                                                                    '04:50:31'},
                                                    'send-time': {'#text': '00:00:48'}},
                        'ospf3-router-lsa': {'bits': '0x2',
                                                'ospf3-link': [{'link-intf-id': '2',
                                                                'link-metric': '5',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '2',
                                                                'nbr-rtr-id': '106.187.14.241'},
                                                            {'link-intf-id': '3',
                                                                'link-metric': '100',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '3',
                                                                'nbr-rtr-id': '111.87.5.252'},
                                                            {'link-intf-id': '4',
                                                                'link-metric': '100',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '3',
                                                                'nbr-rtr-id': '59.128.2.250'}],
                                                'ospf3-lsa-topology': {'ospf-topology-id': '0',
                                                                    'ospf-topology-name': 'default',
                                                                    'ospf3-lsa-topology-link': [{'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '100',
                                                                                                    'ospf-lsa-topology-link-node-id': '59.128.2.250',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'},
                                                                                                {'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '100',
                                                                                                    'ospf-lsa-topology-link-node-id': '111.87.5.252',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'},
                                                                                                {'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '5',
                                                                                                    'ospf-lsa-topology-link-node-id': '106.187.14.241',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'}]},
                                                'ospf3-options': '0x33'},
                        'sequence-number': '0x80001a0c'},
                        {'advertising-router': '106.187.14.241',
                        'age': '1356',
                        'checksum': '0x94a3',
                        'lsa-id': '0.0.0.0',
                        'lsa-length': '72',
                        'lsa-type': 'Router',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:37:23'},
                                                    'expiration-time': {'#text': '00:37:24'},
                                                    'installation-time': {'#text': '00:22:30'},
                                                    'lsa-change-count': '280',
                                                    'lsa-changed-time': {'#text': '2w6d '
                                                                                    '04:10:26'},
                                                    'send-time': {'#text': '00:22:28'}},
                        'ospf3-router-lsa': {'bits': '0x2',
                                                'ospf3-link': [{'link-intf-id': '2',
                                                                'link-metric': '5',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '2',
                                                                'nbr-rtr-id': '106.187.14.240'},
                                                            {'link-intf-id': '3',
                                                                'link-metric': '120',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '3',
                                                                'nbr-rtr-id': '111.87.5.253'},
                                                            {'link-intf-id': '4',
                                                                'link-metric': '120',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '3',
                                                                'nbr-rtr-id': '59.128.2.251'}],
                                                'ospf3-lsa-topology': {'ospf-topology-id': '0',
                                                                    'ospf-topology-name': 'default',
                                                                    'ospf3-lsa-topology-link': [{'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '120',
                                                                                                    'ospf-lsa-topology-link-node-id': '59.128.2.251',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'},
                                                                                                {'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '120',
                                                                                                    'ospf-lsa-topology-link-node-id': '111.87.5.253',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'},
                                                                                                {'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '5',
                                                                                                    'ospf-lsa-topology-link-node-id': '106.187.14.240',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'}]},
                                                'ospf3-options': '0x33'},
                        'sequence-number': '0x800018b7'},
                        {'advertising-router': '111.87.5.252',
                        'age': '1010',
                        'checksum': '0xae6c',
                        'lsa-id': '0.0.0.0',
                        'lsa-length': '56',
                        'lsa-type': 'Router',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:43:09'},
                                                    'database-entry-state': 'Ours',
                                                    'expiration-time': {'#text': '00:43:10'},
                                                    'generation-timer': {'#text': '00:33:09'},
                                                    'installation-time': {'#text': '00:16:50'},
                                                    'lsa-change-count': '6',
                                                    'lsa-changed-time': {'#text': '3w0d '
                                                                                    '17:02:09'},
                                                    'send-time': {'#text': '00:16:48'}},
                        'ospf3-router-lsa': {'bits': '0x2',
                                                'ospf3-link': [{'link-intf-id': '2',
                                                                'link-metric': '5',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '2',
                                                                'nbr-rtr-id': '111.87.5.253'},
                                                            {'link-intf-id': '3',
                                                                'link-metric': '100',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '3',
                                                                'nbr-rtr-id': '106.187.14.240'}],
                                                'ospf3-lsa-topology': {'ospf-topology-id': '0',
                                                                    'ospf-topology-name': 'default',
                                                                    'ospf3-lsa-topology-link': [{'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '100',
                                                                                                    'ospf-lsa-topology-link-node-id': '106.187.14.240',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'},
                                                                                                {'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '5',
                                                                                                    'ospf-lsa-topology-link-node-id': '111.87.5.253',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'}]},
                                                'ospf3-options': '0x33'},
                        'our-entry': None,
                        'sequence-number': '0x80001890'},
                        {'advertising-router': '111.87.5.253',
                        'age': '1012',
                        'checksum': '0x8fdc',
                        'lsa-id': '0.0.0.0',
                        'lsa-length': '56',
                        'lsa-type': 'Router',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:43:07'},
                                                    'expiration-time': {'#text': '00:43:08'},
                                                    'installation-time': {'#text': '00:16:49'},
                                                    'lsa-change-count': '181',
                                                    'lsa-changed-time': {'#text': '3w0d '
                                                                                    '17:02:14'},
                                                    'send-time': {'#text': '00:16:48'}},
                        'ospf3-router-lsa': {'bits': '0x2',
                                                'ospf3-link': [{'link-intf-id': '2',
                                                                'link-metric': '5',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '2',
                                                                'nbr-rtr-id': '111.87.5.252'},
                                                            {'link-intf-id': '3',
                                                                'link-metric': '120',
                                                                'link-type-name': 'PointToPoint',
                                                                'link-type-value': '1',
                                                                'nbr-intf-id': '3',
                                                                'nbr-rtr-id': '106.187.14.241'}],
                                                'ospf3-lsa-topology': {'ospf-topology-id': '0',
                                                                    'ospf-topology-name': 'default',
                                                                    'ospf3-lsa-topology-link': [{'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '120',
                                                                                                    'ospf-lsa-topology-link-node-id': '106.187.14.241',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'},
                                                                                                {'link-type-name': 'PointToPoint',
                                                                                                    'ospf-lsa-topology-link-metric': '5',
                                                                                                    'ospf-lsa-topology-link-node-id': '111.87.5.252',
                                                                                                    'ospf-lsa-topology-link-state': 'Bidirectional'}]},
                                                'ospf3-options': '0x33'},
                        'sequence-number': '0x8000182a'},
                        {'advertising-router': '59.128.2.250',
                        'age': '1754',
                        'checksum': '0xc4fc',
                        'lsa-id': '0.0.0.1',
                        'lsa-length': '76',
                        'lsa-type': 'IntraArPfx',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:30:46'},
                                                    'expiration-time': {'#text': '00:30:46'},
                                                    'installation-time': {'#text': '00:29:08'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '29w5d '
                                                                                    '21:33:07'},
                                                    'send-time': {'#text': '00:29:06'}},
                        'ospf3-intra-area-prefix-lsa': {'ospf3-prefix': ['2001:268:fb80:3e::/64',
                                                                            '2001:268:fb8f:29::/64',
                                                                            '2001:268:fb80::13/128'],
                                                        'ospf3-prefix-metric': ['5',
                                                                                '100',
                                                                                '0'],
                                                        'ospf3-prefix-options': ['0x0',
                                                                                    '0x0',
                                                                                    '0x2'],
                                                        'prefix-count': '3',
                                                        'reference-lsa-id': '0.0.0.0',
                                                        'reference-lsa-router-id': '59.128.2.250',
                                                        'reference-lsa-type': 'Router'},
                        'sequence-number': '0x8000178c'},
                        {'advertising-router': '59.128.2.251',
                        'age': '1004',
                        'checksum': '0x9e2d',
                        'lsa-id': '0.0.0.1',
                        'lsa-length': '76',
                        'lsa-type': 'IntraArPfx',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:43:16'},
                                                    'expiration-time': {'#text': '00:43:16'},
                                                    'installation-time': {'#text': '00:16:35'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '29w5d '
                                                                                    '21:33:07'},
                                                    'send-time': {'#text': '00:16:33'}},
                        'ospf3-intra-area-prefix-lsa': {'ospf3-prefix': ['2001:268:fb80:3e::/64',
                                                                            '2001:268:fb8f:9::/64',
                                                                            '2001:268:fb80::14/128'],
                                                        'ospf3-prefix-metric': ['5',
                                                                                '120',
                                                                                '0'],
                                                        'ospf3-prefix-options': ['0x0',
                                                                                    '0x0',
                                                                                    '0x2'],
                                                        'prefix-count': '3',
                                                        'reference-lsa-id': '0.0.0.0',
                                                        'reference-lsa-router-id': '59.128.2.251',
                                                        'reference-lsa-type': 'Router'},
                        'sequence-number': '0x8000178b'},
                        {'advertising-router': '106.187.14.240',
                        'age': '2780',
                        'checksum': '0x6948',
                        'lsa-id': '0.0.0.1',
                        'lsa-length': '88',
                        'lsa-type': 'IntraArPfx',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:13:39'},
                                                    'expiration-time': {'#text': '00:13:40'},
                                                    'installation-time': {'#text': '00:46:17'},
                                                    'lsa-change-count': '147',
                                                    'lsa-changed-time': {'#text': '2w6d '
                                                                                    '04:50:31'},
                                                    'send-time': {'#text': '00:46:15'}},
                        'ospf3-intra-area-prefix-lsa': {'ospf3-prefix': ['2001:268:fb8f:5::/64',
                                                                            '2001:268:fb8f:1f::/64',
                                                                            '2001:268:fb8f:29::/64',
                                                                            '2001:268:fb8f::1/128'],
                                                        'ospf3-prefix-metric': ['5',
                                                                                '100',
                                                                                '100',
                                                                                '0'],
                                                        'ospf3-prefix-options': ['0x0',
                                                                                    '0x0',
                                                                                    '0x0',
                                                                                    '0x2'],
                                                        'prefix-count': '4',
                                                        'reference-lsa-id': '0.0.0.0',
                                                        'reference-lsa-router-id': '106.187.14.240',
                                                        'reference-lsa-type': 'Router'},
                        'sequence-number': '0x80001808'},
                        {'advertising-router': '106.187.14.241',
                        'age': '1023',
                        'checksum': '0xa81e',
                        'lsa-id': '0.0.0.1',
                        'lsa-length': '88',
                        'lsa-type': 'IntraArPfx',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:42:56'},
                                                    'expiration-time': {'#text': '00:42:57'},
                                                    'installation-time': {'#text': '00:16:57'},
                                                    'lsa-change-count': '111',
                                                    'lsa-changed-time': {'#text': '2w6d '
                                                                                    '04:10:26'},
                                                    'send-time': {'#text': '00:16:55'}},
                        'ospf3-intra-area-prefix-lsa': {'ospf3-prefix': ['2001:268:fb8f:5::/64',
                                                                            '2001:268:fb8f:21::/64',
                                                                            '2001:268:fb8f:9::/64',
                                                                            '2001:268:fb8f::2/128'],
                                                        'ospf3-prefix-metric': ['5',
                                                                                '120',
                                                                                '120',
                                                                                '0'],
                                                        'ospf3-prefix-options': ['0x0',
                                                                                    '0x0',
                                                                                    '0x0',
                                                                                    '0x2'],
                                                        'prefix-count': '4',
                                                        'reference-lsa-id': '0.0.0.0',
                                                        'reference-lsa-router-id': '106.187.14.241',
                                                        'reference-lsa-type': 'Router'},
                        'sequence-number': '0x800017e6'},
                        {'advertising-router': '111.87.5.252',
                        'age': '1510',
                        'checksum': '0x9b24',
                        'lsa-id': '0.0.0.1',
                        'lsa-length': '76',
                        'lsa-type': 'IntraArPfx',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:34:49'},
                                                    'database-entry-state': 'Ours',
                                                    'expiration-time': {'#text': '00:34:50'},
                                                    'generation-timer': {'#text': '00:24:49'},
                                                    'installation-time': {'#text': '00:25:10'},
                                                    'lsa-change-count': '2',
                                                    'lsa-changed-time': {'#text': '29w5d '
                                                                                    '21:40:56'},
                                                    'send-time': {'#text': '00:25:08'}},
                        'ospf3-intra-area-prefix-lsa': {'ospf3-prefix': ['2001:268:fb90:14::/64',
                                                                            '2001:268:fb8f:1f::/64',
                                                                            '2001:268:fb90::b/128'],
                                                        'ospf3-prefix-metric': ['5',
                                                                                '100',
                                                                                '0'],
                                                        'ospf3-prefix-options': ['0x0',
                                                                                    '0x0',
                                                                                    '0x2'],
                                                        'prefix-count': '3',
                                                        'reference-lsa-id': '0.0.0.0',
                                                        'reference-lsa-router-id': '111.87.5.252',
                                                        'reference-lsa-type': 'Router'},
                        'our-entry': None,
                        'sequence-number': '0x8000178a'},
                        {'advertising-router': '111.87.5.253',
                        'age': '512',
                        'checksum': '0x8820',
                        'lsa-id': '0.0.0.1',
                        'lsa-length': '76',
                        'lsa-type': 'IntraArPfx',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:51:27'},
                                                    'expiration-time': {'#text': '00:51:28'},
                                                    'installation-time': {'#text': '00:08:29'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '29w5d '
                                                                                    '21:33:18'},
                                                    'send-time': {'#text': '00:08:27'}},
                        'ospf3-intra-area-prefix-lsa': {'ospf3-prefix': ['2001:268:fb90:14::/64',
                                                                            '2001:268:fb8f:21::/64',
                                                                            '2001:268:fb90::c/128'],
                                                        'ospf3-prefix-metric': ['5',
                                                                                '120',
                                                                                '0'],
                                                        'ospf3-prefix-options': ['0x0',
                                                                                    '0x0',
                                                                                    '0x2'],
                                                        'prefix-count': '3',
                                                        'reference-lsa-id': '0.0.0.0',
                                                        'reference-lsa-router-id': '111.87.5.253',
                                                        'reference-lsa-type': 'Router'},
                        'sequence-number': '0x80001788'},
                        {'advertising-router': '59.128.2.250',
                        'age': '1379',
                        'checksum': '0x3c81',
                        'lsa-id': '0.0.0.1',
                        'lsa-length': '28',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:37:01'},
                                                    'expiration-time': {'#text': '00:37:01'},
                                                    'installation-time': {'#text': '00:22:53'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '29w5d '
                                                                                    '21:03:56'},
                                                    'send-time': {'#text': '00:22:51'}},
                        'ospf3-external-lsa': {'metric': '1',
                                                'ospf3-prefix': '::/0',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x8000178e'},
                        {'advertising-router': '59.128.2.250',
                        'age': '1004',
                        'checksum': '0x21bf',
                        'lsa-id': '0.0.0.3',
                        'lsa-length': '44',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:43:16'},
                                                    'expiration-time': {'#text': '00:43:16'},
                                                    'installation-time': {'#text': '00:16:38'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '29w5d '
                                                                                    '21:03:56'},
                                                    'send-time': {'#text': '00:16:36'}},
                        'ospf3-external-lsa': {'metric': '50',
                                                'ospf3-prefix': '2001:268:fb8f::2/128',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x8000178e'},
                        {'advertising-router': '59.128.2.250',
                        'age': '2880',
                        'checksum': '0xcc71',
                        'lsa-id': '0.0.0.4',
                        'lsa-length': '44',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:12:00'},
                                                    'expiration-time': {'#text': '00:12:00'},
                                                    'installation-time': {'#text': '00:47:53'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '2w6d '
                                                                                    '04:50:27'},
                                                    'send-time': {'#text': '00:47:51'}},
                        'ospf3-external-lsa': {'metric': '50',
                                                'ospf3-prefix': '2001:268:fb8f::1/128',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x80000246'},
                        {'advertising-router': '59.128.2.251',
                        'age': '1379',
                        'checksum': '0x4081',
                        'lsa-id': '0.0.0.1',
                        'lsa-length': '28',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:37:01'},
                                                    'expiration-time': {'#text': '00:37:01'},
                                                    'installation-time': {'#text': '00:22:50'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '29w5d '
                                                                                    '21:03:55'},
                                                    'send-time': {'#text': '00:22:48'}},
                        'ospf3-external-lsa': {'metric': '1',
                                                'ospf3-prefix': '::/0',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x80001789'},
                        {'advertising-router': '59.128.2.251',
                        'age': '2879',
                        'checksum': '0x17d0',
                        'lsa-id': '0.0.0.2',
                        'lsa-length': '44',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:12:01'},
                                                    'expiration-time': {'#text': '00:12:01'},
                                                    'installation-time': {'#text': '00:47:50'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '29w5d '
                                                                                    '21:03:55'},
                                                    'send-time': {'#text': '00:47:48'}},
                        'ospf3-external-lsa': {'metric': '50',
                                                'ospf3-prefix': '2001:268:fb8f::1/128',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x80001788'},
                        {'advertising-router': '59.128.2.251',
                        'age': '254',
                        'checksum': '0xea52',
                        'lsa-id': '0.0.0.3',
                        'lsa-length': '44',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:55:46'},
                                                    'expiration-time': {'#text': '00:55:46'},
                                                    'installation-time': {'#text': '00:04:05'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '2w6d '
                                                                                    '04:10:22'},
                                                    'send-time': {'#text': '00:04:03'}},
                        'ospf3-external-lsa': {'metric': '50',
                                                'ospf3-prefix': '2001:268:fb8f::2/128',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x80000246'},
                        {'advertising-router': '106.187.14.240',
                        'age': '1689',
                        'checksum': '0xbddb',
                        'lsa-id': '0.0.0.18',
                        'lsa-length': '28',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:31:50'},
                                                    'expiration-time': {'#text': '00:31:51'},
                                                    'installation-time': {'#text': '00:28:06'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '4w1d '
                                                                                    '01:47:27'},
                                                    'send-time': {'#text': '00:28:04'}},
                        'ospf3-external-lsa': {'metric': '1',
                                                'ospf3-prefix': '::/0',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x80000349'},
                        {'advertising-router': '106.187.14.240',
                        'age': '871',
                        'checksum': '0x3603',
                        'lsa-id': '0.0.0.19',
                        'lsa-length': '44',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:45:28'},
                                                    'expiration-time': {'#text': '00:45:29'},
                                                    'installation-time': {'#text': '00:14:28'},
                                                    'lsa-change-count': '3',
                                                    'lsa-changed-time': {'#text': '3w3d '
                                                                                    '02:05:14'},
                                                    'send-time': {'#text': '00:14:26'}},
                        'ospf3-external-lsa': {'metric': '50',
                                                'ospf3-prefix': '2001:268:fa00:200::1001/128',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x8000034d'},
                        {'advertising-router': '106.187.14.240',
                        'age': '2235',
                        'checksum': '0xab95',
                        'lsa-id': '0.0.0.22',
                        'lsa-length': '44',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:22:45'},
                                                    'expiration-time': {'#text': '00:22:45'},
                                                    'installation-time': {'#text': '00:37:12'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '3w0d '
                                                                                    '17:02:14'},
                                                    'send-time': {'#text': '00:37:10'}},
                        'ospf3-external-lsa': {'metric': '50',
                                                'ospf3-prefix': '2001:268:fb90::b/128',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x800002b9'},
                        {'advertising-router': '106.187.14.240',
                        'age': '598',
                        'checksum': '0x7049',
                        'lsa-id': '0.0.0.23',
                        'lsa-length': '44',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:50:01'},
                                                    'expiration-time': {'#text': '00:50:02'},
                                                    'installation-time': {'#text': '00:09:55'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '2w6d '
                                                                                    '04:50:31'},
                                                    'send-time': {'#text': '00:09:53'}},
                        'ospf3-external-lsa': {'metric': '50',
                                                'ospf3-prefix': '2001:268:fb80::14/128',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x80000247'},
                        {'advertising-router': '106.187.14.240',
                        'age': '2507',
                        'checksum': '0x4e6c',
                        'lsa-id': '0.0.0.24',
                        'lsa-length': '44',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:18:12'},
                                                    'expiration-time': {'#text': '00:18:13'},
                                                    'installation-time': {'#text': '00:41:44'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '2w6d '
                                                                                    '04:50:25'},
                                                    'send-time': {'#text': '00:41:42'}},
                        'ospf3-external-lsa': {'metric': '50',
                                                'ospf3-prefix': '2001:268:fb80::13/128',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x80000246'},
                        {'advertising-router': '106.187.14.241',
                        'age': '2690',
                        'checksum': '0xd341',
                        'lsa-id': '0.0.0.9',
                        'lsa-length': '44',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:15:10'},
                                                    'expiration-time': {'#text': '00:15:10'},
                                                    'installation-time': {'#text': '00:44:44'},
                                                    'lsa-change-count': '11',
                                                    'lsa-changed-time': {'#text': '3w2d '
                                                                                    '03:23:47'},
                                                    'send-time': {'#text': '00:44:42'}},
                        'ospf3-external-lsa': {'metric': '50',
                                                'ospf3-prefix': '2001:268:fb90::c/128',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x800002f0'},
                        {'advertising-router': '106.187.14.241',
                        'age': '690',
                        'checksum': '0xd4f2',
                        'lsa-id': '0.0.0.10',
                        'lsa-length': '44',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:48:30'},
                                                    'expiration-time': {'#text': '00:48:30'},
                                                    'installation-time': {'#text': '00:11:24'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '2w6d '
                                                                                    '04:10:26'},
                                                    'send-time': {'#text': '00:11:22'}},
                        'ospf3-external-lsa': {'metric': '50',
                                                'ospf3-prefix': '2001:268:fb80::13/128',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x80000246'},
                        {'advertising-router': '106.187.14.241',
                        'age': '23',
                        'checksum': '0xe4e0',
                        'lsa-id': '0.0.0.11',
                        'lsa-length': '44',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:59:36'},
                                                    'expiration-time': {'#text': '00:59:37'},
                                                    'installation-time': {'#text': '00:00:17'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '2w6d '
                                                                                    '04:10:20'},
                                                    'send-time': {'#text': '00:00:15'}},
                        'ospf3-external-lsa': {'metric': '50',
                                                'ospf3-prefix': '2001:268:fb80::14/128',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x80000246'},
                        {'advertising-router': '111.87.5.252',
                        'age': '2010',
                        'checksum': '0x3ff4',
                        'lsa-id': '0.0.0.1',
                        'lsa-length': '44',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:26:29'},
                                                    'database-entry-state': 'Ours',
                                                    'expiration-time': {'#text': '00:26:30'},
                                                    'generation-timer': {'#text': '00:16:29'},
                                                    'installation-time': {'#text': '00:33:30'},
                                                    'lsa-change-count': '2',
                                                    'lsa-changed-time': {'#text': '3w0d '
                                                                                    '17:02:14'},
                                                    'send-time': {'#text': '00:33:28'}},
                        'ospf3-external-lsa': {'metric': '50',
                                                'ospf3-prefix': '2001:268:fb8f::1/128',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'our-entry': None,
                        'sequence-number': '0x8000063f'},
                        {'advertising-router': '111.87.5.253',
                        'age': '2012',
                        'checksum': '0x7dcd',
                        'lsa-id': '0.0.0.1',
                        'lsa-length': '44',
                        'lsa-type': 'Extern',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:26:27'},
                                                    'expiration-time': {'#text': '00:26:28'},
                                                    'installation-time': {'#text': '00:33:29'},
                                                    'lsa-change-count': '15',
                                                    'lsa-changed-time': {'#text': '3w3d '
                                                                                    '00:31:13'},
                                                    'send-time': {'#text': '00:33:28'}},
                        'ospf3-external-lsa': {'metric': '50',
                                                'ospf3-prefix': '2001:268:fb8f::2/128',
                                                'ospf3-prefix-options': '0x0',
                                                'type-value': '1'},
                        'sequence-number': '0x80000e1e'},
                        {'advertising-router': '111.87.5.252',
                        'age': '510',
                        'checksum': '0xae5c',
                        'lsa-id': '0.0.0.2',
                        'lsa-length': '56',
                        'lsa-type': 'Link',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:51:29'},
                                                    'database-entry-state': 'Ours',
                                                    'expiration-time': {'#text': '00:51:30'},
                                                    'generation-timer': {'#text': '00:41:29'},
                                                    'installation-time': {'#text': '00:08:30'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '29w5d '
                                                                                    '21:40:56'},
                                                    'send-time': {'#text': '00:08:28'}},
                        'ospf3-link-lsa': {'linklocal-address': 'fe80::250:56ff:fe8d:c829',
                                            'ospf3-options': '0x33',
                                            'ospf3-prefix': '2001:268:fb90:14::/64',
                                            'ospf3-prefix-options': '0x0',
                                            'prefix-count': '1',
                                            'router-priority': '128'},
                        'our-entry': None,
                        'sequence-number': '0x8000178a'},
                        {'advertising-router': '111.87.5.253',
                        'age': '2512',
                        'checksum': '0x13d7',
                        'lsa-id': '0.0.0.2',
                        'lsa-length': '56',
                        'lsa-type': 'Link',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:18:07'},
                                                    'expiration-time': {'#text': '00:18:08'},
                                                    'installation-time': {'#text': '00:41:49'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '29w5d '
                                                                                    '21:33:17'}},
                        'ospf3-link-lsa': {'linklocal-address': 'fe80::250:56ff:fe8d:53c0',
                                            'ospf3-options': '0x33',
                                            'ospf3-prefix': '2001:268:fb90:14::/64',
                                            'ospf3-prefix-options': '0x0',
                                            'prefix-count': '1',
                                            'router-priority': '128'},
                        'sequence-number': '0x80001787'},
                        {'advertising-router': '106.187.14.240',
                        'age': '1144',
                        'checksum': '0xbe92',
                        'lsa-id': '0.0.0.3',
                        'lsa-length': '56',
                        'lsa-type': 'Link',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:40:56'},
                                                    'expiration-time': {'#text': '00:40:56'},
                                                    'installation-time': {'#text': '00:19:01'},
                                                    'lsa-change-count': '1',
                                                    'lsa-changed-time': {'#text': '29w5d '
                                                                                    '21:33:04'},
                                                    'send-time': {'#text': '6w2d '
                                                                            '02:47:58'}},
                        'ospf3-link-lsa': {'linklocal-address': 'fe80::250:56ff:fe8d:72bd',
                                            'ospf3-options': '0x33',
                                            'ospf3-prefix': '2001:268:fb8f:1f::/64',
                                            'ospf3-prefix-options': '0x0',
                                            'prefix-count': '1',
                                            'router-priority': '128'},
                        'sequence-number': '0x8000179e'},
                        {'advertising-router': '111.87.5.252',
                        'age': '10',
                        'checksum': '0x5e7d',
                        'lsa-id': '0.0.0.3',
                        'lsa-length': '56',
                        'lsa-type': 'Link',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:59:49'},
                                    'database-entry-state': 'Ours',
                                    'expiration-time': {'#text': '00:59:50'},
                                    'generation-timer': {'#text': '00:49:49'},
                                    'installation-time': {'#text': '00:00:10'},
                                    'lsa-change-count': '1',
                                    'lsa-changed-time': {'#text': '29w5d '
                                                                    '21:40:56'},
                                                    'send-time': {'#text': '00:00:08'}},
                        'ospf3-link-lsa': {'linklocal-address': 'fe80::250:56ff:fe8d:a96c',
                                            'ospf3-options': '0x33',
                                            'ospf3-prefix': '2001:268:fb8f:1f::/64',
                                            'ospf3-prefix-options': '0x0',
                                            'prefix-count': '1',
                                            'router-priority': '128'},
                        'our-entry': None,
                        'sequence-number': '0x8000178a'},
                        {'advertising-router': '111.87.5.252',
                        'age': '2510',
                        'checksum': '0xa440',
                        'lsa-id': '0.0.0.1',
                        'lsa-length': '44',
                        'lsa-type': 'Link',
                        'ospf-database-extensive': {'aging-timer': {'#text': '00:18:09'},
                                'database-entry-state': 'Ours',
                                'expiration-time': {'#text': '00:18:10'},
                                'generation-timer': {'#text': '00:08:09'},
                                'installation-time': {'#text': '00:41:50'},
                                'lsa-change-count': '1',
                                'lsa-changed-time': {'#text': '29w5d '
                                                                '21:46:59'}},
                        'ospf3-link-lsa': {'linklocal-address': 'fe80::250:560f:fc8d:7c08',
                                            'ospf3-options': '0x33',
                                            'prefix-count': '0',
                                            'router-priority': '128'},
                        'our-entry': None,
                        'sequence-number': '0x8000178b'}],
    'ospf3-intf-header': [{'ospf-area': '0.0.0.8',
                            'ospf-intf': 'ge-0/0/0.0'},
                            {'ospf-area': '0.0.0.8',
                            'ospf-intf': 'ge-0/0/1.0'},
                            {'ospf-area': '0.0.0.8',
                            'ospf-intf': 'lo0.0'}]}}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowOspf3DatabaseExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowOspf3DatabaseExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()