"""
IOSXE C9300 parsers for the following show commands:
    * show inventory
"""
# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, ListOf


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
                        'state': str,
                        Optional('pid'): str,
                        Optional('serial_number'): str,
                        'status': str,
                        Optional('system_power'): str,
                        Optional('poe_power'): str,
                        Optional('watts'): str
                    }
                },
                'system_temperature_state': str,
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

        # Switch 1 FAN 1 is OK
        p1 = re.compile(r'^Switch +(?P<switch>\d+) +FAN +(?P<fan>\d+) +is +(?P<state>[\w\s]+)$')

        # Switch 1 FAN 1 direction is Front to Back
        p1_1 = re.compile(r'^Switch +(?P<switch>\d+) +FAN +(?P<fan>\d+) +direction +is +(?P<direction>[\w\s]+)$')

        # Switch   FAN     Speed   State
        # ----------------------------------
        # 1        1       14240     OK
        p1_2 = re.compile(r'^(?P<switch>\d+)\s+(?P<fan>\d+)\s+(?P<speed>\d+)\s+(?P<state>[\w\s]+)$')

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
            m = p1_2.match(line)
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
                   'fru_authentication': str,
                   'stack_cable_a_authentication': str,
                   'stack_cable_b_authentication': str,
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
        for line in output.splitlines():
            line = line.strip()

            #Switch:1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                switch_dict = result_dict.setdefault('switch', {})
                switch_id_dict = switch_dict.setdefault(int(switch), {})

            #Mainboard Authentication:     Passed
            m = p2.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict['mainboard_authentication'] = group['mainboard_authentication']

            #FRU Authentication:           Not Available
            m = p3.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict['fru_authentication'] = group['fru_authentication']

            #Stack Cable A Authentication: Passed
            m = p4.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict['stack_cable_a_authentication'] = group['stack_cable_a_authentication']

            #Stack Cable B Authentication: Passed
            m = p5.match(line)
            if m:
                group = m.groupdict()
                switch_id_dict['stack_cable_b_authentication'] = group['stack_cable_b_authentication']
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

