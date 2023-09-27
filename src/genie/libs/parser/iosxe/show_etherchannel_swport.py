"""show_etherchannel_swport.py
   supported commands:
     *  show etherchannel swport summary
     *  show etherchannel swport <port_channel> summary
     *  show etherchannel swport load-balancing
     *  show etherchannel swport auto
     *  show etherchannel swport <port-channel> auto
"""
# Python
import re
import random
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         ListOf

# import parser utils
from genie.libs.parser.utils.common import Common

logger = logging.getLogger(__name__)
# ====================================================
#  schema for show etherchannel swport summary
# ====================================================
class ShowEtherChannelSwportSummarySchema(MetaParser):
    """Schema for:
        show etherchannel swport summary
        show etherchannel swport <port-channel> summary
        show etherchannel swport auto
        show etherchannel swport <port-channel> auto
        """

    schema = {
        'number_of_lag_in_use': int,
        'number_of_aggregators': int,
        Optional('interfaces'): {
            Any(): {
                Optional('name'): str,
                Optional('bundle_id'): int,
                Optional('protocol'): str,
                Optional('flags'): str,
                Optional('oper_status'): str,
                Optional('activity'): str,
                Optional('members'): {
                    Any(): {
                        Optional('interface'): str,
                        Optional('flags'): str,
                        Optional('bundled'): bool,                        
                        'port_channel': {
                            'port_channel_member': bool,
                            Optional('port_channel_int'): str,
                        },
                    }
                },
                Optional('port_channel'): {
                    'port_channel_member': bool,
                    'port_channel_member_intfs': ListOf(str),
                },
            },
        }
    }

# ====================================================
#  parser for show etherchannel summary
# ====================================================
class ShowEtherChannelSwportSummary(ShowEtherChannelSwportSummarySchema):
    """Parser for :
      show etherchannel swport summary
      show etherchannel swport <port-channel> summary
      """

    cli_command = [
                  'show etherchannel swport summary',
                  'show etherchannel swport {port_channel} summary',
                ]
    exclude = ['current_time', 'last_read', 'last_write',
        'retrans', 'keepalives', 'total', 'value', 'retransmit', 
        'total_data', 'with_data', 'krtt', 'receive_idletime', 
        'sent_idletime', 'sndnxt', 'snduna', 'sndwnd', 'uptime',
        'ackhold', 'delrcvwnd', 'rcvnxt', 'receive_idletime', 
        'rcvwnd', 'updates', 'down_time', 'last_reset', 
        'notifications', 'opens', 'route_refresh', 'total',
        'updates', 'up_time', 'rtto', 'rtv', 'srtt', 'pmtuager',
        'min_rtt', 'max_rtt', 'dropped', 'established', 
        'reset_reason', 'irs', 'iss', 'tcp_semaphore', 
        'foreign_port', 'status_flags', 'local_port', 
        'keepalive', 'out_of_order']


    def cli(self, port_channel="", output=None):
        if output is None:
            if not port_channel:
                output = self.device.execute(self.cli_command[0])
            else:
                output = self.device.execute(self.cli_command[1].format(port_channel=port_channel))

        # Number of channel-groups in use: 2
        p1 = re.compile(r'^Number\s+of\s+channel-groups\s+in\s+use:\s+(?P<number_of_lag_in_use>\d+)$')
        # Number of aggregators:           2
        p2 = re.compile(r'^Number\s+of\s+aggregators:\s+(?P<number_of_aggregators>\d+)$') 
        # Group  Port-channel  Protocol    Ports
        # ------+-------------+-----------+-----------------------------------------------
        # 1      Po1(SU)         PAgP      Gi0/1(P)    Gi0/2(P)
        p3 = re.compile(r'^\s*(?P<bundle_id>[\d\s]+)(?P<name>[\w\-]+)\((?P<flags>[\w]+)\)?'
                        '( +(?P<protocol>[\w\-]+))?( +((?P<ports>[\w\-\s\/\(\)]+)))?$')
        # Group  Port-channel  Protocol    Ports
        # ------+-------------+-----------+-----------------------------------------------
        # 10     Po10(SU)        PAgP        Gi1/0/15(P)     Gi1/0/16(P)     
        #                                    Gi1/0/17(P)      
        p4 = re.compile(r'^\s*(?P<ports>[\w\-\/\(\)]+)$')
        #                                  Te2/0/3(s)      Te3/0/1(s)
        #                                  Te3/0/2(D)      Te3/0/3(P)
        p5 = re.compile(r'^\s*(?P<port1>[\w\-\/\(\)]+)\s+(?P<port2>[\w\-\/\(\)]+)$')

        ret_dict = {}
        m1 = ""
        for line in output.splitlines():
            line = line.strip()

            # Number of channel-groups in use: 2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'number_of_lag_in_use': int(group.pop('number_of_lag_in_use'))})
                continue

            # Number of aggregators:           2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'number_of_aggregators': int(group.pop('number_of_aggregators'))})
                continue

            # 1      Po1(SU)         PAgP      Gi0/1(P)    Gi0/2(P)
            m = p3.match(line)
            if m:
                protocol = None
                group = m.groupdict()
                name = Common.convert_intf_name(group.pop("name"))
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(name, {})

                intf_dict.update({
                    'name': name,
                    'bundle_id': int(group.pop("bundle_id"))
                })
                if group.get("protocol"):
                    if '-' in group.get("protocol"):
                        protocol = None
                    else:
                        protocol = group.pop("protocol").strip().lower()
                if protocol:
                    intf_dict.update({'protocol': protocol})

                flags = group.pop("flags")
                intf_dict.update({'flags': flags})
                activity = 'auto' if 'a' in flags.lower() else None
                if activity:
                    intf_dict.update({'activity': activity})
                oper_status = 'up' if flags in ['RU', 'SU'] else 'down'
                intf_dict.update({'oper_status': oper_status})

                if group.get('ports'):
                    ports = group.pop('ports').split()

                    # port_channel
                    eth_list = []

                    port_dict = intf_dict.setdefault('members', {})
                    for port in ports:
                        port_value = port.split('(')
                        interface = Common.convert_intf_name(port_value[0])
                        state = port_value[1].replace(')','')
                        eth_list.append(interface)

                        port_item = port_dict.setdefault(interface, {})
                        port_item.update({'interface': interface,
                                          'flags': state,
                                          'bundled': True if state in ['bndl','P'] else False})

                        # port_channel
                        port_item.setdefault('port_channel', {}).update({'port_channel_member': True,
                                                                         'port_channel_int': name})

                    # port_channel
                    if eth_list:
                        port_dict = intf_dict.setdefault('port_channel', {})
                        port_dict['port_channel_member'] = True
                        port_dict['port_channel_member_intfs'] = sorted(eth_list)
                m = ""
                continue

            # 10     Po10(SU)        PAgP        Gi1/0/15(P)     Gi1/0/16(P)
            #                                    Gi1/0/17(P)
            m = p4.match(line)
            if m and intf_dict:
                group = m.groupdict()
                ports = group.pop('ports').split()
                for port in ports:
                    port_value = port.split('(')
                    interface = Common.convert_intf_name(port_value[0])
                    state = port_value[1].replace(')','')
                    eth_list.append(interface)
                    port_item = intf_dict['members'].setdefault(interface, {})

                    port_item.update({'interface': interface,
                                      'flags': state,
                                      'bundled': True if state in ['bndl','P'] else False})

                    # port_channel
                    port_item.setdefault('port_channel', {}).update({'port_channel_member': True,
                                                                     'port_channel_int': name})

                # port_channel
                if eth_list:
                    intf_dict['port_channel']['port_channel_member_intfs'] = sorted(eth_list)
                continue

            #                                  Te2/0/3(s)      Te3/0/1(s)
            #                                  Te3/0/2(D)      Te3/0/3(P)
            m = p5.match(line)
            if m and intf_dict:
                group = m.groupdict()
                ports = [group.pop('port1'), group.pop('port2')]

                for port in ports:
                    port_value = port.split('(')
                    interface = Common.convert_intf_name(port_value[0])
                    state = port_value[1].replace(')', '')
                    eth_list.append(interface)
                    port_item = intf_dict['members'].setdefault(interface, {})

                    port_item.update({'interface': interface,
                                      'flags': state,
                                      'bundled': True if state in ['bndl','P'] else False})

                    # port_channel
                    port_item.setdefault('port_channel', {}).update({'port_channel_member': True,
                                                                     'port_channel_int': name})

                # port_channel
                if eth_list:
                    intf_dict['port_channel']['port_channel_member_intfs'] = sorted(eth_list)
                continue
        return ret_dict

# ====================================================
#  schema for show etherchannel swport load-balance
# ====================================================
class ShowEtherChannelSWLoadBalanceSchema(MetaParser):
    """Schema for:
        show etherchannel swport load-balance"""

    schema = {
        'load_balance_cfg': str,
        'non_ip': str,
        'ipv4': str,
        'ipv6': str,
    }


# ====================================================
#  parser for show etherchannel swport load-balance
# ====================================================
class ShowEtherChannelSWLoadBalance(ShowEtherChannelSWLoadBalanceSchema):
    """Parser for :
      show etherchannel swport load-balance"""

    cli_command = 'show etherchannel swport load-balance'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initialize result dict
        ret_dict = {}
        # EtherChannel Load-Balancing Configuration:
        #       src-ip  
        p1 = re.compile(r'^\s*(?P<load_balance_cfg>\S+)$')
        # EtherChannel Load-Balancing Addresses Used Per-Protocol:
        # Non-IP: Source MAC address 
        p2 = re.compile(r'^Non-IP: (?P<non_ip>.*)$') 
        #   IPv4: Source IP address   
        p3 = re.compile(r'^\s*IPv4: (?P<ipv4>.*)$') 
        #   IPv6: Source IP address 
        p4 = re.compile(r'^\s*IPv6: (?P<ipv6>.*)$')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            #       src-ip
            m = p1.match(line)
            if m:
                load_balance_cfg = m.groupdict()['load_balance_cfg']
                ret_dict.update({'load_balance_cfg': load_balance_cfg})
                continue

            # Non-IP: Source MAC address
            m = p2.match(line)
            if m:
                Non_IP = m.groupdict()['non_ip']
                ret_dict.update({'non_ip': Non_IP})
                continue

            #   IPv4: Source IP address
            m = p3.match(line)
            if m:
                IPv4 = m.groupdict()['ipv4']
                ret_dict.update({'ipv4': IPv4})
                continue

            #   IPv6: Source IP address
            m = p4.match(line)
            if m:
                IPv6 = m.groupdict()['ipv6']
                ret_dict.update({'ipv6': IPv6})
                continue

        return ret_dict

# ====================================================
#  parser for show etherchannel auto
# ====================================================
class ShowEtherChannelSwportAuto(ShowEtherChannelSwportSummary):
    """Parser for :
      show etherchannel swport auto
      show etherchannel swport <port-channel> auto     
      """

    cli_command = [
                  'show etherchannel swport auto',
                  'show etherchannel swport {port_channel} auto',
                ]
    def cli(self, port_channel="", output=None):
        if output is None:
            if not port_channel:
                show_output = self.device.execute(self.cli_command[0])
            else:
                show_output = self.device.execute(self.cli_command[1].format(port_channel=port_channel))            
        
        # Call super
        return super().cli(output=show_output, port_channel=port_channel)

