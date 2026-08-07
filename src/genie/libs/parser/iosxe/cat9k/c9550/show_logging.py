''' show_logging.py

IOSXE parsers for the following show commands:
    * show logging onboard 
    * show logging onboard switch {switch_num} rp {switch_mode} voltage detail
    * show logging onboard rp {switch_mode} voltage detail
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


class ShowLoggingOnboardRpActiveVoltageDetailSchema(MetaParser):
    '''Schema for:
        show logging onboard switch {switch_num} rp {switch_mode} voltage detail
        show logging onboard rp {switch_mode} voltage detail
    '''

    schema = {
        Optional('voltage_summary'): {
            Optional('number_of_sensors'): int,
            Optional('sensors'): {
                Any(): {
                    'sensor_id': int,
                    'normal_range_min': int,
                    'normal_range_max': int,
                    'maximum_sensor_value': int,
                },
            },
            Optional('sensor_value_duration'): {
                Any(): {
                    'durations': ListOf(str),
                },
            },
            Optional('no_historical_data'): str,
        },
        Optional('voltage_continuous'): {
            Optional('sensors'): {
                Any(): {
                    'sensor_id': int,
                },
            },
            Optional('time_stamp'): {
                Any(): {
                    'sensor_values': {
                        Any(): int,
                    },
                },
            },
        },
    }


class ShowLoggingOnboardRpActiveVoltageDetail(ShowLoggingOnboardRpActiveVoltageDetailSchema):
    """
    Parser for:
        show logging onboard switch {switch_num} rp {switch_mode} voltage detail
        show logging onboard rp {switch_mode} voltage detail
    """

    cli_command = [
        'show logging onboard switch {switch_num} rp {switch_mode} voltage detail',
        'show logging onboard rp {switch_mode} voltage detail',
    ]

    def cli(self, switch_num="", switch_mode="", output=None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[0].format(
                    switch_num=switch_num, switch_mode=switch_mode)
            else:
                cmd = self.cli_command[1].format(switch_mode=switch_mode)

            output = self.device.execute(cmd)

        ret_dict = {}
        section = None
        summary_sensor_section = False
        duration_section = False
        continuous_sensor_section = False
        continuous_sensor_order = []

        # VOLTAGE SUMMARY INFORMATION
        p1 = re.compile(r'^VOLTAGE SUMMARY INFORMATION$')

        # VOLTAGE CONTINUOUS INFORMATION
        p2 = re.compile(r'^VOLTAGE CONTINUOUS INFORMATION$')

        # Number of sensors          : 23
        p3 = re.compile(r'^Number +of +sensors\s+:\s+(?P<number_of_sensors>\d+)$')

        # Sensor                    ID         Normal Range          Maximum Sensor Value (Volts)
        p4 = re.compile(r'^Sensor\s+ID\s+Normal Range\s+Maximum Sensor Value(?: \(Volts\))?$')

        # CPU_P3P3V_S5              0          0 - 3                 3
        p5 = re.compile(
            r'^(?P<sensor>.+?)\s+(?P<sensor_id>\d+)\s+'
            r'(?P<normal_range_min>\d+)\s+-\s+'
            r'(?P<normal_range_max>\d+)\s+'
            r'(?P<maximum_sensor_value>\d+)$')

        # Sensor Value
        p6 = re.compile(r'^Sensor Value$')

        # Total sensor value duration
        p7 = re.compile(r'^Total sensor value duration$')

        # No historical data
        p8 = re.compile(r'^No historical data$')

        # 0   0s      810s    810s
        p9 = re.compile(r'^(?P<sensor_value>\d+)\s+(?P<durations>.+)$')

        # Sensor                    ID
        p10 = re.compile(r'^Sensor\s+ID$')

        # CPU_P3P3V_S5              0
        p11 = re.compile(r'^(?P<sensor>.+?)\s+(?P<sensor_id>\d+)$')

        #        Time Stamp   | Sensor Voltage 0V
        # MM/DD/YYYY HH:MM:SS | Sensor Value
        p12 = re.compile(r'^(Time Stamp|MM/DD/YYYY).*$')

        # 04/23/2026 13:28:01   3   1   2   1
        p13 = re.compile(
            r'^(?P<time_stamp>\d{2}\/\d{2}\/\d{4}\s+\d{2}:\d{2}:\d{2})'
            r'\s+(?P<sensor_values>[\d\s]+)$')

        for line in output.splitlines():
            line = line.strip()

            if not line or line.startswith('---'):
                continue

            # VOLTAGE SUMMARY INFORMATION
            m = p1.match(line)
            if m:
                section = 'summary'
                summary_sensor_section = False
                duration_section = False
                continuous_sensor_section = False
                ret_dict.setdefault('voltage_summary', {})
                continue

            # VOLTAGE CONTINUOUS INFORMATION
            m = p2.match(line)
            if m:
                section = 'continuous'
                summary_sensor_section = False
                duration_section = False
                continuous_sensor_section = False
                ret_dict.setdefault('voltage_continuous', {})
                continue

            # Number of sensors          : 23
            m = p3.match(line)
            if m and section == 'summary':
                group = m.groupdict()
                summary_dict = ret_dict.setdefault('voltage_summary', {})
                summary_dict['number_of_sensors'] = int(group['number_of_sensors'])
                continue

            # Sensor                    ID         Normal Range          Maximum Sensor Value (Volts)
            m = p4.match(line)
            if m and section == 'summary':
                summary_sensor_section = True
                duration_section = False
                continue

            # Sensor Value
            m = p6.match(line)
            if m and section == 'summary':
                summary_sensor_section = False
                continue

            # Total sensor value duration
            m = p7.match(line)
            if m and section == 'summary':
                duration_section = True
                continue

            # No historical data
            m = p8.match(line)
            if m and section == 'summary':
                summary_dict = ret_dict.setdefault('voltage_summary', {})
                summary_dict['no_historical_data'] = line
                duration_section = False
                continue

            # CPU_P3P3V_S5              0          0 - 3                 3
            m = p5.match(line)
            if m and summary_sensor_section:
                group = m.groupdict()
                sensor = group.pop('sensor')
                sensor_dict = ret_dict.setdefault('voltage_summary', {}).setdefault(
                    'sensors', {}).setdefault(sensor, {})
                sensor_dict['sensor_id'] = int(group['sensor_id'])
                sensor_dict['normal_range_min'] = int(group['normal_range_min'])
                sensor_dict['normal_range_max'] = int(group['normal_range_max'])
                sensor_dict['maximum_sensor_value'] = int(group['maximum_sensor_value'])
                continue

            # 0   0s      810s    810s
            m = p9.match(line)
            if m and duration_section:
                group = m.groupdict()
                summary_dict = ret_dict.setdefault('voltage_summary', {})
                duration_dict = summary_dict.setdefault('sensor_value_duration', {})
                duration_dict.setdefault(group['sensor_value'], {})['durations'] = (
                    group['durations'].split())
                continue

            # Sensor                    ID
            m = p10.match(line)
            if m and section == 'continuous':
                continuous_sensor_section = True
                continue

            #        Time Stamp   | Sensor Voltage 0V
            # MM/DD/YYYY HH:MM:SS | Sensor Value
            m = p12.match(line)
            if m and section == 'continuous':
                continuous_sensor_section = False
                continue

            # CPU_P3P3V_S5              0
            m = p11.match(line)
            if m and continuous_sensor_section:
                group = m.groupdict()
                sensor = group['sensor']
                continuous_sensor_order.append(sensor)
                sensor_dict = ret_dict.setdefault('voltage_continuous', {}).setdefault(
                    'sensors', {}).setdefault(sensor, {})
                sensor_dict['sensor_id'] = int(group['sensor_id'])
                continue

            # 04/23/2026 13:28:01   3   1   2   1
            m = p13.match(line)
            if m and section == 'continuous':
                group = m.groupdict()
                sensor_values = [
                    int(sensor_value)
                    for sensor_value in group['sensor_values'].split()
                ]
                time_dict = ret_dict.setdefault('voltage_continuous', {}).setdefault(
                    'time_stamp', {}).setdefault(group['time_stamp'], {})
                time_dict['sensor_values'] = {}

                for sensor, sensor_value in zip(
                        continuous_sensor_order, sensor_values):
                    time_dict['sensor_values'][sensor] = sensor_value
                continue

        return ret_dict
