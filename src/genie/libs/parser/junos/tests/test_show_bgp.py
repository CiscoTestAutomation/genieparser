
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# junos show_ospf
from genie.libs.parser.junos.show_bgp import (ShowBgpGroupBrief,
                                              ShowBgpGroupDetail)


class TestShowBgpGroupBrief(unittest.TestCase):
    """ Unit tests for:
            * show bgp group brief | no-more
    """
    maxDiff = None
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: Genie       Index: 0                   Flags: <Export Eval>
        Export: [ (v4_WATARI && NEXT-HOP-SELF) ] 
        Options: <Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 1
        10.189.5.253+179
        inet.0: 0/682/682/0

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v6_Genie    Index: 1                   Flags: <Export Eval>
        Export: [ (v6_WATARI && NEXT-HOP-SELF) ] 
        Options: <Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 1
        2001:db8:223c:ca45::c+60268
        inet6.0: 0/0/0/0

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v4_RRC_72_TRIANGLE Index: 2                Flags: <Export Eval>
        Export: [ (ALL_out && v4_NEXT-HOP-SELF_hktGCS001) ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 3        Established: 0
        10.189.5.245+179
        10.189.5.243+179
        10.189.5.242+179

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v6_RRC_72_TRIANGLE Index: 3                Flags: <Export Eval>
        Export: [ (ALL_out && v6_NEXT-HOP-SELF_hktGCS001) ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 2        Established: 0  
        2001:db8:223c:ca45::7+179
        2001:db8:223c:ca45::8

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v6_RRC_72_SQUARE Index: 4                  Flags: <Export Eval>
        Export: [ ALL_out ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 2        Established: 0
        2001:db8:223c:ca45::9
        2001:db8:223c:ca45::a

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v4_RRC_72_SQUARE Index: 5                  Flags: <Export Eval>
        Export: [ ALL_out ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 2        Established: 0
        10.189.5.241+179
        10.189.5.240

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v4_Kentik       Index: 6                   Flags: <Export Eval>
        Export: [ v4_Kentik_NO-DEFAULT ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        10.49.216.179

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v6_Kentik       Index: 7                   Flags: <Export Eval>
        Export: [ v6_Kentik_NO-DEFAULT ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0                           
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        2001:db8:6be:89bb::1:140

        Group Type: External                               Local AS: 65171
        Name: sggjbb001       Index: 8                   Flags: <Export Eval>
        Export: [ (ALL_out && (NEXT-HOP-SELF && HKG-SNG_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        10.189.6.250

        Group Type: External                               Local AS: 65171
        Name: v6_sggjbb001    Index: 9                   Flags: <Export Eval>
        Export: [ (ALL_out && (NEXT-HOP-SELF && v6_HKG-SNG_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        2001:db8:5961:ca45::1

        Group Type: External                               Local AS: 65171
        Name: sjkGCS001-EC11  Index: 10                  Flags: <Export Eval>
        Export: [ ((LABELSTACK_O2B || HKG-EC_out) && (NEXT-HOP-SELF && HKG-EC_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 1
        10.169.14.240+60606
        inet.0: 682/684/684/0
        inet.3: 2/2/2/0

        Group Type: External                               Local AS: 65171
        Name: v6_sjkGCS001-EC11 Index: 11                Flags: <Export Eval>
        Export: [ (v6_HKG-EC_out && (NEXT-HOP-SELF && v6_HKG-EC_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>        
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 1
        2001:db8:eb18:ca45::1+179
        inet6.0: 0/0/0/0

        Group Type: External                               Local AS: 65171
        Name: obpGCS001-WC11  Index: 12                  Flags: <Export Eval>
        Export: [ (HKG-WC_out && (NEXT-HOP-SELF && HKG-WC_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        10.169.14.249

        Group Type: External                               Local AS: 65171
        Name: v6_obpGCS001-WC11 Index: 13                Flags: <Export Eval>
        Export: [ (v6_HKG-WC_out && (NEXT-HOP-SELF && v6_HKG-WC_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        2001:db8:eb18:ca45::11

        Groups: 14 Peers: 19   External: 6    Internal: 13   Down peers: 15  Flaps: 359
        Table          Tot Paths  Act Paths Suppressed    History Damp State    Pending
        inet.0               
                            1366        682          0          0          0          0
        inet.3               
                            2          2          0          0          0          0
        inet6.0              
                            0          0          0          0          0          0
    '''}

    golden_parsed_output = {
        "bgp-group-information": {
            "bgp-group": [
                {
                    "bgp-option-information": {
                        "bgp-options": "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v4_WATARI && NEXT-HOP-SELF)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "682",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "0",
                            "name": "inet.0",
                            "received-prefix-count": "682"
                        }
                    ],
                    "established-count": "1",
                    "group-flags": "Export Eval",
                    "group-index": "0",
                    "local-as": "65171",
                    "name": "Genie",
                    "peer-address": [
                        "10.189.5.253+179"
                    ],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v6_WATARI && NEXT-HOP-SELF)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "0",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "0",
                            "name": "inet6.0",
                            "received-prefix-count": "0"
                        }
                    ],
                    "established-count": "1",
                    "group-flags": "Export Eval",
                    "group-index": "1",
                    "local-as": "65171",
                    "name": "v6_Genie",
                    "peer-address": [
                        "2001:db8:223c:ca45::c+60268"
                    ],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && v4_NEXT-HOP-SELF_hktGCS001)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "2",
                    "local-as": "65171",
                    "name": "v4_RRC_72_TRIANGLE",
                    "peer-address": [
                        "10.189.5.245+179",
                        "10.189.5.243+179",
                        "10.189.5.242+179"
                    ],
                    "peer-as": "65171",
                    "peer-count": "3",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && v6_NEXT-HOP-SELF_hktGCS001)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "3",
                    "local-as": "65171",
                    "name": "v6_RRC_72_TRIANGLE",
                    "peer-address": [
                        "2001:db8:223c:ca45::7+179",
                        "2001:db8:223c:ca45::8"
                    ],
                    "peer-as": "65171",
                    "peer-count": "2",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "ALL_out",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "4",
                    "local-as": "65171",
                    "name": "v6_RRC_72_SQUARE",
                    "peer-address": [
                        "2001:db8:223c:ca45::9",
                        "2001:db8:223c:ca45::a"
                    ],
                    "peer-as": "65171",
                    "peer-count": "2",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "ALL_out",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "5",
                    "local-as": "65171",
                    "name": "v4_RRC_72_SQUARE",
                    "peer-address": [
                        "10.189.5.241+179",
                        "10.189.5.240"
                    ],
                    "peer-as": "65171",
                    "peer-count": "2",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "v4_Kentik_NO-DEFAULT",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "6",
                    "local-as": "65171",
                    "name": "v4_Kentik",
                    "peer-address": [
                        "10.49.216.179"
                    ],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "v6_Kentik_NO-DEFAULT",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "7",
                    "local-as": "65171",
                    "name": "v6_Kentik",
                    "peer-address": [
                        "2001:db8:6be:89bb::1:140"
                    ],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && (NEXT-HOP-SELF && HKG-SNG_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "8",
                    "local-as": "65171",
                    "name": "sggjbb001",
                    "peer-address": [
                        "10.189.6.250"
                    ],
                    "peer-count": "1",
                    "type": "External"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && (NEXT-HOP-SELF && v6_HKG-SNG_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "9",
                    "local-as": "65171",
                    "name": "v6_sggjbb001",
                    "peer-address": [
                        "2001:db8:5961:ca45::1"
                    ],
                    "peer-count": "1",
                    "type": "External"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "((LABELSTACK_O2B || HKG-EC_out) && (NEXT-HOP-SELF && HKG-EC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "684",
                            "active-prefix-count": "682",
                            "advertised-prefix-count": "0",
                            "name": "inet.0",
                            "received-prefix-count": "684"
                        },
                        {
                            "accepted-prefix-count": "2",
                            "active-prefix-count": "2",
                            "advertised-prefix-count": "0",
                            "name": "inet.3",
                            "received-prefix-count": "2"
                        }
                    ],
                    "established-count": "1",
                    "group-flags": "Export Eval",
                    "group-index": "10",
                    "local-as": "65171",
                    "name": "sjkGCS001-EC11",
                    "peer-address": [
                        "10.169.14.240+60606"
                    ],
                    "peer-count": "1",
                    "type": "External"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v6_HKG-EC_out && (NEXT-HOP-SELF && v6_HKG-EC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "0",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "0",
                            "name": "inet6.0",
                            "received-prefix-count": "0"
                        }
                    ],
                    "established-count": "1",
                    "group-flags": "Export Eval",
                    "group-index": "11",
                    "local-as": "65171",
                    "name": "v6_sjkGCS001-EC11",
                    "peer-address": [
                        "2001:db8:eb18:ca45::1+179"
                    ],
                    "peer-count": "1",
                    "type": "External"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(HKG-WC_out && (NEXT-HOP-SELF && HKG-WC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "12",
                    "local-as": "65171",
                    "name": "obpGCS001-WC11",
                    "peer-address": [
                        "10.169.14.249"
                    ],
                    "peer-count": "1",
                    "type": "External"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v6_HKG-WC_out && (NEXT-HOP-SELF && v6_HKG-WC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "13",
                    "local-as": "65171",
                    "name": "v6_obpGCS001-WC11",
                    "peer-address": [
                        "2001:db8:eb18:ca45::11"
                    ],
                    "peer-count": "1",
                    "type": "External"
                }
            ],
            "bgp-information": {
                "bgp-rib": [
                    {
                        "active-prefix-count": "682",
                        "damped-prefix-count": "0",
                        "history-prefix-count": "0",
                        "name": "inet.0",
                        "pending-prefix-count": "0",
                        "suppressed-prefix-count": "0",
                        "total-prefix-count": "1366"
                    },
                    {
                        "active-prefix-count": "2",
                        "damped-prefix-count": "0",
                        "history-prefix-count": "0",
                        "name": "inet.3",
                        "pending-prefix-count": "0",
                        "suppressed-prefix-count": "0",
                        "total-prefix-count": "2"
                    },
                    {
                        "active-prefix-count": "0",
                        "damped-prefix-count": "0",
                        "history-prefix-count": "0",
                        "name": "inet6.0",
                        "pending-prefix-count": "0",
                        "suppressed-prefix-count": "0",
                        "total-prefix-count": "0"
                    }
                ],
                "down-peer-count": "15",
                "external-peer-count": "6",
                "flap-count": "359",
                "group-count": "14",
                "internal-peer-count": "13",
                "peer-count": "19"
            }
        }
    }
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpGroupBrief(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpGroupBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

class TestShowBgpGroupDetail(unittest.TestCase):
    """ Unit tests for:
            * show bgp group detail | no-more
    """
    maxDiff = None
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: Genie       Index: 0                   Flags: <Export Eval>
        Export: [ (v4_WATARI && NEXT-HOP-SELF) ] 
        Options: <Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 1
        10.189.5.253+179
        Route Queue Timer: unset Route Queue: empty
        Table inet.0
            Active prefixes:              0
            Received prefixes:            682
            Accepted prefixes:            682
            Suppressed due to damping:    0
            Advertised prefixes:          682

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v6_Genie    Index: 1                   Flags: <Export Eval>
        Export: [ (v6_WATARI && NEXT-HOP-SELF) ] 
        Options: <Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 1
        2001:db8:223c:ca45::c+60268
        Route Queue Timer: unset Route Queue: empty
        Table inet6.0
            Active prefixes:              0
            Received prefixes:            0
            Accepted prefixes:            0
            Suppressed due to damping:    0
            Advertised prefixes:          0

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v4_RRC_72_TRIANGLE Index: 2                Flags: <Export Eval>
        Export: [ (ALL_out && v4_NEXT-HOP-SELF_hktGCS001) ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 3        Established: 0  
        10.189.5.245
        10.189.5.243
        10.189.5.242+179

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v6_RRC_72_TRIANGLE Index: 3                Flags: <Export Eval>
        Export: [ (ALL_out && v6_NEXT-HOP-SELF_hktGCS001) ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 2        Established: 0
        2001:db8:223c:ca45::7+179
        2001:db8:223c:ca45::8+179

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v6_RRC_72_SQUARE Index: 4                  Flags: <Export Eval>
        Export: [ ALL_out ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 2        Established: 0
        2001:db8:223c:ca45::9
        2001:db8:223c:ca45::a+179

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v4_RRC_72_SQUARE Index: 5                  Flags: <Export Eval>
        Export: [ ALL_out ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 2        Established: 0
        10.189.5.241+179
        10.189.5.240

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v4_Kentik       Index: 6                   Flags: <Export Eval>
        Export: [ v4_Kentik_NO-DEFAULT ] 
        Options: <Cluster Confed>             
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        10.49.216.179

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v6_Kentik       Index: 7                   Flags: <Export Eval>
        Export: [ v6_Kentik_NO-DEFAULT ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        2001:db8:6be:89bb::1:140

        Group Type: External                               Local AS: 65171
        Name: sggjbb001       Index: 8                   Flags: <Export Eval>
        Export: [ (ALL_out && (NEXT-HOP-SELF && HKG-SNG_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        10.189.6.250

        Group Type: External                               Local AS: 65171
        Name: v6_sggjbb001    Index: 9                   Flags: <Export Eval>
        Export: [ (ALL_out && (NEXT-HOP-SELF && v6_HKG-SNG_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        2001:db8:5961:ca45::1

        Group Type: External                               Local AS: 65171
        Name: sjkGCS001-EC11  Index: 10                  Flags: <Export Eval>
        Export: [ ((LABELSTACK_O2B || HKG-EC_out) && (NEXT-HOP-SELF && HKG-EC_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>        
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 1
        10.169.14.240+60606
        Route Queue Timer: unset Route Queue: empty
        Table inet.0
            Active prefixes:              682
            Received prefixes:            684
            Accepted prefixes:            684
            Suppressed due to damping:    0
            Advertised prefixes:          0
        Table inet.3
            Active prefixes:              2
            Received prefixes:            2
            Accepted prefixes:            2
            Suppressed due to damping:    0
            Advertised prefixes:          0

        Group Type: External                               Local AS: 65171
        Name: v6_sjkGCS001-EC11 Index: 11                Flags: <Export Eval>
        Export: [ (v6_HKG-EC_out && (NEXT-HOP-SELF && v6_HKG-EC_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 1
        2001:db8:eb18:ca45::1+179
        Route Queue Timer: unset Route Queue: empty
        Table inet6.0
            Active prefixes:              0
            Received prefixes:            0
            Accepted prefixes:            0
            Suppressed due to damping:    0
            Advertised prefixes:          0

        Group Type: External                               Local AS: 65171
        Name: obpGCS001-WC11  Index: 12                  Flags: <Export Eval>
        Export: [ (HKG-WC_out && (NEXT-HOP-SELF && HKG-WC_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0                           
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        10.169.14.249

        Group Type: External                               Local AS: 65171
        Name: v6_obpGCS001-WC11 Index: 13                Flags: <Export Eval>
        Export: [ (v6_HKG-WC_out && (NEXT-HOP-SELF && v6_HKG-WC_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        2001:db8:eb18:ca45::11

        Groups: 14 Peers: 19   External: 6    Internal: 13   Down peers: 15  Flaps: 359
        Table inet.0
            Received prefixes:            1366
            Accepted prefixes:            1366
            Active prefixes:              682
            Suppressed due to damping:    0
            Received external prefixes:   684
            Active external prefixes:     682
            Externals suppressed:         0
            Received internal prefixes:   682
            Active internal prefixes:     0
            Internals suppressed:         0
            RIB State: BGP restart is complete
        Table inet.3
            Received prefixes:            2
            Accepted prefixes:            2
            Active prefixes:              2
            Suppressed due to damping:    0
            Received external prefixes:   2
            Active external prefixes:     2
            Externals suppressed:         0
            Received internal prefixes:   0
            Active internal prefixes:     0
            Internals suppressed:         0
            RIB State: BGP restart is complete
        Table inet6.0
            Received prefixes:            0     
            Accepted prefixes:            0
            Active prefixes:              0
            Suppressed due to damping:    0
            Received external prefixes:   0
            Active external prefixes:     0
            Externals suppressed:         0
            Received internal prefixes:   0
            Active internal prefixes:     0
            Internals suppressed:         0
            RIB State: BGP restart is complete
    '''}

    golden_parsed_output = {
        "bgp-group-information": {
            "bgp-group": [
                {
                    "bgp-option-information": {
                        "bgp-options": "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v4_WATARI && NEXT-HOP-SELF)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "682",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "682",
                            "name": "inet.0",
                            "received-prefix-count": "682",
                            "suppressed-prefix-count": "0"
                        }
                    ],
                    "established-count": "1",
                    "group-flags": "Export Eval",
                    "group-index": "0",
                    "local-as": "65171",
                    "name": "Genie",
                    "peer-address": [
                        "10.189.5.253+179"
                    ],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "route-queue": {
                        "state": "empty",
                        "timer": "unset"
                    },
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v6_WATARI && NEXT-HOP-SELF)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "0",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "0",
                            "name": "inet6.0",
                            "received-prefix-count": "0",
                            "suppressed-prefix-count": "0"
                        }
                    ],
                    "established-count": "1",
                    "group-flags": "Export Eval",
                    "group-index": "1",
                    "local-as": "65171",
                    "name": "v6_Genie",
                    "peer-address": [
                        "2001:db8:223c:ca45::c+60268"
                    ],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "route-queue": {
                        "state": "empty",
                        "timer": "unset"
                    },
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && v4_NEXT-HOP-SELF_hktGCS001)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "2",
                    "local-as": "65171",
                    "name": "v4_RRC_72_TRIANGLE",
                    "peer-address": [
                        "10.189.5.245",
                        "10.189.5.243",
                        "10.189.5.242+179"
                    ],
                    "peer-as": "65171",
                    "peer-count": "3",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && v6_NEXT-HOP-SELF_hktGCS001)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "3",
                    "local-as": "65171",
                    "name": "v6_RRC_72_TRIANGLE",
                    "peer-address": [
                        "2001:db8:223c:ca45::7+179",
                        "2001:db8:223c:ca45::8+179"
                    ],
                    "peer-as": "65171",
                    "peer-count": "2",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "ALL_out",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "4",
                    "local-as": "65171",
                    "name": "v6_RRC_72_SQUARE",
                    "peer-address": [
                        "2001:db8:223c:ca45::9",
                        "2001:db8:223c:ca45::a+179"
                    ],
                    "peer-as": "65171",
                    "peer-count": "2",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "ALL_out",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "5",
                    "local-as": "65171",
                    "name": "v4_RRC_72_SQUARE",
                    "peer-address": [
                        "10.189.5.241+179",
                        "10.189.5.240"
                    ],
                    "peer-as": "65171",
                    "peer-count": "2",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "v4_Kentik_NO-DEFAULT",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "6",
                    "local-as": "65171",
                    "name": "v4_Kentik",
                    "peer-address": [
                        "10.49.216.179"
                    ],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "v6_Kentik_NO-DEFAULT",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "7",
                    "local-as": "65171",
                    "name": "v6_Kentik",
                    "peer-address": [
                        "2001:db8:6be:89bb::1:140"
                    ],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "type": "Internal"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && (NEXT-HOP-SELF && HKG-SNG_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "8",
                    "local-as": "65171",
                    "name": "sggjbb001",
                    "peer-address": [
                        "10.189.6.250"
                    ],
                    "peer-count": "1",
                    "type": "External"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && (NEXT-HOP-SELF && v6_HKG-SNG_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "9",
                    "local-as": "65171",
                    "name": "v6_sggjbb001",
                    "peer-address": [
                        "2001:db8:5961:ca45::1"
                    ],
                    "peer-count": "1",
                    "type": "External"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "((LABELSTACK_O2B || HKG-EC_out) && (NEXT-HOP-SELF && HKG-EC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "684",
                            "active-prefix-count": "682",
                            "advertised-prefix-count": "0",
                            "name": "inet.0",
                            "received-prefix-count": "684",
                            "suppressed-prefix-count": "0"
                        },
                        {
                            "accepted-prefix-count": "2",
                            "active-prefix-count": "2",
                            "advertised-prefix-count": "0",
                            "name": "inet.3",
                            "received-prefix-count": "2",
                            "suppressed-prefix-count": "0"
                        }
                    ],
                    "established-count": "1",
                    "group-flags": "Export Eval",
                    "group-index": "10",
                    "local-as": "65171",
                    "name": "sjkGCS001-EC11",
                    "peer-address": [
                        "10.169.14.240+60606"
                    ],
                    "peer-count": "1",
                    "route-queue": {
                        "state": "empty",
                        "timer": "unset"
                    },
                    "type": "External"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v6_HKG-EC_out && (NEXT-HOP-SELF && v6_HKG-EC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "0",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "0",
                            "name": "inet6.0",
                            "received-prefix-count": "0",
                            "suppressed-prefix-count": "0"
                        }
                    ],
                    "established-count": "1",
                    "group-flags": "Export Eval",
                    "group-index": "11",
                    "local-as": "65171",
                    "name": "v6_sjkGCS001-EC11",
                    "peer-address": [
                        "2001:db8:eb18:ca45::1+179"
                    ],
                    "peer-count": "1",
                    "route-queue": {
                        "state": "empty",
                        "timer": "unset"
                    },
                    "type": "External"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(HKG-WC_out && (NEXT-HOP-SELF && HKG-WC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "12",
                    "local-as": "65171",
                    "name": "obpGCS001-WC11",
                    "peer-address": [
                        "10.169.14.249"
                    ],
                    "peer-count": "1",
                    "type": "External"
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v6_HKG-WC_out && (NEXT-HOP-SELF && v6_HKG-WC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0"
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "13",
                    "local-as": "65171",
                    "name": "v6_obpGCS001-WC11",
                    "peer-address": [
                        "2001:db8:eb18:ca45::11"
                    ],
                    "peer-count": "1",
                    "type": "External"
                }
            ],
            "bgp-information": {
                "bgp-rib": [
                    {
                        "accepted-prefix-count": "1366",
                        "active-external-prefix-count": "682",
                        "active-internal-prefix-count": "0",
                        "active-prefix-count": "682",
                        "bgp-rib-state": "BGP restart is complete",
                        "name": "inet.0",
                        "received-prefix-count": "1366",
                        "suppressed-external-prefix-count": "0",
                        "suppressed-internal-prefix-count": "0",
                        "suppressed-prefix-count": "0",
                        "total-external-prefix-count": "684",
                        "total-internal-prefix-count": "682"
                    },
                    {
                        "accepted-prefix-count": "2",
                        "active-external-prefix-count": "2",
                        "active-internal-prefix-count": "0",
                        "active-prefix-count": "2",
                        "bgp-rib-state": "BGP restart is complete",
                        "name": "inet.3",
                        "received-prefix-count": "2",
                        "suppressed-external-prefix-count": "0",
                        "suppressed-internal-prefix-count": "0",
                        "suppressed-prefix-count": "0",
                        "total-external-prefix-count": "2",
                        "total-internal-prefix-count": "0"
                    },
                    {
                        "accepted-prefix-count": "0",
                        "active-external-prefix-count": "0",
                        "active-internal-prefix-count": "0",
                        "active-prefix-count": "0",
                        "bgp-rib-state": "BGP restart is complete",
                        "name": "inet6.0",
                        "received-prefix-count": "0",
                        "suppressed-external-prefix-count": "0",
                        "suppressed-internal-prefix-count": "0",
                        "suppressed-prefix-count": "0",
                        "total-external-prefix-count": "0",
                        "total-internal-prefix-count": "0"
                    }
                ],
                "down-peer-count": "15",
                "external-peer-count": "6",
                "flap-count": "359",
                "group-count": "14",
                "internal-peer-count": "13",
                "peer-count": "19"
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpGroupDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpGroupDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
if __name__ == '__main__':
    unittest.main()
