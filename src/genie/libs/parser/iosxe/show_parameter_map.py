"""show_parameter-map.py
    * 'show parameter-map type inspect {param}'
    * 'show parameter-map type inspect-zone {zone}'
    * 'show parameter-map type inspect-global'
    * 'show parameter-map type inspect-vrf {vrf}'
"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

class ShowParameterMapTypeInspectParamSchema(MetaParser):
    """Schema for show parameter-map type inspect {param}"""
    schema = {
        'log_dropped_packet': str,
        'log_flow': str,
        'icmp_unreachable': str,
        'audit_trail': str,
        'alert': str,
        'max_incomplete': {
            'level': str,
            'value': str,
        },
        'one_minute': {
            'level': str,
            'value': str,
        },
        'sessions_rate': {
            'level': str,
            'value': str,
        },
        'udp': {
            'idle_time': int,
            'ageout_time': int,
            'halfopen_idle_time': int,
            'halfopen_ageout_time': int,
        },
        'icmp': {
            'idle_time': int,
            'ageout_time': int,
        },
        'dns_timeout': int,
        'tcp': {
            'window_scaling_enforcement': str,
            'idle_time': int,
            'ageout_time': int,
            'finwait_time': int,
            'synwait_time': int,
            'half_open': str,
            'half_close': str,
            'idle': str,
            'max_incomplete_host': str,
            'block_time': int,
        },
        'zone_mismatch_drop': str,
        'application_inspect': str,
        'sessions_maximum': str,
        'number_of_packet_per_flow': str,
    }

class ShowParameterMapTypeInspectParam(ShowParameterMapTypeInspectParamSchema):
    """Parser for show parameter-map type inspect {param}"""

    cli_command = 'show parameter-map type inspect {param}'

    def cli(self, param='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(param=param))

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing each line
	#log dropped-packet off
        p1 = re.compile(r'^log dropped-packet (?P<log_dropped_packet>\S+)$')
		
	#log flow off
        p2 = re.compile(r'^log flow (?P<log_flow>\S+)$')
		
	#icmp unreachable drop
        p3 = re.compile(r'^icmp unreachable (?P<icmp_unreachable>\S+)$')
		
	#audit-trail off
        p4 = re.compile(r'^audit-trail (?P<audit_trail>\S+)$')
		
	#alert on
        p5 = re.compile(r'^alert (?P<alert>\S+)$')
		
	#max-incomplete low  unlimited
	#max-incomplete high unlimited
        p6 = re.compile(r'^max-incomplete (?P<level>\S+) (?P<value>\S+)$')
		
	#one-minute low  unlimited
	#one-minute high unlimited
        p7 = re.compile(r'^one-minute (?P<level>\S+) (?P<value>\S+)$')
		
	#sessions rate low  unlimited
	#sessions rate high unlimited
        p8 = re.compile(r'^sessions rate (?P<level>\S+) +(?P<value>\S+)$')
		
	#udp idle-time 30 ageout-time 30
        p9 = re.compile(r'^udp idle-time +(?P<idle_time>\d+) +ageout-time +(?P<ageout_time>\d+)$')
		
	#udp halfopen idle-time 30000 ms ageout-time 30000 ms
        p10 = re.compile(r'^udp halfopen idle-time +(?P<halfopen_idle_time>\d+) ms ageout-time +(?P<halfopen_ageout_time>\d+) ms$')
		
	#icmp idle-time 10 ageout-time 10
        p11 = re.compile(r'^icmp idle-time +(?P<idle_time>\d+) +ageout-time +(?P<ageout_time>\d+)$')
		
	#dns-timeout 5
        p12 = re.compile(r'^dns-timeout +(?P<dns_timeout>\d+)$')
		
	#tcp window scaling enforcement loose on
        p13 = re.compile(r'^tcp window scaling enforcement loose (?P<window_scaling_enforcement>\S+)$')
		
	#zone-mismatch drop off
        p14 = re.compile(r'^zone-mismatch drop (?P<zone_mismatch_drop>\S+)$')
		
	#application-inspect all
        p15 = re.compile(r'^application-inspect (?P<application_inspect>\S+)$')
		
	#tcp idle-time 3600 ageout-time 3600
        p16 = re.compile(r'^tcp idle-time +(?P<idle_time>\d+) +ageout-time +(?P<ageout_time>\d+)$')
		
	#tcp finwait-time 1 ageout-time 1
        p17 = re.compile(r'^tcp finwait-time +(?P<finwait_time>\d+) +ageout-time +(?P<ageout_time>\d+)$')
		
	#tcp synwait-time 30 ageout-time 30
        p18 = re.compile(r'^tcp synwait-time +(?P<synwait_time>\d+) +ageout-time +(?P<ageout_time>\d+)$')
		
	#tcp half-open on, half-close on, idle on
        p19 = re.compile(r'^tcp half-open (?P<half_open>\S+), half-close (?P<half_close>\S+), idle (?P<idle>\S+)$')
		
	#tcp max-incomplete host unlimited block-time 0
        p20 = re.compile(r'^tcp max-incomplete host (?P<max_incomplete_host>\S+) block-time (?P<block_time>\d+)$')
		
	#sessions maximum unlimited
        p21 = re.compile(r'^sessions maximum (?P<sessions_maximum>\S+)$')
		
	#number of packet per flow default
        p22 = re.compile(r'^number of packet per flow (?P<number_of_packet_per_flow>\S+)$')

        # Iterate over each line in the output
        for line in output.splitlines():
            line = line.strip()

            # Match each line with the corresponding regex
            #log dropped-packet off
            m = p1.match(line)
            if m:
                parsed_dict['log_dropped_packet'] = m.group('log_dropped_packet')
                continue

            #log flow off
            m = p2.match(line)
            if m:
                parsed_dict['log_flow'] = m.group('log_flow')
                continue

            #icmp unreachable drop
            m = p3.match(line)
            if m:
                parsed_dict['icmp_unreachable'] = m.group('icmp_unreachable')
                continue

            #audit-trail off
            m = p4.match(line)
            if m:
                parsed_dict['audit_trail'] = m.group('audit_trail')
                continue

            #alert on
            m = p5.match(line)
            if m:
                parsed_dict['alert'] = m.group('alert')
                continue

            #max-incomplete low  unlimited
            m = p6.match(line)
            if m:
                max_incomplete = parsed_dict.setdefault('max_incomplete', {})
                max_incomplete['level'] = m.group('level')
                max_incomplete['value'] = m.group('value')
                continue

            #one-minute low  unlimited
            m = p7.match(line)
            if m:
                one_minute = parsed_dict.setdefault('one_minute', {})
                one_minute['level'] = m.group('level')
                one_minute['value'] = m.group('value')
                continue

            #sessions rate low  unlimited
            m = p8.match(line)
            if m:
                sessions_rate = parsed_dict.setdefault('sessions_rate', {})
                sessions_rate['level'] = m.group('level')
                sessions_rate['value'] = m.group('value')
                continue

            #udp idle-time 30 ageout-time 30
            m = p9.match(line)
            if m:
                udp = parsed_dict.setdefault('udp', {})
                udp['idle_time'] = int(m.group('idle_time'))
                udp['ageout_time'] = int(m.group('ageout_time'))
                continue

            #udp halfopen idle-time 30000 ms ageout-time 30000 ms
            m = p10.match(line)
            if m:
                udp = parsed_dict.setdefault('udp', {})
                udp['halfopen_idle_time'] = int(m.group('halfopen_idle_time'))
                udp['halfopen_ageout_time'] = int(m.group('halfopen_ageout_time'))
                continue

            #icmp idle-time 10 ageout-time 10
            m = p11.match(line)
            if m:
                icmp = parsed_dict.setdefault('icmp', {})
                icmp['idle_time'] = int(m.group('idle_time'))
                icmp['ageout_time'] = int(m.group('ageout_time'))
                continue

            #dns-timeout 5
            m = p12.match(line)
            if m:
                parsed_dict['dns_timeout'] = int(m.group('dns_timeout'))
                continue

            #tcp window scaling enforcement loose on
            m = p13.match(line)
            if m:
                tcp = parsed_dict.setdefault('tcp', {})
                tcp['window_scaling_enforcement'] = m.group('window_scaling_enforcement')
                continue

            #zone-mismatch drop off
            m = p14.match(line)
            if m:
                parsed_dict['zone_mismatch_drop'] = m.group('zone_mismatch_drop')
                continue

            #application-inspect all
            m = p15.match(line)
            if m:
                parsed_dict['application_inspect'] = m.group('application_inspect')
                continue

            #tcp idle-time 3600 ageout-time 3600
            m = p16.match(line)
            if m:
                tcp = parsed_dict.setdefault('tcp', {})
                tcp['idle_time'] = int(m.group('idle_time'))
                tcp['ageout_time'] = int(m.group('ageout_time'))
                continue

            #tcp finwait-time 1 ageout-time 1
            m = p17.match(line)
            if m:
                tcp = parsed_dict.setdefault('tcp', {})
                tcp['finwait_time'] = int(m.group('finwait_time'))
                tcp['ageout_time'] = int(m.group('ageout_time'))
                continue

            #tcp synwait-time 30 ageout-time 30
            m = p18.match(line)
            if m:
                tcp = parsed_dict.setdefault('tcp', {})
                tcp['synwait_time'] = int(m.group('synwait_time'))
                tcp['ageout_time'] = int(m.group('ageout_time'))
                continue

            #tcp half-open on, half-close on, idle on
            m = p19.match(line)
            if m:
                tcp = parsed_dict.setdefault('tcp', {})
                tcp['half_open'] = m.group('half_open')
                tcp['half_close'] = m.group('half_close')
                tcp['idle'] = m.group('idle')
                continue

            #tcp max-incomplete host unlimited block-time 0
            m = p20.match(line)
            if m:
                tcp = parsed_dict.setdefault('tcp', {})
                tcp['max_incomplete_host'] = m.group('max_incomplete_host')
                tcp['block_time'] = int(m.group('block_time'))
                continue

            #sessions maximum unlimited
            m = p21.match(line)
            if m:
                parsed_dict['sessions_maximum'] = m.group('sessions_maximum')
                continue

            #number of packet per flow default
            m = p22.match(line)
            if m:
                parsed_dict['number_of_packet_per_flow'] = m.group('number_of_packet_per_flow')
                continue

        return parsed_dict

class ShowParameterMapTypeInspectZoneSchema(MetaParser):
    """Schema for show parameter-map type inspect-zone {zone_name}"""
    schema = {
        'parameter_map': {
            'type': str,
            'name': str,
            Optional('tcp_syn_flood_rate'): int,
            Optional('max_destination'): int,
            Optional('alert'): str,
            Optional('threat_detection'): str,
        }
    }


class ShowParameterMapTypeInspectZone(ShowParameterMapTypeInspectZoneSchema):
    """Parser for show parameter-map type inspect-zone {zone_name}"""

    cli_command = ['show parameter-map type inspect-zone',
                   'show parameter-map type inspect-zone {zone_name}']

    def cli(self, zone_name='', output=None):
        if output is None:
            if zone_name:
                output = self.device.execute(self.cli_command[1].format(zone_name=zone_name))
            else:
                output = self.device.execute(self.cli_command[0])

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing each line
        # parameter-map type inspect-zone test-zone
        p1 = re.compile(r'^\s*parameter-map\s+type\s+(?P<type>inspect-zone)\s+(?P<name>\S+)\s*$')
        
        # tcp syn-flood-rate 10
        p2 = re.compile(r'^\s*tcp\s+syn-flood-rate\s+(?P<tcp_syn_flood_rate>\d+)\s*$')
        
        # max-destination 10000
        p3 = re.compile(r'^\s*max-destination\s+(?P<max_destination>\d+)\s*$')
        
        # alert off
        p4 = re.compile(r'^\s*alert\s+(?P<alert>\S+)\s*$')
        
        # threat detection disabled
        p5 = re.compile(r'^\s*threat\s+detection\s+(?P<threat_detection>\S+)\s*$')

        # Iterate over each line in the output
        for line in output.splitlines():
            line = line.strip()

            # parameter-map type inspect-zone test-zone
            m = p1.match(line)
            if m:
                parameter_map_dict = parsed_dict.setdefault('parameter_map', {})
                parameter_map_dict['type'] = m.group('type')
                parameter_map_dict['name'] = m.group('name')
                continue

            # tcp syn-flood-rate 10
            m = p2.match(line)
            if m:
                parsed_dict['parameter_map']['tcp_syn_flood_rate'] = int(m.group('tcp_syn_flood_rate'))
                continue

            # max-destination 10000
            m = p3.match(line)
            if m:
                parsed_dict['parameter_map']['max_destination'] = int(m.group('max_destination'))
                continue

            # alert off
            m = p4.match(line)
            if m:
                parsed_dict['parameter_map']['alert'] = m.group('alert')
                continue

            # threat detection disabled
            m = p5.match(line)
            if m:
                parsed_dict['parameter_map']['threat_detection'] = m.group('threat_detection')
                continue

        return parsed_dict

class ShowParameterMapInspectGlobalSchema(MetaParser):
    schema = {
        'parameter_map_type_inspect_global': {
            'log_dropped_packet': str,
            'log_flow': str,
            'log_flow_export_fnf': str,
            Optional('log_flow_export_template_timeout_rate'): int,
            'alert': str,
            'lisp_inner_packet_inspection': str,
            'multi_tenancy': str,
            'icmp_unreachable': str,
            'session_reclassify': str,
        },
        'vpn_zone_security': str,
        'vpn_disallow_dia': {
            'aggressive_aging': str,
            'syn_flood_limit': str,
            'tcp_window_scaling_enforcement': str,
            'zone_mismatch_drop': str,
            'max_incomplete': str,
            'max_incomplete_tcp': str,
            'max_incomplete_udp': str,
            'max_incomplete_icmp': str,
            'application_inspect': str,
            'vrf_inspect': str,
        }
    }

# Implement the parser class
class ShowParameterMapInspectGlobal(ShowParameterMapInspectGlobalSchema):
    cli_command = 'show parameter-map type inspect-global'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Define regular expressions with examples
        # "log dropped-packet enabled"
        p1 = re.compile(r'^log dropped-packet (\S+)$')

        # "no log flow"
        p2 = re.compile(r'^no log flow$')

        # "no log flow-export fnf"
        p3 = re.compile(r'^no log flow-export fnf$')

        # "log flow-export template timeout-rate 60"
        p4 = re.compile(r'^log flow-export template timeout-rate (\d+)$')

        # "alert enabled"
        p5 = re.compile(r'^alert (\S+)$')

        # "lisp inner packet inspection enabled"
        p6 = re.compile(r'^lisp inner packet inspection (\S+)$')

        # "multi-tenancy enabled"
        p7 = re.compile(r'^multi-tenancy (\S+)$')

        # "icmp unreachable enabled"
        p8 = re.compile(r'^icmp unreachable (\S+)$')

        # "Session reclassify enabled"
        p9 = re.compile(r'^Session reclassify (\S+)$')

        # "vpn zone security enabled"
        p10 = re.compile(r'^vpn zone security (\S+)$')

        # "vpn disallow dia"
        p11 = re.compile(r'^vpn disallow dia$')

        # "aggressive aging enabled"
        p12 = re.compile(r'^aggressive aging (\S+)$')

        # "syn_flood_limit 100"
        p13 = re.compile(r'^syn_flood_limit\s+(\S+)$')

        # "tcp window scaling enforcement always enabled"
        p14 = re.compile(r'^tcp window scaling enforcement\s+(\S+ \S+)$')

        # "zone-mismatch drop enabled"
        p15 = re.compile(r'^zone-mismatch drop (\S+)$')

        # "max incomplete 10"
        p16 = re.compile(r'^max incomplete (\S+)')

        # "max_incomplete TCP 20"
        p17 = re.compile(r'^max_incomplete TCP (\S+)$')

        # "max_incomplete UDP 15"
        p18 = re.compile(r'^max_incomplete UDP (\S+)$')

        # "max_incomplete ICMP 5"
        p19 = re.compile(r'^max_incomplete ICMP (\S+)$')

        # "application-inspect enabled"
        p20 = re.compile(r'^application-inspect (\S+)$')

        # "vrf default inspect enabled"
        p21 = re.compile(r'^vrf default inspect (\S+)$')

        # Parse the output
        for line in output.splitlines():
            line = line.strip()

            # Match each line against the regular expressions

            #"log dropped-packet enabled"
            m = p1.match(line)
            if m:
                parameter_map_type_inspect_global = parsed_dict.setdefault('parameter_map_type_inspect_global', {})
                parameter_map_type_inspect_global['log_dropped_packet'] = m.group(1)
                continue

            #"no log flow"
            m = p2.match(line)
            if m:
                parameter_map_type_inspect_global['log_flow'] = 'no'
                continue

            #"no log flow-export fnf"
            m = p3.match(line)
            if m:
                parameter_map_type_inspect_global['log_flow_export_fnf'] = 'no'
                continue

            #"log flow-export template timeout-rate 60"
            m = p4.match(line)
            if m:
                parameter_map_type_inspect_global['log_flow_export_template_timeout_rate'] = int(m.group(1))
                continue

            #"alert enabled"
            m = p5.match(line)
            if m:
                parameter_map_type_inspect_global['alert'] = m.group(1)
                continue

            #"lisp inner packet inspection enabled"
            m = p6.match(line)
            if m:
                parameter_map_type_inspect_global['lisp_inner_packet_inspection'] = m.group(1)
                continue

            #"multi-tenancy enabled"
            m = p7.match(line)
            if m:
                parameter_map_type_inspect_global['multi_tenancy'] = m.group(1)
                continue

            #"icmp unreachable enabled"
            m = p8.match(line)
            if m:
                parameter_map_type_inspect_global['icmp_unreachable'] = m.group(1)
                continue

            #"Session reclassify enabled"
            m = p9.match(line)
            if m:
                parameter_map_type_inspect_global['session_reclassify'] = m.group(1)
                continue

            #"vpn zone security enabled"
            m = p10.match(line)
            if m:
                vpn_zone_security = parsed_dict.setdefault('vpn_zone_security', {})
                parsed_dict['vpn_zone_security'] = m.group(1)
                continue

            #"vpn disallow dia"
            m = p11.match(line)
            if m:
                continue

            #"aggressive aging enabled"
            m = p12.match(line)
            if m:
                vpn_disallow_dia = parsed_dict.setdefault('vpn_disallow_dia', {})
                vpn_disallow_dia['aggressive_aging'] = m.group(1)
                continue

            #"syn_flood_limit 100"
            m = p13.match(line)
            if m:
                vpn_disallow_dia['syn_flood_limit'] = m.group(1)
                continue

            #"tcp window scaling enforcement always enabled"
            m = p14.match(line)
            if m:
                vpn_disallow_dia['tcp_window_scaling_enforcement'] = m.group(1)
                continue

            #"zone-mismatch drop enabled"
            m = p15.match(line)
            if m:
                vpn_disallow_dia['zone_mismatch_drop'] = m.group(1)
                continue

            #"max incomplete 10"
            m = p16.match(line)
            if m:
                vpn_disallow_dia['max_incomplete'] = m.group(1)
                continue

            #"max_incomplete TCP 20"
            m = p17.match(line)
            if m:
                vpn_disallow_dia['max_incomplete_tcp'] = m.group(1)
                continue

            #"max_incomplete UDP 15"
            m = p18.match(line)
            if m:
                vpn_disallow_dia['max_incomplete_udp'] = m.group(1)
                continue

            #"max_incomplete ICMP 5"
            m = p19.match(line)
            if m:
                vpn_disallow_dia['max_incomplete_icmp'] = m.group(1)
                continue

            #"application-inspect enabled"
            m = p20.match(line)
            if m:
                vpn_disallow_dia['application_inspect'] = m.group(1)
                continue

            #"vrf default inspect enabled"
            m = p21.match(line)
            if m:
                vpn_disallow_dia['vrf_inspect'] = m.group(1)
                continue

        return parsed_dict


# ======================================================
# Schema for 'show parameter-map type inspect-vrf {vrf}'
# ======================================================

class ShowParameterMapTypeInspectVrfSchema(MetaParser):
    """Schema for show parameter-map type inspect-vrf {vrf}"""
    schema = {
        'parameter_map': {
            'type': str,
            'name': str,
            Optional('refcount'): int,
            Optional('total_session'): str,
            Optional('aggressive_aging'): str,
            Optional('tcp_syn_flood_limit'): str,
            Optional('alert'): str,
            Optional('max_incomplete'): str,
            Optional('max_incomplete_tcp'): str,
            Optional('max_incomplete_udp'): str,
            Optional('max_incomplete_icmp'): str,
        }
    }


# ======================================================
# Parser for 'show parameter-map type inspect-vrf {vrf}'
# ======================================================

class ShowParameterMapTypeInspectVrf(ShowParameterMapTypeInspectVrfSchema):
    """Parser for show parameter-map type inspect-vrf {vrf}"""

    cli_command = 'show parameter-map type inspect-vrf {vrf}'

    def cli(self, vrf='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vrf=vrf))

        # Initialize the result dictionary
        parsed_dict = {}

        # Define regular expressions for parsing
        # parameter-map type inspect-vrf test_vrf (refcount = 1)
        p1 = re.compile(r'^\s*parameter-map\s+type\s+(?P<type>inspect-vrf)\s+(?P<name>\S+)\s+\(refcount\s+=\s+(?P<refcount>\d+)\)\s*$')
        
        # total_session unlimited
        p2 = re.compile(r'^\s*total_session\s+(?P<total_session>\S+)\s*$')
        
        # aggressive aging disabled
        p3 = re.compile(r'^\s*aggressive\s+aging\s+(?P<aggressive_aging>\S+)\s*$')
        
        # tcp syn_flood_limit unlimited
        p4 = re.compile(r'^\s*tcp\s+syn_flood_limit\s+(?P<tcp_syn_flood_limit>\S+)\s*$')
        
        # alert on
        p5 = re.compile(r'^\s*alert\s+(?P<alert>\S+)\s*$')
        
        # max_incomplete 1000
        p6 = re.compile(r'^\s*max_incomplete\s+(?P<max_incomplete>\S+)\s*$')
        
        # max_incomplete TCP unlimited
        p7 = re.compile(r'^\s*max_incomplete\s+TCP\s+(?P<max_incomplete_tcp>\S+)\s*$')
        
        # max_incomplete UDP unlimited
        p8 = re.compile(r'^\s*max_incomplete\s+UDP\s+(?P<max_incomplete_udp>\S+)\s*$')
        
        # max_incomplete ICMP unlimited
        p9 = re.compile(r'^\s*max_incomplete\s+ICMP\s+(?P<max_incomplete_icmp>\S+)\s*$')

        # Iterate over each line in the output
        for line in output.splitlines():
            line = line.strip()

            # parameter-map type inspect-vrf test_vrf (refcount = 1)
            m = p1.match(line)
            if m:
                parameter_map_dict = parsed_dict.setdefault('parameter_map', {})
                parameter_map_dict['type'] = m.group('type')
                parameter_map_dict['name'] = m.group('name')
                parameter_map_dict['refcount'] = int(m.group('refcount'))
                continue

            # total_session unlimited
            m = p2.match(line)
            if m:
                parsed_dict['parameter_map']['total_session'] = m.group('total_session')
                continue

            # aggressive aging disabled
            m = p3.match(line)
            if m:
                parsed_dict['parameter_map']['aggressive_aging'] = m.group('aggressive_aging')
                continue

            # tcp syn_flood_limit unlimited
            m = p4.match(line)
            if m:
                parsed_dict['parameter_map']['tcp_syn_flood_limit'] = m.group('tcp_syn_flood_limit')
                continue

            # alert on
            m = p5.match(line)
            if m:
                parsed_dict['parameter_map']['alert'] = m.group('alert')
                continue

            # max_incomplete 1000
            m = p6.match(line)
            if m:
                parsed_dict['parameter_map']['max_incomplete'] = m.group('max_incomplete')
                continue

            # max_incomplete TCP unlimited
            m = p7.match(line)
            if m:
                parsed_dict['parameter_map']['max_incomplete_tcp'] = m.group('max_incomplete_tcp')
                continue

            # max_incomplete UDP unlimited
            m = p8.match(line)
            if m:
                parsed_dict['parameter_map']['max_incomplete_udp'] = m.group('max_incomplete_udp')
                continue

            # max_incomplete ICMP unlimited
            m = p9.match(line)
            if m:
                parsed_dict['parameter_map']['max_incomplete_icmp'] = m.group('max_incomplete_icmp')
                continue

        return parsed_dict

