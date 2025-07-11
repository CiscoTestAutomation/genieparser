"""show_parameter-map.py
    * 'show parameter-map type inspect {param}'
"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

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
