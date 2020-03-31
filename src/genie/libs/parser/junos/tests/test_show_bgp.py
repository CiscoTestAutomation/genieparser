
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# junos show_ospf
from genie.libs.parser.junos.show_bgp import (ShowBgpGroupBrief)


class TestShowBgpGroupBrief(unittest.TestCase):
    """ Unit tests for:
            * show ospf interface
            * show ospf interface {interface}
    """
    maxDiff = None
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: hktGCS002       Index: 0                   Flags: <Export Eval>
        Export: [ (v4_WATARI && NEXT-HOP-SELF) ] 
        Options: <Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 1
        111.87.5.253+179
        inet.0: 0/682/682/0

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v6_hktGCS002    Index: 1                   Flags: <Export Eval>
        Export: [ (v6_WATARI && NEXT-HOP-SELF) ] 
        Options: <Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 1
        2001:268:fb90::c+60268
        inet6.0: 0/0/0/0

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v4_RRC_72_TRIANGLE Index: 2                Flags: <Export Eval>
        Export: [ (ALL_out && v4_NEXT-HOP-SELF_hktGCS001) ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 3        Established: 0
        111.87.5.245+179
        111.87.5.243+179
        111.87.5.242+179

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v6_RRC_72_TRIANGLE Index: 3                Flags: <Export Eval>
        Export: [ (ALL_out && v6_NEXT-HOP-SELF_hktGCS001) ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 2        Established: 0  
        2001:268:fb90::7+179
        2001:268:fb90::8

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v6_RRC_72_SQUARE Index: 4                  Flags: <Export Eval>
        Export: [ ALL_out ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 2        Established: 0
        2001:268:fb90::9
        2001:268:fb90::a

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v4_RRC_72_SQUARE Index: 5                  Flags: <Export Eval>
        Export: [ ALL_out ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 2        Established: 0
        111.87.5.241+179
        111.87.5.240

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v4_Kentik       Index: 6                   Flags: <Export Eval>
        Export: [ v4_Kentik_NO-DEFAULT ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        27.85.216.179

        Group Type: Internal    AS: 65171                  Local AS: 65171
        Name: v6_Kentik       Index: 7                   Flags: <Export Eval>
        Export: [ v6_Kentik_NO-DEFAULT ] 
        Options: <Cluster Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0                           
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        2001:268:fa03:272::1:140

        Group Type: External                               Local AS: 65171
        Name: sggjbb001       Index: 8                   Flags: <Export Eval>
        Export: [ (ALL_out && (NEXT-HOP-SELF && HKG-SNG_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        111.87.6.250

        Group Type: External                               Local AS: 65171
        Name: v6_sggjbb001    Index: 9                   Flags: <Export Eval>
        Export: [ (ALL_out && (NEXT-HOP-SELF && v6_HKG-SNG_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        2001:268:fb91::1

        Group Type: External                               Local AS: 65171
        Name: sjkGCS001-EC11  Index: 10                  Flags: <Export Eval>
        Export: [ ((LABELSTACK_O2B || HKG-EC_out) && (NEXT-HOP-SELF && HKG-EC_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 1
        106.187.14.240+60606
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
        2001:268:fb8f::1+179
        inet6.0: 0/0/0/0

        Group Type: External                               Local AS: 65171
        Name: obpGCS001-WC11  Index: 12                  Flags: <Export Eval>
        Export: [ (HKG-WC_out && (NEXT-HOP-SELF && HKG-WC_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        106.187.14.249

        Group Type: External                               Local AS: 65171
        Name: v6_obpGCS001-WC11 Index: 13                Flags: <Export Eval>
        Export: [ (v6_HKG-WC_out && (NEXT-HOP-SELF && v6_HKG-WC_AddMED)) ] 
        Options: <Multihop Confed>
        Options: <GracefulShutdownRcv>
        Holdtime: 0
        Graceful Shutdown Receiver local-preference: 0
        Total peers: 1        Established: 0
        2001:268:fb8f::11

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
                    "name": "hktGCS002",
                    "peer-address": [
                        "111.87.5.253+179"
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
                    "name": "v6_hktGCS002",
                    "peer-address": [
                        "2001:268:fb90::c+60268"
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
                        "111.87.5.245+179",
                        "111.87.5.243+179",
                        "111.87.5.242+179"
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
                        "2001:268:fb90::7+179",
                        "2001:268:fb90::8"
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
                        "2001:268:fb90::9",
                        "2001:268:fb90::a"
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
                        "111.87.5.241+179",
                        "111.87.5.240"
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
                        "27.85.216.179"
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
                        "2001:268:fa03:272::1:140"
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
                        "111.87.6.250"
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
                        "2001:268:fb91::1"
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
                        "106.187.14.240+60606"
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
                        "2001:268:fb8f::1+179"
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
                        "106.187.14.249"
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
                        "2001:268:fb8f::11"
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

    def test_show_ospf_interface_detail(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBgpGroupBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
