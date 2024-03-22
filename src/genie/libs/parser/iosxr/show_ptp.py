""" show_ptp.py
IOSXR parsers for the following commands:
    * 'show ptp platform servo'
    * 'show ptp foreign-masters brief'
"""

# Python
import re

# Metaparser
from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowPtpPlatformServoSchema(MetaParser):
    ''' Schema for:
            * 'show ptp platform servo'
    '''

    schema = {
        'platform_servo_stats': {
            'servo_status': str,
            'servo_stat_index': int,
            'device_status': str,
            'servo_mode': str,
            'servo_log_level': int,
            'phase_alignment_accuracy': str,
            'sync_timestamp_updated': int,
            'sync_timestamp_discarded': int,
            'delay_timestamp_updated': int,
            'delay_timestamp_discarded': int,
            'previous_received_timestamp': {
                't1': float,
                't2': float,
                't3': float,
                't4': float
            },
            'last_received_timestamp': {
                't1': float,
                't2': float,
                't3': float,
                't4': float
            },
            'offset_from_master': str,
            'mean_path_delay': str,
            'set_time': int,
            'step_time': int,
            'adjust_freq': int,
            Optional('adjust_freq_time'): int,
            'last_set_time': float,
            'flag': int,
            'last_step_time': int,
            'last_adjust_freq': int
        }
    }


# ================================
# Parser for 'show ptp platform servo'
# ================================
class ShowPtpPlatformServo(ShowPtpPlatformServoSchema):

    cli_command = ['show ptp platform servo']

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # Servo status: Running
        p1 = re.compile(r'^Servo\s+status:\s+(?P<servo_status>[a-zA-Z]+)$')

        # Servo stat_index: 2
        p2 = re.compile(r'^Servo\s+stat_index:\s+(?P<servo_stat_index>\d+)$')

        # Device status: PHASE_LOCKED
        # Device status: FREQ_LOCKED
        p3 = re.compile(r'^Device\s+status:\s+(?P<device_status>[\w]+)$')

        # Servo Mode: Hybrid
        # Servo Mode: Non Hybrid
        p4 = re.compile(r'^Servo\s+Mode:\s+(?P<servo_mode>[a-zA-Z ]+)$')

        # Servo log level: 0
        p5 = re.compile(r'^Servo\s+log\s+level:\s+(?P<servo_log_level>\d+)$')

        # Phase Alignment Accuracy: -8 ns
        # Phase Alignment Accuracy: -17034645174 ns
        p6 = re.compile(r'^Phase\s+Alignment\s+Accuracy:\s+(?P<phase_alignment_accuracy>[-\w ]+)$')

        # Sync timestamp updated: 9848934
        p7 = re.compile(r'^Sync\s+timestamp\s+updated:\s+(?P<sync_timestamp_updated>\d+)$')

        # Sync timestamp discarded: 0
        p8 = re.compile(r'^Sync\s+timestamp\s+discarded:\s+(?P<sync_timestamp_discarded>\d+)$')

        # Delay timestamp updated: 9848973
        p9 = re.compile(r'^Delay\s+timestamp\s+updated:\s+(?P<delay_timestamp_updated>\d+)$')

        # Delay timestamp discarded: 0
        p10 = re.compile(r'^Delay\s+timestamp\s+discarded:\s+(?P<delay_timestamp_discarded>\d+)$')

        # Previous Received Timestamp T1: 1674467002.900294787  T2: 1674467002.900304552  T3: 1674467002.905436033  T4: 1674467002.905445830
        p11 = re.compile(r'^Previous\s+Received\s+Timestamp\s+T1:\s+(?P<t1>[\d.]+)\s+T2:\s+(?P<t2>[\d.]+)\s+T3:\s+(?P<t3>[\d.]+)\s+T4:\s+(?P<t4>[\d.]+)$')

        # Last Received Timestamp T1: 1671703729.684676938 T2: 1671703746.719324326 T3: 1671703746.779917501 T4: 1671703729.745274543
        p12 = re.compile(r'^Last\s+Received\s+Timestamp\s+T1:\s+(?P<t1>[\d.]+)\s+T2:\s+(?P<t2>[\d.]+)\s+T3:\s+(?P<t3>[\d.]+)\s+T4:\s+(?P<t4>[\d.]+)$')

        # Offset from master: 17 secs, 34645173 nsecs
        # Offset from master: -0 secs, 22 nsecs
        p13 = re.compile(r'^Offset\s+from\s+master:\s+(?P<offset_from_master>[-\w ]+),\s+\d+\s+nsecs$')

        # Mean path delay : 0 secs, 2215 nsecs
        # Mean path delay   :  0 secs, 9732 nsecs
        p14 = re.compile(r'^Mean\s+path\s+delay\s+:\s+(?P<mean_path_delay>[\w ]+),\s+\d+\s+nsecs$')

        # setTime():1854 stepTime():7989 adjustFreq():789 adjustFreqTime():437113
        # setTime():2  stepTime():1  adjustFreq():420942 adjustFreqTime():0
        # setTime():0  stepTime():0 adjustFreq():0
        p15 = re.compile(r'^setTime\(\):(?P<set_time>\d+)\s+stepTime\(\):(?P<step_time>\d+)\s+adjustFreq\(\):(?P<adjust_freq>\d+)(?:\s+adjustFreqTime\(\):(?P<adjust_freq_time>\d+))?$')

        # Last setTime: 1.000000000 flag:0 Last stepTime:262310484, Last adjustFreq:9999988
        # Last setTime: 273.000000000 flag:0  Last stepTime:105006084, Last adjustFreq:-19615
        # Last setTime: 0.000000000 flag:0  Last stepTime:0 Last adjustFreq:0
        p16 = re.compile(r'^Last\s+setTime:\s+(?P<last_set_time>[-\d.]+)\s+flag:(?P<flag>\d+)\s+Last\s+stepTime:(?P<last_step_time>[-\d]+)(?:(,))?\s+Last\s+adjustFreq:(?P<last_adjust_freq>[-\d]+)$')

        for line in output.splitlines():
            line = line.strip()

            # Servo status: Running
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ptp_dict = ret_dict.setdefault('platform_servo_stats',{})
                ptp_dict.update({'servo_status': group['servo_status']})
                continue

            # Servo stat_index: 2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                servo_stat_index = int(group['servo_stat_index'])
                ptp_dict.update({'servo_stat_index': servo_stat_index})
                continue

            # Device status: PHASE_LOCKED
            # Device status: FREQ_LOCKED
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ptp_dict.update({'device_status': group['device_status']})
                continue

            # Servo Mode: Hybrid
            # Servo Mode: Non Hybrid
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ptp_dict.update({'servo_mode': group['servo_mode']})
                continue

            # Servo log level: 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                servo_log_level = int(group['servo_log_level'])
                ptp_dict.update({'servo_log_level': servo_log_level})
                continue

            # Phase Alignment Accuracy: -8 ns
            # Phase Alignment Accuracy: -17034645174 ns
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ptp_dict.update({'phase_alignment_accuracy': group['phase_alignment_accuracy']})
                continue

            # Sync timestamp updated: 9848934
            m = p7.match(line)
            if m:
                group = m.groupdict()
                sync_timestamp_updated = int(group['sync_timestamp_updated'])
                ptp_dict.update({'sync_timestamp_updated': sync_timestamp_updated})
                continue

            # Sync timestamp discarded: 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                sync_timestamp_discarded = int(group['sync_timestamp_discarded'])
                ptp_dict.update({'sync_timestamp_discarded': sync_timestamp_discarded})
                continue

            # Delay timestamp updated: 9848973
            m = p9.match(line)
            if m:
                group = m.groupdict()
                delay_timestamp_updated = int(group['delay_timestamp_updated'])
                ptp_dict.update({'delay_timestamp_updated': delay_timestamp_updated})
                continue

            # Delay timestamp discarded: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                delay_timestamp_discarded = int(group['delay_timestamp_discarded'])
                ptp_dict.update({'delay_timestamp_discarded': delay_timestamp_discarded})
                continue

            # Previous Received Timestamp T1: 1674467002.900294787  T2: 1674467002.900304552  T3: 1674467002.905436033  T4: 1674467002.905445830
            m = p11.match(line)
            if m:
                group = m.groupdict()
                previous_received_timestamp_dict = ptp_dict.setdefault('previous_received_timestamp',{})
                t1 = float(group['t1'])
                previous_received_timestamp_dict.update({'t1': t1})
                t2 = float(group['t2'])
                previous_received_timestamp_dict.update({'t2': t2})
                t3 = float(group['t3'])
                previous_received_timestamp_dict.update({'t3': t3})
                t4 = float(group['t4'])
                previous_received_timestamp_dict.update({'t4': t4})
                continue

            # Last Received Timestamp T1: 1671703729.684676938 T2: 1671703746.719324326 T3: 1671703746.779917501 T4: 1671703729.745274543
            m = p12.match(line)
            if m:
                group = m.groupdict()
                last_received_timestamp_dict = ptp_dict.setdefault('last_received_timestamp',{})
                t1 = float(group['t1'])
                last_received_timestamp_dict.update({'t1': t1})
                t2 = float(group['t2'])
                last_received_timestamp_dict.update({'t2': t2})
                t3 = float(group['t3'])
                last_received_timestamp_dict.update({'t3': t3})
                t4 = float(group['t4'])
                last_received_timestamp_dict.update({'t4': t4})
                continue

            # Offset from master: 17 secs, 34645173 nsecs
            # Offset from master: -0 secs, 22 nsecs
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ptp_dict.update({'offset_from_master': group['offset_from_master']})
                continue

            # Mean path delay : 0 secs, 2215 nsecs
            # Mean path delay   :  0 secs, 9732 nsecs
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ptp_dict.update({'mean_path_delay': group['mean_path_delay']})
                continue

            # setTime():1854 stepTime():7989 adjustFreq():789 adjustFreqTime():437113
            # setTime():2  stepTime():1  adjustFreq():420942 adjustFreqTime():0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                set_time = int(group['set_time'])
                ptp_dict.update({'set_time': set_time})
                step_time = int(group['step_time'])
                ptp_dict.update({'step_time': step_time})
                adjust_freq = int(group['adjust_freq'])
                ptp_dict.update({'adjust_freq': adjust_freq})
                if group['adjust_freq_time']:
                    adjust_freq_time = int(group['adjust_freq_time'])
                    ptp_dict.update({'adjust_freq_time': adjust_freq_time})
                continue

            # Last setTime: 1.000000000 flag:0 Last stepTime:262310484, Last adjustFreq:9999988
            # Last setTime: 273.000000000 flag:0  Last stepTime:105006084, Last adjustFreq:-19615
            m = p16.match(line)
            if m:
                group = m.groupdict()
                last_set_time = float(group['last_set_time'])
                ptp_dict.update({'last_set_time': last_set_time})
                flag = int(group['flag'])
                ptp_dict.update({'flag': flag})
                last_step_time = int(group['last_step_time'])
                ptp_dict.update({'last_step_time': last_step_time})
                last_adjust_freq = int(group['last_adjust_freq'])
                ptp_dict.update({'last_adjust_freq': last_adjust_freq})
                continue

        return ret_dict

class ShowPtpForeignMastersBriefSchema(MetaParser):
    ''' Schema for:
            * 'show ptp foreign-masters brief'
    '''

    schema = {
        'interface_name': {
            Any(): {
                'transport': str,
                'address': str,
                'cfg_pri': str,
                'priority1': int,
                'state': list
            }
        }
    }


# ================================
# Parser for 'show ptp foreign-masters brief'
# ================================
class ShowPtpForeignMastersBrief(ShowPtpForeignMastersBriefSchema):

    cli_command = ['show ptp foreign-masters brief']

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}

        # Gi0/0/0/19 IPv4 192.168.254.1 None 128 Q,GM
        # Gi0/0/0/16        Ethernet  8478.ac6c.0aa2            None     128    M,Q
        # Te0/0/2/1         Ethernet  8478.ac6c.0a91            None     128    M,Q,GM
        p1 = re.compile(r'^(?P<interface_name>\S+)\s+(?P<transport>\w+)\s+(?P<address>\S+)\s+(?P<cfg_pri>[None]+)\s+(?P<priority1>\d+)\s+(?P<state>[A-Z,]+)$')

        for line in output.splitlines():
            line = line.strip()

            # Gi0/0/0/19 IPv4 192.168.254.1 None 128 Q,GM
            # Gi0/0/0/16        Ethernet  8478.ac6c.0aa2            None     128    M,Q
            # Te0/0/2/1         Ethernet  8478.ac6c.0a91            None     128    M,Q,GM
            m = p1.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict.setdefault('interface_name',{}).setdefault(group['interface_name'],{})
                int_dict.update({'transport': group['transport']})
                int_dict.update({'address': group['address']})
                int_dict.update({'cfg_pri': group['cfg_pri']})
                int_dict.update({'priority1': int(group['priority1'])})
                int_dict.update({'state': group['state'].split(',')})
                continue

        return ret_dict
