''' show_platform.py

IOSXE C9400 parsers for the following show commands:

    * 'show environment'
    * 'show environment | include {include}'
    * 'show environment all'
    * 'show environment all | include {include}'
'''

# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

log = logging.getLogger(__name__)


class ShowEnvironmentSchema(MetaParser):
    """Schema for show environment
                  show environment | include {include} """

    schema = {
        Optional('critical_alarms'): int,
        Optional('major_alarms'): int,
        Optional('minor_alarms'): int,
        'slot': {
            Any(): {
                'sensor': {
                    Any(): {
                        'state': str,
                        'reading': str,
                        Optional('threshold'): {
                            'minor': int,
                            'major': int,
                            'critical': int,
                            'shutdown': int,
                            'unit': str,
                        }
                    },
                }
            },
        }
    }


class ShowEnvironment(ShowEnvironmentSchema):
    """Parser for show environment
                  show environment | include {include}"""

    cli_command = ['show environment', 'show environment | include {include}']

    def cli(self, include='', output=None):
        if not output:
            if include:
                cmd = self.cli_command[1].format(include=include)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Number of Critical alarms:  0
        p1 = re.compile(
            r'^Number +of +Critical +alarms: +(?P<critic_alarms>\d+)$')

        # Number of Major alarms:     0
        p2 = re.compile(r'^Number +of +Major +alarms: +(?P<maj_alarms>\d+)$')

        # Number of Minor alarms:     0
        p3 = re.compile(r'^Number +of +Minor +alarms: +(?P<min_alarms>\d+)$')

        # Slot        Sensor          Current State   Reading        Threshold(Minor,Major,Critical,Shutdown)
        # ----------  --------------  --------------- ------------   ---------------------------------------
        # R0          Temp: Coretemp  Normal          47   Celsius	(107,117,123,125)(Celsius)
        # R0          V1: VX1         Normal          871  mV     	na
        # R0          HotSwap: Volts  Normal          53   V DC   	na
        # R0          Temp:   outlet  Normal          39   Celsius	(63 ,73 ,103,105)(Celsius)
        # R0          Temp:    inlet  Normal          32   Celsius	(56 ,66 ,96 ,98 )(Celsius)
        p4 = re.compile(
            r'(?P<slot>\S+)\s+(?P<sensor_name>\S+(:\s+\S+)?)\s+(?P<state>\S+)\s+(?P<reading>\d+\s+\S+(\s+(AC|DC))?)\s+(\((?P<minor>\d+\s*),(?P<major>\d+\s*),(?P<critical>\d+\s*),(?P<shutdown>\d+\s*)\)\((?P<unit>\S+)\))?'
        )

        for line in output.splitlines():
            line = line.strip()

            # Number of Critical alarms:  0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['critical_alarms'] = int(group['critic_alarms'])
                continue

            # Number of Major alarms:     0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['major_alarms'] = int(group['maj_alarms'])
                continue

            # Number of Minor alarms:     0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['minor_alarms'] = int(group['min_alarms'])
                continue

            # Slot        Sensor          Current State   Reading        Threshold(Minor,Major,Critical,Shutdown)
            # ----------  --------------  --------------- ------------   ---------------------------------------
            # R0          Temp: Coretemp  Normal          47   Celsius	(107,117,123,125)(Celsius)
            # R0          V1: VX1         Normal          871  mV     	na
            # R0          HotSwap: Volts  Normal          53   V DC   	na
            # R0          Temp:   outlet  Normal          39   Celsius	(63 ,73 ,103,105)(Celsius)
            # R0          Temp:    inlet  Normal          32   Celsius	(56 ,66 ,96 ,98 )(Celsius)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                sensor_name = group.pop('sensor_name')
                slot = group.pop('slot')
                fin_dict = ret_dict.setdefault('slot', {}).\
                                    setdefault(slot, {}).\
                                    setdefault('sensor',{}).\
                                    setdefault(sensor_name, {})

                fin_dict['state'] = group['state']
                fin_dict['reading'] = group['reading']
                if group['minor']:
                    fin_dict.setdefault('threshold', {})
                    for key in [
                            'minor', 'major', 'critical', 'shutdown', 'unit'
                    ]:
                        fin_dict['threshold'][key] = int(
                            group[key]) if key != 'unit' else group[key]
                continue

        return ret_dict


class ShowEnvironmentAllSchema(MetaParser):
    """Schema for show environment all
                  show environment all | include {include} """

    schema = {
        Optional('critical_alarms'): int,
        Optional('major_alarms'): int,
        Optional('minor_alarms'): int,
        'sensor_list': {
            Any(): {
                'slot': {
                    Any(): {
                        'sensor': {
                            Any(): {
                                'state': str,
                                'reading': str,
                                Optional('threshold'): {
                                    'minor': int,
                                    'major': int,
                                    'critical': int,
                                    'shutdown': int,
                                    'unit': str,
                                }
                            }
                        }
                    }
                }
            }
        },
        'power_supply': {
            'slot': {
                Any(): {
                    'model_no': str,
                    'type': str,
                    'capacity': str,
                    'status': str,
                    'fan_1_state': str,
                    'fan_2_state': str,
                }
            },
            'current_configuration_mode': str,
            'current_operating_state': str,
            'currently_active': int,
            'currently_available': int,
        },
        'fantray': {
            'status': str,
            'power_consumed_by_fantray_watts': int,
            'fantray_airflow_direction': str,
            'fantray_beacon_led': str,
            'fantray_status_led': str,
            'system': str,
        }
    }


class ShowEnvironmentAll(ShowEnvironmentAllSchema):
    """Parser for show environment all
                  show environment all | include {include}"""

    cli_command = [
        'show environment all', 'show environment all | include {include}'
    ]

    def cli(self, include='', output=None):
        if not output:
            if include:
                cmd = self.cli_command[1].format(include=include)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Number of Critical alarms:  0
        p1 = re.compile(
            r'^Number +of +Critical +alarms: +(?P<critic_alarms>\d+)$')

        # Number of Major alarms:     0
        p2 = re.compile(r'^Number +of +Major +alarms: +(?P<maj_alarms>\d+)$')

        # Number of Minor alarms:     0
        p3 = re.compile(r'^Number +of +Minor +alarms: +(?P<min_alarms>\d+)$')

        # Sensor List:  Environmental Monitoring
        p4 = re.compile(r'Sensor\s+List:\s+(?P<sensor_list>.+)')

        #  Sensor           Location          State          Reading           Threshold(Minor,Major,Critical,Shutdown)
        #  Temp: Coretemp   R0                Normal            48 Celsius          	(107,117,123,125)(Celsius)
        #  Temp: UADP       R0                Normal            56 Celsius          	(107,117,123,125)(Celsius)
        #  V1: VX1          R0                Normal            869 mV               	na
        #  Temp:    inlet   R0                Normal            32 Celsius          	(56 ,66 ,96 ,98 )(Celsius)
        p5 = re.compile(
            r'(?P<sensor_name>\S+(:\s+\S+)?)\s+(?P<slot>([A-Z][0-9]|\d/\d))\s+(?P<state>\S+)\s+(?P<reading>\d+\s+\S+(\s+(AC|DC))?)\s+(\((?P<minor>\d+\s*),(?P<major>\d+\s*),(?P<critical>\d+\s*),(?P<shutdown>\d+\s*)\)\((?P<unit>\S+)\))?'
        )

        # Power                                                       Fan States
        # Supply  Model No              Type  Capacity  Status        1     2
        # ------  --------------------  ----  --------  ------------  -----------
        # PS1     C9400-PWR-3200AC      ac    3200 W    active        good  good
        # PS2     C9400-PWR-3200AC      ac    n.a.      faulty        good  good
        p6 = re.compile(
            r'(?P<ps_slot>PS\S+)\s+(?P<model_no>\S+)\s+(?P<type>\S+)\s+(?P<capacity>\S+(\s+\S+)?)\s+(?P<status>\S+)\s+(?P<fan_1_state>\S+)\s+(?P<fan_2_state>\S+)$'
        )

        # PS Current Configuration Mode : Combined
        # PS Current Operating State    : Combined
        # Power supplies currently active    : 1
        # Power supplies currently available : 1
        p7 = re.compile(
            r'(PS|Power supplies)\s+(?P<ps_key>.+)\s+:\s+(?P<ps_value>\S+)')

        # Fantray : good
        # Power consumed by Fantray : 540 Watts
        # Fantray airflow direction : side-to-side
        # Fantray beacon LED: off
        # Fantray status LED: green
        # SYSTEM : GREEN
        p8 = re.compile(
            r'(?P<fantray_key>((.+)?Fantray(.+)?)|SYSTEM)(\s+)?:\s+(?P<fantray_value>(\S+)|(\d+\s+Watts))'
        )

        for line in output.splitlines():
            line = line.strip()

            # Number of Critical alarms:  0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['critical_alarms'] = int(group['critic_alarms'])
                continue

            # Number of Major alarms:     0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['major_alarms'] = int(group['maj_alarms'])
                continue

            # Number of Minor alarms:     0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['minor_alarms'] = int(group['min_alarms'])
                continue

            # Sensor List:  Environmental Monitoring
            m = p4.match(line)
            if m:
                group = m.groupdict()
                sensor_dict = ret_dict.setdefault('sensor_list',
                                                  {}).setdefault(
                                                      group['sensor_list'], {})
                continue

            #  Sensor           Location          State          Reading           Threshold(Minor,Major,Critical,Shutdown)
            #  Temp: Coretemp   R0                Normal            48 Celsius          	(107,117,123,125)(Celsius)
            #  Temp: UADP       R0                Normal            56 Celsius          	(107,117,123,125)(Celsius)
            #  V1: VX1          R0                Normal            869 mV               	na
            #  Temp:    inlet   R0                Normal            32 Celsius          	(56 ,66 ,96 ,98 )(Celsius)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                sensor_name = group.pop('sensor_name')
                slot = group.pop('slot')
                fin_dict = sensor_dict.setdefault('slot', {}).setdefault(slot, {}).\
                    setdefault('sensor', {}).setdefault(sensor_name, {})

                fin_dict['state'] = group['state']
                fin_dict['reading'] = group['reading']
                if group['minor']:
                    fin_dict.setdefault('threshold', {})
                    for key in [
                            'minor', 'major', 'critical', 'shutdown', 'unit'
                    ]:
                        fin_dict['threshold'][key] = int(
                            group[key]) if key != 'unit' else group[key]
                continue

            # Power                                                       Fan States
            # Supply  Model No              Type  Capacity  Status        1     2
            # ------  --------------------  ----  --------  ------------  -----------
            # PS1     C9400-PWR-3200AC      ac    3200 W    active        good  good
            # PS2     C9400-PWR-3200AC      ac    n.a.      faulty        good  good
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ps_slot = group.pop('ps_slot')
                ps_dict = ret_dict.setdefault('power_supply', {})
                ps_slot_dict = ps_dict.setdefault('slot',
                                                  {}).setdefault(ps_slot, {})
                ps_slot_dict.update({k: v for k, v in group.items()})

            # PS Current Configuration Mode : Combined
            # PS Current Operating State    : Combined
            # Power supplies currently active    : 1
            # Power supplies currently available : 1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ps_key = group['ps_key'].strip().lower().replace(' ', '_')
                if 'active' in ps_key or 'available' in ps_key:
                    ps_value = int(group['ps_value'])
                else:
                    ps_value = group['ps_value']
                ps_dict.setdefault(ps_key, ps_value)

            # Fantray : good
            # Power consumed by Fantray : 540 Watts
            # Fantray airflow direction : side-to-side
            # Fantray beacon LED: off
            # Fantray status LED: green
            # SYSTEM : GREEN
            m = p8.match(line)
            if m:
                group = m.groupdict()
                fantray_key = group['fantray_key'].strip().lower().replace(
                    ' ', '_')
                if 'power_consumed' in fantray_key:
                    fantray_value = int(group['fantray_value'])
                    fantray_key += '_watts'
                else:
                    fantray_value = group['fantray_value']
                if 'fantray' == fantray_key:
                    ret_dict.setdefault('fantray',
                                        {}).setdefault('status', fantray_value)
                else:
                    ret_dict.setdefault('fantray',
                                        {}).setdefault(fantray_key,
                                                       fantray_value)

        return ret_dict