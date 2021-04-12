'''
* 'show sdwan zonebfwdp sessions'
* 'show sdwan zbfw zonepair-statistics'
'''
# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use

class ShowSdwanZonebfwdpSessionsSchema(MetaParser):
    schema = {
        'session_db': {
            Any(): {
                'session_id': int,
                'state': str,
                'src_ip': str,
                'dst_ip': str,
                'src_port': int,
                'dst_port': int,
                'protocol': str,
                'src_vrf': int,
                'dst_vrf': int,
                'src_vpn_id': int,
                'dst_vpn_id': int,
                'zp_name': str,
                'classmap_name': str,
                'nat_flags': str,
                'internal_flags': int,
                'total_initiator_bytes': int,
                'total_responder_bytes': int,
                Optional('application_type'): str
                }
         }
    }

class ShowSdwanZonebfwdpSessions(ShowSdwanZonebfwdpSessionsSchema):
    """Parser for show sdwan zonebfwdp sessions
    parser class - implements detail parsing mechanisms for cli output.
    """

    cli_command = 'show sdwan zonebfwdp sessions'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        #18005202  open    10.76.0.7  172.16.186.50    49873  443   PROTO_L7_HTTPS  2    2    1    0    ZP_lanZone_wanZone_I_-1639760094  Isn4451ZbfPolicy-seq-1-cm_  -      0         3684       67394                   
        p1 = re.compile(r'^(?P<sess_id>\d+)\s+(?P<state>\w+)\s+(?P<src_ip>\S+)\s+(?P<dst_ip>\S+)\s+(?P<src_port>\d+)\s+(?P<dst_port>\d+)\s+(?P<proto>\S+)\s+(?P<src_vrf>\d+)\s+(?P<dst_vrf>\d+)\s+(?P<src_vpn_id>\d+)\s+(?P<dst_vpn_id>\d+)\s+(?P<zp_name>\S+)\s+(?P<classmap_name>\S+)\s+(?P<nat_flags>\S+)\s+(?P<internal_flags>\d+)\s+(?P<tot_init_bytes>\d+)\s+(?P<tot_resp_bytes>\d+)$')

        #4583 open 10.225.18.63 10.196.18.63 1024 1024 PROTO_L4_UDP 3 3 20 20 ZP_LAN_ZONE_vpn20_LAN__968352866 ZBFW-seq-1-cm_ - 0 2435061651 2435062756 /statistical-p2p
        p2 = re.compile(r'^(?P<sess_id>\d+)\s+(?P<state>\w+)\s+(?P<src_ip>\S+)\s+(?P<dst_ip>\S+)\s+(?P<src_port>\d+)\s+(?P<dst_port>\d+)\s+(?P<proto>\S+)\s+(?P<src_vrf>\d+)\s+(?P<dst_vrf>\d+)\s+(?P<src_vpn_id>\d+)\s+(?P<dst_vpn_id>\d+)\s+(?P<zp_name>\S+)\s+(?P<classmap_name>\S+)\s+(?P<nat_flags>\S+)\s+(?P<internal_flags>\d+)\s+(?P<tot_init_bytes>\d+)\s+(?P<tot_resp_bytes>\d+)\s+(?P<app_type>\S+)$')


        ret_dict = {}
        sess_num = 0
        for line in out.splitlines():
            line = line.strip()
            
            ##18005202  open    10.76.0.7  172.16.186.50    49873  443   PROTO_L7_HTTPS  2    2    1    0    ZP_lanZone_wanZone_I_-1639760094  Isn4451ZbfPolicy-seq-1-cm_  -      0         3684       67394                   

            m = p1.match(line)      
            if m:
                groups = m.groupdict()
                sess_dict = ret_dict.setdefault('session_db', {})
                feature_dict = sess_dict.setdefault(sess_num, {})
                feature_dict.update(({'session_id': int(groups['sess_id'])}))
                feature_dict.update(({'state': (groups['state'])}))
                feature_dict.update(({'src_ip': (groups['src_ip'])}))
                feature_dict.update(({'dst_ip': (groups['dst_ip'])}))
                feature_dict.update(({'src_port': int(groups['src_port'])}))
                feature_dict.update(({'dst_port': int(groups['dst_port'])}))
                feature_dict.update(({'protocol': (groups['proto'])}))
                feature_dict.update(({'src_vrf': int(groups['src_vrf'])}))
                feature_dict.update(({'dst_vrf': int(groups['dst_vrf'])}))
                feature_dict.update(({'src_vpn_id': int(groups['src_vpn_id'])}))
                feature_dict.update(({'dst_vpn_id': int(groups['dst_vpn_id'])}))
                feature_dict.update(({'zp_name': (groups['zp_name'])}))
                feature_dict.update(({'classmap_name': (groups['classmap_name'])}))
                feature_dict.update(({'nat_flags': (groups['nat_flags'])}))
                feature_dict.update(({'internal_flags': int(groups['internal_flags'])}))
                feature_dict.update(({'total_initiator_bytes': int(groups['tot_init_bytes'])}))
                feature_dict.update(({'total_responder_bytes': int(groups['tot_resp_bytes'])}))
                sess_num = sess_num + 1 
                last_dict_ptr = feature_dict
                continue

            #4583 open 10.225.18.63 10.196.18.63 1024 1024 PROTO_L4_UDP 3 3 20 20 ZP_LAN_ZONE_vpn20_LAN__968352866 ZBFW-seq-1-cm_ - 0 2435061651 2435062756 /statistical-p2p
            m = p2.match(line)      
            if m:
                groups = m.groupdict()
                sess_dict = ret_dict.setdefault('session_db', {})
                feature_dict = sess_dict.setdefault(sess_num, {})
                feature_dict.update(({'session_id': int(groups['sess_id'])}))
                feature_dict.update(({'state': (groups['state'])}))
                feature_dict.update(({'src_ip': (groups['src_ip'])}))
                feature_dict.update(({'dst_ip': (groups['dst_ip'])}))
                feature_dict.update(({'src_port': int(groups['src_port'])}))
                feature_dict.update(({'dst_port': int(groups['dst_port'])}))
                feature_dict.update(({'protocol': (groups['proto'])}))
                feature_dict.update(({'src_vrf': int(groups['src_vrf'])}))
                feature_dict.update(({'dst_vrf': int(groups['dst_vrf'])}))
                feature_dict.update(({'src_vpn_id': int(groups['src_vpn_id'])}))
                feature_dict.update(({'dst_vpn_id': int(groups['dst_vpn_id'])}))
                feature_dict.update(({'zp_name': (groups['zp_name'])}))
                feature_dict.update(({'classmap_name': (groups['classmap_name'])}))
                feature_dict.update(({'nat_flags': (groups['nat_flags'])}))
                feature_dict.update(({'internal_flags': int(groups['internal_flags'])}))
                feature_dict.update(({'total_initiator_bytes': int(groups['tot_init_bytes'])}))
                feature_dict.update(({'total_responder_bytes': int(groups['tot_resp_bytes'])}))
                feature_dict.update(({'application_type': (groups['app_type'])}))
                sess_num = sess_num + 1 
                last_dict_ptr = feature_dict
                continue
        
        return(ret_dict)


class ShowSdwanZbfwStatisticsSchema(MetaParser):
    schema = {
        'zonepair_name': {
            Any(): {
                'src_zone_name': str,
                'dst_zone_name': str,
                'policy_name': str,
                'class_entry': {
                    Any():{
                        'zonepair_name': str,
                        'class_action': str,
                        'pkts_counter': int,
                        'bytes_counter': int,
                        'attempted_conn': int,
                        'current_active_conn': int,
                        'max_active_conn': int,
                        'current_halfopen_conn': int,
                        'max_halfopen_conn': int,
                        'current_terminating_conn': int,
                        'max_terminating_conn': int,
                        'time_since_last_session_create': int,
                        Optional('match_entry'): {
                            Any(): {
                                'seq_num': int,
                                Optional('match_crit'): str,
                                'match_type': str
                            }
                        },
                        Optional('proto_entry'):{
                            int: {
                                'protocol_name': str,
                                'byte_counters': int,
                                'pkt_counters': int
                            }
                        },
                        'l7_policy_name': str      
                    }
                },   
                Optional('l7_class_entry'): {
                    Any(): {
                        'parent_class_name': str,
                        'child_class_action': str,
                        'pkts_counter': int,
                        'bytes_counter': int,
                        'attempted_conn': int,
                        'current_active_conn': int,
                        'max_active_conn': int,
                        'current_halfopen_conn': int,
                        'max_halfopen_conn': int,
                        'current_terminating_conn': int,
                        'max_terminating_conn': int,
                        'time_since_last_session_create': int,
                        Optional('l7_match_entry'): {
                            Any(): {
                                'byte_counters': int,
                                'pkt_counters': int
                            }
                        }
                    }
                }          
            }
        }
    }        



class ShowSdwanZbfwStatistics(ShowSdwanZbfwStatisticsSchema):
    """Parser for show sdwan zbfw zonepair-statistics
    parser class - implements detail parsing mechanisms for cli output.
    """

    cli_command = 'show sdwan zbfw zonepair-statistics'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #zbfw zonepair-statistics ZP_lanZone_lanZone_Is_-902685811
        #p1 = re.compile(r'^zbfw zonepair-statistics (?P<zp_name>\S+)$')
        p1 = re.compile(r'^zbfw\s+zonepair-statistics\s+(?P<zp_name>\S+)$')

        #fw-traffic-class-entry Isn4451ZbfPolicy-seq-1-cm_
        p2 = re.compile(r'^(?P<class_name>(fw-traffic-class-entry|fw-l7-traffic-class-entry)) (?P<class_entry>\S+)$')
                        
        #fw-tc-match-entry "match-any Isn4451ZbfPolicy-svrf1-l4-cm_" 11
        #p3 = re.compile(r'^fw-tc-match-entry "(?P<match_crit>\S+)\s+(?P<tc_entry>[\w\d\s-]+)"\s(?P<tc_num>\S+)$')
        p3 = re.compile(r'^fw-tc-match-entry\s+"(?P<match_crit>\S+)\s+(?P<tc_entry>[\w\d\s-]+)"\s+(?P<tc_num>\S+)$')

        #fw-tc-match-entry Isn4451ZbfPolicy-seq-vrf5-acl_ 3
        #p4 = re.compile(r'^fw-tc-match-entry (?P<tc_entry>[\w\d\s-]+)\s(?P<tc_num>\S+)$')
        p4 = re.compile(r'^fw-tc-match-entry\s+(?P<tc_entry>[\w\d\s-]+)\s(?P<tc_num>\S+)$')

        #fw-tc-proto-entry 1
        #p5 = re.compile(r'^(?P<match_name>fw-tc-proto-entry|fw-l7-tc-match-app-entry)\s+(?P<entry_val>[\w\d\-]+)$')
        p5 = re.compile(r'^(?P<match_name>fw-tc-proto-entry|fw-l7-tc-match-app-entry)\s+(?P<entry_val>[\w\d\-]+)$')

        #l7-policy-name                 NONE
        p6 = re.compile(r'^(?P<entry_name>l7-policy-name)\s+(?P<entry_val>\S+)$')

        #src-zone-name lanZone
        #p5 = re.compile(r'^(?P<key>\S+)\s+(?P<value>\S+)$')
        p7 = re.compile(r'^(?P<key>\S+)\s+\"?(?P<value>[\w\s\d\-\_]+)\"?$')


        ret_dict = {}
        last_dict_ptr = {}
        for line in out.splitlines():
            line = line.strip()

            #zbfw zonepair-statistics ZP_lanZone_lanZone_Is_-902685811
            m = p1.match(line)      
            if m:
                groups = m.groupdict()
                feature_dict = ret_dict.setdefault('zonepair_name', {}).setdefault(groups['zp_name'], {})
                last_dict_ptr = feature_dict
                continue

            #fw-traffic-class-entry Isn4451ZbfPolicy-seq-1-cm_
            m = p2.match(line)      
            if m:
                groups = m.groupdict()
                if(groups['class_name'] == 'fw-l7-traffic-class-entry'):
                    class_dict = feature_dict.setdefault('l7_class_entry', {}).setdefault(groups['class_entry'], {})
                else:
                    class_dict = feature_dict.setdefault('class_entry', {}).setdefault(groups['class_entry'], {})
                last_dict_ptr = class_dict
                continue

            #fw-tc-match-entry "match-any Isn4451ZbfPolicy-svrf1-l4-cm_" 11
            m = p3.match(line)
            if m:
                groups = m.groupdict()                
                tc_dict = class_dict.setdefault('match_entry', {}).setdefault(groups['tc_entry'], {})
                tc_dict.update({'seq_num': int(groups['tc_num'])})
                tc_dict.update({'match_crit': (groups['match_crit'])})
                last_dict_ptr = tc_dict
                continue

            m = p4.match(line)
            if m:
                groups = m.groupdict()
                tc_dict = class_dict.setdefault('match_entry', {}).setdefault(groups['tc_entry'], {})
                tc_dict.update({'seq_num': int(groups['tc_num'])})
                last_dict_ptr = tc_dict
                continue

            m = p5.match(line)
            if m:
                groups = m.groupdict()
                if(groups['match_name'] == 'fw-l7-tc-match-app-entry'):
                    tc1_dict = class_dict.setdefault('l7_match_entry', {}).setdefault(groups['entry_val'], {})
                else:
                    tc1_dict = class_dict.setdefault('proto_entry', {}).setdefault(int(groups['entry_val']), {})

                    #tc1_dict = class_dict.setdefault(groups['entry_name'], {})
                    #tc1_dict.update({'seq_num': int(groups['tc_num'])})
                last_dict_ptr = tc1_dict
                continue

            m = p6.match(line)
            if m:
                groups = m.groupdict()
                class_dict.update({groups['entry_name'].replace('-', '_'): (groups['entry_val'])})
                continue

            #src-zone-name lanZone
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                if groups['key'].replace('-', '_').strip() in ['class_action','src_zone_name','dst_zone_name','policy_name','zonepair_name','class_action','protocol_name','match_type','parent_class_name','child_class_action']:
                    last_dict_ptr.update({groups['key'].replace('-', '_'): groups['value']})
                else:
                    last_dict_ptr.update({groups['key'].replace('-', '_'): int(groups['value'])})
                    continue

        return(ret_dict) 