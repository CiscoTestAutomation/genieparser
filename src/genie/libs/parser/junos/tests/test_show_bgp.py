# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.junos.show_bgp import (
    ShowBgpGroupBrief,
    ShowBgpGroupDetail,
    ShowBgpGroupSummary,
    ShowBgpSummary,
    ShowBgpNeighbor,
)


class TestShowBgpGroupBrief(unittest.TestCase):
    """ Unit tests for:
            * show bgp group brief | no-more
    """

    maxDiff = None
    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
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
        Export: [ (ALL_out && v4_NEXT-HOP-SELF_pyats201) ]
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
        Export: [ (ALL_out && v6_NEXT-HOP-SELF_pyats201) ]
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
        Name: v4_pyats       Index: 6                   Flags: <Export Eval>
        Export: [ v4_pyats_NO-DEFAULT ]
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
        Name: sjkGDS221-EC11  Index: 10                  Flags: <Export Eval>
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
        Name: v6_sjkGDS221-EC11 Index: 11                Flags: <Export Eval>
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
    """
    }

    golden_parsed_output = {
        "bgp-group-information": {
            "bgp-group": [
                {
                    "bgp-option-information": {
                        "bgp-options": "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v4_WATARI && NEXT-HOP-SELF)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
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
                    "group-flags": "Export Eval",
                    "group-index": "0",
                    "local-as": "65171",
                    "name": "Genie",
                    "peer-address": ["10.189.5.253+179"],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v6_WATARI && NEXT-HOP-SELF)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
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
                    "group-flags": "Export Eval",
                    "group-index": "1",
                    "local-as": "65171",
                    "name": "v6_Genie",
                    "peer-address": ["2001:db8:223c:ca45::c+60268"],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && v4_NEXT-HOP-SELF_pyats201)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "2",
                    "local-as": "65171",
                    "name": "v4_RRC_72_TRIANGLE",
                    "peer-address": [
                        "10.189.5.245+179",
                        "10.189.5.243+179",
                        "10.189.5.242+179",
                    ],
                    "peer-as": "65171",
                    "peer-count": "3",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && v6_NEXT-HOP-SELF_pyats201)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "3",
                    "local-as": "65171",
                    "name": "v6_RRC_72_TRIANGLE",
                    "peer-address": [
                        "2001:db8:223c:ca45::7+179",
                        "2001:db8:223c:ca45::8",
                    ],
                    "peer-as": "65171",
                    "peer-count": "2",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "ALL_out",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "4",
                    "local-as": "65171",
                    "name": "v6_RRC_72_SQUARE",
                    "peer-address": ["2001:db8:223c:ca45::9", "2001:db8:223c:ca45::a"],
                    "peer-as": "65171",
                    "peer-count": "2",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "ALL_out",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "5",
                    "local-as": "65171",
                    "name": "v4_RRC_72_SQUARE",
                    "peer-address": ["10.189.5.241+179", "10.189.5.240"],
                    "peer-as": "65171",
                    "peer-count": "2",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "v4_pyats_NO-DEFAULT",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "6",
                    "local-as": "65171",
                    "name": "v4_pyats",
                    "peer-address": ["10.49.216.179"],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "v6_Kentik_NO-DEFAULT",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "7",
                    "local-as": "65171",
                    "name": "v6_Kentik",
                    "peer-address": ["2001:db8:6be:89bb::1:140"],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && (NEXT-HOP-SELF && HKG-SNG_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "8",
                    "local-as": "65171",
                    "name": "sggjbb001",
                    "peer-address": ["10.189.6.250"],
                    "peer-count": "1",
                    "type": "External",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && (NEXT-HOP-SELF && v6_HKG-SNG_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "9",
                    "local-as": "65171",
                    "name": "v6_sggjbb001",
                    "peer-address": ["2001:db8:5961:ca45::1"],
                    "peer-count": "1",
                    "type": "External",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "((LABELSTACK_O2B || HKG-EC_out) && (NEXT-HOP-SELF && HKG-EC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
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
                    "group-flags": "Export Eval",
                    "group-index": "10",
                    "local-as": "65171",
                    "name": "sjkGDS221-EC11",
                    "peer-address": ["10.169.14.240+60606"],
                    "peer-count": "1",
                    "type": "External",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v6_HKG-EC_out && (NEXT-HOP-SELF && v6_HKG-EC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
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
                    "group-flags": "Export Eval",
                    "group-index": "11",
                    "local-as": "65171",
                    "name": "v6_sjkGDS221-EC11",
                    "peer-address": ["2001:db8:eb18:ca45::1+179"],
                    "peer-count": "1",
                    "type": "External",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(HKG-WC_out && (NEXT-HOP-SELF && HKG-WC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "12",
                    "local-as": "65171",
                    "name": "obpGCS001-WC11",
                    "peer-address": ["10.169.14.249"],
                    "peer-count": "1",
                    "type": "External",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v6_HKG-WC_out && (NEXT-HOP-SELF && v6_HKG-WC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "13",
                    "local-as": "65171",
                    "name": "v6_obpGCS001-WC11",
                    "peer-address": ["2001:db8:eb18:ca45::11"],
                    "peer-count": "1",
                    "type": "External",
                },
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
                        "total-prefix-count": "1366",
                    },
                    {
                        "active-prefix-count": "2",
                        "damped-prefix-count": "0",
                        "history-prefix-count": "0",
                        "name": "inet.3",
                        "pending-prefix-count": "0",
                        "suppressed-prefix-count": "0",
                        "total-prefix-count": "2",
                    },
                    {
                        "active-prefix-count": "0",
                        "damped-prefix-count": "0",
                        "history-prefix-count": "0",
                        "name": "inet6.0",
                        "pending-prefix-count": "0",
                        "suppressed-prefix-count": "0",
                        "total-prefix-count": "0",
                    },
                ],
                "down-peer-count": "15",
                "external-peer-count": "6",
                "flap-count": "359",
                "group-count": "14",
                "internal-peer-count": "13",
                "peer-count": "19",
            },
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
    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
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
        Export: [ (ALL_out && v4_NEXT-HOP-SELF_pyats201) ]
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
        Export: [ (ALL_out && v6_NEXT-HOP-SELF_pyats201) ]
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
        Name: v4_pyats       Index: 6                   Flags: <Export Eval>
        Export: [ v4_pyats_NO-DEFAULT ]
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
        Name: sjkGDS221-EC11  Index: 10                  Flags: <Export Eval>
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
        Name: v6_sjkGDS221-EC11 Index: 11                Flags: <Export Eval>
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
    """
    }

    golden_parsed_output = {
        "bgp-group-information": {
            "bgp-group": [
                {
                    "bgp-option-information": {
                        "bgp-options": "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v4_WATARI && NEXT-HOP-SELF)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "682",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "682",
                            "name": "inet.0",
                            "received-prefix-count": "682",
                            "suppressed-prefix-count": "0",
                        }
                    ],
                    "established-count": "1",
                    "group-flags": "Export Eval",
                    "group-index": "0",
                    "local-as": "65171",
                    "name": "Genie",
                    "peer-address": ["10.189.5.253+179"],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "route-queue": {"state": "empty", "timer": "unset"},
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v6_WATARI && NEXT-HOP-SELF)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "0",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "0",
                            "name": "inet6.0",
                            "received-prefix-count": "0",
                            "suppressed-prefix-count": "0",
                        }
                    ],
                    "established-count": "1",
                    "group-flags": "Export Eval",
                    "group-index": "1",
                    "local-as": "65171",
                    "name": "v6_Genie",
                    "peer-address": ["2001:db8:223c:ca45::c+60268"],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "route-queue": {"state": "empty", "timer": "unset"},
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && v4_NEXT-HOP-SELF_pyats201)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "2",
                    "local-as": "65171",
                    "name": "v4_RRC_72_TRIANGLE",
                    "peer-address": [
                        "10.189.5.245",
                        "10.189.5.243",
                        "10.189.5.242+179",
                    ],
                    "peer-as": "65171",
                    "peer-count": "3",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && v6_NEXT-HOP-SELF_pyats201)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "3",
                    "local-as": "65171",
                    "name": "v6_RRC_72_TRIANGLE",
                    "peer-address": [
                        "2001:db8:223c:ca45::7+179",
                        "2001:db8:223c:ca45::8+179",
                    ],
                    "peer-as": "65171",
                    "peer-count": "2",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "ALL_out",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "4",
                    "local-as": "65171",
                    "name": "v6_RRC_72_SQUARE",
                    "peer-address": [
                        "2001:db8:223c:ca45::9",
                        "2001:db8:223c:ca45::a+179",
                    ],
                    "peer-as": "65171",
                    "peer-count": "2",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "ALL_out",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "5",
                    "local-as": "65171",
                    "name": "v4_RRC_72_SQUARE",
                    "peer-address": ["10.189.5.241+179", "10.189.5.240"],
                    "peer-as": "65171",
                    "peer-count": "2",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "v4_pyats_NO-DEFAULT",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "6",
                    "local-as": "65171",
                    "name": "v4_pyats",
                    "peer-address": ["10.49.216.179"],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Cluster Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "v6_Kentik_NO-DEFAULT",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "7",
                    "local-as": "65171",
                    "name": "v6_Kentik",
                    "peer-address": ["2001:db8:6be:89bb::1:140"],
                    "peer-as": "65171",
                    "peer-count": "1",
                    "type": "Internal",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && (NEXT-HOP-SELF && HKG-SNG_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "8",
                    "local-as": "65171",
                    "name": "sggjbb001",
                    "peer-address": ["10.189.6.250"],
                    "peer-count": "1",
                    "type": "External",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(ALL_out && (NEXT-HOP-SELF && v6_HKG-SNG_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "9",
                    "local-as": "65171",
                    "name": "v6_sggjbb001",
                    "peer-address": ["2001:db8:5961:ca45::1"],
                    "peer-count": "1",
                    "type": "External",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "((LABELSTACK_O2B || HKG-EC_out) && (NEXT-HOP-SELF && HKG-EC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "684",
                            "active-prefix-count": "682",
                            "advertised-prefix-count": "0",
                            "name": "inet.0",
                            "received-prefix-count": "684",
                            "suppressed-prefix-count": "0",
                        },
                        {
                            "accepted-prefix-count": "2",
                            "active-prefix-count": "2",
                            "advertised-prefix-count": "0",
                            "name": "inet.3",
                            "received-prefix-count": "2",
                            "suppressed-prefix-count": "0",
                        },
                    ],
                    "established-count": "1",
                    "group-flags": "Export Eval",
                    "group-index": "10",
                    "local-as": "65171",
                    "name": "sjkGDS221-EC11",
                    "peer-address": ["10.169.14.240+60606"],
                    "peer-count": "1",
                    "route-queue": {"state": "empty", "timer": "unset"},
                    "type": "External",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v6_HKG-EC_out && (NEXT-HOP-SELF && v6_HKG-EC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "0",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "0",
                            "name": "inet6.0",
                            "received-prefix-count": "0",
                            "suppressed-prefix-count": "0",
                        }
                    ],
                    "established-count": "1",
                    "group-flags": "Export Eval",
                    "group-index": "11",
                    "local-as": "65171",
                    "name": "v6_sjkGDS221-EC11",
                    "peer-address": ["2001:db8:eb18:ca45::1+179"],
                    "peer-count": "1",
                    "route-queue": {"state": "empty", "timer": "unset"},
                    "type": "External",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(HKG-WC_out && (NEXT-HOP-SELF && HKG-WC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "12",
                    "local-as": "65171",
                    "name": "obpGCS001-WC11",
                    "peer-address": ["10.169.14.249"],
                    "peer-count": "1",
                    "type": "External",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Multihop Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "export-policy": "(v6_HKG-WC_out && (NEXT-HOP-SELF && v6_HKG-WC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "0",
                    },
                    "established-count": "0",
                    "group-flags": "Export Eval",
                    "group-index": "13",
                    "local-as": "65171",
                    "name": "v6_obpGCS001-WC11",
                    "peer-address": ["2001:db8:eb18:ca45::11"],
                    "peer-count": "1",
                    "type": "External",
                },
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
                        "total-internal-prefix-count": "682",
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
                        "total-internal-prefix-count": "0",
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
    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    # show bgp group summary | no-more
    golden_output = {
        "execute.return_value": """
    Group        Type       Peers     Established    Active/Received/Accepted/Damped
    hktGCS002    Internal   1         1
      inet.0           : 0/682/682/0
    v6_hktGCS002 Internal   1         1
      inet6.0          : 0/0/0/0
    v4_RRC_72_TRIANGLE Internal 3     0
    v6_RRC_72_TRIANGLE Internal 2     0
    v6_RRC_72_SQUARE Internal 2       0
    v4_RRC_72_SQUARE Internal 2       0
    v4_pyats    Internal   1         0
    v6_Kentik    Internal   1         0
    sggjbb001    External   1         0
    v6_sggjbb001 External   1         0
    sjkGDS221-EC11 External 1         1
      inet.0           : 682/684/684/0
      inet.3           : 2/2/2/0
    v6_sjkGDS221-EC11 External 1      1
      inet6.0          : 0/0/0/0
    obpGCS001-WC11 External 1         0
    v6_obpGCS001-WC11 External 1      0

    Groups: 14 Peers: 19   External: 6    Internal: 13   Down peers: 15  Flaps: 359
      inet.0           : 682/1366/1366/0 External: 682/684/684/0 Internal: 0/682/682/0
      inet.3           : 2/2/2/0 External: 2/2/2/0 Internal: 0/0/0/0
      inet6.0          : 0/0/0/0 External: 0/0/0/0 Internal: 0/0/0/0
    """
    }

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
                    "name": "v4_pyats",
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
                    "name": "sjkGDS221-EC11",
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
                    "name": "v6_sjkGDS221-EC11",
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
    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    # show bgp summary | no-more
    golden_output = {
        "execute.return_value": """
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

    """
    }

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


class TestShowBgpNeighbor(unittest.TestCase):
    """ Unit tests for:
            * show bgp neighbor
    """

    maxDiff = None

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show bgp neighbor
        Peer: 10.49.216.179 AS 65171   Local: 10.189.5.252 AS 65171
        Description: v4_pyats
        Group: v4_pyats             Routing-Instance: master
        Forwarding routing-instance: master
        Type: Internal    State: Active       (route reflector client)Flags: <>
        Last State: Idle          Last Event: Start
        Last Error: None
        Export: [ v4_pyats_NO-DEFAULT ] Import: [ 11 ]
        Options: <Preference LocalAddress HoldTime LogUpDown Cluster PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Local Address: 10.189.5.252 Holdtime: 720 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 10.169.14.240+60606 AS 65151 Local: 10.189.5.252+179 AS 65171
        Description: sjkGDS221-EC11
        Group: sjkGDS221-EC11        Routing-Instance: master
        Forwarding routing-instance: master
        Type: External    State: Established    Flags: <Sync>
        Last State: OpenConfirm   Last Event: RecvKeepAlive
        Last Error: Hold Timer Expired Error
        Export: [ ((LABELSTACK_O2B || HKG-EC_out) && (NEXT-HOP-SELF && HKG-EC_AddMED)) ]
        Options: <Multihop Preference LocalAddress HoldTime AuthKey Ttl LogUpDown AddressFamily PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Address families configured: inet-unicast inet-labeled-unicast
        Local Address: 10.189.5.252 Holdtime: 30 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 127
        Last flap event: HoldTime
        Error: 'Hold Timer Expired Error' Sent: 156 Recv: 17
        Error: 'Cease' Sent: 0 Recv: 6
        Peer ID: 10.169.14.240  Local ID: 10.189.5.252      Active Holdtime: 30
        Keepalive Interval: 10         Group index: 10   Peer index: 0    SNMP index: 15
        I/O Session Thread: bgpio-0 State: Enabled
        BFD: disabled, down
        NLRI for restart configured on peer: inet-unicast inet-labeled-unicast
        NLRI advertised by peer: inet-unicast inet-labeled-unicast
        NLRI for this session: inet-unicast inet-labeled-unicast
        Peer supports Refresh capability (2)
        Stale routes from peer are kept for: 300
        Peer does not support Restarter functionality
        Restart flag received from the peer: Notification
        NLRI that restart is negotiated for: inet-unicast inet-labeled-unicast
        NLRI of received end-of-rib markers: inet-unicast inet-labeled-unicast
        NLRI of all end-of-rib markers sent: inet-unicast inet-labeled-unicast
        Peer does not support LLGR Restarter functionality
        Peer supports 4 byte AS extension (peer-as 65151)
        Peer does not support Addpath
        NLRI(s) enabled for color nexthop resolution: inet-unicast
        Entropy label NLRI: inet-labeled-unicast
            Entropy label: No; next hop validation: Yes
            Local entropy label capability: Yes; stitching capability: Yes
        Table inet.0 Bit: 20000
            RIB State: BGP restart is complete
            Send state: in sync
            Active prefixes:              682
            Received prefixes:            684
            Accepted prefixes:            684
            Suppressed due to damping:    0
            Advertised prefixes:          0
        Table inet.3 Bit: 30000
            RIB State: BGP restart is complete
            Send state: in sync
            Active prefixes:              2
            Received prefixes:            2
            Accepted prefixes:            2
            Suppressed due to damping:    0
            Advertised prefixes:          0
        Last traffic (seconds): Received 3    Sent 3    Checked 1999164
        Input messages:  Total 280022 Updates 61419   Refreshes 0     Octets 7137084
        Output messages: Total 221176 Updates 0       Refreshes 0     Octets 4202359
        Output Queue[1]: 0            (inet.0, inet-unicast)
        Output Queue[2]: 0            (inet.3, inet-labeled-unicast)

        Peer: 10.169.14.249 AS 65151  Local: 10.189.5.252 AS 65171
        Description: obpGCS001-WC11
        Group: obpGCS001-WC11        Routing-Instance: master
        Forwarding routing-instance: master
        Type: External    State: Active         Flags: <>
        Last State: Idle          Last Event: Start
        Last Error: None
        Export: [ (HKG-WC_out && (NEXT-HOP-SELF && HKG-WC_AddMED)) ]
        Options: <Multihop Preference LocalAddress HoldTime AuthKey Ttl LogUpDown PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 10.189.5.252 Holdtime: 30 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 10.189.5.240+179 AS 65171 Local: 10.189.5.252 AS 65171
        Description: cm-hkm003
        Group: v4_RRC_72_SQUARE      Routing-Instance: master
        Forwarding routing-instance: master
        Type: Internal    State: Connect      (route reflector client)Flags: <>
        Last State: Active        Last Event: ConnectRetry
        Last Error: None
        Export: [ ALL_out ] Import: [ REJ_LONG_ASPATH ]
        Options: <Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 10.189.5.252 Holdtime: 60 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 10.189.5.241+179 AS 65171 Local: 10.189.5.252 AS 65171
        Description: cm-hkm004
        Group: v4_RRC_72_SQUARE      Routing-Instance: master
        Forwarding routing-instance: master
        Type: Internal    State: Connect      (route reflector client)Flags: <>
        Last State: Active        Last Event: ConnectRetry
        Last Error: None
        Export: [ ALL_out ] Import: [ REJ_LONG_ASPATH ]
        Options: <Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 10.189.5.252 Holdtime: 60 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 10.189.5.242 AS 65171    Local: 10.189.5.252 AS 65171
        Description: cm-hkt003
        Group: v4_RRC_72_TRIANGLE    Routing-Instance: master
        Forwarding routing-instance: master
        Type: Internal    State: Active       (route reflector client)Flags: <>
        Last State: Idle          Last Event: Start
        Last Error: None
        Export: [ (ALL_out && v4_NEXT-HOP-SELF_pyats201) ] Import: [ REJ_LONG_ASPATH ]
        Options: <Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 10.189.5.252 Holdtime: 60 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 10.189.5.243 AS 65171    Local: 10.189.5.252 AS 65171
        Description: cm-hkt004
        Group: v4_RRC_72_TRIANGLE    Routing-Instance: master
        Forwarding routing-instance: master
        Type: Internal    State: Active       (route reflector client)Flags: <>
        Last State: Idle          Last Event: Start
        Last Error: None
        Export: [ (ALL_out && v4_NEXT-HOP-SELF_pyats201) ] Import: [ REJ_LONG_ASPATH ]
        Options: <Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 10.189.5.252 Holdtime: 60 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 10.189.5.245 AS 65171    Local: 10.189.5.252 AS 65171
        Description: lg-hkt001
        Group: v4_RRC_72_TRIANGLE    Routing-Instance: master
        Forwarding routing-instance: master
        Type: Internal    State: Active       (route reflector client)Flags: <>
        Last State: Idle          Last Event: Start
        Last Error: None
        Export: [ (ALL_out && v4_NEXT-HOP-SELF_pyats201) ] Import: [ REJ_LONG_ASPATH ]
        Options: <Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 10.189.5.252 Holdtime: 60 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 10.189.5.253+179 AS 65171 Local: 10.189.5.252+60144 AS 65171
        Description: hktGCS002
        Group: hktGCS002             Routing-Instance: master
        Forwarding routing-instance: master
        Type: Internal    State: Established    Flags: <Sync>
        Last State: OpenConfirm   Last Event: RecvKeepAlive
        Last Error: Hold Timer Expired Error
        Export: [ (v4_WATARI && NEXT-HOP-SELF) ]
        Options: <Preference LocalAddress HoldTime AuthKey LogUpDown PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 10.189.5.252 Holdtime: 60 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 44
        Last flap event: RecvNotify
        Error: 'Hold Timer Expired Error' Sent: 18 Recv: 36
        Error: 'Cease' Sent: 10 Recv: 2
        Peer ID: 10.189.5.253    Local ID: 10.189.5.252      Active Holdtime: 60
        Keepalive Interval: 20         Group index: 0    Peer index: 0    SNMP index: 0
        I/O Session Thread: bgpio-0 State: Enabled
        BFD: disabled, down
        NLRI for restart configured on peer: inet-unicast
        NLRI advertised by peer: inet-unicast
        NLRI for this session: inet-unicast
        Peer supports Refresh capability (2)
        Stale routes from peer are kept for: 300
        Peer does not support Restarter functionality
        Restart flag received from the peer: Notification
        NLRI that restart is negotiated for: inet-unicast
        NLRI of received end-of-rib markers: inet-unicast
        NLRI of all end-of-rib markers sent: inet-unicast
        Peer does not support LLGR Restarter functionality
        Peer supports 4 byte AS extension (peer-as 65171)
        Peer does not support Addpath
        NLRI(s) enabled for color nexthop resolution: inet-unicast
        Table inet.0 Bit: 20001
            RIB State: BGP restart is complete
            Send state: in sync
            Active prefixes:              0
            Received prefixes:            682
            Accepted prefixes:            682
            Suppressed due to damping:    0
            Advertised prefixes:          682
        Last traffic (seconds): Received 13   Sent 3    Checked 1999134
        Input messages:  Total 110633 Updates 4       Refreshes 0     Octets 2104771
        Output messages: Total 171942 Updates 61307   Refreshes 0     Octets 5078640
        Output Queue[1]: 0            (inet.0, inet-unicast)

        Peer: 10.189.6.250 AS 65181    Local: 10.189.5.252 AS 65171
        Description: sggjbb001
        Group: sggjbb001             Routing-Instance: master
        Forwarding routing-instance: master
        Type: External    State: Active         Flags: <>
        Last State: Idle          Last Event: Start
        Last Error: None
        Export: [ (ALL_out && (NEXT-HOP-SELF && HKG-SNG_AddMED)) ]
        Options: <Multihop Preference LocalAddress HoldTime AuthKey Ttl LogUpDown PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 10.189.5.252 Holdtime: 30 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 2001:db8:6be:89bb::1:140+179 AS 65171 Local: 2001:db8:223c:ca45::b AS 65171
        Description: v6_Kentik
        Group: v6_Kentik             Routing-Instance: master
        Forwarding routing-instance: master
        Type: Internal    State: Connect      (route reflector client)Flags: <>
        Last State: Active        Last Event: ConnectRetry
        Last Error: None
        Export: [ v6_Kentik_NO-DEFAULT ] Import: [ 11 ]
        Options: <Preference LocalAddress HoldTime LogUpDown Cluster PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Local Address: 2001:db8:223c:ca45::b Holdtime: 720 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 2001:db8:eb18:ca45::1+179 AS 65151 Local: 2001:db8:223c:ca45::b+63754 AS 65171
        Description: sjkGDS221-EC11
        Group: v6_sjkGDS221-EC11     Routing-Instance: master
        Forwarding routing-instance: master
        Type: External    State: Established    Flags: <Sync>
        Last State: OpenConfirm   Last Event: RecvKeepAlive
        Last Error: Hold Timer Expired Error
        Export: [ (v6_HKG-EC_out && (NEXT-HOP-SELF && v6_HKG-EC_AddMED)) ]
        Options: <Multihop Preference LocalAddress HoldTime AuthKey Ttl LogUpDown PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 2001:db8:223c:ca45::b Holdtime: 30 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 133
        Last flap event: HoldTime
        Error: 'Hold Timer Expired Error' Sent: 171 Recv: 24
        Error: 'Cease' Sent: 0 Recv: 5
        Peer ID: 10.169.14.240  Local ID: 10.189.5.252      Active Holdtime: 30
        Keepalive Interval: 10         Group index: 11   Peer index: 0    SNMP index: 16
        I/O Session Thread: bgpio-0 State: Enabled
        BFD: disabled, down
        NLRI for restart configured on peer: inet6-unicast
        NLRI advertised by peer: inet6-unicast
        NLRI for this session: inet6-unicast
        Peer supports Refresh capability (2)
        Stale routes from peer are kept for: 300
        Peer does not support Restarter functionality
        Restart flag received from the peer: Notification
        NLRI that restart is negotiated for: inet6-unicast
        NLRI of received end-of-rib markers: inet6-unicast
        NLRI of all end-of-rib markers sent: inet6-unicast
        Peer does not support LLGR Restarter functionality
        Peer supports 4 byte AS extension (peer-as 65151)
        Peer does not support Addpath
        NLRI(s) enabled for color nexthop resolution: inet6-unicast
        Table inet6.0 Bit: 40000
            RIB State: BGP restart is complete
            Send state: in sync
            Active prefixes:              0
            Received prefixes:            0
            Accepted prefixes:            0
            Suppressed due to damping:    0
            Advertised prefixes:          0
        Last traffic (seconds): Received 1    Sent 3    Checked 1999159
        Input messages:  Total 218603 Updates 1       Refreshes 0     Octets 4153468
        Output messages: Total 221174 Updates 0       Refreshes 0     Octets 4202317
        Output Queue[3]: 0            (inet6.0, inet6-unicast)

        Peer: 2001:db8:eb18:ca45::11 AS 65151 Local: 2001:db8:223c:ca45::b AS 65171
        Description: obpGCS001-WC11
        Group: v6_obpGCS001-WC11     Routing-Instance: master
        Forwarding routing-instance: master
        Type: External    State: Active         Flags: <>
        Last State: Idle          Last Event: Start
        Last Error: None
        Export: [ (v6_HKG-WC_out && (NEXT-HOP-SELF && v6_HKG-WC_AddMED)) ]
        Options: <Multihop Preference LocalAddress HoldTime AuthKey Ttl LogUpDown PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 2001:db8:223c:ca45::b Holdtime: 30 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 2001:db8:223c:ca45::7 AS 65171 Local: 2001:db8:223c:ca45::b AS 65171
        Description: cm-hkt003
        Group: v6_RRC_72_TRIANGLE    Routing-Instance: master
        Forwarding routing-instance: master
        Type: Internal    State: Active       (route reflector client)Flags: <>
        Last State: Idle          Last Event: Start
        Last Error: None
        Export: [ (ALL_out && v6_NEXT-HOP-SELF_pyats201) ]
        Options: <Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 2001:db8:223c:ca45::b Holdtime: 60 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 2001:db8:223c:ca45::8+179 AS 65171 Local: 2001:db8:223c:ca45::b AS 65171
        Description: cm-hkt004
        Group: v6_RRC_72_TRIANGLE    Routing-Instance: master
        Forwarding routing-instance: master
        Type: Internal    State: Connect      (route reflector client)Flags: <>
        Last State: Active        Last Event: ConnectRetry
        Last Error: None
        Export: [ (ALL_out && v6_NEXT-HOP-SELF_pyats201) ]
        Options: <Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 2001:db8:223c:ca45::b Holdtime: 60 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 2001:db8:223c:ca45::9 AS 65171 Local: 2001:db8:223c:ca45::b AS 65171
        Description: cm-hkm003
        Group: v6_RRC_72_SQUARE      Routing-Instance: master
        Forwarding routing-instance: master
        Type: Internal    State: Active       (route reflector client)Flags: <>
        Last State: Idle          Last Event: Start
        Last Error: None
        Export: [ ALL_out ]
        Options: <Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 2001:db8:223c:ca45::b Holdtime: 60 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 2001:db8:223c:ca45::a+179 AS 65171 Local: 2001:db8:223c:ca45::b AS 65171
        Description: cm-hkm004
        Group: v6_RRC_72_SQUARE      Routing-Instance: master
        Forwarding routing-instance: master
        Type: Internal    State: Connect      (route reflector client)Flags: <>
        Last State: Active        Last Event: ConnectRetry
        Last Error: None
        Export: [ ALL_out ]
        Options: <Preference LocalAddress HoldTime AuthKey LogUpDown Cluster PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 2001:db8:223c:ca45::b Holdtime: 60 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0

        Peer: 2001:db8:223c:ca45::c+60268 AS 65171 Local: 2001:db8:223c:ca45::b+179 AS 65171
        Description: hktGCS002
        Group: v6_hktGCS002          Routing-Instance: master
        Forwarding routing-instance: master
        Type: Internal    State: Established    Flags: <Sync>
        Last State: OpenConfirm   Last Event: RecvKeepAlive
        Last Error: Hold Timer Expired Error
        Export: [ (v6_WATARI && NEXT-HOP-SELF) ]
        Options: <Preference LocalAddress HoldTime AuthKey LogUpDown PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 2001:db8:223c:ca45::b Holdtime: 60 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 55
        Last flap event: HoldTime
        Error: 'Hold Timer Expired Error' Sent: 27 Recv: 40
        Error: 'Cease' Sent: 16 Recv: 0
        Peer ID: 10.189.5.253    Local ID: 10.189.5.252      Active Holdtime: 60
        Keepalive Interval: 20         Group index: 1    Peer index: 0    SNMP index: 1
        I/O Session Thread: bgpio-0 State: Enabled
        BFD: disabled, down
        NLRI for restart configured on peer: inet6-unicast
        NLRI advertised by peer: inet6-unicast
        NLRI for this session: inet6-unicast
        Peer supports Refresh capability (2)
        Stale routes from peer are kept for: 300
        Peer does not support Restarter functionality
        Restart flag received from the peer: Notification
        NLRI that restart is negotiated for: inet6-unicast
        NLRI of received end-of-rib markers: inet6-unicast
        NLRI of all end-of-rib markers sent: inet6-unicast
        Peer does not support LLGR Restarter functionality
        Peer supports 4 byte AS extension (peer-as 65171)
        Peer does not support Addpath
        NLRI(s) enabled for color nexthop resolution: inet6-unicast
        Table inet6.0 Bit: 40001
            RIB State: BGP restart is complete
            Send state: in sync
            Active prefixes:              0
            Received prefixes:            0
            Accepted prefixes:            0
            Suppressed due to damping:    0
            Advertised prefixes:          0
        Last traffic (seconds): Received 6    Sent 5    Checked 16510983
        Input messages:  Total 110662 Updates 1       Refreshes 0     Octets 2102633
        Output messages: Total 110664 Updates 0       Refreshes 0     Octets 2102627
        Output Queue[3]: 0            (inet6.0, inet6-unicast)

        Peer: 2001:db8:5961:ca45::1 AS 65181 Local: 2001:db8:223c:ca45::b AS 65171
        Description: sggjbb001
        Group: v6_sggjbb001          Routing-Instance: master
        Forwarding routing-instance: master
        Type: External    State: Active         Flags: <>
        Last State: Idle          Last Event: Start
        Last Error: None
        Export: [ (ALL_out && (NEXT-HOP-SELF && v6_HKG-SNG_AddMED)) ]
        Options: <Multihop Preference LocalAddress HoldTime AuthKey Ttl LogUpDown PeerAS Refresh Confed>
        Options: <GracefulShutdownRcv>
        Authentication key is configured
        Local Address: 2001:db8:223c:ca45::b Holdtime: 30 Preference: 170
        Graceful Shutdown Receiver local-preference: 0
        Number of flaps: 0
    """
    }

    golden_parsed_output = {
        "bgp-information": {
            "bgp-peer": [
                {
                    "bgp-option-information": {
                        "bgp-options": "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "LogUpDown "
                        "Cluster "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "v4_pyats_NO-DEFAULT",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "720",
                        "import-policy": "11",
                        "local-address": "10.189.5.252",
                        "preference": "170",
                    },
                    "description": "v4_pyats",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "Start",
                    "last-state": "Idle",
                    "local-address": "10.189.5.252",
                    "local-as": "65171",
                    "peer-address": "10.49.216.179",
                    "peer-as": "65171",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "v4_pyats",
                    "peer-state": "Active",
                    "peer-type": "Internal",
                    "route-reflector-client": True,
                },
                {
                    "bgp-bfd": {
                        "bfd-configuration-state": "disabled",
                        "bfd-operational-state": "down",
                    },
                    "bgp-error": [
                        {
                            "name": "Hold Timer Expired " "Error",
                            "receive-count": "17",
                            "send-count": "156",
                        },
                        {"name": "Cease", "receive-count": "6", "send-count": "0"},
                    ],
                    "bgp-option-information": {
                        "address-families": "inet-unicast " "inet-labeled-unicast",
                        "authentication-configured": True,
                        "bgp-options": "Multihop "
                        "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "Ttl "
                        "LogUpDown "
                        "AddressFamily "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "((LABELSTACK_O2B "
                        "|| "
                        "HKG-EC_out) "
                        "&& "
                        "(NEXT-HOP-SELF "
                        "&& "
                        "HKG-EC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "30",
                        "local-address": "10.189.5.252",
                        "preference": "170",
                    },
                    "bgp-output-queue": [
                        {
                            "count": "0",
                            "number": "1",
                            "rib-adv-nlri": "inet-unicast",
                            "table-name": "inet.0",
                        },
                        {
                            "count": "0",
                            "number": "2",
                            "rib-adv-nlri": "inet-labeled-unicast",
                            "table-name": "inet.3",
                        },
                    ],
                    "bgp-peer-iosession": {
                        "iosession-state": "Enabled",
                        "iosession-thread-name": "bgpio-0",
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "684",
                            "active-prefix-count": "682",
                            "advertised-prefix-count": "0",
                            "bgp-rib-state": "BGP restart " "is complete",
                            "name": "inet.0",
                            "received-prefix-count": "684",
                            "rib-bit": "20000",
                            "send-state": "in sync",
                            "suppressed-prefix-count": "0",
                        },
                        {
                            "accepted-prefix-count": "2",
                            "active-prefix-count": "2",
                            "advertised-prefix-count": "0",
                            "bgp-rib-state": "BGP restart " "is complete",
                            "name": "inet.3",
                            "received-prefix-count": "2",
                            "rib-bit": "30000",
                            "send-state": "in sync",
                            "suppressed-prefix-count": "0",
                        },
                    ],
                    "active-holdtime": '30',
                    "peer-id": "10.169.14.240",
                    "local-id": "10.189.5.252",
                    "description": "sjkGDS221-EC11",
                    "entropy-label": "No",
                    "entropy-label-capability": "Yes",
                    "entropy-label-no-next-hop-validation": "Yes",
                    "entropy-label-stitching-capability": "Yes",
                    "flap-count": "127",
                    "group-index": "10",
                    "input-messages": "280022",
                    "input-octets": "7137084",
                    "input-refreshes": "0",
                    "input-updates": "61419",
                    "keepalive-interval": "10",
                    "last-checked": "1999164",
                    "last-error": "Hold Timer Expired Error",
                    "last-event": "RecvKeepAlive",
                    "last-flap-event": "HoldTime",
                    "last-received": "3",
                    "last-sent": "3",
                    "last-state": "OpenConfirm",
                    "local-address": "10.189.5.252+179",
                    "local-as": "65171",
                    "local-ext-nh-color-nlri": "inet-unicast",
                    "nlri-type": "inet-labeled-unicast",
                    "nlri-type-peer": "inet-unicast " "inet-labeled-unicast",
                    "nlri-type-session": "inet-unicast " "inet-labeled-unicast",
                    "output-messages": "221176",
                    "output-octets": "4202359",
                    "output-refreshes": "0",
                    "output-updates": "0",
                    "peer-4byte-as-capability-advertised": "65151",
                    "peer-addpath-not-supported": True,
                    "peer-address": "10.169.14.240+60606",
                    "peer-as": "65151",
                    "peer-cfg-rti": "master",
                    "peer-end-of-rib-received": "inet-unicast " "inet-labeled-unicast",
                    "peer-end-of-rib-sent": "inet-unicast " "inet-labeled-unicast",
                    "peer-flags": "Sync",
                    "peer-fwd-rti": "master",
                    "peer-group": "sjkGDS221-EC11",
                    "peer-index": "0",
                    "peer-no-llgr-restarter": True,
                    "peer-no-restart": True,
                    "peer-refresh-capability": "2",
                    "peer-restart-flags-received": "Notification",
                    "peer-restart-nlri-configured": "inet-unicast "
                    "inet-labeled-unicast",
                    "peer-restart-nlri-negotiated": "inet-unicast "
                    "inet-labeled-unicast",
                    "peer-stale-route-time-configured": "300",
                    "peer-state": "Established",
                    "peer-type": "External",
                    "snmp-index": "15",
                },
                {
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Multihop "
                        "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "Ttl "
                        "LogUpDown "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "(HKG-WC_out "
                        "&& "
                        "(NEXT-HOP-SELF "
                        "&& "
                        "HKG-WC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "30",
                        "local-address": "10.189.5.252",
                        "preference": "170",
                    },
                    "description": "obpGCS001-WC11",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "Start",
                    "last-state": "Idle",
                    "local-address": "10.189.5.252",
                    "local-as": "65171",
                    "peer-address": "10.169.14.249",
                    "peer-as": "65151",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "obpGCS001-WC11",
                    "peer-state": "Active",
                    "peer-type": "External",
                },
                {
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "LogUpDown "
                        "Cluster "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "ALL_out",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "60",
                        "import-policy": "REJ_LONG_ASPATH",
                        "local-address": "10.189.5.252",
                        "preference": "170",
                    },
                    "description": "cm-hkm003",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "ConnectRetry",
                    "last-state": "Active",
                    "local-address": "10.189.5.252",
                    "local-as": "65171",
                    "peer-address": "10.189.5.240+179",
                    "peer-as": "65171",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "v4_RRC_72_SQUARE",
                    "peer-state": "Connect",
                    "peer-type": "Internal",
                    "route-reflector-client": True,
                },
                {
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "LogUpDown "
                        "Cluster "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "ALL_out",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "60",
                        "import-policy": "REJ_LONG_ASPATH",
                        "local-address": "10.189.5.252",
                        "preference": "170",
                    },
                    "description": "cm-hkm004",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "ConnectRetry",
                    "last-state": "Active",
                    "local-address": "10.189.5.252",
                    "local-as": "65171",
                    "peer-address": "10.189.5.241+179",
                    "peer-as": "65171",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "v4_RRC_72_SQUARE",
                    "peer-state": "Connect",
                    "peer-type": "Internal",
                    "route-reflector-client": True,
                },
                {
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "LogUpDown "
                        "Cluster "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "(ALL_out "
                        "&& "
                        "v4_NEXT-HOP-SELF_pyats201) "
                        "] "
                        "Import: "
                        "[ "
                        "REJ_LONG_ASPATH",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "60",
                        "local-address": "10.189.5.252",
                        "preference": "170",
                    },
                    "description": "cm-hkt003",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "Start",
                    "last-state": "Idle",
                    "local-address": "10.189.5.252",
                    "local-as": "65171",
                    "peer-address": "10.189.5.242",
                    "peer-as": "65171",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "v4_RRC_72_TRIANGLE",
                    "peer-state": "Active",
                    "peer-type": "Internal",
                    "route-reflector-client": True,
                },
                {
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "LogUpDown "
                        "Cluster "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "(ALL_out "
                        "&& "
                        "v4_NEXT-HOP-SELF_pyats201) "
                        "] "
                        "Import: "
                        "[ "
                        "REJ_LONG_ASPATH",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "60",
                        "local-address": "10.189.5.252",
                        "preference": "170",
                    },
                    "description": "cm-hkt004",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "Start",
                    "last-state": "Idle",
                    "local-address": "10.189.5.252",
                    "local-as": "65171",
                    "peer-address": "10.189.5.243",
                    "peer-as": "65171",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "v4_RRC_72_TRIANGLE",
                    "peer-state": "Active",
                    "peer-type": "Internal",
                    "route-reflector-client": True,
                },
                {
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "LogUpDown "
                        "Cluster "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "(ALL_out "
                        "&& "
                        "v4_NEXT-HOP-SELF_pyats201) "
                        "] "
                        "Import: "
                        "[ "
                        "REJ_LONG_ASPATH",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "60",
                        "local-address": "10.189.5.252",
                        "preference": "170",
                    },
                    "description": "lg-hkt001",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "Start",
                    "last-state": "Idle",
                    "local-address": "10.189.5.252",
                    "local-as": "65171",
                    "peer-address": "10.189.5.245",
                    "peer-as": "65171",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "v4_RRC_72_TRIANGLE",
                    "peer-state": "Active",
                    "peer-type": "Internal",
                    "route-reflector-client": True,
                },
                {
                    "bgp-bfd": {
                        "bfd-configuration-state": "disabled",
                        "bfd-operational-state": "down",
                    },
                    "bgp-error": [
                        {
                            "name": "Hold Timer Expired " "Error",
                            "receive-count": "36",
                            "send-count": "18",
                        },
                        {"name": "Cease", "receive-count": "2", "send-count": "10"},
                    ],
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "LogUpDown "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "(v4_WATARI " "&& " "NEXT-HOP-SELF)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "60",
                        "local-address": "10.189.5.252",
                        "preference": "170",
                    },
                    "bgp-output-queue": [
                        {
                            "count": "0",
                            "number": "1",
                            "rib-adv-nlri": "inet-unicast",
                            "table-name": "inet.0",
                        }
                    ],
                    "bgp-peer-iosession": {
                        "iosession-state": "Enabled",
                        "iosession-thread-name": "bgpio-0",
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "682",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "682",
                            "bgp-rib-state": "BGP restart " "is complete",
                            "name": "inet.0",
                            "received-prefix-count": "682",
                            "rib-bit": "20001",
                            "send-state": "in sync",
                            "suppressed-prefix-count": "0",
                        }
                    ],
                    "description": "hktGCS002",
                    "flap-count": "44",
                    "group-index": "0",
                    "input-messages": "110633",
                    "input-octets": "2104771",
                    "input-refreshes": "0",
                    "input-updates": "4",
                    "keepalive-interval": "20",
                    "last-checked": "1999134",
                    "last-error": "Hold Timer Expired Error",
                    "last-event": "RecvKeepAlive",
                    "last-flap-event": "RecvNotify",
                    "last-received": "13",
                    "last-sent": "3",
                    "last-state": "OpenConfirm",
                    "local-address": "10.189.5.252+60144",
                    "local-as": "65171",
                    "local-ext-nh-color-nlri": "inet-unicast",
                    "nlri-type-peer": "inet-unicast",
                    "nlri-type-session": "inet-unicast",
                    "output-messages": "171942",
                    "output-octets": "5078640",
                    "output-refreshes": "0",
                    "output-updates": "61307",
                    "peer-4byte-as-capability-advertised": "65171",
                    "peer-addpath-not-supported": True,
                    "active-holdtime": '60',
                    "peer-id": "10.189.5.253",
                    "local-id": "10.189.5.252",
                    "peer-address": "10.189.5.253+179",
                    "peer-as": "65171",
                    "peer-cfg-rti": "master",
                    "peer-end-of-rib-received": "inet-unicast",
                    "peer-end-of-rib-sent": "inet-unicast",
                    "peer-flags": "Sync",
                    "peer-fwd-rti": "master",
                    "peer-group": "hktGCS002",
                    "peer-index": "0",
                    "peer-no-llgr-restarter": True,
                    "peer-no-restart": True,
                    "peer-refresh-capability": "2",
                    "peer-restart-flags-received": "Notification",
                    "peer-restart-nlri-configured": "inet-unicast",
                    "peer-restart-nlri-negotiated": "inet-unicast",
                    "peer-stale-route-time-configured": "300",
                    "peer-state": "Established",
                    "peer-type": "Internal",
                    "snmp-index": "0",
                },
                {
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Multihop "
                        "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "Ttl "
                        "LogUpDown "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "(ALL_out "
                        "&& "
                        "(NEXT-HOP-SELF "
                        "&& "
                        "HKG-SNG_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "30",
                        "local-address": "10.189.5.252",
                        "preference": "170",
                    },
                    "description": "sggjbb001",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "Start",
                    "last-state": "Idle",
                    "local-address": "10.189.5.252",
                    "local-as": "65171",
                    "peer-address": "10.189.6.250",
                    "peer-as": "65181",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "sggjbb001",
                    "peer-state": "Active",
                    "peer-type": "External",
                },
                {
                    "bgp-option-information": {
                        "bgp-options": "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "LogUpDown "
                        "Cluster "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "v6_Kentik_NO-DEFAULT",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "720",
                        "import-policy": "11",
                        "local-address": "2001:db8:223c:ca45::b",
                        "preference": "170",
                    },
                    "description": "v6_Kentik",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "ConnectRetry",
                    "last-state": "Active",
                    "local-address": "2001:db8:223c:ca45::b",
                    "local-as": "65171",
                    "peer-address": "2001:db8:6be:89bb::1:140+179",
                    "peer-as": "65171",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "v6_Kentik",
                    "peer-state": "Connect",
                    "peer-type": "Internal",
                    "route-reflector-client": True,
                },
                {
                    "bgp-bfd": {
                        "bfd-configuration-state": "disabled",
                        "bfd-operational-state": "down",
                    },
                    "bgp-error": [
                        {
                            "name": "Hold Timer Expired " "Error",
                            "receive-count": "24",
                            "send-count": "171",
                        },
                        {"name": "Cease", "receive-count": "5", "send-count": "0"},
                    ],
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Multihop "
                        "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "Ttl "
                        "LogUpDown "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "(v6_HKG-EC_out "
                        "&& "
                        "(NEXT-HOP-SELF "
                        "&& "
                        "v6_HKG-EC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "30",
                        "local-address": "2001:db8:223c:ca45::b",
                        "preference": "170",
                    },
                    "bgp-output-queue": [
                        {
                            "count": "0",
                            "number": "3",
                            "rib-adv-nlri": "inet6-unicast",
                            "table-name": "inet6.0",
                        }
                    ],
                    "bgp-peer-iosession": {
                        "iosession-state": "Enabled",
                        "iosession-thread-name": "bgpio-0",
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "0",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "0",
                            "bgp-rib-state": "BGP restart " "is complete",
                            "name": "inet6.0",
                            "received-prefix-count": "0",
                            "rib-bit": "40000",
                            "send-state": "in sync",
                            "suppressed-prefix-count": "0",
                        }
                    ],
                    "description": "sjkGDS221-EC11",
                    "flap-count": "133",
                    "group-index": "11",
                    "input-messages": "218603",
                    "input-octets": "4153468",
                    "input-refreshes": "0",
                    "input-updates": "1",
                    "keepalive-interval": "10",
                    "last-checked": "1999159",
                    "last-error": "Hold Timer Expired Error",
                    "last-event": "RecvKeepAlive",
                    "last-flap-event": "HoldTime",
                    "last-received": "1",
                    "last-sent": "3",
                    "last-state": "OpenConfirm",
                    "local-address": "2001:db8:223c:ca45::b+63754",
                    "local-as": "65171",
                    "local-ext-nh-color-nlri": "inet6-unicast",
                    "nlri-type-peer": "inet6-unicast",
                    "nlri-type-session": "inet6-unicast",
                    "output-messages": "221174",
                    "output-octets": "4202317",
                    "output-refreshes": "0",
                    "output-updates": "0",
                    "peer-4byte-as-capability-advertised": "65151",
                    "peer-addpath-not-supported": True,
                    "active-holdtime": '30',
                    "peer-id": "10.169.14.240",
                    "local-id": "10.189.5.252",
                    "peer-address": "2001:db8:eb18:ca45::1+179",
                    "peer-as": "65151",
                    "peer-cfg-rti": "master",
                    "peer-end-of-rib-received": "inet6-unicast",
                    "peer-end-of-rib-sent": "inet6-unicast",
                    "peer-flags": "Sync",
                    "peer-fwd-rti": "master",
                    "peer-group": "v6_sjkGDS221-EC11",
                    "peer-index": "0",
                    "peer-no-llgr-restarter": True,
                    "peer-no-restart": True,
                    "peer-refresh-capability": "2",
                    "peer-restart-flags-received": "Notification",
                    "peer-restart-nlri-configured": "inet6-unicast",
                    "peer-restart-nlri-negotiated": "inet6-unicast",
                    "peer-stale-route-time-configured": "300",
                    "peer-state": "Established",
                    "peer-type": "External",
                    "snmp-index": "16",
                },
                {
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Multihop "
                        "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "Ttl "
                        "LogUpDown "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "(v6_HKG-WC_out "
                        "&& "
                        "(NEXT-HOP-SELF "
                        "&& "
                        "v6_HKG-WC_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "30",
                        "local-address": "2001:db8:223c:ca45::b",
                        "preference": "170",
                    },
                    "description": "obpGCS001-WC11",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "Start",
                    "last-state": "Idle",
                    "local-address": "2001:db8:223c:ca45::b",
                    "local-as": "65171",
                    "peer-address": "2001:db8:eb18:ca45::11",
                    "peer-as": "65151",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "v6_obpGCS001-WC11",
                    "peer-state": "Active",
                    "peer-type": "External",
                },
                {
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "LogUpDown "
                        "Cluster "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "(ALL_out "
                        "&& "
                        "v6_NEXT-HOP-SELF_pyats201)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "60",
                        "local-address": "2001:db8:223c:ca45::b",
                        "preference": "170",
                    },
                    "description": "cm-hkt003",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "Start",
                    "last-state": "Idle",
                    "local-address": "2001:db8:223c:ca45::b",
                    "local-as": "65171",
                    "peer-address": "2001:db8:223c:ca45::7",
                    "peer-as": "65171",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "v6_RRC_72_TRIANGLE",
                    "peer-state": "Active",
                    "peer-type": "Internal",
                    "route-reflector-client": True,
                },
                {
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "LogUpDown "
                        "Cluster "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "(ALL_out "
                        "&& "
                        "v6_NEXT-HOP-SELF_pyats201)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "60",
                        "local-address": "2001:db8:223c:ca45::b",
                        "preference": "170",
                    },
                    "description": "cm-hkt004",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "ConnectRetry",
                    "last-state": "Active",
                    "local-address": "2001:db8:223c:ca45::b",
                    "local-as": "65171",
                    "peer-address": "2001:db8:223c:ca45::8+179",
                    "peer-as": "65171",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "v6_RRC_72_TRIANGLE",
                    "peer-state": "Connect",
                    "peer-type": "Internal",
                    "route-reflector-client": True,
                },
                {
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "LogUpDown "
                        "Cluster "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "ALL_out",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "60",
                        "local-address": "2001:db8:223c:ca45::b",
                        "preference": "170",
                    },
                    "description": "cm-hkm003",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "Start",
                    "last-state": "Idle",
                    "local-address": "2001:db8:223c:ca45::b",
                    "local-as": "65171",
                    "peer-address": "2001:db8:223c:ca45::9",
                    "peer-as": "65171",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "v6_RRC_72_SQUARE",
                    "peer-state": "Active",
                    "peer-type": "Internal",
                    "route-reflector-client": True,
                },
                {
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "LogUpDown "
                        "Cluster "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "ALL_out",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "60",
                        "local-address": "2001:db8:223c:ca45::b",
                        "preference": "170",
                    },
                    "description": "cm-hkm004",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "ConnectRetry",
                    "last-state": "Active",
                    "local-address": "2001:db8:223c:ca45::b",
                    "local-as": "65171",
                    "peer-address": "2001:db8:223c:ca45::a+179",
                    "peer-as": "65171",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "v6_RRC_72_SQUARE",
                    "peer-state": "Connect",
                    "peer-type": "Internal",
                    "route-reflector-client": True,
                },
                {
                    "bgp-bfd": {
                        "bfd-configuration-state": "disabled",
                        "bfd-operational-state": "down",
                    },
                    "bgp-error": [
                        {
                            "name": "Hold Timer Expired " "Error",
                            "receive-count": "40",
                            "send-count": "27",
                        },
                        {"name": "Cease", "receive-count": "0", "send-count": "16"},
                    ],
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "LogUpDown "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "(v6_WATARI " "&& " "NEXT-HOP-SELF)",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "60",
                        "local-address": "2001:db8:223c:ca45::b",
                        "preference": "170",
                    },
                    "bgp-output-queue": [
                        {
                            "count": "0",
                            "number": "3",
                            "rib-adv-nlri": "inet6-unicast",
                            "table-name": "inet6.0",
                        }
                    ],
                    "bgp-peer-iosession": {
                        "iosession-state": "Enabled",
                        "iosession-thread-name": "bgpio-0",
                    },
                    "bgp-rib": [
                        {
                            "accepted-prefix-count": "0",
                            "active-prefix-count": "0",
                            "advertised-prefix-count": "0",
                            "bgp-rib-state": "BGP restart " "is complete",
                            "name": "inet6.0",
                            "received-prefix-count": "0",
                            "rib-bit": "40001",
                            "send-state": "in sync",
                            "suppressed-prefix-count": "0",
                        }
                    ],
                    "description": "hktGCS002",
                    "flap-count": "55",
                    "group-index": "1",
                    "input-messages": "110662",
                    "input-octets": "2102633",
                    "input-refreshes": "0",
                    "input-updates": "1",
                    "keepalive-interval": "20",
                    "last-checked": "16510983",
                    "last-error": "Hold Timer Expired Error",
                    "last-event": "RecvKeepAlive",
                    "last-flap-event": "HoldTime",
                    "last-received": "6",
                    "last-sent": "5",
                    "last-state": "OpenConfirm",
                    "local-address": "2001:db8:223c:ca45::b+179",
                    "local-as": "65171",
                    "local-ext-nh-color-nlri": "inet6-unicast",
                    "nlri-type-peer": "inet6-unicast",
                    "nlri-type-session": "inet6-unicast",
                    "output-messages": "110664",
                    "output-octets": "2102627",
                    "output-refreshes": "0",
                    "output-updates": "0",
                    "peer-4byte-as-capability-advertised": "65171",
                    "peer-addpath-not-supported": True,
                    "active-holdtime": '60',
                    "peer-id": "10.189.5.253",
                    "local-id": "10.189.5.252",
                    "peer-address": "2001:db8:223c:ca45::c+60268",
                    "peer-as": "65171",
                    "peer-cfg-rti": "master",
                    "peer-end-of-rib-received": "inet6-unicast",
                    "peer-end-of-rib-sent": "inet6-unicast",
                    "peer-flags": "Sync",
                    "peer-fwd-rti": "master",
                    "peer-group": "v6_hktGCS002",
                    "peer-index": "0",
                    "peer-no-llgr-restarter": True,
                    "peer-no-restart": True,
                    "peer-refresh-capability": "2",
                    "peer-restart-flags-received": "Notification",
                    "peer-restart-nlri-configured": "inet6-unicast",
                    "peer-restart-nlri-negotiated": "inet6-unicast",
                    "peer-stale-route-time-configured": "300",
                    "peer-state": "Established",
                    "peer-type": "Internal",
                    "snmp-index": "1",
                },
                {
                    "bgp-option-information": {
                        "authentication-configured": True,
                        "bgp-options": "Multihop "
                        "Preference "
                        "LocalAddress "
                        "HoldTime "
                        "AuthKey "
                        "Ttl "
                        "LogUpDown "
                        "PeerAS "
                        "Refresh "
                        "Confed",
                        "bgp-options-extended": "GracefulShutdownRcv",
                        "bgp-options2": True,
                        "export-policy": "(ALL_out "
                        "&& "
                        "(NEXT-HOP-SELF "
                        "&& "
                        "v6_HKG-SNG_AddMED))",
                        "gshut-recv-local-preference": "0",
                        "holdtime": "30",
                        "local-address": "2001:db8:223c:ca45::b",
                        "preference": "170",
                    },
                    "description": "sggjbb001",
                    "flap-count": "0",
                    "last-error": "None",
                    "last-event": "Start",
                    "last-state": "Idle",
                    "local-address": "2001:db8:223c:ca45::b",
                    "local-as": "65171",
                    "peer-address": "2001:db8:5961:ca45::1",
                    "peer-as": "65181",
                    "peer-cfg-rti": "master",
                    "peer-flags": "",
                    "peer-fwd-rti": "master",
                    "peer-group": "v6_sggjbb001",
                    "peer-state": "Active",
                    "peer-type": "External",
                },
            ]
        }
    }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBgpNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)      

if __name__ == "__main__":
    unittest.main()
