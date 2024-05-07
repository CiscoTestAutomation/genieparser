''' show_platform.py

IOSXE C9400 parsers for the following show commands:

    * 'show environment'
    * 'show environment | include {include}'
    * 'show environment all'
    * 'show environment all | include {include}'
    * 'show boot'
    * 'Show module'
    * 'show platform hardware chassis fantray detail'
    * 'show platform hardware chassis fantray detail switch {mode}'
'''

# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or

from genie.libs.parser.utils.common import Common

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


class ShowBootSchema(MetaParser):
    """Schema for show boot"""

    schema = {
        'boot_variable': str,
        'manual_boot': bool,
        'baud_variable': str,
        'enable_break': bool,
        'boot_mode': str,
        'ipxe_timeout': str,
        'config_file': str,
        'standby_boot_variable': str,
        'standby_manual_boot': bool,
        'standby_baud_variable': str,
        'standby_enable_break': bool,
        'standby_boot_mode': str,
        'standby_ipxe_timeout': str,
        'standby_config_file': str,
    }


class ShowBoot(ShowBootSchema):
    """Parser for show boot"""

    cli_command = 'show boot'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # BOOT variable = flash:packages.conf;
        p1 = re.compile(r'(^BOOT\s*variable)\s*=\s*(?P<boot_variable>.*);$')
        # MANUAL_BOOT variable = no
        p2 = re.compile(r'(^MANUAL_BOOT\s*variable)\s*=\s*(?P<manual_boot>\w+)$')
        # BAUD variable = 9600
        p3 = re.compile(r'(^BAUD\s*variable)\s*=\s*(?P<baud_variable>\w+)$')
        # ENABLE_BREAK variable = yes
        p4 = re.compile(r'(^ENABLE_BREAK\s*variable)\s*=?\s*(?P<enable_break>.*)$')
        # BOOTMODE variable = yes
        p5 = re.compile(r'(^BOOTMODE\s*variable)\s*=?\s*(?P<boot_mode>.*)$')
        # IPXE_TIMEOUT variable = 0
        p6 = re.compile(r'(^IPXE_TIMEOUT\s*variable)\s*=?\s*(?P<ipxe_timeout>.*)$')
        # CONFIG_FILE variable = 0
        p7 = re.compile(r'(^CONFIG_FILE\s*variable)\s*=\s*(?P<config_file>.*)$')

        # Standby BOOT variable = flash:packages.conf;
        p8 = re.compile(r'(^Standby\s*BOOT\s*variable)\s*=\s*(?P<standby_boot_variable>.*);$')
        # Standby MANUAL_BOOT variable = no
        p9 = re.compile(r'(^Standby\s*MANUAL_BOOT\s*variable)\s*=\s*(?P<standby_manual_boot>\w+)$')
        # Standby BAUD variable = 9600
        p10 = re.compile(r'(^Standby\s*BAUD\s*variable)\s*=\s*(?P<standby_baud_variable>\w+)$')
        # Standby ENABLE_BREAK variable = yes
        p11 = re.compile(r'(^Standby\s*ENABLE_BREAK\s*variable)\s*=?\s*(?P<standby_enable_break>.*)$')
        # Standby BOOTMODE variable = yes
        p12 = re.compile(r'(^Standby\s*BOOTMODE\s*variable)\s*=?\s*(?P<standby_boot_mode>.*)$')
        # Standby IPXE_TIMEOUT variable = 0
        p13 = re.compile(r'(^Standby\s*IPXE_TIMEOUT\s*variable)\s*=?\s*(?P<standby_ipxe_timeout>.*)$')
        # Standby CONFIG_FILE variable = 0
        p14 = re.compile(r'(^Standby\s*CONFIG_FILE\s*variable)\s*=\s*(?P<standby_config_file>.*)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            mo = p1.match(line)
            if mo:
                ret_dict.update(mo.groupdict())

            mo = p2.match(line)
            if mo:
                group = mo.groupdict()
                manual_boot = group['manual_boot'] == 'yes'
                ret_dict.update({'manual_boot': manual_boot})

            mo = p3.match(line)
            if mo:
                group = mo.groupdict()
                ret_dict.update({'baud_variable': group['baud_variable']})

            mo = p4.match(line)
            if mo:
                group = mo.groupdict()
                enable_break = group['enable_break'] == 'yes'
                ret_dict.update({'enable_break': enable_break})

            mo = p5.match(line)
            if mo:
                ret_dict.update(mo.groupdict())

            mo = p6.match(line)
            if mo:
                ret_dict.update(mo.groupdict())

            mo = p7.match(line)
            if mo:
                ret_dict.update(mo.groupdict())

            mo = p8.match(line)
            if mo:
                ret_dict.update(mo.groupdict())

            mo = p9.match(line)
            if mo:
                group = mo.groupdict()
                standby_manual_boot = group['standby_manual_boot'] == 'yes'
                ret_dict.update({'standby_manual_boot': standby_manual_boot})

            mo = p10.match(line)
            if mo:
                group = mo.groupdict()
                ret_dict.update({'standby_baud_variable': group['standby_baud_variable']})

            mo = p11.match(line)
            if mo:
                group = mo.groupdict()
                standby_enable_break = group['standby_enable_break'] == 'yes'
                ret_dict.update({'standby_enable_break': standby_enable_break})

            mo = p12.match(line)
            if mo:
                ret_dict.update(mo.groupdict())

            mo = p13.match(line)
            if mo:
                ret_dict.update(mo.groupdict())

            mo = p14.match(line)
            if mo:
                ret_dict.update(mo.groupdict())

        return ret_dict


class ShowModuleSchema(MetaParser):
    """Schema for show module"""
    schema = {
        Optional('switch'): {
            Any(): {
                'port': str,
                'model': str,
                'serial_number': str,
                'mac_address': str,
                'hw_ver': str,
                'sw_ver': str
            },
        },
        Optional('module'):{
            int: {
                'ports':int,
                'card_type':str,
                'model':str,
                'serial':str,
                'mac_address':str,
                'hw':str,
                'fw':str,
                'sw':str,
                'status':str,
                Optional('redundancy_role'):str,
                Optional('operating_redundancy_mode'):str,
                Optional('configured_redundancy_mode'):str,
                Optional('redundancy_status'):str,
            },
        },
        Optional('number_of_mac_address'):int,
        Optional('chassis_mac_address_lower_range'):str,
        Optional('chassis_mac_address_upper_range'):str,
    }


class ShowModule(ShowModuleSchema):
    """Parser for show module"""

    cli_command = 'show module'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<switch>\d+) *'
                        '(?P<port>\w+) +'
                        '(?P<model>[\w\-]+) +'
                        '(?P<serial_number>\w+) +'
                        '(?P<mac_address>[\w\.]+) +'
                        '(?P<hw_ver>\w+) +'
                        '(?P<sw_ver>[\w\.]+)$')
        
        # Chassis Type: C9500X-28C8D

        # Mod Ports Card Type                                   Model          Serial No.
        # ---+-----+--------------------------------------+--------------+--------------
        # 1   38   Cisco Catalyst 9500X-28C8D Switch           C9500X-28C8D     FDO25030SLN
        # 10  24   24-Port 10 Gigabit Ethernet (SFP+)          C9400-LC-24XS    JAE21500658        
    
        p2=re.compile(r'^(?P<mod>[\d]+)\s+(?P<ports>[\d]+)\s+(?P<card_type>.*)\s+(?P<model>\S+)\s+(?P<serial>\S+)$')
                
        # Mod MAC addresses                    Hw   Fw           Sw                 Status
        # ---+--------------------------------+----+------------+------------------+--------
        # 1   F87A.4125.1400 to F87A.4125.147D 0.2  17.7.0.41     BLD_POLARIS_DEV_LA ok
            
        p3=re.compile(r'^(?P<mod_1>\d+)+\s+(?P<mac_address>[\w\.]+) .*(?P<hw>\d+.?\d+?) +(?P<fw>\S+) +(?P<sw>\S+) +(?P<status>\S+)$')
        
        #Mod Redundancy Role     Operating Mode  Configured Mode  Redundancy Status
        #---+-------------------+---------------+---------------+------------------
        #3   Active              sso             sso              Active
        #4   Standby             sso             sso              Standby Hot        

        p4=re.compile(r'^(?P<mod_2>\d+)+ *(?P<redundancy_role>\S+) *(?P<operating_redundancy_mode>\S+) *(?P<configured_redundancy_mode>\S+) *(?P<redundancy_status>.*)$')
        
        #Chassis MAC address range: 512 addresses from f87a.4125.1400 to f87a.4125.15ff 
        p5=re.compile(r'^Chassis MAC address range: (?P<number_of_mac_address>\d+) addresses from (?P<chassis_mac_address_lower_range>.*) to (?P<chassis_mac_address_upper_range>.*)$')
        
        for line in output.splitlines():
            line = line.strip()

            # Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver.
            # ------  -----   ---------             -----------  --------------  -------       --------
            #  1       56     WS-C3850-48P-E        FOC1902X062  689c.e2ff.b9d9  V04           16.9.1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('switch')
                switch_dict = ret_dict.setdefault('switch', {}).setdefault(int(switch), {})
                switch_dict.update({k: v.lower() for k, v in group.items()})
                continue    
                
            # Chassis Type: C9500X-28C8D

            # Mod Ports Card Type                                   Model          Serial No.
            # ---+-----+--------------------------------------+--------------+--------------
            # 1   38   Cisco Catalyst 9500X-28C8D Switch           C9500X-28C8D     FDO25030SLN
            m = p2.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('mod')
                switch_dict = ret_dict.setdefault('module', {}).setdefault(int(switch), {})
                switch_dict.update({k: v.strip() for k, v in group.items()})
                switch_dict['ports']=int(group['ports'])
                continue
                
            # Mod MAC addresses                    Hw   Fw           Sw                 Status
            # ---+--------------------------------+----+------------+------------------+--------
            # 1   F87A.4125.1400 to F87A.4125.147D 0.2  17.7.0.41     BLD_POLARIS_DEV_LA ok
            
            m=p3.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('mod_1')
                switch_dict = ret_dict.setdefault('module', {}).setdefault(int(switch), {})
                switch_dict.update({k: v.strip() for k, v in group.items()})
                continue
                
            # Mod Redundancy Role     Operating Redundancy Mode Configured Redundancy Mode
            # ---+-------------------+-------------------------+---------------------------
            # 1   Active              non-redundant             Non-redundant
            m=p4.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('mod_2')
                switch_dict = ret_dict.setdefault('module', {}).setdefault(int(switch), {})
                switch_dict.update({k: v.lower().strip() for k, v in group.items()})
                continue
            
            #Chassis MAC address range: 512 addresses from f87a.4125.1400 to f87a.4125.15ff 
            m=p5.match(line)
            if m:
                group=m.groupdict()
                ret_dict.update({k: v.lower().strip() for k, v in group.items()})
                ret_dict['number_of_mac_address'] = int(group['number_of_mac_address'])
                continue
                
        return ret_dict


class ShowHardwareLedSchema(MetaParser):
    """
    Schema for show hardware led
    """
    schema = {
        'switch':str,
        'system':str,
        'line_card_supervisor': {
            Any():{
                'beacon': str,
                'status':str,
                Optional('port_led_status'):{
                    str: str
                    },
                Optional('group_led'):{
                    str: str
                    }
                }
            },
        'rj45_console':str,
        Optional('fantray_status'): str,
        Optional('fantray_beacon'): str,
        Optional('power_supply_beacon_status'):{
            int : str
        }
    }     

class ShowHardwareLed(ShowHardwareLedSchema):
    """ Parser for show hardware led"""

    cli_command = "show hardware led"
    
    def cli(self,output=None): 
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}

        # SWITCH: C9404R
        p1 = re.compile('^SWITCH:\s+(?P<switch>\S+)$')

        # SYSTEM: GREEN
        p2 = re.compile('^SYSTEM:\s+(?P<system>\w+)$')

        # Line Card : 1
        # SUPERVISOR: ACTIVE
        p3 = re.compile('^(Line Card :|SUPERVISOR:)\s+(?P<line_card_supervisor>\w+)$')

        # PORT STATUS: (48)
        p4 = re.compile('^PORT STATUS:\s+\((?P<port_nums_in_status>\d+)\)+\s+(?P<led_ports>((\S+:[\w-]+\s*))+)$')

        # BEACON:     OFF
        p5 = re.compile('^BEACON:\s+(?P<beacon>\w+)$')

        # STATUS: GREEN
        p6 = re.compile('^STATUS:\s+(?P<status>\w+)$')

        # GROUP LED: UPLINK-G1:GREEN UPLINK-G2:BLACK UPLINK-G3:BLACK UPLINK-G4:BLACK
        p7 = re.compile('^GROUP LED:\s+(?P<group_led>((\S+:\w+\s*))+)$')

        # RJ45 CONSOLE: GREEN
        p8 = re.compile('^RJ45 CONSOLE:\s+(?P<rj45_console>\w+)$')

        # FANTRAY STATUS: GREEN
        p9 = re.compile('^FANTRAY STATUS:\s+(?P<fantray_status>\w+)$')

        # FANTRAY BEACON: BLACK
        p10 = re.compile('^FANTRAY BEACON:\s+(?P<fantray_beacon>\w+)$')

        # POWER-SUPPLY 1 BEACON: OFF
        p11 = re.compile('^POWER-SUPPLY\s+(?P<power_supply_num>\d+)\s+BEACON:\s+(?P<power_supply_status>\w+)$')


        for line in output.splitlines():
            line = line.strip()
            
            # SWITCH: C9404R
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['switch'] = group["switch"]
                continue
            
            # SYSTEM: GREEN
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['system'] = group["system"]
                continue

            # Line Card : 1
            # SUPERVISOR: ACTIVE
            m = p3.match(line)
            if m:
                group = m.groupdict()
                slot_dict=ret_dict.setdefault('line_card_supervisor',{}).setdefault(group['line_card_supervisor'],{})       
                continue

            # BEACON:     OFF
            m = p5.match(line)
            if m:
                group = m.groupdict()
                slot_dict.update({'beacon': group['beacon']})      
                continue
            
            # STATUS: GREEN
            m = p6.match(line)
            if m:
                group = m.groupdict()
                slot_dict.update({'status': group['status']})      
                continue

            # PORT STATUS: (48)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                for port in group['led_ports'].split():
                    port = (port.split(':'))
                    port_led_dict = slot_dict.setdefault('port_led_status',{})
                    port_led_dict.update({Common.convert_intf_name(port[0]): port[1]})
                continue

            
            # GROUP LED: UPLINK-G1:GREEN UPLINK-G2:BLACK UPLINK-G3:BLACK UPLINK-G4:BLACK
            m = p7.match(line)
            if m:
                group = m.groupdict()
                for uplink in group['group_led'].split():
                    uplink = (uplink.split(':'))
                    group_led_dict = slot_dict.setdefault('group_led',{})
                    group_led_dict.update({(uplink[0]): uplink[1]})
                continue
            
            # RJ45 CONSOLE: GREEN
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'rj45_console': group['rj45_console']})      
                continue

            # FANTRAY STATUS: GREEN
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'fantray_status': group['fantray_status']})
                continue
                
            # FANTRAY BEACON: BLACK
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'fantray_beacon': group['fantray_beacon']})
                continue
            
            # POWER-SUPPLY 1 BEACON: OFF
            m = p11.match(line)
            if m:
                group = m.groupdict()
                power_supply_dict= ret_dict.setdefault('power_supply_beacon_status',{})
                power_supply_dict.setdefault(int(group['power_supply_num']),group['power_supply_status'])
                continue

        return ret_dict

class ShowPlatformHardwareChassisFantrayDetailSchema(MetaParser):
    """ Schema for show platform hardware chassis fantray detail"""

    schema = {
        'fantray_details': {
            int: {
                'fan': {
                    Any(): Or(str, int),
                },
                'throttle': str,
                'interrupt_source': str,
                'temp': Or(int, str),
                'press': Or(int, str)
            }
        },
        Optional('interrupt_source_register'): int,
        Optional('global_version'): int,
        Optional('beacon_led_status'): str,
        Optional('status_led'): str
    }

class ShowPlatformHardwareChassisFantrayDetail(ShowPlatformHardwareChassisFantrayDetailSchema):
    """ Parser for show platform hardware chassis fantray detail"""

    cli_command = 'show platform hardware chassis fantray detail'

    def cli(self, output=None):
        if output is None:
            # Execute command to get output
            output = self.device.execute(self.cli_command)

        # Initial return dictionary
        ret_dict = {}

        # Row  Fan1   | Fan2   | Fan3   | Fan4   | Throttle | Interrupt Source | Temp | Press
        p1 = re.compile(r'^\s*Row\s+(?P<header>.*)$')

        # 1    3450     3510     3480     3510     35%        0x0                28       102
        p2 = re.compile(r'^\s*(?P<row>\d+)\s+(?P<fan_data>.*)\s+(?P<throttle>\S+)\s+(?P<interrupt_source>\S+)\s+(?P<temp>\S+)\s+(?P<press>\S+)$')

        # Fantray global interrupt source register
        p3 = re.compile(r'^Fantray global interrupt source register = (?P<interrupt_source_register>\S+)$')

        # Fantray global version
        p4 = re.compile(r'^Fantray global version: (?P<global_version>\d+)$')

        # Fantray beacon LED status
        p5 = re.compile(r'^Fantray beacon LED status: (?P<beacon_led_status>\S+)$')

        # Fantray status LED
        p6 = re.compile(r'^Fantray status LED: (?P<status_led>\S+)$')

        headers = []  # Initialize headers list

        for line in output.splitlines():
            line = line.strip()

            # Row Fan1 | Fan2 | Fan3 | Fan4 | Throttle | Interrupt Source | Temp | Press
            m = p1.match(line)
            if m:
                # Extracting and cleaning up the headers
                headers = [header.strip() for header in m.group('header').split('|')]
                continue

            # 1 3450 3510 3480 3510 35% 0x0 28 102
            m = p2.match(line)
            if m:
                group = m.groupdict()
                row = int(group.pop('row'))
                fan_data = group.pop('fan_data').split()
                ret_dict.setdefault('fantray_details', {})[row] = {
                    'fan': {headers[i]: int(value) if value.isdigit() else value for i, value in enumerate(fan_data)},
                    'throttle': group['throttle'],
                    'interrupt_source': group['interrupt_source'],
                    'temp': int(group['temp']) if group['temp'].isdigit() else group['temp'],
                    'press': int(group['press']) if group['press'].isdigit() else group['press']
                }
                continue

            # Fantray global interrupt source register
            m = p3.match(line)
            if m:
                ret_dict['interrupt_source_register'] = int(m.group('interrupt_source_register'), 16)
                continue

            # Fantray global version
            m = p4.match(line)
            if m:
                ret_dict['global_version'] = int(m.group('global_version'))
                continue

            # Fantray beacon LED status
            m = p5.match(line)
            if m:
                ret_dict['beacon_led_status'] = m.group('beacon_led_status')
                continue

            # Fantray status LED
            m = p6.match(line)
            if m:
                ret_dict['status_led'] = m.group('status_led')
                continue

        return ret_dict

class ShowPlatformHardwareChassisFantrayDetailSwitchSchema(MetaParser):
    """ Schema for show platform hardware chassis fantray detail switch {mode}"""

    schema = {
        'fantray_details': {
            Any(): {
                'fan': {
                    Any(): str
                },
                'throttle': str,
                'interrupt_source': str,
                'temp': str,
                'press': str
            }
        },
        Optional('interrupt_source_register'): str,
        Optional('global_version'): str,
        Optional('beacon_led_status'): str,
        Optional('status_led'): str
    }


class ShowPlatformHardwareChassisFantrayDetailSwitch(ShowPlatformHardwareChassisFantrayDetailSwitchSchema):
    """ Parser for show platform hardware chassis fantray detail switch {mode}"""

    cli_command = 'show platform hardware chassis fantray detail switch {mode}'

    def cli(self, mode, output=None):
        if output is None:
            # Execute command to get output
            output = self.device.execute(self.cli_command.format(mode=mode))

        # Initial return dictionary
        ret_dict = {}

        # Row  Fan1   | Fan2   | Fan3   | Fan4   | Throttle | Interrupt Source | Temp | Press
        p1 = re.compile(r'^\s*Row\s+(?P<header>.*)$')

        # 1    3450     3510     3480     3510     35%        0x0                28       102
        p2 = re.compile(r'^\s*(?P<row>\d+)\s+(?P<fan_data>.*?)\s+(?P<throttle>\S+)\s+(?P<interrupt_source>\S+)\s+(?P<temp>\S+)\s+(?P<press>\S+)$')

        # Pattern for Fantray global interrupt source register
        p3 = re.compile(r'^Fantray global interrupt source register = (?P<interrupt_source_register>\S+)$')

        # Pattern for Fantray global version
        p4 = re.compile(r'^Fantray global version: (?P<global_version>\S+)$')

        # Pattern for Fantray beacon LED status
        p5 = re.compile(r'^Fantray beacon LED status: (?P<beacon_led_status>\S+)$')

        # Pattern for Fantray status LED
        p6 = re.compile(r'^Fantray status LED: (?P<status_led>\S+)$')

        headers = []  # Initialize headers list

        for line in output.splitlines():
            line = line.strip()

            # Extract headers
            m = p1.match(line)
            if m:
                # Extracting and cleaning up the headers
                headers = [header.strip() for header in m.group('header').split('|')]
                continue

            # Check for the row data
            m = p2.match(line)
            if m:
                group = m.groupdict()
                row = group.pop('row')
                fan_data = group.pop('fan_data').split()
                ret_dict.setdefault('fantray_details', {})[row] = {
                    'fan': {headers[i]: value for i, value in enumerate(fan_data)},
                    **group
                }
                continue

            # Fantray global interrupt source register
            m = p3.match(line)
            if m:
                ret_dict['interrupt_source_register'] = m.group('interrupt_source_register')
                continue

            # Fantray global version
            m = p4.match(line)
            if m:
                ret_dict['global_version'] = m.group('global_version')
                continue

            # Fantray beacon LED status
            m = p5.match(line)
            if m:
                ret_dict['beacon_led_status'] = m.group('beacon_led_status')
                continue

            # Fantray status LED
            m = p6.match(line)
            if m:
                ret_dict['status_led'] = m.group('status_led')
                continue

        return ret_dict