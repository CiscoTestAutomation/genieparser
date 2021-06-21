import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ===================
# Schema for:
#  * 'show class-map'
# ===================
class ShowClassMapSchema(MetaParser):
    """Schema for show class-map."""

    schema = {
        "class_maps": {
            str: {
              "match_criteria": str,
              "cm_id": int,
              Optional("description"): str,
              "index": {
                  int: {
                      Optional("match"): {
                          Optional(str): list
                      }
                  }
              }
            }
        }
    }


# ===================
# Parser for:
#  * 'show class-map'
# ===================
class ShowClassMap(ShowClassMapSchema):
    """Parser for show class-map"""

    cli_command = ['show class-map', 'show class-map {class_map}']

    def cli(self, class_map='', output=None):
        if output is None:
            if class_map:
                cmd = self.cli_command[1].format(class_map=class_map)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        #Class Map match-any system-cpp-police-ewlc-control (id 23)
        #  Description: EWLC Control
        #   Match none
        #
        # Class Map match-any system-cpp-police-topology-control (id 2)
        #  Description: Topology control
        #   Match none
        #
        # Class Map match-any system-cpp-police-sw-forward (id 3)
        #  Description: Sw forwarding, L2 LVX data packets, LOGGING, Transit Traffic
        #   Match none
        #
        # Class Map match-any system-cpp-default (id 4)
        #  Description: EWLC Data, Inter FED Traffic
        #   Match none
        #
        # Class Map match-any system-cpp-police-sys-data (id 5)
        #  Description: Openflow, Exception, EGR Exception, NFL Sampled Data, RPF Failed
        #   Match none
        #
        # Class Map match-any system-cpp-police-punt-webauth (id 6)
        #  Description: Punt Webauth
        #   Match none
        #
        # Class Map match-any system-cpp-police-l2lvx-control (id 7)
        #  Description: L2 LVX control packets
        #   Match none
        #
        # Class Map match-any class-default (id 0)
        #   Match any
        #
        # Class Map match-any system-cpp-police-forus (id 8)
        #  Description: Forus Address resolution and Forus traffic
        #   Match none
        #
        # Class Map match-any system-cpp-police-multicast-end-station (id 9)
        #  Description: MCAST END STATION
        #   Match none
        #
        # Class Map match-any system-cpp-police-high-rate-app (id 10)
        #  Description: High Rate Applications
        #   Match none
        #
        # Class Map match-any system-cpp-police-multicast (id 11)
        #  Description: MCAST Data
        #   Match none
        #
        # Class Map match-any system-cpp-police-l2-control (id 12)
        #  Description: L2 control
        #   Match none
        #
        # Class Map match-any system-cpp-police-dot1x-auth (id 13)
        #  Description: DOT1X Auth
        #   Match none
        #
        # Class Map match-any system-cpp-police-data (id 14)
        #  Description: ICMP redirect, ICMP_GEN and BROADCAST
        #   Match none
        #
        # Class Map match-any system-cpp-police-stackwise-virt-control (id 15)
        #  Description: Stackwise Virtual OOB
        #   Match none
        #
        # Class Map match-any system-cpp-police-control-low-priority (id 16)
        #  Description: General punt
        #   Match none
        #
        # Class Map match-any non-client-nrt-class (id 1)
        #   Match non-client-nrt
        # Class Map match-any system-cpp-police-routing-control (id 17)
        #  Description: Routing control and Low Latency
        #   Match none
        #
        # Class Map match-any system-cpp-police-protocol-snooping (id 18)
        #  Description: Protocol snooping
        #   Match none
        #
        # Class Map match-any system-cpp-police-dhcp-snooping (id 19)
        #  Description: DHCP snooping
        #   Match none
        #
        # Class Map match-any system-cpp-police-ios-routing (id 21)
        #  Description: L2 control, Topology control, Routing control, Low Latency
        #   Match none
        #
        # Class Map match-any system-cpp-police-system-critical (id 20)
        #  Description: System Critical and Gold Pkt
        #   Match none
        #
        # Class Map match-any system-cpp-police-ios-feature (id 22)
        #  Description: ICMPGEN,BROADCAST,ICMP,L2LVXCntrl,ProtoSnoop,PuntWebauth,MCASTData,Transit,DOT1XAuth,Swfwd,LOGGING,L2LVXData,ForusTraffic,ForusARP,McastEndStn,Openflow,Exception,EGRExcption,NflSampled,RpfFailed
        #   Match none

        class_map_dict = {}

        # Class Map match-any system-cpp-police-ios-feature (id 22)
        cm_header_capture = re.compile(
            r"^(\s+|)Class\sMap\s(?P<match_criteria>\S+)\s+(?P<cm_name>\S+)\s+\(id\s+(?P<cm_id>\d+)\)")

        #  Description: ICMPGEN,BROADCAST,ICMP,L2LVXCntrl,ProtoSnoop,PuntWebauth,MCASTData,Transit,DOT1XAuth,Swfwd,LOGGING,L2LVXData,ForusTraffic,ForusARP,McastEndStn,Openflow,Exception,EGRExcption,NflSampled,RpfFailed
        description_capture = re.compile(r"^Description:\s+(?P<description>.*$)")

        # Match access-group name AutoConf-4.0-Acl-Transactional-Data
        p_match_access = re.compile(r"^Match\s+access-group\s+name\s+(?P<value>.*)$")

        # Match protocol attribute traffic-class multimedia-conferencing
        p_match_protocol = re.compile(r"^Match\s+protocol\s+attribute\s+(?P<value>.*)$")

        # Match none
        p_match_none = re.compile(r"^Match\s+none$")

        # Match any
        p_match_any = re.compile(r"^Match\s+any$")

        # Match non-client-nrt
        p_match_non_client = re.compile(r"^Match\s+non-client-nrt$")

        # Match   dscp af21 (18) af22 (20) af23 (22)
        p_match_dscp = re.compile(r"^Match\s+dscp\s+(?P<values>.*)$")

        # Match cos  2
        p_match_cos = re.compile(r"^Match\s+cos\s+(?P<values>.*)$")

        match_index = 1

        # Remove unwanted lines from raw text
        for line in out.splitlines():
            line = line.strip()
            # Class Map match-any system-cpp-police-ios-feature (id 22)
            cm_match = cm_header_capture.match(line)
            if not class_map_dict.get('class_maps'):
                class_map_dict['class_maps'] = {}
            if cm_match:
                groups = cm_match.groupdict()
                cm_name = groups['cm_name']
                match_criteria = groups['match_criteria']
                cm_id = int(groups['cm_id'])
                if not class_map_dict['class_maps'].get(cm_name, {}):
                    class_map_dict['class_maps'].update({cm_name: {}})
                class_map_dict['class_maps'][cm_name].update({'match_criteria': match_criteria, 'cm_id': cm_id})
                match_index = 1
                continue
            #  Description: ICMPGEN,BROADCAST,ICMP,L2LVXCntrl,ProtoSnoop,PuntWebauth,MCASTData,Transit,DOT1XAuth,Swfwd,LOGGING,L2LVXData,ForusTraffic,ForusARP,McastEndStn,Openflow,Exception,EGRExcption,NflSampled,RpfFailed
            desc_match = description_capture.match(line)
            if desc_match:
                groups = desc_match.groupdict()
                description = groups['description']
                if class_map_dict['class_maps'].get(cm_name, {}):
                    class_map_dict['class_maps'][cm_name].update({'description': description})
                continue
            elif p_match_access.match(line):
                # Match access-group name AutoConf-4.0-Acl-Transactional-Data
                match = p_match_access.match(line)
                if not class_map_dict['class_maps'][cm_name].get("index"):
                  class_map_dict['class_maps'][cm_name].update({ "index": {} })
                class_map_dict["class_maps"][cm_name]["index"].update({ match_index: {} })
                class_map_dict['class_maps'][cm_name]["index"][match_index].update({ "match": { "access_group": [] }})
                class_map_dict["class_maps"][cm_name]["index"][match_index]["match"]["access_group"].append(match.group("value"))
                match_index += 1
                continue
            elif p_match_protocol.match(line):
                # Match protocol attribute traffic-class multimedia-conferencing
                match = p_match_protocol.match(line)
                if not class_map_dict['class_maps'][cm_name].get("index"):
                  class_map_dict['class_maps'][cm_name].update({ "index": {} })
                class_map_dict["class_maps"][cm_name]["index"].update({ match_index: {} })
                class_map_dict['class_maps'][cm_name]["index"][match_index].update({ "match": { "protocol_attribute": [] }})
                class_map_dict["class_maps"][cm_name]["index"][match_index]["match"]["protocol_attribute"].append(match.group("value"))
                match_index += 1
                continue
            elif p_match_none.match(line):
                # Match none
                if not class_map_dict['class_maps'][cm_name].get("index"):
                  class_map_dict['class_maps'][cm_name].update({ "index": {} })
                class_map_dict["class_maps"][cm_name]["index"].update({ match_index: {} })
                class_map_dict['class_maps'][cm_name]["index"][match_index].update({ "match": { "policy": [] }})
                class_map_dict["class_maps"][cm_name]["index"][match_index]["match"]["policy"].append("none")
                match_index += 1
                continue
            elif p_match_any.match(line):
                if not class_map_dict['class_maps'][cm_name].get("index"):
                   class_map_dict['class_maps'][cm_name].update({ "index": {} })
                class_map_dict["class_maps"][cm_name]["index"].update({ match_index: {} })
                class_map_dict['class_maps'][cm_name]["index"][match_index].update({ "match": { "policy": [] }})
                class_map_dict["class_maps"][cm_name]["index"][match_index]["match"]["policy"].append("any")
                match_index += 1
                continue
            elif p_match_non_client.match(line):
                # Match non-client-nrt
                if not class_map_dict['class_maps'][cm_name].get("index"):
                   class_map_dict['class_maps'][cm_name].update({ "index": {} })
                class_map_dict["class_maps"][cm_name]["index"].update({ match_index: {} })
                class_map_dict['class_maps'][cm_name]["index"][match_index].update({ "match": { "policy": [] }})
                class_map_dict["class_maps"][cm_name]["index"][match_index]["match"]["policy"].append("non_client_nrt")
                match_index += 1
                continue
            elif p_match_dscp.match(line):
                # Match   dscp af21 (18) af22 (20) af23 (22)
                match = p_match_dscp.match(line)
                if not class_map_dict['class_maps'][cm_name].get("index"):
                  class_map_dict['class_maps'][cm_name].update({ "index": {} })
                class_map_dict["class_maps"][cm_name]["index"].update({ match_index: {} })
                class_map_dict['class_maps'][cm_name]["index"][match_index].update({ "match": { "dscp": [] }})
                dscp_values = match.group("values").split(" ")
                dscp_list = [dscp_values[index] for index in range(0, len(dscp_values), 2)]
                class_map_dict["class_maps"][cm_name]["index"][match_index]["match"]["dscp"] = dscp_list
                match_index += 1
                continue
            elif p_match_cos.match(line):
                # Match cos  2
                match = p_match_cos.match(line)
                if not class_map_dict["class_maps"][cm_name].get("index"):
                  class_map_dict["class_maps"][cm_name].update({ "index": {} })
                class_map_dict["class_maps"][cm_name]["index"].update({ match_index: {} })
                class_map_dict["class_maps"][cm_name]["index"][match_index].update({ "match": { "cos": [] }})
                cos_values = match.group("values").split(" ")
                class_map_dict["class_maps"][cm_name]["index"][match_index]["match"]["cos"] = cos_values
                match_index += 1
                continue

        return class_map_dict
