"""show_msdp.py

NXOS parser for the following show commands:
    * show ip msdp peer vrf <vrf>
    * show ip msdp sa-cache detail vrf <vrf>
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
                        'mesh_group': str,
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

        out = self.device.execute('show ip msdp peer vrf {}'.format(vrf if vrf else "all"))
        result_dict = {}

        # MSDP peer 1.1.1.1 for VRF "default"
        p1 = re.compile(r'^\s*MSDP +peer +(?P<address>[\d\.]+) +for +VRF +\"(?P<vrf>[\w]+)\"$')

        # AS 100, local address: 3.3.3.3 (loopback0)
        p2 = re.compile(r'^\s*AS +(?P<peer_as>[\d]+), +local address: +(?P<connect_source_address>[\d\.]+)'
                        ' +\((?P<connect_source>[\w]+)\)$')
        #   Description: R1
        p3 = re.compile(r'^\s*Description: +(?P<description>[\w\s]+)$')

        #   Connection status: Established
        #   Connection status: Admin-shutdown
        #   Connection status: Inactive, Connecting in: 0.217135
        p4 = re.compile(r'^\s*Connection status: +(?P<session_state>[\w]+)(, +Connecting +in:'
                        ' +(?P<conecting_time>[\w\:\.]+))?$')
        #     Uptime(Downtime): 01:27:25
        p5 = re.compile(r'^\s*Uptime\(Downtime\): +(?P<elapsed_time>[\w\:]+)$')

        #     Last reset reason: Keepalive timer expired
        p6 = re.compile(r'^\s*Last +reset +reason: +(?P<reset_reason>[\S\s]+)$')

        #     Password: not set
        p7 = re.compile(r'^\s*Password: +(?P<password>[\w\s]+)$')

        #   Keepalive Interval: 60 sec
        p8 = re.compile(r'^\s*Keepalive Interval: +(?P<keepalive_interval>[\d]+) +sec$')

        #   Keepalive Timeout: 90 sec
        p9 = re.compile(r'^\s*Keepalive Timeout: +(?P<keepalive_timeout>[\d]+) +sec$')

        #   Reconnection Interval: 33 sec
        p10 = re.compile(r'^\s*Reconnection Interval: +(?P<reconnection_interval>[\d]+) +sec$')

        #   Policies:
        p11 = re.compile(r'^\s*Policies:$')

        #     SA in: none, SA out: none
        p12 = re.compile(r'^\s*SA +in: +(?P<sa_in>[\w]+), +SA +out: +(?P<sa_out>[\w]+)$')

        #     SA limit: 111
        p13 = re.compile(r'^\s*SA +limit: +(?P<sa_limit>[\w]+)$')

        #   Member of mesh-group: 1
        p14 = re.compile(r'^\s*Member +of +mesh-group: +(?P<mesh_group>[\w]+)$')

        #   Statistics (in/out):
        p15 = re.compile(r'^\s*Statistics +\(in/out\):$')

        #     Last messaged received: 00:00:22
        p16 = re.compile(r'^\s*Last messaged received: +(?P<last_message_received>[\w\:]+)$')

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
        p22 = re.compile(r'^\s*Cache Lifetime: +(?P<cache_lifetime>[\w\:]+)$')

        #     Established Transitions: 6
        p23 = re.compile(r'^\s*Established Transitions: +(?P<established_transition>[\d]+)$')

        #     Connection Attempts: 0
        p24 = re.compile(r'^\s*Connection Attempts: +(?P<connection_attemps>[\d]+)$')

        #     Discontinuity Time: 01:27:25
        p25 = re.compile(r'^\s*Discontinuity Time: +(?P<discontinuity_time>[\w\:]+)$')

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
                address_dict.update({'description': group.get("description")})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                session_state = group.get("session_state").lower()
                address_dict.update({'session_state': session_state})
                address_dict.update({'enable': True if session_state not in ["shutdown",'inactive'] else False})
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

        out = self.device.execute('show ip msdp sa-cache detail vrf {}'.format(vrf if vrf else "all"))

        result_dict = {}
        # MSDP SA Route Cache for VRF "default" - 1 entries
        p1 = re.compile(r'^\s*MSDP SA Route Cache for VRF +\"(?P<vrf>[\w]+)\" +\- +(?P<number_of_entries>[\d]+) +entries$')

        # Source          Group            RP               ASN         Uptime
        # 173.1.1.2       228.1.1.1        10.106.106.106   100         00:02:43
        p2 = re.compile(r'^\s*(?P<source>[\d\.]+) +(?P<group>[\d\.]+) +(?P<rp>[\d\.]+) +(?P<asn>[\d\.]+) +(?P<uptime>[\d\:\.]+)$')

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
