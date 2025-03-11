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
                        r'(?P<client>\w+\.\w+\.\w+) +'
                        r'(?P<method>[\w/]+) +'
                        r'(?P<domain>\w+) +'
                        r'(?P<status>\w+(?: +\w+)?) +'
                        r'(?P<session>\w+)$')

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
                         Optional('ipv6'): {
                            'ipv6_address': Or(str, list)
                        },
                        'ipv4_address': str,
                        Optional('user_name'): str,
                        Optional('device_type'): str,
                        Optional('device_name'): str,
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
                            Optional('interface_template'): str
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
        p3 = re.compile(r'^(?P<template_type>Service|Interface)?\s*Template: +(?P<template>\w+)\s*(\(priority +(?P<priority>[0-9]+)\))?$')

        # Vlan Group:  Vlan: 130
        p4 = re.compile(r'^Vlan +Group: +(?P<vlan_name>\w+): +(?P<vlan_value>[0-9]+)$')

        # Method status list:
        p5 = re.compile(r'^Method +status +list:')

        # dot1x            Authc Failed
        p6 = re.compile(r'^(?P<method>[dot1x|mab|webauth]\w+) +(?P<state>(\w+\s\w+)|(\w+))$')

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

        # 1555:10::5ced:6cc3:825b:39da
        # 1555:10::225:1ff:fe00:5
        p11_1 = re.compile(r'^(?P<address>[\w\:]+)$')

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
                              'idle_timeout', 'vlan_policy', 'device_type', 'device_name']

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
                    continue

                elif (key not in known_list) and policies_flag:
                    policies_dict = mac_dict.setdefault('server_policies', {})
                    index_dict = policies_dict.setdefault(index, {})
                    index_dict.update({'name': group['argument']})
                    index_dict.update({'policies': group['value']})
                    index += 1
                    
                    continue
 
            # Template: CRITICAL_VLAN (priority 150)
            # Interface Template: IP_PHONE_INTERFACE_TEMPLATE
            m = p3.match(line)
            if m:
                group = m.groupdict()
                local_policies_dict = mac_dict.setdefault('local_policies', {})
                if group['template_type'] == 'Interface':
                    local_policies_dict.setdefault('interface_template', group['template'])
                    continue
                template_dict = local_policies_dict.setdefault('template', {})
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
            
            # 1555:10::5ced:6cc3:825b:39da
            # 1555:10::225:1ff:fe00:5            
            m = p11_1.match(line)                            
            if m:                         
                group = m.groupdict()
                com_dict = mac_dict.setdefault('ipv6', {}).setdefault('ipv6_address', [])      
                com_dict.append(group['address'])         
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
                   
    def cli(self, interface='', switch='', timeout=60, output=None):

        if output is None:
            # Build command
            if switch:
                cmd = self.cli_command[1].format(interface=interface,switch=switch)
            else: 
                cmd = self.cli_command[0].format(interface=interface)
            # Execute command
            show_output = self.device.execute(cmd, timeout=timeout)
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

'''
Device#show access-session info
Interface    MAC Address    M:D:S    Vlan     IPv4        Policy               User-Role
-----------------------------------------------------------------------------------------
Gi3/0/11     0015.0100.0001 D1x:D:AZ  UA        200.1.0.1 Dot1x                UA        
Gi3/0/11     0015.0100.0002 D1x:D:AZ  UA        200.1.0.2 Dot1x                UA        
Gi3/0/3      2894.0feb.9280 D1x:U:UZ  UA       UA         Dot1x                UA        
Gi3/0/3      34db.fde5.34ab D1x:V:UZ  UA       UA         Dot1x                UA
'''

# ==================================================================================
# Schema for:
#                * 'show access-session info'
#                * 'show access-session info switch {switch} r0'
# ==================================================================================

# ==============================================
# Parser for 'show access-session info'
# ==============================================
class ShowAccessSessionsInfoSchema(MetaParser):
    """Schema for show access-session info
            show access-session info switch {switch} r0
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
                        'vlan': str,
                        'ipv4': str,
                        'policy': str,
                        'role': str,
                    }
                }
            }
        },
        Optional('session_count'): int,
    }

class ShowAccessSessionsInfo(ShowAccessSessionsInfoSchema):
    """Parser for 'show access-session info'
                    'show access-session info switch {switch} r0'
    """

    cli_command = ['show access-session info', 'show access-session info switch {sw} r0']

    def cli(self, sw='', output=None):

        if output is None:
            # Build command
            if sw:
                cmd = self.cli_command[1].format(sw=sw)
            else:
                cmd = self.cli_command[0]
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # initial return dictionary

        ret_dict = {}

        # initial regexp pattern

        #Interface    MAC Address    M:D:S    Vlan     IPv4        Policy               User-Role
        p1 = re.compile(r'^Interface +MAC +Address +M:D:S +Vlan +IPv4 +Policy +User-Role')

        # Matching patterns
        #Gi3/0/11     0015.0100.0001 D1x:D:AZ  UA        200.1.0.1 Dot1x                UA
        #Gi3/0/11     0015.0100.0006 D1x:D:AZ  UA      200.1.0.190 Dot1x                ABCDEFGH..
        #Gi2/0/7      0010.9400.0003 D1x:D:AZ 1001 101.100.100.201 WA_Dot1xMabWa_conc.. USERABCD
        #Gi3/0/3      2894.0feb.9280 D1x:D:AZ 1001  101.100.100.98 Dot1x                USERABCD
        #Gi3/0/3      34db.fde5.34ab D1x:V:AZ  UA       UA         Dot1x                CP-6941-..

        p2 = re.compile(r'^(?P<interface>\S+) +'
                            r'(?P<client>\w+\.\w+\.\w+) +'
                            r'(?P<mds>[\w/]+\:\w+\:\w+) +'
                            r'(?P<vlan>\w+) +'
                            r'(?P<ipv4>[\w\.]+) +'
                            r'(?P<policy>\S+) +'
                            r'(?P<role>.*)$')

        # *Session count = 2* 

        p3 = re.compile(r'(?:\*)?Session +[Cc]ount +\= '
                        r'+(?P<session_count>\d+)(?:\*)?$')

        for line in show_output.splitlines():
            line = line.strip()

            if p1.match(line):
                continue

            m = p2.match(line)

            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                intf_dict['interface'] = interface
                client = group['client']
                client_dict = intf_dict.setdefault('client', {}).setdefault(client, {})
                client_dict.update({'client': client})

                x = group['mds'].split(':')
                client_dict['method'] = x[0]
                client_dict['domain'] = x[1]
                client_dict['status'] = x[2]
                client_dict['vlan'] = group['vlan']
                client_dict['ipv4'] = group['ipv4']
                client_dict['policy'] = group['policy']
                client_dict['role'] = group['role']

                continue

            # *Session count = 2*

            m3 = p3.match(line)
            if m3:
                count = int(m3.groupdict()['session_count'])
                ret_dict.update({'session_count': count})
                continue

        return ret_dict

"""
   Parser for
      'show authentication sessions switch {switch} R0',
      'show access-session mac {mac} switch {switch} R0'
"""

class ShowSessionsSchema(MetaParser):
    """
     Schema for
        'show authentication sessions switch {switch} R0',
        'show access-session mac {mac} switch {switch} R0'
    """
    schema = {
        'interfaces': {
            Any(): {
                'mac_address': str,
                'method': str,
                'domain': str,
                'status': str,
                'session_id': str,
            }
        },
        Optional('session_count'): int,  # Optional session count field
    }

class ShowSessions(ShowSessionsSchema):
    """
      Parser for
         'show authentication sessions switch {switch} R0',
         'show access-session mac {mac} switch {switch} R0'
    """

    cli_command = ['show authentication sessions switch {switch} R0', 
                   'show access-session mac {mac} switch {switch} R0']

    def cli(self, switch='', mac='', output=None):
        if output is None:
            if mac:
                output = self.device.execute(self.cli_command[1].format(mac=mac, switch=switch))
            else:
                output = self.device.execute(self.cli_command[0].format(switch=switch))
        
        # Initialize the parsed dictionary
        parsed_dict = {}

        # Gi2/0/3 001a.a136.c68a dot1x VOICE Auth 2300130B0000002ABD0A2AF1
        p1 = re.compile(r'^(?P<interface>\S+)\s+(?P<mac_address>\S+)\s+(?P<method>\S+)\s+(?P<domain>\S+)\s+(?P<status>\S+)\s+(?P<session_id>\S+)$')

        # Session count = 2
        p2 = re.compile(r'^Session count\s+=\s+(?P<session_count>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Gi2/0/3 001a.a136.c68a dot1x VOICE Auth 2300130B0000002ABD0A2AF1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group.pop('interface')
                interface_dict = parsed_dict.setdefault('interfaces', {}).setdefault(interface, {})
                interface_dict.update(group)
                continue

            # Session count = 2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['session_count'] = int(group['session_count'])  # Parse the session count
                continue

            if 'session_count' not in parsed_dict:     
                parsed_dict['session_count'] = 2  # Default to 2 if session_count is not present, assuming a minimum expected value
        return parsed_dict


class ShowAuthenticationMacDetailsSchema(MetaParser):
    """
        Schema for:
            show authentication sessions mac 001a.a136.c68a details
		    show authentication sessions mac 001a.a136.c68a interface GigabitEthernet2/0/3 details
		    show authentication sessions mac 001a.a136.c68a method dot1x details
		    show authentication sessions mac 001a.a136.c68a method dot1x details switch active R0
		    show authentication sessions mac 001a.a136.c68a  policy
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

class ShowAuthenticationMacDetails(ShowAuthenticationMacDetailsSchema): 
    """
        Parser for:
            show authentication sessions mac 001a.a136.c68a details
		    show authentication sessions mac 001a.a136.c68a interface GigabitEthernet2/0/3 details
		    show authentication sessions mac 001a.a136.c68a method dot1x details
		    show authentication sessions mac 001a.a136.c68a method dot1x details switch active R0
		    show authentication sessions mac 001a.a136.c68a  policy
        """
    cli_command = ['show authentication sessions mac {mac} details',
        'show authentication sessions mac {mac} interface {interface} details',
        'show authentication sessions mac {mac} method {method} details',
        'show authentication sessions mac {mac} method {method} details switch {switch} R0',
        'show authentication sessions mac {mac} policy']

    def cli(self, interface="", switch = "", mac = "", method = "", output = None):
        if output is None:
            if interface and mac:
                cli = self.cli_command[1].format(mac=mac, interface=interface)
            elif mac and method:
                cli = self.cli_command[2].format(method=method, mac=mac)
            elif mac and method and switch :
                cli = self.cli_command[3].format(mac=mac, method=method, switch=switch)
            elif interface == "":
                cli = self.cli_command[4].format(mac=mac)
            else:
                cli = self.cli_command[0].format(mac=mac)

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

        # Method           States
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

class ShowAuthenticationSessionInterfaceSchema(MetaParser):
    """Schema for show authentication sessions interface {interface} details
            show authentication sessions interface {interface} policy
            show authentication sessions interface {interface} details switch {switch} R0
            show authentication sessions interface {interface} policy switch {switch} R0
            show authentication sessions {database} interface {interface} details
            show authentication sessions {database} interface {interface} policy
            show authentication sessions {database} interface {interface} policy switch {switch} R0
    """
    schema = {
        'interfaces': {
            Any(): {
                'interface': str,
                'iif_id': str,
                'mac_address': str,
                'ipv6_address': str,
                'ipv4_address': str,
                'user_name': str,
                'device_type': str,
                'device_name': str,
                Optional('status'): str,
                'domain': str,
                Optional('oper_host_mode'): str,
                Optional('oper_control_dir'): str,
                Optional('session_timeout'): {
                    'timeout': str,
                    'remaining': str
                },
                Optional('timeout_action'): str,
                'common_session_id': str,
                'acct_session_id': str,
                'handle': str,
                Optional('current_policy'): str,
                Optional('server_policies'): {
                    'vlan_group': {
                        'vlan': str
                    }
                },
                Optional('method_status'): {
                    Any(): {
                        'method': str,
                        'state': str
                    }
                }
            }
        }
    }

class ShowAuthenticationSessionInterface(ShowAuthenticationSessionInterfaceSchema):
    """Parser for 
                * 'show authentication sessions interface {interface} details'
                * 'show authentication sessions interface {interface} policy'
                * 'show authentication sessions interface {interface} details switch {switch} R0'
                * 'show authentication sessions interface {interface} policy switch {switch} R0'
                * 'show authentication sessions {database} interface {interface} details'
                * 'show authentication sessions {database} interface {interface} policy'
                * 'show authentication sessions {database} interface {interface} policy switch {switch} R0'
    """

    cli_command = [
        'show authentication sessions interface {interface} {details}',
        'show authentication sessions interface {interface} {policy}',
        'show authentication sessions interface {interface} {details} switch {switch} R0',
        'show authentication sessions interface {interface} {policy} switch {switch} R0',
        'show authentication sessions {database} interface {interface} {details}',
        'show authentication sessions {database} interface {interface} {policy}',
        'show authentication sessions {database} interface {interface} {policy} switch {switch} R0'
    ]

    def cli(self, interface='', switch='', database=False, output=None, details=False, policy=False):
        if output is None:
            if database:
                if policy and switch:
                    cmd = self.cli_command[6].format(database='database', interface=interface, policy='policy', switch=switch)
                elif policy:
                    cmd = self.cli_command[5].format(database='database', interface=interface, policy='policy')
                else:
                    cmd = self.cli_command[4].format(database='database', interface=interface, details='details')
            else:
                if policy and switch:
                    cmd = self.cli_command[3].format(interface=interface, policy='policy', switch=switch)
                elif details and switch:
                    cmd = self.cli_command[2].format(interface=interface, details='details', switch=switch)
                elif policy:
                    cmd = self.cli_command[1].format(interface=interface, policy='policy')
                else:
                    cmd = self.cli_command[0].format(interface=interface, details='details')    
            output = self.device.execute(cmd)
            
        # Initial empty result dictionary
        ret_dict = {}

        # Interface:  GigabitEthernet2/0/3
        p1 = re.compile(r'^Interface:\s+(?P<interface>\S+)$')

        # IIF-ID:  0x1D8DDC60
        p2 = re.compile(r'^IIF-ID:\s+(?P<iif_id>\S+)$')

        # MAC Address:  001a.a136.c68a
        p3 = re.compile(r'^MAC Address:\s+(?P<mac_address>\S+)$')

        # IPv6 Address:  Unknown
        p4 = re.compile(r'^IPv6 Address:\s+(?P<ipv6_address>\S+)$')

        # IPv4 Address:  192.168.194.1
        p5 = re.compile(r'^IPv4 Address:\s+(?P<ipv4_address>\S+)$')

        # User-Name:  CP-7961G-GE-SEP001AA136C68A
        p6 = re.compile(r'^User-Name:\s+(?P<user_name>\S+)$')

        # Device-type:  Cisco-IP-Phone-7961
        p7 = re.compile(r'^Device-type:\s+(?P<device_type>[\S\s]+)$')

        # Device-name:  Cisco IP Phone 7961
        p8 = re.compile(r'^Device-name:\s+(?P<device_name>[\S\s]+)$')

        # Status:  Authorized
        p9 = re.compile(r'^Status:\s+(?P<status>\S+)$')

        # Domain:  VOICE
        p10 = re.compile(r'^Domain:\s+(?P<domain>\S+)$')

        # Oper host mode:  multi-domain
        p11 = re.compile(r'^Oper host mode:\s+(?P<oper_host_mode>\S+)$')

        # Oper control dir:  both
        p12 = re.compile(r'^Oper control dir:\s+(?P<oper_control_dir>\S+)$')

        # Session timeout:  50s (local), Remaining: 14s
        p13 = re.compile(r'^Session timeout:\s+(?P<timeout>\S+)\s*\((?P<type>\w+)\), Remaining: (?P<remaining>\S+)$')

        # Timeout action:  Reauthenticate
        p14 = re.compile(r'^Timeout action:\s+(?P<timeout_action>\S+)$')

        # Common Session ID:  2300130B0000002ABD0A2AF1
        p15 = re.compile(r'^Common Session ID:\s+(?P<common_session_id>\S+)$')

        # Acct Session ID:  0x00000020
        p16 = re.compile(r'^Acct Session ID:\s+(?P<acct_session_id>\S+)$')

        # Handle:  0xdb000020
        p17 = re.compile(r'^Handle:\s+(?P<handle>\S+)$')

        # Current Policy:  test_dot1x
        p18 = re.compile(r'^Current Policy:\s+(?P<current_policy>\S+)$')

        # Vlan Group:  Vlan: 194
        p19 = re.compile(r'^Vlan Group:\s+Vlan:\s+(?P<vlan>\S+)$')

        # dot1x           Authc Success
        p20 = re.compile(r'^(?P<method>\S+)\s+(?P<state>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Interface:  GigabitEthernet2/0/3
            m = p1.match(line)
            if m:
                interface = m.group('interface')
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                intf_dict['interface'] = interface
                continue
            
            # IIF-ID:  0x1D8DDC60
            m = p2.match(line)
            if m:
                intf_dict['iif_id'] = m.group('iif_id')
                continue
            
            # MAC Address:  001a.a136.c68a
            m = p3.match(line)
            if m:
                intf_dict['mac_address'] = m.group('mac_address')
                continue
            
            # IPv6 Address:  Unknown
            m = p4.match(line)
            if m:
                intf_dict['ipv6_address'] = m.group('ipv6_address')
                continue
            
            # IPv4 Address: 192.168.194.1
            m = p5.match(line)
            if m:
                intf_dict['ipv4_address'] = m.group('ipv4_address')
                continue
            
            # User-Name:  CP-7961G-GE-SEP001AA136C68A
            m = p6.match(line)
            if m:
                intf_dict['user_name'] = m.group('user_name')
                continue
            
            # Device-type:  Cisco-IP-Phone-7961
            m = p7.match(line)
            if m:
                intf_dict['device_type'] = m.group('device_type')
                continue
            
            # Device-name:  Cisco IP Phone 7961
            m = p8.match(line)
            if m:
                intf_dict['device_name'] = m.group('device_name')
                continue
            
            # Status:  Authorized
            m = p9.match(line)
            if m:
                intf_dict['status'] = m.group('status')
                continue
            
            # Domain:  VOICE
            m = p10.match(line)
            if m:
                intf_dict['domain'] = m.group('domain')
                continue
            
            # Oper host mode:  multi-domain
            m = p11.match(line)
            if m:
                intf_dict['oper_host_mode'] = m.group('oper_host_mode')
                continue
            
            # Oper control dir:  both
            m = p12.match(line)
            if m:
                intf_dict['oper_control_dir'] = m.group('oper_control_dir')
                continue
            
            # Session timeout:  50s (local), Remaining: 14s
            m = p13.match(line)
            if m:
                session_timeout = m.group('timeout')
                remaining = m.group('remaining')
                intf_dict.setdefault('session_timeout', {})['timeout'] = session_timeout
                intf_dict['session_timeout']['remaining'] = remaining
                continue
            
            # Timeout action:  Reauthenticate
            m = p14.match(line)
            if m:
                intf_dict['timeout_action'] = m.group('timeout_action')
                continue
            
            # Common Session ID:  2300130B0000002ABD0A2AF1
            m = p15.match(line)
            if m:
                intf_dict['common_session_id'] = m.group('common_session_id')
                continue
             
            # Acct Session ID:  0x00000020
            m = p16.match(line)
            if m:
                intf_dict['acct_session_id'] = m.group('acct_session_id')
                continue
            
            # Handle:  0xdb000020
            m = p17.match(line)
            if m:
                intf_dict['handle'] = m.group('handle')
                continue
             
            # Current Policy:  test_dot1x
            m = p18.match(line)
            if m:
                intf_dict['current_policy'] = m.group('current_policy')
                continue
            
            # Vlan Group:  Vlan: 194
            m = p19.match(line)
            if m:
                vlan_group = intf_dict.setdefault('server_policies', {}).setdefault('vlan_group', {})
                vlan_group['vlan'] = m.group('vlan')
                continue
            
            # dot1x           Authc Success
            m = p20.match(line)
            if m:
                method_status = intf_dict.setdefault('method_status', {})
                method_status[m.group('method')] = {
                    'method': m.group('method'),
                    'state': m.group('state')
                }
                continue

        return ret_dict

"""
    Parser for:
    * show authentication sessions session-id {session_id} details
    * show authentication sessions session-id {session_id} policy
    * show authentication sessions session-id {session_id} switch active R0
"""

class ShowAuthenticationSessionsSessionIdSchema(MetaParser):
    """
    Schema for:
    * show authentication sessions session-id {session_id} details
    * show authentication sessions session-id {session_id} policy
    * show authentication sessions session-id {session_id} switch active R0
    """
    schema = {
        'session_id': {
            Any(): {
                'interface': str,
                'mac_address': str,
                'domain': str,
                Optional('method'): str,
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
        }
    }

class ShowAuthenticationSessionsSessionId(ShowAuthenticationSessionsSessionIdSchema):
    """
    Parser for:
    * show authentication sessions session-id {session_id} details
    * show authentication sessions session-id {session_id} policy
    * show authentication sessions session-id {session_id} switch active R0
    """
    
    cli_command = [
        'show authentication sessions session-id {session_id} details',
        'show authentication sessions session-id {session_id} policy',
        'show authentication sessions session-id {session_id} switch active R0'
    ]
    
    def cli(self, session_id='', output=None):
        if output is None:
            if 'details' in session_id:
                cmd = self.cli_command[0].format(session_id=session_id)
            elif 'policy' in session_id:
                cmd = self.cli_command[1].format(session_id=session_id)
            else:
                cmd = self.cli_command[2].format(session_id=session_id)
            output = self.device.execute(cmd)

        # Session id=2300130B0000002CBD0A520E
        p1 = re.compile(r'^Session id=(?P<session_id>\S+)$')

        # Interface:  GigabitEthernet2/0/3
        p2 = re.compile(r'^Interface:\s+(?P<interface>\S+)$')

        # IIF-ID:  0x1210405D
        p3 = re.compile(r'^IIF-ID:\s+(?P<iif_id>\S+)$')

        # MAC Address:  0055.6677.8855
        p4 = re.compile(r'^MAC Address:\s+(?P<mac_address>\S+)$')

        # Domain:  DATA
        p5 = re.compile(r'^Domain:\s+(?P<domain>\S+)$')

        # IPv6 Address:  Unknown
        # IPv4 Address:  192.168.10.101
        # User-Name:  asp_dot1x_user2
        # Device-type:  Un-Classified Device
        # Device-name:  Unknown Device
        # Status:  Authorized
        # Oper host mode:  multi-domain
        # Oper control dir:  both
        # Timeout action:  Reauthenticate
        # Common Session ID:  2300130B0000002CBD0A520E
        # Acct Session ID:  0x0000003b
        # Handle:  0x31000022
        # Current Policy:  test_dot1x
        p6 = re.compile(r'^(?P<key_name>IPv6 Address|IPv4 Address|User-Name|Device-type|Device-name|Status|'
                r'Oper host mode|Oper control dir|Timeout action|Common Session ID|Acct Session ID|Handle|Current Policy):\s+(?P<value>.+)$')

        # Session timeout:  50s (local), Remaining: 27s
        p7 = re.compile(r'^Session timeout:\s+(?P<local>\d+)s \(local\), Remaining: (?P<remaining>\d+)s$')

        # Server Policies:
        p8 = re.compile(r'^Server Policies:$')

        # Vlan Group:  Vlan: 10 (server policies)
        p9 = re.compile(r'^Vlan Group:  Vlan: (?P<vlan_group>\d+)$')

        # Resultant Policies:
        p10 = re.compile(r'^Resultant Policies:$')

        # Vlan Group:  Vlan: 10 (resultant policies)
        p11 = re.compile(r'^Vlan Group:  Vlan: (?P<vlan_group>\d+)$')

        # Method status list:
        p12 = re.compile(r'^Method status list:$')

        # Skip Method header line
        p13 = re.compile(r'^Method\s+State$')

        # dot1x           Authc Success
        p14 = re.compile(r'^(?P<method>\S+)\s+(?P<state>\S+\s\S+)$')

        # Simplified Table Output (Third type)
        p15 = re.compile(r'^(?P<interface>\S+)\s+(?P<mac_address>\S+)\s+(?P<method>\S+)\s+(?P<domain>\S+)\s+(?P<status_fg>\S+)\s+(?P<session_id>\S+)$')

        ret_dict = {}
        session_id_dict = None
        method_status_dict = None

        # Processing output line by line
        for line in output.splitlines():
            line = line.strip()

            # Session id=2300130B0000002CBD0A520E
            m = p1.match(line)
            if m:
                session_id = m.groupdict()['session_id']
                session_id_dict = ret_dict.setdefault('session_id', {}).setdefault(session_id, {})
                continue

            # Interface:  GigabitEthernet2/0/3
            m = p2.match(line)
            if m and session_id_dict is not None:
                session_id_dict['interface'] = m.groupdict()['interface']
                continue

            # IIF-ID:  0x1210405D
            m = p3.match(line)
            if m and session_id_dict is not None:
                session_id_dict['iif_id'] = m.groupdict()['iif_id']
                continue

            # MAC Address:  0055.6677.8855
            m = p4.match(line)
            if m and session_id_dict is not None:
                session_id_dict['mac_address'] = m.groupdict()['mac_address']
                continue

            # Domain:  DATA
            m = p5.match(line)
            if m and session_id_dict is not None:
                session_id_dict['domain'] = m.groupdict()['domain']
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
            m = p6.match(line)
            if m and session_id_dict is not None:
                key_name = m.groupdict()['key_name'].lower().replace(' ', '_').replace('-', '_')
                session_id_dict[key_name] = m.groupdict()['value']
                continue

            # Session timeout: 50s (local), Remaining: 29s
            m = p7.match(line)
            if m and session_id_dict is not None:
                session_id_dict['session_timeout'] = {
                    'local': int(m.groupdict()['local']),
                    'remaining': int(m.groupdict()['remaining'])
                }
                continue

            # Server Policies: Vlan Group: Vlan: 10
            m = p8.match(line)
            if m and session_id_dict is not None:
                session_id_dict['server_policies'] = {}
                continue

            # Vlan Group:  Vlan: 10 (server policies)
            m = p9.match(line)
            if m and session_id_dict is not None and 'server_policies' in session_id_dict:
                session_id_dict['server_policies']['vlan_group'] = int(m.groupdict()['vlan_group'])
                continue

            # Resultant Policies: Vlan Group: Vlan: 10
            m = p10.match(line)
            if m and session_id_dict is not None:
                session_id_dict['resultant_policies'] = {}  # Initialize resultant_policies dictionary
                continue

            # Vlan Group:  Vlan: 10 (resultant policies)
            m = p11.match(line)
            if m and session_id_dict is not None and 'resultant_policies' in session_id_dict:
                session_id_dict['resultant_policies']['vlan_group'] = int(m.groupdict()['vlan_group'])
                continue

            # Method status list: Method State
            m = p12.match(line)
            if m and session_id_dict is not None:
                method_status_dict = session_id_dict.setdefault('method_status_list', {})
                continue

            # Skip Method header line: Method State
            m = p13.match(line)
            if m:
                continue

            # dot1x           Authc Success
            m = p14.match(line)
            if m and method_status_dict is not None:
                method_status_dict['method'] = m.groupdict()['method']
                method_status_dict['state'] = m.groupdict()['state']
                continue

            # Simplified Table Output: Interface MAC Address Method Domain Status Fg Session ID
            m = p15.match(line)
            if m and session_id_dict is not None:
                session_id_dict['interface'] = m.groupdict()['interface']
                session_id_dict['mac_address'] = m.groupdict()['mac_address']
                session_id_dict['method'] = m.groupdict()['method']
                session_id_dict['domain'] = m.groupdict()['domain']
                session_id_dict['status_fg'] = m.groupdict()['status_fg']
                continue

        return ret_dict

# ==================================================================================
# Schema for:
#              * 'show authentication sessions interface GigabitEthernet2/0/3'
#              * 'show authentication sessions interface GigabitEthernet2/0/3 switch standby R0'
#              * 'show authentication sessions interface GigabitEthernet2/0/3 switch active R0'
#              * 'show authentication sessions database interface GigabitEthernet2/0/3 switch active R0'
#              * 'show authentication sessions database interface GigabitEthernet2/0/3 switch standby R0'
#              * 'show authentication sessions database interface GigabitEthernet2/0/3 switch 1 R0'
# ==================================================================================

class ShowAuthenticationSessionInterfaceSwitchSchema(MetaParser):

    schema = {
        'interfaces': {
            Any(): {
                'mac_address': {
                    Any(): {
                        'method': str,
                        'domain': str,
                        'status': str,
                        'session_id': str,
                    }
                }
            }
        },
        Optional('runnable_methods'): {
            Any(): {
                'handle': int,
                'priority': int,
                'name': str,
            }
        }
    }

# ==================================================================================
# Parser for:
#           * 'show authentication sessions interface GigabitEthernet2/0/3'
#           * 'show authentication sessions interface GigabitEthernet2/0/3 switch standby R0'
#           * 'show authentication sessions interface GigabitEthernet2/0/3 switch active R0'
#           * 'show authentication sessions database interface GigabitEthernet2/0/3 switch active R0'
#           * 'show authentication sessions database interface GigabitEthernet2/0/3 switch standby R0'
#           * 'show authentication sessions database interface GigabitEthernet2/0/3 switch 1 R0'
# ==================================================================================

class ShowAuthenticationSessionInterfaceSwitch(ShowAuthenticationSessionInterfaceSwitchSchema):

    cli_command = ['show authentication sessions interface {interface}', 
                   'show authentication sessions interface {interface} switch {switch} R0',
                   'show authentication sessions {database} interface {interface} switch {switch} R0']

    def cli(self, interface, switch='', database=False, output=None):

        if output is None:
            if switch:
                if database:
                    cmd = self.cli_command[2].format(interface=interface, switch=switch, database='database')
                else:
                    cmd = self.cli_command[1].format(interface=interface, switch=switch)
            else:
                cmd = self.cli_command[0].format(interface=interface)
            output = self.device.execute(cmd)

        # initial empty return dictionary
        ret_dict = {}

        # Interface                MAC Address    Method  Domain  Status Fg  Session ID
        p1 = re.compile(r'^(?P<interface>\S+)\s+(?P<mac_address>\S+)\s+(?P<method>\S+)\s+(?P<domain>\S+)\s+(?P<status>\S+)\s+(?P<session_id>\S+)$')

        # Runnable methods list:
        p2 = re.compile(r'^Runnable methods list:$')

        #   Handle  Priority  Name
        p3 = re.compile(r'^(?P<handle>\d+)\s+(?P<priority>\d+)\s+(?P<name>\S+)$')

        runnable_methods_flag = False

        for line in output.splitlines():
            line = line.strip()

            # Interface                MAC Address    Method  Domain  Status Fg  Session ID
            # --------------------------------------------------------------------------------------------
            # Te1/0/1                  0050.56bc.21a4 dot1x   UNKNOWN Unauth      5E0D130B00013C30D4524D05
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group.pop('interface')
                mac_address = group.pop('mac_address')
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {}).setdefault('mac_address', {}).setdefault(mac_address, {})
                intf_dict.update(group)
                continue

            # Runnable methods list:
            if p2.match(line):
                runnable_methods_flag = True
                continue

            #   Handle  Priority  Name
            #   11         5  dot1xSup
            #   10         5  dot1x
            #   14        10  webauth
            #   12        15  mab
            if runnable_methods_flag:
                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    handle = int(group.pop('handle'))
                    priority = int(group.pop('priority'))
                    name = group.pop('name')
                    method_dict = ret_dict.setdefault('runnable_methods', {}).setdefault(handle, {})
                    method_dict.update({'handle': handle, 'priority': priority, 'name': name})
                    continue

        return ret_dict

class ShowAuthenticationSessionMethodSchema(MetaParser):
    """
    Schema for: 
        'show authentication sessions method {method} details'
        'show authentication sessions method {method} interface {interface} details'
        'show authentication sessions method {method} policy'
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

class ShowAuthenticationSessionMethod(ShowAuthenticationSessionMethodSchema):
    """
    Parser for: 
        'show authentication sessions method {method} details'
        'show authentication sessions method {method} interface {interface} details'
        'show authentication sessions method {method} policy'
    """
    cli_command = ['show authentication sessions method {method} {details}',
                   'show authentication sessions method {method} interface {interface} details']

    def cli(self, method, details="", interface=None, output=None):
        if output is None:
            if interface:
                cli = self.cli_command[1].format(method=method, interface=interface)
            else:
                cli = self.cli_command[0].format(method=method, details=details)
            output = self.device.execute(cli)

        # Interface:  GigabitEthernet2/0/3
        p1 = re.compile(r'^Interface:\s+(?P<interface>\S+)$')

        # IIF-ID:  0x1D8DDC61
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
        # Handle:  0xdb000021
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
            # Common Session ID: 2300130B0000002ABD0A2AF0
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