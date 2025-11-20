'''show_logging.py

IOSXE parsers for the following show commands:

    * show logging onboard slot {slot} status
    * show logging onboard {switch} {switch_num} slot {slot_num} voltage
    * show logging onboard {switch} {switch_num} slot {slot_num} temperature
    * show logging onboard rp {slot} uptime detail
'''

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or


class ShowLoggingOnboardSlotStatusSchema(MetaParser):
    """Schema for show logging onboard slot <slot> status"""

    schema = {
        Any(): {
            'path': str,
            'cli_enable_status': str,
        },
    }

class ShowLoggingOnboardSlotStatus(ShowLoggingOnboardSlotStatusSchema):
    """Parser for show logging onboard slot <slot> status"""

    cli_command = 'show logging onboard slot {slot} status'

    def cli(self, slot = "", output=None):
        if output is None:
            #Build the command
            cmd = self.cli_command.format(slot = slot)
            output = self.device.execute(cmd)

        ret_dict = {}
        current_app = None

        # Application Uptime:
        p1 = re.compile(r'^(?P<application>(Application.*?):)$')

        # Path: /obfl_cc/1/
        p2 = re.compile(r'^\s*Path:?\s?(?P<path>.*)$')

        # Cli enable status: enabled
        p3 = re.compile(r'^\s*Cli enable status:?\s?(?P<cli_enable_status>.*)$')

        for line in output.splitlines():
            # remove any trailing or leading spaces
            line = line.strip()

            # Application Uptime:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_app = group['application']
                ret_dict.setdefault(current_app, {})
                continue

            # Path: /obfl_cc/1/
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[current_app]['path'] = group['path']
                continue

            # Cli enable status: enabled
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict[current_app]['cli_enable_status'] = group['cli_enable_status']
                continue

        return ret_dict

class ShowLoggingOnboardRpUptimeDetailSchema(MetaParser):
    """Schema for show logging onboard rp {slot} uptime detail"""

    schema = {
        "uptime_summary": {
            "first_customer_power_on": str,
            "total_uptime": {
                "years": int,
                "weeks": int, 
                "days": int,
                "hours": int,
                "minutes": int
            },
            "total_downtime": {
                "years": int,
                "weeks": int,
                "days": int, 
                "hours": int,
                "minutes": int
            },
            "number_of_resets": int,
            "number_of_slot_changes": int,
            "current_reset_reason": str,
            "current_reset_timestamp": str,
            "current_slot": int,
            "chassis_type": str,
            "current_uptime": {
                "years": int,
                "weeks": int,
                "days": int,
                "hours": int, 
                "minutes": int
            }
        },
        "uptime_continuous": {
            Any(): {
                "timestamp": str,
                "reset_reason": str,
                "uptime": {
                    "years": int,
                    "weeks": int,
                    "days": int,
                    "hours": int,
                    "minutes": int
}}}    }

class ShowLoggingOnboardRpUptimeDetail(ShowLoggingOnboardRpUptimeDetailSchema):
    """Parser for show logging onboard rp {slot} uptime detail"""


    cli_command = 'show logging onboard rp {slot} uptime detail'

    def cli(self, slot = "", output=None):
        if output is None:
            cmd = self.cli_command.format(slot = slot)
            output = self.device.execute(cmd)

        ret_dict = {}

        # First customer power on : 01/23/2023 05:19:47
        p1 = re.compile(r'^First customer power on\s*:\s*(?P<timestamp>.+)$')
        
        # Total uptime            :  0  years  33 weeks  5  days  20 hours  30 minutes
        p2 = re.compile(r'^Total uptime\s*:\s*(?P<years>\d+)\s+years?\s+(?P<weeks>\d+)\s+weeks?\s+(?P<days>\d+)\s+days?\s+(?P<hours>\d+)\s+hours?\s+(?P<minutes>\d+)\s+minutes?$')
        
        # Total downtime          :  0  years  9  weeks  4  days  3  hours  21 minutes
        p3 = re.compile(r'^Total downtime\s*:\s*(?P<years>\d+)\s+years?\s+(?P<weeks>\d+)\s+weeks?\s+(?P<days>\d+)\s+days?\s+(?P<hours>\d+)\s+hours?\s+(?P<minutes>\d+)\s+minutes?$')
        
        # Number of resets        : 1451
        p4 = re.compile(r'^Number of resets\s*:\s*(?P<resets>\d+)$')
        
        # Number of slot changes  : 1
        p5 = re.compile(r'^Number of slot changes\s*:\s*(?P<slot_changes>\d+)$')
        
        # Current reset reason    : Image Install
        p6 = re.compile(r'^Current reset reason\s*:\s*(?P<reason>.+)$')
        
        # Current reset timestamp : 11/22/2023 01:08:54
        p7 = re.compile(r'^Current reset timestamp\s*:\s*(?P<timestamp>.+)$')
        
        # Current slot            : 5
        p8 = re.compile(r'^Current slot\s*:\s*(?P<slot>\d+)$')
        
        # Chassis type            : C9610R
        p9 = re.compile(r'^Chassis type\s*:\s*(?P<chassis>.+)$')
        
        # Current uptime          :  0  years  0  weeks  1  days  4  hours  2  minutes
        p10 = re.compile(r'^Current uptime\s*:\s*(?P<years>\d+)\s+years?\s+(?P<weeks>\d+)\s+weeks?\s+(?P<days>\d+)\s+days?\s+(?P<hours>\d+)\s+hours?\s+(?P<minutes>\d+)\s+minutes?$')
        
        # 11/20/2023 21:27:11   Reload Command
        p11 = re.compile(r'^(?P<timestamp>\d{2}/\d{2}/\d{4}\s+\d{2}:\d{2}:\d{2})\s+(?P<reason>.+?)\s*$')
        
        # 0     0     0     0     19
        p12 = re.compile(r'^\s*(?P<years>\d+)\s+(?P<weeks>\d+)\s+(?P<days>\d+)\s+(?P<hours>\d+)\s+(?P<minutes>\d+)\s*$')

        in_continuous_section = False
        current_entry = None
        entry_index = 1

        for line in output.splitlines():
            line = line.rstrip()
            if not line:
                continue
                
            stripped = line.strip()
            
            # Skip separator lines
            if stripped.startswith('---') or 'UPTIME SUMMARY' in stripped or 'UPTIME CONTINUOUS' in stripped:
                if 'CONTINUOUS' in stripped:
                    in_continuous_section = True
                continue
                
            # Skip header lines in continuous section
            if in_continuous_section and ('Time Stamp' in stripped or 'MM/DD/YYYY' in stripped or 
                                        'Uptime' in stripped or 'years weeks' in stripped):
                continue

            # Parse uptime summary section
            if not in_continuous_section:
                # First customer power on : 01/23/2023 05:19:47
                m = p1.match(stripped)
                if m:
                    summary = ret_dict.setdefault('uptime_summary', {})
                    summary['first_customer_power_on'] = m.group('timestamp').strip()
                    continue

                # Total uptime            :  0  years  33 weeks  5  days  20 hours  30 minutes
                m = p2.match(stripped)
                if m:
                    summary = ret_dict.setdefault('uptime_summary', {})
                    summary['total_uptime'] = {
                        'years': int(m.group('years')),
                        'weeks': int(m.group('weeks')),
                        'days': int(m.group('days')),
                        'hours': int(m.group('hours')),
                        'minutes': int(m.group('minutes'))
                    }
                    continue

                # Total downtime          :  0  years  9  weeks  4  days  3  hours  21 minutes
                m = p3.match(stripped)
                if m:
                    summary = ret_dict.setdefault('uptime_summary', {})
                    summary['total_downtime'] = {
                        'years': int(m.group('years')),
                        'weeks': int(m.group('weeks')),
                        'days': int(m.group('days')),
                        'hours': int(m.group('hours')),
                        'minutes': int(m.group('minutes'))
                    }
                    continue

                # Number of resets        : 1451
                m = p4.match(stripped)
                if m:
                    summary = ret_dict.setdefault('uptime_summary', {})
                    summary['number_of_resets'] = int(m.group('resets'))
                    continue

                # Number of slot changes  : 1
                m = p5.match(stripped)
                if m:
                    summary = ret_dict.setdefault('uptime_summary', {})
                    summary['number_of_slot_changes'] = int(m.group('slot_changes'))
                    continue

                # Current reset reason    : Image Install
                m = p6.match(stripped)
                if m:
                    summary = ret_dict.setdefault('uptime_summary', {})
                    summary['current_reset_reason'] = m.group('reason').strip()
                    continue

                # Current reset timestamp : 11/22/2023 01:08:54
                m = p7.match(stripped)
                if m:
                    summary = ret_dict.setdefault('uptime_summary', {})
                    summary['current_reset_timestamp'] = m.group('timestamp').strip()
                    continue

                # Current slot            : 5
                m = p8.match(stripped)
                if m:
                    summary = ret_dict.setdefault('uptime_summary', {})
                    summary['current_slot'] = int(m.group('slot'))
                    continue

                # Chassis type            : C9610R
                m = p9.match(stripped)
                if m:
                    summary = ret_dict.setdefault('uptime_summary', {})
                    summary['chassis_type'] = m.group('chassis').strip()
                    continue

                # Current uptime          :  0  years  0  weeks  1  days  4  hours  2  minutes
                m = p10.match(stripped)
                if m:
                    summary = ret_dict.setdefault('uptime_summary', {})
                    summary['current_uptime'] = {
                        'years': int(m.group('years')),
                        'weeks': int(m.group('weeks')),
                        'days': int(m.group('days')),
                        'hours': int(m.group('hours')),
                        'minutes': int(m.group('minutes'))
                    }
                    continue

            else:
                # 11/20/2023 21:27:11   Reload Command
                m = p11.match(stripped)
                if m:
                    continuous = ret_dict.setdefault('uptime_continuous', {})
                    current_entry = continuous.setdefault(str(entry_index), {})
                    current_entry['timestamp'] = m.group('timestamp').strip()
                    current_entry['reset_reason'] = m.group('reason').strip()
                    continue

                # 0     0     0     0     19
                m = p12.match(stripped)
                if m and current_entry:
                    current_entry['uptime'] = {
                        'years': int(m.group('years')),
                        'weeks': int(m.group('weeks')),
                        'days': int(m.group('days')),
                        'hours': int(m.group('hours')),
                        'minutes': int(m.group('minutes'))
                    }
                    entry_index += 1
                    current_entry = None
                    continue

        return ret_dict
class ShowLoggingOnboardSlotVoltageSchema(MetaParser):
    """Schema for show logging onboard {switch} {switch_num} slot {slot_num} voltage"""

    schema = {
        Optional('number_of_sensors'): int,
        Optional('sensors'): {
            Any(): {
                'id': int,
                'normal_range': str,
                'max_sensor_value': int,
            }
        },
        Optional('sensor_value_duration'): {
            Any(): {
                'durations': list,
            }
        },
        Optional('no_historical_data'): str,
    }

class ShowLoggingOnboardSlotVoltage(ShowLoggingOnboardSlotVoltageSchema):
    """Parser for show logging onboard {switch} {switch_num} slot {slot_num} voltage"""

    cli_command = [
        'show logging onboard switch {switch_num} slot {slot_num} voltage',
        'show logging onboard slot {slot_num} voltage'
    ]

    def cli(self, slot_num = "", switch_num = "", output=None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[0].format(switch_num=switch_num, slot_num=slot_num)
            else:
                cmd = self.cli_command[1].format(slot_num=slot_num)

            output = self.device.execute(cmd)

        ret_dict = {}
        sensors = {}
        sensor_value_duration = {}
        sensors_section = False
        duration_section = False
        
        # Number of sensors          : 6
        p0 = re.compile(r'^Number of sensors\s*:\s*(\d+)$')

        # Sensor                    ID         Normal Range          Maximum Sensor Value
        p1 = re.compile(r'^Sensor\s+ID\s+Normal Range\s+Maximum Sensor Value$')

        # P1V1_FPGA                 0          0 - 1                 1
        p2 = re.compile(r'^(\S+)\s+(\d+)\s+([\d\s\-\_]+)\s+(\d+)$')

        # Sensor Value
        p3 = re.compile(r'^Sensor Value$')

        # Sensor Value             Total duration at sensor value by each sensor
        p4 = re.compile(r'^Sensor Value\s+Total duration at sensor value by each sensor$')

        # 0   0s      810s    810s    810s    810s    810s
        p5 = re.compile(r'^(\d+)\s+(.+)$')

        # No historical data
        p6 = re.compile(r'^No historical data$')

        for line in output.splitlines():
            line = line.strip()
            
            # Number of sensors          : 6
            m = p0.match(line)
            if m:
                ret_dict['number_of_sensors'] = int(m.group(1))
                continue

            # Sensor                    ID         Normal Range          Maximum Sensor Value
            if p1.match(line):
                sensors_section = True
                continue

            # Sensor Value
            if sensors_section and p3.match(line):
                sensors_section = False
                continue

            # Sensor Value             Total duration at sensor value by each sensor
            if p4.match(line):
                duration_section = True
                continue

            # P1V1_FPGA                 0          0 - 1                 1
            if sensors_section:
                m = p2.match(line)
                if m:
                    name = m.group(1)
                    sensors[name] = {
                        'id': int(m.group(2)),
                        'normal_range': m.group(3).strip(),
                        'max_sensor_value': int(m.group(4)),
                    }
                continue

            # No historical data
            if p6.match(line):
                ret_dict['no_historical_data'] = 'No historical data'
                break

            # 0   0s      810s    810s    810s    810s    810s
            if duration_section:
                m = p5.match(line)
                if m:
                    value = m.group(1)
                    durations = m.group(2).split()
                    sensor_value_duration[value] = {'durations': durations}
                continue

        if sensors:
            ret_dict['sensors'] = sensors
        if sensor_value_duration:
            ret_dict['sensor_value_duration'] = sensor_value_duration

        return ret_dict
            
class ShowLoggingOnboardSlotTemperatureSchema(MetaParser):
    """Schema for show logging onboard {switch} {switch_num} slot {slot_num} temperature"""

    schema = {
        'number_of_sensors': int,
        'sensors': {
            Any(): {
                'id': int,
                'normal_range': str,
                'max_sensor_value': int,
            }
        },
        'sensor_value_duration': {
            Any(): {
                'durations': list,
            }
        },
    }

class ShowLoggingOnboardSlotTemperature(ShowLoggingOnboardSlotTemperatureSchema):
    """Parser for show logging onboard {switch} {switch_num} slot {slot_num} temperature"""

    cli_command = [
        'show logging onboard switch {switch_num} slot {slot_num} temperature',
        'show logging onboard slot {slot_num} temperature'
    ]

    def cli(self, slot_num = "", switch_num = "", output = None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[0].format(switch_num=switch_num, slot_num=slot_num)
            else:
                cmd = self.cli_command[1].format(slot_num=slot_num)

            output = self.device.execute(cmd)

        ret_dict = {}
        sensors = {}
        sensor_value_duration = {}
        sensors_section = False
        duration_section = False

        # Number of sensors          : 4
        p0 = re.compile(r'^Number of sensors\s*:\s*(\d+)$')

        # Sensor                    ID         Normal Range          Maximum Sensor Value
        p1 = re.compile(r'^Sensor\s+ID\s+Normal Range\s+Maximum Sensor Value$')

        # Temp: InltRight           0          0 - 65                27
        p2 = re.compile(r'^(\S.+?)\s+(\d+)\s+([\d\s\-\_]+)\s+(\d+)$')

        # Sensor Value
        p3 = re.compile(r'^Sensor Value$')

        # Sensor Value             Total duration at sensor value by each sensor
        p4 = re.compile(r'^Sensor Value\s+Total duration at sensor value by each sensor$')

        # 0                       22m     22m     22m     22m
        p5 = re.compile(r'^(\d+)\s+(.+)$')

        for line in output.splitlines():
            line = line.strip()

            # Number of sensors          : 4
            m = p0.match(line)
            if m:
                ret_dict['number_of_sensors'] = int(m.group(1))
                continue

            # Sensor                    ID         Normal Range          Maximum Sensor Value
            if p1.match(line):
                sensors_section = True
                continue

            # Sensor Value
            if sensors_section and p3.match(line):
                sensors_section = False
                continue

            # Sensor Value             Total duration at sensor value by each sensor
            if p4.match(line):
                duration_section = True
                continue

            # Temp: InltRight           0          0 - 65                27
            if sensors_section:
                m = p2.match(line)
                if m:
                    name = m.group(1)
                    sensors[name] = {
                        'id': int(m.group(2)),
                        'normal_range': m.group(3).strip(),
                        'max_sensor_value': int(m.group(4)),
                    }
                continue

            # 0                       22m     22m     22m     22m
            if duration_section:
                m = p5.match(line)
                if m:
                    value = m.group(1)
                    durations = m.group(2).split()
                    sensor_value_duration[value] = {'durations': durations}
                continue

        if sensors:
            ret_dict['sensors'] = sensors
        if sensor_value_duration:
            ret_dict['sensor_value_duration'] = sensor_value_duration

        return ret_dict
