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
                         '(?P<client>[\w\.]+) +'
                         '(?P<method>\w+) +'
                         '(?P<domain>\w+) +'
                         '(?P<status>\w+) +'
                         '(?P<session>\w+)$')

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
    """
    cli_command = ['show access-session mac {mac} details', 
                'show access-session mac {mac} details switch {mode} {rp_slot}',
                'show access-session interface {interface} details switch {mode} {rp_slot}']
    
    def cli(self, mac, mode=None, rp_slot=None, interface=None, output=None):
        if output is None:
            if interface and mode and rp_slot:
                cli = self.cli_command[2].format(mac=mac, interface=interface, mode=mode, rp_slot=rp_slot)
            elif mode and rp_slot:
                cli = self.cli_command[1].format(mac=mac, mode=mode, rp_slot=rp_slot)
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
