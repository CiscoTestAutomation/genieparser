"""show_access_seesion.py
   supported commands:
     * show access-session
     * show access-session interface {interface} details
     * show access-session brief
     * show access-session event-logging mac <mac>
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
						ShowAuthenticationSessionsInterfaceDetails

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
        p1 = re.compile(r'^Session +count \= +(?P<val>\d+)$')
        p2 = re.compile(r'^(?P<intf>[\w\/\-\.]+) +'
                         '(?P<client>[\w\.]+) +'
                         '(?P<method>\w+) +'
                         '(?P<domain>\w+) +'
                         '(?P<status>\w+) +'
                         '(?P<session>\w+)$')

        for line in out.splitlines():
            line = line.strip()
            line = line.replace('\t', '    ')
            
            # Session count = 1
            m = p1.match(line)
            if m:
                ret_dict['session_count'] = int(m.groupdict()['val'])
                continue

            # Gi1/0/1                  f4cf.beff.9cb1 dot1x   DATA    Auth        000000000000000BB6FC9EAF
            m = p2.match(line)
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
