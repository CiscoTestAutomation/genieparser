'''show_environment.py

NXOS parsers for the following show commands:
    * show environment
'''

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
                                         
# import parser utils
from genie.libs.parser.utils.common import Common


# ========================================
# Schema for 'show environment'
# ========================================
class ShowEnvironmentSchema(MetaParser):
    """Schema for show environment"""

    schema = {
        Optional('fans'):{
            Any():{
                Optional('model'): str,
                Optional('hw'): str,
                Optional('direction'): str,
                Optional('status'): str
            },
            Optional('fan_zone_speed'): str,
            Optional('fan_air_filter'): str,
        },
        Optional('power'):{
            Optional('voltage'): int,
            Optional('power_supply'):{
                Any():{
                    Optional('model'): str,
                    Optional('actual_output_watts'): int,
                    Optional('actual_input_watts'): int,
                    Optional('total_capacity_watts'): int,
                    Optional('status'): str
                }
            },
            Optional('modules'):{
                Any(): {
                    Optional('model'): str,
                    Optional('actual_drawn'): str,
                    Optional('allocated_power'): float,
                    Optional('status'): str
                }
            },
            Optional('power_supply_mode'):{
                Optional('config_mode'): str,
                Optional('oper_mode'): str
            },
            Optional('power_usage_summary'):{
                Optional('total_power_capacity_watts'): float,
                Optional('total_grid_a_power_watts'): float,
                Optional('total_grid_b_power_watts'): float,
                Optional('total_power_cumulative_watts'): float,
                Optional('total_power_output_watts'): float,
                Optional('total_power_input_watts'): float,
                Optional('total_power_allocated_watts'): float,
                Optional('total_power_available_watts'): float
            }
        },
        Optional('temperature'): {
            Any(): {
                Any(): {
                Optional('major_threshold_celsius'): int,
                Optional('minor_threshold_celsius'): int,
                Optional('current_temp_celsius'): int,
                Optional('status'): str
                }
            }
        }
    }

# ========================================
# Parser for 'show environment'
# ========================================

class ShowEnvironment(ShowEnvironmentSchema):
    """Parser for show environment, """

    cli_command = ['show environment']

    exclude = []

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output
        
        #Match fan details
        #Fan1(sys_fan1)  N9K-C9508-FAN        0.6020 front-to-back   Ok
        p1 = re.compile(r'^\s*(?P<sys_fan>Fan\d+\(sys_fan\d+\))?\s+(?P<model>[A-Za-z0-9\-]+)? +(?P<hw>[0-9.-]+)+ +(?P<dir>[a-z-]+)? +(?P<status>\w+)?\s*')
        
        #Fan_in_PS1                           --     front-to-back   Ok
        p2 = re.compile(r'^\s*(?P<ps_fan>Fan_in_PS\d+)?\s+(?P<model>[A-Za-z0-9\-]+)?\s+(?P<hw>[0-9.-]+)+ +(?P<dir>[a-z-]+)? +(?P<status>\w+)?\s*')

        #Fan Zone Speed: Zone 1: 0x41
        p3 = re.compile(r'^\s*Fan Zone Speed: ([Zone0-9x: ]+)')

        #Fan Air Filter : NotSupported
        p4 = re.compile(r'^\s*Fan Air Filter : (\w+)')

        #Match Power and power supply details
        #Voltage: 12 Volts
        p5 = re.compile(r'^\s*Voltage: +(?P<voltage>[0-9]+)\s+Volts')

        #1        N9K-PAC-3000W-B      1087 W             1150 W      3000 W      Ok
        p6 = re.compile(r'^\s*(?P<ps_id>\d+)\s+(?P<model>[A-Z0-9-]+)\s*(?P<act_out>\d+)\s?W\s*(?P<act_in>\d+)\s?W\s*(?P<tot_cap>\d+)\s?W\s+(?P<status>\w+)\s*')

        #1        N9K-X9736Q-FX           401.00 W     936.00 W    Powered-Up
        #Xb22     N9K-C9508-FM-E          175.00 W     564.00 W    Powered-Up
        #fan1     N9K-C9508-FAN            81.00 W     249.00 W    Powered-Up
        p7 = re.compile(r'^\s*(?P<module>[fanXb0-9]+)\s+(?P<model>[A-Za-z0-9-]+)\s*(?P<act_draw>[0-9.]+)\s+W\s+(?P<powr_alloc>[0-9.]+)\s+W\s+(?P<status>[a-zA-Z-]+)\s*')
        
        #Power Supply redundancy mode (configured)                Non-Redundant(combined)
        p8 = re.compile(r'^\s*Power Supply redundancy mode \(configured\)\s+(?P<conf_mode>[-\w\(\)]+)')

        #Power Supply redundancy mode (operational)               Non-Redundant(combined)
        p9 = re.compile(r'^\s*Power Supply redundancy mode \(operational\)\s+(?P<oper_mode>[-\w\(\)]+)')

        #Total Power Capacity (based on configured mode)            18000.00 W
        p10 = re.compile(r'^\s*Total Power Capacity \(based on configured mode\)\s*([0-9.]+)\sW\s*')
        
        #Total Grid-A (first half of PS slots) Power Capacity       12000.00 W
        p11 = re.compile(r'^\s*Total Grid-A \(first half of PS slots\) Power Capacity\s*([0-9.]+)\sW\s*')

        #Total Grid-B (second half of PS slots) Power Capacity      6000.00 W
        p12 = re.compile(r'^\s*Total Grid-B \(second half of PS slots\) Power Capacity\s*([0-9.]+)\sW\s*')

        #Total Power of all Inputs (cumulative)                     18000.00 W
        p13 = re.compile(r'^\s*Total Power of all Inputs \(cumulative\)\s*([0-9.]+)\sW\s*')

        #Total Power Output (actual draw)                           5655.00 W
        p14 = re.compile(r'^\s*Total Power Output \(actual draw\)\s*([0-9.]+)\sW\s*')

        #Total Power Input (actual draw)                            6038.00 W
        p15 = re.compile(r'^\s*Total Power Input \(actual draw\)\s*([0-9.]+)\sW\s*')

        #Total Power Allocated (budget)                             10759.00 W
        p16 = re.compile(r'^\s*Total Power Allocated \(budget\)\s*([0-9.]+)\sW\s*')

        #Total Power Available for additional modules               7241.00 W
        p17 = re.compile(r'^\s*Total Power Available for additional modules\s*([0-9.]+)\sW\s*')

        #Match Temperatures
        #1        CPU             85              75          53         Ok
        #3        SUG0            105             95          59         Ok
        p18 = re.compile(r'^\s*(?P<mod>\d+)\s+(?P<sensor>\w+)\s+(?P<major_thresh>\d+)\s+(?P<minor_thresh>\d+)\s+(?P<curr_temp>\d+)\s+(?P<status>\w+)\s*')


        parsed_env_dict = {}
        parsed_env_dict.setdefault('fans', {})
        parsed_env_dict.setdefault('power', {}).setdefault('power_supply', {})
        parsed_env_dict.setdefault('power', {}).setdefault('power_supply_mode', {})
        parsed_env_dict.setdefault('power', {}).setdefault('power_usage_summary', {})
        parsed_env_dict.setdefault('temperature', {})
        
        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            #Match fan details
            #Fan1(sys_fan1)  N9K-C9508-FAN        0.6020 front-to-back   Ok
            m = p1.match(line)
            if m:
                parsed_env_dict['fans'][m.group('sys_fan')] = {
                    'model': m.group('model'), 'hw': m.group('hw'), \
                    'direction':  m.group('dir'), 'status': m.group('status')
                }
                continue
            
            #Fan_in_PS1 
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                parsed_env_dict['fans'][groups['ps_fan']] = {'hw': groups['hw'], 'direction': groups['dir'], 'status': groups['status']}
                continue
            
            #Fan Zone Speed: Zone 1: 0x41
            m = p3.match(line)
            if m:
                parsed_env_dict['fans']['fan_zone_speed']= m.group(1)
                continue
            
            #Fan Air Filter : NotSupported
            m = p4.match(line)
            if m:
                parsed_env_dict['fans']['fan_air_filter']= m.group(1)
                continue
            
            #Match Power and power supply details
            #Voltage: 12 Volts
            m = p5.match(line)
            if m:
                parsed_env_dict['power']['voltage'] = int(m.group('voltage'))
                continue
            
            #1        N9K-PAC-3000W-B      1087 W             1150 W      3000 W      Ok
            m = p6.match(line)
            if m:
                gpdict = m.groupdict()
                parsed_env_dict['power']['power_supply'][gpdict['ps_id']] = {
                    'model': gpdict['model'], 'actual_output_watts': int(gpdict['act_out']), \
                    'actual_input_watts': int(gpdict['act_in']), 'total_capacity_watts': int(gpdict['tot_cap']), \
                    'status': gpdict['status']
                }
                continue
            
            #1        N9K-X9736Q-FX           401.00 W     936.00 W    Powered-Up
            #Xb22     N9K-C9508-FM-E          175.00 W     564.00 W    Powered-Up
            #fan1     N9K-C9508-FAN            81.00 W     249.00 W    Powered-Up
            m = p7.match(line)
            if m:
                gpdict = m.groupdict()
                if 'modules' not in parsed_env_dict['power']:
                    parsed_env_dict['power'].setdefault('modules', {})
                parsed_env_dict['power']['modules'][gpdict['module']]= {
                    'model': gpdict['model'], 'actual_drawn': gpdict['act_draw'] , \
                    'allocated_power': float(gpdict['powr_alloc']) , \
                    'status': gpdict['status']
                }
                continue
            
            #Power Supply redundancy mode (configured)                Non-Redundant(combined)
            m = p8.match(line)
            if m:
                parsed_env_dict['power']['power_supply_mode']['config_mode'] = m.group('conf_mode')
                continue
            
            #Power Supply redundancy mode (operational)               Non-Redundant(combined)
            m = p9.match(line)
            if m:
                parsed_env_dict['power']['power_supply_mode']['oper_mode'] = m.group('oper_mode')
                continue
            
            #Total Power Capacity (based on configured mode)            18000.00 W
            m = p10.match(line)
            if m:
                parsed_env_dict['power']['power_usage_summary']['total_power_capacity_watts'] = float(m.group(1))
                continue

            #Total Grid-A (first half of PS slots) Power Capacity       12000.00 W
            m = p11.match(line)
            if m:
                parsed_env_dict['power']['power_usage_summary']['total_grid_a_power_watts'] = float(m.group(1))
                continue
            
            #Total Power of all Inputs (cumulative)                     18000.00 W
            m = p12.match(line)
            if m:
                parsed_env_dict['power']['power_usage_summary']['total_grid_b_power_watts'] = float(m.group(1))
                continue
            
            #Total Power of all Inputs (cumulative)                     18000.00 W
            m = p13.match(line)
            if m:
                parsed_env_dict['power']['power_usage_summary']['total_power_cumulative_watts'] = float(m.group(1))
                continue
            
            #Total Power Output (actual draw)                           5655.00 W
            m = p14.match(line)
            if m:
                parsed_env_dict['power']['power_usage_summary']['total_power_output_watts'] = float(m.group(1))
                continue
            
            #Total Power Input (actual draw)                            6038.00 W
            m = p15.match(line)
            if m:
                parsed_env_dict['power']['power_usage_summary']['total_power_input_watts'] = float(m.group(1))
                continue
            
            #Total Power Allocated (budget)                             10759.00 W
            m = p16.match(line)
            if m:
                parsed_env_dict['power']['power_usage_summary']['total_power_allocated_watts'] = float(m.group(1))
                continue
            
            #Total Power Available for additional modules               7241.00 W
            m = p17.match(line)
            if m:
                parsed_env_dict['power']['power_usage_summary']['total_power_available_watts'] = float(m.group(1))
                continue
            
            #Match Temperatures
            #1        CPU             85              75          53         Ok
            #3        SUG0            105             95          59         Ok
            m = p18.match(line)
            if m:
                groupdict = m.groupdict()
                if groupdict['mod'] not in parsed_env_dict['temperature']:
                    parsed_env_dict['temperature'][groupdict['mod']] = {}
                
                if groupdict['sensor'] not in parsed_env_dict['temperature'][groupdict['mod']]:
                    parsed_env_dict['temperature'][groupdict['mod']][groupdict['sensor']] = {}
                parsed_env_dict['temperature'][groupdict['mod']][groupdict['sensor']] = {
                    'major_threshold_celsius': int(groupdict['major_thresh']), \
                    'minor_threshold_celsius': int(groupdict['minor_thresh']), \
                    'current_temp_celsius': int(groupdict['curr_temp']), \
                    'status': groupdict['status']
                }
                continue


        return parsed_env_dict

# ========================================
# Schema for 'show environment fan'
# ========================================
class ShowEnvironmentFanSchema(MetaParser):
    """Schema for show environment fan"""

    schema = {
        Optional('fans'):{
            Any():{
                Optional('model'): str,
                Optional('hw'): str,
                Optional('direction'): str,
                Optional('status'): str
            },
            Optional('fan_zone_speed'): str,
            Optional('fan_air_filter'): str,
        }

    }

# ========================================
# Parser for 'show environment fan'
# ========================================

class ShowEnvironmentFan(ShowEnvironmentFanSchema):
    """Parser for show environment """

    cli_command = 'show environment fan'

    exclude = []

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        #Match fan details
        #Fan1(sys_fan1)  N9K-C9508-FAN        0.6020 front-to-back   Ok
        p1 = re.compile(r'^\s*(?P<sys_fan>Fan\d+\(sys_fan\d+\))?\s+(?P<model>[A-Za-z0-9\-]+)? +(?P<hw>[0-9.-]+)+ +(?P<dir>[a-z-]+)? +(?P<status>\w+)?\s*')
        
        #Fan_in_PS1                           --     front-to-back   Ok
        p2 = re.compile(r'^\s*(?P<ps_fan>Fan_in_PS\d+)?\s+(?P<model>[A-Za-z0-9\-]+)?\s+(?P<hw>[0-9.-]+)+ +(?P<dir>[a-z-]+)? +(?P<status>\w+)?\s*')

        #Fan Zone Speed: Zone 1: 0x41
        p3 = re.compile(r'^\s*Fan Zone Speed: ([Zone0-9x: ]+)')

        #Fan Air Filter : NotSupported
        p4 = re.compile(r'^\s*Fan Air Filter : (\w+)')

        parsed_env_fan_dict = {}
        parsed_env_fan_dict.setdefault('fans', {})
        
        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            #Match fan details
            #Fan1(sys_fan1)  N9K-C9508-FAN        0.6020 front-to-back   Ok
            m = p1.match(line)
            if m:
                parsed_env_fan_dict['fans'][m.group('sys_fan')] = {
                    'model': m.group('model'), 'hw': m.group('hw'), \
                    'direction':  m.group('dir'), 'status': m.group('status')
                }
                continue
            
            #Fan_in_PS1 
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                parsed_env_fan_dict['fans'][groups['ps_fan']] = {'hw': groups['hw'], 'direction': groups['dir'], 'status': groups['status']}
                continue
            
            #Fan Zone Speed: Zone 1: 0x41
            m = p3.match(line)
            if m:
                parsed_env_fan_dict['fans']['fan_zone_speed']= m.group(1)
                continue
            
            #Fan Air Filter : NotSupported
            m = p4.match(line)
            if m:
                parsed_env_fan_dict['fans']['fan_air_filter']= m.group(1)
                continue

        return parsed_env_fan_dict

# ========================================
# Schema for 'show environment fan detail'
# ========================================
class ShowEnvironmentFanDetailSchema(MetaParser):
    """Schema for show environment fan detail"""

    schema = {
        Optional('fans'):{
            Any():{
                Optional('model'): str,
                Optional('hw'): str,
                Optional('direction'): str,
                Optional('status'): str
            },
            Optional('fan_zone_speed'): str,
            Optional('fan_air_filter'): str,
            Optional('sys_fans'): {
                Any(): {
                    Any(): {
                        Optional('direction'): str,
                        Optional('speed_percent'): int,
                        Optional('speed_rpm'): int
                    }
                }
            },
            Optional('ps_fans'): {
                Optional(Any()): {
                    Optional('fan1_speed'): int,
                    Optional('fan2_speed'): int
                }
            }
        }

    }

# ========================================
# Parser for 'show environment fan detail'
# ========================================
class ShowEnvironmentFanDetail(ShowEnvironmentFanDetailSchema):
    """Parser for show environment detail """

    cli_command = 'show environment fan detail'

    exclude = []

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        #Match fan details
        #Fan1(sys_fan1)  N9K-C9508-FAN        0.6020 front-to-back   Ok
        p1 = re.compile(r'^\s*(?P<sys_fan>Fan\d+\(sys_fan\d+\))?\s+(?P<model>[A-Za-z0-9\-]+)? +(?P<hw>[0-9.-]+)+ +(?P<dir>[a-z-]+)? +(?P<status>\w+)?\s*')
        
        #Fan_in_PS1                           --     front-to-back   Ok
        p2 = re.compile(r'^\s*(?P<ps_fan>Fan_in_PS\d+)\s+(?P<model>[A-Za-z0-9\-]+)?\s+(?P<hw>[0-9.-]+) +(?P<dir>[a-z-]+) +(?P<status>\w+)\s*')

        #Fan Zone Speed: Zone 1: 0x41
        p3 = re.compile(r'^\s*Fan Zone Speed: ([Zone0-9x: ]+)')

        #Fan Air Filter : NotSupported
        p4 = re.compile(r'^\s*Fan Air Filter : (\w+)')

        #Fan1(sys_fan1)      fan6    front-to-back    84        3272
        # Fan2(sys_fan2)      fan1    front-to-back    51        3280
        # Fan2(sys_fan2)      fan2    front-to-back    61        2362
        p5 = re.compile(r'^\s*(?P<fan>Fan\d+\(sys_fan\d+\))?\s+(?P<fan_num>fan\d+)?\s+(?P<dir>[a-z-]+)?\s+(?P<speed_per>\d+)?\s+(?P<speed_rpm>\d+)?\s*')

        # Fan_in_PS1            7978                8537
        # Fan_in_PS2            8021                8473
        p6 = re.compile(r'^\s*(?P<ps_fan>Fan_in_PS\d+)\s+(?P<fan1_speed>\d+)\s+(?P<fan2_speed>\d+)\s*')

        parsed_env_fan_dict = {}
        parsed_env_fan_dict.setdefault('fans', {})
        parsed_env_fan_dict.setdefault('fans', {}).setdefault('sys_fans', {})
        parsed_env_fan_dict.setdefault('fans', {}).setdefault('ps_fans', {})

        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            #Match fan details
            #Fan1(sys_fan1)  N9K-C9508-FAN        0.6020 front-to-back   Ok
            m = p1.match(line)
            if m:
                parsed_env_fan_dict['fans'][m.group('sys_fan')] = {
                    'model': m.group('model'), 'hw': m.group('hw'), \
                    'direction':  m.group('dir'), 'status': m.group('status')
                }
                continue
            
            #Fan_in_PS1 
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                parsed_env_fan_dict['fans'][groups['ps_fan']] = {'hw': groups['hw'], 'direction': groups['dir'], 'status': groups['status']}
                continue
            
            #Fan Zone Speed: Zone 1: 0x41
            m = p3.match(line)
            if m:
                parsed_env_fan_dict['fans']['fan_zone_speed']= m.group(1)
                continue
            
            #Fan Air Filter : NotSupported
            m = p4.match(line)
            if m:
                parsed_env_fan_dict['fans']['fan_air_filter']= m.group(1)
                continue

            #Fan1(sys_fan1)      fan6    front-to-back    84        3272
            # Fan2(sys_fan2)      fan1    front-to-back    51        3280
            # Fan2(sys_fan2)      fan2    front-to-back    61        2362
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                if groups['fan'] not in parsed_env_fan_dict['fans']['sys_fans']:
                    parsed_env_fan_dict['fans']['sys_fans'][groups['fan']] = {}
                parsed_env_fan_dict['fans']['sys_fans'][groups['fan']][groups['fan_num']] = \
                {'direction': groups['dir'] , 'speed_percent': int(groups['speed_per']) , 'speed_rpm': int(groups['speed_rpm']) }
                continue

            # Fan_in_PS1            7978                8537
            # Fan_in_PS2            8021                8473
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                parsed_env_fan_dict['fans']['ps_fans'][groups['ps_fan']] = {'fan1_speed': int(groups['fan1_speed']), 'fan2_speed': int(groups['fan2_speed'])}
                continue

        return parsed_env_fan_dict


# ========================================
# Schema for 'show environment power'
# ========================================
class ShowEnvironmentPowerSchema(MetaParser):
    """Schema for show environment power"""

    schema = {
        Optional('power'):{
            Optional('voltage'): int,
            Optional('power_supply'):{
                Any():{
                    Optional('model'): str,
                    Optional('actual_output_watts'): int,
                    Optional('actual_input_watts'): int,
                    Optional('total_capacity_watts'): int,
                    Optional('status'): str
                }
            },
            Optional('modules'):{
                Any(): {
                    Optional('model'): str,
                    Optional('actual_drawn'): str,
                    Optional('allocated_power'): float,
                    Optional('status'): str
                }
            },
            Optional('power_supply_mode'):{
                Optional('config_mode'): str,
                Optional('oper_mode'): str
            },
            Optional('power_usage_summary'):{
                Optional('total_power_capacity_watts'): float,
                Optional('total_grid_a_power_watts'): float,
                Optional('total_grid_b_power_watts'): float,
                Optional('total_power_cumulative_watts'): float,
                Optional('total_power_output_watts'): float,
                Optional('total_power_input_watts'): float,
                Optional('total_power_allocated_watts'): float,
                Optional('total_power_available_watts'): float
            }
        }
    }

# ========================================
# Parser for 'show environment power'
# ========================================

class ShowEnvironmentPower(ShowEnvironmentPowerSchema):
    """Parser for show environment power """

    cli_command = 'show environment power'

    exclude = []

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        #Match Power and power supply details
        #Voltage: 12 Volts
        p1 = re.compile(r'^\s*Voltage: +(?P<voltage>[0-9]+)\s+Volts')

        #1        N9K-PAC-3000W-B      1087 W             1150 W      3000 W      Ok
        p2 = re.compile(r'^\s*(?P<ps_id>\d+)\s+(?P<model>[A-Z0-9-]+)\s*(?P<act_out>\d+)\s?W\s*(?P<act_in>\d+)\s?W\s*(?P<tot_cap>\d+)\s?W\s+(?P<status>\w+)\s*')

        #1        N9K-X9736Q-FX           401.00 W     936.00 W    Powered-Up
        #Xb22     N9K-C9508-FM-E          175.00 W     564.00 W    Powered-Up
        #fan1     N9K-C9508-FAN            81.00 W     249.00 W    Powered-Up
        p3 = re.compile(r'^\s*(?P<module>[fanXb0-9]+)\s+(?P<model>[A-Za-z0-9-]+)\s*(?P<act_draw>[0-9.]+)\s+W\s+(?P<powr_alloc>[0-9.]+)\s+W\s+(?P<status>[a-zA-Z-]+)\s*')
        
        #Power Supply redundancy mode (configured)                Non-Redundant(combined)
        p4 = re.compile(r'^\s*Power Supply redundancy mode \(configured\)\s+(?P<conf_mode>[-\w\(\)]+)')

        #Power Supply redundancy mode (operational)               Non-Redundant(combined)
        p5 = re.compile(r'^\s*Power Supply redundancy mode \(operational\)\s+(?P<oper_mode>[-\w\(\)]+)')

        #Total Power Capacity (based on configured mode)            18000.00 W
        p6 = re.compile(r'^\s*Total Power Capacity \(based on configured mode\)\s*([0-9.]+)\sW\s*')
        
        #Total Grid-A (first half of PS slots) Power Capacity       12000.00 W
        p7 = re.compile(r'^\s*Total Grid-A \(first half of PS slots\) Power Capacity\s*([0-9.]+)\sW\s*')

        #Total Grid-B (second half of PS slots) Power Capacity      6000.00 W
        p8 = re.compile(r'^\s*Total Grid-B \(second half of PS slots\) Power Capacity\s*([0-9.]+)\sW\s*')

        #Total Power of all Inputs (cumulative)                     18000.00 W
        p9 = re.compile(r'^\s*Total Power of all Inputs \(cumulative\)\s*([0-9.]+)\sW\s*')

        #Total Power Output (actual draw)                           5655.00 W
        p10 = re.compile(r'^\s*Total Power Output \(actual draw\)\s*([0-9.]+)\sW\s*')

        #Total Power Input (actual draw)                            6038.00 W
        p11 = re.compile(r'^\s*Total Power Input \(actual draw\)\s*([0-9.]+)\sW\s*')

        #Total Power Allocated (budget)                             10759.00 W
        p12 = re.compile(r'^\s*Total Power Allocated \(budget\)\s*([0-9.]+)\sW\s*')

        #Total Power Available for additional modules               7241.00 W
        p13 = re.compile(r'^\s*Total Power Available for additional modules\s*([0-9.]+)\sW\s*')

        parsed_env_power_dict = {}
        parsed_env_power_dict.setdefault('power', {}).setdefault('power_supply', {})
        parsed_env_power_dict.setdefault('power', {}).setdefault('power_supply_mode', {})
        parsed_env_power_dict.setdefault('power', {}).setdefault('power_usage_summary', {})
        
        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            #Match Power and power supply details
            #Voltage: 12 Volts
            m = p1.match(line)
            if m:
                parsed_env_power_dict['power']['voltage'] = int(m.group('voltage'))
                continue
            
            #1        N9K-PAC-3000W-B      1087 W             1150 W      3000 W      Ok
            m = p2.match(line)
            if m:
                gpdict = m.groupdict()
                parsed_env_power_dict['power']['power_supply'][gpdict['ps_id']] = {
                    'model': gpdict['model'], 'actual_output_watts': int(gpdict['act_out']), \
                    'actual_input_watts': int(gpdict['act_in']), 'total_capacity_watts': int(gpdict['tot_cap']), \
                    'status': gpdict['status']
                }
                continue
            
            #1        N9K-X9736Q-FX           401.00 W     936.00 W    Powered-Up
            #Xb22     N9K-C9508-FM-E          175.00 W     564.00 W    Powered-Up
            #fan1     N9K-C9508-FAN            81.00 W     249.00 W    Powered-Up
            m = p3.match(line)
            if m:
                gpdict = m.groupdict()
                if 'modules' not in parsed_env_power_dict['power']:
                    parsed_env_power_dict['power'].setdefault('modules', {})
                parsed_env_power_dict['power']['modules'][gpdict['module']]= {
                    'model': gpdict['model'], 'actual_drawn': gpdict['act_draw'] , \
                    'allocated_power': float(gpdict['powr_alloc']) , \
                    'status': gpdict['status']
                }
                continue
            
            #Power Supply redundancy mode (configured)                Non-Redundant(combined)
            m = p4.match(line)
            if m:
                parsed_env_power_dict['power']['power_supply_mode']['config_mode'] = m.group('conf_mode')
                continue
            
            #Power Supply redundancy mode (operational)               Non-Redundant(combined)
            m = p5.match(line)
            if m:
                parsed_env_power_dict['power']['power_supply_mode']['oper_mode'] = m.group('oper_mode')
                continue
            
            #Total Power Capacity (based on configured mode)            18000.00 W
            m = p6.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_power_capacity_watts'] = float(m.group(1))
                continue

            #Total Grid-A (first half of PS slots) Power Capacity       12000.00 W
            m = p7.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_grid_a_power_watts'] = float(m.group(1))
                continue
            
            #Total Power of all Inputs (cumulative)                     18000.00 W
            m = p8.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_grid_b_power_watts'] = float(m.group(1))
                continue
            
            #Total Power of all Inputs (cumulative)                     18000.00 W
            m = p9.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_power_cumulative_watts'] = float(m.group(1))
                continue
            
            #Total Power Output (actual draw)                           5655.00 W
            m = p10.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_power_output_watts'] = float(m.group(1))
                continue
            
            #Total Power Input (actual draw)                            6038.00 W
            m = p11.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_power_input_watts'] = float(m.group(1))
                continue
            
            #Total Power Allocated (budget)                             10759.00 W
            m = p12.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_power_allocated_watts'] = float(m.group(1))
                continue
            
            #Total Power Available for additional modules               7241.00 W
            m = p13.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_power_available_watts'] = float(m.group(1))
                continue


        return parsed_env_power_dict


# ========================================
# Schema for 'show environment power detail'
# ========================================
class ShowEnvironmentPowerDetailSchema(MetaParser):
    """Schema for show environment power detail"""

    schema = {
        Optional('power'):{
            Optional('voltage'): int,
            Optional('power_supply'):{
                Any():{
                    Optional('model'): str,
                    Optional('actual_output_watts'): int,
                    Optional('actual_input_watts'): int,
                    Optional('total_capacity_watts'): int,
                    Optional('status'): str
                }
            },
            Optional('modules'):{
                Any(): {
                    Optional('model'): str,
                    Optional('actual_drawn'): str,
                    Optional('allocated_power'): float,
                    Optional('status'): str
                }
            },
            Optional('power_supply_mode'):{
                Optional('config_mode'): str,
                Optional('oper_mode'): str
            },
            Optional('power_usage_summary'):{
                Optional('total_power_capacity_watts'): float,
                Optional('total_grid_a_power_watts'): float,
                Optional('total_grid_b_power_watts'): float,
                Optional('total_power_cumulative_watts'): float,
                Optional('total_power_output_watts'): float,
                Optional('total_power_input_watts'): float,
                Optional('total_power_allocated_watts'): float,
                Optional('total_power_available_watts'): float
            },
            Optional('power_usage_details'):{
                Optional('power_reserved_for_sup_watts'): str,
                Optional('power_reserved_for_fabric_sc_watts'): str,
                Optional('power_reserved_for_fan_module_watts'): str,
                Optional('total_power_reserved_watts'): str,
                Optional('all_inlet_cords_connected'): str
            },
            Optional('power_supply_details'):{
                Any():{
                    Optional('total_capacity_watts'): int,
                    Optional('voltage'): int, 
                    Optional('Pin'): float,
                    Optional('Vin'): float,
                    Optional('Iin'): float,
                    Optional('Pout'): float,
                    Optional('Vout'): float,
                    Optional('Iout'): float,
                    Optional('cord_connected'): bool,
                    Optional('connected_to'): str,
                    Optional('software_alarm'): str,
                    Optional('hardware_alarm'): str,
                    Optional('hw_registers'): list
                }
            }
        }
    }


# ========================================
# Parser for 'show environment power detail'
# ========================================

class ShowEnvironmentPowerDetail(ShowEnvironmentPowerDetailSchema):
    """Parser for show environment power detail """

    cli_command = 'show environment power detail'

    exclude = []

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        #Match Power and power supply details
        #Voltage: 12 Volts
        p1 = re.compile(r'^\s*Voltage: +(?P<voltage>[0-9]+)\s+Volts')

        #1        N9K-PAC-3000W-B      1087 W             1150 W      3000 W      Ok
        p2 = re.compile(r'^\s*(?P<ps_id>\d+)\s+(?P<model>[A-Z0-9-]+)\s*(?P<act_out>\d+)\s?W\s*(?P<act_in>\d+)\s?W\s*(?P<tot_cap>\d+)\s?W\s+(?P<status>\w+)\s*')

        #1        N9K-X9736Q-FX           401.00 W     936.00 W    Powered-Up
        #Xb22     N9K-C9508-FM-E          175.00 W     564.00 W    Powered-Up
        #fan1     N9K-C9508-FAN            81.00 W     249.00 W    Powered-Up
        p3 = re.compile(r'^\s*(?P<module>[fanXb0-9]+)\s+(?P<model>[A-Za-z0-9-]+)\s*(?P<act_draw>[0-9.]+)\s+W\s+(?P<powr_alloc>[0-9.]+)\s+W\s+(?P<status>[a-zA-Z-]+)\s*')
        
        #Power Supply redundancy mode (configured)                Non-Redundant(combined)
        p4 = re.compile(r'^\s*Power Supply redundancy mode \(configured\)\s+(?P<conf_mode>[-\w\(\)]+)')

        #Power Supply redundancy mode (operational)               Non-Redundant(combined)
        p5 = re.compile(r'^\s*Power Supply redundancy mode \(operational\)\s+(?P<oper_mode>[-\w\(\)]+)')

        #Total Power Capacity (based on configured mode)            18000.00 W
        p6 = re.compile(r'^\s*Total Power Capacity \(based on configured mode\)\s*([0-9.]+)\sW\s*')
        
        #Total Grid-A (first half of PS slots) Power Capacity       12000.00 W
        p7 = re.compile(r'^\s*Total Grid-A \(first half of PS slots\) Power Capacity\s*([0-9.]+)\sW\s*')

        #Total Grid-B (second half of PS slots) Power Capacity      6000.00 W
        p8 = re.compile(r'^\s*Total Grid-B \(second half of PS slots\) Power Capacity\s*([0-9.]+)\sW\s*')

        #Total Power of all Inputs (cumulative)                     18000.00 W
        p9 = re.compile(r'^\s*Total Power of all Inputs \(cumulative\)\s*([0-9.]+)\sW\s*')

        #Total Power Output (actual draw)                           5655.00 W
        p10 = re.compile(r'^\s*Total Power Output \(actual draw\)\s*([0-9.]+)\sW\s*')

        #Total Power Input (actual draw)                            6038.00 W
        p11 = re.compile(r'^\s*Total Power Input \(actual draw\)\s*([0-9.]+)\sW\s*')

        #Total Power Allocated (budget)                             10759.00 W
        p12 = re.compile(r'^\s*Total Power Allocated \(budget\)\s*([0-9.]+)\sW\s*')

        #Total Power Available for additional modules               7241.00 W
        p13 = re.compile(r'^\s*Total Power Available for additional modules\s*([0-9.]+)\sW\s*')


        # Power reserved for Supervisor(s):                              180 W
        p14 = re.compile(r'^\s*Power reserved for Supervisor\(s\):\s+(?P<pow_res_sup>[0-9NA/]+)\s?W?') 

        # Power reserved for Fabric, SC Module(s):                      2870 W
        p15 = re.compile(r'^\s*Power reserved for Fabric, SC Module\(s\):\s+(?P<pow_res_sc>[0-9NA/]+)\s?W?')

        # Power reserved for Fan Module(s):                              740 W
        p16 = re.compile(r'^\s*Power reserved for Fan Module\(s\):\s+(?P<pow_res_fan>[0-9NA/]+)\s?W?')

        # Total power reserved for Sups,SCs,Fabrics,Fans:               3799 W
        p17 = re.compile(r'^\s*Total power reserved for Sups,SCs,Fabrics,Fans:\s+(?P<pow_res_total>[0-9NA/]+)\s?W?')

        # Are all inlet cords connected: No
        p18 = re.compile(r'^\s*Are all inlet cords connected:\s+(?P<inlet_cord_connected>\w+)')

        # PS_5 total capacity:       0 W   Voltage:12V
        # PS_7 total capacity:    3000 W   Voltage:12V
        p19 = re.compile(r'^\s*(?P<ps>PS_\d+)\s+total capacity: +(?P<tot_cap>\d+) W\s+Voltage:(?P<voltage>\d+)V\s*')

        # Pin:1143.68W  Vin:236.07V    Iin:4.89A    Pout:1076.82W    Vout:12.08V    Iout:90.03A
        # Pin:0.00W  Vin:0.00V    Iin:0.00A    Pout:0.00W    Vout:0.00V    Iout:0.00A
        p20 = re.compile(r'^\s*Pin:(?P<power_in>[0-9.]+)W\s+Vin:(?P<volt_in>[0-9.]+)V\s+Iin:(?P<cur_in>[0-9.]+)A\s+Pout:(?P<power_out>[0-9.]+)W\s+Vout:(?P<volt_out>[0-9.]+)V\s+Iout:(?P<cur_out>[0-9.]+)A\s*')

        # Cord connected to 220V AC
        # Cord not connected
        p21 = re.compile(r'^\s*(?P<cord_connected>[Cord connected]+)\s?to?\s?(?P<input>\d+)?V?')

        # Software-Alarm: No
        p22 = re.compile(r'^\s*Software-Alarm: (?P<soft_alarm>.*)')
        
        # Hardware alarm_bits reg0:20, reg2: 1,
        # Hardware alarm_bits
        p23 = re.compile(r'^\s*Hardware alarm_bits\s?(?P<hard_alarm>.*)')
        
        # Reg0 bit5: No input detected
        # Reg2 bit0: Vin out of range
        p24 = re.compile(r'^\s*(?P<reg_bit>Reg\d+ bit\d+): (?P<reg_val>.*)\s*')

        parsed_env_power_dict = {}
        parsed_env_power_dict.setdefault('power', {}).setdefault('power_supply', {})
        parsed_env_power_dict.setdefault('power', {}).setdefault('power_supply_mode', {})
        parsed_env_power_dict.setdefault('power', {}).setdefault('power_usage_summary', {})
        parsed_env_power_dict.setdefault('power', {}).setdefault('power_usage_details', {})
        parsed_env_power_dict.setdefault('power', {}).setdefault('power_supply_details', {})
        
        ps = ''

        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            #Match Power and power supply details
            #Voltage: 12 Volts
            m = p1.match(line)
            if m:
                parsed_env_power_dict['power']['voltage'] = int(m.group('voltage'))
                continue
            
            #1        N9K-PAC-3000W-B      1087 W             1150 W      3000 W      Ok
            m = p2.match(line)
            if m:
                gpdict = m.groupdict()
                parsed_env_power_dict['power']['power_supply'][gpdict['ps_id']] = {
                    'model': gpdict['model'], 'actual_output_watts': int(gpdict['act_out']), \
                    'actual_input_watts': int(gpdict['act_in']), 'total_capacity_watts': int(gpdict['tot_cap']), \
                    'status': gpdict['status']
                }
                continue
            
            #1        N9K-X9736Q-FX           401.00 W     936.00 W    Powered-Up
            #Xb22     N9K-C9508-FM-E          175.00 W     564.00 W    Powered-Up
            #fan1     N9K-C9508-FAN            81.00 W     249.00 W    Powered-Up
            m = p3.match(line)
            if m:
                gpdict = m.groupdict()
                if 'modules' not in parsed_env_power_dict['power']:
                    parsed_env_power_dict['power'].setdefault('modules', {})
                parsed_env_power_dict['power']['modules'][gpdict['module']]= {
                    'model': gpdict['model'], 'actual_drawn': gpdict['act_draw'] , \
                    'allocated_power': float(gpdict['powr_alloc']) , \
                    'status': gpdict['status']
                }
                continue
            
            #Power Supply redundancy mode (configured)                Non-Redundant(combined)
            m = p4.match(line)
            if m:
                parsed_env_power_dict['power']['power_supply_mode']['config_mode'] = m.group('conf_mode')
                continue
            
            #Power Supply redundancy mode (operational)               Non-Redundant(combined)
            m = p5.match(line)
            if m:
                parsed_env_power_dict['power']['power_supply_mode']['oper_mode'] = m.group('oper_mode')
                continue
            
            #Total Power Capacity (based on configured mode)            18000.00 W
            m = p6.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_power_capacity_watts'] = float(m.group(1))
                continue

            #Total Grid-A (first half of PS slots) Power Capacity       12000.00 W
            m = p7.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_grid_a_power_watts'] = float(m.group(1))
                continue
            
            #Total Power of all Inputs (cumulative)                     18000.00 W
            m = p8.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_grid_b_power_watts'] = float(m.group(1))
                continue
            
            #Total Power of all Inputs (cumulative)                     18000.00 W
            m = p9.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_power_cumulative_watts'] = float(m.group(1))
                continue
            
            #Total Power Output (actual draw)                           5655.00 W
            m = p10.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_power_output_watts'] = float(m.group(1))
                continue
            
            #Total Power Input (actual draw)                            6038.00 W
            m = p11.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_power_input_watts'] = float(m.group(1))
                continue
            
            #Total Power Allocated (budget)                             10759.00 W
            m = p12.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_power_allocated_watts'] = float(m.group(1))
                continue
            
            #Total Power Available for additional modules               7241.00 W
            m = p13.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_summary']['total_power_available_watts'] = float(m.group(1))
                continue

            m = p14.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_details']['power_reserved_for_sup_watts'] = m.group('pow_res_sup')
                continue

            m = p15.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_details']['power_reserved_for_fabric_sc_watts'] = m.group('pow_res_sc')
                continue

            m = p16.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_details']['power_reserved_for_fan_module_watts'] = m.group('pow_res_fan')
                continue

            m = p17.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_details']['total_power_reserved_watts'] = m.group('pow_res_total')
                continue

            m = p18.match(line)
            if m:
                parsed_env_power_dict['power']['power_usage_details']['all_inlet_cords_connected'] = m.group('inlet_cord_connected')
                continue

            # PS_5 total capacity:       0 W   Voltage:12V
            # PS_7 total capacity:    3000 W   Voltage:12V
            m = p19.match(line)
            if m:
                ps = m.group('ps')
                parsed_env_power_dict['power']['power_supply_details'][ps] = {'total_capacity_watts': int(m.group('tot_cap')), 'voltage': int(m.group('voltage'))}
                continue
            
            # Pin:1143.68W  Vin:236.07V    Iin:4.89A    Pout:1076.82W    Vout:12.08V    Iout:90.03A
            # Pin:0.00W  Vin:0.00V    Iin:0.00A    Pout:0.00W    Vout:0.00V    Iout:0.00A
            m = p20.match(line)
            if m:
                p_dict = m.groupdict()
                if ps:
                    parsed_env_power_dict['power']['power_supply_details'][ps].update({'Pin': float(p_dict['power_in']), \
                        'Pout': float(p_dict['power_out']), \
                        'Vin': float(p_dict['volt_in']), \
                        'Vout': float(p_dict['volt_out']), \
                        'Iin': float(p_dict['cur_in']), \
                        'Iout': float(p_dict['cur_out'])})
                continue

            # Cord connected to 220V AC
            # Cord not connected
            m = p21.match(line)
            if m:
                if ps:
                    parsed_env_power_dict['power']['power_supply_details'][ps].update({'cord_connected': False if 'not' in m.group('cord_connected') else True, \
                        'connected_to': str(m.group('input'))})
                continue

            # Software-Alarm: No
            m = p22.match(line)
            if m:
                if ps:
                    parsed_env_power_dict['power']['power_supply_details'][ps]['software_alarm'] = m.group('soft_alarm')

            # Hardware alarm_bits reg0:20, reg2: 1,
            # Hardware alarm_bits
            m = p23.match(line)
            if m:
                v_dict = m.groupdict()
                if ps:
                    parsed_env_power_dict['power']['power_supply_details'][ps]['hardware_alarm'] = v_dict['hard_alarm']
            
            # Reg0 bit5: No input detected
            # Reg2 bit0: Vin out of range
            m = p24.match(line)
            if m:
                if ps:
                    if 'hw_registers' not in parsed_env_power_dict['power']['power_supply_details'][ps]:
                        parsed_env_power_dict['power']['power_supply_details'][ps]['hw_registers'] = []
                    parsed_env_power_dict['power']['power_supply_details'][ps]['hw_registers'].append({m.group('reg_bit'): m.group('reg_val')})
                continue

        return parsed_env_power_dict


# ========================================
# Schema for 'show environment temperature'
# ========================================
class ShowEnvironmentTemperatureSchema(MetaParser):
    """Schema for show environment temperature """

    schema = {
        Any(): {
            Any(): {
            Optional('major_threshold_celsius'): int,
            Optional('minor_threshold_celsius'): int,
            Optional('current_temp_celsius'): int,
            Optional('status'): str
            }
        }
    }

# ========================================
# Parser for 'show environment temperature'
# ========================================

class ShowEnvironmentTemperature(ShowEnvironmentTemperatureSchema):
    """Parser for show environment temperature """

    cli_command = ['show environment temperature', 'show environment temperature module {module}']

    exclude = []

    def cli(self, module="", output=None):
        if output is None:
            if module:
                cmd = self.cli_command[1].format(module=module)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        #Match Temperatures
        #1        CPU             85              75          53         Ok
        p1 = re.compile(r'^\s*(?P<mod>\d+)\s+'
                        r'(?P<sensor>\w+)\s+'
                        r'(?P<major_thresh>\d+)\s+'
                        r'(?P<minor_thresh>\d+)\s+'
                        r'(?P<curr_temp>\d+)\s+'
                        r'(?P<status>\w+)\s*')


        parsed_env_temp_dict = {}
        
        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()
            
            #Match Temperatures
            #1        CPU             85              75          53         Ok
            #3        SUG0            105             95          59         Ok
            m = p1.match(line)
            if m:
                groupdict = m.groupdict()
                if groupdict['mod'] not in parsed_env_temp_dict:
                    parsed_env_temp_dict[groupdict['mod']] = {}
                
                if groupdict['sensor'] not in parsed_env_temp_dict[groupdict['mod']]:
                    parsed_env_temp_dict[groupdict['mod']][groupdict['sensor']] = {}
                parsed_env_temp_dict[groupdict['mod']][groupdict['sensor']] = {
                    'major_threshold_celsius': int(groupdict['major_thresh']), \
                    'minor_threshold_celsius': int(groupdict['minor_thresh']), \
                    'current_temp_celsius': int(groupdict['curr_temp']), \
                    'status': groupdict['status']
                }
                continue


        return parsed_env_temp_dict

