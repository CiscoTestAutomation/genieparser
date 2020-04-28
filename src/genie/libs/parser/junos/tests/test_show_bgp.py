
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.junos.show_bgp import (ShowBgpGroupBrief,
                                              ShowBgpGroupDetail,
                                              ShowBgpGroupSummary,
                                              ShowBgpSummary)


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


class TestShowBgpGroupSummary(unittest.TestCase):
    """ Unit tests for:
            * show bgp group summary | no-more
    """
    maxDiff = None
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    # show bgp group summary | no-more
    golden_output = {'execute.return_value': '''
    Group        Type       Peers     Established    Active/Received/Accepted/Damped
    hktGCS002    Internal   1         1          
      inet.0           : 0/682/682/0
    v6_hktGCS002 Internal   1         1          
      inet6.0          : 0/0/0/0
    v4_RRC_72_TRIANGLE Internal 3     0          
    v6_RRC_72_TRIANGLE Internal 2     0          
    v6_RRC_72_SQUARE Internal 2       0          
    v4_RRC_72_SQUARE Internal 2       0          
    v4_Kentik    Internal   1         0          
    v6_Kentik    Internal   1         0          
    sggjbb001    External   1         0          
    v6_sggjbb001 External   1         0          
    sjkGCS001-EC11 External 1         1          
      inet.0           : 682/684/684/0
      inet.3           : 2/2/2/0
    v6_sjkGCS001-EC11 External 1      1          
      inet6.0          : 0/0/0/0
    obpGCS001-WC11 External 1         0          
    v6_obpGCS001-WC11 External 1      0          

    Groups: 14 Peers: 19   External: 6    Internal: 13   Down peers: 15  Flaps: 359
      inet.0           : 682/1366/1366/0 External: 682/684/684/0 Internal: 0/682/682/0
      inet.3           : 2/2/2/0 External: 2/2/2/0 Internal: 0/0/0/0
      inet6.0          : 0/0/0/0 External: 0/0/0/0 Internal: 0/0/0/0
    '''}

    golden_parsed_output = {
        "bgp-group-information": {
            "bgp-group": [
                {
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "682",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "0",
                            "name": "inet.0",
                            "received-prefix-count": "682",
                        }
                    ],
                    "established-count": "1",
                    "name": "hktGCS002",
                    "peer-count": "1",
                    "type": "Internal",
                },
                {
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "0",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "0",
                            "name": "inet6.0",
                            "received-prefix-count": "0",
                        }
                    ],
                    "established-count": "1",
                    "name": "v6_hktGCS002",
                    "peer-count": "1",
                    "type": "Internal",
                },
                {
                    "established-count": "0",
                    "name": "v4_RRC_72_TRIANGLE",
                    "peer-count": "3",
                    "type": "Internal",
                },
                {
                    "established-count": "0",
                    "name": "v6_RRC_72_TRIANGLE",
                    "peer-count": "2",
                    "type": "Internal",
                },
                {
                    "established-count": "0",
                    "name": "v6_RRC_72_SQUARE",
                    "peer-count": "2",
                    "type": "Internal",
                },
                {
                    "established-count": "0",
                    "name": "v4_RRC_72_SQUARE",
                    "peer-count": "2",
                    "type": "Internal",
                },
                {
                    "established-count": "0",
                    "name": "v4_Kentik",
                    "peer-count": "1",
                    "type": "Internal",
                },
                {
                    "established-count": "0",
                    "name": "v6_Kentik",
                    "peer-count": "1",
                    "type": "Internal",
                },
                {
                    "established-count": "0",
                    "name": "sggjbb001",
                    "peer-count": "1",
                    "type": "External",
                },
                {
                    "established-count": "0",
                    "name": "v6_sggjbb001",
                    "peer-count": "1",
                    "type": "External",
                },
                {
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "684",
                            "active-prefix-count": "682",
                            "advertised-prefix-count": "0",
                            "name": "inet.0",
                            "received-prefix-count": "684",
                        },
                        {
                            "accepted-prefix-count": "2",
                            "active-prefix-count": "2",
                            "advertised-prefix-count": "0",
                            "name": "inet.3",
                            "received-prefix-count": "2",
                        },
                    ],
                    "established-count": "1",
                    "name": "sjkGCS001-EC11",
                    "peer-count": "1",
                    "type": "External",
                },
                {
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "0",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "0",
                            "name": "inet6.0",
                            "received-prefix-count": "0",
                        }
                    ],
                    "established-count": "1",
                    "name": "v6_sjkGCS001-EC11",
                    "peer-count": "1",
                    "type": "External",
                },
                {
                    "established-count": "0",
                    "name": "obpGCS001-WC11",
                    "peer-count": "1",
                    "type": "External",
                },
                {
                    "established-count": "0",
                    "name": "v6_obpGCS001-WC11",
                    "peer-count": "1",
                    "type": "External",
                },
            ],
            "bgp-information": {
                "bgp-rib": [
                    {
                        "accepted-external-prefix-count": "684",
                        "accepted-internal-prefix-count": "682",
                        "accepted-prefix-count": "1366",
                        "active-external-prefix-count": "682",
                        "active-internal-prefix-count": "0",
                        "active-prefix-count": "682",
                        "name": "inet.0",
                        "received-prefix-count": "1366",
                        "suppressed-external-prefix-count": "0",
                        "suppressed-internal-prefix-count": "0",
                        "suppressed-prefix-count": "0",
                        "total-external-prefix-count": "684",
                        "total-internal-prefix-count": "682",
                    },
                    {
                        "accepted-external-prefix-count": "2",
                        "accepted-internal-prefix-count": "0",
                        "accepted-prefix-count": "2",
                        "active-external-prefix-count": "2",
                        "active-internal-prefix-count": "0",
                        "active-prefix-count": "2",
                        "name": "inet.3",
                        "received-prefix-count": "2",
                        "suppressed-external-prefix-count": "0",
                        "suppressed-internal-prefix-count": "0",
                        "suppressed-prefix-count": "0",
                        "total-external-prefix-count": "2",
                        "total-internal-prefix-count": "0",
                    },
                    {
                        "accepted-external-prefix-count": "0",
                        "accepted-internal-prefix-count": "0",
                        "accepted-prefix-count": "0",
                        "active-external-prefix-count": "0",
                        "active-internal-prefix-count": "0",
                        "active-prefix-count": "0",
                        "name": "inet6.0",
                        "received-prefix-count": "0",
                        "suppressed-external-prefix-count": "0",
                        "suppressed-internal-prefix-count": "0",
                        "suppressed-prefix-count": "0",
                        "total-external-prefix-count": "0",
                        "total-internal-prefix-count": "0",
                    },
                ],
                "down-peer-count": "15",
                "external-peer-count": "6",
                "flap-count": "359",
                "group-count": "14",
                "internal-peer-count": "13",
                "peer-count": "19",
            },
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpGroupSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpGroupSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowBgpSummary(unittest.TestCase):
    """ Unit tests for:
            * show bgp summary
    """
    maxDiff = None
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    # show bgp summary | no-more
    golden_output = {'execute.return_value': '''
        Threading mode: BGP I/O
        Groups: 14 Peers: 19 Down peers: 15
        Table          Tot Paths  Act Paths Suppressed    History Damp State    Pending
        inet.0               
                            1366        682          0          0          0          0
        inet.3               
                               2          2          0          0          0          0
        inet6.0              
                               0          0          0          0          0          0
        Peer                     AS      InPkt     OutPkt    OutQ   Flaps Last Up/Dwn State|#Active/Received/Accepted/Damped...
        10.49.216.179         65171          0          0       0       0 29w5d 22:42:36 Connect
        10.169.14.240        65151     280414     221573       0     127 3w2d 4:19:15 Establ
          inet.0: 682/684/684/0
          inet.3: 2/2/2/0
        10.169.14.249        65151          0          0       0       0 29w5d 22:42:36 Active
        10.189.5.240          65171          0          0       0       0 29w5d 22:42:36 Connect
        10.189.5.241          65171          0          0       0       0 29w5d 22:42:36 Connect
        10.189.5.242          65171          0          0       0       0 29w5d 22:42:36 Active
        10.189.5.243          65171          0          0       0       0 29w5d 22:42:36 Active
        10.189.5.245          65171          0          0       0       0 29w5d 22:42:36 Active
        10.189.5.253          65171     110832     172140       0      44 3w2d 4:18:45 Establ
          inet.0: 0/682/682/0
        10.189.6.250          65181          0          0       0       0 29w5d 22:42:36 Active
        2001:db8:6be:89bb::1:140       65171          0          0       0       0 29w5d 22:42:36 Connect
        2001:db8:eb18:ca45::1       65151     218994     221571       0     133 3w2d 4:19:10 Establ
          inet6.0: 0/0/0/0
        2001:db8:eb18:ca45::11       65151          0          0       0       0 29w5d 22:42:36 Connect
        2001:db8:223c:ca45::7       65171          0          0       0       0 29w5d 22:42:36 Active
        2001:db8:223c:ca45::8       65171          0          0       0       0 29w5d 22:42:36 Connect
        2001:db8:223c:ca45::9       65171          0          0       0       0 29w5d 22:42:36 Connect
        2001:db8:223c:ca45::a       65171          0          0       0       0 29w5d 22:42:36 Connect
        2001:db8:223c:ca45::c       65171     110861     110862       0      55 3w2d 4:27:54 Establ
          inet6.0: 0/0/0/0
        2001:db8:5961:ca45::1       65181          0          0       0       0 29w5d 22:42:36 Connect

    '''}

    golden_parsed_output = {
        "bgp-information": {
            "group-count": "14",
            "peer-count": "19",
            "bgp-peer": [
                {
                    "flap-count": "0",
                    "peer-address": "10.49.216.179",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65171",
                    "output-messages": "0",
                    "peer-state": "Connect",
                    "input-messages": "0",
                },
                {
                    "flap-count": "127",
                    "peer-address": "10.169.14.240",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "3w2d 4:19:15"},
                    "peer-as": "65151",
                    "output-messages": "221573",
                    "bgp-rib": [
                        {
                            "received-prefix-count": "684",
                            "active-prefix-count": "682",
                            "name": "inet.0",
                            "suppressed-prefix-count": "0",
                            "accepted-prefix-count": "684",
                        },
                        {
                            "received-prefix-count": "2",
                            "active-prefix-count": "2",
                            "name": "inet.3",
                            "suppressed-prefix-count": "0",
                            "accepted-prefix-count": "2",
                        },
                    ],
                    "peer-state": "Establ",
                    "input-messages": "280414",
                },
                {
                    "flap-count": "0",
                    "peer-address": "10.169.14.249",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65151",
                    "output-messages": "0",
                    "peer-state": "Active",
                    "input-messages": "0",
                },
                {
                    "flap-count": "0",
                    "peer-address": "10.189.5.240",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65171",
                    "output-messages": "0",
                    "peer-state": "Connect",
                    "input-messages": "0",
                },
                {
                    "flap-count": "0",
                    "peer-address": "10.189.5.241",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65171",
                    "output-messages": "0",
                    "peer-state": "Connect",
                    "input-messages": "0",
                },
                {
                    "flap-count": "0",
                    "peer-address": "10.189.5.242",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65171",
                    "output-messages": "0",
                    "peer-state": "Active",
                    "input-messages": "0",
                },
                {
                    "flap-count": "0",
                    "peer-address": "10.189.5.243",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65171",
                    "output-messages": "0",
                    "peer-state": "Active",
                    "input-messages": "0",
                },
                {
                    "flap-count": "0",
                    "peer-address": "10.189.5.245",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65171",
                    "output-messages": "0",
                    "peer-state": "Active",
                    "input-messages": "0",
                },
                {
                    "flap-count": "44",
                    "peer-address": "10.189.5.253",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "3w2d 4:18:45"},
                    "peer-as": "65171",
                    "output-messages": "172140",
                    "bgp-rib": [
                        {
                            "received-prefix-count": "682",
                            "active-prefix-count": "0",
                            "name": "inet.0",
                            "suppressed-prefix-count": "0",
                            "accepted-prefix-count": "682",
                        }
                    ],
                    "peer-state": "Establ",
                    "input-messages": "110832",
                },
                {
                    "flap-count": "0",
                    "peer-address": "10.189.6.250",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65181",
                    "output-messages": "0",
                    "peer-state": "Active",
                    "input-messages": "0",
                },
                {
                    "flap-count": "0",
                    "peer-address": "2001:db8:6be:89bb::1:140",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65171",
                    "output-messages": "0",
                    "peer-state": "Connect",
                    "input-messages": "0",
                },
                {
                    "flap-count": "133",
                    "peer-address": "2001:db8:eb18:ca45::1",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "3w2d 4:19:10"},
                    "peer-as": "65151",
                    "output-messages": "221571",
                    "bgp-rib": [
                        {
                            "received-prefix-count": "0",
                            "active-prefix-count": "0",
                            "name": "inet6.0",
                            "suppressed-prefix-count": "0",
                            "accepted-prefix-count": "0",
                        }
                    ],
                    "peer-state": "Establ",
                    "input-messages": "218994",
                },
                {
                    "flap-count": "0",
                    "peer-address": "2001:db8:eb18:ca45::11",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65151",
                    "output-messages": "0",
                    "peer-state": "Connect",
                    "input-messages": "0",
                },
                {
                    "flap-count": "0",
                    "peer-address": "2001:db8:223c:ca45::7",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65171",
                    "output-messages": "0",
                    "peer-state": "Active",
                    "input-messages": "0",
                },
                {
                    "flap-count": "0",
                    "peer-address": "2001:db8:223c:ca45::8",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65171",
                    "output-messages": "0",
                    "peer-state": "Connect",
                    "input-messages": "0",
                },
                {
                    "flap-count": "0",
                    "peer-address": "2001:db8:223c:ca45::9",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65171",
                    "output-messages": "0",
                    "peer-state": "Connect",
                    "input-messages": "0",
                },
                {
                    "flap-count": "0",
                    "peer-address": "2001:db8:223c:ca45::a",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65171",
                    "output-messages": "0",
                    "peer-state": "Connect",
                    "input-messages": "0",
                },
                {
                    "flap-count": "55",
                    "peer-address": "2001:db8:223c:ca45::c",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "3w2d 4:27:54"},
                    "peer-as": "65171",
                    "output-messages": "110862",
                    "bgp-rib": [
                        {
                            "received-prefix-count": "0",
                            "active-prefix-count": "0",
                            "name": "inet6.0",
                            "suppressed-prefix-count": "0",
                            "accepted-prefix-count": "0",
                        }
                    ],
                    "peer-state": "Establ",
                    "input-messages": "110861",
                },
                {
                    "flap-count": "0",
                    "peer-address": "2001:db8:5961:ca45::1",
                    "route-queue-count": "0",
                    "elapsed-time": {"#text": "29w5d 22:42:36"},
                    "peer-as": "65181",
                    "output-messages": "0",
                    "peer-state": "Connect",
                    "input-messages": "0",
                },
            ],
            "bgp-rib": [
                {
                    "active-prefix-count": "682",
                    "total-prefix-count": "1366",
                    "name": "inet.0",
                    "damped-prefix-count": "0",
                    "suppressed-prefix-count": "0",
                    "pending-prefix-count": "0",
                    "history-prefix-count": "0",
                },
                {
                    "active-prefix-count": "2",
                    "total-prefix-count": "2",
                    "name": "inet.3",
                    "damped-prefix-count": "0",
                    "suppressed-prefix-count": "0",
                    "pending-prefix-count": "0",
                    "history-prefix-count": "0",
                },
                {
                    "active-prefix-count": "0",
                    "total-prefix-count": "0",
                    "name": "inet6.0",
                    "damped-prefix-count": "0",
                    "suppressed-prefix-count": "0",
                    "pending-prefix-count": "0",
                    "history-prefix-count": "0",
                },
            ],
            "bgp-thread-mode": "BGP I/O",
            "down-peer-count": "15",
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
