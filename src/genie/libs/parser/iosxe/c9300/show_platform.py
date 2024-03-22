"""
IOSXE C9300 parsers for the following show commands:
    * show inventory
    * 'show platform software fed {state} matm macTable vlan {vlan}'
    * 'show platform software fed {switch} {state} matm macTable vlan {vlan}'
"""
# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, ListOf
from genie.libs.parser.utils.common import Common


# ============================
#  Schema for 'show inventory'
# ============================
class ShowInventorySchema(MetaParser):

    """ Schema for:
        * show inventory
    """
    schema = {
        'index': {
            Any():
                {'name': str,
                 'descr': str,
                 Optional('pid'): str,
                 Optional('vid'): str,
                 Optional('sn'): str,
                }
            }
        }


# ============================
#  Parser for 'show inventory'
# ============================
class ShowInventory(ShowInventorySchema):
    """
    Parser for :
        * show inventory
    """

    cli_command = 'show inventory'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        index = 0

        # --------------------------------------------------------------
        # Regex patterns
        # --------------------------------------------------------------
        # NAME: "c93xx Stack", DESCR: "c93xx Stack"
        p1 = re.compile(r'^NAME: +\"(?P<name>[\s\S]+)\",'
                        r' +DESCR: +\"(?P<descr>[\s\S]+)\"$')

        # PID: C9300-48UXM       , VID: V02  , SN: FCW2242G0V3
        # PID: C9300-24T         , VID:      , SN:
        p2 = re.compile(r'^PID: +(?P<pid>\S+) +, +VID:( +(?P<vid>\S+))? +,'
                        r' +SN:( +(?P<sn>\S+))?$')

        # --------------------------------------------------------------
        # Build the parsed output
        # --------------------------------------------------------------
        for line in out.splitlines():
            line = line.strip()

            # NAME: "c93xx Stack", DESCR: "c93xx Stack"
            m = p1.match(line)
            if m:
                index += 1
                group = m.groupdict()
                final_dict = parsed_dict.setdefault('index', {}).setdefault(index, {})
                for key in group.keys():
                    if group[key]:
                        final_dict[key] = group[key]
                continue

            # PID: C9300-48UXM       , VID: V02  , SN: FCW2242G0V3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                for key in group.keys():
                    if group[key]:
                        final_dict[key] = group[key]
                continue

        return parsed_dict


class ShowEnvironmentAllSchema(MetaParser):
    """Schema for show environment all"""
    schema = {
        Optional('sensor_list'): {
            'location':{ 
                Any():{
                    'sensor':{
                        Any():{
                            'state': str,
                            'reading':str,
                            Optional('range'):{
                                'min' : str,
                                'max': str,
                            } 
                        }
                    }
                }
            }
        },
        'switch': {
            Any(): {
                'fan': {
                    Any(): {
                        'state': str,
                        Optional('direction'): str,
                        Optional('speed'): int,
                    },
                },
                'power_supply': {
                    Any(): {
                        Optional('state'): str,
                        Optional('pid'): str,
                        Optional('serial_number'): str,
                        'status': str,
                        Optional('system_power'): str,
                        Optional('poe_power'): str,
                        Optional('watts'): str
                    }
                },
                Optional('system_temperature_state'): str,
                Optional('inlet_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('outlet_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('hotspot_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('asic_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
            },
        },
    }


class ShowEnvironmentAll(ShowEnvironmentAllSchema):
    """Parser for show environment all"""
    PS_MAPPING = {'A': '1', 'B': '2'}

    cli_command = 'show environment all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        #  Sensor          Location        State               Reading       Range(min-max)
        #  PS1 Vout        2               GOOD               56125 mV          na
        #  PS1 Vin         2               GOOD              205000 mV        90 - 264
        p0 = re.compile(r'^(?P<sensor>(\w+ \w+))\s+(?P<location>\d)\s+(?P<state>(\w+( \w+)?))\s+(?P<reading>(\w+ \w+))\s+(?P<min>[\w ]+)(( - )?(?P<max>[\w]+)?)$')

        # Switch 1 FAN 1 is OK
        p1 = re.compile(r'^Switch +(?P<switch>\d+) +FAN +(?P<fan>\d+) +is +(?P<state>[\w\s]+)$')

        # Switch 1 FAN 1 direction is Front to Back
        p1_1 = re.compile(r'^Switch +(?P<switch>\d+) +FAN +(?P<fan>\d+) +direction +is +(?P<direction>[\w\s]+)$')

        # Switch   FAN     Speed   State
        # ----------------------------------
        # 1        1       14240     OK
        p1_2 = re.compile(r'^(?P<switch>\d+)\s+(?P<fan>\d+)\s+(?P<speed>\d+)\s+(?P<state>[\w]+)$')
        
        # Switch     FAN     Speed     State     Airflow direction
        # ---------------------------------------------------
        # 1        1    5440       OK     Front to Back
        p1_2_3 = re.compile(r'^(?P<switch>\d+)\s+(?P<fan>\d+)\s+(?P<speed>\d+)\s+(?P<state>[\w]+)\s+(?P<direction>[\w\s]+)$')

        # FAN PS-1 is OK
        p2 = re.compile(r'^FAN +PS\-(?P<ps>\d+) +is +(?P<state>[\w\s]+)$')

        # Switch 1: SYSTEM TEMPERATURE is OK
        p3 = re.compile(r'^Switch +(?P<switch>\d+): +SYSTEM +TEMPERATURE +is +(?P<state>[\w\s]+)$')

        # Inlet Temperature Value: 21 Degree Celsius
        # Outlet Temperature Value: 32 Degree Celsius
        # Hotspot Temperature Value: 49 Degree Celsius
        p4 = re.compile(r'^(?P<type>\w+) +Temperature +Value: +(?P<temperature>\d+) +Degree +Celsius$')

        # Temperature State: GREEN
        p5 = re.compile(r'^Temperature +State: +(?P<state>\w+)$')

        # Yellow Threshold : 105 Degree Celsius
        # Red Threshold    : 125 Degree Celsius
        p6 = re.compile(r'^(?P<color>\w+) +Threshold *: +(?P<temperature>\d+) +Degree +Celsius$')

        # SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
        # --  ------------------  ----------  ---------------  -------  -------  -----
        # 1A  PWR-C1-350WAC-P     DCC2337B0K5  OK              Good     n/a      350
        # 1A  PWR-C4-950WAC-R     APS222700VU  No Input Power  Bad      n/a      950
        # 1B  Not Present
        p7 = re.compile(r'^(?P<sw>\d+)(?P<ps>\w+) *'
                        r'((?P<pid>[\w\-]+) +'
                        r'(?P<serial_number>\w+) +)?'
                        r'(?P<status>(\w+|Not Present|No Input Power)) *'
                        r'((?P<system_power>\w+) +'
                        r'(?P<poe_power>[\w\/]+) +'
                        r'(?P<watts>\w+))?$')

        for line in out.splitlines():
            line = line.strip()

            #  Sensor          Location        State               Reading       Range(min-max)
            #  PS1 Vout        2               GOOD               56125 mV          na
            #  PS1 Vin         2               GOOD              205000 mV        90 - 264
            m = p0.match(line)
            if m:
                group = m.groupdict()
                sensor_dict = ret_dict.setdefault('sensor_list', {}) \
                    .setdefault('location', {}).setdefault(group['location'], {}) \
                        .setdefault('sensor', {}).setdefault(group['sensor'], {})
                sensor_dict.update({"state": group['state']})
                sensor_dict.update({"reading": group['reading']})
                range_dict = sensor_dict.setdefault('range',{})
                if group['min'] != 'na':
                    range_dict.update({"min": group['min']})
                    range_dict.update({"max": group['max']}) 
                else:
                    range_dict.update({'min': 'na'})
                    range_dict.update({'max': 'na'})
                continue

            # Switch 1 FAN 1 is OK
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                root_dict.setdefault('fan', {}).setdefault(fan, {}).setdefault('state', group['state'])
                continue

            # Switch 1 FAN 1 direction is Front to Back
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                fan_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})\
                                   .setdefault('fan', {}).setdefault(fan, {})
                fan_dict.update({'direction': group['direction']})
                continue

            # Switch   FAN     Speed   State
            # ----------------------------------
            #   1       1      14240     OK

            # Switch     FAN     Speed     State     Airflow direction
            # ---------------------------------------------------
            # 1        1    5440       OK     Front to Back
            m1 = p1_2.match(line)
            m2 = p1_2_3.match(line)
            m = m1 if m1 else m2
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                speed = int(group['speed'])
                state = group['state']

                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                fan_dict = root_dict.setdefault('fan', {}).setdefault(fan, {})
                fan_dict.update({'speed': speed,
                                 'state': state})
                if 'direction' in group:
                    fan_dict.update({'direction':group['direction']})
                continue

            # FAN PS-1 is OK
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ps = group['ps']
                power_supply_dict = root_dict.setdefault('power_supply', {}).setdefault(ps, {})
                power_supply_dict.setdefault('state', group['state'])
                continue

            # Switch 1: SYSTEM TEMPERATURE is OK
            m = p3.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                root_dict['system_temperature_state'] = group['state']
                continue

            # Inlet Temperature Value: 34 Degree Celsius
            # Hotspot Temperature Value: 45 Degree Celsius
            # ASIC Temperature Value: 36 Degree Celsius
            m = p4.match(line)
            if m:
                group = m.groupdict()
                temp_type = group['type'].lower() + '_temperature'
                temp_dict = root_dict.setdefault(temp_type, {})
                temp_dict['value'] = group['temperature']
                continue

            # Temperature State: GREEN
            m = p5.match(line)
            if m:
                temp_dict['state'] = m.groupdict()['state']
                continue

            # Yellow Threshold : 46 Degree Celsius
            # Red Threshold    : 56 Degree Celsius
            m = p6.match(line)
            if m:
                group = m.groupdict()
                color_type = group['color'].lower() + '_threshold'
                temp_dict[color_type] = group['temperature']
                continue

            # SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
            # --  ------------------  ----------  ---------------  -------  -------  -----
            # 1A  PWR-C1-715WAC       DCB1844G1ZY  OK              Good     Good     715
            # 1B  Not Present
            m = p7.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('sw')
                ps = self.PS_MAPPING[group.pop('ps')]
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                power_supply_dict = root_dict.setdefault('power_supply', {}).setdefault(ps, {})
                power_supply_dict.update({k: v for k, v in group.items()
                        if k in ['pid', 'serial_number', 'watts'] and v})
                power_supply_dict.update({k: v for k, v in group.items()
                        if k in ['status', 'system_power', 'poe_power'] and v})
                continue
        return ret_dict

# ========================================================
# Schema for:
#  * 'show platform hardware authentication status'
# ========================================================
class ShowPlatformHardwareAuthenticationStatusSchema(MetaParser):
    """Schema for show platform hardware authentication status."""

    schema = {
        'switch': {
            int: {
                   'mainboard_authentication': str,
                   Optional('fru_authentication'): str,
                   'stack_cable_a_authentication': str,
                   'stack_cable_b_authentication': str,
                    Optional('stack_adapter_a_authentication'):str,
                    Optional('stack_adapter_b_authentication'):str,
             },
    },
    }


# ===================================================
# Parser for:
#  * 'show platform hardware authentication status'
# ===================================================
class ShowPlatformHardwareAuthenticationStatus(ShowPlatformHardwareAuthenticationStatusSchema):
    """Parser for show platform hardware authentication status"""

    cli_command = 'show platform hardware authentication status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        result_dict = {}
        # Switch 1:
        p1 = re.compile(r'^Switch\s+(?P<switch>\d+):$')

        #    Mainboard Authentication:     Passed
        p2 = re.compile(r'^Mainboard Authentication:\s+(?P<mainboard_authentication>\w+(\s\w+)?)$')

        #    FRU Authentication:           Not Available
        p3 = re.compile(r'^FRU Authentication:\s+(?P<fru_authentication>\w+(\s\w+)?)$')
        #    Stack Cable A Authentication: Passed
        p4 = re.compile(r'^Stack Cable A Authentication:\s+(?P<stack_cable_a_authentication>\w+(\s\w+)?)$')
        #    Stack Cable B Authentication: Passed
        p5 = re.compile(r'^Stack Cable B Authentication:\s+(?P<stack_cable_b_authentication>\w+(\s\w+)?)$')
        # Stack Adapter A Authentication Passed
        p6 = re.compile(r'^Stack Adapter A (Authentication:|Authenticatio)\s+(?P<stack_adapter_a_authentication>[\s\w]+)$')
        # Stack Adapter B Authentication Passed
        p7 = re.compile(r'^Stack Adapter B (Authentication:|Authenticatio)\s+(?P<stack_adapter_b_authentication>[\s\w]+)$')

        for line in output.splitlines():
            line = line.strip()

            #Switch:1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                switch_dict = result_dict.setdefault('switch', {})
                switch_id_dict = switch_dict.setdefault(int(switch), {})
                continue

            #Mainboard Authentication:     Passed
            m = p2.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict['mainboard_authentication'] = group['mainboard_authentication']
                continue

            #FRU Authentication:           Not Available
            m = p3.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict['fru_authentication'] = group['fru_authentication']
                continue

            #Stack Cable A Authentication: Passed
            m = p4.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict['stack_cable_a_authentication'] = group['stack_cable_a_authentication']
                continue

            #Stack Cable B Authentication: Passed
            m = p5.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict['stack_cable_b_authentication'] = group['stack_cable_b_authentication']
                continue

            # Stack Adapter A Authentication Passed
            m = p6.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict['stack_adapter_a_authentication'] = group['stack_adapter_a_authentication']
                continue

            # Stack Adapter B Authentication Passed
            m = p7.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict['stack_adapter_b_authentication'] = group['stack_adapter_b_authentication']
                continue
        
        return result_dict

class ShowLicenseAuthorizationSchema(MetaParser):

    schema={
        "overall status":{
          "active":{
            "pid": str,
            "sn": str
            }
          },
        "status": str,
        "purchased_licenses": str
    }

class ShowLicenseAuthorization(ShowLicenseAuthorizationSchema):
    """
    Parser for :
        'ShowLicenseAuthorization'
    """
    cli_command = 'show license authorization'

    def cli(self,output=None): 

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        #Active: PID:C9300-24UX,SN:FCW2147L0C5
        p1 = re.compile(r'^Active:\s+PID:(?P<pid>\S+)+SN:(?P<sn>\S+).*$') 

        #Status: NOT INSTALLED
        p2 = re.compile(r'^Status:\s(?P<status>\S+\s+\S+).*$')

        #No Purchase Information Available
        p3 = re.compile(r'^(?P<purchased_licenses>\S+\s+Purchase+\s+\S+\s+\S+).*$')

        for line in output.splitlines():
            line=line.strip()

            #Active: PID:C9300-24UX,SN:FCW2147L0C5
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sub_dict=ret_dict.setdefault("overall status",{}).setdefault("active",{})
                pid = group['pid']
                sn = group['sn']
                sub_dict['pid'] = pid
                sub_dict['sn'] = sn
                continue

            #Status: NOT INSTALLED
            m = p2.match(line)
            if m:
                group = m.groupdict()
                status = group['status']
                ret_dict['status'] = status
                continue

            #No Purchase Information Available    
            m = p3.match(line)
            if m:
                group = m.groupdict()
                purchased_licenses = group['purchased_licenses']
                ret_dict['purchased_licenses'] = purchased_licenses
                continue

        return ret_dict

# ============================================================
# Parser for 'show diagnostics status '
# ============================================================ 

class ShowDiagnosticStatusSchema(MetaParser):
    """Schema for show diagnostics status"""

    schema = {
        'diagnostic_status':{
            'card': int,
            'description': str,
            'run_by': str
        },
        "current_running_test":{
          Any():{
            'run_by': str
          }
        }
    }

class ShowDiagnosticStatus(ShowDiagnosticStatusSchema):
    """Schema for show diagnostics status"""

    cli_command = 'show diagnostic status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        #1      C9300-24UX                        DiagThermalTest                 <HM>
        p1 = re.compile(r'^(?P<card>\d)+\s+(?P<description>\S+)+\s+\S+\s+.(?P<run_by>\w+).*$')

        # DiagFanTest                     <HM>
        p2 = re.compile(r"^(?P<current_running_test>\S+\s+)<HM>$")

        for line in output.splitlines():
            line = line.strip()

            #1      C9300-24UX                        DiagThermalTest                 <HM>
            m = p1.match(line)
            if m:
                group = m.groupdict()
                card  = int(group['card'])
                description = group['description']
                run = group['run_by']
                sub_dict = ret_dict.setdefault("diagnostic_status",{})
                sub_dict['card'] = card
                sub_dict['description'] = description
                sub_dict['run_by'] = run
                continue

            # DiagFanTest                     <HM>
            m = p2.match(line)
            if m:
                group = m.groupdict()
                current_running_test = group['current_running_test'].strip()
                tmp_dict = ret_dict.setdefault("current_running_test",{}).setdefault(current_running_test,{})
                tmp_dict['run_by'] = run
                continue

        return ret_dict

# ===========================================================================================
# Parser for 'show platform hardware fedswitch active fwd-asic resource asic all cpp-vbin all'
# ===========================================================================================

class ShowPlatformHardwareFedSwitchActiveFwdAsicResourceAsicAllCppVbinAllSchema(MetaParser):
    """show platform hardware fed switch active fwd-asic resource asic all cpp-vbin all"""

    schema={
       "asic":{
          Any():{
             "cpp_virtual_bin":{
                Any():{
                   "definition": ListOf(str)
                }
             }
          }
       }
    }

class ShowPlatformHardwareFedSwitchActiveFwdAsicResourceAsicAllCppVbinAll(ShowPlatformHardwareFedSwitchActiveFwdAsicResourceAsicAllCppVbinAllSchema):
    """show platform hardware fed switch active fwd-asic resource asic all cpp-vbin all"""

    cli_command = 'show platform hardware fed switch active fwd-asic resource asic all cpp-vbin all'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        #ASIC#0:
        p1=re.compile(r'^(?P<asic>ASIC.*)$')

        #CPP Virtual Bin (CPP_VBIN) [0]
        p2=re.compile(r'^(?P<cpp_virtual_bin>CPP.*)$')

        #virtualBin0 = 0x1
        p3=re.compile(r'^(?P<virtual>virtual+.*)$')

        for line in output.splitlines():
            line = line.strip()

            #ASIC#0:	
            m = p1.match(line)
            if m:
                group = m.groupdict()
                asic = group['asic']
                sub_dict = ret_dict.setdefault("asic",{}).setdefault(asic,{})
                continue

            #CPP Virtual Bin (CPP_VBIN) [0]		
            m = p2.match(line)
            if m:
                group = m.groupdict()
                cpp_virtual_bin = group['cpp_virtual_bin']
                sub_dict1 = sub_dict.setdefault('cpp_virtual_bin',{}).setdefault(cpp_virtual_bin,{})
                def_list = sub_dict1.setdefault('definition', [])
                continue

            #virtualBin0 = 0x1
            m = p3.match(line)
            if m and m.groupdict()['virtual'] != 'exit':
                def_list.append(m.groupdict()['virtual'])
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceSchema(MetaParser):
    """Schema for show platform hardware fed {switch} {switch_var} qos queue stats interface {interface}"""

    schema = {
        'interface': {
            Any(): {
                'voq_id': {
                    Any(): {
                        'packets': {
                            'enqueued': int,
                            'dropped': int,
                            'total': int
                        },
                        'bytes': {
                            'enqueued': int,
                            'dropped': int,
                            'total': int
                        },
                        'slice': {
                            Any(): {
                                'sms_bytes': int,
                                'hbm_blocks': int,
                                'hbm_bytes': int
                            }
                        }
                    }
                }
            }
        }
    }


class ShowPlatformHardwareFedSwitchQosQueueStatsInterface(ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceSchema):
    """Parser for show platform hardware fed {switch} {switch_var} qos queue stats interface {interface}"""

    cli_command = ['show platform hardware fed active qos queue stats interface {interface}',
        'show platform hardware fed switch {switch_num} qos queue stats interface {interface}']

    def cli(self, interface, switch_num=None, output=None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[1].format(switch_num=switch_num, interface=interface)
            else:
                cmd = self.cli_command[0].format(interface=interface)
            
            output = self.device.execute(cmd)

        # VOQ Stats For : HundredGigE1/0/5 [ 0x544 ]
        # VOQ Stats For : HundredGigE2/0/2.1 [ 0x550 ]
        p1 = re.compile(r'^VOQ Stats For : (?P<interface>[\w\/\.]+)\s+.*$')

        # 0      | Enqueued |                        1194566957 |                       78841419162 |
        # | Dropped  |                                 0 |                                 0 |
        # | Total    |                        1194566957 |                       78841419162 |
        # |----------|-----------------------------------------------------------------------|
        p2 = re.compile(r'^(?P<voq_id>\d+)?\s*\|\s+(?P<header>\w+)\s+\|\s+(?P<packets>\d+)\s+\|\s+(?P<bytes>\d+)\s+\|$')

        # |   Slice  |         0 |         1 |         2 |         3 |         4 |         5 |
        p3 = re.compile(r'^\|\s+Slice\s+\|\s+(?P<slice0>\d+)\s\|\s+(?P<slice1>\d+)\s\|\s+(?P<slice2>\d+)\s\|'
                    r'\s+(?P<slice3>\d+)\s\|\s+(?P<slice4>\d+)\s\|\s+(?P<slice5>\d+)\s\|$')
        
        # |SMS Bytes |         0 |         0 |         0 |         0 |         0 |         0 |
        p4 = re.compile(r'^\|\s*(?P<slice_type>SMS Bytes|HBM Blocks|HBM Bytes)\s*\|\s+(?P<slice0>\d+)\s\|\s+(?P<slice1>\d+)\s\|'
            r'\s+(?P<slice2>\d+)\s\|\s+(?P<slice3>\d+)\s\|\s+(?P<slice4>\d+)\s\|\s+(?P<slice5>\d+)\s\|$')
        
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # VOQ Stats For : HundredGigE1/0/5 [ 0x544 ]
            m = p1.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(m.groupdict()['interface']), {})
                continue
            
            # 0      | Enqueued |                        1194566957 |                       78841419162 |
            # | Dropped  |                                 0 |                                 0 |
            # | Total    |                        1194566957 |                       78841419162 |
            # |----------|-----------------------------------------------------------------------|
            m = p2.match(line)
            if m:
                res_dict = m.groupdict()
                if res_dict['voq_id']:
                    voq_dict = int_dict.setdefault('voq_id', {}).setdefault(res_dict['voq_id'], {})
                
                pkts_dict = voq_dict.setdefault('packets', {})
                bytes_dict = voq_dict.setdefault('bytes', {})
                pkts_dict.setdefault(res_dict['header'].lower(), int(res_dict['packets']))
                bytes_dict.setdefault(res_dict['header'].lower(), int(res_dict['bytes']))
                continue

            # |   Slice  |         0 |         1 |         2 |         3 |         4 |         5 |
            m = p3.match(line)
            if m:
                slice_dict = voq_dict.setdefault('slice', {})
                slice_dict0 = slice_dict.setdefault(m.groupdict()['slice0'], {})
                slice_dict1 = slice_dict.setdefault(m.groupdict()['slice1'], {})
                slice_dict2 = slice_dict.setdefault(m.groupdict()['slice2'], {})
                slice_dict3 = slice_dict.setdefault(m.groupdict()['slice3'], {})
                slice_dict4 = slice_dict.setdefault(m.groupdict()['slice4'], {})
                slice_dict5 = slice_dict.setdefault(m.groupdict()['slice5'], {})
                continue
            
            # |SMS Bytes |         0 |         0 |         0 |         0 |         0 |         0 |
            m = p4.match(line)
            if m:
                grp_output = m.groupdict()
                slice_type = grp_output['slice_type'].replace(' ', '_').lower()
                slice_dict0.setdefault(slice_type, int(grp_output['slice0']))
                slice_dict1.setdefault(slice_type, int(grp_output['slice1']))
                slice_dict2.setdefault(slice_type, int(grp_output['slice2']))
                slice_dict3.setdefault(slice_type, int(grp_output['slice3']))
                slice_dict4.setdefault(slice_type, int(grp_output['slice4']))
                slice_dict5.setdefault(slice_type, int(grp_output['slice5']))
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear(ShowPlatformHardwareFedSwitchQosQueueStatsInterface):
    """Parser for show platform hardware fed switch {switch} qos queue stats interface {interface} clear"""

    cli_command = ['show platform hardware fed active qos queue stats interface {interface} clear',
            'show platform hardware fed switch {switch_num} qos queue stats interface {interface} clear']

    def cli(self, interface, switch_num=None, output=None):

        return super().cli(interface=interface, switch_num=switch_num, output=output)


class ShowPlatformSoftwareFedMatmMactableVlanSchema(MetaParser):
    """Schema for show platform software fed {state} matm macTable vlan {vlan}"""

    schema = {
        "total_mac_address": int,
        "summary":{
            "total_secure_address": int,
            "total_drop_address": int,
            "total_lisp_local_address": int,
            "total_lisp_remote_address": int
        },
        "type":{
            Any(): str
        }
    }


class ShowPlatformSoftwareFedMatmMactableVlan(ShowPlatformSoftwareFedMatmMactableVlanSchema):
    """Parser for show platform software fed {state} matm macTable vlan {vlan}"""

    cli_command = ['show platform software fed {state} matm macTable vlan {vlan}',
                'show platform software fed {switch} {state} matm macTable vlan {vlan}']

    def cli(self, state, vlan, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch, state=state, vlan=vlan)
            else:
                cmd = self.cli_command[0].format(state=state, vlan=vlan)
            output = self.device.execute(cmd)

        # Total Mac number of addresses:: 34
        p1 = re.compile(r"^Total Mac number of addresses::\s+(?P<total_mac_address>\d+)$")

        # Total number of secure addresses:: 0 
        p2 = re.compile(r"^Total number of secure addresses::\s+(?P<total_secure_address>\d+)$")

        # Total number of drop addresses:: 0
        p3 = re.compile(r"^Total number of drop addresses::\s+(?P<total_drop_address>\d+)$")

        # Total number of lisp local addresses:: 0
        p4 = re.compile(r"^Total number of lisp local addresses::\s+(?P<total_lisp_local_address>\d+)$")

        # Total number of lisp remote addresses:: 0
        p5 = re.compile(r"^Total number of lisp remote addresses::\s+(?P<total_lisp_remote_address>\d+)$")

        # MAT_LISP_REMOTE_ADDR 0x1000000  MAT_VPLS_ADDR        0x2000000  MAT_LISP_GW_ADDR     0x4000000
        p6 = re.compile(r"(?P<key>[\w_\-]+)\s+(?P<value>[\w_\-]+)")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            
            # Total Mac number of addresses:: 34
            m = p1.match(line)
            if m:
                ret_dict['total_mac_address'] = int(m.groupdict()['total_mac_address'])
                continue

            # Total number of secure addresses:: 0 
            m = p2.match(line)
            if m:
                summary_dict = ret_dict.setdefault('summary', {})
                summary_dict['total_secure_address'] = int(m.groupdict()['total_secure_address'])
                continue

            # Total number of drop addresses:: 0
            m = p3.match(line)
            if m:
                summary_dict['total_drop_address'] = int(m.groupdict()['total_drop_address'])
                continue

            # Total number of lisp local addresses:: 0
            m = p4.match(line)
            if m:
                summary_dict['total_lisp_local_address'] = int(m.groupdict()['total_lisp_local_address'])
                continue

            # Total number of lisp remote addresses:: 0
            m = p5.match(line)
            if m:
                summary_dict['total_lisp_remote_address'] = int(m.groupdict()['total_lisp_remote_address'])
                continue

            # MAT_LISP_REMOTE_ADDR 0x1000000  MAT_VPLS_ADDR        0x2000000  MAT_LISP_GW_ADDR     0x4000000
            m = p6.finditer(line)
            if m:
                type_dict = ret_dict.setdefault('type', {})
                [type_dict.update({each_pair.groupdict()['key'].lower():each_pair.groupdict()['value']}) for each_pair in m]
                continue

        return ret_dict
