# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

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
    
    cli_command = ["show policy-map type inspect zone-pair","show policy-map type inspect zone-pair {zone_pair_name}"]

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


        for line in out.splitlines():

            #Zone-pair: GREEN->DEFAULT
            m1= p1.match(line)
            if m1:
                #{'zone_pair_name':'GREEN->DEFAULT'}
                groups=m1.groupdict()
                zone_pair_dict= parsed_dict.setdefault('zone_pair', {}).setdefault(groups['zone_pair_name'], {})

            #Service-policy inspect : TEST
            m2= p2.match(line)
            if m2:
                #{'service_policy_inspect':'TEST'}
                groups = m2.groupdict()
                service_policy_dict = zone_pair_dict.\
                    setdefault('service_policy_inspect', {}).\
                    setdefault(groups['service_policy_inspect'], {})
            
            # Class-map: TEST (match-any)
            m3= p3.match(line)
            if m3:
                #{'class_map_name':'TEST','class_map_type':'match-any'}
                groups=m3.groupdict()

                class_map_dict = service_policy_dict.\
                    setdefault('class_map', {}).\
                    setdefault(groups['class_map_name'], {})

                class_map_dict.update({'class_map_type': groups['class_map_type']})

            # Match: access-group name HBN2
            m4= p4.match(line)
            if m4:
                #{'class_map_match':'access-group name HBN2'}
                groups=m4.groupdict()
                class_map_match_list = class_map_dict.setdefault('class_map_match', [])
                class_map_match_list.append(groups['class_map_match'])

            #Inspect #Pass #Drop
            m5= p5.match(line)
            if m5:
                #{'class_map_action':'Inspect'}
                groups=m5.groupdict()
                class_map_action_dict = class_map_dict.\
                    setdefault('class_map_action', {}).\
                    setdefault(groups['class_map_action'], {})

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
            #0 packets, 0 bytes
            m13= p13.match(line)
            if m13:
                #{'packets_total':0,'bytes_total':0}
                groups=m13.groupdict()
                class_map_action_dict.update({
                    'total_packets': int(groups['packets_total']),
                    'total_bytes': int(groups['bytes_total'])
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

