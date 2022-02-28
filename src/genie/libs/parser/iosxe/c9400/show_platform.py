''' show_platform.py

IOSXE C9400 parsers for the following show commands:

    * 'show environment'
    * 'show environment | include {include}'
    * 'show environment all'
    * 'show environment all | include {include}'
    * 'show boot'
    * 'Show module'
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
            
        p2=re.compile(r'^(?P<mod>\d+) *(?P<ports>\d+) +(?P<card_type>.*) +(?P<model>\S+) +(?P<serial>\S+)$')
                
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
