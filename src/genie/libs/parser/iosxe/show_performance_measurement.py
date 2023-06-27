
# Python
from contextlib import redirect_stderr
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

''' show_pm.py

IOSXE parsers for the following show commands:

    ----------------------------------------------------------------------------
    * 'show performance-measurement interfaces'
    * 'show performance-measurement interfaces detail'
    * 'show performance-measurement interfaces private'
    * 'show performance-measurement interfaces {multiple}'
    * 'show performance-measurement interfaces name <name>'
    * 'show performance-measurement interfaces name <name> {multiple}'
    ----------------------------------------------------------------------------
    * 'show performance-measurement responder counters interface'
    * 'show performance-measurement responder counters interface {name}'
    * 'show performance-measurement responder interfaces'
    * 'show performance-measurement responder interfaces name {name}'
    * 'show performance-measurement responder summary'
    ----------------------------------------------------------------------------
'''

# ====================
# Schema for:
#   * 'show performance-measurement interfaces'
#   * 'show performance-measurement interfaces detail'
#   * 'show performance-measurement interfaces private'
#   * 'show performance-measurement interfaces {multiple}'
#   * 'show performance-measurement interfaces name <name>'
#   * 'show performance-measurement interfaces name <name> {multiple}'
# ====================
class ShowPerformanceMeasurementInterfacesSchema(MetaParser):
    '''Schema for:
        * 'show performance-measurement interfaces'
        * 'show performance-measurement interfaces detail'
        * 'show performance-measurement interfaces private'
        * 'show performance-measurement interfaces {multiple}'
        * 'show performance-measurement interfaces name <name>'
        * 'show performance-measurement interfaces name <name> {multiple}'
    '''
    schema = {
        Any(): {
            'ifh': str,
            'delay_measurement_enabled': str,
            'loss_measurement_enabled': str,
            'local_ipv4_address': str,
            'local_ipv6_address': str,
            'state': str,
            Optional('mpls_caps'): str,
            Optional('delay_measurement'): {
                'session_id': int,
                'profile_name': str,
                Optional('last_advertisement'): {
                    Optional('advertised_at'): {
                        'hour': int,
                        'minute': int,
                        'second': int,
                        'day': int,
                        'month': int,
                        'year': int,
                        'seconds_ago': int
                    },
                    Optional('advertised_reason'): str,
                    Optional('advertised_anomaly'): str,
                    Optional('advertised_delays'): {
                        'average': int,
                        'minimum': int,
                        'maximum': int,
                        'variance': int
                    },
                    Optional('no_advertisements'): bool
                },
                Optional('next_advertisement'): {
                    Optional('check_scheduled'): Or(int, {'check_scheduled': int, 'in_n_more_probes': int}),
                    Optional('aggregated_delays'): {
                        'average': int,
                        'minimum': int,
                        'maximum': int,
                        'variance': int
                    },
                    Optional('rolling_average'): int,
                    Optional('no_probes'): bool
                },
                Optional('last_error'): {
                    'error': str,
                    'timestamp': {
                        'hour': int,
                        'minute': int,
                        'second': int,
                        'day': int,
                        'month': int,
                        'year': int
                    }
                },
                Optional('current_probe'): {
                    'started_at': {
                        'hour': int,
                        'minute': int,
                        'second': int,
                        'day': int,
                        'month': int,
                        'year': int,
                        'seconds_ago': int
                    },
                    'packets': {
                        'packets_sent': int,
                        'packets_received': int
                    },
                    'measured_delays': {
                        'average': int,
                        'minimum': int,
                        'maximum': int,
                        'variance': int
                    },

                    Optional('probe_samples'): {
                        Any(): {
                            'hour': int,
                            'minute': int,
                            'second': int,
                            'day': int,
                            'month': int,
                            'year': int,
                            'measured_delay': int
                        },
                        Optional('no_history'): bool
                    },
                    Optional('next_probe_scheduled'): {
                        'hour': int,
                        'minute': int,
                        'second': int,
                        'day': int,
                        'month': int,
                        'year': int,
                        'remaining_seconds': int
                    },
                    Optional('next_burst_packet'): int,
                    Optional('burst_completed'): bool
                },
                Optional('liveness_detection'): {
                    'session_creation_timestamp': {
                        'day': int,
                        'month': int,
                        'hour': int,
                        'minute': int,
                        'second': float
                    },
                    'session_state': str,
                    'last_state_change_timestamp': {
                        'day': int,
                        'month': int,
                        'hour': int,
                        'minute': int,
                        'second': float
                    },
                    'missed_count': int,
                    'received_count': int,
                    'backoff': int,
                    Optional('unique_path_name'): str,
                    'loss_in_last_interval': {
                        'percent': int,
                        'tx': int,
                        'rx': int
                    }
                }
            },
            Optional('loss_measurement'): {
                'session_id': int,
                'profile_name': str,
                Optional('last_advertisement'): {
                    Optional('advertised_at'): {
                        'hour': int,
                        'minute': int,
                        'second': int,
                        'day': int,
                        'month': int,
                        'year': int,
                        'seconds_ago': int
                    },
                    Optional('no_advertisements'): bool,
                    Optional('advertised_reason'): str,
                    Optional('advertised_anomaly'): str,
                    Optional('advertised_loss'): {
                        'capped': float,
                        'average': float,
                        'minimum': float,
                        'maximum': float,
                        'variance': float
                    }
                },
                Optional('next_advertisement'): {
                    Optional('check_scheduled'): Or(int, {'check_scheduled': int, 'in_n_more_probes': int}),
                    Optional('aggregated_loss'): {
                        'capped': float,
                        'average': float,
                        'minimum': float,
                        'maximum': float,
                        'variance': float
                    },
                    Optional('no_probes'): bool,
                    Optional('rolling_average'): float
                },
                Optional('last_error'): {
                    'error': str,
                    'timestamp': {
                        'hour': int,
                        'minute': int,
                        'second': int,
                        'day': int,
                        'month': int,
                        'year': int
                    }
                },
                Optional('current_probe'): {
                    Optional('started_at'): {
                        'hour': int,
                        'minute': int,
                        'second': int,
                        'day': int,
                        'month': int,
                        'year': int,
                        'seconds_ago': int
                    },
                    Optional('packets'): {
                        'packets_sent': int,
                        'packets_received': int
                    },
                    Optional('measured_loss'): {
                        'capped': float,
                        'average': float,
                        'minimum': float,
                        'maximum': float,
                        'variance': float
                    },

                    Optional('probe_samples'): {
                        Any(): {
                            'hour': int,
                            'minute': int,
                            'second': int,
                            'day': int,
                            'month': int,
                            'year': int,
                            'tx0': int,
                            'tx1': int,
                            'rx0': int,
                            'rx1': int,
                            Optional('co'): int,
                            'loss': float
                        },
                        Optional('no_history'): bool
                    },
                    Optional('next_probe_scheduled'): {
                        'hour': int,
                        'minute': int,
                        'second': int,
                        'day': int,
                        'month': int,
                        'year': int,
                        'remaining_seconds': int
                    },
                    Optional('next_burst_packet'): int,
                    Optional('burst_completed'): bool,
                    Optional('not_running_info'): str
                },
                Optional('liveness_detection'): {
                    'session_creation_timestamp': {
                        'day': int,
                        'month': int,
                        'hour': int,
                        'minute': int,
                        'second': float
                    },
                    'session_state': str,
                    'last_state_change_timestamp': {
                        'day': int,
                        'month': int,
                        'hour': int,
                        'minute': int,
                        'second': float
                    },
                    'missed_count': int,
                    'received_count': int,
                    'backoff': int,
                    Optional('unique_path_name'): str,
                    'loss_in_last_interval': {
                        'percent': int,
                        'tx': int,
                        'rx': int
                    }
                }
            }
        }
    }

# ====================
# Parser for:
#   * 'show performance-measurement interfaces'
#   * 'show performance-measurement interfaces detail'
#   * 'show performance-measurement interfaces private'
#   * 'show performance-measurement interfaces {multiple}'
#   * 'show performance-measurement interfaces name <name>'
#   * 'show performance-measurement interfaces name <name> {multiple}'
# ====================
class ShowPerformanceMeasurementInterfaces(ShowPerformanceMeasurementInterfacesSchema):
    '''Parser for:
        * 'show performance-measurement interfaces'
        * 'show performance-measurement interfaces detail'
        * 'show performance-measurement interfaces private'
        * 'show performance-measurement interfaces {multiple}'
        * 'show performance-measurement interfaces name <name>'
        * 'show performance-measurement interfaces name <name> {multiple}'
    '''
    cli_command = [
        'show performance-measurement interfaces',
        'show performance-measurement interfaces {option1}',
        'show performance-measurement interfaces {option1} {option2}',
        'show performance-measurement interfaces name {name}',
        'show performance-measurement interfaces name {name} {option1}',
        'show performance-measurement interfaces name {name} {option1} {option2}'
    ]

    def cli(self, name=None, option1=None, option2=None, output=None):
        if not output:
            cmd = ''
            if name:
                if option1:
                    if option2:
                        cmd = self.cli_command[5].format(name=name, option1=option1, option2=option2)
                    else:
                        cmd = self.cli_command[4].format(name=name, option1=option1)
                else:
                    cmd = self.cli_command[3].format(name=name)
            elif option1:
                if option2:
                    cmd = self.cli_command[2].format(option1=option1, option2=option2)
                else:
                    cmd = self.cli_command[1].format(option1=option1)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Interface Name: Ethernet0/0 (ifh: 0x2)
        p1 = re.compile(r'^Interface Name: (?P<interface_name>\S+) \(ifh: (?P<ifh>\S+)\)$')

        # Delay-Measurement           : Enabled
        p2 = re.compile(r'^Delay-Measurement\s+: (?P<delay_measurement_enabled>\S+)$')

        # Loss-Measurement            : Disabled
        p3 = re.compile(r'^Loss-Measurement\s+: (?P<loss_measurement_enabled>\S+)$')

        # Local IPV4 Address          : 19.1.1.3
        p4 = re.compile(r'^Local IPV4 Address\s+: (?P<local_ipv4_address>[\d\.]+)$')

        # Local IPV6 Address          : ::
        p5 = re.compile(r'^Local IPV6 Address\s+: (?P<local_ipv6_address>[\d:A-F]+)$')

        # State                       : Up
        p6 = re.compile(r'^State\s+: (?P<state>\S+)$')

        # MPLS Caps                   : Not created
        p7 = re.compile(r'^MPLS Caps\s+: (?P<mpls_caps>.+)$')

        # Delay Measurement session:
        p8 = re.compile(r'^Delay Measurement session:$')

        #     Session ID                : 1
        p9 = re.compile(r'^Session ID\s+: (?P<session_id>\d+)$')

        #     Profile name              : Not configured
        p10 = re.compile(r'^Profile name\s+: (?P<profile_name>.+)$')

        #     Last advertisement:
        p11 = re.compile(r'^Last advertisement:$')

        #     No advertisements have occured
        p12 = re.compile(r'^No advertisements have occured$')

        #     Next advertisement:
        p13 = re.compile(r'^Next advertisement:$')

        #     Check scheduled in 2 more probes (roughly every 120 seconds)
        p14 = re.compile(r'^Check scheduled in (?P<in_n_more_probes>\d+) more probes \(roughly every (?P<check_scheduled>\d+) seconds\)$')

        #     No probes completed
        p15 = re.compile(r'^No probes completed$')

        #     Last Error:
        p16 = re.compile(r'^Last Error:$')

        #     Timestamp: 13:11:32 10-18 2021
        p17 = re.compile(r'^Timestamp: (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<month>\d+)-(?P<day>\d+) (?P<year>\d+)$')

        #     0 0 packet sent error. INVALID_OUT_IF
        p18 = re.compile(r'^(?P<error>.+)$')

        #     Current Probe:
        p19 = re.compile(r'^Current Probe:$')

        #     Started at 13:11:17 10-18 2021 (16 seconds ago)
        p20 = re.compile(r'^Started at (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<month>\d+)-(?P<day>\d+) (?P<year>\d+) \((?P<seconds_ago>\d+) seconds ago\)$')

        #     Packets Sent: 6, received: 0
        p21 = re.compile(r'^Packets Sent: (?P<packets_sent>\d+), received: (?P<packets_received>\d+)$')

        #     Measured delays (uSec): avg: 0, min: 0, max: 0, variance: 0
        p22 = re.compile(r'^Measured delays \(uSec\): avg: (?P<average>\d+), min: (?P<minimum>\d+), max: (?P<maximum>\d+), variance: (?P<variance>\d+)$')

        #     Probe samples:
        p23 = re.compile(r'^Probe samples:$')

        #         No History
        p24 = re.compile(r'^No History$')

        #     Next probe scheduled at 13:11:47 10-18 2021 (in 14 seconds)
        p25 = re.compile(r'^Next probe scheduled at (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<month>\d+)-(?P<day>\d+) (?P<year>\d+) \(in (?P<remaining_seconds>\d+) seconds\)$')

        #     Next burst packet will be sent in 2 seconds
        p26 = re.compile(r'^Next burst packet will be sent in (?P<next_burst_packet>\d+) seconds$')

        #       Not running: Platform not supported
        p27 = re.compile(r'^Not running: (?P<not_running_info>.+)$')

        #     Liveness Detection:
        p28 = re.compile(r'^Liveness Detection:$')

        #     Session Creation Timestamp: 10-18 12:56:46.731
        p29 = re.compile(r'Session Creation Timestamp: (?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d*\.\d+)$')

        #     Session State: Down
        p30 = re.compile(r'^Session State: (?P<session_state>\S+)$')

        #     Last State Change Timestamp: 10-18 12:58:47.578
        p31 = re.compile(r'^Last State Change Timestamp: (?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d*\.\d+)$')

        #     Missed count   [consecutive]: 296
        p32 = re.compile(r'^Missed count\s+\[consecutive\]: (?P<missed_count>\d+)$')

        #     Received count [consecutive]: 0
        p33 = re.compile(r'^Received count\s+\[consecutive\]: (?P<received_count>\d+)$')

        #     Backoff                     : 1
        p34 = re.compile(r'^Backoff\s+: (?P<backoff>\d+)$')

        #     Unique Path Name            : Path-1
        p35 = re.compile(r'^Unique Path Name\s+: (?P<unique_path_name>.+)$')

        #     Loss in Last Interval       : 100 % [TX: 6 RX: 0]
        p36 = re.compile(r'^Loss in Last Interval\s+: (?P<percent>\d+) % \[TX: (?P<tx>\d+) RX: (?P<rx>\d+)\]$')

        #     Advertised at: 05:15:42 11-02 2021 (4901 seconds ago)
        p37 = re.compile(r'^Advertised at: (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<month>\d+)-(?P<day>\d+) (?P<year>\d+) \((?P<seconds_ago>\d+) seconds ago\)$')

        #     Advertised reason: First advertisement
        p38 = re.compile(r'^Advertised reason: (?P<advertised_reason>.+)$')

        #     Advertised anomaly: INACTIVE
        p39 = re.compile(r'^Advertised anomaly: (?P<advertised_anomaly>.+)$')

        #     Advertised delays (uSec): avg: 752, min: 575, max: 947, variance: 99
        p40 = re.compile(r'^Advertised delays \(uSec\): avg: (?P<average>\d+), min: (?P<minimum>\d+), max: (?P<maximum>\d+), variance: (?P<variance>\d+)$')

        #     Check scheduled at the end of the current probe (roughly every 120 seconds)
        p41 = re.compile(r'^Check scheduled at the end of the current probe \(roughly every (?P<check_scheduled>\d+) seconds\)$')

        #     Aggregated delays (uSec): avg: 383, min: 313, max: 499, variance: 51
        p42 = re.compile(r'^Aggregated delays \(uSec\): avg: (?P<average>\d+), min: (?P<minimum>\d+), max: (?P<maximum>\d+), variance: (?P<variance>\d+)$')

        #     Rolling average (uSec): 395
        p43 = re.compile(r'^Rolling average \(uSec\): (?P<rolling_average>\d+)$')

        #     Probe samples:
        p44 = re.compile(r'^Probe samples:$')

        #     Packet Rx Timestamp       Measured Delay (nsec)
        p45 = re.compile(r'^Packet Rx Timestamp\s+Measured Delay \(nsec\)$')

        #     06:37:21 11-02 2021       432500
        p46 = re.compile(r'^(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<month>\d+)-(?P<day>\d+) (?P<year>\d+)\s+(?P<measured_delay>\d+)$')

        #     Burst completed
        p47 = re.compile(r'^Burst completed$')

        # Loss Measurement session:
        p48 = re.compile(r'^Loss Measurement session:$')

        #     Advertised loss(%) [Capped @ 50.331642%]: avg: 0.000000, min: 0.000000, max: 0.000000, variance: 0.000000
        p49 = re.compile(r'^Advertised loss\(%\) \[Capped @ (?P<capped>\d*\.\d+)%\]: avg: (?P<average>\d*\.\d+), min: (?P<minimum>\d*\.\d+), max: (?P<maximum>\d*\.\d+), variance: (?P<variance>\d*\.\d+)$')

        #     Aggregated loss(%) [Capped @ 50.331642%]: avg: 0.000000, min: 0.000000, max: 0.000000, variance: 0.000000
        p50 = re.compile(r'^Aggregated loss\(%\) \[Capped @ (?P<capped>\d*\.\d+)%\]: avg: (?P<average>\d*\.\d+), min: (?P<minimum>\d*\.\d+), max: (?P<maximum>\d*\.\d+), variance: (?P<variance>\d*\.\d+)$')

        #     Rolling average (%): 0.000000
        p51 = re.compile(r'^Rolling average \(%\): (?P<rolling_average>\d*\.\d+)$')

        #     Measured loss(%) [Capped @ 50.331642%]: avg: 0.000000, min: 0.000000, max: 0.000000, variance: 0.000000
        p52 = re.compile(r'^Measured loss\(%\) \[Capped @ (?P<capped>\d*\.\d+)%\]: avg: (?P<average>\d*\.\d+), min: (?P<minimum>\d*\.\d+), max: (?P<maximum>\d*\.\d+), variance: (?P<variance>\d*\.\d+)$')

        #         Rx Timestamp              Last TX    TX         Last RX    RX         Loss(0-100%)
        #         Rx Timestamp              Last TX    TX         Last RX    RX         Col  Loss(0-100%)
        p53 = re.compile(r'^Rx Timestamp\s+Last TX\s+TX\s+Last RX\s+RX\s+(Col\s+)?Loss\(0-100%\)$')

        #         13:11:32 10-18 2021       56         57         57         58         0.000000
        #         13:11:32 10-18 2021       56         57         57         58         1 0.000000
        p54 = re.compile(r'^(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+) (?P<month>\d+)-(?P<day>\d+) (?P<year>\d+)\s+(?P<tx0>\d+)\s+(?P<tx1>\d+)\s+(?P<rx0>\d+)\s+(?P<rx1>\d+)\s+((?P<co>\d+)\s+)?(?P<loss>\d*\.\d+)$')

        ret_dict = {}
        intf_name = ''
        current_section = ''
        for line in output.splitlines():
            line = line.strip()

            # Interface Name: Ethernet0/0 (ifh: 0x2)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_name = group['interface_name']
                ret_dict.setdefault(intf_name, {'ifh': group['ifh']})
                continue

            # Delay-Measurement           : Enabled
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('delay_measurement_enabled', group['delay_measurement_enabled'])
                continue

            # Loss-Measurement            : Disabled
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('loss_measurement_enabled', group['loss_measurement_enabled'])
                continue

            # Local IPV4 Address          : 19.1.1.3
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('local_ipv4_address', group['local_ipv4_address'])
                continue

            # Local IPV6 Address          : ::
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('local_ipv6_address', group['local_ipv6_address'])
                continue

            # State                       : Up
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('state', group['state'])
                continue

            # MPLS Caps                   : Not created
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('mpls_caps', group['mpls_caps'])
                continue

            # Delay Measurement session:
            m = p8.match(line)
            if m:
                ret_dict[intf_name].setdefault('delay_measurement', {})
                index_dict = ret_dict[intf_name]['delay_measurement']
                continue

            #     Session ID                : 1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                index_dict.setdefault('session_id', int(group['session_id']))
                continue

            #     Profile name              : Not configured
            m = p10.match(line)
            if m:
                group = m.groupdict()
                index_dict.setdefault('profile_name', group['profile_name'])
                continue

            #     Last advertisement:
            m = p11.match(line)
            if m:
                index_dict.setdefault('last_advertisement', {})
                current_section = 'last_advertisement'
                section_dict = index_dict[current_section]
                continue

            #     No advertisements have occured
            m = p12.match(line)
            if m:
                section_dict.setdefault('no_advertisements', True)
                continue

            #     Next advertisement:
            m = p13.match(line)
            if m:
                index_dict.setdefault('next_advertisement', {})
                current_section = 'next_advertisement'
                section_dict = index_dict[current_section]
                continue

            #     Check scheduled in 2 more probes (roughly every 120 seconds)
            m = p14.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('check_scheduled', {
                    'in_n_more_probes': int(group['in_n_more_probes']),
                    'check_scheduled': int(group['check_scheduled'])
                })
                continue

            #     No probes completed
            m = p15.match(line)
            if m:
                section_dict.setdefault('no_probes', True)
                continue


            #     Last Error:
            m = p16.match(line)
            if m:
                index_dict.setdefault('last_error', {})
                current_section = 'last_error'
                section_dict = index_dict[current_section]
                continue

            #     Timestamp: 13:11:32 10-18 2021
            m = p17.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('timestamp', {
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': int(group['second']),
                    'day': int(group['day']),
                    'month': int(group['month']),
                    'year': int(group['year'])
                })
                continue
            #     0 0 packet sent error. INVALID_OUT_IF
            m = p18.match(line)
            if m:
                if current_section == 'last_error' and 'error' not in section_dict:
                    group = m.groupdict()
                    section_dict.setdefault('error', group['error'])
                    continue

            #     Current Probe:
            m = p19.match(line)
            if m:
                index_dict.setdefault('current_probe', {})
                current_section = 'current_probe'
                section_dict = index_dict[current_section]
                continue

            #     Started at 13:11:17 10-18 2021 (16 seconds ago)
            m = p20.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('started_at', {
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': int(group['second']),
                    'day': int(group['day']),
                    'month': int(group['month']),
                    'year': int(group['year']),
                    'seconds_ago': int(group['seconds_ago'])
                })
                continue

            #     Packets Sent: 6, received: 0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('packets', {
                    'packets_sent': int(group['packets_sent']),
                    'packets_received': int(group['packets_received'])
                })
                continue

            #     Measured delays (uSec): avg: 0, min: 0, max: 0, variance: 0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('measured_delays', {
                    'average': int(group['average']),
                    'minimum': int(group['minimum']),
                    'maximum': int(group['maximum']),
                    'variance': int(group['variance'])
                })
                continue

            #     Probe samples:
            m = p23.match(line)
            if m:
                section_dict.setdefault('probe_samples', {})
                continue

            #         No History
            m = p24.match(line)
            if m:
                section_dict['probe_samples'].setdefault('no_history', True)
                continue

            #     Next probe scheduled at 13:11:47 10-18 2021 (in 14 seconds)
            m = p25.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('next_probe_scheduled', {
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': int(group['second']),
                    'day': int(group['day']),
                    'month': int(group['month']),
                    'year': int(group['year']),
                    'remaining_seconds': int(group['remaining_seconds'])
                })
                continue

            #     Next burst packet will be sent in 2 seconds
            m = p26.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('next_burst_packet', int(group['next_burst_packet']))
                continue

            #       Not running: Platform not supported
            m = p27.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('not_running_info', group['not_running_info'])
                continue

            #     Liveness Detection:
            m = p28.match(line)
            if m:
                index_dict.setdefault('liveness_detection', {})
                current_section = 'liveness_detection'
                section_dict = index_dict[current_section]
                continue

            #     Session Creation Timestamp: 10-18 12:56:46.731
            m = p29.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('session_creation_timestamp', {
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': float(group['second']),
                    'day': int(group['day']),
                    'month': int(group['month']),
                })
                continue

            #     Session State: Down
            m = p30.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('session_state', group['session_state'])
                continue


            #     Last State Change Timestamp: 10-18 12:58:47.578
            m = p31.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('last_state_change_timestamp', {
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': float(group['second']),
                    'day': int(group['day']),
                    'month': int(group['month']),
                })
                continue


            #     Missed count   [consecutive]: 296
            m = p32.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('missed_count', int(group['missed_count']))
                continue

            #     Received count [consecutive]: 0
            m = p33.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('received_count', int(group['received_count']))
                continue

            #     Backoff                     : 1
            m = p34.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('backoff', int(group['backoff']))
                continue

            #     Unique Path Name            : Path-1
            m = p35.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('unique_path_name', group['unique_path_name'])
                continue

            #     Loss in Last Interval       : 100 % [TX: 6 RX: 0]
            m = p36.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('loss_in_last_interval', {
                    'percent': int(group['percent']),
                    'tx': int(group['tx']),
                    'rx': int(group['rx'])
                })
                continue

            #     Advertised at: 05:15:42 11-02 2021 (4901 seconds ago)
            m = p37.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('advertised_at', {
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': int(group['second']),
                    'day': int(group['day']),
                    'month': int(group['month']),
                    'year': int(group['year']),
                    'seconds_ago': int(group['seconds_ago'])
                })
                continue

            #     Advertised reason: First advertisement
            m = p38.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('advertised_reason', group['advertised_reason'])
                continue

            #     Advertised anomaly: INACTIVE
            m = p39.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('advertised_anomaly', group['advertised_anomaly'])
                continue

            #     Advertised delays (uSec): avg: 752, min: 575, max: 947, variance: 99
            m = p40.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('advertised_delays', {
                    'average': int(group['average']),
                    'minimum': int(group['minimum']),
                    'maximum': int(group['maximum']),
                    'variance': int(group['variance'])
                })
                continue

            #     Check scheduled at the end of the current probe (roughly every 120 seconds)
            m = p41.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('check_scheduled', int(group['check_scheduled']))
                continue

            #     Aggregated delays (uSec): avg: 383, min: 313, max: 499, variance: 51
            m = p42.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('aggregated_delays', {
                    'average': int(group['average']),
                    'minimum': int(group['minimum']),
                    'maximum': int(group['maximum']),
                    'variance': int(group['variance'])
                })
                continue

            #     Rolling average (uSec): 395
            m = p43.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('rolling_average', int(group['rolling_average']))
                continue

            #     Probe samples:
            m = p44.match(line)
            if m:
                section_dict.setdefault('probe_samples', {})
                continue


            #     Packet Rx Timestamp       Measured Delay (nsec)
            m = p45.match(line)
            if m:
                count_probes = -1
                continue

            #     06:37:21 11-02 2021       432500
            m = p46.match(line)
            if m:
                group = m.groupdict()
                count_probes += 1
                section_dict['probe_samples'].setdefault(count_probes, {
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': int(group['second']),
                    'day': int(group['day']),
                    'month': int(group['month']),
                    'year': int(group['year']),
                    'measured_delay': int(group['measured_delay'])
                })
                continue

            #     Burst completed
            m = p47.match(line)
            if m:
                section_dict.setdefault('burst_completed', True)
                continue


            # Loss Measurement session:
            m = p48.match(line)
            if m:
                ret_dict[intf_name].setdefault('loss_measurement', {})
                index_dict = ret_dict[intf_name]['loss_measurement']
                continue

            #     Advertised loss(%) [Capped @ 50.331642%]: avg: 0.000000, min: 0.000000, max: 0.000000, variance: 0.000000
            m = p49.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('advertised_loss', {
                    'capped': float(group['capped']),
                    'average': float(group['average']),
                    'minimum': float(group['minimum']),
                    'maximum': float(group['maximum']),
                    'variance': float(group['variance'])
                })
                continue

            #     Aggregated loss(%) [Capped @ 50.331642%]: avg: 0.000000, min: 0.000000, max: 0.000000, variance: 0.000000
            m = p50.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('aggregated_loss', {
                    'capped': float(group['capped']),
                    'average': float(group['average']),
                    'minimum': float(group['minimum']),
                    'maximum': float(group['maximum']),
                    'variance': float(group['variance'])
                })
                continue

            #     Rolling average (%): 0.000000
            m = p51.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('rolling_average', float(group['rolling_average']))
                continue

            #     Measured loss(%) [Capped @ 50.331642%]: avg: 0.000000, min: 0.000000, max: 0.000000, variance: 0.000000
            m = p52.match(line)
            if m:
                group = m.groupdict()
                section_dict.setdefault('measured_loss', {
                    'capped': float(group['capped']),
                    'average': float(group['average']),
                    'minimum': float(group['minimum']),
                    'maximum': float(group['maximum']),
                    'variance': float(group['variance'])
                })
                continue

            #         Rx Timestamp              Last TX    TX         Last RX    RX         Loss(0-100%)
            #         Rx Timestamp              Last TX    TX         Last RX    RX         Col  Loss(0-100%)
            m = p53.match(line)
            if m:
                count_probes = -1
                continue

            #         13:11:32 10-18 2021       56         57         57         58         0.000000
            #         13:11:32 10-18 2021       56         57         57         58         1 0.000000
            m = p54.match(line)
            if m:
                group = m.groupdict()
                count_probes += 1
                section_dict['probe_samples'].setdefault(count_probes, {
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': int(group['second']),
                    'day': int(group['day']),
                    'month': int(group['month']),
                    'year': int(group['year']),
                    'tx0': int(group['tx0']),
                    'tx1': int(group['tx1']),
                    'rx0': int(group['rx0']),
                    'rx1': int(group['rx1']),
                    'loss': float(group['loss']),
                    'co': int(group['co'])
                })
                continue

        return ret_dict

# ====================
# Schema for:
#   * 'show performance-measurement responder interfaces'
#   * 'show performance-measurement responder interfaces name {name}'
# ====================
class ShowPerformanceMeasurementResponderInterfacesSchema(MetaParser):
    '''Schema for:
        * 'show performance-measurement responder interfaces'
        * 'show performance-measurement responder interfaces name {name}'
    '''
    schema = {
        Any(): {  # Interface name
            'interface_handle': str,
            'local_ipv4_address': str,
            'local_ipv6_address': str,
            'current_rate': int,
            'rate_high_water_mark': int,
            'cleanup_time_remaining': int,
            Optional('loss_color_type'): str,
            Optional('loss_color_inact_remain'): int
        }
    }

# ====================
# Parser for:
#   * 'show performance-measurement responder interfaces'
#   * 'show performance-measurement responder interfaces name {name}'
# ====================
class ShowPerformanceMeasurementResponderInterfaces(ShowPerformanceMeasurementResponderInterfacesSchema):
    '''Parser for:
        * 'show performance-measurement responder interfaces',
        * 'show performance-measurement responder interfaces name {name}'

    '''
    cli_command = [
        'show performance-measurement responder interfaces',
        'show performance-measurement responder interfaces name {name}'
    ]

    def cli(self, name=None, output=None):

        if not output:
            if name:
                cmd = self.cli_command[1].format(name=name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Interface Name: Ethernet0/1
        p1 = re.compile(r'^Interface Name: (?P<interface_name>\S+)$')

        # Interface Handle        : 0x3
        p2 = re.compile(r'^Interface Handle\s+: (?P<interface_handle>\S+)$')

        # Local IPV4 Address      : 110.1.1.3
        p3 = re.compile(r'^Local IPV4 Address\s+: (?P<local_ipv4_address>[\d\.]+)$')

        # Local IPV6 Address      : ::
        p4 = re.compile(r'^Local IPV6 Address\s+: (?P<local_ipv6_address>[\d:A-F]+)$')

        # Current rate            : 0 pkts/sec
        p5 = re.compile(r'^Current rate\s+: (?P<current_rate>\d+) pkts/sec$')

        # Rate high water mark    : 0 pkts/sec
        p6 = re.compile(r'^Rate high water mark\s+: (?P<rate_high_watermark>\d+) pkts/sec$')

        # Cleanup time remaining  : 3599 sec
        p7 = re.compile(r'^Cleanup time remaining\s+: (?P<cleanup_time_remaining>\d+) sec$')

        # Loss color type         : dual-color gre
        p8 = re.compile(r'^Loss color type\s+: (?P<loss_color_type>.+)$')

        # Loss color inact remain : 1006 sec
        p9 = re.compile(r'^Loss color inact remain\s+: (?P<loss_color_inact_remain>\d+) sec$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Interface Name: Ethernet0/1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_name = group['interface_name']
                ret_dict.setdefault(intf_name, {})
                continue

            # Interface Handle        : 0x3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('interface_handle', group['interface_handle'])
                continue

            # Local IPV4 Address      : 110.1.1.3
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('local_ipv4_address', group['local_ipv4_address'])
                continue

            # Local IPV6 Address      : ::
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('local_ipv6_address', group['local_ipv6_address'])
                continue

            # Current rate            : 0 pkts/sec
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('current_rate', int(group['current_rate']))
                continue

            # Rate high water mark    : 0 pkts/sec
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('rate_high_water_mark', int(group['rate_high_watermark']))
                continue

            # Cleanup time remaining  : 3599 sec
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('cleanup_time_remaining', int(group['cleanup_time_remaining']))
                continue

            # Loss color type         : dual-color gre
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('loss_color_type', group['loss_color_type'])
                continue

            # Loss color inact remain : 1006 sec
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('loss_color_inact_remain', int(group['loss_color_inact_remain']))
                continue


        return ret_dict

# ====================
# Schema for:
#   * 'show performance-measurement responder counters interface'
#   * 'show performance-measurement responder counters interface {name}'
# ====================
class ShowPerformanceMeasurementResponderCountersSchema(MetaParser):
    '''Schema for:
        * 'show performance-measurement responder counters interface'
        * 'show performance-measurement responder counters interface {name}'
    '''
    schema = {
        Any(): {  # Interface name
            'total_query_packets_received': int,
            'total_reply_packets_sent': int,
            'total_reply_packets_sent_errors': int,
            'total_uro_tlv_not_present_errors': int,
            'total_invalid_port_number_errors': int,
            'total_no_source_address_errors': int,
            'total_no_return_path_errors': int,
            'total_unsupported_querier_control_code_errors': int,
            'total_unsupported_timestamp_format_errors': int,
            'total_timestamp_not_available_errors': int,
            'total_unsupported_mandatory_tlv_errors': int,
            'total_invalid_packet_errors': int,
            Optional('total_loss_probe_color_errors'): int
        }
    }

# ====================
# Parser for:
#   * 'show performance-measurement responder counters interface'
#   * 'show performance-measurement responder counters interface name {name}'
# ====================
class ShowPerformanceMeasurementResponderCounters(ShowPerformanceMeasurementResponderCountersSchema):
    '''Parser for:
        * 'show performance-measurement responder counters interface'
        * 'show performance-measurement responder counters interface name {name}'
    '''
    cli_command = [
        'show performance-measurement responder counters interface',
        'show performance-measurement responder counters interfaces name {name}'
    ]

    def cli(self, name=None, output=None):

        if not output:
            if name:
                cmd = self.cli_command[1].format(name=name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)


        # Interface Name: Ethernet0/1
        p1 = re.compile(r'^Interface Name: (?P<interface_name>\S+)$')
        
        #     Total query packets received                  : 23304
        p2 = re.compile(r'^Total query packets received\s+: (?P<total_query_packets_received>\d+)$')

        #     Total reply packets sent                      : 23302
        p3 = re.compile(r'^Total reply packets sent\s+: (?P<total_reply_packets_sent>\d+)$')

        #     Total reply packets sent errors               : 2
        p4 = re.compile(r'^Total reply packets sent errors\s+: (?P<total_reply_packets_sent_errors>\d+)$')

        #     Total URO TLV not present errors              : 0
        p5 = re.compile(r'^Total URO TLV not present errors\s+: (?P<total_uro_tlv_not_present_errors>\d+)$')

        #     Total invalid port number errors              : 0
        p6 = re.compile(r'^Total invalid port number errors\s+: (?P<total_invalid_port_number_errors>\d+)$')

        #     Total no source address errors                : 0
        p7 = re.compile(r'^Total no source address errors\s+: (?P<total_no_source_address_errors>\d+)$')

        #     Total no return path errors                   : 0
        p8 = re.compile(r'^Total no return path errors\s+: (?P<total_no_return_path_errors>\d+)$')

        #     Total unsupported querier control code errors : 0
        p9 = re.compile(r'^Total unsupported querier control code errors\s+: (?P<total_unsupported_querier_control_code_errors>\d+)$')

        #     Total unsupported timestamp format errors     : 0
        p10 = re.compile(r'^Total unsupported timestamp format errors\s+: (?P<total_unsupported_timestamp_format_errors>\d+)$')

        #     Total timestamp not available errors          : 0
        p11 = re.compile(r'^Total timestamp not available errors\s+: (?P<total_timestamp_not_available_errors>\d+)$')

        #     Total unsupported mandatory TLV errors        : 0
        p12 = re.compile(r'^Total unsupported mandatory TLV errors\s+: (?P<total_unsupported_mandatory_tlv_errors>\d+)$')

        #     Total invalid packet errors                   : 0
        p13 = re.compile(r'^Total invalid packet errors\s+: (?P<total_invalid_packet_errors>\d+)$')

        #     Total loss probe color errors                 : 2
        p14 = re.compile(r'^Total loss probe color errors\s+: (?P<total_loss_probe_color_errors>\d+)$')


        intf_name = ''
        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Interface Name: Ethernet0/1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_name = group['interface_name']
                ret_dict.setdefault(intf_name, {})
                continue

            #     Total query packets received                  : 23304
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_query_packets_received', int(group['total_query_packets_received']))
                continue

            #     Total reply packets sent                      : 23302
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_reply_packets_sent', int(group['total_reply_packets_sent']))
                continue

            #     Total reply packets sent errors               : 2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_reply_packets_sent_errors', int(group['total_reply_packets_sent_errors']))
                continue

            #     Total URO TLV not present errors              : 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_uro_tlv_not_present_errors', int(group['total_uro_tlv_not_present_errors']))
                continue

            #     Total invalid port number errors              : 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_invalid_port_number_errors', int(group['total_invalid_port_number_errors']))
                continue

            #     Total no source address errors                : 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_no_source_address_errors', int(group['total_no_source_address_errors']))
                continue

            #     Total no return path errors                   : 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_no_return_path_errors', int(group['total_no_return_path_errors']))
                continue

            #     Total unsupported querier control code errors : 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_unsupported_querier_control_code_errors', int(group['total_unsupported_querier_control_code_errors']))
                continue

            #     Total unsupported timestamp format errors     : 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_unsupported_timestamp_format_errors', int(group['total_unsupported_timestamp_format_errors']))
                continue

            #     Total timestamp not available errors          : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_timestamp_not_available_errors', int(group['total_timestamp_not_available_errors']))
                continue

            #     Total unsupported mandatory TLV errors        : 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_unsupported_mandatory_tlv_errors', int(group['total_unsupported_mandatory_tlv_errors']))
                continue

            #     Total invalid packet errors                   : 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_invalid_packet_errors', int(group['total_invalid_packet_errors']))
                continue

            #     Total loss probe color errors                 : 2
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict[intf_name].setdefault('total_loss_probe_color_errors', int(group['total_loss_probe_color_errors']))
                continue

        return ret_dict

# ====================
# Schema for:
#   * 'show performance-measurement responder summary'
# ====================
class ShowPerformanceMeasurementResponderSummarySchema(MetaParser):
    '''Schema for:
        * 'show performance-measurement responder summary'
    '''
    schema = {
            'total_interfaces': int,
            'total_query_packets_received': int,
            'total_reply_packets_sent': int,
            'total_reply_packets_sent_errors': int,
            'total_uro_tlv_not_present_errors': int,
            'total_invalid_port_number_errors': int,
            'total_no_source_address_errors': int,
            'total_no_return_path_errors': int,
            'total_unsupported_querier_control_code_errors': int,
            'total_unsupported_timestamp_format_errors': int,
            'total_timestamp_not_available_errors': int,
            'total_unsupported_mandatory_tlv_errors': int,
            'total_invalid_packet_errors': int,
            Optional('total_loss_probe_color_errors'): int,
            'current_rate': int,
            'rate_high_water_mark': int
    }

# ====================
# Parser for:
#   * 'show performance-measurement responder summary'
# ====================
class ShowPerformanceMeasurementResponderSummary(ShowPerformanceMeasurementResponderSummarySchema):
    '''Parser for:
        * 'show performance-measurement responder summary'

    '''
    cli_command = [
        'show performance-measurement responder summary'
    ]
    def cli(self, output=None):
        
        if not output:
            cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Total interfaces                              : 2
        p1 = re.compile(r'^Total interfaces\s+: (?P<total_interfaces>\d+)$')

        # Total query packets received                  : 45501
        p2 = re.compile(r'^Total query packets received\s+: (?P<total_query_packets_received>\d+)$')

        # Total reply packets sent                      : 45499
        p3 = re.compile(r'^Total reply packets sent\s+: (?P<total_reply_packets_sent>\d+)$')

        # Total reply packets sent errors               : 2
        p4 = re.compile(r'^Total reply packets sent errors\s+: (?P<total_reply_packets_sent_errors>\d+)$')

        # Total URO TLV not present errors              : 0
        p5 = re.compile(r'^Total URO TLV not present errors\s+: (?P<total_uro_tlv_not_present_errors>\d+)$')

        # Total invalid port number errors              : 0
        p6 = re.compile(r'^Total invalid port number errors\s+: (?P<total_invalid_port_number_errors>\d+)$')

        # Total no source address errors                : 0
        p7 = re.compile(r'^Total no source address errors\s+: (?P<total_no_source_address_errors>\d+)$')

        # Total no return path errors                   : 0
        p8 = re.compile(r'^Total no return path errors\s+: (?P<total_no_return_path_errors>\d+)$')

        # Total unsupported querier control code errors : 0
        p9 = re.compile(r'^Total unsupported querier control code errors\s+: (?P<total_unsupported_querier>\d+)$')

        # Total unsupported timestamp format errors     : 0
        p10 = re.compile(r'^Total unsupported timestamp format errors\s+: (?P<total_unsupported_timestamp_format_errors>\d+)$')

        # Total timestamp not available errors          : 0
        p11 = re.compile(r'^Total timestamp not available errors\s+: (?P<total_timestamp_not_available_errors>\d+)$')

        # Total unsupported mandatory TLV errors        : 0
        p12 = re.compile(r'^Total unsupported mandatory TLV errors\s+: (?P<total_unsupported_mandatory_tlv_errors>\d+)$')

        # Total invalid packet errors                   : 0
        p13 = re.compile(r'^Total invalid packet errors\s+: (?P<total_invalid_packet_errors>\d+)$')

        #     Total loss probe color errors                 : 2
        p14 = re.compile(r'^Total loss probe color errors\s+: (?P<total_loss_probe_color_errors>\d+)$')

        # Current rate                                  : 0 pkts/sec
        p15 = re.compile(r'^Current rate\s+: (?P<current_rate>\d+) pkts/sec$')

        # Rate high water mark                          : 0 pkts/sec
        p16 = re.compile(r'^Rate high water mark\s+: (?P<rate_high_water_mark>\d+) pkts/sec$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Total interfaces                              : 2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_interfaces', int(group['total_interfaces']))
                continue

            # Total query packets received                  : 45501
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_query_packets_received', int(group['total_query_packets_received']))
                continue

            # Total reply packets sent                      : 45499
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_reply_packets_sent', int(group['total_reply_packets_sent']))
                continue

            # Total reply packets sent errors               : 2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_reply_packets_sent_errors', int(group['total_reply_packets_sent_errors']))
                continue

            # Total URO TLV not present errors              : 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_uro_tlv_not_present_errors', int(group['total_uro_tlv_not_present_errors']))
                continue

            # Total invalid port number errors              : 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_invalid_port_number_errors', int(group['total_invalid_port_number_errors']))
                continue

            # Total no source address errors                : 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_no_source_address_errors', int(group['total_no_source_address_errors']))
                continue

            # Total no return path errors                   : 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_no_return_path_errors', int(group['total_no_return_path_errors']))
                continue

            # Total unsupported querier control code errors : 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_unsupported_querier_control_code_errors', int(group['total_unsupported_querier']))
                continue

            # Total unsupported timestamp format errors     : 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_unsupported_timestamp_format_errors', int(group['total_unsupported_timestamp_format_errors']))
                continue

            # Total timestamp not available errors          : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_timestamp_not_available_errors', int(group['total_timestamp_not_available_errors']))
                continue

            # Total unsupported mandatory TLV errors        : 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_unsupported_mandatory_tlv_errors', int(group['total_unsupported_mandatory_tlv_errors']))
                continue

            # Total invalid packet errors                   : 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_invalid_packet_errors', int(group['total_invalid_packet_errors']))
                continue

            #     Total loss probe color errors                 : 2
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_loss_probe_color_errors', int(group['total_loss_probe_color_errors']))
                continue

            # Current rate                                  : 0 pkts/sec
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('current_rate', int(group['current_rate']))
                continue

            # Rate high water mark                          : 0 pkts/sec
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('rate_high_water_mark', int(group['rate_high_water_mark']))
                continue

        return ret_dict
