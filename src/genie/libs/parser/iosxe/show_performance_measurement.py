
# Python
from contextlib import redirect_stderr
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

''' show_pm.py

IOSXE parsers for the following show commands:

    ----------------------------------------------------------------------------
    * 'show performance-measurement summary'
    * 'show performance-measurement summary detail'
    * 'show performance-measurement summary private'
    * 'show performance-measurement summary detail private'
    ----------------------------------------------------------------------------
    * 'show performance-measurement paths'
    ----------------------------------------------------------------------------
    * 'show performance-measurement sr-policy'
    * 'show performance-measurement sr-policy detail'
    * 'show performance-measurement sr-policy private'
    * 'show performance-measurement sr-policy verbose'
    * 'show performance-measurement sr-policy detail verbose'
    * 'show performance-measurement sr-policy detail private'
    * 'show performance-measurement sr-policy private verbose'
    * 'show performance-measurement sr-policy detail private verbose'
    * 'show performance-measurement sr-policy name {name}'
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
    * 'show performance-measurement sr-policy'
    * 'show performance-measurement sr-policy detail'
    * 'show performance-measurement sr-policy private'
    * 'show performance-measurement sr-policy verbose'
    * 'show performance-measurement sr-policy detail verbose'
    * 'show performance-measurement sr-policy detail private'
    * 'show performance-measurement sr-policy private verbose'
    * 'show performance-measurement sr-policy detail private verbose'
    * 'show performance-measurement sr-policy name {name}'
    ----------------------------------------------------------------------------
'''

class ShowPerformanceMeasurementSrPolicySchema(MetaParser):
    '''Schema for:
        * 'show performance-measurement sr-policy'
        * 'show performance-measurement sr-policy detail'
        * 'show performance-measurement sr-policy private'
        * 'show performance-measurement sr-policy verbose'
        * 'show performance-measurement sr-policy detail verbose'
        * 'show performance-measurement sr-policy detail private'
        * 'show performance-measurement sr-policy private verbose'
        * 'show performance-measurement sr-policy detail private verbose'
        * 'show performance-measurement sr-policy name {name}'
    '''
    schema = {
        Any(): {

            'color': int,
            'endpoint': str,
            'source': str,
            'profile_name': str,
            'policy_update_timestamp': {
                'month': int,
                'day': int,
                'hour': int,
                'minute': int,
                'second': float
            },
            'number_of_candidate_paths': int,

            'candidate_paths': {

                Any(): {
                    'preference': int,
                    'protocol_origin': str,
                    Optional('discriminator'): int,
                    Optional('active'): str,
                    'number_of_segment_lists': int,
                    'number_of_atomic_paths': int,
                    'number_of_live_up_atomic_paths': int,
                    'number_of_live_unknown_atomic': int,
                    'max_packets_per_burst': int,
                    'max_packets_per_probe': int,
                    'ap_min_run_per_probe': int,
                    'round_robin_bursts': int,
                    'round_robin_probes': int,
                    'last_advertisement': {
                        Optional('advertised_at'): {
                            'hour': int,
                            'minute': int,
                            'second': int,
                            'day': int,
                            'year': int,
                            'seconds_ago': int
                        },
                        Optional('advertised_delays'): {
                            'average': int,
                            'minimum': int,
                            'maximum': int,
                            'variance': int
                        },
                        Optional('advertised_reason'): str,
                    },
                    'next_advertisement': {
                        Optional('check_schedule'): {
                            'probes': int,
                            'seconds': int
                        },
                        Optional('aggregate_delays'): {
                            'average': int,
                            'minimum': int,
                            'maximum': int,
                            'variance': int
                        },
                    },
                    'last_probe': {
                        Optional('packets'): {
                            'packets_sent': int,
                            'packets_received': int
                        },
                        Optional('measured_delays'): {
                            'average': int,
                            'minimum': int,
                            'maximum': int,
                            'variance': int
                        }
                    },
                    'current_probe': {
                        Optional('packets'): {
                            'packets_sent': int,
                            'packets_received': int
                        },
                        Optional('measured_delays'): {
                            'average': int,
                            'minimum': int,
                            'maximum': int,
                            'variance': int
                        }
                    },
                    Optional('segment_list'): {
                        'name': str,
                        'number_of_atomic_paths': int,
                        'last_advertisement': {
                            Optional('advertised_at'): {
                                'day': int,
                                'hour': int,
                                'minute': int,
                                'second': int,
                                'seconds_ago': int,
                                'year': int
                            },
                            Optional('advertised_delays'): {
                                'average': int,
                                'minimum': int,
                                'maximum': int,
                                'variance': int
                            },
                            Optional('advertised_reason'): str,
                        },
                        Optional('next_advertisement'): {
                            Optional('check_schedule'): {
                                'probes': int,
                                'seconds': int
                            },
                            Optional('aggregate_delays'): {
                                'average': int,
                                'minimum': int,
                                'maximum': int,
                                'variance': int
                            },
                        },
                        Optional('last_probe'): {
                            Optional('packets'): {
                                'packets_sent': int,
                                'packets_received': int
                            },
                            Optional('measured_delays'): {
                                'average': int,
                                'minimum': int,
                                'maximum': int,
                                'variance': int
                            }
                        },
                        Optional('current_probe'): {
                            Optional('packets'): {
                                'packets_sent': int,
                                'packets_received': int
                            },
                            Optional('measured_delays'): {
                                'average': int,
                                'minimum': int,
                                'maximum': int,
                                'variance': int
                            }
                        },
                        Optional('atomic_paths'): {
                            Any(): {
                                'hops': {
                                    Any(): str
                                },
                                'labels': {
                                    Any(): Or(str, int)
                                },
                                'outgoing_interface': str,
                                'max_ip_mtu': int,
                                'next_hop': str,
                                'destination': str,
                                'session_id': int,
                                'last_advertisement': {
                                    Optional('advertised_reason'): str,
                                    Optional('advertised_at'): {
                                        'day': int,
                                        'hour': int,
                                        'minute': int,
                                        'second': int,
                                        'seconds_ago': int,
                                        'year': int
                                    },
                                    Optional('advertised_delays'): {
                                        'average': int,
                                        'minimum': int,
                                        'maximum': int,
                                        'variance': int
                                    },
                                },
                                'next_advertisement': {
                                    Optional('aggregate_delays'): {
                                        'average': int,
                                        'minimum': int,
                                        'maximum': int,
                                        'variance': int
                                    },
                                    Optional('rolling_average'): int
                                },
                                'last_probe': {
                                    Optional('packets'): {
                                        'packets_sent': int,
                                        'packets_received': int
                                    },
                                    Optional('measured_delays'): {
                                        'average': int,
                                        'minimum': int,
                                        'maximum': int,
                                        'variance': int
                                    }
                                },
                                'current_probe': {
                                    Optional('packets'): {
                                        'packets_sent': int,
                                        'packets_received': int
                                    },
                                    Optional('measured_delays'): {
                                        'average': int,
                                        'minimum': int,
                                        'maximum': int,
                                        'variance': int
                                    }
                                },
                                'probe_samples': {
                                    'samples': {
                                        Any(): {
                                            'hour': int,
                                            'minute': int,
                                            'second': int,
                                            'day': int,
                                            'year': int,
                                            'delay': int
                                        }
                                    }
                                },
                                'liveness_detection': {
                                    'session_creation_timestamp': {
                                        'month': int,
                                        'day': int,
                                        'hour': int,
                                        'minute': int,
                                        'second': float
                                    },
                                    'session_state': str,
                                    'last_state_change_timestamp': {
                                        'month': int,
                                        'day': int,
                                        'hour': int,
                                        'minute': int,
                                        'second': float
                                    },
                                    'missed_count': int,
                                    'received_count': int,
                                    'backoff': int,
                                    'unique_path_name': str,
                                    'loss_in_last_interval': {
                                        'percent': int,
                                        'tx': int,
                                        'rx': int
                                    }
                                }

                            }
                        }
                    }
                }

            }
        }
    }

# ====================
# Parser for:
#   * 'show performance-measurement sr-policy'
#   * 'show performance-measurement sr-policy detail'
#   * 'show performance-measurement sr-policy private'
#   * 'show performance-measurement sr-policy verbose'
#   * 'show performance-measurement sr-policy detail verbose'
#   * 'show performance-measurement sr-policy detail private'
#   * 'show performance-measurement sr-policy private verbose'
#   * 'show performance-measurement sr-policy detail private verbose'
#   * 'show performance-measurement sr-policy name {name}'
class ShowPerformanceMeasurementSrPolicy(ShowPerformanceMeasurementSrPolicySchema):
    '''Parser for:
        * 'show performance-measurement sr-policy'
        * 'show performance-measurement sr-policy detail'
        * 'show performance-measurement sr-policy private'
        * 'show performance-measurement sr-policy verbose'
        * 'show performance-measurement sr-policy detail verbose'
        * 'show performance-measurement sr-policy detail private'
        * 'show performance-measurement sr-policy private verbose'
        * 'show performance-measurement sr-policy detail private verbose'
        * 'show performance-measurement sr-policy name {name}'
    '''

    cli_command = [
        'show performance-measurement sr-policy',
        'show performance-measurement sr-policy {detail}',
        'show performance-measurement sr-policy {detail} {private}',
        'show performance-measurement sr-policy {detail} {private} {verbose}',
        'show performance-measurement sr-policy name {name}',
        'show performance-measurement sr-policy name {name} {detail}',
        'show performance-measurement sr-policy name {name} {detail} {private}',
        'show performance-measurement sr-policy name {name} {detail} {private} {verbose}'
    ]

    def cli(self, name=None, detail=None, private=None, verbose=None, output=None):
        if not output:
            cmd = ''
            if name:
                if detail:
                    if private:
                        if verbose:
                            cmd = self.cli_command[7].format(name=name, detail=detail, private=private, verbose=verbose)
                        else:
                            cmd = self.cli_command[6].format(name=name, detail=detail, private=private)
                    else:
                        cmd = self.cli_command[5].format(name=name, detail=detail)
                else:
                    cmd = self.cli_command[4].format(name=name)
            else:
                if detail:
                    if private:
                        if verbose:
                            cmd = self.cli_command[3].format(detail=detail, private=private, verbose=verbose)
                        else:
                            cmd = self.cli_command[2].format(detail=detail, private=private)
                    else:
                        cmd = self.cli_command[1].format(detail=detail)
                else:
                    cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # SR Policy name: Ethernet0/0
        p1 = re.compile(r'^SR Policy name: (?P<sr_policy_name>\S+)$')

        # Color                           : 1235
        p2 = re.compile(r'^Color\s+: (?P<color>\d+)$')

        # Endpoint                        : 1.1.1.7
        p3 = re.compile(r'^Endpoint\s+: (?P<endpoint>[\d\.:A-F]+)$')

        # Source                          : 1.1.1.3
        p4 = re.compile(r'^Source\s+: (?P<source>[\d\.:A-F]+)$')

        # Profile name                    : Not configured
        p5 = re.compile(r'^Profile name\s+: (?P<profile_name>.+)$')

        # Policy Update Timestamp         : 05-20 06:46:52.222
        p6 = re.compile(r'^Policy Update Timestamp\s+: (?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d*\.\d+)$')

        # Number of candidate-paths       : 1
        p7 = re.compile(r'^Number of candidate-paths\s+: (?P<number_of_candidate_paths>\d+)$')

        # Candidate-Path:
        p8 = re.compile(r'^Candidate-Path:$')

        # Preference                    : 100
        p9 = re.compile(r'^Preference\s+: (?P<preference>\d+)$')

        # Protocol-origin               : CLI
        p10 = re.compile(r'^Protocol-origin\s+: (?P<protocol_origin>.+)$')

        # Discriminator                 : 0
        p11 = re.compile(r'^Discriminator\s+: (?P<discriminator>\d+)$')

        # Active:                       : No
        p12 = re.compile(r'^Active:\s+: (?P<active>\S+)$')

        # Number of segment-lists       : 1
        p13 = re.compile(r'^Number of segment-lists\s+: (?P<number_of_segment_lists>\d+)$')

        # Number of atomic paths        : 1
        p14 = re.compile(r'^Number of atomic paths\s+: (?P<number_of_atomic_paths>\d+)$')

        # Number of live UP atomic paths: 1
        p15 = re.compile(r'^Number of live UP atomic paths:\s+(?P<number_of_live_up_atomic_paths>\d+)$')

        # Number of live Unknown atomic : 1
        p16 = re.compile(r'^Number of live Unknown atomic\s+: (?P<number_of_live_unknown_atomic>\d+)$')

        # Max Pkts per Burst            : 500
        p17 = re.compile(r'^Max Pkts per Burst\s+: (?P<max_packets_per_burst>\d+)$')

        # Max Pkts per Probe            : 15000
        p18 = re.compile(r'^Max Pkts per Probe\s+: (?P<max_packets_per_probe>\d+)$')

        # AP Min Run per Probe          : 3
        p19 = re.compile(r'^AP Min Run per Probe\s+: (?P<ap_min_run_per_probe>\d+)$')

        # Round-robin bursts            : 1
        p20 = re.compile(r'^Round-robin bursts\s+: (?P<round_robin_bursts>\d+)$')

        # Round-robin probes            : 1
        p21 = re.compile(r'^Round-robin probes\s+: (?P<round_robin_probes>\d+)$')

        # Last advertisement:
        p22 = re.compile(r'^Last advertisement:$')

        # Advertised at: 09:06:42  20 2021 (92796 seconds ago)
        p23 = re.compile(r'^Advertised at: (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)\s+(?P<day>\d+)\s+(?P<year>\d+)\s+\((?P<seconds_ago>\d+) seconds ago\)$')

        # Advertised delays (uSec): avg: 465, min: 1, max: 999, variance: 464
        p24 = re.compile(r'^Advertised delays\s+\(uSec\): avg: (?P<average>\d+), min: (?P<minimum>\d+), max: (?P<maximum>\d+), variance: (?P<variance>\d+)$')

        # Next advertisement:
        p25 = re.compile(r'^Next advertisement:$')

        # Check scheduled in 2 more probes (roughly every 120 seconds)
        p26 = re.compile(r'^Check scheduled in (?P<probes>\d+) more probe\S* \(roughly every (?P<second>\d+) seconds\)$')

        # Aggregated delays (uSec): avg: 233, min: 1, max: 499, variance: 232
        p27 = re.compile(r'^Aggregated delays \(uSec\): avg: (?P<average>\d+), min: (?P<minimum>\d+), max: (?P<maximum>\d+), variance: (?P<variance>\d+)$')

        # Last probe:
        p28 = re.compile(r'^Last probe:$')

        # Packets Sent: 30, received: 30
        p29 = re.compile(r'^Packets Sent: (?P<sent>\d+), received: (?P<received>\d+)$')

        # Measured delays (uSec): avg: 233, min: 1, max: 499, variance: 232
        p30 = re.compile(r'^Measured delays \(uSec\): avg: (?P<average>\d+), min: (?P<minimum>\d+), max: (?P<maximum>\d+), variance: (?P<variance>\d+)$')

        # Current probe:
        p31 = re.compile(r'^Current probe:$')

        # Segment-List:
        p32 = re.compile(r'^Segment-List:$')

        # Name                        : SL7
        p33 = re.compile(r'^Name\s+: (?P<name>\S+)$')

        # Number of atomic paths      : 1
        p34 = re.compile(r'^Number of atomic paths\s+: (?P<number_of_atomic_paths>\d+)$')

        # Atomic path:
        p35 = re.compile(r'^Atomic path:$')

        # Hops                      : 1.1.1.7
        p36 = re.compile(r'^Hops\s+: (?P<hops>.+)$')

        # Labels                    : 16230
        # Labels                    : FCCC:CCC1:AA22:AA33:AA11:E003::
        p37 = re.compile(r'^Labels\s+: (?P<labels>[\d:A-F,\s]+)$')

        # Outgoing Interface        : Ethernet0/1
        p38 = re.compile(r'^Outgoing Interface\s+: (?P<outgoing_interface>\S+)$')

        # Max IP MTU                : 1500
        p39 = re.compile(r'^Max IP MTU\s+: (?P<max_ip_mtu>\d+)$')

        # Next Hop                  : 110.1.1.4
        p40 = re.compile(r'^Next Hop\s+: (?P<next_hop>[\d\.:A-F]+)$')

        # Destination               : 1.1.1.7
        p41 = re.compile(r'^Destination\s+: (?P<destination>[\d\.:A-F]+)$')

        # Session ID                : 10
        p42 = re.compile(r'^Session ID\s+: (?P<session_id>\d+)$')

        # Advertised reason: Periodic timer, avg delay threshold crossed
        p43 = re.compile(r'^Advertised reason: (?P<advertised_reason>.+)$')

        # Rolling average (uSec): 287
        p44 = re.compile(r'^Rolling average \(uSec\): (?P<rolling_average>\d+)$')

        # Probe samples:
        p45 = re.compile(r'^Probe samples:$')

        # Packet Rx Timestamp Measured Delay
        p46 = re.compile(r'^Packet Rx Timestamp Measured Delay$')

        # 10:53:18  21 2021 0
        p47 = re.compile(r'^(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)\s+(?P<day>\d+)\s+(?P<year>\d+)\s+(?P<delay>\d+)$')

        # Liveness Detection:
        p48 = re.compile(r'^Liveness Detection:$')

        # Session Creation Timestamp: 05-20 06:46:52.222
        p49 = re.compile(r'^Session Creation Timestamp: (?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d*\.\d+)$')

        # Session State: Up
        p50 = re.compile(r'^Session State: (?P<session_state>\S+)$')

        # Last State Change Timestamp: 05-20 06:46:52.414
        p51 = re.compile(r'^Last State Change Timestamp: (?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d*\.\d+)$')

        # Missed count   [consecutive]: 0
        p52 = re.compile(r'^Missed count\s+\[consecutive\]: (?P<missed_count>\d+)$')

        # Received count [consecutive]: 101186
        p53 = re.compile(r'^Received count \[consecutive\]: (?P<received_count>\d+)$')

        # Backoff                     : 0
        p54 = re.compile(r'^Backoff\s+: (?P<backoff>\d+)$')

        # Unique Path Name            : Path-10
        p55 = re.compile(r'^Unique Path Name\s+: (?P<unique_path_name>\S+)$')

        # Loss in Last Interval       : 0 % [TX: 6 RX: 6]
        p56 = re.compile(r'^Loss in Last Interval\s+: (?P<percent>\d+) % \[TX: (?P<tx>\d+) RX: (?P<rx>\d+)\]$')

        ret_dict = {}
        sr_pol = ''
        cur_cand_path = -1
        cur_atom_path = -1
        for line in output.splitlines():
            line = line.strip()

            # SR Policy name: Ethernet0/0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sr_pol = group['sr_policy_name']
                ret_dict.setdefault(sr_pol, {})
                cur_cand_path = -1
                continue

            # Color                           : 1235
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[sr_pol].setdefault('color', int(group['color']))
                continue

            # Endpoint                        : 1.1.1.7
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict[sr_pol].setdefault('endpoint', group['endpoint'])
                continue

            # Source                          : 1.1.1.3
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict[sr_pol].setdefault('source', group['source'])
                continue

            # Profile name                    : Not configured
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict[sr_pol].setdefault('profile_name', group['profile_name'])
                continue

            # Policy Update Timestamp         : 05-20 06:46:52.222
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict[sr_pol].setdefault('policy_update_timestamp', {
                    'month': int(group['month']),
                    'day': int(group['day']),
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': float(group['second'])
                })
                continue

            # Number of candidate-paths       : 1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict[sr_pol].setdefault('number_of_candidate_paths', int(group['number_of_candidate_paths']))
                continue

            # Candidate-Path:
            m = p8.match(line)
            if m:
                if 'candidate_paths' not in ret_dict[sr_pol]:
                    ret_dict[sr_pol].setdefault('candidate_paths', {})
                cur_cand_path += 1
                ret_dict[sr_pol]['candidate_paths'].setdefault(cur_cand_path, {})
                cand_dict = ret_dict[sr_pol]['candidate_paths'][cur_cand_path]
                continue

            # Preference                    : 100
            m = p9.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('preference', int(group['preference']))
                continue

            # Protocol-origin               : CLI
            m = p10.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('protocol_origin', group['protocol_origin'])
                continue

            # Discriminator                 : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('discriminator', int(group['discriminator']))
                continue

            # Active:                       : No
            m = p12.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('active', group['active'])
                continue

            # Number of segment-lists       : 1
            m = p13.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('number_of_segment_lists', int(group['number_of_segment_lists']))
                continue

            # Number of atomic paths        : 1
            m = p14.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('number_of_atomic_paths', int(group['number_of_atomic_paths']))
                continue

            # Number of live UP atomic paths: 1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('number_of_live_up_atomic_paths', int(group['number_of_live_up_atomic_paths']))
                continue

            # Number of live Unknown atomic : 1
            m = p16.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('number_of_live_unknown_atomic', int(group['number_of_live_unknown_atomic']))
                continue

            # Max Pkts per Burst            : 500
            m = p17.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('max_packets_per_burst', int(group['max_packets_per_burst']))
                continue

            # Max Pkts per Probe            : 15000
            m = p18.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('max_packets_per_probe', int(group['max_packets_per_probe']))
                continue

            # AP Min Run per Probe          : 3
            m = p19.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('ap_min_run_per_probe', int(group['ap_min_run_per_probe']))
                continue

            # Round-robin bursts            : 1
            m = p20.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('round_robin_bursts', int(group['round_robin_bursts']))
                continue

            # Round-robin probes            : 1
            m = p21.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('round_robin_probes', int(group['round_robin_probes']))
                continue

            # Last advertisement:
            m = p22.match(line)
            if m:
                cand_dict.setdefault('last_advertisement', {})
                sect_dict = cand_dict['last_advertisement']
                continue

            # Advertised at: 09:06:42  20 2021 (92796 seconds ago)
            m = p23.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('advertised_at', {
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': int(group['second']),
                    'day': int(group['day']),
                    'year': int(group['year']),
                    'seconds_ago': int(group['seconds_ago'])
                })
                continue

            # Advertised delays (uSec): avg: 465, min: 1, max: 999, variance: 464
            m = p24.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('advertised_delays', {
                    'average': int(group['average']),
                    'minimum': int(group['minimum']),
                    'maximum': int(group['maximum']),
                    'variance': int(group['variance'])
                })
                continue

            # Next advertisement:
            m = p25.match(line)
            if m:
                cand_dict.setdefault('next_advertisement', {})
                sect_dict = cand_dict['next_advertisement']
                continue

            # Check scheduled in 2 more probes (roughly every 120 seconds)
            m = p26.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('check_schedule', {
                    'probes': int(group['probes']),
                    'seconds': int(group['second'])
                })
                continue

            # Aggregated delays (uSec): avg: 233, min: 1, max: 499, variance: 232
            m = p27.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('aggregate_delays', {
                    'average': int(group['average']),
                    'minimum': int(group['minimum']),
                    'maximum': int(group['maximum']),
                    'variance': int(group['variance'])
                })
                continue

            # Last probe:
            m = p28.match(line)
            if m:
                cand_dict.setdefault('last_probe', {})
                sect_dict = cand_dict['last_probe']
                continue

            # Packets Sent: 30, received: 30
            m = p29.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('packets', {
                    'packets_sent': int(group['sent']),
                    'packets_received': int(group['received'])
                })
                continue

            # Measured delays (uSec): avg: 233, min: 1, max: 499, variance: 232
            m = p30.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('measured_delays', {
                    'average': int(group['average']),
                    'minimum': int(group['minimum']),
                    'maximum': int(group['maximum']),
                    'variance': int(group['variance'])
                })
                continue

            # Current probe:
            m = p31.match(line)
            if m:
                cand_dict.setdefault('current_probe', {})
                sect_dict = cand_dict['current_probe']
                continue

            # Segment-List:
            m = p32.match(line)
            if m:
                ret_dict[sr_pol]['candidate_paths'][cur_cand_path].setdefault('segment_list', {})
                cand_dict = ret_dict[sr_pol]['candidate_paths'][cur_cand_path]['segment_list']
                cur_atom_path = -1
                continue

            # Name                        : SL7
            m = p33.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('name', group['name'])
                continue

            # Number of atomic paths      : 1
            m = p34.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('number_of_atomic_paths', group['number_of_atomic_paths'])
                continue

            # Atomic path:
            m = p35.match(line)
            if m:
                if 'atomic_paths' not in ret_dict[sr_pol]['candidate_paths'][cur_cand_path]['segment_list']:
                    ret_dict[sr_pol]['candidate_paths'][cur_cand_path]['segment_list'].setdefault('atomic_paths', {})
                cur_atom_path += 1
                ret_dict[sr_pol]['candidate_paths'][cur_cand_path]['segment_list']['atomic_paths'].setdefault(cur_atom_path, {})
                cand_dict = ret_dict[sr_pol]['candidate_paths'][cur_cand_path]['segment_list']['atomic_paths'][cur_atom_path]
                continue


            # Hops                      : 1.1.1.7
            m = p36.match(line)
            if m:
                group = m.groupdict()
                hops = {}
                hop_vals = group['hops'].split(', ')
                for i in range(len(hop_vals)):
                    hops.setdefault(i, str(hop_vals[i]))

                cand_dict.setdefault('hops', hops)
                continue

            # Labels                    : 16230
            # Labels                    : FCCC:CCC1:AA22:AA33:AA11:E003::
            m = p37.match(line)
            if m:
                group = m.groupdict()
                labels = {}
                label_vals = group['labels'].split(', ')
                for i in range(len(label_vals)):
                    if isinstance(label_vals[i], int):
                        labels.setdefault(i, int(label_vals[i]))
                    else:
                        labels.setdefault(i, str(label_vals[i]))
                cand_dict.setdefault('labels', labels)
                continue

            # Outgoing Interface        : Ethernet0/1
            m = p38.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('outgoing_interface', group['outgoing_interface'])
                continue

            # Max IP MTU                : 1500
            m = p39.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('max_ip_mtu', int(group['max_ip_mtu']))
                continue

            # Next Hop                  : 110.1.1.4
            m = p40.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('next_hop', group['next_hop'])
                continue


            # Destination               : 1.1.1.7
            m = p41.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('destination', group['destination'])
                continue

            # Session ID                : 10
            m = p42.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('session_id', int(group['session_id']))
                continue

            # Advertised reason: Periodic timer, avg delay threshold crossed
            m = p43.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('advertised_reason', group['advertised_reason'])
                continue

            # Rolling average (uSec): 287
            m = p44.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('rolling_average', int(group['rolling_average']))
                continue

            # Probe samples:
            m = p45.match(line)
            if m:
                cand_dict.setdefault('probe_samples', {'samples': {}})
                sect_dict = cand_dict['probe_samples']['samples']
                continue

            # Packet Rx Timestamp Measured Delay
            m = p46.match(line)
            if m:
                count_samples = -1
                continue

            # 10:53:18  21 2021 0
            m = p47.match(line)
            if m:
                group = m.groupdict()
                count_samples += 1
                sect_dict.setdefault(count_samples, {
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': int(group['second']),
                    'day': int(group['day']),
                    'year': int(group['year']),
                    'delay': int(group['delay'])
                })
                continue

            # Liveness Detection:
            m = p48.match(line)
            if m:
                cand_dict.setdefault('liveness_detection', {})
                sect_dict = cand_dict['liveness_detection']
                continue

            # Session Creation Timestamp: 05-20 06:46:52.222
            m = p49.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('session_creation_timestamp', {
                    'day': int(group['day']),
                    'month': int(group['month']),
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': float(group['second'])
                })
                continue

            # Session State: Up
            m = p50.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('session_state', group['session_state'])
                continue

            # Last State Change Timestamp: 05-20 06:46:52.414
            m = p51.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('last_state_change_timestamp', {
                    'month': int(group['month']),
                    'day': int(group['day']),
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': float(group['second'])
                })
                continue

            # Missed count   [consecutive]: 0
            p52 = re.compile(r'^Missed count\s+\[consecutive\]: (?P<missed_count>\d+)$')
            m = p52.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('missed_count', int(group['missed_count']))
                continue

            # Received count [consecutive]: 101186
            m = p53.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('received_count', int(group['received_count']))
                continue

            # Backoff                     : 0
            m = p54.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('backoff', int(group['backoff']))
                continue

            # Unique Path Name            : Path-10
            m = p55.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('unique_path_name', group['unique_path_name'])
                continue

            # Loss in Last Interval       : 0 % [TX: 6 RX: 6]
            m = p56.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('loss_in_last_interval', {
                    'percent': int(group['percent']),
                    'tx': int(group['tx']),
                    'rx': int(group['rx'])
                })
                continue

        return ret_dict

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
#   * 'show performance-measurement summary'
#   * 'show performance-measurement summary detail'
#   * 'show performance-measurement summary private'
#   * 'show performance-measurement summary detail private'
# ====================
class ShowPerformanceMeasurementSummarySchema(MetaParser):
    '''Schema for:
        * 'show performance-measurement summary'
        * 'show performance-measurement summary detail'
        * 'show performance-measurement summary private'
    '''

    schema = {
        'total_interfaces': int,
        'total_sr_policies': int,
        'total_endpoints': int,
        'maximum_pps': int,
        'dual_color_gre': {
            'bit_pos' : int,
            Optional('info'): str,
        },
        'interface_delay_measurement': {
            'total_sessions': int,
            'counters': {
                'packets': {
                    'sent': int,
                    'received': int,
                },
                'errors': {
                    Optional('sent_errors'): int,
                    Optional('received_errors'): int,
                    Optional('tx'): {
                        'interface_down': int,
                        'no_mpls_caps': int,
                        'no_ip_address': int,
                        'other': int,
                    },
                    Optional('rx'): {
                        'negative_delay': int,
                        'delay_threshold_exceeded': int,
                        'missing_tx_timestamp': int,
                        'missing_rx_timestamp': int,
                        'probe_full': int,
                        'probe_not_started': int,
                        'control_code_error': int,
                        'control_code_notif': int,
                    },
                },
                'probes': {
                    'started': int,
                    'completed': int,
                    'incomplete': int,
                    'advertisements': int,
                },
            },
        },
        'sr_policy_delay_measurement': {
            'total_sessions': int,
            'counters': {
                'packets': {
                    'sent': int,
                    'received': int,
                },
                'errors': {
                    Optional('sent_errors'): int,
                    Optional('received_errors'): int,
                    Optional('tx'): {
                        'no_ip_address': int,
                        'other': int,
                    },
                    Optional('rx'): {
                        'negative_delay': int,
                        'delay_threshold_exceeded': int,
                        'missing_tx_timestamp': int,
                        'missing_rx_timestamp': int,
                        'probe_full': int,
                        'probe_not_started': int,
                        'control_code_error': int,
                        'control_code_notif': int,
                    },
                },
                'probes': {
                    'started': int,
                    'completed': int,
                    'incomplete': int,
                    'advertisements': int,
                },
            },
        },
        'endpoint_delay_measurement': {
            'total_sessions': int,
            'counters': {
                'packets': {
                    'sent': int,
                    'received': int,
                },
                'errors': {
                    Optional('sent_errors'): int,
                    Optional('received_errors'): int,
                    Optional('tx'): {
                        'interface_down': int,
                        'no_mpls_caps': int,
                        'no_ip_address': int,
                        'other': int,
                    },
                    Optional('rx'): {
                        'negative_delay': int,
                        'delay_threshold_exceeded': int,
                        'missing_tx_timestamp': int,
                        'missing_rx_timestamp': int,
                        'probe_full': int,
                        'probe_not_started': int,
                        'control_code_error': int,
                        'control_code_notif': int,
                    },
                },
                'probes': {
                    'started': int,
                    'completed': int,
                    'incomplete': int,
                    'advertisements': int,
                },
            },
        },
        'interface_loss_measurement': {
            'total_sessions': int,
            'counters': {
                'packets': {
                    'sent': int,
                    'received': int,
                },
                'errors': {
                    Optional('sent_errors'): int,
                    Optional('received_errors'): int,
                    Optional('tx'): {
                        'interface_down': int,
                        'no_mpls_caps': int,
                        'no_ip_address': int,
                        'other': int,
                    },
                    Optional('rx'): {
                        'negative_delay': int,
                        'delay_threshold_exceeded': int,
                        'missing_tx_timestamp': int,
                        'missing_rx_timestamp': int,
                        'probe_full': int,
                        'probe_not_started': int,
                        'control_code_error': int,
                        'control_code_notif': int,
                    },
                },
                'probes': {
                    'started': int,
                    'completed': int,
                    'incomplete': int,
                    'advertisements': int,
                },
            },
        },
        'global_counters': {
            'packets_sent': int,
            'query_packets_received': int,
            'invalid_session_id': int,
            'no_session': int,
        },
        'hw_support_mpls_gal_timestamp': str,
        'hw_support_ipv4_twamp_timestamp': str,
        'hw_support_ipv6_twamp_timestamp': str,
        'hw_support_64_bit_timestamp': str,
        'hw_support_ipv4_udp_checksum': str,
        Optional('max_packets_per_burst'): int,
        Optional('querier_rx_queue'): {
            'size': int,
            'enqueues': int,
            'high_water_mark': int,
            'high_water_mark_time': str,
        },
        Optional('responder_rx_queue'): {
            'size': int,
            'enqueues': int,
            'high_water_mark': int,
            'high_water_mark_time': str,
        },
        Optional('querier_im_queue'): {
            'size': int,
            'enqueues': int,
            'high_water_mark': int,
            'high_water_mark_time': str,
        },
        Optional('querier_cfg_queue'): {
            'size': int,
            'enqueues': int,
            'high_water_mark': int,
            'high_water_mark_time': str,
        },
        Optional('querier_chkpt_queue'): {
            'size': int,
            'enqueues': int,
            'high_water_mark': int,
            'high_water_mark_time': str,
        },
        Optional('udp_port_gal_oob_ipv4'): int,
        Optional('udp_port_gal_oob_ipv6'): int,
        Optional('udp_port_twamp_query_ipv4'): int,
        Optional('udp_port_twamp_query_ipv6'): int,
        Optional('udp_port_twamp_reply_ipv4'): int,
        Optional('udp_port_twamp_reply_ipv6'): int,
        Optional('udp_port_sdlm_query_ipv4'): int,
        Optional('udp_port_sdlm_query_ipv6'): int,
        Optional('udp_port_sdlm_reply_ipv4'): int,
        Optional('udp_port_sdlm_reply_ipv6'): int,
        Optional('last_error_querier'): {
            Optional('info'): str,
            Optional('timestamp'): str,
            Optional('session_id'): int,
        },
        Optional('last_error_receive'): {
            Optional('info'): str,
            Optional('timestamp'): str,
        },
        Optional('pm_runtime'): {
            Any(): {
                'name': str,
                'last': int,
                'avg': int,
                'total': int,
                'cnt': int,
                'wrapped': int,
            },
        },
    }

# ====================
# Parser for:
#   * 'show performance-measurement summary'
#   * 'show performance-measurement summary detail'
#   * 'show performance-measurement summary private'
#   * 'show performance-measurement summary detail private'
# ====================
class ShowPerformanceMeasurementSummary(ShowPerformanceMeasurementSummarySchema):
    '''Parser for:
        * 'show performance-measurement summary'
        * 'show performance-measurement summary detail'
        * 'show performance-measurement summary private'
        * 'show performance-measurement summary detail private'
    '''

    cli_command = [
        'show performance-measurement summary',
        'show performance-measurement summary {detail}',
        'show performance-measurement summary {detail} {private}',
    ]

    def cli(self, detail=None, private=None, output=None):
        if not output:
            cmd = ''
            if detail:
                if private:
                    cmd = self.cli_command[2].format(detail=detail, private=private)
                else:
                    cmd = self.cli_command[1].format(detail=detail)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # Total interfaces                              : 5
        p1 = re.compile(r'^Total interfaces\s+: (?P<total_interfaces>\d+)$')

        # Total SR Policies                             : 3
        p2 = re.compile(r'^Total SR Policies\s+: (?P<total_sr_policies>\d+)$')

        # Total endpoints                               : 2
        p3 = re.compile(r'^Total endpoints\s+: (?P<total_endpoints>\d+)$')

        # Maximum PPS                                   : 2000 pkts/sec
        p4 = re.compile(r'^Maximum PPS\s+: (?P<maximum_pps>\d+) pkts/sec$')

        # Dual-color gre bit-position                   : 8 - Failed, last success 0
        p5 = re.compile(r'^Dual-color gre bit-position\s+: (?P<bit_pos>\d+)( - (?P<info>.+))?$')

        # Interface Delay-Measurement:
        p6 = re.compile(r'^(?P<trans_type>.+) (?P<measurement_type>.+)-Measurement:$')

        # Total sessions                              : 2
        p7 = re.compile(r'^Total sessions\s+: (?P<total_sessions>\d+)$')

        # Counters:
        p8 = re.compile(r'^Counters:$')

        #     Packets:
        p9 = re.compile(r'^Packets:$')

        #     Total sent                              : 288628
        p10 = re.compile(r'^Total sent\s+: (?P<sent>\d+)$')

        #     Total received                          : 0
        p11 = re.compile(r'^Total received\s+: (?P<received>\d+)$')

        #     Errors:
        p12 = re.compile(r'^Errors:$')

        #     Total sent errors                       : 14
        p13 = re.compile(r'^Total sent errors\s+: (?P<sent_errors>\d+)$')

        #     Total received errors                   : 0
        p14 = re.compile(r'^Total received errors\s+: (?P<received_errors>\d+)$')

        #     Probes:
        p15 = re.compile(r'^Probes:$')

        #     Total started                           : 28866
        p16 = re.compile(r'^Total started\s+: (?P<started>\d+)$')

        #     Total completed                         : 0
        p17 = re.compile(r'^Total completed\s+: (?P<completed>\d+)$')

        #     Total incomplete                        : 28864
        p18 = re.compile(r'^Total incomplete\s+: (?P<incomplete>\d+)$')

        #     Total advertisements                    : 0
        p19 = re.compile(r'^Total advertisements\s+: (?P<advertisements>\d+)$')

        # Global Counters:
        p20 = re.compile(r'^Global Counters:$')

        # Total packets sent                          : 3607644
        p21 = re.compile(r'^Total packets sent\s+: (?P<packets_sent>\d+)$')

        # Total query packets received                : 3319004
        p22 = re.compile(r'^Total query packets received\s+: (?P<query_packets_received>\d+)$')

        # Total invalid session id                    : 0
        p23 = re.compile(r'^Total invalid session id\s+: (?P<invalid_session_id>\d+)$')

        # Total no session                            : 0
        p24 = re.compile(r'^Total no session\s+: (?P<no_session>\d+)')

        # HW Support for MPLS-GAL [RFC6374] timestamp   : Yes
        p25 = re.compile(r'^HW Support for MPLS-GAL \[RFC6374\] timestamp\s+: (?P<hw_support_mpls_gal_timestamp>\S+)$')

        # HW Support for IPv4 TWAMP [RF5357] timestamp  : Yes
        p26 = re.compile(r'^HW Support for IPv4 TWAMP \[RF5357\] timestamp\s+: (?P<hw_support_ipv4_twamp_timestamp>\S+)$')

        # HW Support for IPv6 TWAMP [RF5357] timestamp  : No
        p27 = re.compile(r'^HW Support for IPv6 TWAMP \[RF5357\] timestamp\s+: (?P<hw_support_ipv6_twamp_timestamp>\S+)$')

        # HW Support for 64 bit timestamp               : Yes
        p28 = re.compile(r'^HW Support for 64 bit timestamp\s+: (?P<hw_support_64_bit_timestamp>\S+)$')

        # HW Support for IPv4 UDP Cheksum               : Yes
        p29 = re.compile(r'^HW Support for IPv4 UDP Cheksum\s+: (?P<hw_support_ipv4_udp_cheksum>\S+)$')

        # TX:
        p30 = re.compile(r'^TX:$')

        #   Total interface down                : 0
        p31 = re.compile(r'Total interface down\s+: (?P<interface_down>\d+)$')

        #   Total no MPLS caps                  : 0
        p32 = re.compile(r'^Total no MPLS caps\s+: (?P<no_mpls_caps>\d+)$')

        #   Total no IP address                 : 0
        p33 = re.compile(r'^Total no IP address\s+: (?P<no_ip_address>\d+)$')

        #   Total other                         : 14
        p34 = re.compile(r'^Total other\s+: (?P<other>\d+)$')

        # RX:
        p35 = re.compile(r'^RX:$')

        #   Total negative delay                : 0
        p36 = re.compile(r'^Total negative delay\s+: (?P<negative_delay>\d+)$')

        #   Total delay threshold exceeded      : 0
        p37 = re.compile(r'^Total delay threshold exceeded\s+: (?P<delay_threshold_exceeded>\d+)$')

        #   Total missing TX timestamp          : 0
        p38 = re.compile(r'^Total missing TX timestamp\s+: (?P<missing_tx_timestamp>\d+)$')

        #   Total missing RX timestamp          : 0
        p39 = re.compile(r'^Total missing RX timestamp\s+: (?P<missing_rx_timestamp>\d+)$')

        #   Total probe full                    : 0
        p40 = re.compile(r'^Total probe full\s+: (?P<probe_full>\d+)$')

        #   Total probe not started             : 0
        p41 = re.compile(r'^Total probe not started\s+: (?P<probe_not_started>\d+)$')

        #   Total control code error            : 0
        p42 = re.compile(r'^Total control code error\s+: (?P<control_code_error>\d+)$')

        #   Total control code notif            : 0
        p43 = re.compile(r'^Total control code notif\s+: (?P<control_code_notif>\d+)$')

        # Querier RX queue:
        p44 = re.compile(r'^(?P<q_or_p>\S+) (?P<type>\S+) queue:$')

        # Size                                   : 0
        p45 = re.compile(r'^Size\s+: (?P<size>\d+)$')

        # Enqueues                               : 5860
        p46 = re.compile(r'^Enqueues\s+: (?P<enqueues>\d+)$')

        # High water mark                        : 7
        p47 = re.compile(r'^High water mark\s+: (?P<high_water_mark>\d+)$')

        # High water mark time                   : 19 1970 09:42:09.484
        p48 = re.compile(r'^High water mark time\s+: (?P<high_water_mark_time>.+)$')

        # Max packets per burst                         : 2000
        p49 = re.compile(r'^Max packets per burst\s+: (?P<max_packets_per_burst>\d+)$')

        # UDP Port GAL OOB IPV4                         : 63426
        p50 = re.compile(r'^UDP Port (?P<type>.+\S)\s+: (?P<value>\d+)$')

        # Last Error [Querier]:
        p51 = re.compile(r'^Last Error \[(?P<err_type>\S+)\]:$')

        # Timestamp: 06:30:28  20 2021
        p52 = re.compile(r'^Timestamp: (?P<timestamp>.+)$')

        # Unknown destination address type 0.
        p53 = re.compile(r'^(?P<info>.+)$')

        # Session ID: 2
        p54 = re.compile(r'^Session ID: (?P<session_id>\d+)$')

        # PM RUNTIME
        p55 = re.compile(r'^PM RUNTIME$')

        # NAME                LAST        AVG         TOTAL               CNT         WRAPPED
        p56 = re.compile(r'^NAME\s+LAST\s+AVG\s+TOTAL\s+CNT\s+WRAPPED$')

        # CP PROBE START      34000       341861      44442000            130         0
        p57 = re.compile(r'^(?P<name>.+)\s+(?P<last>\d+)\s+(?P<avg>\d+)\s+(?P<total>\d+)\s+(?P<cnt>\d+)\s+(?P<wrapped>\d+)$')

        ret_dict = {}
        trans_type = err_type = ''
        for line in output.splitlines():
            line = line.strip()

            # Total interfaces                              : 5
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_interfaces', int(group['total_interfaces']))
                continue

            # Total SR Policies                             : 3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_sr_policies', int(group['total_sr_policies']))
                continue

            # Total endpoints                               : 2
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_endpoints', int(group['total_endpoints']))
                continue

            # Maximum PPS                                   : 2000 pkts/sec
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('maximum_pps', int(group['maximum_pps']))
                continue

            # Dual-color gre bit-position                   : 8 - Failed, last success 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('dual_color_gre', {'bit_pos': int(group['bit_pos'])})
                if group['info']:
                    ret_dict['dual_color_gre'].setdefault('info', group['info'])
                continue

            # Interface Delay-Measurement:
            m = p6.match(line)
            if m:
                group = m.groupdict()
                trans_type = group['trans_type'].lower().replace('-', '_').replace(' ', '_')
                measurement_type = group['measurement_type'].lower()
                trans_meas_type = trans_type + "_" + measurement_type + "_measurement"
                ret_dict.setdefault(trans_meas_type, {})
                index_dict = ret_dict[trans_meas_type]
                continue

            # Total sessions                              : 2
            m = p7.match(line)
            if m:
                group = m.groupdict()
                index_dict.setdefault('total_sessions', int(group['total_sessions']))

            # Counters:
            m = p8.match(line)
            if m:
                index_dict.setdefault('counters', {})
                sub_index = index_dict['counters']
                continue

            #     Packets:
            m = p9.match(line)
            if m:
                sub_index.setdefault('packets', {})
                continue


            #     Total sent                              : 288628
            m = p10.match(line)
            if m:
                group = m.groupdict()
                sub_index['packets'].setdefault('sent', int(group['sent']))
                continue

            #     Total received                          : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                sub_index['packets'].setdefault('received', int(group['received']))
                continue

            #     Errors:
            m = p12.match(line)
            if m:
                sub_index.setdefault('errors', {})
                continue

            #     Total sent errors                       : 14
            m = p13.match(line)
            if m:
                group = m.groupdict()
                sub_index['errors'].setdefault('sent_errors', int(group['sent_errors']))
                continue

            #     Total received errors                   : 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                sub_index['errors'].setdefault('received_errors', int(group['received_errors']))
                continue

            #     Probes:
            m = p15.match(line)
            if m:
                sub_index.setdefault('probes', {})
                continue

            #     Total started                           : 28866
            m = p16.match(line)
            if m:
                group = m.groupdict()
                sub_index['probes'].setdefault('started', int(group['started']))
                continue

            #     Total completed                         : 0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                sub_index['probes'].setdefault('completed', int(group['completed']))
                continue

            #     Total incomplete                        : 28864
            m = p18.match(line)
            if m:
                group = m.groupdict()
                sub_index['probes'].setdefault('incomplete', int(group['incomplete']))
                continue

            #     Total advertisements                    : 0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                sub_index['probes'].setdefault('advertisements', int(group['advertisements']))
                continue

            # Global Counters:
            m = p20.match(line)
            if m:
                ret_dict.setdefault('global_counters', {})
                index_dict = ret_dict['global_counters']
                continue

            # Total packets sent                          : 3607644
            m = p21.match(line)
            if m:
                group = m.groupdict()
                index_dict.setdefault('packets_sent', int(group['packets_sent']))
                continue

            # Total query packets received                : 3319004
            m = p22.match(line)
            if m:
                group = m.groupdict()
                index_dict.setdefault('query_packets_received', int(group['query_packets_received']))
                continue

            # Total invalid session id                    : 0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                index_dict.setdefault('invalid_session_id', int(group['invalid_session_id']))
                continue

            # Total no session                            : 0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                index_dict.setdefault('no_session', int(group['no_session']))
                continue

            # HW Support for MPLS-GAL [RFC6374] timestamp   : Yes
            m = p25.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('hw_support_mpls_gal_timestamp', group['hw_support_mpls_gal_timestamp'])
                continue

            # HW Support for IPv4 TWAMP [RF5357] timestamp  : Yes
            m = p26.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('hw_support_ipv4_twamp_timestamp', group['hw_support_ipv4_twamp_timestamp'])
                continue

            # HW Support for IPv6 TWAMP [RF5357] timestamp  : No
            m = p27.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('hw_support_ipv6_twamp_timestamp', group['hw_support_ipv6_twamp_timestamp'])
                continue

            # HW Support for 64 bit timestamp               : Yes
            m = p28.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('hw_support_64_bit_timestamp', group['hw_support_64_bit_timestamp'])
                continue

            # HW Support for IPv4 UDP Cheksum               : Yes
            m = p29.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('hw_support_ipv4_udp_checksum', group['hw_support_ipv4_udp_cheksum'])
                continue

            # TX:
            m = p30.match(line)
            if m:
                group = m.groupdict()
                sub_index['errors'].setdefault('tx', {})
                current_error = sub_index['errors']['tx']
                continue

            #   Total interface down                : 0
            m = p31.match(line)
            if m:
                group = m.groupdict()
                current_error.setdefault('interface_down', int(group['interface_down']))
                continue

            #   Total no MPLS caps                  : 0
            m = p32.match(line)
            if m:
                group = m.groupdict()
                current_error.setdefault('no_mpls_caps', int(group['no_mpls_caps']))
                continue

            #   Total no IP address                 : 0
            m = p33.match(line)
            if m:
                group = m.groupdict()
                current_error.setdefault('no_ip_address', int(group['no_ip_address']))
                continue

            #   Total other                         : 14
            m = p34.match(line)
            if m:
                group = m.groupdict()
                current_error.setdefault('other', int(group['other']))
                continue

            # RX:
            m = p35.match(line)
            if m:
                group = m.groupdict()
                sub_index['errors'].setdefault('rx', {})
                current_error = sub_index['errors']['rx']
                continue

            #   Total negative delay                : 0
            m = p36.match(line)
            if m:
                group = m.groupdict()
                current_error.setdefault('negative_delay', int(group['negative_delay']))
                continue

            #   Total delay threshold exceeded      : 0
            m = p37.match(line)
            if m:
                group = m.groupdict()
                current_error.setdefault('delay_threshold_exceeded', int(group['delay_threshold_exceeded']))
                continue

            #   Total missing TX timestamp          : 0
            m = p38.match(line)
            if m:
                group = m.groupdict()
                current_error.setdefault('missing_tx_timestamp', int(group['missing_tx_timestamp']))
                continue

            #   Total missing RX timestamp          : 0
            m = p39.match(line)
            if m:
                group = m.groupdict()
                current_error.setdefault('missing_rx_timestamp', int(group['missing_rx_timestamp']))
                continue

            #   Total probe full                    : 0
            m = p40.match(line)
            if m:
                group = m.groupdict()
                current_error.setdefault('probe_full', int(group['probe_full']))
                continue

            #   Total probe not started             : 0
            m = p41.match(line)
            if m:
                group = m.groupdict()
                current_error.setdefault('probe_not_started', int(group['probe_not_started']))
                continue

            #   Total control code error            : 0
            m = p42.match(line)
            if m:
                group = m.groupdict()
                current_error.setdefault('control_code_error', int(group['control_code_error']))
                continue

            #   Total control code notif            : 0
            m = p43.match(line)
            if m:
                group = m.groupdict()
                current_error.setdefault('control_code_notif', int(group['control_code_notif']))
                continue

            # Querier RX queue:
            m = p44.match(line)
            if m:
                group = m.groupdict()
                dic_name = group['q_or_p'].lower() + "_" + group['type'].lower() + "_queue"
                ret_dict.setdefault(dic_name, {})
                index_dict = ret_dict[dic_name]
                continue

            # Size                                   : 0
            m = p45.match(line)
            if m:
                group = m.groupdict()
                index_dict.setdefault('size', int(group['size']))
                continue

            # Enqueues                               : 5860
            m = p46.match(line)
            if m:
                group = m.groupdict()
                index_dict.setdefault('enqueues', int(group['enqueues']))
                continue

            # High water mark                        : 7
            m = p47.match(line)
            if m:
                group = m.groupdict()
                index_dict.setdefault('high_water_mark', int(group['high_water_mark']))
                continue

            # High water mark time                   : 19 1970 09:42:09.484
            m = p48.match(line)
            if m:
                group = m.groupdict()
                index_dict.setdefault('high_water_mark_time', group['high_water_mark_time'])
                continue

            # Max packets per burst                         : 2000
            m = p49.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('max_packets_per_burst', int(group['max_packets_per_burst']))
                continue

            # UDP Port GAL OOB IPV4                         : 63426
            m = p50.match(line)
            if m:
                group = m.groupdict()
                uportname = 'udp_port_' + group['type'].replace(' ', '_').replace('-', '_').lower()
                ret_dict.setdefault(uportname, int(group['value']))
                continue

            # Last Error [Querier]:
            m = p51.match(line)
            if m:
                group = m.groupdict()
                err_type = 'last_error_' + group['err_type'].lower()
                ret_dict.setdefault(err_type, {})
                index_dict = ret_dict[err_type]
                continue


            # Timestamp: 06:30:28  20 2021
            m = p52.match(line)
            if m:
                group = m.groupdict()
                index_dict.setdefault('timestamp', group['timestamp'])
                continue

            # Unknown destination address type 0.
            m = p53.match(line)
            if m:
                if err_type in ret_dict and 'info' not in ret_dict[err_type]:
                    group = m.groupdict()
                    ret_dict[err_type].setdefault('info', group['info'])
                    continue

            # Session ID: 2
            m = p54.match(line)
            if m:
                group = m.groupdict()
                index_dict.setdefault('session_id', int(group['session_id']))
                continue

            # PM RUNTIME
            m = p55.match(line)
            if m:
                ret_dict.setdefault('pm_runtime', {})
                continue

            # NAME                LAST        AVG         TOTAL               CNT         WRAPPED
            m = p56.match(line)
            if m:
                count_pm_runtime = 0
                continue

            # CP PROBE START      34000       341861      44442000            130         0
            m = p57.match(line)
            if m:
                group = m.groupdict()
                probe = {
                    'name': group['name'].strip(),
                    'last': int(group['last']),
                    'avg': int(group['avg']),
                    'total': int(group['total']),
                    'cnt': int(group['cnt']),
                    'wrapped': int(group['wrapped'])
                }
                ret_dict['pm_runtime'].setdefault(count_pm_runtime, probe)
                count_pm_runtime += 1
                continue

        return ret_dict

# ====================
# Schema for:
#   * 'show performance-measurement paths'
# ====================
class ShowPerformanceMeasurementPathsSchema(MetaParser):
    '''Schema for:
        * 'show performance-measurement paths'
    '''
    schema = {
        Any(): {
            'source': str,
            Optional('endpoint'): str,
            Optional('next_hop'): str,
            Optional('dest'): str,
            Optional('sr_labels'): Or(str, int),
            Optional('outgoing_intf'): str,
            'backoff': int,
            'used_cnt': int,
            Optional('cleanup'): int,
        }
    }

# ====================
# Parser for:
#   * 'show performance-measurement paths'
# ====================
class ShowPerformanceMeasurementPaths(ShowPerformanceMeasurementPathsSchema):
    '''Parser for:
        * 'show performance-measurement paths'
    '''
    cli_command = 'show performance-measurement paths'

    def cli(self, output=None):

        if not output:
            output = self.device.execute(self.cli_command)

        # Path name: Path-7
        p1 = re.compile(r'^Path name:\s+(?P<path_name>(.+))$')

        #   Source                          : 1:2:3:3::1
        p2 = re.compile(r'^Source\s+:\s+(?P<source>[\d\.:A-F]+)$')

        #   Endpoint                        : 1:1:1:7::1
        p3 = re.compile(r'^Endpoint\s+:\s+(?P<endpoint>[\d\.:A-F]+)$')

        #   Next-Hop                        : 1:1:1:7::1
        p4 = re.compile(r'^Next-Hop\s+:\s+(?P<next_hop>[\d\.:A-F]+)$')

        #   Destination                     : 1:1:1:7::1
        p5 = re.compile(r'^Destination\s+:\s+(?P<dest>[\d\.:A-F]+)$')

        #   SR Labels                       : 25, 17
        p6 = re.compile(r'^SR Labels\s+:\s+(?P<sr_labels>([\d:A-F,\s]+))$')

        #   Outgoing Interface              : Ethernet1/2
        p7 = re.compile(r'^Outgoing Interface\s+:\s+(?P<outgoing_intf>(\S+))$')

        #   Backoff                         : 1
        p8 = re.compile(r'^Backoff\s+:\s+(?P<backoff>(\d+))$')

        #   Used Cnt                        : 1
        p9 = re.compile(r'^Used Cnt\s+:\s+(?P<used_cnt>(\d+))$')

        #   Cleanup (seconds)               : 3599
        p10 = re.compile(r'^Cleanup \(seconds\)\s+:\s+(?P<cleanup>(\d+))$')

        # Init return dict
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Path name: Path-7
            m = p1.match(line)
            if m:
                group = m.groupdict()
                path_name = group['path_name']
                ret_dict.setdefault(path_name, {})
                continue

            # Source                          : 1:2:3:3::1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[path_name].setdefault('source', group['source'])
                continue

            #   Endpoint                        : 1:1:1:7::1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict[path_name].setdefault('endpoint', group['endpoint'])
                continue

            #   Next-Hop                        : 1:1:1:7::1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict[path_name].setdefault('next_hop', group['next_hop'])
                continue

            #   Destination                     : 1:1:1:7::1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict[path_name].setdefault('dest', group['dest'])
                continue

            #   SR Labels                       : 25, 17
            m = p6.match(line)
            if m:
                group = m.groupdict()
                labels = group['sr_labels']
                if labels.isdigit(): labels = int(labels)
                ret_dict[path_name].setdefault('sr_labels', labels)
                continue

            #   Outgoing Interface              : Ethernet1/2
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict[path_name].setdefault('outgoing_intf', group['outgoing_intf'])
                continue

            #   Backoff                         : 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict[path_name].setdefault('backoff', int(group['backoff']))
                continue

            #   Used Cnt                        : 1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict[path_name].setdefault('used_cnt', int(group['used_cnt']))
                continue

            #   Cleanup (seconds)               : 3599
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict[path_name].setdefault('cleanup', int(group['cleanup']))
                continue

        return ret_dict


# ====================
# Schema for:
#   * 'show performance-measurement sr-policy'
#   * 'show performance-measurement sr-policy detail'
#   * 'show performance-measurement sr-policy private'
#   * 'show performance-measurement sr-policy verbose'
#   * 'show performance-measurement sr-policy detail verbose'
#   * 'show performance-measurement sr-policy detail private'
#   * 'show performance-measurement sr-policy private verbose'
#   * 'show performance-measurement sr-policy detail private verbose'
#   * 'show performance-measurement sr-policy name {name}'
# ====================
class ShowPerformanceMeasurementSrPolicySchema(MetaParser):
    '''Schema for:
        * 'show performance-measurement sr-policy'
        * 'show performance-measurement sr-policy detail'
        * 'show performance-measurement sr-policy private'
        * 'show performance-measurement sr-policy verbose'
        * 'show performance-measurement sr-policy detail verbose'
        * 'show performance-measurement sr-policy detail private'
        * 'show performance-measurement sr-policy private verbose'
        * 'show performance-measurement sr-policy detail private verbose'
        * 'show performance-measurement sr-policy name {name}'
    '''
    schema = {
        Any(): {

            'color': int,
            'endpoint': str,
            'source': str,
            'profile_name': str,
            'policy_update_timestamp': {
                'month': int,
                'day': int,
                'hour': int,
                'minute': int,
                'second': float
            },
            'number_of_candidate_paths': int,

            'candidate_paths': {

                Any(): {
                    'preference': int,
                    'protocol_origin': str,
                    Optional('discriminator'): int,
                    Optional('active'): str,
                    'number_of_segment_lists': int,
                    'number_of_atomic_paths': int,
                    'number_of_live_up_atomic_paths': int,
                    'number_of_live_unknown_atomic': int,
                    'max_packets_per_burst': int,
                    'max_packets_per_probe': int,
                    'ap_min_run_per_probe': int,
                    'round_robin_bursts': int,
                    'round_robin_probes': int,
                    'last_advertisement': {
                        Optional('advertised_at'): {
                            'hour': int,
                            'minute': int,
                            'second': int,
                            'day': int,
                            'year': int,
                            'seconds_ago': int
                        },
                        Optional('advertised_delays'): {
                            'average': int,
                            'minimum': int,
                            'maximum': int,
                            'variance': int
                        },
                        Optional('advertised_reason'): str,
                    },
                    'next_advertisement': {
                        Optional('check_schedule'): {
                            'probes': int,
                            'seconds': int
                        },
                        Optional('aggregate_delays'): {
                            'average': int,
                            'minimum': int,
                            'maximum': int,
                            'variance': int
                        },
                    },
                    'last_probe': {
                        Optional('packets'): {
                            'packets_sent': int,
                            'packets_received': int
                        },
                        Optional('measured_delays'): {
                            'average': int,
                            'minimum': int,
                            'maximum': int,
                            'variance': int
                        }
                    },
                    'current_probe': {
                        Optional('packets'): {
                            'packets_sent': int,
                            'packets_received': int
                        },
                        Optional('measured_delays'): {
                            'average': int,
                            'minimum': int,
                            'maximum': int,
                            'variance': int
                        }
                    },
                    Optional('segment_list'): {
                        'name': str,
                        'number_of_atomic_paths': int,
                        'last_advertisement': {
                            Optional('advertised_at'): {
                                'day': int,
                                'hour': int,
                                'minute': int,
                                'second': int,
                                'seconds_ago': int,
                                'year': int
                            },
                            Optional('advertised_delays'): {
                                'average': int,
                                'minimum': int,
                                'maximum': int,
                                'variance': int
                            },
                            Optional('advertised_reason'): str,
                        },
                        Optional('next_advertisement'): {
                            Optional('check_schedule'): {
                                'probes': int,
                                'seconds': int
                            },
                            Optional('aggregate_delays'): {
                                'average': int,
                                'minimum': int,
                                'maximum': int,
                                'variance': int
                            },
                        },
                        Optional('last_probe'): {
                            Optional('packets'): {
                                'packets_sent': int,
                                'packets_received': int
                            },
                            Optional('measured_delays'): {
                                'average': int,
                                'minimum': int,
                                'maximum': int,
                                'variance': int
                            }
                        },
                        Optional('current_probe'): {
                            Optional('packets'): {
                                'packets_sent': int,
                                'packets_received': int
                            },
                            Optional('measured_delays'): {
                                'average': int,
                                'minimum': int,
                                'maximum': int,
                                'variance': int
                            }
                        },
                        Optional('atomic_paths'): {
                            Any(): {
                                'hops': {
                                    Any(): str
                                },
                                'labels': {
                                    Any(): Or(str, int)
                                },
                                'outgoing_interface': str,
                                'max_ip_mtu': int,
                                'next_hop': str,
                                'destination': str,
                                'session_id': int,
                                'last_advertisement': {
                                    Optional('advertised_reason'): str,
                                    Optional('advertised_at'): {
                                        'day': int,
                                        'hour': int,
                                        'minute': int,
                                        'second': int,
                                        'seconds_ago': int,
                                        'year': int
                                    },
                                    Optional('advertised_delays'): {
                                        'average': int,
                                        'minimum': int,
                                        'maximum': int,
                                        'variance': int
                                    },
                                },
                                'next_advertisement': {
                                    Optional('aggregate_delays'): {
                                        'average': int,
                                        'minimum': int,
                                        'maximum': int,
                                        'variance': int
                                    },
                                    Optional('rolling_average'): int
                                },
                                'last_probe': {
                                    Optional('packets'): {
                                        'packets_sent': int,
                                        'packets_received': int
                                    },
                                    Optional('measured_delays'): {
                                        'average': int,
                                        'minimum': int,
                                        'maximum': int,
                                        'variance': int
                                    }
                                },
                                'current_probe': {
                                    Optional('packets'): {
                                        'packets_sent': int,
                                        'packets_received': int
                                    },
                                    Optional('measured_delays'): {
                                        'average': int,
                                        'minimum': int,
                                        'maximum': int,
                                        'variance': int
                                    }
                                },
                                'probe_samples': {
                                    'samples': {
                                        Any(): {
                                            'hour': int,
                                            'minute': int,
                                            'second': int,
                                            'day': int,
                                            'year': int,
                                            'delay': int
                                        }
                                    }
                                },
                                'liveness_detection': {
                                    'session_creation_timestamp': {
                                        'month': int,
                                        'day': int,
                                        'hour': int,
                                        'minute': int,
                                        'second': float
                                    },
                                    'session_state': str,
                                    'last_state_change_timestamp': {
                                        'month': int,
                                        'day': int,
                                        'hour': int,
                                        'minute': int,
                                        'second': float
                                    },
                                    'missed_count': int,
                                    'received_count': int,
                                    'backoff': int,
                                    'unique_path_name': str,
                                    'loss_in_last_interval': {
                                        'percent': int,
                                        'tx': int,
                                        'rx': int
                                    }
                                }

                            }
                        }
                    }
                }

            }
        }
    }

# ====================
# Parser for:
#   * 'show performance-measurement sr-policy'
#   * 'show performance-measurement sr-policy detail'
#   * 'show performance-measurement sr-policy private'
#   * 'show performance-measurement sr-policy verbose'
#   * 'show performance-measurement sr-policy detail verbose'
#   * 'show performance-measurement sr-policy detail private'
#   * 'show performance-measurement sr-policy private verbose'
#   * 'show performance-measurement sr-policy detail private verbose'
#   * 'show performance-measurement sr-policy name {name}'
# ====================
class ShowPerformanceMeasurementSrPolicy(ShowPerformanceMeasurementSrPolicySchema):
    '''Parser for:
        * 'show performance-measurement sr-policy'
        * 'show performance-measurement sr-policy detail'
        * 'show performance-measurement sr-policy private'
        * 'show performance-measurement sr-policy verbose'
        * 'show performance-measurement sr-policy detail verbose'
        * 'show performance-measurement sr-policy detail private'
        * 'show performance-measurement sr-policy private verbose'
        * 'show performance-measurement sr-policy detail private verbose'
        * 'show performance-measurement sr-policy name {name}'
    '''

    cli_command = [
        'show performance-measurement sr-policy',
        'show performance-measurement sr-policy {detail}',
        'show performance-measurement sr-policy {detail} {private}',
        'show performance-measurement sr-policy {detail} {private} {verbose}',
        'show performance-measurement sr-policy name {name}',
        'show performance-measurement sr-policy name {name} {detail}',
        'show performance-measurement sr-policy name {name} {detail} {private}',
        'show performance-measurement sr-policy name {name} {detail} {private} {verbose}'
    ]

    def cli(self, name=None, detail=None, private=None, verbose=None, output=None):
        if not output:
            cmd = ''
            if name:
                if detail:
                    if private:
                        if verbose:
                            cmd = self.cli_command[7].format(name=name, detail=detail, private=private, verbose=verbose)
                        else:
                            cmd = self.cli_command[6].format(name=name, detail=detail, private=private)
                    else:
                        cmd = self.cli_command[5].format(name=name, detail=detail)
                else:
                    cmd = self.cli_command[4].format(name=name)
            else:
                if detail:
                    if private:
                        if verbose:
                            cmd = self.cli_command[3].format(detail=detail, private=private, verbose=verbose)
                        else:
                            cmd = self.cli_command[2].format(detail=detail, private=private)
                    else:
                        cmd = self.cli_command[1].format(detail=detail)
                else:
                    cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # SR Policy name: Ethernet0/0
        p1 = re.compile(r'^SR Policy name: (?P<sr_policy_name>\S+)$')

        # Color                           : 1235
        p2 = re.compile(r'^Color\s+: (?P<color>\d+)$')

        # Endpoint                        : 1.1.1.7
        p3 = re.compile(r'^Endpoint\s+: (?P<endpoint>[\d\.:A-F]+)$')

        # Source                          : 1.1.1.3
        p4 = re.compile(r'^Source\s+: (?P<source>[\d\.:A-F]+)$')

        # Profile name                    : Not configured
        p5 = re.compile(r'^Profile name\s+: (?P<profile_name>.+)$')

        # Policy Update Timestamp         : 05-20 06:46:52.222
        p6 = re.compile(r'^Policy Update Timestamp\s+: (?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d*\.\d+)$')

        # Number of candidate-paths       : 1
        p7 = re.compile(r'^Number of candidate-paths\s+: (?P<number_of_candidate_paths>\d+)$')

        # Candidate-Path:
        p8 = re.compile(r'^Candidate-Path:$')

        # Preference                    : 100
        p9 = re.compile(r'^Preference\s+: (?P<preference>\d+)$')

        # Protocol-origin               : CLI
        p10 = re.compile(r'^Protocol-origin\s+: (?P<protocol_origin>.+)$')

        # Discriminator                 : 0
        p11 = re.compile(r'^Discriminator\s+: (?P<discriminator>\d+)$')

        # Active:                       : No
        p12 = re.compile(r'^Active:\s+: (?P<active>\S+)$')

        # Number of segment-lists       : 1
        p13 = re.compile(r'^Number of segment-lists\s+: (?P<number_of_segment_lists>\d+)$')

        # Number of atomic paths        : 1
        p14 = re.compile(r'^Number of atomic paths\s+: (?P<number_of_atomic_paths>\d+)$')

        # Number of live UP atomic paths: 1
        p15 = re.compile(r'^Number of live UP atomic paths:\s+(?P<number_of_live_up_atomic_paths>\d+)$')

        # Number of live Unknown atomic : 1
        p16 = re.compile(r'^Number of live Unknown atomic\s+: (?P<number_of_live_unknown_atomic>\d+)$')

        # Max Pkts per Burst            : 500
        p17 = re.compile(r'^Max Pkts per Burst\s+: (?P<max_packets_per_burst>\d+)$')

        # Max Pkts per Probe            : 15000
        p18 = re.compile(r'^Max Pkts per Probe\s+: (?P<max_packets_per_probe>\d+)$')

        # AP Min Run per Probe          : 3
        p19 = re.compile(r'^AP Min Run per Probe\s+: (?P<ap_min_run_per_probe>\d+)$')

        # Round-robin bursts            : 1
        p20 = re.compile(r'^Round-robin bursts\s+: (?P<round_robin_bursts>\d+)$')

        # Round-robin probes            : 1
        p21 = re.compile(r'^Round-robin probes\s+: (?P<round_robin_probes>\d+)$')

        # Last advertisement:
        p22 = re.compile(r'^Last advertisement:$')

        # Advertised at: 09:06:42  20 2021 (92796 seconds ago)
        p23 = re.compile(r'^Advertised at: (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)\s+(?P<day>\d+)\s+(?P<year>\d+)\s+\((?P<seconds_ago>\d+) seconds ago\)$')

        # Advertised delays (uSec): avg: 465, min: 1, max: 999, variance: 464
        p24 = re.compile(r'^Advertised delays\s+\(uSec\): avg: (?P<average>\d+), min: (?P<minimum>\d+), max: (?P<maximum>\d+), variance: (?P<variance>\d+)$')

        # Next advertisement:
        p25 = re.compile(r'^Next advertisement:$')

        # Check scheduled in 2 more probes (roughly every 120 seconds)
        p26 = re.compile(r'^Check scheduled in (?P<probes>\d+) more probe\S* \(roughly every (?P<second>\d+) seconds\)$')

        # Aggregated delays (uSec): avg: 233, min: 1, max: 499, variance: 232
        p27 = re.compile(r'^Aggregated delays \(uSec\): avg: (?P<average>\d+), min: (?P<minimum>\d+), max: (?P<maximum>\d+), variance: (?P<variance>\d+)$')

        # Last probe:
        p28 = re.compile(r'^Last probe:$')

        # Packets Sent: 30, received: 30
        p29 = re.compile(r'^Packets Sent: (?P<sent>\d+), received: (?P<received>\d+)$')

        # Measured delays (uSec): avg: 233, min: 1, max: 499, variance: 232
        p30 = re.compile(r'^Measured delays \(uSec\): avg: (?P<average>\d+), min: (?P<minimum>\d+), max: (?P<maximum>\d+), variance: (?P<variance>\d+)$')

        # Current probe:
        p31 = re.compile(r'^Current probe:$')

        # Segment-List:
        p32 = re.compile(r'^Segment-List:$')

        # Name                        : SL7
        p33 = re.compile(r'^Name\s+: (?P<name>\S+)$')

        # Number of atomic paths      : 1
        p34 = re.compile(r'^Number of atomic paths\s+: (?P<number_of_atomic_paths>\d+)$')

        # Atomic path:
        p35 = re.compile(r'^Atomic path:$')

        # Hops                      : 1.1.1.7
        p36 = re.compile(r'^Hops\s+: (?P<hops>.+)$')

        # Labels                    : 16230
        # Labels                    : FCCC:CCC1:AA22:AA33:AA11:E003::
        p37 = re.compile(r'^Labels\s+: (?P<labels>[\d:A-F,\s]+)$')

        # Outgoing Interface        : Ethernet0/1
        p38 = re.compile(r'^Outgoing Interface\s+: (?P<outgoing_interface>\S+)$')

        # Max IP MTU                : 1500
        p39 = re.compile(r'^Max IP MTU\s+: (?P<max_ip_mtu>\d+)$')

        # Next Hop                  : 110.1.1.4
        p40 = re.compile(r'^Next Hop\s+: (?P<next_hop>[\d\.:A-F]+)$')

        # Destination               : 1.1.1.7
        p41 = re.compile(r'^Destination\s+: (?P<destination>[\d\.:A-F]+)$')

        # Session ID                : 10
        p42 = re.compile(r'^Session ID\s+: (?P<session_id>\d+)$')

        # Advertised reason: Periodic timer, avg delay threshold crossed
        p43 = re.compile(r'^Advertised reason: (?P<advertised_reason>.+)$')

        # Rolling average (uSec): 287
        p44 = re.compile(r'^Rolling average \(uSec\): (?P<rolling_average>\d+)$')

        # Probe samples:
        p45 = re.compile(r'^Probe samples:$')

        # Packet Rx Timestamp Measured Delay
        p46 = re.compile(r'^Packet Rx Timestamp Measured Delay$')

        # 10:53:18  21 2021 0
        p47 = re.compile(r'^(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)\s+(?P<day>\d+)\s+(?P<year>\d+)\s+(?P<delay>\d+)$')

        # Liveness Detection:
        p48 = re.compile(r'^Liveness Detection:$')

        # Session Creation Timestamp: 05-20 06:46:52.222
        p49 = re.compile(r'^Session Creation Timestamp: (?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d*\.\d+)$')

        # Session State: Up
        p50 = re.compile(r'^Session State: (?P<session_state>\S+)$')

        # Last State Change Timestamp: 05-20 06:46:52.414
        p51 = re.compile(r'^Last State Change Timestamp: (?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+):(?P<second>\d*\.\d+)$')

        # Missed count   [consecutive]: 0
        p52 = re.compile(r'^Missed count\s+\[consecutive\]: (?P<missed_count>\d+)$')

        # Received count [consecutive]: 101186
        p53 = re.compile(r'^Received count \[consecutive\]: (?P<received_count>\d+)$')

        # Backoff                     : 0
        p54 = re.compile(r'^Backoff\s+: (?P<backoff>\d+)$')

        # Unique Path Name            : Path-10
        p55 = re.compile(r'^Unique Path Name\s+: (?P<unique_path_name>\S+)$')

        # Loss in Last Interval       : 0 % [TX: 6 RX: 6]
        p56 = re.compile(r'^Loss in Last Interval\s+: (?P<percent>\d+) % \[TX: (?P<tx>\d+) RX: (?P<rx>\d+)\]$')

        ret_dict = {}
        sr_pol = ''
        cur_cand_path = -1
        cur_atom_path = -1
        for line in output.splitlines():
            line = line.strip()

            # SR Policy name: Ethernet0/0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sr_pol = group['sr_policy_name']
                ret_dict.setdefault(sr_pol, {})
                cur_cand_path = -1
                continue

            # Color                           : 1235
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[sr_pol].setdefault('color', int(group['color']))
                continue

            # Endpoint                        : 1.1.1.7
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict[sr_pol].setdefault('endpoint', group['endpoint'])
                continue

            # Source                          : 1.1.1.3
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict[sr_pol].setdefault('source', group['source'])
                continue

            # Profile name                    : Not configured
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict[sr_pol].setdefault('profile_name', group['profile_name'])
                continue

            # Policy Update Timestamp         : 05-20 06:46:52.222
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict[sr_pol].setdefault('policy_update_timestamp', {
                    'month': int(group['month']),
                    'day': int(group['day']),
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': float(group['second'])
                })
                continue

            # Number of candidate-paths       : 1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict[sr_pol].setdefault('number_of_candidate_paths', int(group['number_of_candidate_paths']))
                continue

            # Candidate-Path:
            m = p8.match(line)
            if m:
                if 'candidate_paths' not in ret_dict[sr_pol]:
                    ret_dict[sr_pol].setdefault('candidate_paths', {})
                cur_cand_path += 1
                ret_dict[sr_pol]['candidate_paths'].setdefault(cur_cand_path, {})
                cand_dict = ret_dict[sr_pol]['candidate_paths'][cur_cand_path]
                continue

            # Preference                    : 100
            m = p9.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('preference', int(group['preference']))
                continue

            # Protocol-origin               : CLI
            m = p10.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('protocol_origin', group['protocol_origin'])
                continue

            # Discriminator                 : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('discriminator', int(group['discriminator']))
                continue

            # Active:                       : No
            m = p12.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('active', group['active'])
                continue

            # Number of segment-lists       : 1
            m = p13.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('number_of_segment_lists', int(group['number_of_segment_lists']))
                continue

            # Number of atomic paths        : 1
            m = p14.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('number_of_atomic_paths', int(group['number_of_atomic_paths']))
                continue

            # Number of live UP atomic paths: 1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('number_of_live_up_atomic_paths', int(group['number_of_live_up_atomic_paths']))
                continue

            # Number of live Unknown atomic : 1
            m = p16.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('number_of_live_unknown_atomic', int(group['number_of_live_unknown_atomic']))
                continue

            # Max Pkts per Burst            : 500
            m = p17.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('max_packets_per_burst', int(group['max_packets_per_burst']))
                continue

            # Max Pkts per Probe            : 15000
            m = p18.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('max_packets_per_probe', int(group['max_packets_per_probe']))
                continue

            # AP Min Run per Probe          : 3
            m = p19.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('ap_min_run_per_probe', int(group['ap_min_run_per_probe']))
                continue

            # Round-robin bursts            : 1
            m = p20.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('round_robin_bursts', int(group['round_robin_bursts']))
                continue

            # Round-robin probes            : 1
            m = p21.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('round_robin_probes', int(group['round_robin_probes']))
                continue

            # Last advertisement:
            m = p22.match(line)
            if m:
                cand_dict.setdefault('last_advertisement', {})
                sect_dict = cand_dict['last_advertisement']
                continue

            # Advertised at: 09:06:42  20 2021 (92796 seconds ago)
            m = p23.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('advertised_at', {
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': int(group['second']),
                    'day': int(group['day']),
                    'year': int(group['year']),
                    'seconds_ago': int(group['seconds_ago'])
                })
                continue

            # Advertised delays (uSec): avg: 465, min: 1, max: 999, variance: 464
            m = p24.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('advertised_delays', {
                    'average': int(group['average']),
                    'minimum': int(group['minimum']),
                    'maximum': int(group['maximum']),
                    'variance': int(group['variance'])
                })
                continue

            # Next advertisement:
            m = p25.match(line)
            if m:
                cand_dict.setdefault('next_advertisement', {})
                sect_dict = cand_dict['next_advertisement']
                continue

            # Check scheduled in 2 more probes (roughly every 120 seconds)
            m = p26.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('check_schedule', {
                    'probes': int(group['probes']),
                    'seconds': int(group['second'])
                })
                continue

            # Aggregated delays (uSec): avg: 233, min: 1, max: 499, variance: 232
            m = p27.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('aggregate_delays', {
                    'average': int(group['average']),
                    'minimum': int(group['minimum']),
                    'maximum': int(group['maximum']),
                    'variance': int(group['variance'])
                })
                continue

            # Last probe:
            m = p28.match(line)
            if m:
                cand_dict.setdefault('last_probe', {})
                sect_dict = cand_dict['last_probe']
                continue

            # Packets Sent: 30, received: 30
            m = p29.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('packets', {
                    'packets_sent': int(group['sent']),
                    'packets_received': int(group['received'])
                })
                continue

            # Measured delays (uSec): avg: 233, min: 1, max: 499, variance: 232
            m = p30.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('measured_delays', {
                    'average': int(group['average']),
                    'minimum': int(group['minimum']),
                    'maximum': int(group['maximum']),
                    'variance': int(group['variance'])
                })
                continue

            # Current probe:
            m = p31.match(line)
            if m:
                cand_dict.setdefault('current_probe', {})
                sect_dict = cand_dict['current_probe']
                continue

            # Segment-List:
            m = p32.match(line)
            if m:
                ret_dict[sr_pol]['candidate_paths'][cur_cand_path].setdefault('segment_list', {})
                cand_dict = ret_dict[sr_pol]['candidate_paths'][cur_cand_path]['segment_list']
                cur_atom_path = -1
                continue

            # Name                        : SL7
            m = p33.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('name', group['name'])
                continue

            # Number of atomic paths      : 1
            m = p34.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('number_of_atomic_paths', group['number_of_atomic_paths'])
                continue

            # Atomic path:
            m = p35.match(line)
            if m:
                if 'atomic_paths' not in ret_dict[sr_pol]['candidate_paths'][cur_cand_path]['segment_list']:
                    ret_dict[sr_pol]['candidate_paths'][cur_cand_path]['segment_list'].setdefault('atomic_paths', {})
                cur_atom_path += 1
                ret_dict[sr_pol]['candidate_paths'][cur_cand_path]['segment_list']['atomic_paths'].setdefault(cur_atom_path, {})
                cand_dict = ret_dict[sr_pol]['candidate_paths'][cur_cand_path]['segment_list']['atomic_paths'][cur_atom_path]
                continue


            # Hops                      : 1.1.1.7
            m = p36.match(line)
            if m:
                group = m.groupdict()
                hops = {}
                hop_vals = group['hops'].split(', ')
                for i in range(len(hop_vals)):
                    hops.setdefault(i, str(hop_vals[i]))

                cand_dict.setdefault('hops', hops)
                continue

            # Labels                    : 16230
            # Labels                    : FCCC:CCC1:AA22:AA33:AA11:E003::
            m = p37.match(line)
            if m:
                group = m.groupdict()
                labels = {}
                label_vals = group['labels'].split(', ')
                for i in range(len(label_vals)):
                    if isinstance(label_vals[i], int):
                        labels.setdefault(i, int(label_vals[i]))
                    else:
                        labels.setdefault(i, str(label_vals[i]))
                cand_dict.setdefault('labels', labels)
                continue

            # Outgoing Interface        : Ethernet0/1
            m = p38.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('outgoing_interface', group['outgoing_interface'])
                continue

            # Max IP MTU                : 1500
            m = p39.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('max_ip_mtu', int(group['max_ip_mtu']))
                continue

            # Next Hop                  : 110.1.1.4
            m = p40.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('next_hop', group['next_hop'])
                continue


            # Destination               : 1.1.1.7
            m = p41.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('destination', group['destination'])
                continue

            # Session ID                : 10
            m = p42.match(line)
            if m:
                group = m.groupdict()
                cand_dict.setdefault('session_id', int(group['session_id']))
                continue

            # Advertised reason: Periodic timer, avg delay threshold crossed
            m = p43.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('advertised_reason', group['advertised_reason'])
                continue

            # Rolling average (uSec): 287
            m = p44.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('rolling_average', int(group['rolling_average']))
                continue

            # Probe samples:
            m = p45.match(line)
            if m:
                cand_dict.setdefault('probe_samples', {'samples': {}})
                sect_dict = cand_dict['probe_samples']['samples']
                continue

            # Packet Rx Timestamp Measured Delay
            m = p46.match(line)
            if m:
                count_samples = -1
                continue

            # 10:53:18  21 2021 0
            m = p47.match(line)
            if m:
                group = m.groupdict()
                count_samples += 1
                sect_dict.setdefault(count_samples, {
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': int(group['second']),
                    'day': int(group['day']),
                    'year': int(group['year']),
                    'delay': int(group['delay'])
                })
                continue

            # Liveness Detection:
            m = p48.match(line)
            if m:
                cand_dict.setdefault('liveness_detection', {})
                sect_dict = cand_dict['liveness_detection']
                continue

            # Session Creation Timestamp: 05-20 06:46:52.222
            m = p49.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('session_creation_timestamp', {
                    'day': int(group['day']),
                    'month': int(group['month']),
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': float(group['second'])
                })
                continue

            # Session State: Up
            m = p50.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('session_state', group['session_state'])
                continue

            # Last State Change Timestamp: 05-20 06:46:52.414
            m = p51.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('last_state_change_timestamp', {
                    'month': int(group['month']),
                    'day': int(group['day']),
                    'hour': int(group['hour']),
                    'minute': int(group['minute']),
                    'second': float(group['second'])
                })
                continue

            # Missed count   [consecutive]: 0
            p52 = re.compile(r'^Missed count\s+\[consecutive\]: (?P<missed_count>\d+)$')
            m = p52.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('missed_count', int(group['missed_count']))
                continue

            # Received count [consecutive]: 101186
            m = p53.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('received_count', int(group['received_count']))
                continue

            # Backoff                     : 0
            m = p54.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('backoff', int(group['backoff']))
                continue

            # Unique Path Name            : Path-10
            m = p55.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('unique_path_name', group['unique_path_name'])
                continue

            # Loss in Last Interval       : 0 % [TX: 6 RX: 6]
            m = p56.match(line)
            if m:
                group = m.groupdict()
                sect_dict.setdefault('loss_in_last_interval', {
                    'percent': int(group['percent']),
                    'tx': int(group['tx']),
                    'rx': int(group['rx'])
                })
                continue

        return ret_dict

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
