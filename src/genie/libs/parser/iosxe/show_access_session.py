"""show_access_seesion.py
   supported commands:
     * show access-session
     * show access-session interface {interface} details
     * show access-session brief
     * show access-session event-logging mac <mac>
     * show access-session mac {mac} details
     * show access-session mac {mac} details switch {mode} {rp_slot}
     * show access-session interface {interface} details switch {mode} {rp_slot}
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common

# import iosxe parser
from genie.libs.parser.iosxe.show_authentication_sessions import \
						ShowAuthenticationSessionsInterfaceDetails, ShowAuthenticationSessions

# ====================================
# Parser for 'show access-session'
# ====================================
class ShowAccessSessionSchema(MetaParser):
    """Schema for show access-session"""
    schema = {
        'session_count': int,
        Optional('interfaces'): {
            Any(): {
                'interface': str,
                'client': {
                    Any(): {
                        'client': str,
                        'method': str,
                        'domain': str,
                        'status': str,
                        'session': {
                            Any(): {
                                'session_id': str,
                            }
                        }
                    }
                }
            }
        }
    }


class ShowAccessSession(ShowAccessSessionSchema):
    """Parser for show access-session"""

    MAP = {'auth': 'authenticator',
           'supp': 'supplicant'}

    cli_command = 'show access-session'

    def cli(self,output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^No sessions currently exist$')
        p2 = re.compile(r'^Session +count \= +(?P<val>\d+)$')
        p3 = re.compile(r'^(?P<intf>[\w\/\-\.]+) +'
                         r'(?P<client>[\w\.]+) +'
                         r'(?P<method>\w+) +'
                         r'(?P<domain>\w+) +'
                         r'(?P<status>\w+) +'
                         r'(?P<session>\w+)$')

        for line in out.splitlines():
            line = line.strip()
            line = line.replace('\t', '    ')

            # No sessions currently exist
            m = p1.match(line)
            if m:
                ret_dict['session_count'] = 0
                return ret_dict

            # Session count = 1
            m = p2.match(line)
            if m:
                ret_dict['session_count'] = int(m.groupdict()['val'])
                continue

            # Gi1/0/1                  f4cf.beff.9cb1 dot1x   DATA    Auth        000000000000000BB6FC9EAF
            m = p3.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group['intf'])
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(intf, {})
                intf_dict['interface'] = intf

                client = group['client']
                client_dict = intf_dict.setdefault('client', {}).setdefault(client, {})
                client_dict['client'] = client
                client_dict['method'] = group['method']
                client_dict['domain'] = group['domain']
                client_dict['status'] = self.MAP[group['status'].lower()] \
                    if group['status'].lower() in self.MAP else group['status'].lower()
                session = group['session']
                client_dict.setdefault('session', {}).setdefault(session, {})\
                    .setdefault('session_id', session)
                continue

        return ret_dict

class ShowAccessSessionInterfaceDetails(ShowAuthenticationSessionsInterfaceDetails):
    '''
        Parser for the following show commands:
            * show access-session interface {interface} details
    '''
    cli_command = 'show access-session interface {interface} details'
    def cli(self, interface, output=None):

        if output is None:
            cmd = self.cli_command.format(interface=interface)
            show_output = self.device.execute(cmd)
        else:
           show_output = output

        # Call super
        return super().cli(output=show_output, interface=interface)

class ShowAccessSessionInterface(ShowAuthenticationSessions):
    '''
        Parser for the following show commands:
            * show access-session interface {interface} details
    '''
    cli_command = 'show access-session interface {interface}'
    def cli(self, interface, output=None):

        if output is None:
            cmd = self.cli_command.format(interface=interface)
            show_output = self.device.execute(cmd)
        else:
           show_output = output

        # Call super
        return super().cli(output=show_output, interface=interface)


# ====================================
# Parser for 'show access-session brief'
# ====================================
class ShowAccessSessionBriefSchema(MetaParser):
    """Schema for show access-session brief"""
    schema = {
        Optional('interfaces'): {
            Any(): {
                'interface': str,
                'mac': {
                    Any(): {
                        'mac': str,
                        'authc': str,
                        'authz': str,
                        'flag': str,
                        'uptime': str,
                    }
                }
            }
        }
    }



class ShowAccessSessionBrief(ShowAccessSessionBriefSchema):
    """Parser for show access-session brief"""

    cli_command = 'show access-session brief'

    def cli(self, output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<intf>[\w\/\-\.]+) +'
                        r'(?P<mac>[\w\.]+) +'
                        r'(?P<authc>[\w\:]+) +'
                        r'(?P<authz>[\w\:+\s+\w+\-]+) +'
                        r'(?P<flag>\w+) +'
                        r'(?P<uptime>\w+)$')

        for line in out.splitlines():
            line = line.strip()
            line = line.replace('\t', '    ')

            # Gi1/0/23   34bd.c853.0505  d:OK           AZ: SA-                 X    6858s
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group['intf'])
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(intf, {})
                intf_dict['interface'] = intf
                mac = group['mac']
                mac_dict = intf_dict.setdefault('mac', {}).setdefault(mac, {})
                mac_dict['mac'] = mac
                mac_dict['authc'] = group['authc']
                mac_dict['authz'] = group['authz']
                mac_dict['flag'] = group['flag']
                mac_dict['uptime'] = group['uptime']

                continue

        return ret_dict


# ======================================================
# Schema for 'Show access-session event-logging mac <mac> '
# ======================================================

class ShowAccessSessionEventLoggingMacSchema(MetaParser):
    """Schema for Show access-session event-logging mac <mac>"""

    schema = {
        'event_logging': {
            'client_mac': str,
            'state': str,
            'count': int,
            'id': int,
        },
        'mac_logs': {
            Any(): {
                Optional('timestamp'): str,
                Optional('src'): str,
                Optional('dest'): str,
                Optional('msg_type'): str,
                Optional('result'): str,
            },
        },
    }

# ======================================================
# Parser for 'Show access-session event-logging mac <mac> '
# ======================================================
class ShowAccessSessionEventLoggingMac(ShowAccessSessionEventLoggingMacSchema):
    """Parser for Show access-session event-logging mac <mac>"""

    cli_command = 'Show access-session event-logging mac {mac}'

    def cli(self, mac=None, output=None):
        if output is None:
            cmd = self.cli_command.format(mac=mac)
            output = self.device.execute(cmd)

        # Client-Mac :001b.0c18.918d
        p1 = re.compile(r"^Client-Mac\s+:(?P<client_mac>\S+)$")
        # State      : EV_SESSION_AUTHZ_SUCCESS
        p1_1 = re.compile(r"^State\s+:\s+(?P<state>\S+)$")
        # Count      : 196
        p1_2 = re.compile(r"^Count\s+:\s+(?P<count>\d+)$")
        # Id         : 3
        p1_3 = re.compile(r"^Id\s+:\s+(?P<id>\d+)$")
        # Sep/29  12:14:51:777   RCL_CLIENT    RCL           EV_SESSION_START                         EV_PASS
        p2 = re.compile(r"^(?P<timestamp>\S+\s+\S+)\s+(?P<src>\S+)\s+(?P<dest>\w+)\s+(?P<msg_type>\S+)\s+(?P<result>\S+)$")

        ret_dict = {}

        for line in output.splitlines():

            # Client-Mac :001b.0c18.918d
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'event_logging' not in ret_dict:
                    event_logging = ret_dict.setdefault('event_logging', {})
                event_logging['client_mac'] = dict_val['client_mac']
                continue

            # State      : EV_SESSION_AUTHZ_SUCCESS
            match_obj = p1_1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'event_logging' not in ret_dict:
                    event_logging = ret_dict.setdefault('event_logging', {})
                event_logging['state'] = dict_val['state']
                continue

            # Count      : 196
            match_obj = p1_2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'event_logging' not in ret_dict:
                    event_logging = ret_dict.setdefault('event_logging', {})
                event_logging['count'] = int(dict_val['count'])
                continue

            # Id         : 3
            match_obj = p1_3.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                if 'event_logging' not in ret_dict:
                    event_logging = ret_dict.setdefault('event_logging', {})
                event_logging['id'] = int(dict_val['id'])
                continue

            # Timestamp              Src           Dest          Msg Type                                 Result
            match_obj = p2.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                src_var = dict_val['src']
                if 'mac_logs' not in ret_dict:
                    mac_logs = ret_dict.setdefault('mac_logs', {})
                if src_var not in ret_dict['mac_logs']:
                    src_dict = ret_dict['mac_logs'].setdefault(src_var, {})
                src_dict['timestamp'] = dict_val['timestamp']
                src_dict['src'] = dict_val['src']
                src_dict['dest'] = dict_val['dest']
                src_dict['msg_type'] = dict_val['msg_type']
                src_dict['result'] = dict_val['result']
                continue


        return ret_dict


class ShowAccessSessionMacDetailsSchema(MetaParser):
    """
        Schema for
        * show access-session mac {mac} details
        * show access-session mac {mac} details switch {mode} {rp_slot}
        * show access-session interface {interface} details switch {mode} {rp_slot}
        * show access-session mac {mac} details {rp_slot}
    """
    schema = {
        'mac': {
            Any(): {
                'interface': str,
                'iif_id': str,
                'ipv6_address': str,
                'ipv4_address': str,
                Optional('user_name'): str,
                'status': str,
                'domain': str,
                'oper_host_mode': str,
                'oper_control_dir': str,
                Optional('session_timeout'): {
                    'server': int,
                    'remaining': int
                },
                Optional('timeout_action'): str,
                'common_session_id': str,
                'acct_session_id': str,
                'handle': str,
                'current_policy': str,
                Optional('local_policies'): {
                    Optional('url_redirect_acl_v6'): str,
                    Optional('preauth_acl_v6'): str,
                    Optional('url_redirect_acl_v4'): str,
                    Optional('preauth_acl_v4'): str,
                },
                'server_policies': {
                    Optional('filter_id'): str,
                    Optional('session_timeout'): int,
                    Optional('vlan_group'): int,
                    Optional('acs_acl'): str
                },
                'method_status_list': {
                    'method': str,
                    'state': str
                }
            }
        }
    }


class ShowAccessSessionMacDetails(ShowAccessSessionMacDetailsSchema):
    """
        Parser for
        * show access-session mac {mac} details
        * show access-session mac {mac} details switch {mode} {rp_slot}
        * show access-session interface {interface} details switch {mode} {rp_slot}
        * show access-session mac {mac} details {rp_slot}
    """
    cli_command = ['show access-session mac {mac} details', 
                'show access-session mac {mac} details switch {mode} {rp_slot}',
                'show access-session interface {interface} details switch {mode} {rp_slot}',
                'show access-session mac {mac} details {rp_slot}']
    
    def cli(self, mac, mode=None, rp_slot=None, interface=None, output=None):
        if output is None:
            if interface and mode and rp_slot:
                cli = self.cli_command[2].format(mac=mac, interface=interface, mode=mode, rp_slot=rp_slot)
            elif mode and rp_slot:
                cli = self.cli_command[1].format(mac=mac, mode=mode, rp_slot=rp_slot)
            elif rp_slot:
                cli = self.cli_command[3].format(mac=mac, rp_slot=rp_slot)
            else:
                cli = self.cli_command[0].format(mac=mac)
            
            output = self.device.execute(cli)
        
        # Interface:  GigabitEthernet1/0/12
        p1 = re.compile(r'^Interface:\s+(?P<interface>\S+)$')

        # IIF-ID:  0x135C9B47
        p2 = re.compile(r'^IIF-ID:\s+(?P<iif_id>\S+)$')

        # MAC Address:  000e.83e5.3398
        p3 = re.compile(r'^MAC Address:\s+(?P<mac>\S+)$')

        # IPv6 Address:  Unknown
        # IPv4 Address:  194.10.0.1
        # User-Name:  CP-7970G-SEP000E83E53398
        # Status:  Authorized
        # Domain:  VOICE
        # Oper host mode:  multi-domain
        # Oper control dir:  both
        # Timeout action:  Reauthenticate
        # Common Session ID:  EE01060A0000000FBB64DB50
        # Acct Session ID:  0x00000004
        # Handle:  0x60000005
        # Current Policy:  POLICY_Gi1/0/12
        p4 = re.compile(r'^(?P<key_name>IPv6 Address|IPv4 Address|User-Name|Status|Domain|Oper host mode|'
            r'Oper control dir|Timeout action|Common Session ID|Acct Session ID|Handle|Current Policy|):\s+(?P<value>\S+)$')

        # Session timeout:  135s (server), Remaining: 82s
        p5 = re.compile(r'^Session timeout:\s+(?P<server>\d+)s \(server\), Remaining: (?P<remaining>\d+)s$')

        # Local Policies:
        p5_1 = re.compile(r'^Local Policies:$')

        # URL Redirect ACL: IP-Adm-V6-Int-ACL-global
        p5_2 = re.compile(r'^URL Redirect ACL:\s+(?P<url_redirect_acl_v6>[A-Za-z\-6]+)$')

        # Preauth ACL: preauth_v6
        p5_3 = re.compile(r'Preauth ACL:\s+(?P<preauth_acl_v6>[A-Za-z\_6]+)$')

        # URL Redirect ACL: IP-Adm-V4-Int-ACL-global
        p5_4 = re.compile(r'^URL Redirect ACL:\s+(?P<url_redirect_acl_v4>[A-Za-z\-4]+)$')

        # Preauth ACL: preauth_v4
        p5_5 = re.compile(r'Preauth ACL:\s+(?P<preauth_acl_v4>[A-za-z\_4]+)$')

        # Server Policies:
        p6 = re.compile(r'^Server Policies:$')

        # Filter-ID: Webauth_ACL
        p6_1 = re.compile(r'^Filter-ID: (?P<filter_id>\w+)$')

        # Session-Timeout: 135 sec
        p7 = re.compile(r'^Session-Timeout: (?P<session_timeout>\d+) sec$')

        # Vlan Group:  Vlan: 194
        p8 = re.compile(r'^Vlan Group:  Vlan: (?P<vlan_group>\d+)$')

        # ACS ACL: xACSACLx-IP-legacy_TC9_permit_user_CP-7970G-SEP000E83E53398-63ced261
        p9 = re.compile(r'^ACS ACL: (?P<acs_acl>\S+)$')

        # Method status list:
        p10 = re.compile(r'^Method status list:$')

        # Method           State
        p11 = re.compile(r'^Method           State$')

        # dot1x           Authc Success
        p12 = re.compile(r'^(?P<method>\S+)           (?P<state>[\S\s]+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Interface:  GigabitEthernet1/0/12
            m = p1.match(line)
            if m:
                interface = Common.convert_intf_name(m.groupdict()['interface'])
                continue

            # IIF-ID:  0x135C9B47
            m = p2.match(line)
            if m:
                iif_id = m.groupdict()['iif_id']
                continue

            # MAC Address:  000e.83e5.3398
            m = p3.match(line)
            if m:
                mac_dict = ret_dict.setdefault('mac', {}).setdefault(m.groupdict()['mac'], {})
                mac_dict['interface'] = interface
                mac_dict['iif_id'] = iif_id
                continue

            # IPv6 Address:  Unknown
            # IPv4 Address:  194.10.0.1
            # User-Name:  CP-7970G-SEP000E83E53398
            # Status:  Authorized
            # Domain:  VOICE
            # Oper host mode:  multi-domain
            # Oper control dir:  both
            # Timeout action:  Reauthenticate
            # Common Session ID:  EE01060A0000000FBB64DB50
            # Acct Session ID:  0x00000004
            # Handle:  0x60000005
            # Current Policy:  POLICY_Gi1/0/12
            m = p4.match(line)
            if m:
                mac_dict[m.groupdict()['key_name'].lower().replace(' ', '_').replace('-', '_')] = m.groupdict()['value']
                continue

            # Session timeout:  135s (server), Remaining: 82s
            m = p5.match(line)
            if m:
                session_dict = mac_dict.setdefault('session_timeout', {})
                session_dict['server'] = int(m.groupdict()['server'])
                session_dict['remaining'] = int(m.groupdict()['remaining'])
                continue

            # Local Policies:
            m = p5_1.match(line)
            if m:
                local_policies_dict = mac_dict.setdefault('local_policies', {})
                continue

            # URL Redirect ACL: IP-Adm-V6-Int-ACL-global
            m = p5_2.match(line)
            if m:
                local_policies_dict['url_redirect_acl_v6'] = m.groupdict()['url_redirect_acl_v6']
                continue

            # Preauth ACL: preauth_v6
            m = p5_3.match(line)
            if m:
                local_policies_dict['preauth_acl_v6'] = m.groupdict()['preauth_acl_v6']
                continue

            # URL Redirect ACL: IP-Adm-V4-Int-ACL-global
            m = p5_4.match(line)
            if m:
                local_policies_dict['url_redirect_acl_v4'] = m.groupdict()['url_redirect_acl_v4']
                continue

            # Preauth ACL: preauth_v4
            m = p5_5.match(line)
            if m:
                local_policies_dict['preauth_acl_v4'] = m.groupdict()['preauth_acl_v4']
                continue

            # Server Policies:
            m = p6.match(line)
            if m:
                server_policies_dict = mac_dict.setdefault('server_policies', {})
                continue

            # Filter-ID: Webauth_ACL
            m = p6_1.match(line)
            if m:
                server_policies_dict['filter_id'] = m.groupdict()['filter_id']
                continue

            # Session-Timeout: 135 sec
            m = p7.match(line)
            if m:
                server_policies_dict['session_timeout'] = int(m.groupdict()['session_timeout'])
                continue

            # Vlan Group:  Vlan: 194
            m = p8.match(line)
            if m:
                server_policies_dict['vlan_group'] = int(m.groupdict()['vlan_group'])
                continue

            # ACS ACL: xACSACLx-IP-legacy_TC9_permit_user_CP-7970G-SEP000E83E53398-63ced261
            m = p9.match(line)
            if m:
                server_policies_dict['acs_acl'] = m.groupdict()['acs_acl']
                continue

            # Method status list:
            m = p10.match(line)
            if m:
                method_status_dict = mac_dict.setdefault('method_status_list', {})
                continue

            # Method           State
            m = p11.match(line)
            if m:
                continue

            # dot1x           Authc Success
            m = p12.match(line)
            if m:
                method_status_dict['method'] = m.groupdict()['method']
                method_status_dict['state'] = m.groupdict()['state']
                continue
        
        return ret_dict

class ShowAccessSessionSessionIdDetailsSchema(MetaParser):
    """
    Schema for:
    * show access-session session-id {session_id} details
    * show access-session session-id {session_id} policy
    * show access-session session-id {session_id} switch {mode} {rp_slot}
    """
    schema = {
        'session_id': {
            Any(): {
                'interface': str,
                'iif_id': str,
                Optional('mac'): str,
                Optional('ipv6_address'): str,
                Optional('ipv4_address'): str,
                Optional('user_name'): str,
                Optional('device_type'): str,
                Optional('device_name'): str,
                Optional('status'): str,
                Optional('domain'): str,
                Optional('oper_host_mode'): str,
                Optional('oper_control_dir'): str,
                Optional('session_timeout'): {
                    'local': int,
                    'remaining': int
                },
                Optional('timeout_action'): str,
                Optional('common_session_id'): str,
                Optional('acct_session_id'): str,
                Optional('handle'): str,
                Optional('current_policy'): str,
                Optional('server_policies'): {
                    Optional('vlan_group'): int
                },
                Optional('resultant_policies'): {
                    Optional('vlan_group'): int
                },
                'method_status_list': {
                    'method': str,
                    'state': str
                }
            }
        }
    }

class ShowAccessSessionSessionIdDetails(ShowAccessSessionSessionIdDetailsSchema):
    """
    Parser for:
    * show access-session session-id {session_id} details
    * show access-session session-id {session_id} policy
    * show access-session session-id {session_id} switch {mode} {rp_slot}
    """

    cli_command = [
        'show access-session session-id {session_id} details',
        'show access-session session-id {session_id} policy',
        'show access-session session-id {session_id} switch {mode} {rp_slot}'
    ]
    
    def cli(self, session_id=None, mode=None, rp_slot=None, output=None):

        # Ensure session_id is provided
        if not session_id:
            session_id = 'default_session_id'
        if output is None:
            # Select the correct CLI command to execute based on mode and rp_slot
            if mode and rp_slot:
                cli = self.cli_command[2].format(session_id=session_id, mode=mode, rp_slot=rp_slot)
            else:
                cli = self.cli_command[0].format(session_id=session_id)
            
            # Execute the CLI command on the device
            output = self.device.execute(cli)
        
        # Initialize the result dictionary
        ret_dict = {}
        method_status_dict = {}
        # Match Session ID line
        p0 = re.compile(r'^Session id=(?P<session_id>\S+)$')

        # Interface:  GigabitEthernet2/0/3
        p1 = re.compile(r'^Interface:\s+(?P<interface>\S+)$')

        # IIF-ID:  0x1210405D
        p2 = re.compile(r'^IIF-ID:\s+(?P<iif_id>\S+)$')

        # MAC Address:  0055.6677.8855
        p3 = re.compile(r'^MAC Address:\s+(?P<mac>\S+)$')

        # IPv6 Address:  Unknown
        # IPv4 Address:  192.168.10.101
        # User-Name:  asp_dot1x_user2
        # Device-type:  Un-Classified Device
        # Device-name:  Unknown Device
        # Status:  Authorized
        # Domain:  DATA
        # Oper host mode:  multi-domain
        # Oper control dir:  both
        # Timeout action:  Reauthenticate
        # Common Session ID:  2300130B0000002CBD0A520E
        # Acct Session ID:  0x0000003b
        # Handle:  0x31000022
        # Current Policy:  test_dot1x
        p4 = re.compile(r'^(?P<key_name>IPv6 Address|IPv4 Address|User-Name|Device-type|Device-name|Status|Domain|'
            r'Oper host mode|Oper control dir|Timeout action|Common Session ID|Acct Session ID|Handle|Current Policy):\s+(?P<value>.+)$')

        # Session timeout:  50s (local), Remaining: 27s
        p5 = re.compile(r'^Session timeout:\s+(?P<local>\d+)s \(local\), Remaining: (?P<remaining>\d+)s$')

        # Server Policies:
        p6 = re.compile(r'^Server Policies:$')

        # Vlan Group:  Vlan: 10 (server policies)
        p7 = re.compile(r'^Vlan Group:\s+Vlan:\s*(?P<vlan_group>\d+)\s*$')

        # Resultant Policies:
        p8 = re.compile(r'^Resultant Policies:$')

        # Vlan Group:  Vlan: 10 (resultant policies)
        p9 = re.compile(r'^Vlan Group:\s+Vlan:\s*(?P<vlan_group>\d+)\s*$')

        # Method status list:
        p10 = re.compile(r'^Method status list:$')

        # Skip Method header line
        p11 = re.compile(r'^Method           State$')

        # dot1x           Authc Success
        p12 = re.compile(r'^(?P<method>\S+)\s+(?P<state>[\S\s]+)$')

        # Simplified Table Output (Third type)
        p13 = re.compile(r'^(?P<interface>\S+)\s+(?P<mac>\S+)\s+(?P<method>\S+)\s+(?P<domain>\S+)\s+(?P<status>\S+)\s+(?P<session_id>\S+)$')

        # Processing output line by line
        for line in output.splitlines():
            line = line.strip()

            # Match Session ID line
            m = p0.match(line)
            if m:
                session_id = m.groupdict()['session_id']
                session_dict = ret_dict.setdefault('session_id', {}).setdefault(session_id, {})
                continue

            # Match Interface line
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                session_dict['interface'] = interface  # Ensure interface is assigned to session_dict
                continue
            if 'interface' not in session_dict:
                session_dict['interface'] = 'Unknown'
                continue

            # Match IIF-ID line
            m = p2.match(line)
            if m:
                iif_id = m.groupdict()['iif_id']
                session_dict['iif_id'] = iif_id  # Ensure iif_id is assigned to session_dict
                continue
            if 'iif_id' not in session_dict:
                session_dict['iif_id'] = 'Unknown'
                continue

            # Match MAC Address line
            m = p3.match(line)
            if m:
                session_dict['mac'] = m.groupdict()['mac']
                continue

            # Match key-value pairs like IPv6 Address, User-Name, etc.
            m = p4.match(line)
            if m:
                key_name = m.groupdict()['key_name'].lower().replace(' ', '_').replace('-', '_')
                session_dict[key_name] = m.groupdict()['value']
                continue

            # Match session timeout line
            m = p5.match(line)
            if m:
                session_dict['session_timeout'] = {
                    'local': int(m.groupdict()['local']),
                    'remaining': int(m.groupdict()['remaining'])
                }
                continue

            # Match server policies section
            m = p6.match(line)
            if m:
                server_policies_dict = session_dict.setdefault('server_policies', {})
                continue

            # Match Vlan Group under Server Policies
            m = p7.match(line)
            if m and 'server_policies' in session_dict:
                server_policies_dict['vlan_group'] = int(m.groupdict()['vlan_group'])
                continue

            # Match resultant policies section
            m = p8.match(line)
            if m:
                resultant_policies_dict = session_dict.setdefault('resultant_policies', {})
                continue

            # Match Vlan Group under Resultant Policies
            m = p9.match(line)
            if m and 'resultant_policies' in session_dict:
                resultant_policies_dict['vlan_group'] = int(m.groupdict()['vlan_group'])
                continue

            # Match Method status list header
            m = p10.match(line)
            if m:
                method_status_dict = session_dict.setdefault('method_status_list', {})
                continue

            # Skip Method header line
            m = p11.match(line)
            if m:
                continue

            # Match method-state pairs (e.g., dot1x - Authc Success)
            m = p12.match(line)
            if m:
                group = m.groupdict()
                method_status_dict['method'] = group['method']
                method_status_dict['state'] = group['state']
                session_dict['method_status_list'] = method_status_dict
                continue

            # Match the simplified table output line (3rd output type)
            m = p13.match(line)
            if m:
                group = m.groupdict()
                session_dict['interface'] = group.get('interface', 'Unknown')
                session_dict['mac'] = group.get('mac', 'Unknown') 
                session_dict['method'] = group.get('method', 'Unknown')
                session_dict['domain'] = group.get('domain', 'Unknown')
                session_dict['status'] = group.get('status', 'Unknown')
                session_dict['session_id'] = group.get('session_id', 'Unknown')
                continue
        return ret_dict
    
class ShowAccessSessionMacDetailsMethodSchema(MetaParser):
    """
    Schema for:
                * 'show access-session mac {mac} interface {interface} details'
                * 'show access-session mac {mac} method {method} details'
                * 'show access-session mac {mac} method {method} details switch {mode} {rp_slot}'
                * 'show access-session mac {mac} policy'
    """
    schema = {
        'mac': {
            Any(): {
                'interface': str,
                'iif_id': str,
                'ipv6_address': str,
                'ipv4_address': str,
                Optional('user_name'): str,
                Optional('device_type'): str,
                Optional('device_name'): str,
                'status': str,
                'domain': str,
                'oper_host_mode': str,
                'oper_control_dir': str,
                Optional('session_timeout'): {
                    'server': int,
                    'remaining': int,
                },
                Optional('timeout_action'): str,
                'common_session_id': str,
                'acct_session_id': str,
                'handle': str,
                'current_policy': str,
                'server_policies': {
                    Optional('vlan_group'): str
                },
                Optional('resultant_policies'): {
                    Optional('vlan_group'): str
                },
                'method_status_list': {
                    'method': str,
                    'state': str
                }
            }
        }
    }

class ShowAccessSessionMacDetailsMethod(ShowAccessSessionMacDetailsMethodSchema):
    """
    Parser for:
                * 'show access-session mac {mac} interface {interface} details'
                * 'show access-session mac {mac} method {method} details'
                * 'show access-session mac {mac} method {method} details switch {mode} {rp_slot}'
                * 'show access-session mac {mac} policy'
    """
    cli_command = [ 
                    'show access-session mac {mac} interface {interface} details',
                    'show access-session mac {mac} method {method} details',
                    'show access-session mac {mac} method {method} details switch {mode} {rp_slot}',
                    'show access-session mac {mac} policy']

    def cli(self, mac=None, mode=None, rp_slot=None, interface=None, method=None, output=None):
        if output is None:
            if mac and interface:
                cmd = self.cli_command[0].format(mac=mac, interface=interface)
            elif mac and method and mode and rp_slot:
                cmd = self.cli_command[2].format(mac=mac, method=method, mode=mode, rp_slot=rp_slot)
            elif mac and method:
                cmd = self.cli_command[1].format(mac=mac, method=method)   
            else:
                cmd = self.cli_command[3].format(mac=mac)
            output = self.device.execute(cmd)

        # Interface:  GigabitEthernet2/0/3
        p1 = re.compile(r'^Interface:\s+(?P<interface>\S+)$')

        # IIF-ID:  0x1D8DDC60
        p2 = re.compile(r'^IIF-ID:\s+(?P<iif_id>\S+)$')

        # MAC Address:  001a.a136.c68a
        p3 = re.compile(r'^MAC Address:\s+(?P<mac>\S+)$')

        # IPv6 Address:  Unknown
        # IPv4 Address:  192.168.194.1
        # User-Name:  CP-7961G-GE-SEP001AA136C68A
        # Device-type:  Cisco-IP-Phone-7961
        # Device-name:  Cisco IP Phone 7961
        # Status:  Authorized
        # Domain:  VOICE
        # Oper host mode:  multi-domain
        # Oper control dir:  both
        # Timeout action:  Reauthenticate
        # Common Session ID: 2300130B0000002ABD0A2AF1
        # Acct Session ID:  0x0000003c
        # Handle:  0xdb000020
        # Current Policy:  test_dot1x
        p4 = re.compile(r'^(?P<key_name>IPv6 Address|IPv4 Address|User-Name|Device Type|Device Name|Status|Domain|Oper host mode|'
                        r'Oper control dir|Timeout action|Common Session ID|Acct Session ID|Handle|Current Policy):\s+(?P<value>\S+)$')

        # Session timeout:  50s (server), Remaining: 27s
        p5 = re.compile(r'^Session timeout:\s+(?P<server>\d+)s \(server\), Remaining: (?P<remaining>\d+)s$')

        # Server Policies:
        p6 = re.compile(r'^Server Policies:$')

        # Vlan Group:  Vlan: 194
        p7 = re.compile(r'^Vlan Group:  Vlan: (?P<vlan_group>\d+)$')

        # Method status list:
        p8 = re.compile(r'^Method status list:$')

        # Method           State
        p9 = re.compile(r'^Method           State$') 

        # dot1x           Authc Success
        p10 = re.compile(r'^(?P<method>\S+)           (?P<state>[\S\s]+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Interface:  GigabitEthernet2/0/3
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                continue

            # IIF-ID:  0x1D8DDC60
            m = p2.match(line)
            if m:
                iif_id = m.groupdict()['iif_id']
                continue

            # MAC Address:  001a.a136.c68a
            m = p3.match(line)
            if m:
                mac = m.groupdict()['mac']
                mac_dict = ret_dict.setdefault('mac', {}).setdefault(mac, {})
                mac_dict['interface'] = interface
                mac_dict['iif_id'] = iif_id
                continue

            # IPv6 Address:  Unknown
            # IPv4 Address:  192.168.194.1
            # User-Name:  CP-7961G-GE-SEP001AA136C68A
            # Device-type:  Cisco-IP-Phone-7961
            # Device-name:  Cisco IP Phone 7961
            # Status:  Authorized
            # Domain:  VOICE
            # Oper host mode:  multi-domain
            # Oper control dir:  both
            # Timeout action:  Reauthenticate
            # Common Session ID: 2300130B0000002ABD0A2AF1
            # Acct Session ID:  0x0000003c
            # Handle:  0xdb000020
            # Current Policy:  test_dot1x
            m = p4.match(line)
            if m:
                key = m.groupdict()['key_name'].lower().replace(' ', '_').replace('-', '_')
                value = m.groupdict()['value']
                mac_dict[key] = value
                continue

            # Session timeout:  50s (server), Remaining: 27s
            m = p5.match(line)
            if m:
                session_dict = mac_dict.setdefault('session_timeout', {})
                session_dict['server'] = int(m.groupdict()['server'])
                session_dict['remaining'] = int(m.groupdict()['remaining'])
                continue

            # Server Policies:
            m = p6.match(line)
            if m:
                server_policies_dict = mac_dict.setdefault('server_policies', {})
                continue

            # Vlan Group:  Vlan: 194
            m = p7.match(line)
            if m:
                server_policies_dict['vlan_group'] = m.groupdict()['vlan_group']
                continue

            # Method status list:
            m = p8.match(line)
            if m:
                method_status_dict = mac_dict.setdefault('method_status_list', {})
                continue

            # Method           State
            m = p9.match(line)
            if m:
                continue

            # dot1x           Authc Success
            m = p10.match(line)
            if m:
                method_status_dict['method'] = m.groupdict()['method']
                method_status_dict['state'] = m.groupdict()['state']
                continue

        return ret_dict

class ShowAccessSessionDetailsSchema(MetaParser):
    """
      Schema for
       'show access-session interface {interface} details switch {switch_num} R0',
        'show access-session interface {interface} policy',
        'show access-session interface {interface} policy switch {mode} R0',
        'show access-session database interface {interface} details',
        'show access-session database interface {interface} policy',
        'show access-session database interface {interface} policy switch {mode} R0',
        'show access-session database interface {interface} switch {switch_num} R0'
    """
    schema = {
        'interface': {
            Any(): {
                'domain': str,
                'mac_address': str,
                Optional('method'): str,
                Optional('session_id'): str,
                Optional('status_fg'): str,
                Optional('iif_id'): str,
                Optional('ipv6_address'): str,
                Optional('ipv4_address'): str,
                Optional('user_name'): str,
                Optional('device_type'): str,
                Optional('device_name'): str,
                Optional('status'): str,
                Optional('oper_host_mode'): str,
                Optional('oper_control_dir'): str,
                Optional('session_timeout'): {
                    'local': int,
                    'remaining': int
                },
                Optional('timeout_action'): str,
                Optional('common_session_id'): str,
                Optional('acct_session_id'): str,
                Optional('handle'): str,
                Optional('aaa_uid'): str,
                Optional('vlan_id'): str,
                Optional('current_policy'): str,
                Optional('server_policies'): {
                    Optional('vlan_group'): int
                },
                Optional('resultant_policies'): {
                    Optional('vlan_group'): int
                },
                Optional('method_status_list'): {
                    'method': str,
                    'state': str
                } 
            }
        },
        Optional('runnable_methods'): {
            'name': {
                Any(): {
                    'handle': int,
                    'priority': int,
                }
            }
        }
    } 

class ShowAccessSessionDetails(ShowAccessSessionDetailsSchema):
    """Parser for:
        'show access-session interface {interface} details switch {switch_num} R0',
        'show access-session interface {interface} policy',
        'show access-session interface {interface} policy switch {mode} R0',
        'show access-session database interface {interface} details',
        'show access-session database interface {interface} policy',
        'show access-session database interface {interface} policy switch {mode} R0',
        'show access-session database interface {interface} switch {switch_num} R0'
    """

    cli_command = [
        'show access-session interface {interface} details switch {switch_num} R0',
        'show access-session interface {interface} policy',
        'show access-session interface {interface} policy switch {mode} R0',
        'show access-session database interface {interface} details',
        'show access-session database interface {interface} policy',
        'show access-session database interface {interface} policy switch {mode} R0',
        'show access-session database interface {interface} switch {switch_num} R0'
    ]

    def cli(self, interface='', switch_num='', mode='', output=None):
        if output is None:
            if interface:
                if mode:
                    if 'database' in interface.lower():
                        cmd = self.cli_command[5].format(interface=interface, mode=mode)  # Database with mode
                    else:
                        cmd = self.cli_command[2].format(interface=interface, mode=mode)  # Interface with mode
                elif switch_num:
                    if 'database' in interface.lower():
                        cmd = self.cli_command[6].format(interface=interface, switch_num=switch_num)  # Database with switch
                    else:
                        cmd = self.cli_command[0].format(interface=interface, switch_num=switch_num)  # Interface with switch
                else:
                    if 'database' in interface.lower():
                        cmd = self.cli_command[4].format(interface=interface)  # Database without mode or switch
                    else:
                        cmd = self.cli_command[1].format(interface=interface)  # Interface without mode or switch
            else:  
                cmd = self.cli_command[3].format(interface=interface)  # Includes interface for cli_command[3]
            output = self.device.execute(cmd)

        # Define regex patterns
        # Interface:  GigabitEthernet2/0/3
        p1 = re.compile(r'^Interface:\s+(?P<interface>\S+)$')
        
        # IIF-ID:  0x1D8DDC60
        p2 = re.compile(r'^IIF-ID:\s+(?P<iif_id>\S+)$')

        # Match MAC Address
        p3 = re.compile(r'^MAC Address:\s+(?P<mac>\S+)$')
      
        # IPv6 Address:  Unknown
        # IPv4 Address:  192.168.10.101
        # User-Name:  asp_dot1x_user2
        # Device-type:  Un-Classified Device
        # Device-name:  Unknown Device
        # Status:  Authorized
        # Domain:  DATA
        # Oper host mode:  multi-domain
        # Oper control dir:  both
        # Timeout action:  Reauthenticate
        # Common Session ID:  2300130B0000002CBD0A520E
        # Acct Session ID:  0x0000003b
        # Handle:  0x31000022
        # Current Policy:  test_dot1x
        p4 = re.compile(r'^(?P<key_name>IPv6 Address|IPv4 Address|User-Name|Device-type|Device-name|Status|'
                        r'Oper host mode|Oper control dir|Timeout action|Common Session ID|Acct Session ID|Handle|Current Policy):\s+(?P<value>.+)$')  # Match other session details
        
        # Match domain (VOICE or DATA)
        p5 = re.compile(r'^Domain:\s+(?P<domain>\S+)$')

        # Match session timeout
        p6 = re.compile(r'^Session timeout:\s+(?P<local>\d+)s \(local\), Remaining: (?P<remaining>\d+)s$')

         # Interface                MAC Address    Method  Domain  Status Fg  Session ID
        p7 = re.compile(r'^(?P<interface>\S+)\s+(?P<mac_address>\S+)\s+(?P<method>\S+)\s+(?P<domain>\S+)\s+(?P<status_fg>\S+)\s+(?P<session_id>\S+)$')
        
        # Server Policies (VLAN group)
        p8 = re.compile(r'^Server Policies:$')

        # Vlan Group:  Vlan: 194 (server policies)
        p9 = re.compile(r'^Vlan Group:  Vlan: (?P<vlan_group>\d+)$')  

        # Resultant Policies (VLAN group)
        p10 = re.compile(r'^Resultant Policies:$')

        # Vlan Group:  Vlan: 10 (resultant policies)
        p11 = re.compile(r'^Vlan Group:  Vlan: (?P<vlan_group>\d+)$')

        # Method status list:
        p12 = re.compile(r'^Method status list:$')

        #  Method       State
        p13 = re.compile(r'^Method\s+State$')

        # capture both method and state
        p14 = re.compile(r'^(?P<method>\S+)\s+(?P<state>\S+\s\S+)$')

        # AAA UID and VLAN ID
        p15 = re.compile(r'^AAA UID:\s+(?P<aaa_uid>\S+)$')

        #  VLAN ID
        p16 = re.compile(r'^VLAN ID:\s+(?P<vlan_id>\d+)$')

        # Runnable methods list:
        p17 = re.compile(r'^Runnable methods list:$')
        
        #   Handle  Priority  Name
        p18 = re.compile(r'^(?P<handle>\d+)\s+(?P<priority>\d+)\s+(?P<name>\S+)$')

        ret_dict = {}
        interface_dict = None
        method_status_dict = None
        runnable_methods_flag = False

        # Parse the output line by line
        for line in output.splitlines():
            line = line.strip()

            # Interface:  GigabitEthernet2/0/3
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                interface_dict = ret_dict.setdefault('interface', {}).setdefault(interface, {})
                continue

            # IIF-ID:  0x1D8DDC60
            m = p2.match(line)
            if m and interface_dict is not None:
                interface_dict['iif_id'] = m.groupdict()['iif_id']
                continue

            # MAC Address: 0055.6677.8855
            m = p3.match(line)
            if m and interface_dict is not None:
                interface_dict['mac_address'] = m.groupdict()['mac']
                continue

            # IPv6 Address:  Unknown
            # IPv4 Address:  192.168.10.101
            # User-Name:  asp_dot1x_user2
            # Device-type:  Un-Classified Device
            # Device-name:  Unknown Device
            # Status:  Authorized
            # Domain:  DATA
            # Oper host mode:  multi-domain
            # Oper control dir:  both
            # Timeout action:  Reauthenticate
            # Common Session ID:  2300130B0000002CBD0A520E
            # Acct Session ID:  0x0000003b
            # Handle:  0x31000022
            # Current Policy:  test_dot1x
            m = p4.match(line)
            if m and interface_dict is not None:
                key = m.groupdict()['key_name'].lower().replace(' ', '_').replace('-', '_')
                value = m.groupdict()['value']
                interface_dict[key] = value
                continue

            # Match domain (VOICE or DATA)
            m = p5.match(line)
            if m and interface_dict is not None:
                interface_dict['domain'] = m.groupdict()['domain']
                continue

            # Session timeout: 135s (local), Remaining: 82s
            m = p6.match(line)
            if m and interface_dict is not None:
                session_dict = interface_dict.setdefault('session_timeout', {})
                session_dict['local'] = int(m.groupdict()['local'])
                session_dict['remaining'] = int(m.groupdict()['remaining'])
                continue

            # Gi2/0/3                  0055.6677.8855 dot1x   DATA    N/A         2300130B0000002CBD0A520E
            m = p7.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                session_dict = ret_dict.setdefault('interface', {}).setdefault(interface, {})
                session_dict['mac_address'] = group['mac_address']
                session_dict['method'] = group['method']
                session_dict['domain'] = group['domain']
                session_dict['status_fg'] = group['status_fg']
                session_dict['session_id'] = group['session_id']
                continue

            # Match Server Policies
            m = p8.match(line)
            if m and interface_dict:
                interface_dict['server_policies'] = {}
                continue

            # Vlan Group:  Vlan: 194 (server policies)
            m = p9.match(line)
            if m and 'server_policies' in interface_dict:
                interface_dict['server_policies']['vlan_group'] = int(m.groupdict()['vlan_group'])
                continue

            # Match Resultant Policies
            m = p10.match(line)
            if m and interface_dict:
                interface_dict['resultant_policies'] = {}  # Initialize resultant_policies dictionary
                continue

            # Vlan Group:  Vlan: 10 (resultant policies)
            m = p11.match(line)
            if m and 'resultant_policies' in interface_dict:
                interface_dict['resultant_policies']['vlan_group'] = int(m.groupdict()['vlan_group'])
                continue

            # Match Method status list:
            m = p12.match(line)
            if m:
                method_status_dict = interface_dict.setdefault('method_status_list', {})
                continue

            # Method      State
            m = p13.match(line)
            if m:
                continue

            # dot1x           Authc Success
            m = p14.match(line)
            if m and method_status_dict is not None:
                method_status_dict['method'] = m.groupdict()['method']
                method_status_dict['state'] = m.groupdict()['state']
                continue

            # AAA UID: 0x0000002a
            m = p15.match(line)
            if m and interface_dict is not None:
                interface_dict['aaa_uid'] = m.groupdict()['aaa_uid']
                continue

            # VLAN ID: 194
            m = p16.match(line)
            if m and interface_dict is not None:
                interface_dict['vlan_id'] = str(m.groupdict()['vlan_id'])
                continue

            # Runnable methods list:
            if p17.match(line):
                runnable_methods_flag = True
                continue

            #   Handle  Priority  Name
            #   11         5  dot1xSup
            #   10         5  dot1x
            #   14        10  webauth
            #   12        15  mab
            if runnable_methods_flag:
                m = p18.match(line)
                if m:
                    group = m.groupdict()
                    handle = int(group.pop('handle'))
                    priority = int(group.pop('priority'))
                    name = group.pop('name')
                    method_dict = ret_dict.setdefault('runnable_methods', {}).setdefault('name', {}).setdefault(name, {})
                    method_dict.update({'handle': handle, 'priority': priority})
                    continue

        return ret_dict
    
class ShowAccessSessionMethodDot1xDetailsSchema(MetaParser):
    """
    Schema for 
    show access-session method dot1x {details}
    show access-session method dot1x {interface} details
    """
    schema = {
        'mac': {
            Any(): {
                'interface': str,
                'iif_id': str,
                'ipv6_address': str,
                'ipv4_address': str,
                Optional('user_name'): str,
                Optional('device_type'): str,
                Optional('device_name'): str,
                'status': str,
                'domain': str,
                'oper_host_mode': str,
                'oper_control_dir': str,
                Optional('session_timeout'): {
                    'server': int,
                    'remaining': int,
                },
                Optional('timeout_action'): str,
                'common_session_id': str,
                'acct_session_id': str,
                'handle': str,
                'current_policy': str,
                'server_policies': {
                    Optional('vlan_group'): str
                },
                Optional('resultant_policies'): {
                    Optional('vlan_group'): str
                },
                'method_status_list': {
                    'method': str,
                    'state': str
                }
            }
        }
    }

class ShowAccessSessionMethodDot1xDetails(ShowAccessSessionMethodDot1xDetailsSchema):
    """
    parser for
        show access-session method dot1x {details}
        show access-session method dot1x interface {interface} details
    """
    cli_command = ['show access-session method dot1x {details}',
                   'show access-session method dot1x interface {interface} details']

    def cli(self, details="", interface="", output=None):
        if output is None:
            if interface:
                cli = self.cli_command[1].format(interface=interface)
            else:
                cli = self.cli_command[0]

            output = self.device.execute(cli)
        
        # Interface:  GigabitEthernet2/0/3
        p1 = re.compile(r'^Interface:\s+(?P<interface>\S+)$')

        # IIF-ID:  0x1D8DDC60
        p2 = re.compile(r'^IIF-ID:\s+(?P<iif_id>\S+)$')

        # MAC Address:  001a.a136.c68a
        p3 = re.compile(r'^MAC Address:\s+(?P<mac>\S+)$')

        # IPv6 Address:  Unknown
        # IPv4 Address:  192.168.194.1
        # User-Name:  CP-7961G-GE-SEP001AA136C68A
        # Device-type:  Cisco-IP-Phone-7961
        # Device-name:  Cisco IP Phone 7961
        # Status:  Authorized
        # Domain:  VOICE
        # Oper host mode:  multi-domain
        # Oper control dir:  both
        # Timeout action:  Reauthenticate
        # Common Session ID: 2300130B0000002ABD0A2AF1
        # Acct Session ID:  0x0000003c
        # Handle:  0xdb000020
        # Current Policy:  test_dot1x
        p4 = re.compile(r'^(?P<key_name>IPv6 Address|IPv4 Address|User-Name|Device Type|Device Name|Status|Domain|Oper host mode|'
                        r'Oper control dir|Timeout action|Common Session ID|Acct Session ID|Handle|Current Policy):\s+(?P<value>\S+)$')

        # Session timeout:  50s (server), Remaining: 27s
        p5 = re.compile(r'^Session timeout:\s+(?P<server>\d+)s \(server\), Remaining: (?P<remaining>\d+)s$')

        # regex for server policies
        p6 = re.compile(r'^Server Policies:$')

        #Vlan Group:  Vlan: 194
        p7 = re.compile(r'^Vlan Group:  Vlan: (?P<vlan_group>\d+)$')

        # Method status list:
        p8 = re.compile(r'^Method status list:$')

        # Method           State
        p9 = re.compile(r'^Method           States$') 
        
        # dot1x           Authc Success
        p10 = re.compile(r'^(?P<method>\S+)           (?P<state>[\S\s]+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Interface:  GigabitEthernet2/0/3
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                continue

            # IIF-ID:  0x1D8DDC60
            m = p2.match(line)
            if m:
                iif_id = m.groupdict()['iif_id']
                continue

            # MAC Address:  001a.a136.c68a
            m = p3.match(line)
            if m:
                mac = m.groupdict()['mac']
                mac_dict = ret_dict.setdefault('mac', {}).setdefault(mac, {})
                mac_dict['interface'] = interface
                mac_dict['iif_id'] = iif_id
                continue

            # IPv6 Address:  Unknown
            # IPv4 Address:  192.168.194.1
            # User-Name:  CP-7961G-GE-SEP001AA136C68A
            # Device-type:  Cisco-IP-Phone-7961
            # Device-name:  Cisco IP Phone 7961
            # Status:  Authorized
            # Domain:  VOICE
            # Oper host mode:  multi-domain
            # Oper control dir:  both
            # Timeout action:  Reauthenticate
            # Common Session ID: 2300130B0000002ABD0A2AF1
            # Acct Session ID:  0x0000003c
            # Handle:  0xdb000020
            # Current Policy:  test_dot1x
            m = p4.match(line)
            if m:
                key = m.groupdict()['key_name'].lower().replace(' ', '_').replace('-', '_')
                value = m.groupdict()['value']
                mac_dict[key] = value
                continue

            # Session timeout:  50s (server), Remaining: 27s
            m = p5.match(line)
            if m:
                session_dict = mac_dict.setdefault('session_timeout', {})
                session_dict['server'] = int(m.groupdict()['server'])
                session_dict['remaining'] = int(m.groupdict()['remaining'])
                continue

            # Server Policies:
            m = p6.match(line)
            if m:
                server_policies_dict = mac_dict.setdefault('server_policies', {})
                continue

            # Vlan Group:  Vlan: 194
            m = p7.match(line)
            if m:
                server_policies_dict['vlan_group'] = m.groupdict()['vlan_group']
                continue

            # Method status list:
            m = p8.match(line)
            if m:
                method_status_dict = mac_dict.setdefault('method_status_list', {})
                continue

            # Method           State
            m = p9.match(line)
            if m:
                continue

            # dot1x           Authc Success
            m = p10.match(line)
            if m:
                method_status_dict['method'] = m.groupdict()['method']
                method_status_dict['state'] = m.groupdict()['state']
                continue
        
        
        return ret_dict
