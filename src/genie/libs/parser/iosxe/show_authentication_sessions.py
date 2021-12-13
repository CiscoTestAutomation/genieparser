''' show_authentication_sessions.py

IOSXE parsers for the following show commands:
    * show authentication sessions
    * show authentication sessions interface {interface}
    * show authentication sessions interface {interface} details

'''
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

'''
Device# show authentication sessions 

Interface  MAC Address     Method   Domain   Status         Session ID
Gi1/48     0015.63ff.a727  dot1x    DATA     Authz Success  0A3462B1000000102983C05C
Gi1/5      000f.23ff.69c5  mab      DATA     Authz Success  0A3462B10000000D24F80B58
Gi1/5      0014.bfff.30ca  dot1x    DATA     Authz Success  0A3462B10000000E29811B94
'''


# ==============================================
# Parser for 'show authentication sessions'
# ==============================================
class ShowAuthenticationSessionsSchema(MetaParser):
    """Schema for show authentication sessions
                  show authentication sessions interface {interface}
    """

    schema = {
        'interfaces': {
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
        },
        Optional('session_count'): int,
    }


class ShowAuthenticationSessions(ShowAuthenticationSessionsSchema):
    """Parser for 'show authentication sessions'
                  'show authentication sessions interface {interface}''
    """

    cli_command = ['show authentication sessions', 'show authentication sessions interface {interface}']

    def cli(self, interface=None, output=None):
        if interface:
            cmd = self.cli_command[1].format(interface=interface)
        else:
            cmd = self.cli_command[0]

        if output is None:
            # get output from device
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern

        # Interface  MAC Address     Method   Domain   Status         Session ID
        p1 = re.compile(r'^Interface +MAC +Address +Method +Domain +Status +Session +ID')

        # Interface Identifier Method Domain Status Fg Session ID
        p2 = re.compile(r'^Interface +Identifier +Method +Domain +Status +Fg +Session +ID')

        # Matching patterns
        # Gi1/48     0015.63ff.a727  dot1x    DATA     Authz Success  0A3462B1000000102983C05C
        # Gi1/5      000f.23ff.69c5  mab      DATA     Authz Success  0A3462B10000000D24F80B58
        # Gi1/5      0014.bfff.30ca  dot1x    DATA     Authz Success  0A3462B10000000E29811B94
        # Gi1/0/7    0014.bfff.30ca  N/A      DATA     Authz Success  0A3462B10000000E29811B94
        p4 = re.compile(r'^(?P<interface>\S+) +'
                        '(?P<client>\w+\.\w+\.\w+) +'
                        '(?P<method>[\w/]+) +'
                        '(?P<domain>\w+) +'
                        '(?P<status>\w+(?: +\w+)?) +'
                        '(?P<session>\w+)$')

        # *Session count = 2*
        p5 = re.compile(r'(?:\*)?Session +[Cc]ount +\= '
                        r'+(?P<session_count>\d+)(?:\*)?$')

        for line in out.splitlines():
            line = line.strip()

            # Ignore the title
            if p1.match(line) or p2.match(line):
                continue

            # Gi1/0/48     0015.63ff.a727  dot1x    DATA     Authz Success  0A3462B1000000102983C05C
            # Gi1/7/35  0000.00ff.4444 dot1x  UNKNOWN Auth      141927640000000E0B40EDB0
            m = p4.match(line)

            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                intf_dict['interface'] = interface
                client = group['client']
                client_dict = intf_dict.setdefault('client', {}).setdefault(client, {})
                client_dict.update({'client': client})

                client_dict['method'] = group['method']
                client_dict['domain'] = group['domain']
                client_dict['status'] = group['status']
                session = group['session']
                client_dict.setdefault('session', {}).setdefault(session, {}) \
                    .setdefault('session_id', session)
                continue
            
            # *Session count = 2*
            m5 = p5.match(line)
            if m5:
                count = int(m5.groupdict()['session_count'])
                ret_dict.update({'session_count': count})

                continue

        return ret_dict



# ==================================================================================
# Schema for:
#                * 'show authentication sessions interface {interface} details'
#                * 'show authentication sessions interface {interface} details switch {switch} r0'
#                * 'show authentication sessions mac {mac_address} details'
#                * 'show authentication sessions mac {mac_address} details switch {switch} r0'
# ==================================================================================

class ShowAuthenticationSessionsDetailsSuperSchema(MetaParser):
    """
    Schema for:
                * 'show authentication sessions interface {interface} details'
                * 'show authentication sessions interface {interface} details switch {switch} r0'
                * 'show authentication sessions mac {mac_address} details'
                * 'show authentication sessions mac {mac_address} details switch {switch} r0'
    """
    schema = {
        'interfaces': {
            Any(): {
                'mac_address': {
                    Any(): {
                        Optional('iif_id'): str,
                        Optional('ipv6_address'): str,
                        'ipv4_address': str,
                        Optional('user_name'): str,
                        Optional('periodic_acct_timeout'): str,
                        Optional('timeout_action'): str,
                        Optional('restart_timeout'): {
                            Optional('timeout'): int,
                            Optional('remaining'): int,
                        },
                        Optional('unauth_timeout'): {
                            Optional('timeout'): int,
                            Optional('remaining'): int,
                        },
                        Optional('session_uptime'): str,
                        'status': str,
                        'domain': str,
                        'oper_host_mode': str,
                        'oper_control_dir': str,
                        Optional('authorized_by'): str,
                        Optional('vlan_policy'): str,
                        'session_timeout': {
                            'type': str,  # local, N/A
                            Optional('timeout'): str,
                            Optional('remaining'): str,
                        },
                        'common_session_id': str,
                        'acct_session_id': str,
                        'handle': str,
                        Optional('idle_timeout'): str,
                        Optional('current_policy'): str,
                        Optional('server_policies'): {
                            Any():{ # 1, 2, 3
                                Optional('name'): str,
                                Optional('policies'): str,
                                Optional('security_policy'): str,
                                Optional('security_status'): str
                            }
                        },
                        Optional('local_policies'): {
                            Optional('template'): {
                                Any(): {
                                    'priority': int,
                                }
                            },
                            Optional('vlan_group'): {
                                'vlan': int,
                            },
                            Optional('security_policy'): str,
                            Optional('security_status'): str,
                        },
                        Optional('method_status'): {
                            Any(): {
                                'method': str,
                                'state': str,
                            }
                        }
                    }
                },
            }
        }
    }

# ==================================================================================
# Parser for:
#           * 'show authentication sessions interface {interface} details'
#           * 'show authentication sessions interface {interface} details switch {switch} r0'
#           * 'show authentication sessions mac {mac_address} details'
#           * 'show authentication sessions mac {mac_address} details switch {switch} r0'
# ==================================================================================

class ShowAuthenticationSessionsDetailsSuperParser(ShowAuthenticationSessionsDetailsSuperSchema):
    """
    SuperParser for:
                * 'show authentication sessions interface {interface} details'
                * 'show authentication sessions interface {interface} details switch {switch} r0'
                * 'show authentication sessions mac {mac_address} details'
                * 'show authentication sessions mac {mac_address} details switch {switch} r0'
    """

    def cli(self, interface='', mac_address='', switch='', output=None):


        # Interface:  GigabitEthernet3/0/2
        # IIF-ID:  0x1055240000001F6 
        # MAC Address:  0010.00ff.1011
        # IPv6 Address:  Unknown
        # IPv4 Address:  192.0.2.1
        # User-Name:  auto601
        # Status:  Authorized
        # Domain:  DATA
        # Oper host mode:  single-host
        # Oper control dir:  both
        # Session timeout:  N/A
        # Common Session ID:  AC14FC0A0000101200E28D62
        # Acct Session ID:  Unknown
        # Handle:  0xDB003227
        # Current Policy:  dot1x_dvlan_reauth_hm
        # Authorized By:  Guest Vlan
        # Status:  Authz Success
        # *ACS ACL:* *xGENIEx-Test_ACL_CiscoPhones-e23431ede2*
        p1 = re.compile(r'(?:\*)?(?P<argument>[\w\s\-]+)\:(?:\*)? '
                        r'+(?:\*)?(?P<value>[\w\s\-\.\./]+|\S+)(?:\*)?$')

        # Local Policies:
        p2 = re.compile(r'^Local +Policies:')

        # Template: CRITICAL_VLAN (priority 150)
        # Service Template: DEFAULT_LINKSEC_POLICY_SHOULD_SECURE (priority 150)
        p3 = re.compile(r'^(?:Service +)?Template: +(?P<template>\w+) +\(priority +(?P<priority>[0-9]+)\)$')

        # Vlan Group:  Vlan: 130
        p4 = re.compile(r'^Vlan +Group: +(?P<vlan_name>\w+): +(?P<vlan_value>[0-9]+)$')

        # Method status list:
        p5 = re.compile(r'^Method +status +list:')

        # dot1x            Authc Failed
        p6 = re.compile(r'^(?P<method>[dot1x|mab]\w+) +(?P<state>(\w+\s\w+)|(\w+))$')

        # Runnable methods list:
        p7 = re.compile(r'^Runnable +methods +list:')

        # For IOS output as this line will determine the index
        p8 = re.compile(r'^-+$')

        # Session timeout:  43200s(local), Remaining: 31799s
        # Session timeout:  N/A
        p9 = re.compile(
            r'^Session +timeout: +(?P<value>\S+)(?:\s*\((?P<name>\w+)\), +Remaining: +(?P<remaining>[\S]+))?')

        #   Security Policy:  Should Secure
        #   Security Status:  Link Unsecure
        p10 = re.compile(r'^Security +(?P<security_name>\S+): +(?P<policy_status>[\S ]+)$')
        
        # *      Security Policy:  None      Security Status:  Link Unsecured*
        p10_1 = re.compile(r'(.*)\s+ Security +(?P<security_name>\w+):(\s+)* +'
                r'(?P<policy_status>\w+(\s\w+)?)(\s+)+ Security +(?P<security_name2>\w+):(\s+)* '
                r'+(?P<policy_status2>\w+(\s\w+)?)')

        # IPv6 Address: fe80::2119:3248:786b:40db
        # IPv6 Address: fe80:0000:0000:0000:0204:61ff:fe9d:f156
        # IPv6 Address: fe80:0:0:0:204:61ff:fe9d:f156
        # IPv6 Address: fe80::204:61ff:fe9d:f156
        # IPv6 Address: fe80::204:61ff
        # IPv6 Address: fe9d:f156::1
        p11 = re.compile(r'^IPv6 +Address\: +(?P<ipv6>\S+?)$')

        # Server Policies:
        p12 = re.compile(r'^Server +Policies\:$')

        # Restart timeout:  60s, Remaining: 44s
        p13 = re.compile(r'(Restart\s*timeout)\s*:\s*(?P<timeout>\w+)s(\s*,\s*Remaining\s*:\s*(?P<remaining>\w+)s)?')

        # Unauth timeout:  10s, Remaining: 5s
        p14 = re.compile(r'(Unauth\s*timeout)\s*:\s*(?P<timeout>\w+)s(\s*,\s*Remaining\s*:\s*(?P<remaining>\w+)s)?')

        # initial return dictionary
        ret_dict = {}
        hold_dict = {}
        mac_dict = {}
        policies_dict = {}
        policies_flag = False
        index = 1

        out = output
        for line in out.splitlines():
            line = line.strip()

            # Ignore all titles
            if p2.match(line) or p5.match(line) or p7.match(line):
                continue

            #   Security Policy:  Should Secure
            #   Security Status:  Link Unsecure
            m = p10.match(line)
            if m:
                group = m.groupdict()
                if policies_flag:
                    if index != 1:
                        index += 1
                    if not policies_dict:
                        policies_dict = mac_dict.setdefault('server_policies', {})
                        index_dict = policies_dict.setdefault(index, {})
                    if group['security_name'] == 'Policy':
                        index_dict.update({'security_policy': group['policy_status']})
                    elif group['security_name'] == 'Status':
                        index_dict.update({'security_status': group['policy_status']})
                else:
                    security_dict = mac_dict.setdefault('local_policies', {})
                    if group['security_name'] == 'Policy':
                        security_dict.update(
                            {'security_policy': group['policy_status']})
                    elif group['security_name'] == 'Status':
                        security_dict.update(
                            {'security_status': group['policy_status']})

                continue

            # *      Security Policy:  None      Security Status:  Link Unsecured*
            m = p10_1.match(line)
            if m:
                group = m.groupdict()
                if policies_flag:
                    if not policies_dict:
                        policies_dict = mac_dict.setdefault('server_policies', {})
                        index_dict = policies_dict.setdefault(index, {})
                    index_dict.update({'security_policy': group['policy_status']})
                    index_dict.update({'security_status': group['policy_status2']})
                else:
                    security_dict = mac_dict.setdefault('local_policies', {})
                    security_dict.update({'security_policy': group['policy_status']})
                    security_dict.update({'security_status': group['policy_status2']})
                continue

            # Session timeout:  43200s(local), Remaining: 31799s
            # Session timeout:  N/A
            m = p9.match(line)
            if m:
                group = m.groupdict()
                session_dict = mac_dict.setdefault('session_timeout', {})
                if group['value'] == 'N/A':
                    session_dict.update({'type': r'N/A'})
                else:
                    session_dict.update({'type': group['name']})
                    session_dict.update({'timeout': group['value']})
                    session_dict.update({'remaining': group['remaining']})

                continue
            
            # Restart timeout:  10s, Remaining: 5s
            m13 = p13.match(line)
            if m13:
                restart_dict = mac_dict.setdefault('restart_timeout', {})
                restart_dict.update({'timeout': int(m13.group('timeout'))})
                restart_dict.update({'remaining': int(m13.group('remaining'))})
                continue

            # Unauth timeout:  60s, Remaining: 44s
            m14 = p14.match(line)
            if m14:
                unauth_dict = mac_dict.setdefault('unauth_timeout', {})
                unauth_dict.update({'timeout': int(m14.group('timeout'))})
                unauth_dict.update({'remaining': int(m14.group('remaining'))})
                continue

            # match these lines:
            #             Interface:  GigabitEthernet3/0/2
            #                IIF-ID:  0x1055240000001F6
            #           MAC Address:  0010.00ff.1011
            #          IPv6 Address:  Unknown
            #          IPv4 Address:  192.0.2.1
            #             User-Name:  auto601
            #                Status:  Authorized
            #                Domain:  DATA
            #        Oper host mode:  single-host
            #      Oper control dir:  both
            #     Common Session ID:  AC14FC0A0000101200E28D62
            #       Acct Session ID:  Unknown
            #                Handle:  0xDB003227
            #        Current Policy:  dot1x_dvlan_reauth_hm
            #         Authorized By:  Guest Vlan
            #                Status:  Authz Success
            # *ACS ACL: xGENIEx-Test_ACL_CiscoPhones-e23431ede2*
            # ACS ACL: xACSACLx-IP-ACL_MABDefault_V3-8dase3932
            # URL Redirect ACL: ACLSWITCH_Redirect_v1
            # *ACS ACL:* *xGENIEx-Test_ACL_CiscoPhones-e23431ede2*
            m = p1.match(line)
            if m:
                known_list = ['interface', 'iif_id', 'mac_address', 
                              'ipv6_address', 'ipv4_address', 'user_name', 
                              'status', 'domain', 'oper_host_mode', 
                              'oper_control_dir',
                              'common_session_id', 'acct_session_id', 
                              'handle', 'current_policy', 'authorized_by',
                              'periodic_acct_timeout',
                              'session_uptime', 'timeout_action', 'ip_address',
                              'idle_timeout', 'vlan_policy']

                group = m.groupdict()
                key = re.sub(r'( |-)', '_', group['argument'].lower())

                if key in known_list:
                    # to keep pv4_address as common key
                    if key == 'ip_address':
                        key = 'ipv4_address'

                    if 'interfaces' in ret_dict.keys():
                        if key == 'mac_address':
                            index = 1
                            mac_dict = intf_dict.setdefault(group['value'], {})
                        elif key == 'iif_id':
                            hold_dict.update({'argument': key, 'value': group['value']})
                        elif hold_dict:
                            mac_dict.update({key: group['value']})
                            tmp_keys = hold_dict.pop('argument')
                            tmp_values = hold_dict.pop('value')
                            mac_dict.update({tmp_keys: tmp_values})

                        elif key != 'interface':
                            mac_dict.update({key: group['value']})
                    else:
                        mac_dict = ret_dict.setdefault('interfaces', {})
                        value_dict = mac_dict.setdefault(group['value'], {})
                        intf_dict = value_dict.setdefault('mac_address', {})
                        
                elif (key not in known_list) and policies_flag:
                    policies_dict = mac_dict.setdefault('server_policies', {})
                    index_dict = policies_dict.setdefault(index, {})
                    index_dict.update({'name': group['argument']})
                    index_dict.update({'policies': group['value']})
                    index += 1
                    
                continue
 
            # Template: CRITICAL_VLAN (priority 150)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                template_dict = mac_dict.setdefault('local_policies', {}).setdefault('template', {})
                priority_dict = template_dict.setdefault(group['template'], {})
                priority_dict.update({'priority': int(group['priority'])})
                continue

            # Vlan Group:  Vlan: 130
            m = p4.match(line)
            if m:
                group = m.groupdict()
                vlan_dict = mac_dict.setdefault('local_policies', {}).setdefault('vlan_group', {})

                vlan_dict.update({'vlan': int(group['vlan_value'])})

                continue

            # dot1x            Authc Failed
            m = p6.match(line)
            if m:
                group = m.groupdict()

                method_stat = mac_dict.setdefault('method_status', {}).setdefault(group['method'], {})
                method_stat.update({'method': group['method']})
                method_stat.update({'state': group['state']})
                continue

            # IPv6 Address: fe80::2119:3248:786b:40db
            # IPv6 Address: fe80:0000:0000:0000:0204:61ff:fe9d:f156
            # IPv6 Address: fe80:0:0:0:204:61ff:fe9d:f156
            # IPv6 Address: fe80::204:61ff:fe9d:f156
            # IPv6 Address: fe80::204:61ff
            # IPv6 Address: fe9d:f156::1
            m11 = p11.match(line)
            if m11:
                mac_dict.update({'ipv6_address': m11.groupdict()['ipv6']})

                continue

            # Server Policies:
            m12 = p12.match(line)
            if m12:
                policies_flag = True

                continue

        return ret_dict

# ==================================================================================
# Parser for:
#           * 'show authentication sessions interface {interface} details'
#           * 'show authentication sessions interface {interface} details switch {switch} r0'
# ==================================================================================

class ShowAuthenticationSessionsInterfaceDetails(ShowAuthenticationSessionsDetailsSuperParser):
    """
    Parser for:
                * 'show authentication sessions interface {interface} details'
                * 'show authentication sessions interface {interface} details switch {switch} r0'
    """

    cli_command = ['show authentication sessions interface {interface} details',\
                   'show authentication sessions interface {interface} details switch {switch} r0']
                   
    def cli(self, interface='', switch='', output=None):

        if output is None:
            # Build command
            if switch:
                cmd = self.cli_command[1].format(interface=interface,switch=switch)
            else: 
                cmd = self.cli_command[0].format(interface=interface)
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, interface=interface, switch=switch)

# ==================================================================================
# Parser for:
#           * 'show authentication sessions mac {mac_address} details'
#           * 'show authentication sessions mac {mac_address} details switch {switch} r0'
# ==================================================================================

class ShowAuthenticationSessionsMACDetails(ShowAuthenticationSessionsDetailsSuperParser):
    """
       Parser for:
                * 'show authentication sessions mac {mac_address} details'
                * 'show authentication sessions mac {mac_address} details switch {switch} r0'
    """
    cli_command = ['show authentication sessions mac {mac_address} details',\
                   'show authentication sessions mac {mac_address} details switch {switch} r0'] 
                    

    def cli(self, mac_address='', switch='', output=None):

        if output is None:
            # Build command
            if switch:
                cmd = self.cli_command[1].format(mac_address=mac_address,switch=switch)
            else: 
                cmd = self.cli_command[0].format(mac_address=mac_address)
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, mac_address=mac_address, switch=switch)

#========================================================================================
# Parser for:
#           * 'authentication display config-mode'
#========================================================================================

class AuthenticationDisplayConfigModeSchema(MetaParser):
    schema = {
        'current_config_mode': str,
    }


class AuthenticationDisplayConfigMode(AuthenticationDisplayConfigModeSchema):

    cli_command = 'authentication display config-mode'

    def cli(self,output=None):

        if not output:
            output = self.device.execute(self.cli_command)

        p1 = re.compile(r'^Current\sconfiguration\smode\sis\s(?P<current_config_mode>\S+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('current_config_mode', group['current_config_mode'])
                continue
        
        return ret_dict
