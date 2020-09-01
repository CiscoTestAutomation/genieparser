import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_class import ShowClassMap


# ==============================
# Unit test for 'show class-map'
# ==============================
class TestShowClassMap(unittest.TestCase):
    """Unit test for 'show class-map'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
        "class_maps": {
            "system-cpp-police-ewlc-control": {
                "match_criteria": "match-any",
                "cm_id": 23,
                "description": "EWLC Control",
                "match_policy": "none"
            },
            "system-cpp-police-topology-control": {
                "match_criteria": "match-any",
                "cm_id": 2,
                "description": "Topology control",
                "match_policy": "none"
            },
            "system-cpp-police-sw-forward": {
                "match_criteria": "match-any",
                "cm_id": 3,
                "description": "Sw forwarding, L2 LVX data packets, LOGGING, Transit Traffic",
                "match_policy": "none"
            },
            "system-cpp-default": {
                "match_criteria": "match-any",
                "cm_id": 4,
                "description": "EWLC Data, Inter FED Traffic",
                "match_policy": "none"
            },
            "system-cpp-police-sys-data": {
                "match_criteria": "match-any",
                "cm_id": 5,
                "description": "Openflow, Exception, EGR Exception, NFL Sampled Data, RPF Failed",
                "match_policy": "none"
            },
            "system-cpp-police-punt-webauth": {
                "match_criteria": "match-any",
                "cm_id": 6,
                "description": "Punt Webauth",
                "match_policy": "none"
            },
            "system-cpp-police-l2lvx-control": {
                "match_criteria": "match-any",
                "cm_id": 7,
                "description": "L2 LVX control packets",
                "match_policy": "none"
            },
            "class-default": {
                "match_criteria": "match-any",
                "cm_id": 0,
                "match_policy": "any"
            },
            "system-cpp-police-forus": {
                "match_criteria": "match-any",
                "cm_id": 8,
                "description": "Forus Address resolution and Forus traffic",
                "match_policy": "none"
            },
            "system-cpp-police-multicast-end-station": {
                "match_criteria": "match-any",
                "cm_id": 9,
                "description": "MCAST END STATION",
                "match_policy": "none"
            },
            "system-cpp-police-high-rate-app": {
                "match_criteria": "match-any",
                "cm_id": 10,
                "description": "High Rate Applications",
                "match_policy": "none"
            },
            "system-cpp-police-multicast": {
                "match_criteria": "match-any",
                "cm_id": 11,
                "description": "MCAST Data",
                "match_policy": "none"
            },
            "system-cpp-police-l2-control": {
                "match_criteria": "match-any",
                "cm_id": 12,
                "description": "L2 control",
                "match_policy": "none"
            },
            "system-cpp-police-dot1x-auth": {
                "match_criteria": "match-any",
                "cm_id": 13,
                "description": "DOT1X Auth",
                "match_policy": "none"
            },
            "system-cpp-police-data": {
                "match_criteria": "match-any",
                "cm_id": 14,
                "description": "ICMP redirect, ICMP_GEN and BROADCAST",
                "match_policy": "none"
            },
            "system-cpp-police-stackwise-virt-control": {
                "match_criteria": "match-any",
                "cm_id": 15,
                "description": "Stackwise Virtual OOB",
                "match_policy": "none"
            },
            "system-cpp-police-control-low-priority": {
                "match_criteria": "match-any",
                "cm_id": 16,
                "description": "General punt",
                "match_policy": "none"
            },
            "non-client-nrt-class": {
                "match_criteria": "match-any",
                "cm_id": 1,
                "match_policy": "non-client-nrt"
            },
            "system-cpp-police-routing-control": {
                "match_criteria": "match-any",
                "cm_id": 17,
                "description": "Routing control and Low Latency",
                "match_policy": "none"
            },
            "system-cpp-police-protocol-snooping": {
                "match_criteria": "match-any",
                "cm_id": 18,
                "description": "Protocol snooping",
                "match_policy": "none"
            },
            "system-cpp-police-dhcp-snooping": {
                "match_criteria": "match-any",
                "cm_id": 19,
                "description": "DHCP snooping",
                "match_policy": "none"
            },
            "system-cpp-police-ios-routing": {
                "match_criteria": "match-any",
                "cm_id": 21,
                "description": "L2 control, Topology control, Routing control, Low Latency",
                "match_policy": "none"
            },
            "system-cpp-police-system-critical": {
                "match_criteria": "match-any",
                "cm_id": 20,
                "description": "System Critical and Gold Pkt",
                "match_policy": "none"
            },
            "system-cpp-police-ios-feature": {
                "match_criteria": "match-any",
                "cm_id": 22,
                "description": "ICMPGEN,BROADCAST,ICMP,L2LVXCntrl,ProtoSnoop,PuntWebauth,MCASTData,Transit,DOT1XAuth,Swfwd,LOGGING,L2LVXData,ForusTraffic,ForusARP,McastEndStn,Openflow,Exception,EGRExcption,NflSampled,RpfFailed",
                "match_policy": "none"
            }
        }
    }


    golden_output1 = {'execute.return_value': '''
Class Map match-any system-cpp-police-ewlc-control (id 23)
  Description: EWLC Control 
   Match none 

 Class Map match-any system-cpp-police-topology-control (id 2)
  Description: Topology control
   Match none 

 Class Map match-any system-cpp-police-sw-forward (id 3)
  Description: Sw forwarding, L2 LVX data packets, LOGGING, Transit Traffic
   Match none 

 Class Map match-any system-cpp-default (id 4)
  Description: EWLC Data, Inter FED Traffic 
   Match none 

 Class Map match-any system-cpp-police-sys-data (id 5)
  Description: Openflow, Exception, EGR Exception, NFL Sampled Data, RPF Failed
   Match none 

 Class Map match-any system-cpp-police-punt-webauth (id 6)
  Description: Punt Webauth
   Match none 

 Class Map match-any system-cpp-police-l2lvx-control (id 7)
  Description: L2 LVX control packets
   Match none 

 Class Map match-any class-default (id 0)
   Match any 

 Class Map match-any system-cpp-police-forus (id 8)
  Description: Forus Address resolution and Forus traffic
   Match none 

 Class Map match-any system-cpp-police-multicast-end-station (id 9)
  Description: MCAST END STATION
   Match none 

 Class Map match-any system-cpp-police-high-rate-app (id 10)
  Description: High Rate Applications 
   Match none 

 Class Map match-any system-cpp-police-multicast (id 11)
  Description: MCAST Data
   Match none 

 Class Map match-any system-cpp-police-l2-control (id 12)
  Description: L2 control
   Match none 

 Class Map match-any system-cpp-police-dot1x-auth (id 13)
  Description: DOT1X Auth
   Match none 

 Class Map match-any system-cpp-police-data (id 14)
  Description: ICMP redirect, ICMP_GEN and BROADCAST
   Match none 

 Class Map match-any system-cpp-police-stackwise-virt-control (id 15)
  Description: Stackwise Virtual OOB
   Match none 

 Class Map match-any system-cpp-police-control-low-priority (id 16)
  Description: General punt
   Match none 

 Class Map match-any non-client-nrt-class (id 1)
   Match non-client-nrt 
 Class Map match-any system-cpp-police-routing-control (id 17)
  Description: Routing control and Low Latency
   Match none 

 Class Map match-any system-cpp-police-protocol-snooping (id 18)
  Description: Protocol snooping
   Match none 

 Class Map match-any system-cpp-police-dhcp-snooping (id 19)
  Description: DHCP snooping
   Match none 

 Class Map match-any system-cpp-police-ios-routing (id 21)
  Description: L2 control, Topology control, Routing control, Low Latency
   Match none 

 Class Map match-any system-cpp-police-system-critical (id 20)
  Description: System Critical and Gold Pkt
   Match none 

 Class Map match-any system-cpp-police-ios-feature (id 22)
  Description: ICMPGEN,BROADCAST,ICMP,L2LVXCntrl,ProtoSnoop,PuntWebauth,MCASTData,Transit,DOT1XAuth,Swfwd,LOGGING,L2LVXData,ForusTraffic,ForusARP,McastEndStn,Openflow,Exception,EGRExcption,NflSampled,RpfFailed
   Match none
    '''}

    def test_show_class_map_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowClassMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_class_map_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowClassMap(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
