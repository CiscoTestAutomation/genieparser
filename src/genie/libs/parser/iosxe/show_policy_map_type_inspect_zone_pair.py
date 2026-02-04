# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, ListOf

# parser utils
from genie.libs.parser.utils.common import Common

class ShowPolicyMapTypeInspectZonePairSchema(MetaParser):
    ''' Schema for show policy-map type inspect zone-pair {zone_pair_name}
                   show policy-map type inspect zone-pair  '''
    schema = {
        "zone_pair":{
            Any():{
                "service_policy_inspect":{
                    Any():{
                        "class_map":{
                            Any():{
                                "class_map_type": str,
                                "class_map_match": list,
                                "class_map_action":{
                                    Any():{
                                        Optional("packet_type"):{
                                            Any():{
                                                Optional("switch1_type"):str,
                                                Optional("packets_in_switch1"): int,
                                                Optional("switch2_type"): str,
                                                Optional("packets_in_switch2"): int,
                                            },
                                        },
                                        Optional("sessions_since_startup_or_reset"): int,
                                        Optional("current_session_counts_estab"): int,
                                        Optional("current_session_counts_half_open"): int,
                                        Optional("current_session_counts_terminating"): int,
                                        Optional("maxever_session_counts_estab"):int,
                                        Optional("maxever_session_counts_half_open"):int,
                                        Optional("maxever_session_counts_terminating"):int,
                                        Optional("last_session_created"):str,
                                        Optional("last_statistic_reset"): str,
                                        Optional("last_session_creation_rate"): int,
                                        Optional("last_half_open_session_total"): int,
                                        Optional("total_packets"): int,
                                        Optional("total_bytes"): int
                                    },
                                }
                            },
                        }
                    },
                }
            },
        } 
    }  



class ShowPolicyMapTypeInspectZonePair(ShowPolicyMapTypeInspectZonePairSchema):

    """ Parser for:
      show policy-map type inspect zone-pair
      show policy-map type inspect zone-pair {zone_pair_name} """
    
    
    cli_command = ["show policy-map type inspect zone-pair",
                   "show policy-map type inspect zone-pair {zone_pair_name}"]

    def cli(self, zone_pair_name='',output=None):
        if output is None:
            if zone_pair_name:
                out = self.device.execute(self.cli_command[1].format(zone_pair_name=zone_pair_name))
            else:
                out = self.device.execute(self.cli_command[0])
            
        else:
            out = output

        #Zone-pair: GREEN->DEFAULT
        p1=re.compile(r'\s*Zone-pair+\:+\s+(?P<zone_pair_name>\S+)')

        #Service-policy inspect : TEST
        p2=re.compile(r'\s*Service-policy+\s+inspect+\s+\:+\s+(?P<service_policy_inspect>[\w\W]+)')

        # Class-map: TEST (match-any)
        p3=re.compile(r'\s*Class-map+\:+\s+(?P<class_map_name>[\w-]+)+\s+\(+(?P<class_map_type>\S+)+\)')

        # Match: access-group name HBN2
        p4=re.compile(r'\s*Match+\:+\s+(?P<class_map_match>[\w\W]+)')

        #Inspect
        #Pass
        #Drop
        p5=re.compile(r'\s*(?P<class_map_action>Inspect|Pass|Drop)')

        # Session creations since subsystem startup or last reset 500445
        p6=re.compile(r'\s*Session+\s+creations+\s+since+\s+subsystem+\s+startup+\s+or+\s+last+\s+reset+\s(?P<session_since_reset_or_startup>\d+)')

        # Current session counts (estab/half-open/terminating) [0:0:0]
        p7=re.compile(r'\s*Current+\s+session+\s+counts+\s+\(+estab+\/+half-open+\/+terminating+\)+\s+\[+(?P<session_estab>\d+)+\:+(?P<session_half_open>\d+)+\:+(?P<session_terminating>\d+)+\]')

        # Maxever session counts (estab/half-open/terminating) [500445:428088:0]
        p8=re.compile(r'\s*Maxever+\s+session+\s+counts+\s+\(+estab+\/+half-open+\/+terminating+\)+\s+\[+(?P<max_session_estab>\d+)+\:+(?P<max_session_half_open>\d+)+\:+(?P<max_session_terminating>\d+)+\]')

        #Last session created 00:16:40
        p9=re.compile(r'\s*Last+\s+session+\s+created+\s+(?P<last_sess_created>[\w\W]+)')

        #Last statistic reset never
        p10=re.compile(r'\s*Last+\s+statistic+\s+reset+\s+(?P<last_statistic_reset>[\w\W]+)')

        #Last session creation rate 0
        p11=re.compile(r'\s*Last+\s+session+\s+creation+\s+rate+\s+(?P<last_session_creation_rate>\d+)')

        #Last half-open session total 0
        p12=re.compile(r'\s*Last+\s+half-open+\s+session+\s+total+\s+(?P<last_half_open_session_total>\d+)')

        #0 packets, 0 bytes
        p13=re.compile(r'\s*(?P<packets_total>\d+)+\s+packets+\,+\s+(?P<bytes_total>\d+)+\s+bytes')

        #Packet inspection statistics [process switch:fast switch]
        p14=re.compile(r'\s*Packet+\s+inspection+\s+statistics+\s+\[+(?P<switch1_type>[\w\s]+)+\:(?P<switch2_type>[\w\s]+)+\]')

        #udp packets: [0:84014582]
        p15=re.compile(r'\s*(?P<packet_type>\w+)+\s+packets+\:+\s+\[+(?P<packets_switch1>\d+)+\:(?P<packets_switch2>\d+)+\]')

        parsed_dict={}

        pending_packets_bytes = None
        class_map_action_dict = None
        for line in out.splitlines():

            #Zone-pair: GREEN->DEFAULT
            m1= p1.match(line)
            if m1:
                #{'zone_pair_name':'GREEN->DEFAULT'}
                groups=m1.groupdict()
                zone_pair_dict= parsed_dict.setdefault('zone_pair', {}).setdefault(groups['zone_pair_name'], {})
                pending_packets_bytes = None
                class_map_action_dict = None
            #Service-policy inspect : TEST
            m2= p2.match(line)
            if m2:
                #{'service_policy_inspect':'TEST'}
                groups = m2.groupdict()
                service_policy_dict = zone_pair_dict.\
                    setdefault('service_policy_inspect', {}).\
                    setdefault(groups['service_policy_inspect'], {})
                pending_packets_bytes = None
                class_map_action_dict = None
            # Class-map: TEST (match-any)
            m3= p3.match(line)
            if m3:
                #{'class_map_name':'TEST','class_map_type':'match-any'}
                groups=m3.groupdict()

                class_map_dict = service_policy_dict.\
                    setdefault('class_map', {}).\
                    setdefault(groups['class_map_name'], {})

                class_map_dict.update({'class_map_type': groups['class_map_type']})
                pending_packets_bytes = None
                class_map_action_dict = None
            # Match: access-group name HBN2
            m4= p4.match(line)
            if m4:
                #{'class_map_match':'access-group name HBN2'}
                groups=m4.groupdict()
                class_map_match_list = class_map_dict.setdefault('class_map_match', [])
                class_map_match_list.append(groups['class_map_match'])
                
            # 0 packets, 0 bytes
            m13 = p13.match(line)
            if m13:
                groups = m13.groupdict()
                pending_packets_bytes = {
                    'total_packets': int(groups['packets_total']),
                    'total_bytes': int(groups['bytes_total'])
                }
                # If we already have an action context, apply it immediately
                if class_map_action_dict is not None:
                    class_map_action_dict.update(pending_packets_bytes)
                    pending_packets_bytes = None

            #Inspect #Pass #Drop
            m5= p5.match(line)
            if m5:
                #{'class_map_action':'Inspect'}
                groups=m5.groupdict()
                class_map_action_dict = class_map_dict.\
                    setdefault('class_map_action', {}).\
                    setdefault(groups['class_map_action'], {})
                if pending_packets_bytes is not None:
                    class_map_action_dict.update(pending_packets_bytes)
                    pending_packets_bytes = None
                continue

            # Session creations since subsystem startup or last reset 5004458
            m6= p6.match(line)
            if m6:
                #{'session_since_reset_or_startup':500445}
                groups=m6.groupdict()
                class_map_action_dict.update({
                    'sessions_since_startup_or_reset': int(groups['session_since_reset_or_startup'])
                })

            # Current session counts (estab/half-open/terminating) [0:0:0]
            m7= p7.match(line)
            if m7:
                #{'session_estab':500445,'session_half_open':0,'session_terminating':0}
                groups=m7.groupdict()
                class_map_action_dict.update({
                    'current_session_counts_estab': int(groups['session_estab']),
                    'current_session_counts_half_open': int(groups['session_half_open']),
                    'current_session_counts_terminating': int(groups['session_terminating'])
                })
            # Maxever session counts (estab/half-open/terminating) [500445:428088:0]
            m8= p8.match(line)
            if m8:
                #{'max_session_estab':500445,'max_session_half_open':428088,'max_session_terminating':0}
                groups=m8.groupdict()
                class_map_action_dict.update({
                    'maxever_session_counts_estab': int(groups['max_session_estab']),
                    'maxever_session_counts_half_open': int(groups['max_session_half_open']),
                    'maxever_session_counts_terminating': int(groups['max_session_terminating'])
                })
            #Last session created 00:16:40
            m9= p9.match(line)
            if m9:
                #{'last_sess_created':'00:16:40'}
                groups=m9.groupdict()
                class_map_action_dict.update({
                    'last_session_created': groups['last_sess_created']
                })
            
            #Last statistic reset never
            m10= p10.match(line)
            if m10:
                #{'last_statistic_reset': 'never'}
                groups=m10.groupdict()
                class_map_action_dict.update({
                    'last_statistic_reset': groups['last_statistic_reset']
                })

            #Last session creation rate 0
            m11= p11.match(line)
            if m11:
                #{'last_session_creation_rate':0}
                groups=m11.groupdict()
                class_map_action_dict.update({
                    'last_session_creation_rate': int(groups['last_session_creation_rate'])
                })
            #Last half-open session total 0
            m12= p12.match(line)
            if m12:
                #{'last_half_open_session_total':0}
                groups=m12.groupdict()
                class_map_action_dict.update({
                    'last_half_open_session_total': int(groups['last_half_open_session_total'])
                })

            #Packet inspection statistics [process switch:fast switch]
            m14= p14.match(line)
            if m14:
                #{'switch1_type':'process switch','switch2_type':''fast switch'}
                groups=m14.groupdict()

                switch1_type= groups['switch1_type']
                switch2_type= groups['switch2_type']
                
            #udp packets: [0:84014582]
            #tcp packets: [0:34213312]
            m15= p15.match(line)
            if m15:
                #{'packet_type':'udp','packets_switch1':0,'packets_switch2':84014582}
                groups=m15.groupdict()
                
                class_map_action_dict.setdefault('packet_type',{}).setdefault(groups['packet_type'],{}).update({
                    'switch1_type': switch1_type,
                    'switch2_type': switch2_type,
                    'packets_in_switch1': int(groups['packets_switch1']),
                    'packets_in_switch2': int(groups['packets_switch2'])
                })
                
        return parsed_dict

class ShowPolicyMapTypeInspectZonePairSessionsSchema(MetaParser):
    ''' Schema for show policy-map type inspect zone-pair {zone_pair_name} sessions
                   show policy-map type inspect zone-pair sessions'''
    schema = {
        "zone_pair":{
            Any():{
                "service_policy_inspect":{
                    Any():{
                        "class_map":{
                            Any():{
                                "class_map_type": str,
                                "class_map_match": ListOf(str),
                                "class_map_action": str,
                                Optional("established_sessions"): {
                                    Any():{
                                        "initiator_ip": str,
                                        "initiator_port": str,
                                        "responder_ip": str,
                                        "responder_port": str,
                                        "protocol": str,
                                        "state": str,
                                        "created": str,
                                        "last_heard": str,
                                        "bytes_sent": {
                                            "initiator": str,
                                            "responder": int
                                        }
                                    },
                                },
                                Optional("half_open_sessions"): {
                                    Any():{
                                        "initiator_ip": str,
                                        "initiator_port": str,
                                        "responder_ip": str,
                                        "responder_port": str,
                                        "protocol": str,
                                        "state": str,
                                        "created": str,
                                        "last_heard": str,
                                        "bytes_sent": {
                                            "initiator": str,
                                            "responder": int
                                        }
                                    },
                                },
                                Optional("terminating_sessions"): {
                                    Any():{
                                        "initiator_ip": str,
                                        "initiator_port": str,
                                        "responder_ip": str,
                                        "responder_port": str,
                                        "protocol": str,
                                        "state": str,
                                        "created": str,
                                        "last_heard": str,
                                        "bytes_sent": {
                                            "initiator": str,
                                            "responder": int
                                        }
                                    },
                                },
                                Optional("packets"): int,
                                Optional("bytes"): int
                            },
                        }
                    },
                }
            },
        }
    }

class ShowPolicyMapTypeInspectZonePairSessions(ShowPolicyMapTypeInspectZonePairSessionsSchema):
    """Parser for show policy-map type inspect zone-pair {zone_pair_name} sessions
                    show policy-map type inspect zone-pair sessions"""

    cli_command = ["show policy-map type inspect zone-pair {zone_pair_name} sessions",
                   "show policy-map type inspect zone-pair sessions"]

    def cli(self, zone_pair_name='', output=None):
        if output is None:
            # Execute the command if output is not provided
            if zone_pair_name:
                out = self.device.execute(self.cli_command[0].format(zone_pair_name=zone_pair_name))
            else:
                out = self.device.execute(self.cli_command[1])
        else:
            out = output

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regex patterns
        #Zone-pair: GREEN->DEFAULT
        p1 = re.compile(r'^Zone-pair: +(?P<zone_pair_name>\S+)$')
        #Service-policy inspect : TEST
        p2 = re.compile(r'^Service-policy inspect : +(?P<service_policy_name>\S+)$')
        # Class-map: TEST (match-any)
        p3 = re.compile(r'^Class-map: +(?P<class_map_name>\S+) +\((?P<class_map_type>\S+)\)$')
        # Match: access-group name HBN2
        p4 = re.compile(r'^Match: +(?P<class_map_match>.+)$')
        #Inspect
        #Drop
        #Pass
        p5 = re.compile(r'^(?P<class_map_action>Inspect|Drop|Pass)(?: +\(default action\))?$')
        #0 packets, 0 bytes
        p6 = re.compile(r'^(?P<packets>\d+) packets, +(?P<bytes>\d+) bytes$')
        # Session ID 0x00000000 (10.1.1.1:10001)=>(20.1.1.1:20001) udp SIS_OPEN
        p7 = re.compile(
            r'^Session ID (?P<session_id>\S+) +\((?P<initiator_ip>[\d\.]+):(?P<initiator_port>[\d\*]+)\)=\>'
            r'\((?P<responder_ip>[\d\.]+):(?P<responder_port>[\d\*]+)\) +(?P<protocol>\w+) +(?P<state>\S+)$'
        )
        #Created 00:00:22, Last heard 00:00:13
        p8 = re.compile(r'^Created +(?P<created>[\d\:]+), +Last heard +(?P<last_heard>[\d\:]+)$')
        #Bytes sent (initiator:responder) [10000:0]
        p9 = re.compile(
            r'^Bytes sent \(initiator:responder\) +\[(?P<initiator_bytes>[\d\*]+):(?P<responder_bytes>\d+)\]$'
        )
        #Established Sessions
        p10 = re.compile(r'^(?P<session_type>Established Sessions|Half-open Sessions|Terminating Sessions)$')
        # Context tracking variables
        zone_pair_dict = None
        service_policy_dict = None
        class_map_dict = None
        sessions_dict = None
        current_session_type = None

        for line in out.splitlines():
            line = line.strip()

            #Zone-pair: z1z2
            m1 = p1.match(line)
            if m1:
                groups = m1.groupdict()
                zone_pair_dict = parsed_dict.setdefault("zone_pair", {}).setdefault(groups["zone_pair_name"], {})
                continue
                
            # Service-policy inspect : pmap
            m2 = p2.match(line)
            if m2:
                groups = m2.groupdict()
                service_policy_dict = zone_pair_dict.setdefault("service_policy_inspect", {}).setdefault(
                    groups["service_policy_name"], {}
                )
                continue
                
            # Class-map: cmap (match-any)
            m3 = p3.match(line)
            if m3:
                groups = m3.groupdict()
                class_map_dict = service_policy_dict.setdefault("class_map", {}).setdefault(groups["class_map_name"], {})
                class_map_dict["class_map_type"] = groups["class_map_type"]
                continue
                
            # Match: protocol udp
            m4 = p4.match(line)
            if m4:
                groups = m4.groupdict()
                class_map_dict.setdefault("class_map_match", []).append(groups["class_map_match"])
                continue
                
            # Inspect
            # Drop
            # Pass
            m5 = p5.match(line)
            if m5:
                groups = m5.groupdict()
                class_map_dict["class_map_action"] = groups["class_map_action"]
                continue
                
            # 0 packets, 0 bytes
            m6 = p6.match(line)
            if m6:
                groups = m6.groupdict()
                class_map_dict["packets"] = int(groups["packets"])
                class_map_dict["bytes"] = int(groups["bytes"])
                continue
                
            # Session ID 0x00000000 (10.1.1.1:10001)=>(20.1.1.1:20001) udp SIS_OPEN
            m7 = p7.match(line)
            if m7:
                groups = m7.groupdict()
                session_id = groups["session_id"]
                sessions_dict = class_map_dict.setdefault(current_session_type, {}).setdefault(session_id, {})
                sessions_dict.update({
                    "initiator_ip": groups["initiator_ip"],
                    "initiator_port": groups["initiator_port"],
                    "responder_ip": groups["responder_ip"],
                    "responder_port": groups["responder_port"],
                    "protocol": groups["protocol"],
                    "state": groups["state"]
                })
                continue

            # Created 00:00:22, Last heard 00:00:13
            m8 = p8.match(line)
            if m8:
                groups = m8.groupdict()
                # Only proceed if sessions_dict is set
                if sessions_dict:
                    sessions_dict.update({
                        "created": groups["created"],
                        "last_heard": groups["last_heard"]
                    })
                continue
                
            # Bytes sent (initiator:responder) [10000:0]
            m9 = p9.match(line)
            if m9:
                groups = m9.groupdict()
                # Only proceed if sessions_dict is set
                if sessions_dict:
                    sessions_dict["bytes_sent"] = {
                        "initiator": groups["initiator_bytes"],
                        "responder": int(groups["responder_bytes"])
                    }
                continue
                
            #Established Sessions
            m10 = p10.match(line)
            if m10:
                groups = m10.groupdict()
                if groups["session_type"] == "Established Sessions":
                    current_session_type = "established_sessions"
                elif groups["session_type"] == "Half-open Sessions":
                    current_session_type = "half_open_sessions"
                elif groups["session_type"] == "Terminating Sessions":
                    current_session_type = "terminating_sessions"
                continue
        return parsed_dict

class ShowPolicyMapTypeInspectZonePairSessionSchema(MetaParser):
    ''' Schema for show policy-map type inspect zone-pair {zone_pair_name} session
                   show policy-map type inspect zone-pair session'''
    schema = {
        "zone_pair":{
            Any():{
                "service_policy_inspect":{
                    Any():{
                        "class_map":{
                            Any():{
                                "class_map_type": str,
                                "class_map_match": ListOf(str),
                                "class_map_action": str,
                                Optional("established_sessions"): {
                                    Any():{
                                        "initiator_ip": str,
                                        "initiator_port": str,
                                        "responder_ip": str,
                                        "responder_port": str,
                                        "protocol": str,
                                        "state": str,
                                        "created": str,
                                        "last_heard": str,
                                        "bytes_sent": {
                                            "initiator": str,
                                            "responder": int
                                        }
                                    },
                                },
                                Optional("half_open_sessions"): {
                                    Any():{
                                        "initiator_ip": str,
                                        "initiator_port": str,
                                        "responder_ip": str,
                                        "responder_port": str,
                                        "protocol": str,
                                        "state": str,
                                        "created": str,
                                        "last_heard": str,
                                        "bytes_sent": {
                                            "initiator": str,
                                            "responder": int
                                        }
                                    },
                                },
                                Optional("terminating_sessions"): {
                                    Any():{
                                        "initiator_ip": str,
                                        "initiator_port": str,
                                        "responder_ip": str,
                                        "responder_port": str,
                                        "protocol": str,
                                        "state": str,
                                        "created": str,
                                        "last_heard": str,
                                        "bytes_sent": {
                                            "initiator": str,
                                            "responder": int
                                        }
                                    },
                                },
                                Optional("packets"): int,
                                Optional("bytes"): int
                            },
                        }
                    },
                }
            },
        }
    }

class ShowPolicyMapTypeInspectZonePairSession(ShowPolicyMapTypeInspectZonePairSessionSchema):
    """Parser for show policy-map type inspect zone-pair {zone_pair_name} session
                  show policy-map type inspect zone-pair session"""
    
    cli_command = ["show policy-map type inspect zone-pair {zone_pair_name} session",
                   "show policy-map type inspect zone-pair session"]

    def cli(self, zone_pair_name='', output=None):
        if output is None:
            # Execute the command if output is not provided
            if zone_pair_name:
                out = self.device.execute(self.cli_command[0].format(zone_pair_name=zone_pair_name))
            else:
                out = self.device.execute(self.cli_command[1])
        else:
            out = output

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regex patterns
        #Zone-pair: GREEN->DEFAULT
        p1 = re.compile(r'^Zone-pair: +(?P<zone_pair_name>\S+)$')
        #Service-policy inspect : TEST
        p2 = re.compile(r'^Service-policy inspect : +(?P<service_policy_name>\S+)$')
        # Class-map: TEST (match-any)
        p3 = re.compile(r'^Class-map: +(?P<class_map_name>\S+) +\((?P<class_map_type>\S+)\)$')
        # Match: access-group name HBN2
        p4 = re.compile(r'^Match: +(?P<class_map_match>.+)$')
        #Inspect
        #Drop
        #Pass
        p5 = re.compile(r'^(?P<class_map_action>Inspect|Drop|Pass)(?: +\(default action\))?$')
        #0 packets, 0 bytes
        p6 = re.compile(r'^(?P<packets>\d+) packets, +(?P<bytes>\d+) bytes$')
        # Session ID 0x00000000 (10.1.1.1:10001)=>(20.1.1.1:20001) udp SIS_OPEN
        p7_a = re.compile(
            r'^Session ID (?P<session_id>\S+) +\((?P<initiator_ip>[\d\.]+):(?P<initiator_port>[\d\*]+)\)=\>'
            r'\((?P<responder_ip>[\d\.]+):(?P<responder_port>[\d\*]+)\) +(?P<protocol>\w+) +(?P<state>\S+)$'
        )
        p7_b = re.compile(
            r'^Session ID\s+(?P<session_id>\S+)\s+[\[\(](?P<initiator_ip>[^\]\)]+)[\]\)]:(?P<initiator_port>[\d\*]+)[\)\]]?:?\d*=\>[\[\(](?P<responder_ip>[^\]\)]+)[\]\)]:(?P<responder_port>[\d\*]+)[\)\]]?:?\d*\s+(?P<protocol>\w+)\s+(?P<state>\S+)$'
        )
        #Created 00:00:22, Last heard 00:00:13
        p8 = re.compile(r'^Created +(?P<created>[\d\:]+), +Last heard +(?P<last_heard>[\d\:]+)$')
        #Bytes sent (initiator:responder) [10000:0]
        p9 = re.compile(
            r'^Bytes sent \(initiator:responder\) +\[(?P<initiator_bytes>[\d\*]+):(?P<responder_bytes>\d+)\]$'
        )
        #Established Sessions
        p10 = re.compile(r'^(?P<session_type>Established Sessions|Half-open Sessions|Terminating Sessions)$')


        # Context tracking variables
        zone_pair_dict = None
        service_policy_dict = None
        class_map_dict = None
        sessions_dict = None

        for line in out.splitlines():
            line = line.strip()

            #Zone-pair: z1z2
            m1 = p1.match(line)
            if m1:
                groups = m1.groupdict()
                zone_pair_dict = parsed_dict.setdefault("zone_pair", {}).setdefault(groups["zone_pair_name"], {})
                continue
                
            # Service-policy inspect : pmap
            m2 = p2.match(line)
            if m2:
                groups = m2.groupdict()
                service_policy_dict = zone_pair_dict.setdefault("service_policy_inspect", {}).setdefault(
                    groups["service_policy_name"], {}
                )
                continue
                
            # Class-map: cmap (match-any)
            m3 = p3.match(line)
            if m3:
                groups = m3.groupdict()
                class_map_dict = service_policy_dict.setdefault("class_map", {}).setdefault(groups["class_map_name"], {})
                class_map_dict["class_map_type"] = groups["class_map_type"]
                continue
                
            # Match: protocol udp
            m4 = p4.match(line)
            if m4:
                groups = m4.groupdict()
                class_map_dict.setdefault("class_map_match", []).append(groups["class_map_match"])
                continue
                
            # Inspect
            # Drop
            # Pass
            m5 = p5.match(line)
            if m5:
                groups = m5.groupdict()
                class_map_dict["class_map_action"] = groups["class_map_action"]
                continue
                
            # 0 packets, 0 bytes
            m6 = p6.match(line)
            if m6:
                groups = m6.groupdict()
                class_map_dict["packets"] = int(groups["packets"])
                class_map_dict["bytes"] = int(groups["bytes"])
                continue
                
            # Session ID 0x00000000 (10.1.1.1:10001)=>(20.1.1.1:20001) udp SIS_OPEN
            m7 = p7_a.match(line)
            if not m7:
                m7 = p7_b.match(line)
            if m7:
                groups = m7.groupdict()
                session_id = groups["session_id"]
                sessions_dict = class_map_dict.setdefault(current_session_type, {}).setdefault(session_id, {})
                sessions_dict.update({
                    "initiator_ip": groups["initiator_ip"],
                    "initiator_port": groups["initiator_port"],
                    "responder_ip": groups["responder_ip"],
                    "responder_port": groups["responder_port"],
                    "protocol": groups["protocol"],
                    "state": groups["state"]
                })
                continue
                
            # Created 00:00:22, Last heard 00:00:13
            m8 = p8.match(line)
            if m8:
                groups = m8.groupdict()
                sessions_dict.update({
                    "created": groups["created"],
                    "last_heard": groups["last_heard"]
                })
                continue
                
            # Bytes sent (initiator:responder) [10000:0]
            m9 = p9.match(line)
            if m9:
                groups = m9.groupdict()
                sessions_dict["bytes_sent"] = {
                    "initiator": groups["initiator_bytes"],
                    "responder": int(groups["responder_bytes"])
                }
                continue

            #Established Sessions
            m10 = p10.match(line)
            if m10:
                groups = m10.groupdict()
                if groups["session_type"] == "Established Sessions":
                    current_session_type = "established_sessions"
                elif groups["session_type"] == "Half-open Sessions":
                    current_session_type = "half_open_sessions"
                elif groups["session_type"] == "Terminating Sessions":
                    current_session_type = "terminating_sessions"
                continue
        return parsed_dict

class ShowPolicyFirewallConfigZonePairInOutSchema(MetaParser):
    
    schema = {
        'zone_pair': {
            Any(): {
                'source_zone': str,
                'source_interfaces': ListOf(str),
                'destination_zone': str,
                'destination_interfaces': ListOf(str),
                'service_policy': {
                    'name': str,
                    'class_map': {
                        Any(): {
                            'match_type': str,
                            'match_criteria': ListOf(str),
                            'action': str,
                            Optional('parameter_map'): str
                        }
                    }
                }
            }
        }
    }
class ShowPolicyFirewallConfigZonePairInOut(ShowPolicyFirewallConfigZonePairInOutSchema):
    """ Parser for:
        show policy-firewall config zone-pair in-out
    """

    cli_command = "show policy-firewall config zone-pair in-out"

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # Zone-pair              : in-out
        p1 = re.compile(r'^Zone-pair\s+:\s+(?P<zone_pair>\S+)$')

        # Source Zone            : inside
        p2 = re.compile(r'^Source Zone\s+:\s+(?P<source_zone>\S+)$')

        # Destination Zone       : outside
        p3 = re.compile(r'^Destination Zone\s+:\s+(?P<destination_zone>\S+)$')

        # Service-policy inspect : pmap
        p4 = re.compile(r'^Service-policy inspect\s+:\s+(?P<service_policy>\S+)$')

        # Class-map : nested_cmap (match-any)
        p5 = re.compile(r'^Class-map\s+:\s+(?P<class_name>\S+)\s+\((?P<match_type>match-(?:any|all))\)$')

        # Match protocol tcp
        p6 = re.compile(r'^Match\s+(?P<match_criteria>.+)$')

        # Action : inspect
        p7 = re.compile(r'^Action\s+:\s+(?P<action>[\w\s]+)$')

        # Parameter-map : param
        p8 = re.compile(r'^Parameter-map\s+:\s+(?P<parameter_map>\S+)$')

        # GigabitEthernet1/0/1
        p9 = re.compile(r'^(?P<interface>GigabitEthernet[\d/]+)$')

        result = {}
        zone_pair_name = None
        current_class = None
        current_interfaces = None

        for line in output.splitlines():
            line = line.strip()

            # Zone-pair              : in-out
            m = p1.match(line)
            if m:
                zone_pair_name = m.group('zone_pair')
                result.setdefault('zone_pair', {})[zone_pair_name] = {}
                continue

            #Source Zone            : inside
            m = p2.match(line)
            if m:
                result['zone_pair'][zone_pair_name]['source_zone'] = m.group('source_zone')
                current_interfaces = 'source_interfaces'
                result['zone_pair'][zone_pair_name][current_interfaces] = []
                continue

            # Destination Zone       : outside
            m = p3.match(line)
            if m:
                result['zone_pair'][zone_pair_name]['destination_zone'] = m.group('destination_zone')
                current_interfaces = 'destination_interfaces'
                result['zone_pair'][zone_pair_name][current_interfaces] = []
                continue

            # Service-policy inspect : pmap
            m = p4.match(line)
            if m:
                result['zone_pair'][zone_pair_name].setdefault('service_policy', {})
                result['zone_pair'][zone_pair_name]['service_policy']['name'] = m.group('service_policy')
                result['zone_pair'][zone_pair_name]['service_policy']['class_map'] = {}
                continue

            # Class-map : nested_cmap (match-any)
            m = p5.match(line)
            if m:
                class_name = m.group('class_name')
                match_type = m.group('match_type')
                current_class = class_name
                result['zone_pair'][zone_pair_name]['service_policy']['class_map'][class_name] = {
                    'match_type': match_type,
                    'match_criteria': []
                }
                continue

            # Match protocol tcp
            m = p6.match(line)
            if m and current_class:
                match_text = m.group('match_criteria')
                result['zone_pair'][zone_pair_name]['service_policy']['class_map'][current_class]['match_criteria'].append(
                    f'match {match_text}'
                )
                continue

            # Action : inspect
            m = p7.match(line)
            if m and current_class:
                result['zone_pair'][zone_pair_name]['service_policy']['class_map'][current_class]['action'] = m.group('action')
                continue

            # Parameter-map : param
            m = p8.match(line)
            if m and current_class:
                result['zone_pair'][zone_pair_name]['service_policy']['class_map'][current_class]['parameter_map'] = m.group('parameter_map')
                continue
            
            # GigabitEthernet1/0/1
            m = p9.match(line)
            if m and current_interfaces:
                result['zone_pair'][zone_pair_name][current_interfaces].append(m.group('interface'))
                continue

        return result
    
class ShowPolicyFirewallConfigSchema(MetaParser):
    schema = {
        'zone_pair': {
            Any(): {
                'source_zone': str,
                'source_interfaces': ListOf(str),
                'destination_zone': str,
                'destination_interfaces': ListOf(str),
                'service_policy': {
                    'name': str,
                    'class_map': {
                        Any(): {
                            'match_type': str,
                            'match_criteria': ListOf(str),
                            'action': str,
                            Optional('parameter_map'): str
                        }
                    }
                }
            }
        },
        'parameter_map_configuration': {
                'parameter_map_type_inspect': str,
                Optional('alert_messages'): str,
                Optional('all_application_inspection'): str,
                Optional('audit_trailing'): str,
                Optional('logging_dropped_packets'): str,
                Optional('logging_flow'): str,
                Optional('utd_context_id'): int,
                Optional('icmp_session_idle_time'): {
                    'idle': str,
                    'ageout': str
                },
                Optional('dns_session_idle_time'): str,
                Optional('tcp_session_half_open'): {
                    'half_open': str,
                    'half_close': str,
                    'idle': str
                },
                Optional('tcp_session_idle_time'): {
                    'idle': str,
                    'ageout': str
                },
                Optional('tcp_session_fin_wait_time'): {
                    'wait': str,
                    'ageout': str
                },
                Optional('tcp_session_syn_wait_time'): {
                    'wait': str,
                    'ageout': str
                },
                Optional('tcp_loose_window_scaling_enforcement'): str,
                Optional('tcp_max_half_open_connections'): {
                    'value': str,
                    'block_time': str
                },
                Optional('udp_half_open_session_idle_time'): {
                    'idle': str,
                    'ageout': str
                },
                Optional('udp_session_idle_time'): {
                    'idle': str,
                    'ageout': str
                },
                Optional('sessions_connections_threshold_low'): str,
                Optional('sessions_connection_threshold_high'):str,
                Optional('sessions_connection_rate_threshold_low'): str,
                Optional('sessions_connection_rate_threshold_high'): str,
                Optional('sessions_max_incomplete_threshold_low'): str,
                Optional('sessions_max_incomplete_threshold_high'): str,
                Optional('sessions_max_inspect_sessions'): str,
                Optional('total_packets_per_flow'): str,
                Optional('zone_mismatch_drop_option'): str
            }
        
    }

class ShowPolicyFirewallConfig(ShowPolicyFirewallConfigSchema):
    """ Parser for:
        show policy-firewall config
    """

    cli_command = "show policy-firewall config"

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
            
         # Zone-pair              : in-out
        p1 = re.compile(r'^Zone-pair\s+:\s+(?P<zone_pair>\S+)$')

        # Source Zone            : inside
        p2 = re.compile(r'^Source Zone\s+:\s+(?P<source_zone>\S+)$')

        # Destination Zone       : outside
        p3 = re.compile(r'^Destination Zone\s+:\s+(?P<destination_zone>\S+)$')

        # Service-policy inspect : pmap
        p4 = re.compile(r'^Service-policy inspect\s+:\s+(?P<service_policy>\S+)$')

        # Class-map : nested_cmap (match-any)
        p5 = re.compile(r'^Class-map\s+:\s+(?P<class_name>\S+)\s+\((?P<match_type>match-(?:any|all))\)$')

        # Match class-map cmap
        p5 = re.compile(r'^Class-map\s+:\s+(?P<class_name>\S+)\s+\((?P<match_type>match-(?:any|all))\)$')

        # Match protocol tcp
        p6 = re.compile(r'^Match\s+(?P<match_criteria>.+)$')

        # Action : inspect
        p7 = re.compile(r'^Action\s+:\s+(?P<action>[\w\s]+)$')

        # Parameter-map : param
        p8 = re.compile(r'^Parameter-map\s+:\s+(?P<parameter_map>\S+)$')

        # GigabitEthernet1/0/1
        p9 = re.compile(r'^(?P<interface>GigabitEthernet[\d/]+)$')

        # Parameter-map type inspect: param
        p10 = re.compile(r'^Parameter-map type inspect:\s+(?P<parameter_map_type_inspect>\S+)$')

        # alert messages                 : on
        p11 = re.compile(r'^alert messages\s+:\s+(?P<alert_messages>\w+)$')

        # all application inspection     : on
        p12 = re.compile(r'^all application inspection\s+:\s+(?P<all_application_inspection>\w+)$')

        # audit trailing                 : off
        p13 = re.compile(r'^audit trailing\s+:\s+(?P<audit_trailing>\w+)$')

        # logging dropped-packets        : off
        p14 = re.compile(r'^logging dropped-packets\s+:\s+(?P<logging_dropped_packets>\w+)$')

        # logging flow        : off
        p15 = re.compile(r'^logging flow\s+:\s+(?P<logging_flow>\w+)$')

        # UTD Context ID      : 0
        p16 = re.compile(r'^UTD Context ID\s+:\s+(?P<utd_context_id>\d+)$')

        # icmp session idle-time         : 60 sec, ageout-time: 60 sec
        p17= re.compile(r'^icmp session idle-time\s+:\s+(?P<idle>[\w\s]+),\s+ageout-time:\s+(?P<ageout>[\w\s]+)$')

        # dns session idle-time          : 5 sec
        p18 = re.compile(r'^dns session idle-time\s+:\s+(?P<dns_idle_time>[\w\s]+)$')

        # tcp session half-open          : on, half-close: on, idle: on
        p19= re.compile(r'^tcp session half-open\s+:\s+(?P<half_open>\w+),\s+half-close:\s+(?P<half_close>\w+),\s+idle:\s+(?P<idle>\w+)$')

        # tcp session idle-time          : 80 sec, ageout-time: 80 sec
        p20 = re.compile(r'^tcp session idle-time\s+:\s+(?P<idle>[\w\s]+),\s+ageout-time:\s+(?P<ageout>[\w\s]+)$')

        # tcp session FIN wait-time      : 1 sec, FIN ageout-time: 1 sec
        p21 = re.compile(r'^tcp session FIN wait-time\s+:\s+(?P<wait>[\w\s]+),\s+FIN ageout-time:\s+(?P<ageout>[\w\s]+)$')

        # tcp session SYN wait-time      : 30 sec, SYN ageout-time: 30 sec
        p22 = re.compile(r'^tcp session SYN wait-time\s+:\s+(?P<wait>[\w\s]+),\s+SYN ageout-time:\s+(?P<ageout>[\w\s]+)$')

        # tcp loose window scaling enforcement: off
        p23 = re.compile(r'^tcp loose window scaling enforcement:\s+(?P<tcp_window_enforce>\w+)$')

        # tcp max-half-open connections/host  : unlimited block-time: 0 min
        p24 = re.compile(r'^tcp max-half-open connections/host\s+:\s+(?P<value>\w+)\s+block-time:\s+(?P<block_time>[\w\s]+)$')

        # udp half-open session idle-time: 30000 ms, ageout-time: 30000 ms
        p25 = re.compile(r'^udp half-open session idle-time:\s+(?P<idle>[\w\s]+),\s+ageout-time:\s+(?P<ageout>[\w\s]+)$')

        # udp session idle-time          : 60 sec, ageout-time: 60 sec
        p26 = re.compile(r'^udp session idle-time\s+:\s+(?P<idle>[\w\s]+),\s+ageout-time:\s+(?P<ageout>[\w\s]+)$')

        # sessions, connections/min threshold (low) : unlimited
        p27 = re.compile(r'^sessions, connections/min threshold \(low\)\s+:\s+(?P<low>\w+)$')

        # sessions, connections/min threshold (high): unlimited
        p28 = re.compile(r'^sessions, connections/min threshold \(high\)\s*:\s+(?P<high>\w+)$')

        # sessions, connection rate threshold (low) : unlimited
        p29 = re.compile(r'^sessions, connection rate threshold \(low\)\s+:\s+(?P<low>\w+)$')

        # sessions, connection rate threshold (high): unlimited
        p30 = re.compile(r'^sessions, connection rate threshold \(high\)\s*:\s+(?P<high>\w+)$')

        # sessions, max-incomplete threshold (low)  : unlimited
        p31 = re.compile(r'^sessions, max-incomplete threshold \(low\)\s+:\s+(?P<low>\w+)$')

        # sessions, max-incomplete threshold (high) : unlimited
        p32 = re.compile(r'^sessions, max-incomplete threshold \(high\)\s+:\s+(?P<high>\w+)$')

        # sessions, maximum no. of inspect sessions : unlimited
        p33 = re.compile(r'^sessions, maximum no\. of inspect sessions\s+:\s+(?P<max_sessions>\w+)$')

        # total number of packets per flow          : default
        p34 = re.compile(r'^total number of packets per flow\s+:\s+(?P<total_packets>\w+)$')

        # zone mismatch drop option      : off
        p35 = re.compile(r'^zone mismatch drop option\s+:\s+(?P<zone_mismatch_drop>\w+)$')

        result = {}
        zone_pair_name = None
        current_class = None
        current_interfaces = None
        
        for line in output.splitlines():
            line = line.strip()

            # Zone-pair              : in-out
            m = p1.match(line)
            if m:
                zone_pair_name = m.group('zone_pair')
                result.setdefault('zone_pair', {})[zone_pair_name] = {}
                continue

            # Source Zone            : inside
            m = p2.match(line)
            if m:
                result['zone_pair'][zone_pair_name]['source_zone'] = m.group('source_zone')
                current_interfaces = 'source_interfaces'
                result['zone_pair'][zone_pair_name][current_interfaces] = []
                continue

            #  Destination Zone       : outside
            m = p3.match(line)
            if m:
                result['zone_pair'][zone_pair_name]['destination_zone'] = m.group('destination_zone')
                current_interfaces = 'destination_interfaces'
                result['zone_pair'][zone_pair_name][current_interfaces] = []
                continue

            # Service-policy inspect : pmap
            m = p4.match(line)
            if m:
                result['zone_pair'][zone_pair_name].setdefault('service_policy', {})
                result['zone_pair'][zone_pair_name]['service_policy']['name'] = m.group('service_policy')
                result['zone_pair'][zone_pair_name]['service_policy']['class_map'] = {}
                continue

            # Class-map : nested_cmap (match-any)
            m = p5.match(line)
            if m:
                class_name = m.group('class_name')
                match_type = m.group('match_type')
                current_class = class_name
                result['zone_pair'][zone_pair_name]['service_policy']['class_map'][class_name] = {
                    'match_type': match_type,
                    'match_criteria': []
                }
                continue

            # Match protocol tcp
            m = p6.match(line)
            if m and current_class:
                match_text = m.group('match_criteria')
                result['zone_pair'][zone_pair_name]['service_policy']['class_map'][current_class]['match_criteria'].append(
                    f'match {match_text}'
                )
                continue

            # Action : inspect
            m = p7.match(line)
            if m and current_class:
                result['zone_pair'][zone_pair_name]['service_policy']['class_map'][current_class]['action'] = m.group('action')
                continue

            # Parameter-map : param
            m = p8.match(line)
            if m and current_class:
                result['zone_pair'][zone_pair_name]['service_policy']['class_map'][current_class]['parameter_map'] = m.group('parameter_map')
                continue

            # GigabitEthernet1/0/1
            m = p9.match(line)
            if m and current_interfaces:
                result['zone_pair'][zone_pair_name][current_interfaces].append(m.group('interface'))
                continue
            
            # Parameter-map type inspect: param
            m = p10.match(line)
            if m:
                parameter_map = result.setdefault('parameter_map_configuration', {})
                parameter_map['parameter_map_type_inspect'] = m.group('parameter_map_type_inspect')
                continue
             
            # alert messages                 : on         
            m = p11.match(line)
            if m:
                result['parameter_map_configuration']['alert_messages'] = m.group('alert_messages')
                continue

            # all application inspection     : on
            m = p12.match(line)
            if m:
                result['parameter_map_configuration']['all_application_inspection'] = m.group('all_application_inspection')
                continue

            # audit trailing                 : off
            m = p13.match(line)
            if m:
                result['parameter_map_configuration']['audit_trailing'] = m.group('audit_trailing')
                continue

            # logging dropped-packets        : off
            m = p14.match(line)
            if m:
                result['parameter_map_configuration']['logging_dropped_packets'] = m.group('logging_dropped_packets')
                continue

            # logging flow        : off
            m = p15.match(line)
            if m:
                result['parameter_map_configuration']['logging_flow'] = m.group('logging_flow')
                continue

            #UTD Context ID      : 0
            m = p16.match(line)
            if m:
                result['parameter_map_configuration']['utd_context_id'] = int(m.group('utd_context_id'))
                continue

            # icmp session idle-time         : 60 sec, ageout-time: 60 sec
            m = p17.match(line)
            if m:
                icmp_session = result['parameter_map_configuration'].setdefault('icmp_session_idle_time', {})
                icmp_session['idle'] = m.group('idle')
                icmp_session['ageout'] = m.group('ageout')
                continue

            # dns session idle-time          : 5 sec
            m = p18.match(line)
            if m:
                result['parameter_map_configuration']['dns_session_idle_time'] = m.group('dns_idle_time')
                continue

            # tcp session half-open          : on, half-close: on, idle: on
            m = p19.match(line)
            if m:
                tcp_session = result['parameter_map_configuration'].setdefault('tcp_session_half_open', {})
                tcp_session['half_open'] = m.group('half_open')
                tcp_session['half_close'] = m.group('half_close')
                tcp_session['idle'] = m.group('idle')
                continue

            # tcp session idle-time          : 80 sec, ageout-time: 80 sec
            m = p20.match(line)
            if m:
                tcp_session_idle = result['parameter_map_configuration'].setdefault('tcp_session_idle_time', {})
                tcp_session_idle['idle'] = m.group('idle')
                tcp_session_idle['ageout'] = m.group('ageout')
                continue
               
            #  tcp session FIN wait-time      : 1 sec, FIN ageout-time: 1 sec
            m = p21.match(line)
            if m:
                tcp_session_fin_wait = result['parameter_map_configuration'].setdefault('tcp_session_fin_wait_time', {})
                tcp_session_fin_wait['wait'] = m.group('wait')
                tcp_session_fin_wait['ageout'] = m.group('ageout')
                continue
               
            # tcp session SYN wait-time      : 30 sec, SYN ageout-time: 30 sec
            m = p22.match(line)
            if m:
                tcp_session_syn_wait = result['parameter_map_configuration'].setdefault('tcp_session_syn_wait_time', {})
                tcp_session_syn_wait['wait'] = m.group('wait')
                tcp_session_syn_wait['ageout'] = m.group('ageout')
                continue
         
            #tcp loose window scaling enforcement: off
            m = p23.match(line)
            if m:
                result['parameter_map_configuration']['tcp_loose_window_scaling_enforcement'] = m.group('tcp_window_enforce')
                continue

            # tcp max-half-open connections/host  : unlimited block-time: 0 min
            m = p24.match(line)
            if m:
                tcp_max_half_open = result['parameter_map_configuration'].setdefault('tcp_max_half_open_connections', {})
                tcp_max_half_open['value'] = m.group('value')
                tcp_max_half_open['block_time'] = m.group('block_time')
                continue

            #udp half-open session idle-time: 30000 ms, ageout-time: 30000 ms
            m = p25.match(line)
            if m:
                udp_half_open =  result['parameter_map_configuration'].setdefault('udp_half_open_session_idle_time', {})
                udp_half_open['idle'] = m.group('idle')
                udp_half_open['ageout'] = m.group('ageout')
                continue

            #udp session idle-time          : 60 sec, ageout-time: 60 sec
            m = p26.match(line)
            if m:
                udp_session_idle = result['parameter_map_configuration'].setdefault('udp_session_idle_time', {})
                udp_session_idle['idle'] = m.group('idle')
                udp_session_idle['ageout'] = m.group('ageout')
                continue

            #sessions, connections/min threshold (low) : unlimited
            m = p27.match(line)
            if m:
                result['parameter_map_configuration']['sessions_connections_threshold_low'] = m.group('low')
                continue

            #sessions, connections/min threshold (high): unlimited
            m = p28.match(line)
            if m:
                result['parameter_map_configuration']['sessions_connection_threshold_high'] = m.group('high')
                continue

            #sessions, connection rate threshold (low) : unlimited
            m = p29.match(line)
            if m:
                result['parameter_map_configuration']['sessions_connection_rate_threshold_low'] = m.group('low')
                continue

            #sessions, connection rate threshold (high): unlimited
            m = p30.match(line)
            if m:
                result['parameter_map_configuration']['sessions_connection_rate_threshold_high'] = m.group('high')
                continue

            #sessions, max-incomplete threshold (low)  : unlimited
            m = p31.match(line)
            if m:
                result['parameter_map_configuration']['sessions_max_incomplete_threshold_low'] = m.group('low')
                continue

            #sessions, max-incomplete threshold (high) : unlimited
            m = p32.match(line)
            if m:
                result['parameter_map_configuration']['sessions_max_incomplete_threshold_high'] = m.group('high')
                continue

            #sessions, maximum no. of inspect sessions : unlimited
            m = p33.match(line)
            if m:
                result['parameter_map_configuration']['sessions_max_inspect_sessions'] = m.group('max_sessions')
                continue

            #total number of packets per flow          : default
            m = p34.match(line)
            if m:
                result['parameter_map_configuration']['total_packets_per_flow'] = m.group('total_packets')
                continue

            #zone mismatch drop option      : off
            m = p35.match(line)
            if m:
                result['parameter_map_configuration']['zone_mismatch_drop_option'] = m.group('zone_mismatch_drop')
                continue
        
        return result
