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
                'address': str,
                'priority': int,
                'secure': str,
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
        #     Mail-server[2]: Address: ott-ads-085 Priority: 2  Secure: tls [Not Available]
        p1 = re.compile(r'^(?P<mail_server_id>\S+):( +Address:\s(?P<address>\S+))*( +Priority: (?P<priority>\d+))*( +Secure: (?P<secure>.*))*$')

        for line in output.splitlines():
            line = line.strip()

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