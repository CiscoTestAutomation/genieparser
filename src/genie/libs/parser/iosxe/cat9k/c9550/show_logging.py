''' show_logging.py

IOSXE parsers for the following show commands:
    * show logging onboard 
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or, ListOf

class ShowLoggingOnboardRpActiveUptimeDetailSchema(MetaParser):
    '''Schema for:
        show logging onboard switch {switch_num} rp {switch_mode} uptime detail
        show logging onboard rp {rp} uptime detail
    '''

    schema = {
        'uptime_summary': {
            'first_customer_power_on': str,
            'number_of_reset': int,
            'number_of_slot_changes': int,
            'current_reset_reason': str,
            'current_reset_timestamp': str,
            'current_slot': int,
            'chassis_type': str,
            Any(): {
                'years': int,
                'weeks': int,
                'days': int,
                'hours': int,
                'minutes': int,
            },
        },
        'uptime_continuous': {
            'time_stamp': {
                Any(): {
                    'reset_reason': str,
                    'uptime_years': str,
                    'uptime_weeks': str,
                    'uptime_days': str,
                    'uptime_hours': str,
                    'uptime_minutes': str,
                },
            },
        },
    }

class ShowLoggingOnboardRpActiveUptimeDetail(ShowLoggingOnboardRpActiveUptimeDetailSchema):
    """
    Parser for:
        show logging onboard switch {switch_num} rp {switch_mode} uptime detail
        show logging onboard rp {switch_mode} uptime detail
    """

    cli_command = [
        'show logging onboard switch {switch_num} rp {switch_mode} uptime detail',
        'show logging onboard rp {switch_mode} uptime detail'
    ]

    def cli(self, switch_num="", switch_mode="", output=None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[0].format(switch_num=switch_num, switch_mode=switch_mode)
            else:
                cmd = self.cli_command[1].format(switch_mode=switch_mode)
            
            output = self.device.execute(cmd)

        ret_dict = {}

        # First customer power on : 06/24/2025 03:13:04
        p1 = re.compile(r'^First customer power on :?\s?(?P<first_customer_poweron>(\d+\/){2}\d+ \d+:\d+:\d+)$')

        # Total uptime            :  0  years  14 weeks  6  days  10 hours  45 minutes
        p2 = re.compile(r'^Total uptime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')

        # Total downtime          :  0  years  2  weeks  2  days  15 hours  36 minutes
        p3 = re.compile(r'^Total downtime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')

        # Number of resets        : 457
        p4 = re.compile(r'^Number of resets\s+:\s+(?P<numberof_reset>\d+)$')

        # Number of slot changes  : 1
        p5 = re.compile(r'^Number of slot changes\s+:\s+(?P<numberof_slot_changes>\d+)$')

        # Current reset reason    : redundancy force-switchover
        p6 = re.compile(r'^Current reset reason\s+:\s+(?P<current_reset_reason>.+)$')

        # Current reset timestamp : 10/21/2025 08:34:12
        p7 = re.compile(r'^Current reset timestamp\s+:\s+(?P<current_reset_timestamp>(\d+\/){2}\d+\s+\d+:\d+:\d+)$')

        # Current slot            : 1
        p8 = re.compile(r'^Current slot\s+:\s+(?P<current_slot>\d+)$')

        # Chassis type            : C9550-96L4D
        p9 = re.compile(r'^Chassis type\s+:\s+(?P<chassis_type>.+)$')

        # Current uptime          :  0  years  0  weeks  1  days  21 hours  0  minutes
        p10 = re.compile(r'^Current uptime\s+:\s+(?P<years>\d+)\s+\w+\s+(?P<weeks>\d+)\s+\w+\s+(?P<days>\d+)\s+\w+\s+(?P<hours>\d+)\s+\w+\s+(?P<minutes>\d+)\s+\w+$')

        # 10/21/2025 08:34:12   redundancy force-switchover
        p11 = re.compile(r'^(?P<time_stamp>(\d+\/){2}\d+\s+\d+:\d+:\d+)\s+(?P<reset_reason>.+)$')

        # Match uptime values line - handles the separate line with uptime values
        #  0     0     0     1     0
        p12 = re.compile(r'^\s*(?P<uptime_years>\d+)\s+(?P<uptime_weeks>\d+)\s+(?P<uptime_days>\d+)\s+(?P<uptime_hours>\d+)\s+(?P<uptime_minutes>\d+)\s*$')

        current_timestamp = None

        for line in output.splitlines():
            line = line.strip()

            root_dict = ret_dict.setdefault('uptime_summary', {})

            # First customer power on : 06/24/2025 03:13:04
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict['first_customer_power_on'] = group['first_customer_poweron']
                continue

            # Total uptime            :  0  years  14 weeks  6  days  10 hours  45 minutes
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict1 = root_dict.setdefault('total_uptime', {})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue

            # Total downtime          :  0  years  2  weeks  2  days  15 hours  36 minutes
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict1 = root_dict.setdefault('total_downtime', {})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue

            # Number of resets        : 457
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict['number_of_reset'] = int(group['numberof_reset'])
                continue

            # Number of slot changes  : 1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict['number_of_slot_changes'] = int(group['numberof_slot_changes'])
                continue

            # Current reset reason    : redundancy force-switchover
            m = p6.match(line)
            if m:
                group = m.groupdict()
                root_dict['current_reset_reason'] = group['current_reset_reason']
                continue

            # Current reset timestamp : 10/21/2025 08:34:12
            m = p7.match(line)
            if m:
                group = m.groupdict()
                root_dict['current_reset_timestamp'] = group['current_reset_timestamp']
                continue

            # Current slot            : 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                root_dict['current_slot'] = int(group['current_slot'])
                continue

            # Chassis type            : C9550-96L4D
            m = p9.match(line)
            if m:
                group = m.groupdict()
                root_dict['chassis_type'] = group['chassis_type']
                continue

            # Current uptime          :  0  years  0  weeks  1  days  21 hours  0  minutes
            m = p10.match(line)
            if m:
                group = m.groupdict()
                root_dict1 = root_dict.setdefault('current_uptime', {})
                root_dict1['years'] = int(group['years'])
                root_dict1['weeks'] = int(group['weeks'])
                root_dict1['days'] = int(group['days'])
                root_dict1['hours'] = int(group['hours'])
                root_dict1['minutes'] = int(group['minutes'])
                continue

            # 10/21/2025 08:34:12   redundancy force-switchover
            m = p11.match(line)
            if m:
                group = m.groupdict()
                current_timestamp = group['time_stamp']
                continuous_dict = ret_dict.setdefault('uptime_continuous', {})
                time_dict = continuous_dict.setdefault('time_stamp', {}).setdefault(current_timestamp, {})
                time_dict['reset_reason'] = group['reset_reason'].strip()
                continue

            # Match uptime values line
            #  0     0     0     1     0
            m = p12.match(line)
            if m and current_timestamp:
                group = m.groupdict()
                continuous_dict = ret_dict.setdefault('uptime_continuous', {})
                time_dict = continuous_dict.setdefault('time_stamp', {}).setdefault(current_timestamp, {})
                time_dict['uptime_years'] = group['uptime_years']
                time_dict['uptime_weeks'] = group['uptime_weeks']
                time_dict['uptime_days'] = group['uptime_days']
                time_dict['uptime_hours'] = group['uptime_hours']
                time_dict['uptime_minutes'] = group['uptime_minutes']
                current_timestamp = None  # Reset after processing uptime values
                continue

        return ret_dict