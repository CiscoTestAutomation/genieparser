import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowConnectionSchema(MetaParser):
    '''Schema for show connection name'''
    schema = {
        'last_clearing_of_qfp_drops_statistics': str,
        'connections': {
            Any(): {
                'current_state': str,
                'segment': {
                    Any(): {
                        'tdm_timeslots_in_use': str,
                        Optional('total'): Optional(int),
                    }
                },
                'internal_switching_elements': str,
            }
        }
    }


class ShowConnection(ShowConnectionSchema):
    '''Parser for show connection name'''
    cli_command = 'show connection name'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Initialize the return dictionary
        parsed = {}
        segment_dict = None

        # Last clearing of QFP drops statistics : never 
        p1 = re.compile(r'^Last clearing of QFP drops statistics : (?P<last_clearing_of_qfp_drops_statistics>.+)$')
        # Connection: 1 - 1
        p2 = re.compile(r'^Connection: +(?P<connection>\d+ - \d+)$')
        # Current State: UP
        p3 = re.compile(r'^\s*Current State: +(?P<current_state>.+)$')
        # Segment 1: E1 0/3/0 00
        p4 = re.compile(r'^\s*Segment +(?P<segment>\d+):')
        # TDM timeslots in use: 1-24 (24 total)
        p5 = re.compile(r'^\s*TDM timeslots in use: +(?P<tdm_timeslots_in_use>\d{1,2}-\d{1,2})(?: +\((?P<total>\d+)\s+total\))?$')
        # Internal Switching Elements: VIC TDM Switch
        p6 = re.compile(r'^Internal Switching Elements: +(?P<internal_switching_elements>.+)$')


        for line in out.splitlines():
            line = line.strip()

            # Last clearing of QFP drops statistics : never
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed['last_clearing_of_qfp_drops_statistics'] = group['last_clearing_of_qfp_drops_statistics']
                continue

            # Connection: 1 - 1
            m = p2.match(line)
            if m:
                connection = m.group('connection')
                connection_dict = parsed.setdefault('connections', {}).setdefault(connection, {
                    'current_state': '',
                    'segment': {},
                    'internal_switching_elements': ''
                })
                continue

            # Current State: UP
            m = p3.match(line)
            if m and connection_dict is not None:
                group = m.groupdict()
                connection_dict['current_state'] = group['current_state']
                continue

            # Segment 1: E1 0/3/0 00
            m = p4.match(line)
            if m and connection_dict is not None:
                segment = m.group('segment')
                segment_dict = connection_dict['segment'].setdefault(segment, {
                    'tdm_timeslots_in_use': '',
                })
                continue

            # TDM timeslots in use: 1-24 (24 total)
            m = p5.match(line)
            if m and segment_dict is not None:
                group = m.groupdict()
                segment_dict['tdm_timeslots_in_use'] = group['tdm_timeslots_in_use']
                if group['total'] is not None:
                    segment_dict['total'] = int(group['total'])
                continue

            # Internal Switching Elements: VIC TDM Switch
            m = p6.match(line)
            if m and connection_dict is not None:
                group = m.groupdict()
                connection_dict['internal_switching_elements'] = group['internal_switching_elements']

        return parsed


class ShowConnectionNameSchema(MetaParser):
    '''Schema for show connection name {name}'''
    schema = {
        'connection': str,
        Optional('description'): str,
        'current_state': str,
        'segments': {
            int: {
                'interface': str,
                'state': str,
            }
        }
    }


class ShowConnectionName(ShowConnectionNameSchema):
    '''Parser for show connection name {name}'''
    cli_command = 'show connection name {name}'

    def cli(self, name='', output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(name=name))
        else:
            out = output

        # Initialize the return dictionary
        parsed = {}

        # Connection: 2 - p2p
        p1 = re.compile(r'^Connection:\s+(?P<connection>.+)$')
        # Description: none
        p2 = re.compile(r'^\s*Description:\s+(?P<description>.+)$')
        # Current State: UP
        p3 = re.compile(r'^\s*Current State:\s+(?P<current_state>\S+)$')
        # Segment 1: GigabitEthernet2 up
        p4 = re.compile(r'^\s*Segment\s+(?P<segment>\d+):\s+(?P<interface>\S+)\s+(?P<state>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Connection: 2 - p2p
            m = p1.match(line)
            if m:
                parsed['connection'] = m.group('connection')
                continue

            # Description: none
            m = p2.match(line)
            if m:
                parsed['description'] = m.group('description')
                continue

            # Current State: UP
            m = p3.match(line)
            if m:
                parsed['current_state'] = m.group('current_state')
                continue

            # Segment 1: GigabitEthernet2 up
            m = p4.match(line)
            if m:
                group = m.groupdict()
                segment_num = int(group['segment'])
                segments_dict = parsed.setdefault('segments', {})
                segments_dict[segment_num] = {
                    'interface': group['interface'],
                    'state': group['state']
                }
                continue

        return parsed