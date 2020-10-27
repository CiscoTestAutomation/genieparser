
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_mrib
from genie.libs.parser.iosxr.show_mrib import ShowMribVrfRoute,\
                                              ShowMribVrfRouteSummary


# ==================================================
#  Unit test for 'show mrib vrf <WORD> <WORD> route'
# ==================================================

class test_show_mrib_vrf_route(unittest.TestCase):

    '''Unit test for 'show mrib vrf <WORD> <WORD> route'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf':
            {'default':
                {'address_family':
                    {'ipv4':
                        {'multicast_group':
                            {'224.0.0.0/24':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:00:58'}}},
                            '224.0.0.0/4':
                                {'source_address':
                                    {'*':
                                        {'flags': 'C RPF P',
                                        'rpf_nbr': '0.0.0.0',
                                        'uptime': '00:00:58'}}},
                            '224.0.1.39':
                                {'source_address':
                                    {'*':
                                        {'flags': 'S P',
                                        'uptime': '00:00:58'}}},
                            '227.1.1.1':
                                {'source_address':
                                    {'*':
                                        {'flags': 'C RPF MD MH CD',
                                        'mdt_ifh': '0x803380',
                                        'mvpn_payload': 'ipv4',
                                        'mvpn_remote_tid': '0x0',
                                        'mvpn_tid': '0xe000001f',
                                        'outgoing_interface_list':
                                            {'Loopback0':
                                                {'flags': 'F NS',
                                                'uptime': '00:00:54'}},
                                        'rpf_nbr': '0.0.0.0',
                                        'uptime': '00:00:54'},
                                    '192.168.0.12':
                                        {'flags': 'RPF ME MH',
                                        'incoming_interface_list':
                                            {'Loopback0':
                                                {'flags': 'F NS',
                                                'uptime': '00:00:58',
                                                'rpf_nbr': '192.168.0.12',}},
                                        'mdt_ifh': '0x803380',
                                        'mvpn_payload': 'ipv4',
                                        'mvpn_remote_tid': '0x0',
                                        'mvpn_tid': '0xe000001f',
                                        'outgoing_interface_list':
                                            {'Loopback0':
                                                {'flags': 'F A',
                                                'uptime': '00:00:54'}},
                                        'rpf_nbr': '192.168.0.12',
                                        'uptime': '00:00:54'}}},
                            '232.0.0.0/8':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:00:58'}}},
                            '232.1.1.1':
                                {'source_address':
                                    {'172.16.1.2':
                                        {'flags': 'RPF',
                                        'incoming_interface_list':
                                            {'Bundle-Ether2.200':
                                                {'flags': 'A',
                                                'uptime': '1w3d',
                                                'rpf_nbr': '10.100.1.1',}},
                                        'outgoing_interface_list':
                                            {'Bundle-Ether1.100':
                                                {'flags': 'F NS',
                                                'uptime': '5d22h',
                                                'location': '0/12/CPU0'}},
                                        'rpf_nbr': '10.100.1.1',
                                        'uptime': '13w2d'}}},
                            '236.5.5.5':
                                {'source_address':
                                    {'*':
                                        {'flags': 'C RPF MD MH CD',
                                        'mdt_ifh': '0x803480',
                                        'mvpn_remote_tid': '0xe0800018',
                                        'mvpn_tid': '0xe0000018',
                                        'outgoing_interface_list':
                                            {'Loopback0':
                                                {'flags': 'F NS',
                                                'uptime': '00:00:54'}},
                                        'rpf_nbr': '0.0.0.0',
                                        'uptime': '00:00:54'},
                                    '192.168.0.12':
                                        {'flags': 'RPF ME MH',
                                        'incoming_interface_list':
                                            {'Loopback0':
                                                {'flags': 'F A',
                                                'uptime': '00:00:54',
                                                'rpf_nbr': '192.168.0.12',}},
                                        'mdt_ifh': '0x803480',
                                        'mvpn_remote_tid': '0xe0800018',
                                        'mvpn_tid': '0xe0000018',
                                        'outgoing_interface_list':
                                            {'Loopback0':
                                                {'flags': 'F A',
                                                'uptime': '00:00:54'}},
                                        'rpf_nbr': '192.168.0.12',
                                        'uptime': '00:00:54'},
                                    '192.168.0.22':
                                        {'flags': 'C RPF MD MH CD',
                                        'mdt_ifh': '0x803480',
                                        'mvpn_remote_tid': '0xe0800018',
                                        'mvpn_tid': '0xe0000018',
                                        'outgoing_interface_list':
                                            {'GigabitEthernet0/1/0/1':
                                                {'flags': 'NS',
                                                'uptime': '00:00:01'},
                                            'Loopback0':
                                                {'flags': 'F NS',
                                                'uptime': '00:00:13'}},
                                        'rpf_nbr': '10.121.1.22',
                                        'uptime': '00:00:13'}}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/1/CPU0:rtr1#show mrib vrf default ipv4 route
        Mon Nov  2 15:26:01.015 PST

        IP Multicast Routing Information Base
        Entry flags: L - Domain-Local Source, E - External Source to the Domain,
        C - Directly-Connected Check, S - Signal, IA - Inherit Accept,
        IF - Inherit From, D - Drop, ME - MDT Encap, EID - Encap ID,
        MD - MDT Decap, MT - MDT Threshold Crossed, MH - MDT interface handle
        CD - Conditional Decap, MPLS - MPLS Decap, EX - Extranet
        MoFE - MoFRR Enabled, MoFS - MoFRR State, MoFP - MoFRR Primary
        MoFB - MoFRR Backup, RPFID - RPF ID Set, X - VXLAN
        Interface flags: F - Forward, A - Accept, IC - Internal Copy,
        NS - Negate Signal, DP - Don't Preserve, SP - Signal Present,
        II - Internal Interest, ID - Internal Disinterest, LI - Local Interest,
        LD - Local Disinterest, DI - Decapsulation Interface
        EI - Encapsulation Interface, MI - MDT Interface, LVIF - MPLS Encap,
        EX - Extranet, A2 - Secondary Accept, MT - MDT Threshold Crossed,
        MA - Data MDT Assigned, LMI - mLDP MDT Interface, TMI - P2MP-TE MDT Interface
        IRMI - IR MDT Interface

        (*,224.0.0.0/4) RPF nbr: 0.0.0.0 Flags: C RPF P
            Up: 00:00:58

        (*,224.0.0.0/24) Flags: D P
            Up: 00:00:58

        (*,224.0.1.39) Flags: S P
            Up: 00:00:58

        (*,227.1.1.1) RPF nbr: 0.0.0.0 Flags: C RPF MD MH CD
            MVPN TID: 0xe000001f
            MVPN Remote TID: 0x0
            MVPN Payload: IPv4
            MDT IFH: 0x803380
            Up: 00:00:54
            Outgoing Interface List
                Loopback0 Flags: F NS, Up: 00:00:54

        (192.168.0.12,227.1.1.1) RPF nbr: 192.168.0.12 Flags: RPF ME MH
            MVPN TID: 0xe000001f
            MVPN Remote TID: 0x0
            MVPN Payload: IPv4
            MDT IFH: 0x803380
            Up: 00:00:54
            Incoming Interface List
                Loopback0 Flags: F NS, Up: 00:00:58
            Outgoing Interface List
                Loopback0 Flags: F A, Up: 00:00:54

        (*,232.0.0.0/8) Flags: D P
            Up: 00:00:58

        (172.16.1.2,232.1.1.1) RPF nbr: 10.100.1.1 Flags: RPF
            Up: 13w2d
            Incoming Interface List
                Bundle-Ether2.200 Flags: A, Up: 1w3d
            Outgoing Interface List
                Bundle-Ether1.100 (0/12/CPU0) Flags: F NS, Up: 5d22h

        (*,236.5.5.5) RPF nbr: 0.0.0.0 Flags: C RPF MD MH CD
            MVPN TID: 0xe0000018
            MVPN Remote TID: 0xe0800018
            MVPN Payload: IPv4 IPv6
            MDT IFH: 0x803480
            Up: 00:00:54
            Outgoing Interface List
                Loopback0 Flags: F NS, Up: 00:00:54

        (192.168.0.12,236.5.5.5) RPF nbr: 192.168.0.12 Flags: RPF ME MH
            MVPN TID: 0xe0000018
            MVPN Remote TID: 0xe0800018
            MVPN Payload: IPv4 IPv6
            MDT IFH: 0x803480
            Up: 00:00:54
            Incoming Interface List
            Loopback0 Flags: F A, Up: 00:00:54
            Outgoing Interface List
                Loopback0 Flags: F A, Up: 00:00:54

        (192.168.0.22,236.5.5.5) RPF nbr: 10.121.1.22 Flags: C RPF MD MH CD
            MVPN TID: 0xe0000018
            MVPN Remote TID: 0xe0800018
            MVPN Payload: IPv4 IPv6
            MDT IFH: 0x803480
            Up: 00:00:13
            Outgoing Interface List
                Loopback0 Flags: F NS, Up: 00:00:13
                GigabitEthernet0/1/0/1 Flags: NS, Up: 00:00:01
        '''}

    golden_parsed_output2 = {
        'vrf':
            {'vpn1':
                {'address_family':
                    {'ipv6':
                        {'multicast_group':
                            {'ff00::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff00::/8':
                                {'source_address':
                                    {'*':
                                        {'flags': 'L C RPF P',
                                        'outgoing_interface_list':
                                            {'Decaps6tunnel0':
                                                {'flags': 'NS DI',
                                                'uptime': '00:04:40'}},
                                        'rpf_nbr': '2001:db8:b901:0:150:150:150:150',
                                        'uptime': '00:04:45'}}},
                            'ff02::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff10::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff12::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff15::1:1':
                                {'source_address':
                                    {'2001:db8:1:0:1:1:1:2':
                                        {'flags': 'L RPF MT',
                                        'incoming_interface_list':
                                            {'GigabitEthernet150/0/0/6':
                                                {'flags': 'A',
                                                'uptime': '00:02:53',
                                                'rpf_nbr': '2001:db8:1:0:1:1:1:2'}},
                                        'mt_slot': '0/2/CPU0',
                                        'outgoing_interface_list':
                                            {'mdtvpn1':
                                                {'flags': 'F NS MI MT MA',
                                                'uptime': '00:02:53'}},
                                        'rpf_nbr': '2001:db8:1:0:1:1:1:2',
                                        'uptime': '00:02:53'}}},
                            'ff15::2:1':
                                {'source_address':
                                    {'2001:db8:10:0:4:4:4:5':
                                        {'flags': 'L RPF',
                                        'incoming_interface_list':
                                            {'mdtvpn1':
                                                {'flags': 'A MI',
                                                'uptime': '00:03:35',
                                                'rpf_nbr': '::ffff:192.168.195.200'}},
                                        'outgoing_interface_list':
                                            {'GigabitEthernet150/0/0/6':
                                                {'flags': 'F NS',
                                                'uptime': '00:03:59'}},
                                        'rpf_nbr': '::ffff:192.168.195.200',
                                        'uptime': '00:03:59'}}},
                            'ff20::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff22::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff30::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff32::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff33::/32':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff34::/32':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff35::/32':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff36::/32':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff37::/32':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff38::/32':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff39::/32':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff3a::/32':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff3b::/32':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff3c::/32':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff3d::/32':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff3e::/32':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff3f::/32':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff40::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff42::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff50::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff52::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff60::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff62::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff70::/12':
                                {'source_address':
                                    {'*':
                                        {'flags': 'C RPF P',
                                        'rpf_nbr': '::',
                                        'uptime': '00:04:45'}}},
                            'ff70::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff72::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff80::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff82::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff90::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ff92::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ffa0::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ffa2::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ffb0::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ffb2::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ffc0::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ffc2::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ffd0::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ffd2::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ffe0::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'ffe2::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'fff0::/12':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'fff0::/15':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}},
                            'fff2::/16':
                                {'source_address':
                                    {'*':
                                        {'flags': 'D P',
                                        'uptime': '00:04:45'}}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        RP/0/1/CPU0:rtr1#show mrib vrf vpn1 ipv6 route
        Mon Nov  2 15:26:01.015 PST

        IP Multicast Routing Information Base
        Entry flags: L - Domain-Local Source, E - External Source to the Domain,
            C - Directly-Connected Check, S - Signal, IA - Inherit Accept,
            IF - Inherit From, D - Drop, ME - MDT Encap, EID - Encap ID,
            MD - MDT Decap, MT - MDT Threshold Crossed, MH - MDT interface handle
            CD - Conditional Decap, MPLS - MPLS Decap, EX - Extranet
            MoFE - MoFRR Enabled, MoFS - MoFRR State, MoFP - MoFRR Primary
            MoFB - MoFRR Backup, RPFID - RPF ID Set, X - VXLAN
        Interface flags: F - Forward, A - Accept, IC - Internal Copy,
            NS - Negate Signal, DP - Don't Preserve, SP - Signal Present,
            II - Internal Interest, ID - Internal Disinterest, LI - Local Interest,
            LD - Local Disinterest, DI - Decapsulation Interface
            EI - Encapsulation Interface, MI - MDT Interface, LVIF - MPLS Encap,
            EX - Extranet, A2 - Secondary Accept, MT - MDT Threshold Crossed,
            MA - Data MDT Assigned, LMI - mLDP MDT Interface, TMI - P2MP-TE MDT Interface
            IRMI - IR MDT Interface

        (*,ff00::/8)
          RPF nbr: 2001:db8:b901:0:150:150:150:150 Flags: L C RPF P
          Up: 00:04:45
          Outgoing Interface List
            Decaps6tunnel0 Flags: NS DI, Up: 00:04:40

        (*,ff00::/15)
          Flags: D P
          Up: 00:04:45

        (*,ff02::/16)
          Flags: D P
          Up: 00:04:45

        (*,ff10::/15)
          Flags: D P
          Up: 00:04:45

        (*,ff12::/16)
          Flags: D P
          Up: 00:04:45

        (2001:db8:1:0:1:1:1:2,ff15::1:1)
          RPF nbr: 2001:db8:1:0:1:1:1:2 Flags: L RPF MT
          MT Slot: 0/2/CPU0
          Up: 00:02:53
          Incoming Interface List
            GigabitEthernet150/0/0/6 Flags: A, Up: 00:02:53
          Outgoing Interface List
            mdtvpn1 Flags: F NS MI MT MA, Up: 00:02:53

        (2001:db8:10:0:4:4:4:5,ff15::2:1)
          RPF nbr: ::ffff:192.168.195.200 Flags: L RPF
          Up: 00:03:59
          Incoming Interface List
            mdtvpn1 Flags: A MI, Up: 00:03:35
          Outgoing Interface List
            GigabitEthernet150/0/0/6 Flags: F NS, Up: 00:03:59

        (*,ff20::/15)
          Flags: D P
          Up: 00:04:45

        (*,ff22::/16)
          Flags: D P
          Up: 00:04:45

        (*,ff30::/15)
          Flags: D P
          Up: 00:04:45

        (*,ff32::/16)
          Flags: D P
          Up: 00:04:45

        (*,ff33::/32)
          Flags: D P
          Up: 00:04:45
        (*,ff34::/32)
          Flags: D P
          Up: 00:04:45

        (*,ff35::/32)
          Flags: D P
          Up: 00:04:45

        (*,ff36::/32)
          Flags: D P
          Up: 00:04:45

        (*,ff37::/32)
          Flags: D P
          Up: 00:04:45

        (*,ff38::/32)
          Flags: D P
          Up: 00:04:45

        (*,ff39::/32)
          Flags: D P
          Up: 00:04:45

        (*,ff3a::/32)
          Flags: D P
          Up: 00:04:45

        (*,ff3b::/32)
          Flags: D P
          Up: 00:04:45

        (*,ff3c::/32)
          Flags: D P
          Up: 00:04:45

        (*,ff3d::/32)
          Flags: D P
          Up: 00:04:45

        (*,ff3e::/32)
          Flags: D P
          Up: 00:04:45

        (*,ff3f::/32)
          Flags: D P
          Up: 00:04:45

        (*,ff40::/15)
          Flags: D P
          Up: 00:04:45

        (*,ff42::/16)
          Flags: D P
          Up: 00:04:45

        (*,ff50::/15)
          Flags: D P
          Up: 00:04:45

        (*,ff52::/16)
          Flags: D P
          Up: 00:04:45

        (*,ff60::/15)
          Flags: D P
          Up: 00:04:45

        (*,ff62::/16)
          Flags: D P
          Up: 00:04:45

        (*,ff70::/12)
          RPF nbr: :: Flags: C RPF P
          Up: 00:04:45

        (*,ff70::/15)
          Flags: D P
          Up: 00:04:45

        (*,ff72::/16)
          Flags: D P
          Up: 00:04:45

        (*,ff80::/15)
          Flags: D P
          Up: 00:04:45

        (*,ff82::/16)
          Flags: D P
          Up: 00:04:45

        (*,ff90::/15)
          Flags: D P
          Up: 00:04:45

        (*,ff92::/16)
          Flags: D P
          Up: 00:04:45

        (*,ffa0::/15)
          Flags: D P
          Up: 00:04:45

        (*,ffa2::/16)
          Flags: D P
          Up: 00:04:45

        (*,ffb0::/15)
          Flags: D P
          Up: 00:04:45

        (*,ffb2::/16)
          Flags: D P
          Up: 00:04:45

        (*,ffc0::/15)
          Flags: D P
          Up: 00:04:45

        (*,ffc2::/16)
          Flags: D P
          Up: 00:04:45

        (*,ffd0::/15)
          Flags: D P
          Up: 00:04:45

        (*,ffd2::/16)
          Flags: D P
          Up: 00:04:45

        (*,ffe0::/15)
          Flags: D P
          Up: 00:04:45

        (*,ffe2::/16)
          Flags: D P
          Up: 00:04:45

        (*,fff0::/12)
          Flags: D P
          Up: 00:04:45

        (*,fff0::/15)
          Flags: D P
          Up: 00:04:45

        (*,fff2::/16)
          Flags: D P
          Up: 00:04:45
        '''}

    def test_show_mrib_vrf_route_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMribVrfRoute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_mrib_vrf_default_ipv4_route_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowMribVrfRoute(device=self.device)
        parsed_output = obj.parse(vrf='default', af='ipv4')
        self.assertEqual(parsed_output,self.golden_parsed_output1)

    def test_show_mrib_vrf_nondefault_ipv6_route_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowMribVrfRoute(device=self.device)
        parsed_output = obj.parse(vrf='vpn1', af='ipv6')
        self.assertEqual(parsed_output,self.golden_parsed_output2)


# ===================================================================
#  Unit test for 'show mrib vrf <vrf> <address-family> route summary'
# ===================================================================

class test_show_mrib_vrf_route_summary(unittest.TestCase):
    '''Unit test for "show mrib vrf <vrf> <address-family> route summary"'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'vrf': {
            'vrf_104': {
                'address_family': {
                    'ipv4': {
                        'no_group_ranges': 5,
                        'no_g_routes': 1,
                        'no_s_g_routes': 100,
                        'no_route_x_interfaces': 100,
                        'total_no_interfaces': 202}}}}}

    golden_output1 = {'execute.return_value': '''
        show mrib vrf vrf_104 ipv4 route summary

            Thu Oct  8 15:08:46.116 UTC
            MRIB Route Summary for VRF vrf_104
                No. of group ranges = 5
                No. of (*,G) routes = 1
                No. of (S,G) routes = 100
                No. of Route x Interfaces (RxI) = 100
                Total No. of Interfaces in all routes = 202
        '''}

    def test_show_mrib_vrf_route_summary_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMribVrfRouteSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_mrib_vrf_ipv4_route_summary_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowMribVrfRouteSummary(device=self.device)
        parsed_output = obj.parse(vrf='vrf_104', af='ipv4')
        self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()
