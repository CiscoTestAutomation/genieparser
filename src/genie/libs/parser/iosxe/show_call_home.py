import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

# ==========================================================================================
# Parser Schema for 'show call-home version'
# ==========================================================================================

class ShowCallHomeVersionSchema(MetaParser):
    """
    Schema for
        * 'show call-home version'
    """

    schema = {
        'call_home_version': str,
        'component_version': {
            'call_home': str,
            'eem_call_home': str,
        }
    }

# ==========================================================================================
# Parser for 'show call-home version'
# ==========================================================================================

class ShowCallHomeVersion(ShowCallHomeVersionSchema):
    """
    Parser for
        * 'show call-home version'
    """
    cli_command = ['show call-home version']

    def cli(self, output=None):
        cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(self.cli_command[0])

        ret_dict = {}
        # Call-Home Version 3.0
        p1 = re.compile(r'^Call-Home Version (?P<version>\S+)$')

        # call-home: UNKNOWN
        p2 = re.compile(r'^call-home:\s(?P<comp_ver_call_home>\S+)$')

        # eem-call-home: UNKNOWN
        p3 = re.compile(r'^eem-call-home:\s(?P<comp_ver_eem_call_home>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Call-Home Version 3.0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['call_home_version'] = group['version']
                continue

            # call-home: UNKNOWN
            m = p2.match(line)
            if m:
                ret_dict.setdefault('component_version',{})
                group = m.groupdict()
                ret_dict['component_version']\
                    ['call_home'] = group['comp_ver_call_home'].lower()
                continue

            # eem-call-home: UNKNOWN
            m = p3.match(line)
            if m:
                ret_dict.setdefault('component_version',{})
                group = m.groupdict()
                ret_dict['component_version']\
                    ['eem_call_home'] = group['comp_ver_eem_call_home'].lower()
                continue

        return ret_dict

# ==========================================================================================
# Parser Schema for 'show call-home smart-licensing'
# ==========================================================================================

class ShowCallHomeSmartLicensingSchema(MetaParser):
    """
    Schema for
        * 'show call-home smart-licensing'
    """

    schema = {
        'smart_licensing_settings': {
            'smart_license_messages': str,
            'profile': str,
            'status': str,
            'destination_url': str,
        }
    }

# ==========================================================================================
# Parser for 'show call-home smart-licensing'
# ==========================================================================================

class ShowCallHomeSmartLicensing(ShowCallHomeSmartLicensingSchema):
    """
    Parser for
        * 'show call-home smart-licensing'
    """
    cli_command = ['show call-home smart-licensing']

    def cli(self, output=None):
        cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(self.cli_command[0])
        
        # initializing dictionary
        ret_dict = {}

        # Smart-license messages: enabled
        p1 = re.compile(r'^\s*Smart-license messages: (?P<msg>\S+)$')

        # Profile: CiscoTAC-1 (status: ACTIVE)
        p2 = re.compile(r'^\s*Profile: (?P<profile>[\w\S ]+) \(status: (?P<status>\S+)\)$')

        # Destination  URL(s):  https://tools.cisco.com/its/service/oddce/services/DDCEService
        p3 = re.compile(r'^\s*Destination  URL\(s\):\s*(?P<url>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Smart-license messages: enabled
            m = p1.match(line)
            if m:
                ret_dict.setdefault('smart_licensing_settings',{})
                group = m.groupdict()
                ret_dict['smart_licensing_settings']\
                    ['smart_license_messages'] = group['msg']
                continue

            # Profile: CiscoTAC-1 (status: ACTIVE)
            m = p2.match(line)
            if m:
                ret_dict.setdefault('smart_licensing_settings',{})
                group = m.groupdict()
                ret_dict['smart_licensing_settings']['profile'] = group['profile']
                ret_dict['smart_licensing_settings']['status'] = group['status']
                continue

            # Destination  URL(s):  https://tools.cisco.com/its/service/oddce/services/DDCEService
            m = p3.match(line)
            if m:
                ret_dict.setdefault('smart_licensing_settings',{})
                group = m.groupdict()
                ret_dict['smart_licensing_settings']['destination_url'] = group['url']
                continue

        return ret_dict

# ==========================================================================================
# Parser Schema for 'show call-home profile all'
# ==========================================================================================

class ShowCallHomeProfileAllSchema(MetaParser):
    """
    Schema for
        * 'show call-home profile all'
    """

    schema = {
        'profile': {
            'name':{
                Any():{
                    'status': str,
                    'mode': str,
                    'reporting_data': str,
                    'preferred_message_format': str,
                    'message_size_limit_in_bytes': int,
                    'transport_method': str,
                    Optional ('email_address'): str,
                    Optional ('http_address'): str,
                    Optional ('other_address'): str,
                    Optional ('periodic_info'):{
                        Optional (Any()):{
                            Optional ('scheduled') : str,
                            Optional ('time'): str,
                        }
                    },
                    Optional ('group_pattern'):{
                        Any():{
                            'severity': str,
                        }
                    }
                }
            }
        }
    }

# ==========================================================================================
# Parser for 'show call-home Profile all'
# ==========================================================================================

class ShowCallHomeProfileAll(ShowCallHomeProfileAllSchema):
    """
    Parser for
        * 'show call-home profile all'
    """
    cli_command = ['show call-home profile all']

    def cli(self, output=None):
        cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(self.cli_command[0])
        
        # initializing dictionary
        ret_dict = {}

        # Profile Name: CiscoTAC-1
        p1 = re.compile(r'^Profile Name: (?P<name>[\S\s]+)$')

        # Profile status: ACTIVE
        p2 = re.compile(r'^Profile status: (?P<status>\S+)$')

        # Profile mode: Full Reporting
        p3 = re.compile(r'^Profile mode: (?P<mode>[\w\s]+)$')

        # Reporting Data: Smart Call Home, Smart Licensing
        p4 = re.compile(r'^Reporting Data: (?P<reporting_data>[\S\s]+)$')

        # Preferred Message Format: xml
        p5 = re.compile(r'^Preferred Message Format: (?P<msg_format>[\w\s]+)$')

        # Message Size Limit: 3145728 Bytes
        p6 = re.compile(r'^Message Size Limit: (?P<size_limit>[\d]+) Bytes+$')

        # Transport Method: http
        p7 = re.compile(r'^Transport Method: (?P<method>\S+)$')

        # HTTP  address: https://tools.cisco.com/its/service/oddce/services/DDCEService
        p8 = re.compile(r'^HTTP  address: (?P<http_address>\S+)$')

        #Email address(es): shishir@cisco.com
        p9 = re.compile(r'^Email address\(es\): (?P<email>[\S\s]+)$')

        #                Shisihir213@cisco.com
        p10 = re.compile(r'^ *(?P<other_email>\S+\@\S+\.\S+)$')

        # Other address(es): default
        p11 = re.compile(r'^Other address\(es\): (?P<other_address>\S+)$')

        # Periodic configuration info message is scheduled every 1 day of the month at 09:15
        # Periodic inventory info message is scheduled daily at 00:00
        p12 = re.compile(r'^Periodic (?P<type>\S+) info message is scheduled (?P<frequency>[\w\s]+) at (?P<time>\S+)$')
        
        # Alert-group               Severity
        # ------------------------  ------------
        # crash                     debugging   
        # diagnostic                minor       
        # environment               warning     
        # inventory                 normal      
        p13 = re.compile(r'^(?P<group_pattern>(?!.*--)[\S]+) +(?P<severity>\S+) *$')
        
        for line in output.splitlines():
            line = line.strip()

            # Profile Name: CiscoTAC-1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('profile',{}).setdefault('name',{}).setdefault(group['name'],{})
                continue
            
            # Profile status: ACTIVE
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict['status'] = group['status']
                continue

            # Profile mode: Full Reporting
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict['mode'] = group['mode']
                continue

            # Reporting Data: Smart Call Home, Smart Licensing
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict['reporting_data'] = group['reporting_data']
                continue

            # Preferred Message Format: xml
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict['preferred_message_format'] = group['msg_format']
                continue

            # Message Size Limit: 3145728 Bytes
            m = p6.match(line)
            if m:
                group = m.groupdict()
                root_dict['message_size_limit_in_bytes'] = int(group['size_limit'])
                continue

            # Transport Method: http
            m = p7.match(line)
            if m:
                group = m.groupdict()
                root_dict['transport_method'] = group['method']
                continue

            # HTTP  address: https://tools.cisco.com/its/service/oddce/services/DDCEService
            m = p8.match(line)
            if m:
                group = m.groupdict()
                root_dict['http_address'] = group['http_address']
                continue

            # Email address(es): shishir@cisco.com
            m = p9.match(line)
            if m:
                group = m.groupdict()
                root_dict['email_address'] = group['email']
                continue

            #                Shisihir213@cisco.com
            m = p10.match(line)
            if m:
                group = m.groupdict()
                root_dict['email_address'] = root_dict['email_address'] + ',' + group['other_email']
                continue

            # Other address(es): default
            m = p11.match(line)
            if m:
                group = m.groupdict()
                root_dict['other_address'] = group['other_address']
                continue

            # Periodic configuration info message is scheduled every 1 day of the month at 09:15
            m = p12.match(line)
            if m:
                group = m.groupdict()
                info_dict = root_dict.setdefault('periodic_info',{}).setdefault(group['type'],{})
                info_dict['scheduled'] = group['frequency']
                info_dict['time'] = group['time']
                continue

            # Alert-group               Severity
            # crash                     debugging 
            m = p13.match(line)
            if m:
                group = m.groupdict()
                group_dict = root_dict.setdefault('group_pattern',{}).setdefault(group['group_pattern'],{})
                group_dict['severity'] = group['severity']
                continue

        return ret_dict

# ==========================================================================================
# Parser Schema for 'show call-home statistics'
# ==========================================================================================

class ShowCallHomeStatisticsSchema(MetaParser):
    """
    Schema for
        * 'show call-home statistics'
    """

    schema = {
        'msg_type': {
            Any():{
                'msg_total': int,
                'msg_email': int,
                'msg_http': int,
                'type': {
                    Any():{
                        'total': int,
                        'email': int,
                        'http': int,
                    }
                }
            }
        },
        'msg_sent_time': str
    }

# ==========================================================================================
# Parser for 'show call-home Statistics'
# ==========================================================================================

class ShowCallHomeStatistics(ShowCallHomeStatisticsSchema):
    """
    Parser for
        * 'show call-home statistics'
    """
    cli_command = ['show call-home statistics']

    def cli(self, output=None):
        cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(self.cli_command[0])
        
        # initializing dictionary
        ret_dict = {}

        # Total Success   0                    0                    0
        p1 = re.compile(r'^Total (?P<msg_type>[-\w]+) *(?P<msg_total>\d+) +(?P<msg_email>\d+) +(?P<msg_http>\d+)$')
        
        # Config      0                    0                    0
        p2 = re.compile(r'^(?P<type>[-\w]+) *(?P<total>\d+) +(?P<email>\d+) +(?P<http>\d+)$')
        
        # Last call-home message sent time: n/a
        p3 = re.compile(r'^Last call-home message sent time: (?P<time>.+) *$')

        for line in output.splitlines():
            line = line.strip()
            if ("Total Ratelimit" in line):
                continue
            if ("-dropped" in line):
                line = "Total Ratelimit" + line
            
            # Total Success   0                    0                    0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group['msg_type'] = 'Total ' + group['msg_type']
                root_dict = ret_dict.setdefault('msg_type',{}).setdefault(group['msg_type'],{})
                root_dict['msg_total'] = int(group['msg_total'])
                root_dict['msg_email'] = int(group['msg_email'])
                root_dict['msg_http'] = int(group['msg_http'])
                continue

            # Config      0                    0                    0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                det_dict = root_dict.setdefault('type',{}).setdefault(group['type'],{})
                det_dict['total'] = int(group['total'])
                det_dict['email'] = int(group['email'])
                det_dict['http'] = int(group['http'])
                continue

            # Last call-home message sent time: n/a
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['msg_sent_time'] = group['time']
                continue

        return ret_dict
		
# ==========================================================================================
# Parser Schema for 'show call-home mail-server status'
# ==========================================================================================

class ShowCallHomeMailServerStatusSchema(MetaParser):
    """
    Schema for
        * 'show call-home mail-server status'
    """

    schema = {
        'mail_server': {
            Any():{
                Optional ('address'): str,
                Optional ('priority'): int,
                Optional ('secure'): str,
            }
        }
    }

# ==========================================================================================
# Parser for 'show call-home mail-server status'
# ==========================================================================================

class ShowCallHomeMailServerStatus(ShowCallHomeMailServerStatusSchema):
    """
    Parser for
        * 'show call-home mail-server status'
    """
    cli_command = ['show call-home mail-server status']

    def cli(self, output=None):
        cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(self.cli_command[0])
        
        # initializing dictionary
        ret_dict = {}

        #     Mail-server[1]: Address: ott-ads-035 Priority: 1  Secure: none [Not Available]
        p1 = re.compile(r'^(?P<mail_server_id>\S+):( +Address:\s(?P<address>\S+))*( +Priority: (?P<priority>\d+))*( +Secure: (?P<secure>.*))*$')
        for line in output.splitlines():
            line = line.strip()
            if 'No mail server' in line:
                ret_dict.setdefault('mail_server',{})
                break
            else:
                # Mail-server[1]: Address: ott-ads-035 Priority: 1  Secure: none [Not Available]
                m = p1.match(line)
                if m:
                    group = m.groupdict()
                    root_dict = ret_dict.setdefault('mail_server',{}).setdefault(group['mail_server_id'],{})
                    root_dict['address'] = group['address']
                    root_dict['priority'] = int(group['priority'])
                    root_dict['secure'] = group['secure']
                    continue

        return ret_dict

# ==========================================================================================
# Parser Schema for 'show call-home'
# ==========================================================================================

class ShowCallHomeSchema(MetaParser):
    """
    Schema for
        * 'show call-home'
    """

    schema = {
        'current_call_home_settings': {
            'call_home_feature': str,
            'msg_from_address': str,
            'msg_reply_to_address': str,
            'vrf_for_msg': str,
            'contact_person_email': str,
            'contact_person_phone': str,
            'street_address': str,
            'customer_id': str,
            'contract_id': str,
            'site_id': str,
            'source_ip_address': str,
            'source_interface': str,
            'mail_server':{
                Any(): {
                    Optional('address'): str,
                    Optional('priority'): int,
                    Optional('secure'): str,
                }
            },
            'http_proxy': str,
            'http_secure': {
                'server_identity_check': str,
            },
            'http_resolve_hostname': str,
            'diagnostic_signature': str,
            'profile': {
                Any():{
                    'status': str,
                }
            },
            'smart_licensing_msg': str,
            'aaa_authorization': str,
            'aaa_authorization_username': str,
            'data_privacy': str,
            'syslog_throttling': str,
            'Rate_limit_msg_per_min': int,
            'snapshot_command': str,
        },
        'available_alert_group': {
            'keyword':{
                Any(): {
                    'state': str,
                    'description': str,
                }
            } 
        },
        'profiles': {
            'name': str
        }
    }

# ==========================================================================================
# Parser for 'show call-home'
# ==========================================================================================

class ShowCallHome(ShowCallHomeSchema):
    """
    Parser for
        * 'show call-home'
    """
    cli_command = 'show call-home'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # initializing dictionary
        ret_dict = {}

        # call home feature : enable
        p1 = re.compile(r'^call home feature : (?P<feature>\w+)$')

        # call home message's from address: Not yet set up
        p2 = re.compile(r'^call home message\'s from address: (?P<from>[\w\s]+)$')

        # call home message's reply-to address: Not yet set up
        p3 = re.compile(r'^call home message\'s reply-to address: (?P<reply_to>[\w\s]+)$')

        # vrf for call-home messages: Not yet set up
        p4 = re.compile(r'^vrf for call-home messages: (?P<vrf>[\w\s]+)$')

        # contact person's email address: test@test.com
        p5 = re.compile(r'^contact person\'s email address: (?P<email>[\S\s]+)$')

        # contact person's phone number: Not yet set up
        p6 = re.compile('^contact person\'s phone number: (?P<phone>[\w\s\@\.]+)$')

        #  street address: test
        p7 = re.compile('^street address: (?P<street>[\w\s]+)$')

        # customer ID: Not yet set up
        p8 = re.compile('^customer ID: (?P<customer_id>[\w\s]+)$')

        # contract ID: Not yet set up
        p9 = re.compile('^contract ID: (?P<contract_id>[\w\s]+)$')

        # site ID: test
        p10 = re.compile('^site ID: (?P<site_id>[\w\s]+)$')

        # source ip address: Not yet set up
        p11 = re.compile('^source ip address: (?P<ip_add>[\w\s]+)$')

        # source interface: Not yet set up
        p12 = re.compile('^source interface: (?P<interface>[\w\s]+)$')

        # Mail-server[1]: Address: test_add Priority: 1  Secure: none
        p13 = re.compile(r'^(?P<mail_server_id>\S+): (Address: (?P<address>[\w\S]+)) (Priority: (?P<priority>\S+)) (Secure: (?P<secure>[\w\S]+))*')

        # http proxy: Not yet set up
        p14 = re.compile('^http proxy: (?P<proxy>[\w\s]+)$')

        # server identity check: enabled
        p15 = re.compile('^server identity check: (?P<identity_check>[\w\s]+)$')

        # http resolve-hostname: default
        p16 = re.compile('^http resolve-hostname: (?P<hostname>[\w\s]+)$')

        # Diagnostic signature: enabled
        p17 = re.compile('^Diagnostic signature: (?P<signature>[\w\s]+)$')

        # Profile: Test (status: ACTIVE)
        p18 = re.compile('^Profile: (?P<profile>[\w\S]+) \(status: (?P<status>[\w\s]+)\)$')

        # Smart licensing messages: enabled
        p19 = re.compile('^Smart licensing messages: (?P<smart_licensing>[\w\s]+)$')

        # aaa-authorization: disable
        p20 = re.compile('^aaa-authorization: (?P<aaa_auth>[\w\s]+)$')

        # aaa-authorization username: test
        p21 = re.compile('^aaa-authorization username: (?P<username>[\S\s]+)$')

        # data-privacy: normal
        p22 = re.compile('^data-privacy: (?P<privacy>[\w\s]+)$')

        # syslog throttling: enable
        p23 = re.compile('^syslog throttling: (?P<throttling>[\w\s]+)$')

        # Rate-limit: 1 message(s) per minute
        p24 = re.compile('^Rate-limit: (?P<rate_limit>\d+) message\(s\) per minute$')

        # Snapshot command: Not yet set up
        p25 = re.compile('^Snapshot command: (?P<cmd>[\w\s]+)$')

        # configuration            Enable  configuration info
        p26 = re.compile('^(?P<keyword>\w+) *(?P<state>\w+) *(?P<description>[\w\ ]+)$')

        # Profile Name: Test
        p27 = re.compile('^Profile Name: (?P<name>[\S]+)$')

        # Inititalizing a variable : name
        name = ""

        for line in output.splitlines():
            line = line.strip()

            # call home feature : enable
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('current_call_home_settings',{})
                root_dict['call_home_feature'] = group['feature']
                continue

            # call home message's from address: Not yet set up
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict['msg_from_address'] = group['from']
                continue

            # call home message's reply-to address: Not yet set up
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict['msg_reply_to_address'] = group['reply_to']
                continue

            # vrf for call-home messages: Not yet set up
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict['vrf_for_msg'] = group['vrf']
                continue

            # contact person's email address: test@test.com
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict['contact_person_email'] = group['email']
                continue

            # contact person's phone number: Not yet set up
            m = p6.match(line)
            if m:
                group = m.groupdict()
                root_dict['contact_person_phone'] = group['phone']
                continue

            #  street address: test
            m = p7.match(line)
            if m:
                group = m.groupdict()
                root_dict['street_address'] = group['street']
                continue

            # customer ID: Not yet set up
            m = p8.match(line)
            if m:
                group = m.groupdict()
                root_dict['customer_id'] = group['customer_id']
                continue

            # contract ID: Not yet set up
            m = p9.match(line)
            if m:
                group = m.groupdict()
                root_dict['contract_id'] = group['contract_id']
                continue

            # site ID: test
            m = p10.match(line)
            if m:
                group = m.groupdict()
                root_dict['site_id'] = group['site_id']
                continue

            # source ip address: Not yet set up
            m = p11.match(line)
            if m:
                group = m.groupdict()
                root_dict['source_ip_address'] = group['ip_add']
                continue

            # source interface: Not yet set up
            m = p12.match(line)
            if m:
                group = m.groupdict()
                root_dict['source_interface'] = group['interface']
                continue

            # Mail-server[1]: Address: test_add Priority: 1  Secure: none
            m = p13.match(line)
            if m:
                group = m.groupdict()
                server_dict = root_dict.setdefault('mail_server',{}).setdefault(group['mail_server_id'],{})
                server_dict['address'] = group['address']
                server_dict['priority'] = int(group['priority'])
                server_dict['secure'] = group['secure']
                continue

            # http proxy: Not yet set up
            m = p14.match(line)
            if m:
                group = m.groupdict()
                root_dict['http_proxy'] = group['proxy']
                continue

            # server identity check: enabled
            m = p15.match(line)
            if m:
                group = m.groupdict()
                http_dict = root_dict.setdefault('http_secure',{})
                http_dict['server_identity_check'] = group['identity_check']
                continue

            # http resolve-hostname: default
            m = p16.match(line)
            if m:
                group = m.groupdict()
                root_dict['http_resolve_hostname'] = group['hostname']
                continue

            # Diagnostic signature: enabled
            m = p17.match(line)
            if m:
                group = m.groupdict()
                root_dict['diagnostic_signature'] = group['signature']
                continue

            # Profile: Test (status: ACTIVE)
            m = p18.match(line)
            if m:
                group = m.groupdict()
                profile_dict = root_dict.setdefault('profile',{}).setdefault(group['profile'],{})
                profile_dict['status'] = group['status']
                continue

            # Smart licensing messages: enabled
            m = p19.match(line)
            if m:
                group = m.groupdict()
                root_dict['smart_licensing_msg'] = group['smart_licensing']
                continue

            # aaa-authorization: disable
            m = p20.match(line)
            if m:
                group = m.groupdict()
                root_dict['aaa_authorization'] = group['aaa_auth']
                continue

            # aaa-authorization username: test
            m = p21.match(line)
            if m:
                group = m.groupdict()
                root_dict['aaa_authorization_username'] = group['username']
                continue

            # data-privacy: normal
            m = p22.match(line)
            if m:
                group = m.groupdict()
                root_dict['data_privacy'] = group['privacy']
                continue

            # syslog throttling: enable
            m = p23.match(line)
            if m:
                group = m.groupdict()
                root_dict['syslog_throttling'] = group['throttling']
                continue

            # Rate-limit: 1 message(s) per minute
            m = p24.match(line)
            if m:
                group = m.groupdict()
                root_dict['Rate_limit_msg_per_min'] = int(group['rate_limit'])
                continue

            # Snapshot command: Not yet set up
            m = p25.match(line)
            if m:
                group = m.groupdict()
                root_dict['snapshot_command'] = group['cmd']
                continue

            # configuration            Enable  configuration info
            m = p26.match(line)
            if m:
                group = m.groupdict()
                key_dict = ret_dict.setdefault('available_alert_group',{}).setdefault('keyword',{}).setdefault(group['keyword'],{})
                key_dict['state'] = group['state']
                key_dict['description'] = group['description']
                continue

            # Profile Name: Test
            m = p27.match(line)
            if m:
                group = m.groupdict()
                name_dict = ret_dict.setdefault('profiles',{})
                if name:
                    name = name + ", " + group['name']
                else:
                    name = group['name']
                name_dict['name'] = name
                continue
        return ret_dict
