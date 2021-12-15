"""show_aaa.py
   IOSXE parsers for the following show commands:
     * show aaa servers 
     * show aaa user all
     * show aaa fqdn all
     * show aaa common-criteria policy name {policy_name}  
"""

#python
import re
import logging
logger = logging.getLogger(__name__)

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema,Any,Optional,Or,And,Default,Use
                                         

# ==================================================
# Schema for 'show AAA Server'
# ==================================================
class ShowAAServersSchema(MetaParser):
    """Schema for show aaa servers"""

    schema = {
           'radius_server': {
                Any(): {
                    'id': int,
                    'priority': int,
                    'host': str,
                    Optional('auth_port'): int,
                    Optional('acct_port'): int,
                    Optional('radsec_port'): int,
                    Optional('hostname'): str,
                    Optional('platform_state_type'): {
                        Any(): {
                            Optional('current'): str,
                            Optional('duration'): str,
                            Optional('previous_duration'): str
                        },
                    },
                    Optional('dead_type'): {
                        Optional(Any()): {
                            'total_time': str,
                            'count': str
                        },
                    },

                    Optional('elapsed_time'): str,
                    Optional('estimated_outstanding_access_transactions'): int,
                    Optional('estimated_outstanding_accounting_transactions'): int,
                    Optional('estimated_throttled_access_transactions'): int,
                    Optional('estimated_throttled_accounting_transactions'): int,
                    Optional('maximum_throttled_transactions'): {
                        'access': int,
                        'accounting': int
                        },
                    'quarantined': str,
                    'aaatype': {
                        Any():  {  # authen or author

                            'bad_authenticators': str,
                            Optional('transaction_type'): {
                                Any(): {
                                    'response': {
                                        'avg_response_time': str,
                                        'total_responses': str
                                        },
                                    'transaction': {
                                        'failover': int,
                                        'failure': int,
                                        'success': int,
                                        'timeouts': int,
                                        'total': int
                                        },
                                    },
                                },
                            Optional('malformed_responses'): str,
                            Optional('response'): {
                                'accept': int,
                                'challenge': int,
                                'incorrect': int,
                                'reject': int,
                                'server_error': int,
                                'time': str,
                                'unexpected': int
                            },
                            Optional('throttled'): {
                                    'failure': int,
                                    'timeout': int,
                                    'transaction': int
                                },
                            Optional('transaction'): {
                                    'failure': int,
                                    'success': int
                                },
                            'failover': int,
                            'request': int,
                            'retransmission': int,
                            'timeout': int
                        },
                    },
                    'account': {
                        'bad_authenticators': str,
                        Optional('malformed_responses'): str,
                        Optional('requests'): {
                            'start': int,
                            'interim': int,
                            'stop': int
                        },
                        Optional('responses'): {
                            'start': int,
                            'interim': int,
                            'stop': int,
                        },
                        Optional('response'): {
                            'unexpected': int,
                            'server_error': int,
                            'incorrect': int,
                            'time': str
                        },
                        Optional('throttled'): {
                            'failure': int,
                            'timeout': int,
                            'transaction': int
                            },
                        Optional('transaction'): {
                                'failure': int,
                                'success': int
                            },
                        'failover': int,
                        'request': int,
                        'retransmission': int,
                        'timeout': int
                    },
                    'consecutive_response_failures': {
                            'total': int,
                            'platform_type': {
                                Any(): {
                                    'current': int,
                                    'max': int,
                                    'total': int
                                },
                            },
                        },
                    'consecutive_timeouts': {
                            'total': int,
                            'platform_type': {
                                Any(): {
                                'current': int,
                                'max': int,
                                'total': int
                            },
                        },
                    },
                    'requests_per_minute_past_24_hours': {
                        'average': int,
                        'level_type': {
                            Any(): {
                            'ago': int,
                            'hours': int,
                            'minutes': int
                            },
                        },
                    },
                },
            },
        }

#  ==================================================  
#  Parser for 'show aaa servers'                        
#  ==================================================  
class ShowAAServers(ShowAAServersSchema):
    """Parser for show aaa servers"""

    def cli(self, output = None):
        cli_command = 'show aaa servers'
        if output is None:
            out = self.device.execute(cli_command)
        else:
            out = output

        # initialize variables
        resultdict = {}
        serverdict = {}
        aaadict = {}
        transdict = {}
        consedict = {}

        # RADIUS: id 9, priority 1, host 11.15.24.174, auth-port 1812, acct-port 1813, hostname ISE-RAD
        p1a = re.compile(r'(^.*)\:\s+id\s+(?P<id>\d+)\,\s+priority\s+(?P<priority>(\d+))\,\s+host\s+(?P<host>(.*))\,\s+auth\-port\s+(?P<auth_port>(\d+))\,\s+acct\-port\s+(?P<acct_port>(\d+))\,\s*hostname\s*(?P<hostname>(.*))$')

        # RADIUS: id 9, priority 1, host 11.15.24.174, RADSEC-port 1812,hostname ISE-RAD
        p1b = re.compile(r'(.*)\:\s+id\s+(?P<id>\d+)\,\s+priority\s+(?P<priority>(\d+))\,\s+host\s+(?P<host>(.*))\,\s*(RADSEC\-port\s*(?P<radsec_port>(\d+)))\,\s*hostname\s+(?P<hostname>(.*))$')

        # RADIUS: id 9, priority 1, host 11.15.24.174, auth-port 1812, acct-port 1813
        p1c = re.compile(r'(^.*)\:\s+id\s+(?P<id>\d+)\,\s+priority\s+(?P<priority>(\d+))\,\s+host\s+(?P<host>(.*))\,\s+auth\-port\s+(?P<auth_port>(\d+))\,\s+acct\-port\s+(?P<acct_port>(\d+))$')

        # State: current UP, duration 294173s, previous duration 0s
        p2 = re.compile(r'(^\s*)(State)\:\s+current\s+(?P<current>(.*))\,\s+duration\s+(?P<duration>(.*))\,\s+previous\s+duration\s+(?P<previous_duration>(.*))')

        # Dead: total time 0s, count 0
        p3 = re.compile(r'((.*)Dead)\:\s+total\s+time\s+(?P<total_time>(.*))\,\s+count\s+(?P<count>(.*))$')

        # Platform State from SMD: current UP, duration 4406s, previous duration 0s
        p4 = re.compile(r'(Platform)\s(State)\s+from\s*(.*)\:\s+current\s+(?P<current>(.*))\,\s+duration\s+(?P<duration>(.*))\,\s+previous\s+duration\s+(?P<previous_duration>(.*))$')

        # Platform State from WNCD (1) : current UP
        p5 = re.compile(r'Platform\s(State)\s+from\s*(.*)\s+\((\d+)\)\s+\:\s+current\s+(?P<current>(\w+))$')

        # Quarantined: No
        p6 = re.compile(r'^Quarantined\:\s+(?P<quarantined>(No|Yes))$')

        # Authen: request 0, timeouts 0, failover 0, retransmission 0
        p7 = re.compile(r'^(.*)\:\s+request\s+(?P<request>\d+)\,\s+timeouts\s+(?P<timeout>\d+)\,\s+failover\s+'
                        r'(?P<failover>\d+)\,\s+retransmission\s+(?P<retransmission>\d+)$')

        # Response: accept 0, reject 0, challenge 0
        p8 = re.compile(r'(Response):\s+accept\s+(?P<accept>\d+)\,\s+reject\s+(?P<reject>\d+)\,\s+challenge\s+(?P<challenge>\d+)$')

        # Request: start 0, interim 0, stop 0
        p9 = re.compile(r'(.+)\:\s+start\s+(?P<start>\d+)\,\s+interim\s+(?P<interim>\d+)\,\s+stop\s+(?P<stop>\d+)$')

        # Response: unexpected 0, server error 0, incorrect 0, time 0ms
        p10 = re.compile(r'(Response):\s+unexpected\s+(?P<unexpected>\d+)\,\s+server\s+error\s+'
                         r'(?P<server_error>\d+)\,\s+incorrect\s+(?P<incorrect>\d+)\,\s+time+\s+(?P<time>(.*))$')

        # Transaction: success 0, failure 0
        p11 = re.compile(r'(Transaction)\:\s+success\s+(?P<success>\d+)\,\s+failure\s+(?P<failure>\d+)$')

        # Throttled: transaction 0, timeout 0, failure 0
        p12 = re.compile(
            r'(Throttled)\:\s+transaction\s+(?P<transaction>\d+)\,\s+timeout\s+(?P<timeout>\d+)\,\s+failure\s+(?P<failure>\d+)$')

        # Malformed responses: 0
        p13 = re.compile(r'Malformed\s+responses\:\s+(?P<malformed_responses>\d+)$')

        # Bad authenticators: 0
        p14 = re.compile(r'Bad\s+authenticators\:\s+(?P<bad_authenticators>\d+)$')

        # Dot1x transactions:
        p15 = re.compile(r'(.*)\s+(transactions)\:$')

        # Response: total responses: 0, avg response time: 0ms
        p16 = re.compile(
            r'(Response)\:\s+total\s+responses\:\s+(?P<total_responses>\d+)\,\s+avg\s+response\s+time\:\s+(?P<avg_response_time>(\w+))$')

        # Transaction: timeouts 0, failover 0
        p17 = re.compile(r'(Transaction)\:\s+timeouts\s+(?P<timeouts>\d+)\,\s+failover\s+(?P<failover>\d+)$')

        # Transaction: total 0, success 0, failure 0
        p18 = re.compile(
            r'(Transaction)\:\s+total\s+(?P<total>\d+)\,\s+success\s+(?P<success>\d+)\,\s*failure\s*(?P<failure>\d+)$')

        # Elapsed time since counters last cleared: 1h13m
        p19 = re.compile(
            r'(Elapsed)\s+time\s+since\s+counters\s+last\s+cleared\:\s+(?P<elapsed_time>(\w+))$')

        # Estimated Outstanding Access Transactions: 0
        p20 = re.compile(r'(Estimated)\s+(.*)\s+(.*)\s+(Transactions)\:\s+(\d+)$')

        # Maximum Throttled Transactions: access 0, accounting 0
        p21 = re.compile(
            r'(Maximum)\s+(.+)\s+(Transactions)\:\s+(access)\s+(?P<access>\d+)\,\s+(accounting)\s+(?P<accounting>\d+)$')

        # Consecutive Timeouts: total 0
        # Consecutive Response Failures: total 0
        p22 = re.compile(r'(Consecutive)\s+(.+\s*.*)\:\s+(total)\s+(?P<total>\d+)$')

        # SMD Platform : max 0, current 0 total 0
        p23 = re.compile(
            r'(.+)\s+(Platform)\s*\:\s+(max)\s+(?P<max>\d+)\,\s+(current)\s+(?P<current>\d+)\s+(total)\s+(?P<total>\d+)$')

        # Requests per minute past 24 hours:
        p24 = re.compile(r'(Requests)\s+(per)\s+(minute)\s+(past)\s+(\d+)\s+(hours)\:$')

        # high - 1 hours, 13 minutes ago: 0
        p25 = re.compile(
            r'(.+)\s+\-\s+(?P<hours>\d+)\s+hours\,\s+(?P<minutes>\d+)\s+minutes\s+ago\:\s*(?P<ago>\d+)$')

        # average: 0
        p26 = re.compile(r'(average)\:\s*(?P<average>\d+)$')

        for line in out.splitlines():
            line = line.strip()
        
            # RADIUS: id 9, priority 1, host 11.15.24.174, auth-port 1812, acct-port 1813, hostname ISE-RAD
            res = p1a.match(line)
            if res:
                group = res.groupdict()
                servertype = group['host']
                serverdict = resultdict.setdefault('radius_server', {}).setdefault(servertype, {})
                serverdict.update(
                    {'acct_port': int(group['acct_port']), 'auth_port': int(group['auth_port']), 'host': group['host'],
                     'hostname': group['hostname'], 'priority': int(group['priority']), 'id': int(group['id'])})

            # RADIUS: id 9, priority 1, host 11.15.24.174, RADSEC-port 1812,hostname ISE-RAD
            res = p1b.match(line)
            if res:
                group = res.groupdict()
                servertype = group['host']
                serverdict = resultdict.setdefault('radius_server', {}).setdefault(servertype, {})
                serverdict.update(
                    {'radsec_port': int(group['radsec_port']), 'host': group['host'], 'hostname': group['hostname'],
                     'priority': int(group['priority']), 'id': int(group['id'])})
            
            # RADIUS: id 9, priority 1, host 11.15.24.174, auth-port 1812, acct-port 1813
            res = p1c.match(line)
            if res:
                group = res.groupdict()
                servertype = group['host']
                serverdict = resultdict.setdefault('radius_server', {}).setdefault(servertype, {})
                serverdict.update(
                    {'acct_port': int(group['acct_port']), 'auth_port': int(group['auth_port']), 'host': group['host'],
                     'priority': int(group['priority']), 'id': int(group['id'])})
            
            # State: current UP, duration 294173s, previous duration 0s
            res = p2.match(line)
            if res:
                group = res.groupdict()
                serverdict.setdefault('platform_state_type', {}).setdefault('state', {})
                serverdict['platform_state_type']['state'].update(group)
            
            # Dead: total time 0s, count 0
            res = p3.match(line)
            if res:
                dead = res.group(1).replace(" ","_").lower()
                group = res.groupdict()
                serverdict.setdefault('dead_type', {}).setdefault(dead, {})
                serverdict['dead_type'][dead].update({'total_time': group['total_time'], 'count': group['count']})

            # Platform State from SMD: current UP, duration 4406s, previous duration 0s
            res = p4.match(line)
            if res:
                if 'WNCD' in res.group(3):
                    resd='wncd_'+str((res.group(3).split("("))[1].split(")")[0])
                else:
                    resd='smd'

                pltfm_state = 'platform_state'+'_'+resd
                group = res.groupdict()
                serverdict.setdefault('platform_state_type', {}).setdefault(pltfm_state, {})
                serverdict['platform_state_type'][pltfm_state].update(group)
                    
            # Platform State from WNCD (1) : current UP
            res = p5.match(line)
            if res:
                platform_state = '_'.join(res.group(1, 2,3)).lower()
                group = res.groupdict()
                serverdict.setdefault('platform_state_type', {}).setdefault(platform_state, {})
                serverdict['platform_state_type'][platform_state].update(group)
            
            # Quarantined: No
            res = p6.match(line)
            if res:
                group = res.groupdict()
                serverdict.update(group)

            # Authen: request 0, timeouts 0, failover 0, retransmission 0
            res = p7.match(line)
            if res:
                aaa_type = res.group(1).lower()
                group = res.groupdict()
                if(aaa_type == 'account'):
                    aaadict=serverdict.setdefault(aaa_type, {})
                else:
                    aaadict = serverdict.setdefault('aaatype', {}).setdefault(aaa_type, {})
                aaadict.update({k: int(v) for k, v in group.items()})
            
            # Response: accept 0, reject 0, challenge 0
            res = p8.match(line)
            if res:
                aaaresponse1 = res.group(1).lower()
                group = res.groupdict()
                aaadict.setdefault(aaaresponse1, {})
                aaadict[aaaresponse1].update({k: int(v) for k, v in group.items()})

            # Request: start 0, interim 0, stop 0
            res = p9.match(line)
            if res:
                aaarequest = res.group(1).lower()+'s'
                group = res.groupdict()
                aaadict.setdefault(aaarequest, {})
                aaadict[aaarequest].update({k: int(v) for k, v in group.items()})
            
            # Response: unexpected 0, server error 0, incorrect 0, time 0ms
            res = p10.match(line)
            if res:
                aaaresponse2 = res.group(1).lower()
                group = res.groupdict()
                aaadict.setdefault(aaaresponse2, {})
                aaadict[aaaresponse2].update(
                        {'unexpected': int(group['unexpected']), 'server_error': int(group['server_error']),
                            'incorrect': int(group['incorrect']), 'time': group['time']})

            # Transaction: success 0, failure 0
            res = p11.match(line)
            if res:
                aaatransaction = res.group(1).lower()
                group = res.groupdict()
                aaadict.setdefault(aaatransaction, {})
                aaadict[aaatransaction].update({k: int(v) for k, v in group.items()})
            
            # Throttled: transaction 0, timeout 0, failure 0
            res = p12.match(line)
            if res:
                aaathresold = res.group(1).lower()
                group = res.groupdict()
                aaadict.setdefault(aaathresold, {})
                aaadict[aaathresold].update({k: int(v) for k, v in group.items()})
            
            # Malformed responses: 0
            res = p13.match(line)
            if res:
                group = res.groupdict()
                aaadict.update(group)
            
            # Bad authenticators: 0
            res = p14.match(line)
            if res:
                group = res.groupdict()
                aaadict.update(group)
            
            # Dot1x transactions:
            res = p15.match(line)
            if res:
                transaction_types = res.group(1).replace(" ", "_").lower()
                transdict = aaadict.setdefault('transaction_type', {}).setdefault(transaction_types + 'transactions', {})

            # Response: total responses: 0, avg response time: 0ms
            res = p16.match(line)
            if res:
                aaatransaction_res = res.group(1).lower()
                group = res.groupdict()
                transdict.setdefault(aaatransaction_res, {})
                transdict[aaatransaction_res].update(group)
            
            # Transaction: timeouts 0, failover 0
            res = p17.match(line)
            if res:
                aaatransaction_transaction = res.group(1).lower()
                group = res.groupdict()
                transdict.setdefault(aaatransaction_transaction, {})
                transdict[aaatransaction_transaction].update({k: int(v) for k, v in group.items()})

            # Transaction: total 0, success 0, failure 0
            res = p18.match(line)
            if res:
                aaatransaction_transaction = res.group(1).lower()
                group = res.groupdict()
                transdict.setdefault(aaatransaction_transaction, {})
                transdict[aaatransaction_transaction].update({k: int(v) for k, v in group.items()})

            # Elapsed time since counters last cleared: 1h13m
            res = p19.match(line)
            if res:
                group = res.groupdict()
                serverdict.update(group)
            
            # Estimated Outstanding Access Transactions: 0
            res = p20.match(line)
            if res:
                group = '_'.join(res.group(1, 2, 3, 4)).lower()
                serverdict[group] = int(res.group(5))
            
            # Maximum Throttled Transactions: access 0, accounting 0
            res = p21.match(line)
            if res:
                max_thresold = '_'.join(res.group(1, 2, 3)).lower()
                group = res.groupdict()                        
                serverdict.setdefault(max_thresold, {})
                serverdict[max_thresold].update({k: int(v) for k, v in group.items()})

            # Consecutive Timeouts: total 0
            # Consecutive Response Failures: total 0
            res = p22.match(line)
            if res:
                conse = '_'.join(res.group(1, 2)).lower()
                conse = '_'.join(conse.split(' '))
                group = res.groupdict()
                consedict = serverdict.setdefault(conse, {})
                consedict.update({k: int(v) for k, v in group.items()})
            
            # SMD Platform : max 0, current 0 total 0
            res = p23.match(line)
            if res:
                platform_type = '_'.join(res.group(1, 2)).lower()
                group = res.groupdict()
                consedict = serverdict.setdefault(conse, {})
                platformdict = consedict.setdefault('platform_type', {}).setdefault(platform_type, {})
                platformdict.update({k: int(v) for k, v in group.items()})

            # Requests per minute past 24 hours:
            res = p24.match(line)
            if res:
                req_past = '_'.join(res.groups()).lower()
                serverdict.setdefault(req_past, {})
            
            # high - 1 hours, 13 minutes ago: 0
            res = p25.match(line)
            if res:
                low_high_type = res.group(1).lower()
                group = res.groupdict()
                serverdict.setdefault(req_past, {}).setdefault('level_type', {}).setdefault(low_high_type, {})
                serverdict[req_past]['level_type'][low_high_type].update({k: int(v) for k, v in group.items()})
            
            # average: 0
            res = p26.match(line)
            if res:
                group = res.groupdict()
                serverdict[req_past].update({k: int(v) for k, v in group.items()})

        return resultdict

 # ==================================================
# Schema for 'show aaa user all'
# ==================================================
class ShowAAAUserSchema(MetaParser):
    """Schema for show aaa user all"""

    schema = {
        'unique_id': {
            Any(): {
                Optional('accounting'): {
                    Optional('dynamicattributelist'): list,
                    Optional('events_recorded'): list,
                    Optional('outstanding_stop_records'): str,
                    'log': str,
                    Optional('update_method'): str,
                    Optional('update_interval'): int
                    },
                Optional('general'): {
                    Optional('attributelist'): list,
                    Optional('session_id'): str,
                    Optional('unique_id'): str,
                    },

                Optional('interface'): {
                    'tty_num': int,
                    'call_start': {
                        Optional('start_bytes_in'): int,
                        Optional('start_bytes_out'): int,
                        Optional('start_paks_in'): int,
                        Optional('start_paks_out'): int
                        },
                    'component': str,
                    'cumulative_counts': {
                        'bytes_in': int,
                        'bytes_out': int,
                        'paks_in': int,
                        'paks_out': int
                            },
                    'service_up':{
                        'pre_bytes_in': int,
                        'pre_bytes_out': int,
                        'pre_paks_in': int,
                        'pre_paks_out': int
                        },
                    'starttime': str,
                    'stop_received': int
                },
                Optional('kerb'): str,
                Optional('meth'): str,
                Optional('authen'): {
                    Optional('service'): str,
                    Optional('type'): str,
                    Optional('method'): str
                    },
                Optional('preauth'): str,
                Optional('peru'): str,
                Optional('debg'): str,
                Optional('radi'): str,
                Optional('service_profile'): str,
                Optional('unkn'): str,
                'id': int,
                Optional('type_0'): str,
                Optional('type_auth_proxy'): str,
                Optional('type_call'): str,
                Optional('type_cmd'): str,
                Optional('type_conn'): str,
                Optional('type_connectedapps'): str,
                Optional('type_dot1x'): str,
                Optional('type_exec'): str,
                Optional('type_identity'): str,
                Optional('type_ipsec_tunnel'): str,
                Optional('type_mcast'): str,
                Optional('type_resource'): str,
                Optional('type_rm_call'): str,
                Optional('type_rm_vpdn'): str,
                Optional('type_ssg'): str,
                Optional('type_system'): str,
                Optional('type_vpdn_tunnel'): str,
                Optional('type_vpdn_tunnel_link'): str,
                Optional('type_vrrs'): str,
                Optional('type'):{
                    Optional(Any()):{
                        'attributelist': list,
                        'method_list': str,
                        'session_id': str,
                        'start_sent': str,
                        'stop_only': str,
                        'unique_id': str,
                        'stop_has_been_sent': str,
                        'username': str
                    },
                },
            },
        }
    }

# ==================================================
# Parser for 'show aaa user all'

# ==================================================
class ShowAAAUserAll(ShowAAAUserSchema):
    """Parser for show aaa user all"""

    def cli(self, output=None):
        cli_command = 'show aaa user all'
        if output is None:
            out = self.device.execute(cli_command)
        else:
            out = output
    
        # initialize variables
        resultdict = {}
        uniquedict = {}
        accountdict = {}
        interfacedict = {}
        bytesdict = {}
        general = ''

        # Unique id 13 is currently in use.
        p1 = re.compile(r'Unique\s+(id)\s+(\d+)\s+is\s+currently\s+in\s+use\.$')

        # No data for type 0
        p2 = re.compile(r'(No)\s+(data)\s+for\s+(type)\s+(.*)$')

        # NET: Username=(n/a)
        p3 = re.compile(r'(.*)\:\s+Username\=(?P<username>(.*))$')

        # Session Id=0000137E Unique Id=00001388
        p4 = re.compile(r'(Session)\s+Id\=(?P<session_id>(\w+))\s+(Unique)\s+(Id)\=(?P<unique_id>(\w+))')

        # Start Sent=0 Stop Only=N
        p5 = re.compile(r'(Start)\s+(Sent)\=(?P<start_sent>\w+)\s+(Stop)\s+(Only)\=(?P<stop_only>\w+)')

        # stop_has_been_sent=N
        p6 = re.compile(r'(stop)_(has)_(been)_(sent)\=(?P<stop_has_been_sent>\w+)')

        # Method List=0
        p7 = re.compile(r'(Method)\s+(List)\=(?P<method_list>(.*))')

        # Attribute list:
        p8 = re.compile(r'^\s*(Attribute)\s+(list)\:')

        # 7FB04002C9C8 0 00000001 session-id(408) 4 4990(137E)
        p9 = re.compile(
            r'(\w+)\s+(\d+)\s+(\d+)\s+(.*)\s+(\d+)\s+(.*)')

        # Accounting:
        p10 = re.compile(r'(Accounting):')

        # log=0x18001
        p11 = re.compile(r'(log)\=(?P<log>\w+)')

        # Events recorded :
        p12 = re.compile(r'(Events)\s+(recorded)\s+\:')

        # update method(s) :
        p13 = re.compile(r'(update)\s+(method)\(s\)\s+\:')

        # NONE
        p14 = re.compile(r'(NONE)')

        # update interval = 0
        p15 = re.compile(r'(update)\s+(interval)\s+\=\s*(?P<update_interval>\d+)')

        # Outstanding Stop Records : 0
        p16 = re.compile(r'(Outstanding)\s+(Stop)\s+(Records)\s+\:\s*(?P<outstanding_stop_records>(.*))')

        # Dynamic attribute list:
        p17 = re.compile(r'(Dynamic)\s+(attribute)\s+(list)\:')

        # Debg: No data available
        p18 = re.compile(r'(\w+)\:\s+(No)\s+(data)\s+(available)')

        # Interface:
        p19 = re.compile(r'(Interface)\:')

        # TTY Num = 0
        p20 = re.compile(r'(TTY)\s+(Num)\s*\=\s*(?P<tty_num>(.*))')

        # Stop Received = 0
        p21 = re.compile(r'(Stop)\s+(Received)\s*\=\s*(?P<stop_received>(.*))')

        # Byte/Packet Counts till Call Start:
        p22 = re.compile(r'(Byte\/Packet)\s+(Counts)\s+(till)\s+(Call)\s+(Start)\:')

        # Pre Paks  In = 0             Pre Paks  Out = 0
        p23 = re.compile(r'(\w+)\s+(\w+)\s+(In)\s+\=\s+(\w+)\s+(\w+)\s+(\w+)\s+(Out)\s+\=\s+(\w+)')

        # Byte/Packet Counts till Service Up:
        p24 = re.compile(r'(Byte\/Packet)\s+(Counts)\s+(till)\s+(Service)\s+(Up)\:')

        # Cumulative Byte/Packet Counts :
        p25 = re.compile(r'(Cumulative)\s+(Byte\/Packet)\s+(Counts)\s+\:')

        #   Paks  In = 0             Paks  Out = 0
        p26 = re.compile(r'(\w+)\s+(In)\s+\=\s+(\w+)\s+(\w+)\s+(Out)\s+\=\s+(\w+)')

        # StartTime = 05:18:10 EDT Mar 22 2021
        p27 = re.compile(r'(StartTime)\s+\=\s*(?P<starttime>\d+\:\d+\:\d+\s+\w+\s+\w+\s+\d+\s+\d+)')

        # Component = Exec
        p28 = re.compile(r'(Component)\s+\=\s*(?P<component>\w+)')

        # Authen: service=LOGIN type=ASCII method=NONE
        p29 = re.compile(
            r'(Authen)\:\s+service\=(?P<service>\w+)\s+type\=(?P<type>\w+)\s+method\=(?P<method>\w+)')

        # Service Profile: No Service Profile data.
        p30 = re.compile(r'(\w+\s*\w*)\:\s+(No)\s+(\w+\s*\w*)\s+(data)\.')

        # General:
        p31 = re.compile(r'(General)\:$')

        # Unique Id = 00001388
        p32 = re.compile(r'(Unique)\s+(Id)\s+=\s*(?P<unique_id>(.*))')

        # Session Id = 0000137E
        p33 = re.compile(r'(Session)\s+Id\s*\=\s*(?P<session_id>(.*))')

        # Attribute List:
        p34 = re.compile(r'^\s*(Attribute)\s+(List)\:')

        outs = iter(list(out.splitlines()))
        for line in outs:
            line = line.strip()

            # Unique id 13 is currently in use.
            res = p1.match(line)
            if res:
                id_no = str(res.group(1)).strip() + '_' + str(res.group(2)).strip()
                uniquedict = resultdict.setdefault('unique_id', {}).setdefault(id_no, {})
                uniquedict['id'] = int(res.group(2))
                continue

            # No data for type 0
            res = p2.match(line)
            if res:
                data = str(res.group(1)).strip().lower() + '_' + str(res.group(2)).strip().lower()
                type = str(res.group(3)).strip().lower() + '_' + str(res.group(4)).strip().replace(" ", "_").replace("-", "_").lower()
                uniquedict[type] = data
                continue

            # NET: Username=(n/a)
            res = p3.match(line)
            if res:
                net = str(res.group(1)).strip().lower()
                group = res.groupdict()
                uniquedict.setdefault('type', {}).setdefault(net, {})
                uniquedict['type'][net].update(group)
                continue

            # Session Id=0000137E Unique Id=00001388
            res = p4.match(line)
            if res:
                group = res.groupdict()
                uniquedict['type'][net].update(group)
                continue

            # Start Sent=0 Stop Only=N
            res = p5.match(line)
            if res:
                group = res.groupdict()
                uniquedict['type'][net].update(group)

            # stop_has_been_sent=N
            res = p6.match(line)
            if res:
                group = res.groupdict()
                uniquedict['type'][net].update(group)

            # Method List=0
            res = p7.match(line)
            if res:
                group = res.groupdict()
                uniquedict['type'][net].update(group)

            # Attribute list:
            res = p8.match(line)
            if res:
                net_att = str(res.group(1)).strip().lower() + str(res.group(2)).strip()
                uniquedict['type'][net].setdefault(net_att, {})
                list1 = []
                for i in range(10):
                    p = next(outs)
                    p = p.strip()
                    # 7FB04002C9C8 0 00000001 session-id(408) 4 4990(137E)
                    ma = p9.match(p)
                    if ma:
                        list1.append(ma.groups())
                    else:
                        break
                uniquedict['type'][net][net_att] = list1

            # Accounting:
            res = p10.match(line)
            if res:
                account = str(res.group(1)).strip().lower()
                accountdict = uniquedict.setdefault(account, {})

            # log=0x18001
            res = p11.match(line)
            if res:
                group = res.groupdict()
                accountdict.update(group)

            # Events recorded :
            res = p12.match(line)
            if res:
                event_rec = str(res.group(1)).lower().strip() + '_' + str(res.group(2)).strip()
                accountdict.setdefault(event_rec, {})
                list2 = []
                for i in range(10):
                    p = next(outs)
                    p = p.strip()
                    # update method(s) :
                    ma = p13.match(p)
                    if ma:
                        update_method = 'update_method'
                        accountdict.setdefault(update_method,{})
                        break
                    else:
                        list2.append(p.strip().lower())
                accountdict[event_rec] = list2
                continue

            # update method(s) :
            res = p13.match(line)
            if res:
                update_method = 'update_method'
                accountdict.setdefault(update_method, {})

            # NONE
            res = p14.match(line)
            if res and 'update_method' in accountdict:
                update_method_data = str(res.group(0)).strip()
                accountdict[update_method] = update_method_data

            # update interval = 0
            res = p15.match(line)
            if res:
                group = res.groupdict()
                accountdict.update({k: int(v) for k, v in group.items()})

            # Outstanding Stop Records : 0
            res = p16.match(line)
            if res:
                group = res.groupdict()
                accountdict.update(group)

            # Dynamic attribute list:
            res = p17.match(line)
            if res:
                dynamic_att = str(res.group(1)).strip().lower() + str(res.group(2)).strip() + str(
                    res.group(3)).strip()
                list1 = []
                accountdict.setdefault(dynamic_att, {})
                for i in range(10):
                    p = next(outs)
                    p = p.strip()
                    ma = p9.match(p)
                    if ma:
                        list1.append(ma.groups())
                    else:
                        # Debg: No data available
                        res = p18.match(p)
                        if res:
                            types = str(res.group(1)).strip().replace("-", "_").lower()
                            types = "_".join(types.split(" "))
                            data = str(res.group(2))+'_'+str(res.group(3))
                            uniquedict.setdefault(types, {})
                            uniquedict[types] = data

                        break
                accountdict[dynamic_att] = list1

            # Debg: No data available
            res = p18.match(line)
            if res:
                if "-" in str(res.group(1)):
                    types = str(res.group(1)).strip().replace("-", "_").lower()
                else:
                    types = str(res.group(1)).strip().lower()

                types = "_".join(types.split(" "))
                data = 'no_data'
                uniquedict.setdefault(types, {})
                uniquedict[types] = data

            # Interface:
            res = p19.match(line)
            if res:
                interface = str(res.group(1)).lower()
                interfacedict = uniquedict.setdefault(interface, {})

            # TTY Num = 0
            res = p20.match(line)
            if res:
                group = res.groupdict()
                interfacedict.update({k: int(v) for k, v in group.items()})

            # Stop Received = 0
            res = p21.match(line)
            if res:
                group = res.groupdict()
                interfacedict.update({k: int(v) for k, v in group.items()})

            # Byte/Packet Counts till Call Start:
            res = p22.match(line)
            if res:
                byte_packets = str(res.group(4)).strip().lower() + '_' + str(res.group(5)).strip().lower()
                bytepacketdict = interfacedict.setdefault(byte_packets, {})

            # Pre Paks  In = 0             Pre Paks  Out = 0
            res = p23.match(line)
            if res:
                if 'interface' in uniquedict.keys():
                    bytes_in = str(res.group(1)).strip().lower()+ '_' + str(res.group(2)).strip().lower() + '_' + str(
                        res.group(3)).strip().lower()
                    bytes_out = str(res.group(5)).strip().lower() + '_' + str(res.group(6)).strip().lower()+ '_' + str(
                        res.group(7)).strip().lower()
                if 'service_up' in interfacedict:
                    interfacedict['service_up'].update(
                        {bytes_in: int(res.group(4)), bytes_out: int(res.group(8))})
                else:
                    bytepacketdict.update(
                        {bytes_in: int(res.group(4)), bytes_out: int(res.group(8))})

            # Byte/Packet Counts till Service Up:
            res = p24.match(line)
            if res:
                if 'interface' in uniquedict.keys():
                    byte_packets = str(res.group(4)).strip().lower() + '_' + str(res.group(5)).strip().lower()
                    interfacedict.setdefault(byte_packets, {})

            # Cumulative Byte/Packet Counts :
            res = p25.match(line)
            if res:
                if 'interface' in uniquedict.keys():
                    bytes = str(res.group(1)).strip().lower()+ '_' + str(res.group(3)).strip().lower()
                    bytesdict = interfacedict.setdefault(bytes, {})

            # Paks  In = 0             Paks  Out = 0
            res = p26.match(line)
            if res:
                if 'interface' in uniquedict.keys():
                    bytes_in = str(res.group(1)).strip().lower()+ '_' + str(res.group(2)).strip().lower()
                    bytes_out = str(res.group(4)).strip().lower()+ '_' + str(res.group(5)).strip().lower()
                    bytesdict.update({bytes_in: int(res.group(3)), bytes_out: int(res.group(6))})

            # StartTime = 05:18:10 EDT Mar 22 2021
            res = p27.match(line)
            if res:
                if 'interface' in uniquedict.keys():
                    group = res.groupdict()
                    interfacedict.update(group)

            # Component = Exec
            res = p28.match(line)
            if res:
                if 'interface' in uniquedict.keys():
                    group = res.groupdict()
                    interfacedict.update(group)

            # Authen: service=LOGIN type=ASCII method=NONE
            res = p29.match(line)
            if res:
                authen = res.group(1).lower()
                uniquedict.setdefault(authen, {})
                group = res.groupdict()
                uniquedict[authen].update(group)

            # Service Profile: No Service Profile data.
            res = p30.match(line)
            if res:
                if "-" in str(res.group(1)):
                    types = str(res.group(1)).strip().replace("-", "_").lower()
                else:
                    types = str(res.group(1)).strip().lower()

                types = "_".join(types.split(" "))
                data = 'No_data'
                uniquedict.setdefault(types, {})
                uniquedict[types] = data

            # General:
            res = p31.match(line)
            if res:
                general = str(res.group(1)).strip().lower()
                uniquedict.setdefault(general, {})

            # Unique Id = 00001388
            res = p32.match(line)
            if res:
                if general in uniquedict.keys():
                    group = res.groupdict()
                    uniquedict[general].update(group)

            # Session Id = 0000137E
            res = p33.match(line)
            if res:
                if general in uniquedict.keys():
                    group = res.groupdict()
                    uniquedict[general].update(group)

            # Attribute List:
            res = p34.match(line)
            if res:
                gen_att = str(res.group(1)).strip().lower() + str(res.group(2)).strip().lower()
                uniquedict[general].setdefault(gen_att, {})
                list1 = []
                for i in range(10):
                    p = next(outs)
                    p = p.strip()
                    ma = p9.match(p)
                    if ma:
                        list1.append(ma.groups())
                    else:
                        res = p18.match(p)
                        if res:
                            types = str(res.group(1)).strip().replace("-", "_").lower()
                            types = "_".join(types.split(" "))
                            data = 'no_data'
                            uniquedict.setdefault(types, {})
                            uniquedict[types] = data
                        break
                uniquedict[general][gen_att] = list1

        return resultdict

# ====================================================
#  Schema for show aaa fqdn all
# ====================================================
class ShowAaaFqdnAllSchema(MetaParser):
    schema = {
        'fqdn_name': {
            Any(): {
               'protocol': str,
               'ipv4s': str,
               'ipv6s': str,
                'groups': str,
            },
        }
    }

# ====================================================
#  Parser for show aaa fqdn all
# ====================================================
class ShowAaaFqdnAll(ShowAaaFqdnAllSchema):
    """
    Parser for show aaa fqdn all
    """

    def cli(self, output=None):

        cmd = 'show aaa fqdn all'

        # FQDN Name : fqdnname
        p1 = re.compile(r'(^FQDN\s+Name)\s*:\s*(.*)')
        # Protocol  : RADIUS
        # IPv4s     : 11.15.24.213
        # IPv6s     :
        # Groups    : FQDNNAME radius
        p2 = re.compile(r'(\w+)\s*:\s*(.*)')

        ret_dict = {}
        fqdn_dict = {}

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        for line in out.splitlines():
            line = line.strip()

            # FQDN Name : fqdnname
            res = p1.match(line)
            if res:
                fqdn_dict = ret_dict.setdefault('fqdn_name', {}).setdefault(res.group(2), {})

            # IPv4s     : 11.15.24.213
            # IPv6s     :
            # Groups    : FQDNNAME radius
            res = p2.match(line)
            if res:
                fqdn_dict.update({res.group(1).lower(): res.group(2)})

# ====================================================
#  Schema for show aaa cache group
# ====================================================
class ShowAAACacheGroupSchema(MetaParser):
    """Schema for 'show aaa cache group {server_grp} all'
                  'show aaa cache group {server_grp} profile {profile}'
    """
    schema = {
        'client': {
            Any(): {
                'mac_address': str,
                'profile_name': str,
                'user_name': str,
                'timeout': int
            }
        },
        Optional('total_entries'): int,
    }



# ====================================================
#  Parser for show aaa cache group
# ====================================================
class ShowAAACacheGroup(ShowAAACacheGroupSchema):
    """Parser for 'show aaa cache group {server_grp} all'
                  'show aaa cache group {server_grp} profile {profile}'
    """

    cli_command = [
        'show aaa cache group {server_grp} all',
        'show aaa cache group {server_grp} profile {profile}'
    ]

    def cli(self, server_grp=None, profile=None, output=None):

        # Get output by executing cmd on device
        if output is None:
            if profile:
                cmd = self.cli_command[1].format(server_grp=server_grp,profile=profile)
            else:
                cmd = self.cli_command[0].format(server_grp=server_grp)

            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}
        client_dict = {}

        # MAC ADDR:      000A.0A00.0500
        mac_compile = re.compile(r'MAC ADDR:[\s\t]+(?P<macAddr>\w+\.\w+\.\w+)')
        # Profile Name: regProfile
        profile_compile = re.compile(r'Profile Name:[\s\t]+(?P<profile>[0-9A-Za-z\-\.]+)')
        # User Name:    	test
        user_compile = re.compile(r'User Name:[\s\t]+(?P<user>[0-9A-Za-z\-\.]+)')
        # Timeout:      	86400
        timeout_compile = re.compile(r'Timeout:[\s\t]+(?P<timeout>\w+)')
        # Total number of Cache entries is 2
        total_entries = re.compile(r'Total number of Cache entries is[\s\t]+(?P<count>[0-9]+)')
        for line in output.splitlines():
            line = line.strip()

            # MAC ADDR:      000A.0A00.0500
            m1 = mac_compile.match(line)
            if m1:
                group = m1.groupdict()
                mac = group['macAddr']
                client_dict = ret_dict.setdefault('client', {}).setdefault(mac, {})
                client_dict['mac_address'] = mac
                continue

            # Profile Name: regProfile
            m2 = profile_compile.match(line)
            if m2:
                group = m2.groupdict()
                profile_name = group['profile']
                client_dict['profile_name'] = profile_name
                continue

            # User Name:    	test
            m3 = user_compile.match(line)
            if m3:
                group = m3.groupdict()
                profile_name = group['user']
                client_dict['user_name'] = profile_name

            # Timeout:      	86400
            m3 = timeout_compile.match(line)
            if m3:
                group = m3.groupdict()
                timeout = group['timeout']
                client_dict['timeout'] = int(timeout)
                continue

            # Total number of Cache entries is 2
            m5 = total_entries.match(line)
            if m5:
                count = int(m5.groupdict()['count'])
                ret_dict.update({'total_entries': count})
                continue
        return ret_dict
        

# ================================================================
# Schema for 'show aaa common-criteria policy name {policy_name}'
# ================================================================
class ShowAAACommonCriteraPolicySchema(MetaParser):
    """Schema for show aaa common-criteria policy name {policy_name}"""

    schema = {
                'policy_name': str,
                Optional('minimum_length'): int,
                Optional('maximum_length'): int,
                Optional('upper_count'): int,
                Optional('lower_count'): int,
                Optional('numeric_count'): int,
                Optional('special_count'): int,
                Optional('character_changes'): int,
                Optional('lifetime'): {
                    Optional('years'): int,
                    Optional('months'): int,
                    Optional('days'): int,
                    Optional('hours'): int,
                    Optional('minutes'): int,
                    Optional('seconds'): int
                    }
             }

# ==============================================================
#  Parser for show aaa common-criteria policy name {policy_name}
# ==============================================================
class ShowAAACommonCriteraPolicy(ShowAAACommonCriteraPolicySchema):
    """
    Parser for show aaa common-criteria policy name {policy_name}
    """

    cli_command = 'show aaa common-criteria policy name {policy_name}'
    def cli(self, policy_name, output=None):
        cmd = self.cli_command.format(policy_name=policy_name)
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # Policy name: enable_1
        p1 = re.compile(r'^Policy name\: +(?P<policy_name>\S+\d+)$')

        # Minimum length: 10
        # Maximum length: 128
        p2 = re.compile(r'^(?P<length_key>\S+) length\: +(?P<len>\d+)$')

        # Upper Count: 0
        # Lower Count: 0
        # Numeric Count: 0
        # Special Count: 0
        p3 = re.compile(r'^(?P<count_key>\S+) Count\: +(?P<count>\d+)$')

        # Number of character changes 4
        p4 = re.compile(r'^Number of character changes +(?P<char_changes>\d+)$')

        # Valid forever. User tied to this policy will not expire
        p5 = re.compile(r'^Valid for +(?P<time>(.*))$')

        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()
            
            # Policy name: enable_1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["policy_name"] = group["policy_name"]
            
            # Minimum length: 10
            # Maximum length: 128
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[group["length_key"].lower()+"_"+"length"] = int(group["len"])
            
            # Upper Count: 0
            # Lower Count: 0
            # Numeric Count: 0
            # Special Count: 0
            m = p3.match(line) 
            if m:
                group = m.groupdict()
                ret_dict[group["count_key"].lower()+"_"+"count"] = int(group["count"])
            
            # Number of character changes 4
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["character_changes"] = int(group["char_changes"])
            
            # Valid forever. User tied to this policy will not expire
            m = p5.match(line)
            if m:
                lifetime_dict = ret_dict.setdefault('lifetime', {})
                group = m.groupdict()
                words = group["time"].split()
                grouped_words = [' '.join(words[i: i + 2]) for i in range(0, len(words), 2)]
                for val in grouped_words:
                    lifetime_dict[val.split()[1]] = int(val.split()[0])
        return ret_dict

