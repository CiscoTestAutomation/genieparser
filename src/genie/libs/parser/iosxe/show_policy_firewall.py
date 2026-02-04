"""show_policy_firewall.py

IOSXE parsers for the following show commands:
    * show policy-firewall stats vrf {vrf}
    * show policy-firewall stats zone {zone}
    * show policy-firewall sessions platform destination-port {port}
    * show policy-firewall stats global
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ======================================================
# Schema for 'show policy-firewall stats vrf {vrf}'
# ======================================================
class ShowPolicyFirewallStatsVrfSchema(MetaParser):
    """Schema for show policy-firewall stats vrf {vrf}"""
    
    schema = {
        'vrf': {
            Any(): {
                'parameter_map': str,
                'interface_reference_count': int,
                'total_session_count': int,
                'total_session_exceed': int,
                'total_session_aggressive_aging_period': str,
                'total_session_event_count': int,
                'half_open': {
                    'protocol_stats': {
                        Any(): {  # Protocol name (All, UDP, ICMP, TCP)
                            'session_count': int,
                            'exceed': int
                        }
                    },
                    'tcp_syn_flood_half_open_count': int,
                    'tcp_syn_flood_exceed': int,
                    'half_open_aggressive_aging_period': str,
                    'half_open_event_count': int
                }
            }
        }
    }


# ======================================================
# Parser for 'show policy-firewall stats vrf {vrf}'
# ======================================================
class ShowPolicyFirewallStatsVrf(ShowPolicyFirewallStatsVrfSchema):
    """Parser for show policy-firewall stats vrf {vrf}"""

    cli_command = 'show policy-firewall stats vrf {vrf}'

    def cli(self, vrf="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vrf=vrf))

        ret_dict = {}

        # VRF: green, Parameter-Map: vrf-pmap
        p1 = re.compile(r'^VRF:\s+(?P<vrf>\S+),\s+Parameter-Map:\s+(?P<parameter_map>\S+)$')

        # Interface reference count: 2
        p2 = re.compile(r'^Interface\s+reference\s+count:\s+(?P<interface_reference_count>\d+)$')

        # Total Session Count(estab + half-open): 20, Exceed: 0
        p3 = re.compile(r'^Total\s+Session\s+Count\(estab\s+\+\s+half-open\):\s+(?P<total_session_count>\d+),\s+Exceed:\s+(?P<total_session_exceed>\d+)$')

        # Total Session Aggressive Aging Period Off, Event Count: 0
        p4 = re.compile(r'^Total\s+Session\s+Aggressive\s+Aging\s+Period\s+(?P<aggressive_aging_period>Off|On),\s+Event\s+Count:\s+(?P<event_count>\d+)$')

        # Protocol Session Cnt     Exceed
        # All      20              0
        # UDP      0               0
        # ICMP     0               0
        # TCP      20              0
        p5 = re.compile(r'^(?P<protocol>All|UDP|ICMP|TCP)\s+(?P<session_count>\d+)\s+(?P<exceed>\d+)$')

        # TCP Syn Flood Half Open Count: 20, Exceed: 834
        p6 = re.compile(r'^TCP\s+Syn\s+Flood\s+Half\s+Open\s+Count:\s+(?P<tcp_syn_flood_count>\d+),\s+Exceed:\s+(?P<tcp_syn_flood_exceed>\d+)$')

        # Half Open Aggressive Aging Period Off, Event Count: 0
        p7 = re.compile(r'^Half\s+Open\s+Aggressive\s+Aging\s+Period\s+(?P<half_open_aging_period>Off|On),\s+Event\s+Count:\s+(?P<half_open_event_count>\d+)$')

        current_vrf = None

        for line in output.splitlines():
            line = line.strip()

            # VRF: green, Parameter-Map: vrf-pmap
            m = p1.match(line)
            if m:
                vrf_name = m.group('vrf')
                parameter_map = m.group('parameter_map')
                current_vrf = ret_dict.setdefault('vrf', {}).setdefault(vrf_name, {})
                current_vrf['parameter_map'] = parameter_map
                continue

            # Interface reference count: 2
            m = p2.match(line)
            if m and current_vrf is not None:
                current_vrf['interface_reference_count'] = int(m.group('interface_reference_count'))
                continue

            # Total Session Count(estab + half-open): 20, Exceed: 0
            m = p3.match(line)
            if m and current_vrf is not None:
                current_vrf['total_session_count'] = int(m.group('total_session_count'))
                current_vrf['total_session_exceed'] = int(m.group('total_session_exceed'))
                continue

            # Total Session Aggressive Aging Period Off, Event Count: 0
            m = p4.match(line)
            if m and current_vrf is not None:
                current_vrf['total_session_aggressive_aging_period'] = m.group('aggressive_aging_period')
                current_vrf['total_session_event_count'] = int(m.group('event_count'))
                continue

            # Protocol Session Cnt     Exceed
            m = p5.match(line)
            if m and current_vrf is not None:
                protocol = m.group('protocol')
                session_count = int(m.group('session_count'))
                exceed = int(m.group('exceed'))
                
                half_open_dict = current_vrf.setdefault('half_open', {})
                protocol_stats_dict = half_open_dict.setdefault('protocol_stats', {})
                protocol_dict = protocol_stats_dict.setdefault(protocol, {})
                protocol_dict['session_count'] = session_count
                protocol_dict['exceed'] = exceed
                continue

            # TCP Syn Flood Half Open Count: 20, Exceed: 834
            m = p6.match(line)
            if m and current_vrf is not None:
                half_open_dict = current_vrf.setdefault('half_open', {})
                half_open_dict['tcp_syn_flood_half_open_count'] = int(m.group('tcp_syn_flood_count'))
                half_open_dict['tcp_syn_flood_exceed'] = int(m.group('tcp_syn_flood_exceed'))
                continue

            # Half Open Aggressive Aging Period Off, Event Count: 0
            m = p7.match(line)
            if m and current_vrf is not None:
                half_open_dict = current_vrf.setdefault('half_open', {})
                half_open_dict['half_open_aggressive_aging_period'] = m.group('half_open_aging_period')
                half_open_dict['half_open_event_count'] = int(m.group('half_open_event_count'))
                continue

        return ret_dict


# ======================================================
# Schema for 'show policy-firewall stats zone {zone}'
# ======================================================
class ShowPolicyFirewallStatsZoneSchema(MetaParser):
    """Schema for show policy-firewall stats zone {zone}"""

    schema = {
        'zone': {
            Any(): {
                'parameter_map': str,
                'tcp_syn_packet_conform_limit': int,
                'tcp_syn_packet_exceed_limit': int,
                'threat_detection_statistics': {
                    'syn_attack': {
                        'average_eps': int,
                        'current_eps': int,
                        'threats': int,
                        'total_events': int
                    },
                    'fw_inspect': {
                        'average_eps': int,
                        'current_eps': int,
                        'threats': int,
                        'total_events': int
                    },
                    'fw_policy': {
                        'average_eps': int,
                        'current_eps': int,
                        'threats': int,
                        'total_events': int
                    }
                }
            }
        }
    }


# ======================================================
# Parser for 'show policy-firewall stats zone {zone}'
# ======================================================
class ShowPolicyFirewallStatsZone(ShowPolicyFirewallStatsZoneSchema):
    """Parser for show policy-firewall stats zone {zone}"""

    cli_command = 'show policy-firewall stats zone {zone}'

    def cli(self, zone="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(zone=zone))

        ret_dict = {}

        # Zone: zone1
        p1 = re.compile(r'^Zone:\s+(?P<zone>\S+)$')

        # Parameter-map: pmap-zone
        p2 = re.compile(r'^Parameter-map:\s+(?P<parameter_map>\S+)$')

        # TCP SYN packet conform limit: 79
        p3 = re.compile(r'^TCP\s+SYN\s+packet\s+conform\s+limit:\s+(?P<tcp_syn_conform_limit>\d+)$')

        # TCP SYN packet exceed limit: 609
        p4 = re.compile(r'^TCP\s+SYN\s+packet\s+exceed\s+limit:\s+(?P<tcp_syn_exceed_limit>\d+)$')

        # 10-min SYN attack:      0               0               0               0
        p5 = re.compile(r'^10-min\s+SYN\s+attack:\s+(?P<syn_avg>\d+)\s+(?P<syn_current>\d+)\s+(?P<syn_threats>\d+)\s+(?P<syn_events>\d+)$')

        # 10-min FW inspect:      0               0               0               0
        p6 = re.compile(r'^10-min\s+FW\s+inspect:\s+(?P<fw_inspect_avg>\d+)\s+(?P<fw_inspect_current>\d+)\s+(?P<fw_inspect_threats>\d+)\s+(?P<fw_inspect_events>\d+)$')

        # 10-min FW policy:       0               0               0               0
        p7 = re.compile(r'^10-min\s+FW\s+policy:\s+(?P<fw_policy_avg>\d+)\s+(?P<fw_policy_current>\d+)\s+(?P<fw_policy_threats>\d+)\s+(?P<fw_policy_events>\d+)$')

        current_zone = None

        for line in output.splitlines():
            line = line.strip()

            # Zone: zone1
            m = p1.match(line)
            if m:
                zone_name = m.group('zone')
                current_zone = ret_dict.setdefault('zone', {}).setdefault(zone_name, {})
                continue

            # Parameter-map: pmap-zone
            m = p2.match(line)
            if m and current_zone is not None:
                current_zone['parameter_map'] = m.group('parameter_map')
                continue

            # TCP SYN packet conform limit: 79
            m = p3.match(line)
            if m and current_zone is not None:
                current_zone['tcp_syn_packet_conform_limit'] = int(m.group('tcp_syn_conform_limit'))
                continue

            # TCP SYN packet exceed limit: 609
            m = p4.match(line)
            if m and current_zone is not None:
                current_zone['tcp_syn_packet_exceed_limit'] = int(m.group('tcp_syn_exceed_limit'))
                continue

            # 10-min SYN attack:      0               0               0               0
            m = p5.match(line)
            if m and current_zone is not None:
                threat_stats = current_zone.setdefault('threat_detection_statistics', {})
                syn_attack = threat_stats.setdefault('syn_attack', {})
                syn_attack['average_eps'] = int(m.group('syn_avg'))
                syn_attack['current_eps'] = int(m.group('syn_current'))
                syn_attack['threats'] = int(m.group('syn_threats'))
                syn_attack['total_events'] = int(m.group('syn_events'))
                continue

            # 10-min FW inspect:      0               0               0               0
            m = p6.match(line)
            if m and current_zone is not None:
                threat_stats = current_zone.setdefault('threat_detection_statistics', {})
                fw_inspect = threat_stats.setdefault('fw_inspect', {})
                fw_inspect['average_eps'] = int(m.group('fw_inspect_avg'))
                fw_inspect['current_eps'] = int(m.group('fw_inspect_current'))
                fw_inspect['threats'] = int(m.group('fw_inspect_threats'))
                fw_inspect['total_events'] = int(m.group('fw_inspect_events'))
                continue

            # 10-min FW policy:       0               0               0               0
            m = p7.match(line)
            if m and current_zone is not None:
                threat_stats = current_zone.setdefault('threat_detection_statistics', {})
                fw_policy = threat_stats.setdefault('fw_policy', {})
                fw_policy['average_eps'] = int(m.group('fw_policy_avg'))
                fw_policy['current_eps'] = int(m.group('fw_policy_current'))
                fw_policy['threats'] = int(m.group('fw_policy_threats'))
                fw_policy['total_events'] = int(m.group('fw_policy_events'))
                continue

        return ret_dict

# ===================================================
# Schema for 'show policy-firewall sessions platform v6-source-address'
# ===================================================

class ShowPolicyFirewallSessionsPlatformV6SourceAddressSchema(MetaParser):
    """Schema for 'show policy-firewall sessions platform v6-source-address'"""
    
    schema = {
        Optional('platform_command'): str,
        Optional('session_legend'): {
            's': str,
            'i': str,
            'c': str,
            'd': str,
            'u': str,
            'A/D': str
        },
        Optional('sessions'): {
            Any(): {
                'session_id': str,
                'source_address': str,
                'source_port': str,
                'destination_address': str,
                'destination_port': str,
                'protocol': str,
                'protocol_info': str,
                'protocol_detail': str,
                'channels': str,
                'session_value': str
            }
        }
    }

# ===================================================
# Parser for 'show policy-firewall sessions platform v6-source-address'
# ===================================================

class ShowPolicyFirewallSessionsPlatformV6SourceAddress(ShowPolicyFirewallSessionsPlatformV6SourceAddressSchema):
    """Parser for 'show policy-firewall sessions platform v6-source-address'"""
    
    cli_command = 'show policy-firewall sessions platform v6-source-address {address}'
    
    def cli(self, address='', output=None):
        if output is None:
            if address:
                output = self.device.execute(self.cli_command.format(address=address))
        else:
            output = output
            
        # Initialize parsed dictionary
        parsed_dict = {}
        
        # Parse platform command line
        # --show platform hardware qfp active feature firewall datapath scb ipv6 2001:1:0:0:0:0:0:1 --
        p1 = re.compile(r'^--(?P<command>show platform hardware qfp active feature firewall datapath scb ipv6 [\d:]+)\s*--$')
        
        # Parse session legend line
        # [s=session  i=imprecise channel c=control channel  d=data channel u=utd inspect A/D=appfw action allow/deny]
        p2 = re.compile(r'^\[s=(?P<s>.*?)\s+i=(?P<i>.*?)\s+c=(?P<c>.*?)\s+d=(?P<d>.*?)\s+u=(?P<u>.*?)\s+A/D=(?P<ad>.*?)\]$')
 
        # Parse session data line
        # Session ID:0x00000002 2001:1::1 128 2001:2::2 7993 proto 58 (0:0) (0x3:icmp)	[sd] 3046618007
        p3 = re.compile(r'^Session ID:(?P<session_id>\w+)\s+(?P<src_addr>[\da-fA-F:]+)\s+(?P<src_port>\d+)\s+(?P<dst_addr>[\da-fA-F:]+)\s+(?P<dst_port>\d+)\s+proto\s+(?P<protocol>\d+)\s+(?P<proto_info>\([^)]+\))\s+(?P<proto_detail>\([^)]+\))\s+(?P<channels>\[[^\]]+\])\s+(?P<session_value>\d+)$')
        
        for line in output.splitlines():
            line = line.strip()
            
            # Match platform command
            # --show platform hardware qfp active feature firewall datapath scb ipv6 2001:1:0:0:0:0:0:1 --
            m = p1.match(line)
            if m:
                parsed_dict['platform_command'] = m.groupdict()['command']
                continue
                
            # Match session legend
            # [s=session  i=imprecise channel c=control channel  d=data channel u=utd inspect A/D=appfw action allow/deny]
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                parsed_dict['session_legend'] = {
                    's': groups['s'].strip(),
                    'i': groups['i'].strip(),
                    'c': groups['c'].strip(), 
                    'd': groups['d'].strip(),
                    'u': groups['u'].strip(),
                    'A/D': groups['ad'].strip()
                }
                continue
                
            # Match session data
            # Session ID:0x00000002 2001:1::1 128 2001:2::2 7993 proto 58 (0:0) (0x3:icmp)	[sd] 3046618007
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                session_id = groups['session_id']
                
                if 'sessions' not in parsed_dict:
                    parsed_dict['sessions'] = {}
                    
                parsed_dict['sessions'][session_id] = {
                    'session_id': session_id,
                    'source_address': groups['src_addr'],
                    'source_port': groups['src_port'],
                    'destination_address': groups['dst_addr'],
                    'destination_port': groups['dst_port'],
                    'protocol': groups['protocol'],
                    'protocol_info': groups['proto_info'],
                    'protocol_detail': groups['proto_detail'],
                    'channels': groups['channels'],
                    'session_value': groups['session_value']
                }
                continue
        
        return parsed_dict

# ======================================================
# Schema for 'show policy-firewall stats global'
# ======================================================
class ShowPolicyFirewallStatsGlobalSchema(MetaParser):
    """Schema for show policy-firewall stats global"""

    schema = {
        'global_per_box_statistics': {
            'total_session_aggressive_aging_period': str,
            'total_session_event_count': int,
            'half_open': {
                'protocol_stats': {
                    Any(): {  # Protocol name (All, UDP, ICMP, TCP)
                        'session_count': int,
                        'exceed': int
                    }
                },
                'tcp_syn_flood_half_open_count': int,
                'tcp_syn_flood_exceed': int,
                'half_open_aggressive_aging_period': str,
                'half_open_event_count': int
            }
        }
    }


# ======================================================
# Parser for 'show policy-firewall stats global'
# ======================================================
class ShowPolicyFirewallStatsGlobal(ShowPolicyFirewallStatsGlobalSchema):
    """Parser for show policy-firewall stats global"""

    cli_command = 'show policy-firewall stats global'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Total Session Aggressive Aging Period On, Event Count: 1
        p1 = re.compile(r'^Total\s+Session\s+Aggressive\s+Aging\s+Period\s+(?P<aggressive_aging_period>On|Off),\s+Event\s+Count:\s+(?P<event_count>\d+)$')

        # Protocol Session Cnt     Exceed
        # All      12              0
        # UDP      12              0
        # ICMP     0               0
        # TCP      0               0
        p2 = re.compile(r'^(?P<protocol>All|UDP|ICMP|TCP)\s+(?P<session_count>\d+)\s+(?P<exceed>\d+)$')

        # TCP Syn Flood Half Open Count: 0, Exceed: 0
        p3 = re.compile(r'^TCP\s+Syn\s+Flood\s+Half\s+Open\s+Count:\s+(?P<tcp_syn_flood_count>\d+),\s+Exceed:\s+(?P<tcp_syn_flood_exceed>\d+)$')

        # Half Open Aggressive Aging Period Off, Event Count: 0
        p4 = re.compile(r'^Half\s+Open\s+Aggressive\s+Aging\s+Period\s+(?P<half_open_aging_period>On|Off),\s+Event\s+Count:\s+(?P<half_open_event_count>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Total Session Aggressive Aging Period On, Event Count: 1
            m = p1.match(line)
            if m:
                global_stats = ret_dict.setdefault('global_per_box_statistics', {})
                global_stats['total_session_aggressive_aging_period'] = m.group('aggressive_aging_period')
                global_stats['total_session_event_count'] = int(m.group('event_count'))
                continue

            # All      12              0
            m = p2.match(line)
            if m:
                protocol = m.group('protocol')
                session_count = int(m.group('session_count'))
                exceed = int(m.group('exceed'))
                
                global_stats = ret_dict.setdefault('global_per_box_statistics', {})
                half_open_dict = global_stats.setdefault('half_open', {})
                protocol_stats_dict = half_open_dict.setdefault('protocol_stats', {})
                protocol_dict = protocol_stats_dict.setdefault(protocol, {})
                protocol_dict['session_count'] = session_count
                protocol_dict['exceed'] = exceed
                continue

            # TCP Syn Flood Half Open Count: 0, Exceed: 0
            m = p3.match(line)
            if m:
                global_stats = ret_dict.setdefault('global_per_box_statistics', {})
                half_open_dict = global_stats.setdefault('half_open', {})
                half_open_dict['tcp_syn_flood_half_open_count'] = int(m.group('tcp_syn_flood_count'))
                half_open_dict['tcp_syn_flood_exceed'] = int(m.group('tcp_syn_flood_exceed'))
                continue

            # Half Open Aggressive Aging Period Off, Event Count: 0
            m = p4.match(line)
            if m:
                global_stats = ret_dict.setdefault('global_per_box_statistics', {})
                half_open_dict = global_stats.setdefault('half_open', {})
                half_open_dict['half_open_aggressive_aging_period'] = m.group('half_open_aging_period')
                half_open_dict['half_open_event_count'] = int(m.group('half_open_event_count'))
                continue

        return ret_dict

class ShowPolicyFirewallSessionsPlatformDestinationPortSchema(MetaParser):
   """Schema for show policy-firewall sessions platform destination-port <port>"""

   schema = {
        'platform_command': str,  # The actual platform command executed
        Optional('legend'): {
            'session': str,     # session description
            'imprecise': str,     # imprecise channel description
            'control': str,     # control channel description
            'data': str,     # data channel description
            'utd': str,     # utd inspect description
            'appfw': str    # appfw action allow/deny description (note: A_D not A/D)
        }
    }

class ShowPolicyFirewallSessionsPlatformDestinationPort(ShowPolicyFirewallSessionsPlatformDestinationPortSchema):
    """Parser for show policy-firewall sessions platform destination-port <port>"""

    cli_command = ['show policy-firewall sessions platform destination-port {port}']
    
    def cli(self, port="", output=None):
        if output is None:
            cmd = self.cli_command[0].format(port=port)
            out = self.device.execute(cmd)
        else:
            out = output

        # Initial return dictionary
        ret_dict = {}

        # --show platform hardware qfp active feature firewall datapath scb any any any 0 any all any --
        p1 = re.compile(r"^--(?P<command>show platform hardware qfp active feature firewall datapath scb any any any 0 any all any)\s*--$")

        # Parse session legend line
        # [s=session  i=imprecise channel c=control channel  d=data channel u=utd inspect A/D=appfw action allow/deny]
        p2 = re.compile(r'^\[s=(?P<s>.*?)\s+i=(?P<i>.*?)\s+c=(?P<c>.*?)\s+d=(?P<d>.*?)\s+u=(?P<u>.*?)\s+A/D=(?P<ad>.*?)\]$')

        for line in out.splitlines():
            line = line.strip()
            
            # Match platform command line
            # --show platform hardware qfp active feature firewall datapath scb any any any 0 any all any --
            m = p1.match(line)
            if m:
                ret_dict['platform_command'] = m.groupdict()['command']
                continue

            # Match legend line
            # [s=session  i=imprecise channel c=control channel  d=data channel u=utd inspect A/D=appfw action allow/deny]
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['legend'] = {
                    'session': groups['s'].strip(),
                    'imprecise': groups['i'].strip(),
                    'control': groups['c'].strip(), 
                    'data': groups['d'].strip(),
                    'utd': groups['u'].strip(),
                    'appfw': groups['ad'].strip()
            }

        return ret_dict
