''' show_drops.py
IOSXE parsers for the following show commands:

    * show drops history qfp
    * show drops history qfp clear

'''

# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
# genie.parsergen
try:
    import genie.parsergen
except (ImportError, OSError):
    pass


class ShowDropsHistoryQfpSchema(MetaParser):
    """Schema for show drops history qfp"""

    schema = {
        'stats_cleared': bool, 
        Optional('last_clear_time'): {
            'year': int,
            'month': str,
            'day': int,
            'hour': int,
            'minute': int,
            'second': int
        },    
        Optional('last_clear_lapsed_time'): {
            Optional('weeks'): int,
            Optional('days'): int,
            Optional('hours'): int,
            Optional('minutes'): int,
            'seconds': int
        },    
        'drops_seen': bool, 
        Optional('drop_history'): {
            Any(): {
                '1m': {
                    'packets': int,
                },
                '5m': {
                    'packets': int,
                },
                '30m': {
                    'packets': int,
                },
                'all': {
                    'packets': int,
                }
            },    
        }     
    }

class ShowDropsHistoryQfp(ShowDropsHistoryQfpSchema):
    """
    Parser for
        show drops history qfp
    """

    cli_command = 'show drops history qfp'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Last clearing of QFP drops statistics : never
        p1_1 = re.compile(r'^Last clearing of QFP drops statistics : never$')

        # Last clearing of QFP drops statistics : Fri Jun  9 04:04:39 2023
        p1_2 = re.compile(r'^Last clearing of QFP drops statistics : \w+\s+(?P<month>\w+)'
                          r'\s+(?P<day>\d+)\s+(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)'
                          r'\s+(?P<year>\d+)$')

        # (3w 2d 5h 10m 42s ago)
        # (2d 5h 10m 42s ago)
        # (5h 10m 42s ago)
        # (10m 42s ago)
        # (42s ago)
        p1_3 = re.compile(r'^\(((?P<weeks>\d+)w\s+)?((?P<days>\d+)d\s+)?((?P<hours>\d+)h\s+)?'
                          r'((?P<minutes>\d+)m\s+)?(?P<seconds>\d+)s\s+ago\)$')

        # The Global drop stats were all zero
        p2_1 = re.compile(r'^The Global drop stats were all zero$')

        # Ipv4NoAdj     0      199935      299897    299897
        p2_2 = re.compile(r'^(?P<reason>\w+)\s+(?P<packets_1m>\d+)\s+(?P<packets_5m>\d+)'
                          r'\s+(?P<packets_30m>\d+)\s+(?P<packets_all>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Last clearing of QFP drops statistics : never
            m = p1_1.match(line)
            if m:
                ret_dict['stats_cleared'] = False
                continue

            # Last clearing of QFP drops statistics : Fri Jun  9 04:04:39 2023
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                last_clear_time = {
                    'year'   : int(group['year']),
                    'month'  : group['month'],
                    'day'    : int(group['day']),
                    'hour'   : int(group['hour']),
                    'minute' : int(group['minute']),
                    'second' : int(group['second'])
                }
                ret_dict.update({
                    'stats_cleared'   : True,
                    'last_clear_time' : last_clear_time
                })
                continue

            # (3w 2d 5h 10m 42s ago)
            # (2d 5h 10m 42s ago)
            # (5h 10m 42s ago)
            # (10m 42s ago)
            # (42s ago)
            m = p1_3.match(line)
            if m:
                group = m.groupdict()
                lapsed_time = {}
                if group['weeks'] is not None:
                    lapsed_time['weeks'] = int(group['weeks'])
                if group['days'] is not None:
                    lapsed_time['days'] = int(group['days'])
                if group['hours'] is not None:
                    lapsed_time['hours'] = int(group['hours'])
                if group['minutes'] is not None:
                    lapsed_time['minutes'] = int(group['minutes'])
                lapsed_time['seconds'] = int(group['seconds'])
                ret_dict['last_clear_lapsed_time'] = lapsed_time
                continue

            # The Global drop stats were all zero
            m = p2_1.match(line)
            if m:
                ret_dict['drops_seen'] = False
                continue

            # Ipv4NoAdj     0      199935      299897    299897
            m = p2_2.match(line)
            if m: 
                group = m.groupdict()
                ret_dict['drops_seen'] = True
                reason = group['reason']
                reason_dict = {
                    '1m'  : {'packets': int(group['packets_1m'])},
                    '5m'  : {'packets': int(group['packets_5m'])},
                    '30m' : {'packets': int(group['packets_30m'])},
                    'all' : {'packets': int(group['packets_all'])}
                }
                drop_history_dict = ret_dict.setdefault('drop_history', {})
                drop_history_dict[reason] = reason_dict
                continue

        return ret_dict


class ShowDropsHistoryQfpClear(ShowDropsHistoryQfpSchema):
    """
    Parser for
        show drops history qfp clear
    """

    cli_command = 'show drops history qfp clear'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Last clearing of QFP drops statistics : never
        p1_1 = re.compile(r'^Last clearing of QFP drops statistics : never$')

        # Last clearing of QFP drops statistics : Fri Jun  9 04:04:39 2023
        p1_2 = re.compile(r'^Last clearing of QFP drops statistics : \w+\s+(?P<month>\w+)'
                          r'\s+(?P<day>\d+)\s+(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+)'
                          r'\s+(?P<year>\d+)$')

        # (3w 2d 5h 10m 42s ago)
        # (2d 5h 10m 42s ago)
        # (5h 10m 42s ago)
        # (10m 42s ago)
        # (42s ago)
        p1_3 = re.compile(r'^\(((?P<weeks>\d+)w\s+)?((?P<days>\d+)d\s+)?((?P<hours>\d+)h\s+)?'
                          r'((?P<minutes>\d+)m\s+)?(?P<seconds>\d+)s\s+ago\)$')

        # The Global drop stats were all zero
        p2_1 = re.compile(r'^The Global drop stats were all zero$')

        # Ipv4NoAdj     0      199935      299897    299897
        p2_2 = re.compile(r'^(?P<reason>\w+)\s+(?P<packets_1m>\d+)\s+(?P<packets_5m>\d+)'
                          r'\s+(?P<packets_30m>\d+)\s+(?P<packets_all>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Last clearing of QFP drops statistics : never
            m = p1_1.match(line)
            if m:
                ret_dict['stats_cleared'] = False
                continue

            # Last clearing of QFP drops statistics : Fri Jun  9 04:04:39 2023
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                last_clear_time = {
                    'year'   : int(group['year']),
                    'month'  : group['month'],
                    'day'    : int(group['day']),
                    'hour'   : int(group['hour']),
                    'minute' : int(group['minute']),
                    'second' : int(group['second'])
                }
                ret_dict.update({
                    'stats_cleared'   : True,
                    'last_clear_time' : last_clear_time
                })
                continue

            # (3w 2d 5h 10m 42s ago)
            # (2d 5h 10m 42s ago)
            # (5h 10m 42s ago)
            # (10m 42s ago)
            # (42s ago)
            m = p1_3.match(line)
            if m:
                group = m.groupdict()
                lapsed_time = {}
                if group['weeks'] is not None:
                    lapsed_time['weeks'] = int(group['weeks'])
                if group['days'] is not None:
                    lapsed_time['days'] = int(group['days'])
                if group['hours'] is not None:
                    lapsed_time['hours'] = int(group['hours'])
                if group['minutes'] is not None:
                    lapsed_time['minutes'] = int(group['minutes'])
                lapsed_time['seconds'] = int(group['seconds'])
                ret_dict['last_clear_lapsed_time'] = lapsed_time
                continue

            # The Global drop stats were all zero
            m = p2_1.match(line)
            if m:
                ret_dict['drops_seen'] = False
                continue

            # Ipv4NoAdj     0      199935      299897    299897
            m = p2_2.match(line)
            if m: 
                group = m.groupdict()
                ret_dict['drops_seen'] = True
                reason = group['reason']
                reason_dict = {
                    '1m'  : {'packets': int(group['packets_1m'])},
                    '5m'  : {'packets': int(group['packets_5m'])},
                    '30m' : {'packets': int(group['packets_30m'])},
                    'all' : {'packets': int(group['packets_all'])}
                }
                drop_history_dict = ret_dict.setdefault('drop_history', {})
                drop_history_dict[reason] = reason_dict
                continue

        return ret_dict

