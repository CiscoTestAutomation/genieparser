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
Gi1/48     0015.63b0.f676  dot1x    DATA     Authz Success  0A3462B1000000102983C05C
Gi1/5      000f.23c4.a401  mab      DATA     Authz Success  0A3462B10000000D24F80B58
Gi1/5      0014.bf5d.d26d  dot1x    DATA     Authz Success  0A3462B10000000E29811B94
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
        }
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
        # Gi1/48     0015.63b0.f676  dot1x    DATA     Authz Success  0A3462B1000000102983C05C
        # Gi1/5      000f.23c4.a401  mab      DATA     Authz Success  0A3462B10000000D24F80B58
        # Gi1/5      0014.bf5d.d26d  dot1x    DATA     Authz Success  0A3462B10000000E29811B94
        p4 = re.compile(r'^(?P<interface>\S+) +'
                        '(?P<client>\w+\.\w+\.\w+) +'
                        '(?P<method>\w+) +'
                        '(?P<domain>\w+) +'
                        '(?P<status>\w+(?: +\w+)?) +'
                        '(?P<session>\w+)$')

        for line in out.splitlines():
            line = line.strip()

            # Ignore the title
            if p1.match(line) or p2.match(line):
                continue

            # Gi1/0/48     0015.63b0.f676  dot1x    DATA     Authz Success  0A3462B1000000102983C05C
            # Gi1/7/35  0000.0022.2222 dot1x  UNKNOWN Auth      141927640000000E0B40EDB0
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

        return ret_dict


# ==================================================================================
# Parser for 'show authentication sessions interface {interface} details'
# ==================================================================================
class ShowAuthenticationSessionsInterfaceDetailsSchema(MetaParser):
    """Schema for 'show authentication sessions interface {interface} details'
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
                        Optional('restart_timeout'): str,
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
                        Optional('local_policies'): {
                            'template': {
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
                        'method_status': {
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


class ShowAuthenticationSessionsInterfaceDetails(ShowAuthenticationSessionsInterfaceDetailsSchema):
    """Parser for 'show authentication sessions interface {interface} details'
    """
    cli_command = 'show authentication sessions interface {interface} details'

    def cli(self, interface, output=None):

        if not output:
            # get output from device
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        # Interface:  GigabitEthernet3/0/2
        # IIF-ID:  0x1055240000001F6 
        # MAC Address:  0010.0010.0001
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

        p1 = re.compile(r'^(?P<argument>[\w\s\-]+): +(?P<value>[\w\s\-\.\./]+)$')

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

        # initial return dictionary
        ret_dict = {}
        hold_dict = {}
        mac_dict = {}

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

                security_dict = mac_dict.setdefault('local_policies', {})
                if group['security_name'] == 'Policy':
                    security_dict.update(
                        {'security_policy': group['policy_status']})
                elif group['security_name'] == 'Status':
                    security_dict.update(
                        {'security_status': group['policy_status']})

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

            # match these lines:
            #             Interface:  GigabitEthernet3/0/2
            #                IIF-ID:  0x1055240000001F6 
            #           MAC Address:  0010.0010.0001
            #          IPv6 Address:  Unknown
            #          IPv4 Address:  192.0.2.1
            #             User-Name:  auto601
            #                Status:  Authorized
            #                Domain:  DATA
            #        Oper host mode:  single-host
            #      Oper control dir:  both
            #       Session timeout:  N/A
            #     Common Session ID:  AC14FC0A0000101200E28D62
            #       Acct Session ID:  Unknown
            #                Handle:  0xDB003227
            #        Current Policy:  dot1x_dvlan_reauth_hm
            #         Authorized By:  Guest Vlan
            #                Status:  Authz Success

            m = p1.match(line)
            if m:
                group = m.groupdict()

                key = re.sub(r'( |-)', '_', group['argument'].lower())

                # to keep pv4_address as common key
                if key == 'ip_address':
                    key = 'ipv4_address'

                if 'interfaces' in ret_dict.keys():
                    if key == 'mac_address':
                        mac_dict = intf_dict.setdefault(group['value'], {})
                    elif key == 'iif_id':
                        hold_dict.update({'argument': key, 'value': group['value']})
                    else:
                        if hold_dict:
                            mac_dict.update({key: group['value']})
                            tmp_keys = hold_dict.pop('argument')
                            tmp_values = hold_dict.pop('value')
                            mac_dict.update({tmp_keys: tmp_values})
                        else:
                            if key != 'interface':
                                mac_dict.update({key: group['value']})
                else:
                    intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(group['value'], \
                                                                                 {}).setdefault('mac_address', {})

                # else:
                #     if key != 'interface':
                #         hold_dict.update({group['value']: key})

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

        return ret_dict
