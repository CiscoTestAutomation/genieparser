"""show_x25.py

IOSXE parsers for the following show commands:
    * show x25 vc
"""

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ===============================================
# Schema for:
#   * 'show x25 vc'
# ===============================================
class ShowX25VcSchema(MetaParser):

    """ Schema for:
        * 'show x25 vc'
    """

    schema = {
        'svc': {
            Any(): {
                'state': str,
                'interface': str,
                'started': str,
                'last_input': str,
                'last_output': str,
                'connects': {
                    'local': str,
                    'remote_protocol': str,
                    'remote_address': str,
                },
                'call_pid': str,
                'data_pid': str,
                'window_size': {
                    'input': int,
                    'output': int,
                },
                'packet_size': {
                    'input': int,
                    'output': int,
                },
                'ps': int,
                'pr': int,
                'ack': int,
                'remote_pr': int,
                'rcnt': int,
                'rnr': str,
                'pd_state_timeouts': int,
                'timer_secs': int,
                'statistics': {
                    'data_bytes': {
                        'input': int,
                        'output': int,
                    },
                    'packets': {
                        'input': int,
                        'output': int,
                    },
                    'resets': {
                        'input': int,
                        'output': int,
                    },
                    'rnrs': {
                        'input': int,
                        'output': int,
                    },
                    'rejs': {
                        'input': int,
                        'output': int,
                    },
                    'ints': {
                        'input': int,
                        'output': int,
                    },
                },
            },
        },
    }


# ===============================================
# Parser for:
#   * 'show x25 vc'
# ===============================================
class ShowX25Vc(ShowX25VcSchema):

    """ Parser for:
        * 'show x25 vc'
    """

    cli_command = 'show x25 vc'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize return dictionary
        parsed_dict = {}

        # SVC 1024,  State: D1,  Interface: Serial0/3/1
        p1 = re.compile(r'^SVC\s+(?P<svc>\d+),\s+State:\s+(?P<state>\S+),\s+Interface:\s+(?P<interface>\S+)$')

        # Started 00:00:18, last input 00:00:15, output 00:00:15
        p2 = re.compile(r'^\s*Started\s+(?P<started>\S+),\s+last\s+input\s+(?P<last_input>\S+),\s+output\s+(?P<last_output>\S+)$')

        # Connects 170092 <-> ip 1.0.0.2
        p3 = re.compile(r'^\s*Connects\s+(?P<local>\S+)\s+<->\s+(?P<remote_protocol>\S+)\s+(?P<remote_address>\S+)$')

        # Call PID cisco, Data PID none
        p4 = re.compile(r'^\s*Call\s+PID\s+(?P<call_pid>\S+),\s+Data\s+PID\s+(?P<data_pid>\S+)$')

        # Window size input: 5, output: 5
        p5 = re.compile(r'^\s*Window\s+size\s+input:\s+(?P<input>\d+),\s+output:\s+(?P<output>\d+)$')

        # Packet size input: 128, output: 128
        p6 = re.compile(r'^\s*Packet\s+size\s+input:\s+(?P<input>\d+),\s+output:\s+(?P<output>\d+)$')

        # PS: 0  PR: 0  ACK: 4  Remote PR: 0  RCNT: 4  RNR: no
        p7 = re.compile(r'^\s*PS:\s+(?P<ps>\d+)\s+PR:\s+(?P<pr>\d+)\s+ACK:\s+(?P<ack>\d+)\s+Remote\s+PR:\s+(?P<remote_pr>\d+)\s+RCNT:\s+(?P<rcnt>\d+)\s+RNR:\s+(?P<rnr>\S+)$')

        # P/D state timeouts: 0  timer (secs): 0
        p8 = re.compile(r'^\s*P/D\s+state\s+timeouts:\s+(?P<pd_timeouts>\d+)\s+timer\s+\(secs\):\s+(?P<timer>\d+)$')

        # data bytes 10000/10000 packets 80/80 Resets 0/0 RNRs 0/0 REJs 0/0 INTs 0/0
        p9 = re.compile(r'^\s*data\s+bytes\s+(?P<data_bytes_in>\d+)/(?P<data_bytes_out>\d+)\s+packets\s+(?P<packets_in>\d+)/(?P<packets_out>\d+)\s+Resets\s+(?P<resets_in>\d+)/(?P<resets_out>\d+)\s+RNRs\s+(?P<rnrs_in>\d+)/(?P<rnrs_out>\d+)\s+REJs\s+(?P<rejs_in>\d+)/(?P<rejs_out>\d+)\s+INTs\s+(?P<ints_in>\d+)/(?P<ints_out>\d+)$')

        current_svc = None

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # SVC 1024,  State: D1,  Interface: Serial0/3/1
            m = p1.match(line)
            if m:
                svc = m.groupdict()['svc']
                state = m.groupdict()['state']
                interface = m.groupdict()['interface']
                current_svc = svc

                # Initialize SVC structure
                if 'svc' not in parsed_dict:
                    parsed_dict['svc'] = {}
                if current_svc not in parsed_dict['svc']:
                    parsed_dict['svc'][current_svc] = {}

                parsed_dict['svc'][current_svc]['state'] = state
                parsed_dict['svc'][current_svc]['interface'] = interface
                continue

            # Started 00:00:18, last input 00:00:15, output 00:00:15
            m = p2.match(line)
            if m and current_svc is not None:
                parsed_dict['svc'][current_svc]['started'] = m.groupdict()['started']
                parsed_dict['svc'][current_svc]['last_input'] = m.groupdict()['last_input']
                parsed_dict['svc'][current_svc]['last_output'] = m.groupdict()['last_output']
                continue

            # Connects 170092 <-> ip 1.0.0.2
            m = p3.match(line)
            if m and current_svc is not None:
                parsed_dict['svc'][current_svc]['connects'] = {
                    'local': m.groupdict()['local'],
                    'remote_protocol': m.groupdict()['remote_protocol'],
                    'remote_address': m.groupdict()['remote_address']
                }
                continue

            # Call PID cisco, Data PID none
            m = p4.match(line)
            if m and current_svc is not None:
                parsed_dict['svc'][current_svc]['call_pid'] = m.groupdict()['call_pid']
                parsed_dict['svc'][current_svc]['data_pid'] = m.groupdict()['data_pid']
                continue

            # Window size input: 5, output: 5
            m = p5.match(line)
            if m and current_svc is not None:
                parsed_dict['svc'][current_svc]['window_size'] = {
                    'input': int(m.groupdict()['input']),
                    'output': int(m.groupdict()['output'])
                }
                continue

            # Packet size input: 128, output: 128
            m = p6.match(line)
            if m and current_svc is not None:
                parsed_dict['svc'][current_svc]['packet_size'] = {
                    'input': int(m.groupdict()['input']),
                    'output': int(m.groupdict()['output'])
                }
                continue

            # PS: 0  PR: 0  ACK: 4  Remote PR: 0  RCNT: 4  RNR: no
            m = p7.match(line)
            if m and current_svc is not None:
                parsed_dict['svc'][current_svc]['ps'] = int(m.groupdict()['ps'])
                parsed_dict['svc'][current_svc]['pr'] = int(m.groupdict()['pr'])
                parsed_dict['svc'][current_svc]['ack'] = int(m.groupdict()['ack'])
                parsed_dict['svc'][current_svc]['remote_pr'] = int(m.groupdict()['remote_pr'])
                parsed_dict['svc'][current_svc]['rcnt'] = int(m.groupdict()['rcnt'])
                parsed_dict['svc'][current_svc]['rnr'] = m.groupdict()['rnr']
                continue

            # P/D state timeouts: 0  timer (secs): 0
            m = p8.match(line)
            if m and current_svc is not None:
                parsed_dict['svc'][current_svc]['pd_state_timeouts'] = int(m.groupdict()['pd_timeouts'])
                parsed_dict['svc'][current_svc]['timer_secs'] = int(m.groupdict()['timer'])
                continue

            # data bytes 10000/10000 packets 80/80 Resets 0/0 RNRs 0/0 REJs 0/0 INTs 0/0
            m = p9.match(line)
            if m and current_svc is not None:
                parsed_dict['svc'][current_svc]['statistics'] = {
                    'data_bytes': {
                        'input': int(m.groupdict()['data_bytes_in']),
                        'output': int(m.groupdict()['data_bytes_out'])
                    },
                    'packets': {
                        'input': int(m.groupdict()['packets_in']),
                        'output': int(m.groupdict()['packets_out'])
                    },
                    'resets': {
                        'input': int(m.groupdict()['resets_in']),
                        'output': int(m.groupdict()['resets_out'])
                    },
                    'rnrs': {
                        'input': int(m.groupdict()['rnrs_in']),
                        'output': int(m.groupdict()['rnrs_out'])
                    },
                    'rejs': {
                        'input': int(m.groupdict()['rejs_in']),
                        'output': int(m.groupdict()['rejs_out'])
                    },
                    'ints': {
                        'input': int(m.groupdict()['ints_in']),
                        'output': int(m.groupdict()['ints_out'])
                    }
                }
                continue

        return parsed_dict