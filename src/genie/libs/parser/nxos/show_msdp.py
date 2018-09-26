"""show_msdp.py

NXOS parser for the following show commands:
    * show ip msdp peer vrf <vrf>
    * show ip msdp sa-cache detail vrf <vrf>
    * show ip msdp policy statistics sa-policy <address> in [vrf <vrf>]
    * show ip msdp policy statistics sa-policy <address> out [vrf <vrf>]
    * show ip msdp summary
    * show ip msdp summary vrf all
    * show ip msdp summary vrf <vrf>
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# ====================================================
#  schema for show ip msdp peer vrf <vrf>
# ====================================================
class ShowIpMsdpPeerVrfSchema(MetaParser):
    """Schema for:
        show show ip msdp peer vrf <vrf>"""

    schema = {
        'vrf': {
            Any(): {
                'peer': {
                    Any(): {
                        'connect_source': str,
                        'peer_as': str,
                        'connect_source_address': str,
                        Optional('authentication'): {
                            'password': {
                                'set': bool,
                                Optional('key'): str,
                            }
                        },
                        'enable': bool,
                        Optional('description'): str,
                        Optional('reset_reason'): str,
                        Optional('mesh_group'): str,
                        'sa_limit': str,
                        'session_state': str,
                        'elapsed_time': str,
                        Optional('sa_filter'): {
                            Optional('in'): str,
                            Optional('out'): str,
                        },
                        'timer': {
                            'connect_retry_interval': int,
                            'keepalive_interval': int,
                            'holdtime_interval': int,
                        },
                        'statistics': {
                            'last_message_received': str,
                            Optional('connection_attempts'): int,
                            Optional('cache_lifetime'):str,
                            Optional('established_transitions'):int,
                            'discontinuity_time': str,
                            'port':{
                                'local': int,
                                'remote': int,
                            },
                            'error': {
                                'rpf_failure': str,
                            },
                            'received': {
                                Optional('keepalive'): int,
                                Optional('notification'): int,
                                Optional('sa_message'): int,
                                Optional('sa_response'): int,
                                Optional('sa_request'): int,
                                Optional('total'): int,
                                Optional('ctrl_message'):int,
                                Optional('data_message'): int,
                            },
                            'sent': {
                                Optional('keepalive'): int,
                                Optional('notification'): int,
                                Optional('sa_message'): int,
                                Optional('sa_response'): int,
                                Optional('sa_request'): int,
                                Optional('total'): int,
                                Optional('ctrl_message'): int,
                                Optional('data_message'): int,
                            },

                        },
                    },
                },
            },
        },
    }


# ====================================================
#  parser for show ip msdp peer vrf <vrf>
# ====================================================
class ShowIpMsdpPeerVrf(ShowIpMsdpPeerVrfSchema):
    """Parser for :
       show ip msdp peer vrf <vrf>"""

    def cli(self,vrf=""):

        if vrf and vrf !='default':
            out = self.device.execute('show ip msdp peer vrf {}'.format(vrf))
        else:
            out = self.device.execute('show ip msdp peer')
        result_dict = {}

        # MSDP peer 1.1.1.1 for VRF "default"
        p1 = re.compile(r'^\s*MSDP +peer +(?P<address>[\d\.]+) +for +VRF +\"(?P<vrf>[\w]+)\"$')

        # AS 100, local address: 3.3.3.3 (loopback0)
        p2 = re.compile(r'^\s*AS +(?P<peer_as>[\d]+), +local address: +(?P<connect_source_address>[\d\.]+)'
                        ' +\((?P<connect_source>[\w\-\/\.]+)\)$')
        #   Description: R1
        p3 = re.compile(r'^\s*Description: +(?P<description>[\S\s]+)$')

        #   Connection status: Established
        #   Connection status: Admin-shutdown
        #   Connection status: Inactive, Connecting in: 0.217135
        p4 = re.compile(r'^\s*Connection status: +(?P<session_state>[\w\-]+)(, +(Connecting|Listening) +in:'
                        ' +(?P<conecting_time>[\w\:\.]+))?$')
        #     Uptime(Downtime): 01:27:25
        p5 = re.compile(r'^\s*Uptime\(Downtime\): +(?P<elapsed_time>[\w\:\.]+)$')

        #     Last reset reason: Keepalive timer expired
        p6 = re.compile(r'^\s*Last +reset +reason: +(?P<reset_reason>[\S\s]+)$')

        #     Password: not set
        p7 = re.compile(r'^\s*Password: +(?P<password>[\w\s]+)$')

        #   Keepalive Interval: 60 sec
        p8 = re.compile(r'^\s*Keepalive Interval: +(?P<keepalive_interval>[\d]+) +sec$')

        #   Keepalive Timeout: 90 sec
        p9 = re.compile(r'^\s*Keepalive +Timeout: +(?P<keepalive_timeout>[\d]+) +sec$')

        #   Reconnection Interval: 33 sec
        p10 = re.compile(r'^\s*Reconnection +Interval: +(?P<reconnection_interval>[\d]+) +sec$')

        #   Policies:
        p11 = re.compile(r'^\s*Policies:$')

        #     SA in: none, SA out: none
        p12 = re.compile(r'^\s*SA +in: +(?P<sa_in>[\w]+), +SA +out: +(?P<sa_out>[\w]+)$')

        #     SA limit: 111
        p13 = re.compile(r'^\s*SA +limit: +(?P<sa_limit>[\w]+)$')

        #   Member of mesh-group: 1
        p14 = re.compile(r'^\s*Member +of +mesh-group: +(?P<mesh_group>\S+)$')

        #   Statistics (in/out):
        p15 = re.compile(r'^\s*Statistics +\(in/out\):$')

        #     Last messaged received: 00:00:22
        p16 = re.compile(r'^\s*Last messaged received: +(?P<last_message_received>[\w\:\.]+)$')

        #     SAs: 0/0, SA-Requests: 0/0, SA-Responses: 0/0
        p17 = re.compile(r'^\s*SAs: +(?P<in_sas>[\d]+)/+(?P<out_sas>[\d]+), +SA-Requests:'
                         ' +(?P<in_sa_request>[\d]+)/+(?P<out_sa_request>[\d]+)'
                         ', SA-Responses: +(?P<in_sa_response>[\d]+)/+(?P<out_sa_response>[\d]+)$')

        #     In/Out Ctrl Msgs: 0/0, In/Out Data Msgs: 0/0
        p18 = re.compile(r'^\s*In/Out +Ctrl +Msgs: +(?P<in_ctrl_msg>[\d]+)/+(?P<out_ctrl_msg>[\d]+), In/Out Data Msgs:'
                         ' +(?P<in_data_messages>[\d]+)/+(?P<out_data_messages>[\d]+)$')

        #     Remote/Local Port 26743/639
        p19 = re.compile(r'^\s*Remote/Local Port +(?P<remote_port>[\d]+)/+(?P<local_port>[\d]+)$')

        #     Keepalives: 92/119, Notifications: 0/6
        p20 = re.compile(
            r'^\s*Keepalives: +(?P<in_keepalive>[\d]+)/+(?P<out_keepalive>[\d]+), Notifications:'
            ' +(?P<in_notification>[\d]+)/+(?P<out_notification>[\d]+)$')

        #     RPF check failures: 0
        p21 = re.compile(r'^\s*RPF check failures: +(?P<rpf_check_failures>[\d]+)$')

        #     Cache Lifetime: 00:03:30
        p22 = re.compile(r'^\s*Cache Lifetime: +(?P<cache_lifetime>[\w\:\.]+)$')

        #     Established Transitions: 6
        p23 = re.compile(r'^\s*Established Transitions: +(?P<established_transition>[\d]+)$')

        #     Connection Attempts: 0
        p24 = re.compile(r'^\s*Connection Attempts: +(?P<connection_attemps>[\d]+)$')

        #     Discontinuity Time: 01:27:25
        p25 = re.compile(r'^\s*Discontinuity Time: +(?P<discontinuity_time>[\w\:\.]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                address = group.get("address")
                vrf = group.get("vrf")
                peer_dict = result_dict.setdefault('vrf',{}).setdefault(vrf,{}).setdefault('peer',{})
                address_dict = peer_dict.setdefault(address,{})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                address_dict.update({k:v for k,v in group.items()})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                if group["description"] != 'none':
                    address_dict.update({'description': group.get("description")})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                session_state = group.get("session_state").lower()
                address_dict.update({'session_state': session_state})
                address_dict.update({'enable': True if session_state not in ["admin-shutdown",'inactive'] else False})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                address_dict.update({'elapsed_time': group.get("elapsed_time")})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                address_dict.update({'reset_reason': group.get("reset_reason")})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                passsword_dict = address_dict.setdefault('authentication',{}).setdefault('password',{})
                passsword_dict.update({'set': False if 'not set' in group.get("password") else True})
                if 'not set' not in group.get("password"):
                    passsword_dict.update({'key': group.get("password")})


                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                timer_dict = address_dict.setdefault('timer', {})
                timer_dict.update({'keepalive_interval': int(group.get("keepalive_interval"))})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                timer_dict.update({'holdtime_interval': int(group.get("keepalive_timeout"))})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                timer_dict.update({'connect_retry_interval': int(group.get("reconnection_interval"))})
                continue

            m = p11.match(line)
            if m:
                filter_dict = address_dict.setdefault('sa_filter', {})
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                sa_in = group.get("sa_in")
                sa_out = group.get("sa_out")
                if 'none' not in sa_in:
                    filter_dict.update({"in": sa_in})
                if 'none' not in sa_out:
                    filter_dict.update({"out": sa_out})
                if sa_in == sa_out == 'none':
                    address_dict.pop('sa_filter')
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                address_dict.update({'sa_limit': group.get("sa_limit")})
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                if group["mesh_group"] != 'no': 
                    address_dict.update({'mesh_group': group.get("mesh_group")})
                continue

            m = p15.match(line)
            if m:
                statistic_dict = address_dict.setdefault('statistics', {})
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                statistic_dict.update({"last_message_received": group.get("last_message_received")})
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                sent_dict = statistic_dict.setdefault("sent", {})
                received_dict = statistic_dict.setdefault("received", {})
                received_dict.update({"sa_request": int(group.get("in_sa_request"))})
                sent_dict.update({"sa_request": int(group.get("out_sa_request"))})
                received_dict.update({"total": int(group.get("in_sas"))})
                sent_dict.update({"total": int(group.get("out_sas"))})
                received_dict.update({"sa_response": int(group.get("in_sa_response"))})
                sent_dict.update({"sa_response": int(group.get("out_sa_response"))})
                continue

            m = p18.match(line)
            if m:
                group = m.groupdict()
                received_dict.update({"ctrl_message": int(group.get("in_ctrl_msg"))})
                sent_dict.update({"ctrl_message": int(group.get("out_ctrl_msg"))})
                received_dict.update({"data_message": int(group.get("in_data_messages"))})
                sent_dict.update({"data_message": int(group.get("out_data_messages"))})
                continue

            m = p19.match(line)
            if m:
                group = m.groupdict()
                port_dict = statistic_dict.setdefault('port',{})
                port_dict.update({"remote": int(group.get("remote_port"))})
                port_dict.update({"local": int(group.get("local_port"))})
                continue

            m = p20.match(line)
            if m:
                group = m.groupdict()
                received_dict.update({"keepalive": int(group.get("in_keepalive"))})
                sent_dict.update({"keepalive": int(group.get("out_keepalive"))})
                received_dict.update({"notification": int(group.get("in_notification"))})
                sent_dict.update({"notification": int(group.get("out_notification"))})
                continue

            m = p21.match(line)
            if m:
                group = m.groupdict()
                error_dict = statistic_dict.setdefault("error",{})
                error_dict.update({'rpf_failure': group.get("rpf_check_failures")})
                continue

            m = p22.match(line)
            if m:
                group = m.groupdict()
                statistic_dict.update({'cache_lifetime': group.get("cache_lifetime")})
                continue

            m = p23.match(line)
            if m:
                group = m.groupdict()
                statistic_dict.update({'established_transitions': int(group.get("established_transition"))})
                continue

            m = p24.match(line)
            if m:
                group = m.groupdict()
                statistic_dict.update({'connection_attempts': int(group.get("connection_attemps"))})
                continue

            m = p25.match(line)
            if m:
                group = m.groupdict()
                statistic_dict.update({'discontinuity_time':group.get("discontinuity_time")})
                continue

        return result_dict

# ==================================================
# schema for show ip msdp sa-cache detail vrf <vrf>
# ===================================================
class ShowIpMsdpSaCacheDetailVrfSchema(MetaParser):
    """Schema for:
        show ip msdp sa-cache detail vrf <vrf>"""

    schema = {
        'vrf': {
            Any(): {
                'sa_cache': {
                    Any(): {
                        'group': str,
                        'source_addr': str,
                        'up_time': str,
                        'expire': str,
                        'asn': int,
                        'peer_learned_from': str,
                        'origin_rp': {
                            Any():{
                              'rp_address': str,
                            },
                        },
                    },
                },
            },
        },
    }


# ====================================================
#  parser for show ip msdp sa-cache detail vrf <vrf>
# ====================================================
class ShowIpMsdpSaCacheDetailVrf(ShowIpMsdpSaCacheDetailVrfSchema):
    """Parser for :
       show ip msdp sa-cache detail vrf <vrf>"""

    def cli(self,vrf=""):

        if vrf and vrf !='default':
            out = self.device.execute('show ip msdp sa-cache detail vrf {}'.format(vrf))
        else:
            out = self.device.execute('show ip msdp sa-cache detail')

        result_dict = {}
        # MSDP SA Route Cache for VRF "default" - 1 entries
        p1 = re.compile(r'^\s*MSDP SA Route Cache for VRF +\"(?P<vrf>[\w]+)\" +\- +(?P<number_of_entries>[\d]+) +entries$')

        # Source          Group            RP               ASN         Uptime
        # 173.1.1.2       228.1.1.1        10.106.106.106   100         00:02:43
        p2 = re.compile(r'^\s*(?P<source>[\d\.]+) +(?P<group>[\d\.]+) +(?P<rp>[\d\.]+) +(?P<asn>[\d\.]+) +(?P<uptime>[\w\:\.]+)$')

        #     Peer: 10.106.106.106, Expires: 00:02:32
        p3 = re.compile(r'^\s*Peer: +(?P<peer>[\d\.]+), +Expires: +(?P<expire>[\d\:]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue
            
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = group.get("vrf")
                entries = int(group.get("number_of_entries"))
                if entries:
                    sa_cache_dict = result_dict.setdefault('vrf',{}).setdefault(vrf,{}).setdefault('sa_cache',{})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                sa_source_addr = group.get("source")
                sa_group = group.get("group")
                sa_rp_address = group.get("rp")
                sa_asn = group.get("asn")
                up_time = group.get("uptime")
                subsection_value = "{0} {1}".format(sa_group,sa_source_addr)
                subsection_dict = sa_cache_dict.setdefault(subsection_value, {})
                subsection_dict.update({'group': sa_group})
                subsection_dict.update({'source_addr': sa_source_addr})
                subsection_dict.update({'up_time': up_time})
                subsection_dict.update({'asn': int(sa_asn)})
                rp_dict = subsection_dict.setdefault('origin_rp',{}).setdefault(sa_rp_address,{})
                rp_dict.update({'rp_address': sa_rp_address})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                subsection_dict.update({'peer_learned_from': group.get("peer")})
                subsection_dict.update({'expire': group.get("expire")})
                continue

        return result_dict

# =====================================================================
# schema for show ip msdp policy statistics sa-policy <address> in|out
# =====================================================================
class ShowIpMsdpPolicyStatisticsSaPolicyInOutSchema(MetaParser):
    """Schema for:
        show ip msdp policy statistics sa-policy <address> in
        show ip msdp policy statistics sa-policy <address> out"""

    schema = {
        'vrf': {
            Any(): {
                'peer': {
                    Any(): {                        
                        Optional('in'): {
                           'total_accept_count': int,
                           'total_reject_count': int,
                            Any(): { # 'filtera'
                                Any(): { # 'route-map filtera permit 10 match ip address mcast-all-groups'
                                    Optional('num_of_comparison'): int,
                                    Optional('num_of_matches'): int,
                                    'match': str,
                                },
                            }
                        },
                        Optional('out'): {
                           'total_accept_count': int,
                           'total_reject_count': int,
                            Any(): { # 'filtera'
                                Any(): { # 'route-map filtera permit 10 match ip address mcast-all-groups'
                                    Optional('num_of_comparison'): int,
                                    Optional('num_of_matches'): int,
                                    'match': str,
                                },
                            }
                        }
                    },
                },
            },
        },
    }


# =====================================================================
# parser for show ip msdp policy statistics sa-policy <address> in|out
# =====================================================================
class ShowIpMsdpPolicyStatisticsSaPolicyInOut(ShowIpMsdpPolicyStatisticsSaPolicyInOutSchema):
    """Parser for :
        show ip msdp policy statistics sa-policy <address> in
        show ip msdp policy statistics sa-policy <address> out"""

    def cli(self, peer, method, vrf=''):

        assert method in ['in', 'out']

        cmd = 'show ip msdp policy statistics sa-policy %s %s' % (peer, method)

        if vrf and vrf != 'default':
            cmd += ' vrf %s' % vrf
        else:
            vrf = 'default'

        out = self.device.execute(cmd)

        ret_dict = {}
        match1 = ''

        # route-map filtera permit 10
        p1 = re.compile(r'^(?P<match1>route\-map +(?P<sa_filter>\S+) +permit +(?P<permit>\d+))$')

        # ip prefix-list pfxlista seq 5 permit 224.0.0.0/4             M: 0
        # ip prefix-list pfxlista seq 10 permit 224.0.0.0/4 le 32      M: 0
        p1_1 = re.compile(r'^(?P<match>ip +prefix\-list +(?P<sa_filter>\S+) +seq +(?P<seq>\d+) '
                           '+permit +(?P<permit>\S+)(?P<operator>[\w\s]+)?)'
                           '( +(C: +(?P<comparisions>\d+)))?( +(M: +(?P<matches>\d+)))?$')

        # match ip address mcast-all-groups                          C: 0      M: 0
        p2 = re.compile(r'^(?P<match2>match +ip +address +(?P<match_ip>\S+))'
                         '( +(C: +(?P<comparisions>\d+)))?( +(M: +(?P<matches>\d+)))?$')

        # Total accept count for policy: 0
        p3 = re.compile(r'^Total +accept +count +for +policy: +(?P<total_accept_count>\d+)$')

        # Total reject count for policy: 0
        p4 = re.compile(r'^Total +reject +count +for +policy: +(?P<total_reject_count>\d+)$')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            # route-map filtera permit 10
            m = p1.match(line)
            if m:
                group = m.groupdict()
                match1 = group['match1']
                sa_filter = group['sa_filter']
                permit = group['permit']
                sa_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {})\
                    .setdefault('peer', {}).setdefault(peer, {}).setdefault(method, {})\
                        .setdefault(sa_filter, {})
                continue

            # match ip address mcast-all-groups                          C: 0      M: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                match2 = group['match2']
                match = '%s %s' % (match1, match2)
                match_dict = sa_dict.setdefault(match.strip(), {})
                if group['comparisions']:
                    match_dict['num_of_comparison'] = int(group['comparisions'])
                if group['matches']:
                    match_dict['num_of_matches'] = int(group['matches'])
                match_dict['match'] = match
                continue

            # ip prefix-list pfxlista seq 5 permit 224.0.0.0/4             M: 0
            # ip prefix-list pfxlista seq 10 permit 224.0.0.0/4 le 32      M: 0
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                match = group['match'].strip()
                sa_filter = group['sa_filter']
                match_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {})\
                    .setdefault('peer', {}).setdefault(peer, {}).setdefault(method, {})\
                        .setdefault(sa_filter, {}).setdefault(match, {})
                match_dict['match'] = match
                if group['comparisions']:
                    match_dict['num_of_comparison'] = int(group['comparisions'])
                if group['matches']:
                    match_dict['num_of_matches'] = int(group['matches'])
                continue

            # Total accept count for policy: 0
            m = p3.match(line)
            if m:
                total_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {})\
                    .setdefault('peer', {}).setdefault(peer, {}).setdefault(method, {})
                total_dict['total_accept_count'] = int(m.groupdict()['total_accept_count'])
                continue

            # Total reject count for policy: 0
            m = p4.match(line)
            if m:
                total_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {})\
                    .setdefault('peer', {}).setdefault(peer, {}).setdefault(method, {})
                total_dict['total_reject_count'] = int(m.groupdict()['total_reject_count'])
                continue

        return ret_dict


# ================================================================
# parser for show ip msdp policy statistics sa-policy <address> in
# ================================================================
class ShowIpMsdpPolicyStatisticsSaPolicyIn(ShowIpMsdpPolicyStatisticsSaPolicyInOut):
    """Parser for :
        show ip msdp policy statistics sa-policy <address> in"""

    def cli(self, peer, vrf=''):
        return super().cli(peer=peer, method='in', vrf=vrf)


# ================================================================
# parser for show ip msdp policy statistics sa-policy <address> in
# ================================================================
class ShowIpMsdpPolicyStatisticsSaPolicyOut(ShowIpMsdpPolicyStatisticsSaPolicyInOut):
    """Parser for :
        show ip msdp policy statistics sa-policy <address> out"""

    def cli(self, peer, vrf=''):
        return super().cli(peer=peer, method='out', vrf=vrf)


# ============================================
# schema for show ip msdp summary [vrf <vrf>]
# ============================================
class ShowIpMsdpSummarySchema(MetaParser):
    """Schema for:
        show ip msdp summary
        show ip msdp summary vrf all
        show ip msdp summary vrf <vrf>"""

    schema = {
        'vrf': {
            Any(): {
                'local_as': int,
                'originator_id': str,
                'statistics': {
                    'num_of_configured_peers': int,
                    'num_of_established_peers': int,
                    'num_of_shutdown_peers': int,
                },
                Optional('peer'): {
                    Any(): {
                        'session_state': str,
                        'peer_as': int,
                        'elapsed_time': str,
                        'address': str,
                        'statistics': {
                            'last_message_received': str,
                            'num_of_sg_received': int,
                        },
                    }
                },
            },
        },
    }


# ============================================
# parser for show ip msdp summary [vrf <vrf>]
# ============================================
class ShowIpMsdpSummary(ShowIpMsdpSummarySchema):
    """Parser for :
        show ip msdp summary
        show ip msdp summary vrf all
        show ip msdp summary vrf <vrf>"""

    def cli(self, vrf=''):

        if vrf and vrf !='default':
            out = self.device.execute('show ip msdp summary vrf {}'.format(vrf))
        else:
            out = self.device.execute('show ip msdp summary')

        ret_dict = {}

        # MSDP Peer Status Summary for VRF "default"
        p1 = re.compile(r'^MSDP +Peer +Status +Summary +for +VRF +\"(?P<vrf>\S+)\"$')

        # Local ASN: 0, originator-id: 2.2.2.2
        p2 = re.compile(r'^Local +ASN: +(?P<local_as>\d+), +'
                         'originator\-id: +(?P<originator_id>[\d\.]+)$')

        # Number of configured peers:  1
        p3 = re.compile(r'^Number +of +configured +peers: +(?P<num_of_configured_peers>\d+)$')
        # Number of established peers: 1
        p4 = re.compile(r'^Number +of +established +peers: +(?P<num_of_established_peers>\d+)$')
        # Number of shutdown peers:    0
        p5 = re.compile(r'^Number +of +shutdown +peers: +(?P<num_of_shutdown_peers>\d+)$')

        # Peer            Peer        Connection      Uptime/   Last msg  (S,G)s
        # Address         ASN         State           Downtime  Received  Received
        # 6.6.6.6         0           Established     05:46:19  00:00:51  1
        p6 = re.compile(r'^(?P<address>[\d\.]+) +(?P<peer_as>\d+) +(?P<session_state>[\w\/\-]+) +'
                         '(?P<elapsed_time>[\w\.\:]+) +(?P<last_message_received>[\w\.\:]+) +'
                         '(?P<num_of_sg_received>\d+)$')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            # MSDP Peer Status Summary for VRF "default"
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']
                vrf_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {})
                continue

            # Local ASN: 0, originator-id: 2.2.2.2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['local_as'] = int(group['local_as'])
                vrf_dict['originator_id'] = group['originator_id']
                continue

            # Number of configured peers:  1
            # Number of established peers: 1
            # Number of shutdown peers:    0
            m1 = p3.match(line)
            m2 = p4.match(line)
            m3 = p5.match(line)
            m = m1 or m2 or m3
            if m:
                vrf_dict.setdefault('statistics', {}).update({k:int(v) for k, v in m.groupdict().items()})
                continue

            # # 6.6.6.6         0           Established     05:46:19  00:00:51  1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                address = group['address']
                peer_dict = vrf_dict.setdefault('peer', {}).setdefault(address, {})
                peer_dict['address'] = address
                peer_dict['peer_as'] = int(group['peer_as'])
                peer_dict['session_state'] = group['session_state'].lower()
                peer_dict['elapsed_time'] = group['elapsed_time']
                stat_dict = peer_dict.setdefault('statistics', {})
                stat_dict['last_message_received'] = group['last_message_received']
                stat_dict['num_of_sg_received'] = int(group['num_of_sg_received'])
                continue

        return ret_dict


# ====================================================
# schema for show run msdp [| sec vrf | inc <pip_str>]
# ====================================================
class ShowRunningConfigMsdpSchema(MetaParser):
    """Schema for:
        show run msdp [| sec vrf | inc <pip_str>]"""

    schema = {
        'vrf': {
            Any(): {
                Optional('global'): {
                    Optional('timer'): {
                        'connect_retry_interval': int, # global_connect_retry_interval
                    },
                    Optional('originating_rp'): str,
                },
                Optional('peer'): {
                    Any(): { 
                        Optional('connect_source'): str, # connected_source
                        Optional('peer_as'): str, # peer_as
                        Optional('description'): str, # description
                        Optional('timer'): {
                            'keepalive_interval': int, # keepalive_interval
                            'holdtime_interval': int, # keepalive_interval
                        },
                    }
                }
            }
        }
    }


# =======================================================
# parser for show run msdp [| sec <vrf> | inc <pip_str>]
# =======================================================
class ShowRunningConfigMsdp(ShowRunningConfigMsdpSchema):
    """Parser for :
        show run msdp [| sec <vrf> | inc <pip_str>]"""

    def cli(self, pip_str=None, vrf=None):

        cmd  = 'show running-config msdp'
        if vrf:
            if vrf == 'default':
                # command start with ip pim, or interface without spaces
                cmd += " | sec '^i'"
            else:
                cmd += ' | sec %s' % vrf
        if pip_str:
            cmd += ' | inc %s' % pip_str

        # initial output
        out = self.device.execute(cmd)

        # Init vars
        msdp_dict = {}

        # initial regular express
        # vrf context VRF1
        p_vrf  = re.compile(r'^vrf +context +(?P<vrf>\S+)$')

        # ip msdp keepalive 6.6.6.6 20 30
        p1 = re.compile(r'^ip +msdp +keepalive +(?P<peer>[\d\.]+) +'
                         '(?P<keepalive_interval>\d+) +(?P<holdtime_interval>\d+)$')

        # ip msdp description 6.6.6.6 some description
        p2 = re.compile(r'^ip +msdp +description +(?P<peer>[\d\.]+) +'
                         '(?P<description>.*)$')

        # ip msdp reconnect-interval 20
        p3 = re.compile(r'^ip +msdp +reconnect\-interval +(?P<connect_retry_interval>\d+)$')

        # ip msdp originator-id loopback11
        p4 = re.compile(r'^ip +msdp +originator\-id +(?P<originating_rp>[\w\.\-\/]+)$')

        # ip msdp peer 3.3.3.3 connect-source loopback0 remote-as 234
        # ip msdp peer 6.6.6.6 connect-source loopback11
        p5 = re.compile(r'^ip +msdp +peer +(?P<peer>[\d\.]+) +connect\-source +'
                         '(?P<connected_source>[\w\-\/\.]+)( +remote\-as +(?P<peer_as>\d+))?$')

        for line in out.splitlines():
            if line and not line.startswith(' '):
                vrf_dict = msdp_dict.setdefault('vrf', {}).setdefault('default', {})
            elif vrf:
                vrf_dict = msdp_dict.setdefault('vrf', {}).setdefault(vrf, {})

            line = line.strip()

            # vrf context VRF1
            m = p_vrf.match(line)
            if m:
                vrf_dict = msdp_dict.setdefault('vrf', {}).setdefault(m.groupdict()['vrf'], {})
                continue

            # ip msdp keepalive 6.6.6.6 20 30
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                timer_dict = vrf_dict.setdefault('peer', {})\
                    .setdefault(groups['peer'], {}).setdefault('timer', {})
                timer_dict['keepalive_interval'] = int(groups['keepalive_interval'])
                timer_dict['holdtime_interval'] = int(groups['holdtime_interval'])
                continue

            # ip msdp description 6.6.6.6 some description
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                peer_dict = vrf_dict.setdefault('peer', {}).setdefault(groups['peer'], {})
                peer_dict['description'] = groups['description']
                continue

            # ip msdp reconnect-interval 20
            m = p3.match(line)
            if m:
                global_dict = vrf_dict.setdefault('global', {}).setdefault('timer', {})
                global_dict['connect_retry_interval'] = int(m.groupdict()['connect_retry_interval'])        
                continue

            # ip msdp originator-id loopback11
            m = p4.match(line)
            if m:
                global_dict = vrf_dict.setdefault('global', {})
                global_dict['originating_rp'] = m.groupdict()['originating_rp']
                continue

            # ip msdp peer 3.3.3.3 connect-source loopback0 remote-as 234
            # ip msdp peer 6.6.6.6 connect-source loopback11
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                peer_dict = vrf_dict.setdefault('peer', {}).setdefault(groups['peer'], {})
                peer_dict['connect_source'] = groups['connected_source']
                if groups['peer_as']:
                    peer_dict['peer_as'] = groups['peer_as']
                continue

        return msdp_dict
