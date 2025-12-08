''' show_hw.py
IOSXE parsers for the following show commands:
    * show hw module subslot {subslot} transceiver {transceiver} status
    * show hw-module slot {slot} port-group mode
    * show hw-module usbflash1 security status
    * show hw-module {filesystem} security-lock status
    * show hardware led port {port} {mode}
    * hw-module beacon RP {supervisor} status
    * hw-module beacon slot {slot_num} status
    * show hw-module subslot all oir
    * show hw-module subslot {subslot} entity
    * show hw-module subslot {slot} attribute
    * show platform hardware chassis rp {rp_state} fan-speed-control-data
    * hw-module beacon {switch} {switch_num} slot {slot_num} port {port_num} status
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or

# parser utils
from genie.libs.parser.utils.common import Common


# ==========================
# Schema for:
#  * 'show hw module subslot {subslot} transceiver {transceiver} status'
# ==========================
class ShowHwModuleStatusSchema(MetaParser):
    """Schema for show hw module subslot {subslot} transceiver {transceiver} status."""

    schema = {
    "transceiver_status": {
        "slot_id": int,
        "subslot": int,
        "port_id": int,
        "module_temperature": float,
        "supply_voltage_mVolts": float,
        "bias_current_uAmps": int,
        "tx_power_dBm": float,
        "optical_power_dBm": float
    }
}


# ==========================
# Parser for:
#  * 'show hw module subslot {subslot} transceiver {transceiver} status'
# ==========================
class ShowHwModuleStatus(ShowHwModuleStatusSchema):
    """Parser for show hw module subslot {subslot} transceiver {transceiver} status"""

    cli_command = 'show hw_module subslot {subslot} transceiver {transceiver} status'

    def cli(self, subslot="", transceiver="", output=None):
        if output is None:
            if subslot and transceiver:
                out = self.device.execute(self.cli_command).format(subslot=subslot, transceiver=transceiver)
            else:
                out = self.device.execute(self.cli_command)
        else:
            out = output

        p1 = re.compile(
            # The Transceiver in slot 2 subslot 1 port 1 is disabled.
            r"The\s+Transceiver\s+in\s+slot\s(?P<slot_id>\d+)"
            r"\s+subslot\s+(?P<subslot_id>\d+)"
            r"\s+port\s+(?P<port_id>\d+)\s+is\s+"
            r"(?P<status>(enabled|disabled))")
        #   Module temperature                        = +28.625 C
        p2 = re.compile(r"\s+(?P<module_temperature>\S+)\s+C")
        #   Transceiver Tx supply voltage             = 3252.5 mVolts
        p3 = re.compile(r"\s+(?P<supply_voltage_mVolts>\d+\.\d+)")
        #   Transceiver Tx bias current               = 6706 uAmps
        p4 = re.compile(r"\s+(?P<bias_current_uAmps>\d+)\s+uAmps")
        #   Transceiver Tx power                      = -2.7 dBm
        p5 = re.compile(r"\s+(?P<tx_power_dBm>\S+)\s+dBm")
        #   Transceiver Rx optical power              = -2.1 dBm
        p6 = re.compile(r"\s+(?P<optical_power_dBm>\S+)\s+dBm")

        # initial variables
        transceiver_dict = {}
        # The Transceiver in slot 2 subslot 1 port 1 is disabled.
        #   Module temperature                        = +28.625 C
        #   Transceiver Tx supply voltage             = 3252.5 mVolts
        #   Transceiver Tx bias current               = 6706 uAmps
        #   Transceiver Tx power                      = -2.7 dBm
        #   Transceiver Rx optical power              = -2.1 dBm

        regex_map = {
            "Module temperature": p2,
            "Transceiver Tx supply voltage": p3,
            "Transceiver Tx bias current": p4,
            "Transceiver Tx power": p5,
            "Transceiver Rx optical power": p6
        }

        for line in out.splitlines():
            line_strip = line.strip()
            if not line_strip.startswith("The Transceiver"):
                try:
                    data_type, value = line_strip.split('=', 1)
                    regex = regex_map.get(data_type.strip())
                except ValueError:
                    continue
            else:
                match = p1.match(line_strip)
                if match:
                    groups = match.groupdict()
                    slot_id = int(groups['slot_id'])
                    sub_slot = int(groups['subslot_id'])
                    port_id = int(groups['port_id'])
                    transceiver_dict.update(
                        {'transceiver_status': {'slot_id': slot_id, 'subslot': sub_slot, 'port_id': port_id}})
                continue
            if regex:
                match = regex.match((value))
                groups = match.groupdict()
                for k, v in groups.items():
                    if v is None:
                        continue
                    if v.isdigit():
                        v = int(v)
                    else:
                        try:
                            v = float(v)
                        except ValueError:
                            continue
                    transceiver_dict['transceiver_status'].update({k: v})
        if transceiver_dict:
            return transceiver_dict
        else:
            return {}
# ==================================================================================
#  Schema for 'show hardware led
# ==================================================================================

class ShowHardwareLedSchema(MetaParser):
    """
    Schema for show hardware led
    """
    schema = {
        Optional('current_mode'): str,
        Optional('led_auto_off'): str,
        Optional('led_hw_state'): str,
        Optional('switch'): {
            Any():{
                'system': str,
                Optional('beacon'): str,
                Optional('master'): str,
                Optional('port_led_status'):{
                    str: str
                    },
                Optional('port_duplex'): {
                    Any(): str
                },
                Optional('port_speed'): {
                    Any(): str,
                },
                Optional('stack_port'): {
                    Any(): str
                },
                Optional('poe_port'): {
                    Any(): str
                },
                'rj45_console':str,
                Optional('fantray_status'):{
                    int : str
                },
                Optional('power_supply_beacon_status'):{
                    int : str
                },
                Optional('system_psu'):str,
                Optional('system_fan'):str,
                Optional('stack_power'): str,
                Optional('xps'): str,
                Optional('usb_console'): str
            },
        },
        Optional('system'):str,
        Optional('status'):{
            str: str
        },
        Optional('number_of_ports_in_status'):str,
        Optional('express_setup'):str,
        Optional('dc_a'):str,
        Optional('dc_b'):str,
        Optional('alarm-out'):str,
        Optional('alarm-in1'):str,
        Optional('alarm-in2'):str,
        Optional('alarm-in3'):str,
        Optional('alarm-in4'):str
    }     
                       
class ShowHardwareLed(ShowHardwareLedSchema):
    """ Parser for show hardware led"""

    cli_command = ['show hardware led', 'show hardware led {stack} {switch_num}']
    
    def cli(self, stack=None, switch_num=None, output=None): 
        if output is None:
            if stack and switch_num:
                cmd = self.cli_command[1].format(stack=stack,switch_num=switch_num)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)
            
        # initial variables
        ret_dict = {}
        root_dict = ret_dict

        # SWITCH: 1
        p1 = re.compile(r'^SWITCH:\s+(?P<switch_num>\d+)$')

        # SYSTEM: GREEN
        p2 = re.compile(r'^SYSTEM:\s+(?P<system>\w+)$')

        # BEACON: OFF
        p3 = re.compile(r'^BEACON:\s+(?P<beacon>\w+)$')

        # PORT STATUS: (124) Hu1/0/1:GREEN Hu1/0/2:OFF Hu1/0/3:GREEN Hu1/0/4:OFF Hu1/0/5:OFF Hu1/0/6:GREEN Hu1/0/7:OFF Hu1/0/8:OFF Hu1/0/9:OFF Hu1/0/10:GREEN Hu1/0/11:GREEN Hu1/0/12:GREEN Hu1/0/13:GREEN Hu1/0/14:GREEN Fou1/0/15:GREEN Fou1/0/16:GREEN Fou1/0/17:GREEN Fou1/0/18:GREEN Fou1/0/19:GREEN Fou1/0/20:GREEN Fou1/0/21:GREEN Fou1/0/22:GREEN Hu1/0/23:GREEN Hu1/0/24:GREEN Hu1/0/25:OFF Hu1/0/26:GREEN Hu1/0/27:GREEN Hu1/0/28:GREEN Hu1/0/29:GREEN Hu1/0/30:GREEN Hu1/0/31:OFF Hu1/0/32:GREEN Hu1/0/33:GREEN Hu1/0/34:GREEN Hu1/0/35:GREEN Hu1/0/36:GREEN
        p4 = re.compile(r'^PORT STATUS:\s+\S+\s+(?P<led_ports>((\S+:\w+\s*))+)$')
        
        #STATUS: (28) Gi1/0/1:FLASH_GREEN Gi1/0/2:BLACK Gi1/0/3:BLACK Gi1/0/4:BLACK Gi1/0/5:FLASH_GREEN Gi1/0/6:FLASH_GREEN Gi1/0/7:FLASH_GREEN Gi1/0/8:FLASH_GREEN Gi1/0/9:BLACK Gi1/0/10:FLASH_GREEN Gi1/0/11:FLASH_GREEN Gi1/0/12:BLACK Gi1/0/13:BLACK Gi1/0/14:BLACK Gi1/0/15:BLACK Gi1/0/16:BLACK Gi1/0/17:BLACK Gi1/0/18:BLACK Gi1/0/19:BLACK Gi1/0/20:BLACK Gi1/0/21:BLACK Gi1/0/22:BLACK Gi1/0/23:FLASH_GREEN Gi1/0/24:FLASH_GREEN Gi1/0/25:BLACK Gi1/0/26:BLACK Gi1/0/27:BLACK Gi1/0/28:BLACK
        p4_1 = re.compile(r'^STATUS:\s+\((?P<port_nums_in_status>\d+)\)+\s+(?P<led_ports>((\S+:[\w-]+\s*))+)$')

        # RJ45 CONSOLE: GREEN
        p5 = re.compile(r'^RJ45 CONSOLE:\s+(?P<rj45_console>\w+)$')

        # FANTRAY 1 STATUS: GREEN
        p6 = re.compile(r'^FANTRAY\s+(?P<fantray_num>\d+)\s+STATUS:\s+(?P<fantray_status>\w+)$')

        # POWER-SUPPLY 1 BEACON: OFF
        p7 = re.compile(r'^POWER-SUPPLY\s+(?P<power_supply_num>\d+)\s+BEACON:\s+(?P<power_supply_status>\w+)$')
        
        #DC-A: GREEN
        p7_1 = re.compile(r'^DC-A:\s+(?P<dc_a>\w+)$')

        #DC-B: BLACK
        p7_2 = re.compile(r'^DC-B:\s+(?P<dc_b>\w+)$')

        # SYSTEM PSU: AMBER
        p8 = re.compile(r'^SYSTEM PSU:\s+(?P<system_psu>\w+)$')

        # SYSTEM FAN: GREEN
        p9 = re.compile(r'^SYSTEM FAN:\s+(?P<system_fan>\w+)$')

        #EXPRESS-SETUP: BLACK
        p10 = re.compile(r'^EXPRESS-SETUP:\s+(?P<express_setup>\w+)$')

        # ALARM-OUT: GREEN
        # ALARM-IN1: GREEN
        # ALARM-IN2: GREEN
        p11 = re.compile(r'^(?P<alarm>ALARM\-\w+):\s+(?P<alarm_color>\w+)$')

        # Current Mode: STATUS
        p12 = re.compile(r'^Current Mode:\s+(?P<status>\w+)$')

        # LED Auto off: Disabled // this output changed as below and new line added for hardware state.
        # LED auto-off: Enabled
        p12_1 = re.compile(r'^LED auto-off:\s+(?P<auto_off>\w+)$')

        # LED Hardware State: OFF
        p12_2 = re.compile(r'^LED Hardware State:\s+(?P<hw_state>\w+)$')



        # MASTER: GREEN
        p13 = re.compile(r'^MASTER:\s+(?P<master>\w+)$')

        # DUPLEX: (65) Tw1/0/1:BLACK Tw1/0/2:BLACK Tw1/0/3:BLACK 
        # Tw1/0/4:GREEN Tw1/0/5:BLACK Tw1/0/6:BLACK Tw1/0/7:BLACK
        p14 = re.compile(r'^DUPLEX:\s+\S+\s+(?P<duplex>((\S+:\S+\s*))+)$')

        # SPEED: (65) Tw1/0/1:BLACK Tw1/0/2:BLACK Tw1/0/3:BLACK 
        # Tw1/0/4:BLINK_GREEN Tw1/0/5:BLACK Tw1/0/6:BLACK Tw1/0/7:BLACK
        p15 = re.compile(r'^SPEED:\s+\S+\s+(?P<speed>((\S+:\S+\s*))+)$')

        # STACK: (65) Tw1/0/1:FLASH_GREEN Tw1/0/2:BLACK Tw1/0/3:BLACK
        # Tw1/0/4:BLACK Tw1/0/5:BLACK Tw1/0/6:BLACK Tw1/0/7:BLACK Tw1/0/8:BLACK
        p16 = re.compile(r'^STACK:\s+\S+\s+(?P<stack_port>((\S+:\S+\s*))+)$')

        # POE: (65) Tw1/0/1:BLACK Tw1/0/2:BLACK Tw1/0/3:BLACK Tw1/0/4:BLACK
        # Tw1/0/5:BLACK Tw1/0/6:BLACK Tw1/0/7:BLACK Tw1/0/8:BLACK Tw1/0/9:BLACK
        p17 = re.compile(r'^POE:\s+\S+\s+(?P<poe>((\S+:\S+\s*))+)$')

        # STACK POWER: BLACK
        p18 = re.compile(r'^STACK POWER:\s+(?P<stack_power>\w+)$')

        # XPS: BLACK
        p19 = re.compile(r'^XPS:\s+(?P<xps>\w+)$')

        # USB CONSOLE: BLACK
        p20 = re.compile(r'^USB CONSOLE:\s+(?P<usb_console>\w+)$')

        for line in output.splitlines():
            line = line.strip()
            
            # SWITCH: 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('switch',{}).setdefault(int(group['switch_num']),{})
                continue
            
            # SYSTEM: GREEN
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict.update({'system' : group['system']})
                continue
            
            # BEACON: OFF
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict.update({'beacon' : group['beacon']})
                continue

            # PORT STATUS: (124) Hu1/0/1:GREEN Hu1/0/2:OFF Hu1/0/3:GREEN Hu1/0/4:OFF Hu1/0/5:OFF Hu1/0/6:GREEN Hu1/0/7:OFF Hu1/0/8:OFF Hu1/0/9:OFF Hu1/0/10:GREEN Hu1/0/11:GREEN Hu1/0/12:GREEN Hu1/0/13:GREEN Hu1/0/14:GREEN Fou1/0/15:GREEN Fou1/0/16:GREEN Fou1/0/17:GREEN Fou1/0/18:GREEN Fou1/0/19:GREEN Fou1/0/20:GREEN Fou1/0/21:GREEN Fou1/0/22:GREEN Hu1/0/23:GREEN Hu1/0/24:GREEN Hu1/0/25:OFF Hu1/0/26:GREEN Hu1/0/27:GREEN Hu1/0/28:GREEN Hu1/0/29:GREEN Hu1/0/30:GREEN Hu1/0/31:OFF Hu1/0/32:GREEN Hu1/0/33:GREEN Hu1/0/34:GREEN Hu1/0/35:GREEN Hu1/0/36:GREEN       
            m = p4.match(line)
            if m:
                group = m.groupdict()
                for port in group['led_ports'].split():
                    port = (port.split(':'))
                    port_led_dict = root_dict.setdefault('port_led_status',{})
                    port_led_dict.update({Common.convert_intf_name(port[0]): port[1]})
                continue
            
            # STATUS: (10) Gi1/1:BLINK_GREEN-BLACK Gi1/2:BLACK-BLINK_AMBER Gi1/3:BLACK Gi1/4:BLINK_AMBER Gi1/5:BLINK_AMBER Gi1/6:BLINK_AMBER Gi1/7:BLINK_AMBER Gi1/8:BLINK_AMBER Gi1/9:BLINK_AMBER Gi1/10:BLINK_GREEN
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'number_of_ports_in_status' : group['port_nums_in_status']})
                for port in group['led_ports'].split():
                    port = (port.split(':'))
                    port_led_dict = ret_dict.setdefault('status',{})
                    port_led_dict.update({Common.convert_intf_name(port[0]): port[1]})
                continue
            
            # STATUS: (10) Gi1/1:BLINK_GREEN-BLACK Gi1/2:BLACK-BLINK_AMBER Gi1/3:BLACK Gi1/4:BLINK_AMBER Gi1/5:BLINK_AMBER Gi1/6:BLINK_AMBER Gi1/7:BLINK_AMBER Gi1/8:BLINK_AMBER Gi1/9:BLINK_AMBER Gi1/10:BLINK_GREEN
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'number_of_ports_in_status' : group['port_nums_in_status']})
                for port in group['led_ports'].split():
                    port = (port.split(':'))
                    port_led_dict = ret_dict.setdefault('status',{})
                    port_led_dict.update({port[0]: port[1]})
                continue

            # RJ45 CONSOLE: GREEN
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict.update({'rj45_console' : group['rj45_console']})
                continue

            # FANTRAY 1 STATUS: GREEN
            m = p6.match(line)
            if m:
                group = m.groupdict()
                fantray_dict= root_dict.setdefault('fantray_status',{})
                fantray_dict.setdefault(int(group['fantray_num']),group['fantray_status'])
                continue

            # POWER-SUPPLY 1 BEACON: OFF
            m = p7.match(line)
            if m:
                group = m.groupdict()
                power_supply_dict= root_dict.setdefault('power_supply_beacon_status',{})
                power_supply_dict.setdefault(int(group['power_supply_num']),group['power_supply_status'])
                continue
            
            #DC-A: GREEN
            m = p7_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'dc_a': group['dc_a']})

            #DC-B: BLACK
            m = p7_2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'dc_b': group['dc_b']})

            # SYSTEM PSU: AMBER
            m = p8.match(line)
            if m:
                group = m.groupdict()
                root_dict.update({'system_psu' : group['system_psu']})
                continue

            # SYSTEM FAN: GREEN
            m = p9.match(line)
            if m:
                group = m.groupdict()
                root_dict.update({'system_fan' : group['system_fan']})
                continue
            
            #EXPRESS-SETUP: BLACK
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'express_setup' : group['express_setup']})
                continue

            #ALARM-OUT: GREEN
            #ALARM-IN1: GREEN
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({group['alarm'].lower() : group['alarm_color']})
            
            # Current Mode: STATUS
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'current_mode' : group['status']})
                continue

            # LED Auto off: Disabled
            m = p12_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'led_auto_off' : group['auto_off']})
                continue

            # LED Hardware State: OFF
            m = p12_2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'led_hw_state' : group['hw_state']})
                continue

            # MASTER: GREEN
            m = p13.match(line)
            if m:
                group = m.groupdict()
                root_dict.update({'master' : group['master']})
                continue

            # DUPLEX: (65) Tw1/0/1:BLACK Tw1/0/2:BLACK Tw1/0/3:BLACK 
            # Tw1/0/4:GREEN Tw1/0/5:BLACK Tw1/0/6:BLACK Tw1/0/7:BLACK
            m = p14.match(line)
            if m:
                group = m.groupdict()
                # root_dict = ret_dict.setdefault('switch',{}).setdefault(int(group['switch_num']),{})
                for port in group['duplex'].split():
                    port = (port.split(':'))
                    port_duplex_dict = root_dict.setdefault('port_duplex', {})
                    port_duplex_dict.update({Common.convert_intf_name(port[0]): port[1]})
                continue

            # SPEED: (65) Tw1/0/1:BLACK Tw1/0/2:BLACK Tw1/0/3:BLACK 
            # Tw1/0/4:BLINK_GREEN Tw1/0/5:BLACK Tw1/0/6:BLACK Tw1/0/7:BLACK
            m = p15.match(line)
            if m:
                group = m.groupdict()
                for port in group['speed'].split():
                    port = (port.split(':'))
                    speed_dict = root_dict.setdefault('port_speed', {})
                    speed_dict.update({Common.convert_intf_name(port[0]): port[1]})
                continue

            # STACK: (65) Tw1/0/1:FLASH_GREEN Tw1/0/2:BLACK Tw1/0/3:BLACK
            # Tw1/0/4:BLACK Tw1/0/5:BLACK Tw1/0/6:BLACK Tw1/0/7:BLACK Tw1/0/8:BLACK
            m = p16.match(line)
            if m:
                group = m.groupdict()
                for port in group['stack_port'].split():
                    port = (port.split(':'))
                    stack_dict = root_dict.setdefault('stack_port', {})
                    stack_dict.update({Common.convert_intf_name(port[0]): port[1]})
                continue

            # POE: (65) Tw1/0/1:BLACK Tw1/0/2:BLACK Tw1/0/3:BLACK Tw1/0/4:BLACK
            # Tw1/0/5:BLACK Tw1/0/6:BLACK Tw1/0/7:BLACK Tw1/0/8:BLACK Tw1/0/9:BLACK
            m = p17.match(line)
            if m:
                group = m.groupdict()
                for port in group['poe'].split():
                    port = (port.split(':'))
                    poe_dict = root_dict.setdefault('poe_port', {})
                    poe_dict.update({Common.convert_intf_name(port[0]): port[1]})
                continue

            # STACK POWER: BLACK
            m = p18.match(line)
            if m:
                group = m.groupdict()
                root_dict.update({'stack_power': group['stack_power']})
                continue

            # XPS: BLACK
            m = p19.match(line)
            if m:
                group = m.groupdict()
                root_dict.update({'xps': group['xps']})
                continue

            # USB CONSOLE: BLACK
            m = p20.match(line)
            if m:
                group = m.groupdict()
                root_dict.update({'usb_console': group['usb_console']})
                continue
        return ret_dict



class ShowHardwareLedPortSchema(MetaParser):
    """
    Schema for show hardware led port {port}
    """
    schema = {
        'port_led_status' : {
            str : str
           }
        }

class ShowHardwareLedPort(ShowHardwareLedPortSchema):
    """ Parser for show hardware led port {port}"""

    cli_command = "show hardware led port {port}"
    
    def cli(self,port,output=None): 
        if output is None:
            output = self.device.execute(self.cli_command.format(port=port))

        # initial variables
        ret_dict = {}
        
        # GREEN
        p1 = re.compile(r'^(?P<port_status>\w+)$')

        for line in output.splitlines():
            line = line.strip()
            
            # GREEN
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('port_led_status',{})
                root_dict.update({port : group['port_status']})
                continue
                
        return ret_dict

# ==================================================================================
#  Schema for 'show hw-module slot {slot} port-group mode'
# ==================================================================================
class ShowHwModuleSlotPortGroupModeSchema(MetaParser):
    """Schema for show hw-module slot {slot} port-group mode"""
    schema = {
        'slot':{
                int:{
                    'port_group':{
                        int:{
                            Optional('port'):{
                                Any():{
                                    'mode':str,
                                }
                            }
                        }
                    }    
                }
            }
        }

# ==================================================================================
#  Parser for 'show hw-module slot {slot} port-group mode'
# ==================================================================================
class ShowHwModuleSlotPortGroupMode(ShowHwModuleSlotPortGroupModeSchema):
    """ Parser for show hw-module slot {slot} port-group mode"""

    cli_command = "show hw-module slot {slot} port-group mode"

    def cli(self, slot=None , output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(slot=slot))
            
        ret_dict = {}

        #   2         1              Hu2/0/25            inactive
        p1 = re.compile(r'^(?P<slot>\d+) +(?P<port_group>\d+) +(?P<port>\S+) +(?P<mode>(inactive|400G|100G))$')
        #                             Hu2/0/26            inactive
        #                             Hu2/0/27            400G
        #                             Hu2/0/28            inactive
        p2 = re.compile(r'^(?P<port>\S+) +(?P<mode>(inactive|400G|100G))$')

        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
               group = m.groupdict()
               slot_dict = ret_dict.setdefault('slot',{})  
               slot_id_dict = slot_dict.setdefault(int(group['slot']),{})
               port_group_dict = slot_id_dict.setdefault('port_group',{})
               port_group_id_dict = port_group_dict.setdefault(int(group['port_group']),{})
               port_dict = port_group_id_dict.setdefault('port',{})
               port_id_dict = port_dict.setdefault(str(group['port']),{})
               port_id_dict.update({  
                    'mode' : str(group['mode']),
                })
               continue
            m = p2.match(line)
            if m:
                group = m.groupdict()
                port_id_dict = port_dict.setdefault(str(group['port']),{})
                port_id_dict.update({  
                    'mode' : str(group['mode']),
                })
                continue
        return ret_dict


class ShowHwModuleUsbflash1SecuritySchema(MetaParser):
    '''Schema for show hw-module usbflash1 security status'''
    schema = {
        'switch': {
            Any(): {
                'auth_status': str
            }
        }
    }


class ShowHwModuleUsbflash1Security(ShowHwModuleUsbflash1SecuritySchema):
    '''Parser for show hw-module usbflash1 security status'''

    cli_command = ['show hw-module usbflash1 switch {switch_num} security status', 'show hw-module usbflash1 security status']

    def cli(self, switch_num='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0].format(switch_num = switch_num) if switch_num else self.cli_command[1])
        
        # 1                    USB Not Present
        # 2                    USB Not Present
        # 3                    USB Not Present
        p1 = re.compile(r'^(?P<switch>\d+)\s+(?P<auth_status>.+)$')

        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            # 1                    USB Not Present
            m = p1.match(line)
            if m:
                ret_dict.setdefault('switch', {}).setdefault(m.groupdict()['switch'], {'auth_status': m.groupdict()['auth_status']})
                continue
        
        return ret_dict

# ==================================================================================
#  Schema for 'show hw-module {filesystem} security-lock status'
# ==================================================================================
class ShowHwModuleSecurityLockStatusSchema(MetaParser):
    """Schema for show hw-module {filesystem} security-lock status"""
    schema = {
            Optional('err_msg'): str,
            Optional('drive_support'):bool,
            Optional('lock_enabled'):bool,
            Optional('lock_status'):bool,
            Optional('partitioned'):bool,
            Optional('tam_object'):bool
        }

# ==================================================================================
#  Parser for 'show hw-module {filesystem} security-lock status'
# ==================================================================================
class ShowHwModuleSecurityLockStatus(ShowHwModuleSecurityLockStatusSchema):
    """Schema for show hw-module {filesystem} security-lock status"""

    cli_command = 'show hw-module {filesystem} security-lock status'

    def cli(self, filesystem, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(filesystem=filesystem))

        # Initial Variables
        ret_dict = {}

        # Drive Supported: Yes, Locking Enabled: Yes, Locked: No, Partitioned: Yes, TAM Object: Yes
        p1 = re.compile(
                r"^Drive Supported:\s+(?P<drive_support>\w+),\s+"
                r"Locking Enabled:\s+(?P<lock_enabled>\w+),\s+"
                r"Locked:\s+(?P<lock_status>\w+),\s+"
                r"Partitioned:\s+(?P<partitioned>\w+),\s+"
                r"TAM\s+Object:\s+(?P<tam_object>\w+)$")

        # Any error message with spaces like
        # DEVICE NOT SUPPORTED
        p2 = re.compile(r"^[a-zA-Z0-9_ ]+$")

        for line in output.splitlines():
            line = line.strip()

            # Drive Supported: Yes, Locking Enabled: Yes, Locked: No, Partitioned: Yes, TAM Object: Yes
            m = p1.match(line)
            if m:
                for key, val in m.groupdict().items():
                    ret_dict[key] = True if val == "Yes" else False;
                continue

            # Any error message with spaces like
            # DEVICE NOT SUPPORTED
            m = p2.match(line)
            if m:
                ret_dict['err_msg'] = line
                continue

        return ret_dict

class ShowHardwareLedPortModeSchema(MetaParser):
    """
    Schema for show hardware led port {port} {mode}
    """
    schema = {
        Optional('current_mode'): str,
        'status': str
    }

class ShowHardwareLedPortMode(ShowHardwareLedPortModeSchema):
    """Parser for show hardware led port {port} {mode}"""

    cli_command = "show hardware led port {port} {mode}"
    
    def cli(self, port, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(port=port, mode=mode))

        # Current Mode: STATUS
        p1 = re.compile(r'^Current Mode: (?P<current_mode>[\w\s]+)$')

        # BLINK_GREEN
        p2 = re.compile(r'^(?P<status>\w+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            
            # Current Mode: STATUS
            m = p1.match(line)
            if m:
                ret_dict['current_mode'] = m.groupdict()['current_mode']
                continue

            # BLINK_GREEN
            m = p2.match(line)
            if m:
                ret_dict['status'] = m.groupdict()['status']
                continue
  
        return ret_dict


class HardwareModuleBeaconFanTrayStatusSchema(MetaParser):
    """
    Schema for hw-module beacon fan-tray status
    """
    schema = {
        'fantray_beacon_led': str
    }

class HardwareModuleBeaconFanTrayStatus(HardwareModuleBeaconFanTrayStatusSchema):
    """Parser for hw-module beacon fan-tray status"""

    cli_command = "hw-module beacon fan-tray status"
    
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Fantray Beacon LED: OFF
        p1 = re.compile(r'^Fantray Beacon LED: (?P<fantray_beacon_led>\w+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            
            # Fantray Beacon LED: OFF
            m = p1.match(line)
            if m:
                ret_dict['fantray_beacon_led'] = m.groupdict()['fantray_beacon_led']
                continue
  
        return ret_dict


class HardwareModuleBeaconSlotStatusSchema(MetaParser):
    """
    Schema for hw-module beacon slot {slot_num} status
    """
    schema = {
        'slot_status': str
    }

class HardwareModuleBeaconSlotStatus(HardwareModuleBeaconSlotStatusSchema):
    """Parser for hw-module beacon slot {slot_num} status"""

    cli_command = ["hw-module beacon slot {slot_num} status", "hw-module beacon RP {supervisor} status"]
    
    def cli(self, slot_num=None, supervisor=None, output=None):
        if output is None:
            if slot_num:
                output = self.device.execute(self.cli_command[0].format(slot_num=slot_num))
            else:
                output = self.device.execute(self.cli_command[1].format(supervisor=supervisor))

        # BLACK
        # SOLID BLUE
        p1 = re.compile(r'^(?P<slot_status>[\w\s]+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            
            # BLACK
            m = p1.match(line)
            if m:
                ret_dict['slot_status'] = m.groupdict()['slot_status']
                continue
  
        return ret_dict

class ShowHwModuleSubslotOirSchema(MetaParser):
    """Schema for show hw-module subslot {slot} oir"""
    schema = {
        'subslots': {
            str: {
                'model': str,
                'operational_status': str,
            }
        }
    }

class ShowHwModuleSubslotOir(ShowHwModuleSubslotOirSchema):
    """Parser for show hw-module subslot {slot} oir"""

    cli_command = 'show hw-module subslot {slot} oir'

    def cli(self, slot='', output=None):
        if output is None:
            # Execute the command on the device
            output = self.device.execute(self.cli_command.format(slot=slot))

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Define the regular expression pattern to match each line of the output
        # subslot 0/0             ISR4451-X-4x1GE      ok 
        p0 = re.compile(r'^subslot\s+(?P<subslot>\S+)\s+(?P<model>\S+)\s+(?P<operational_status>\S+)$')

        # Iterate over each line in the output
        for line in output.splitlines():
            line = line.strip()
            # subslot 0/0             ISR4451-X-4x1GE      ok
            if not line:
                continue

            # subslot 0/0             ISR4451-X-4x1GE      ok
            m = p0.match(line)
            if m:
                # Extract the matched groups
                subslot = m.group('subslot')
                model = m.group('model')
                operational_status = m.group('operational_status')

                # Use setdefault to avoid key errors
                subslot_dict = parsed_dict.setdefault('subslots', {}).setdefault(subslot, {})
                subslot_dict['model'] = model
                subslot_dict['operational_status'] = operational_status

        return parsed_dict

# ==========================
# Schema for:
#  * 'show hw-module subslot {subslot} entity'
# ==========================
class ShowHwModuleSubslotEntitySchema(MetaParser):
    """Schema for show hw-module subslot {subslot} entity"""

    schema = {
        'entity_state': {
            'subslot': str,
            'spa_type': str,
            'spa_type_hex': str,
            'last_spa_type': str,
            'last_spa_type_hex': str,
            'oper_status': str,
            'oper_status_code': int,
            'card_status': str,
            'card_status_code': int,
            'last_trap_spa_type': str,
            'last_trap_spa_type_hex': str,
            'last_trap_oper_status': str,
            'last_trap_oper_status_code': int,
            'last_spa_env_get_ok': bool,
            'last_spa_env_read_time': int,
            'last_spa_env_read_time_str': str,
            'resync_reqd': bool,
            'resync_count': int,
            'spa_physical_index': int,
            'spa_container_index': int,
            Optional('transceiver'): {
                Any(): {
                    'container_index': int,
                    Optional('module_entity_index'): int,
                    Optional('port_index'): int,
                    'chassis_index': int,
                    'operational_status': str,
                    'operational_status_code': int,
                    Optional('non_zero_xcvr_sensors'): {
                        Any(): int,
                    },
                },
            },
            Optional('non_zero_spa_temp_sensors'): {
                Any(): int,
            },
            Optional('non_zero_spa_volt_sensors'): {
                Any(): int,
            },
            Optional('non_zero_spa_power_sensors'): str,
        },
    }


# ==========================
# Parser for:
#  * 'show hw-module subslot {subslot} entity'
# ==========================
class ShowHwModuleSubslotEntity(ShowHwModuleSubslotEntitySchema):
    """Parser for show hw-module subslot {subslot} entity"""

    cli_command = 'show hw-module subslot {subslot} entity'

    def cli(self, subslot='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(subslot=subslot))

        # Initial variables
        ret_dict = {}
        current_transceiver = None
        current_transceiver_dict = None

        # Entity state for SPA in subslot 0/1
        p1 = re.compile(r'^Entity\s+state\s+for\s+SPA\s+in\s+subslot\s+(?P<subslot>\S+)$')

        # SPA type:                 (0xC55) EPA-18X1GE
        p2 = re.compile(r'^SPA\s+type:\s+\((?P<hex>0x\w+)\)\s+(?P<type>\S+)$')

        # last spa type:            (0xC55) EPA-18X1GE
        p3 = re.compile(r'^last\s+spa\s+type:\s+\((?P<hex>0x\w+)\)\s+(?P<type>\S+)$')

        # oper_status:              (1) ok
        p4 = re.compile(r'^oper_status:\s+\((?P<code>\d+)\)\s+(?P<status>\S+)$')

        # card status:              (2) full
        p5 = re.compile(r'^card\s+status:\s+\((?P<code>\d+)\)\s+(?P<status>\S+)$')

        # last trap: spa type:      (0xC55) EPA-18X1GE
        p6 = re.compile(r'^last\s+trap:\s+spa\s+type:\s+\((?P<hex>0x\w+)\)\s+(?P<type>\S+)$')

        # last trap: oper status:   (1) ok
        p7 = re.compile(r'^last\s+trap:\s+oper\s+status:\s+\((?P<code>\d+)\)\s+(?P<status>\S+)$')

        # last_spa_env_get_ok:      false
        p8 = re.compile(r'^last_spa_env_get_ok:\s+(?P<status>true|false)$')

        # last_spa_env_read_time:   (0) 145245938 msecs ago
        p9 = re.compile(r'^last_spa_env_read_time:\s+\((?P<value>\d+)\)\s+(?P<time>\d+)\s+msecs\s+ago$')

        # resync_reqd:              false
        p10 = re.compile(r'^resync_reqd:\s+(?P<status>true|false)$')

        # resync_count:             0
        p11 = re.compile(r'^resync_count:\s+(?P<count>\d+)$')

        # SPA physical index:       1520
        p12 = re.compile(r'^SPA\s+physical\s+index:\s+(?P<index>\d+)$')

        # SPA container index:      1028
        p13 = re.compile(r'^SPA\s+container\s+index:\s+(?P<index>\d+)$')

        # transceiver 0
        p14 = re.compile(r'^transceiver\s+(?P<transceiver>\d+)$')

        #   container index:        1571
        p15 = re.compile(r'^container\s+index:\s+(?P<index>\d+)$')

        #   module entity index:    1572
        p16 = re.compile(r'^\s+module\s+entity\s+index:\s+(?P<index>\d+)$')

        #   port index:             1573
        p17 = re.compile(r'^\s+port\s+index:\s+(?P<index>\d+)$')

        #   chassis index:          0
        p18 = re.compile(r'^chassis\s+index:\s+(?P<index>\d+)$')

        #   operational status:     (2) ok
        p19 = re.compile(r'^operational\s+status:\s+\((?P<code>\d+)\)\s+(?P<status>\S+)$')

        #   non-zero xcvr sensors:
        p20 = re.compile(r'^\s+non-zero\s+xcvr\s+sensors:$')

        #     sensor 0:     1599
        p21 = re.compile(r'^\s+sensor\s+(?P<sensor>\d+):\s+(?P<index>\d+)$')

        # non-zero SPA temp sensors:
        p22 = re.compile(r'^non-zero\s+SPA\s+temp\s+sensors:$')

        # sensor 0 has index 1546
        p23 = re.compile(r'^sensor\s+(?P<sensor>\d+)\s+has\s+index\s+(?P<index>\d+)$')

        # non-zero SPA volt sensors:
        p24 = re.compile(r'^non-zero\s+SPA\s+volt\s+sensors:$')

        # non-zero SPA power sensors:
        p25 = re.compile(r'^non-zero\s+SPA\s+power\s+sensors:$')

        # all power sensor indices are zero
        p26 = re.compile(r'^all\s+power\s+sensor\s+indices\s+are\s+zero$')

        current_section = None

        for line in output.splitlines():
            line = line.strip()

            # Entity state for SPA in subslot 0/1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                entity_dict = ret_dict.setdefault('entity_state', {})
                entity_dict['subslot'] = group['subslot']
                continue

            # SPA type:                 (0xC55) EPA-18X1GE
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entity_dict['spa_type'] = group['type']
                entity_dict['spa_type_hex'] = group['hex']
                continue

            # last spa type:            (0xC55) EPA-18X1GE
            m = p3.match(line)
            if m:
                group = m.groupdict()
                entity_dict['last_spa_type'] = group['type']
                entity_dict['last_spa_type_hex'] = group['hex']
                continue

            # oper_status:              (1) ok
            m = p4.match(line)
            if m:
                group = m.groupdict()
                entity_dict['oper_status'] = group['status']
                entity_dict['oper_status_code'] = int(group['code'])
                continue

            # card status:              (2) full
            m = p5.match(line)
            if m:
                group = m.groupdict()
                entity_dict['card_status'] = group['status']
                entity_dict['card_status_code'] = int(group['code'])
                continue

            # last trap: spa type:      (0xC55) EPA-18X1GE
            m = p6.match(line)
            if m:
                group = m.groupdict()
                entity_dict['last_trap_spa_type'] = group['type']
                entity_dict['last_trap_spa_type_hex'] = group['hex']
                continue

            # last trap: oper status:   (1) ok
            m = p7.match(line)
            if m:
                group = m.groupdict()
                entity_dict['last_trap_oper_status'] = group['status']
                entity_dict['last_trap_oper_status_code'] = int(group['code'])
                continue

            # last_spa_env_get_ok:      false
            m = p8.match(line)
            if m:
                group = m.groupdict()
                entity_dict['last_spa_env_get_ok'] = group['status'] == 'true'
                continue

            # last_spa_env_read_time:   (0) 145245938 msecs ago
            m = p9.match(line)
            if m:
                group = m.groupdict()
                entity_dict['last_spa_env_read_time'] = int(group['time'])
                entity_dict['last_spa_env_read_time_str'] = f"({group['value']}) {group['time']} msecs ago"
                continue

            # resync_reqd:              false
            m = p10.match(line)
            if m:
                group = m.groupdict()
                entity_dict['resync_reqd'] = group['status'] == 'true'
                continue

            # resync_count:             0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                entity_dict['resync_count'] = int(group['count'])
                continue

            # SPA physical index:       1520
            m = p12.match(line)
            if m:
                group = m.groupdict()
                entity_dict['spa_physical_index'] = int(group['index'])
                continue

            # SPA container index:      1028
            m = p13.match(line)
            if m:
                group = m.groupdict()
                entity_dict['spa_container_index'] = int(group['index'])
                continue

            # transceiver 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                current_transceiver = group['transceiver']
                current_section = 'transceiver'
                if 'transceiver' not in entity_dict:
                    entity_dict['transceiver'] = {}
                entity_dict['transceiver'][current_transceiver] = {}
                current_transceiver_dict = entity_dict['transceiver'][current_transceiver]
                continue

            # For transceiver section
            if current_section == 'transceiver' and current_transceiver_dict is not None:
                #   container index:        1571
                m = p15.match(line)
                if m:
                    group = m.groupdict()
                    current_transceiver_dict['container_index'] = int(group['index'])
                    continue

                #   module entity index:    1572
                m = p16.match(line)
                if m:
                    group = m.groupdict()
                    index = int(group['index'])
                    if index != 0:  # Only include non-zero values
                        current_transceiver_dict['module_entity_index'] = index
                    continue

                #   port index:             1573
                m = p17.match(line)
                if m:
                    group = m.groupdict()
                    index = int(group['index'])
                    if index != 0:  # Only include non-zero values
                        current_transceiver_dict['port_index'] = index
                    continue

                #   chassis index:          0
                m = p18.match(line)
                if m:
                    group = m.groupdict()
                    current_transceiver_dict['chassis_index'] = int(group['index'])
                    continue

                #   operational status:     (2) ok
                m = p19.match(line)
                if m:
                    group = m.groupdict()
                    current_transceiver_dict['operational_status'] = group['status']
                    current_transceiver_dict['operational_status_code'] = int(group['code'])
                    continue

                #   non-zero xcvr sensors:
                m = p20.match(line)
                if m:
                    # This line indicates start of sensor section
                    continue

                #     sensor 0:     1599
                m = p21.match(line)
                if m:
                    group = m.groupdict()
                    if 'non_zero_xcvr_sensors' not in current_transceiver_dict:
                        current_transceiver_dict['non_zero_xcvr_sensors'] = {}
                    current_transceiver_dict['non_zero_xcvr_sensors'][group['sensor']] = int(group['index'])
                    continue

            # non-zero SPA temp sensors:
            m = p22.match(line)
            if m:
                current_section = 'temp_sensors'
                continue

            # non-zero SPA volt sensors:
            m = p24.match(line)
            if m:
                current_section = 'volt_sensors'
                continue

            # non-zero SPA power sensors:
            m = p25.match(line)
            if m:
                current_section = 'power_sensors'
                continue

            # all power sensor indices are zero
            m = p26.match(line)
            if m:
                entity_dict['non_zero_spa_power_sensors'] = 'all power sensor indices are zero'
                current_section = None
                continue

            # sensor 0 has index 1546
            m = p23.match(line)
            if m:
                group = m.groupdict()
                if current_section == 'temp_sensors':
                    if 'non_zero_spa_temp_sensors' not in entity_dict:
                        entity_dict['non_zero_spa_temp_sensors'] = {}
                    entity_dict['non_zero_spa_temp_sensors'][group['sensor']] = int(group['index'])
                elif current_section == 'volt_sensors':
                    if 'non_zero_spa_volt_sensors' not in entity_dict:
                        entity_dict['non_zero_spa_volt_sensors'] = {}
                    entity_dict['non_zero_spa_volt_sensors'][group['sensor']] = int(group['index'])
                continue

        return ret_dict

# ==========================
# Schema for:
#  * 'show hw-module subslot {slot} attribute'
# ==========================
class ShowHwModuleSubslotAttributeSchema(MetaParser):
    """Schema for show hw-module subslot {slot} attribute"""

    schema = {
        'slot': {
            int: {
                'bay': int,
                'board': int,
                'module': str,
                'spa_type': str,
                'spa_type_hex': str,
                'daughter_board_present': bool,
                'base_mac_addr': str,
                'mac_blk_sz': int,
                'endpt_mac_address_offset': str,
                'basic_attributes': {
                    'length': int,
                    'version': str,
                    'module_type': str,
                    'width': str,
                },
                'power_rating': int,
                'control_endpoint_count': int,
                'daughter_board_count': int,
                'kr_support': str,
                '16_bit_gpio': str,
                'submodule_reset_support': str,
                'extended_attributes': {
                    'module_name': str,
                    'port_type': str,
                    'port_range': str,
                    'per_port_info': {
                        'max_iid': int,
                        'connector': str,
                        'network_clocking': str,
                    },
                },
                'module_oid': str,
                'port_oid': str,
            }
        }
    }


# ==========================
# Parser for:
#  * 'show hw-module subslot {slot} attribute'
# ==========================
class ShowHwModuleSubslotAttribute(ShowHwModuleSubslotAttributeSchema):
    """Parser for show hw-module subslot {slot} attribute"""

    cli_command = 'show hw-module subslot {slot} attribute'

    def cli(self, slot='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(slot=slot))

        # Initial variables
        ret_dict = {}

        # Slot 1 Bay 0 Board 0 Module[SM-X-6X1G] spa_type 0xBC4 Daughter Board Not Present
        p1 = re.compile(r'^Slot\s+(?P<slot>\d+)\s+Bay\s+(?P<bay>\d+)\s+Board\s+(?P<board>\d+)\s+'
                       r'Module\[(?P<module>\S+)\]\s+spa_type\s+(?P<spa_type_hex>0x\w+)\s+'
                       r'Daughter\s+Board\s+(?P<daughter_board>Not Present|Present)$')

        # Base mac_addr 500f.8001.c3f8 mac_blk_sz 10  Endpt MAC Address offset(s) : 0
        p2 = re.compile(r'^Base\s+mac_addr\s+(?P<base_mac_addr>\S+)\s+mac_blk_sz\s+(?P<mac_blk_sz>\d+)\s+'
                       r'Endpt\s+MAC\s+Address\s+offset\(s\)\s*:\s*(?P<endpt_mac_offset>\S+)$')

        # Basic attributes : length 11, version [2], module-type [ngio], width [Single Wide]
        p3 = re.compile(r'^Basic\s+attributes\s*:\s*length\s+(?P<length>\d+),\s*version\s+\[(?P<version>\d+)\],\s*'
                       r'module-type\s+\[(?P<module_type>\w+)\],\s*width\s+\[(?P<width>[\w\s]+)\]$')

        # Power Rating [75], Control Endpoint count [1], Daughter Board Count [0]
        p4 = re.compile(r'^Power\s+Rating\s+\[(?P<power_rating>\d+)\],\s*Control\s+Endpoint\s+count\s+\[(?P<control_endpoint_count>\d+)\],\s*'
                       r'Daughter\s+Board\s+Count\s+\[(?P<daughter_board_count>\d+)\]$')

        # KR Support [0x01], 16-bit GPIO [Present], Submodule reset support [Not required]
        p5 = re.compile(r'^KR\s+Support\s+\[(?P<kr_support>0x\w+)\],\s*16-bit\s+GPIO\s+\[(?P<gpio_16_bit>\w+)\],\s*'
                       r'Submodule\s+reset\s+support\s+\[(?P<submodule_reset_support>[\w\s]+)\]$')

        # Extended Attributes for [SM-X-6X1G]
        p6 = re.compile(r'^Extended\s+Attributes\s+for\s+\[(?P<module_name>\S+)\]$')

        # Port type Ethernet Range [0 5] Per-port Information : Max IID [1] Connector [SFP] Network clocking [disable]
        p7 = re.compile(r'^Port\s+type\s+(?P<port_type>\w+)\s+Range\s+\[(?P<port_range>[\d\s]+)\]\s+'
                       r'Per-port\s+Information\s*:\s*Max\s+IID\s+\[(?P<max_iid>\d+)\]\s+'
                       r'Connector\s+\[(?P<connector>\w+)\]\s+Network\s+clocking\s+\[(?P<network_clocking>\w+)\]$')

        # Module OID: 1 3 6 1 4 1 9 12 3 1 9 96 2
        p8 = re.compile(r'^Module\s+OID:\s+(?P<module_oid>[\d\s]+)$')

        # Port OID: 1 3 6 1 4 1 9 12 3 1 10 109
        p9 = re.compile(r'^Port\s+OID:\s+(?P<port_oid>[\d\s]+)$')

        for line in output.splitlines():
            line = line.strip()

            # Slot 1 Bay 0 Board 0 Module[SM-X-6X1G] spa_type 0xBC4 Daughter Board Not Present
            m = p1.match(line)
            if m:
                group = m.groupdict()
                slot_num = int(group['slot'])
                slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot_num, {})
                slot_dict['bay'] = int(group['bay'])
                slot_dict['board'] = int(group['board'])
                slot_dict['module'] = group['module']
                slot_dict['spa_type_hex'] = group['spa_type_hex']
                slot_dict['spa_type'] = group['spa_type_hex']  # Store hex value as spa_type
                slot_dict['daughter_board_present'] = group['daughter_board'] == 'Present'
                continue

            # Base mac_addr 500f.8001.c3f8 mac_blk_sz 10  Endpt MAC Address offset(s) : 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                slot_dict['base_mac_addr'] = group['base_mac_addr']
                slot_dict['mac_blk_sz'] = int(group['mac_blk_sz'])
                slot_dict['endpt_mac_address_offset'] = group['endpt_mac_offset']
                continue

            # Basic attributes : length 11, version [2], module-type [ngio], width [Single Wide]
            m = p3.match(line)
            if m:
                group = m.groupdict()
                basic_attr_dict = slot_dict.setdefault('basic_attributes', {})
                basic_attr_dict['length'] = int(group['length'])
                basic_attr_dict['version'] = group['version']
                basic_attr_dict['module_type'] = group['module_type']
                basic_attr_dict['width'] = group['width']
                continue

            # Power Rating [75], Control Endpoint count [1], Daughter Board Count [0]
            m = p4.match(line)
            if m:
                group = m.groupdict()
                slot_dict['power_rating'] = int(group['power_rating'])
                slot_dict['control_endpoint_count'] = int(group['control_endpoint_count'])
                slot_dict['daughter_board_count'] = int(group['daughter_board_count'])
                continue

            # KR Support [0x01], 16-bit GPIO [Present], Submodule reset support [Not required]
            m = p5.match(line)
            if m:
                group = m.groupdict()
                slot_dict['kr_support'] = group['kr_support']
                slot_dict['16_bit_gpio'] = group['gpio_16_bit']
                slot_dict['submodule_reset_support'] = group['submodule_reset_support']
                continue

            # Extended Attributes for [SM-X-6X1G]
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ext_attr_dict = slot_dict.setdefault('extended_attributes', {})
                ext_attr_dict['module_name'] = group['module_name']
                continue

            # Port type Ethernet Range [0 5] Per-port Information : Max IID [1] Connector [SFP] Network clocking [disable]
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ext_attr_dict = slot_dict.get('extended_attributes', {})
                ext_attr_dict['port_type'] = group['port_type']
                ext_attr_dict['port_range'] = group['port_range']
                per_port_dict = ext_attr_dict.setdefault('per_port_info', {})
                per_port_dict['max_iid'] = int(group['max_iid'])
                per_port_dict['connector'] = group['connector']
                per_port_dict['network_clocking'] = group['network_clocking']
                continue

            # Module OID: 1 3 6 1 4 1 9 12 3 1 9 96 2
            m = p8.match(line)
            if m:
                group = m.groupdict()
                slot_dict['module_oid'] = group['module_oid']
                continue

            # Port OID: 1 3 6 1 4 1 9 12 3 1 10 109
            m = p9.match(line)
            if m:
                group = m.groupdict()
                slot_dict['port_oid'] = group['port_oid']
                continue

        return ret_dict

class ShowPlatformHardwareChassisRpFanSpeedControlDataSchema(MetaParser):
    """Schema for:
       show platform hardware chassis rp {rp_state} fan-speed-control-data
    """
    schema = {
        'slots': {
            Any(): {  
                'type': str,
                'pwm': int,
                Optional('io_pwm'): Or(str,int),
            }
        }
    }


class ShowPlatformHardwareChassisRpFanSpeedControlData(ShowPlatformHardwareChassisRpFanSpeedControlDataSchema):
    """Parser for:
       show platform hardware chassis rp {rp_state} fan-speed-control-data
    """

    cli_command = 'show platform hardware chassis rp {rp_state} fan-speed-control-data'

    def cli(self, rp_state='', output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(rp_state=rp_state))
        else:
            out = output

        ret_dict = {}

        #    1   LC      76     102
        #    5  SUP      76     N/A
        p1 = re.compile(
            r'^\s*(?P<slot>\d+)\s+(?P<type>\S+)\s+(?P<pwm>\d+)\s+(?P<io_pwm>(?:\d+|N/?A))\s*$',
            re.IGNORECASE
        )

        for line in out.splitlines():
            line = line.rstrip()

            if not line or line.lstrip().startswith('Slot ') or set(line.strip()) == {'-'}:
                continue

            #   1   LC      76      91
            #   3   LC      76      76
            m = p1.match(line)
            if m:
                slot = int(m.group('slot'))
                entry = ret_dict.setdefault('slots', {}).setdefault(slot, {})
                entry['type'] = m.group('type')
                entry['pwm'] = int(m.group('pwm'))
                entry['io_pwm'] = m.group('io_pwm')

                continue

        return ret_dict

class HwModuleBeaconSlotPortStatusSchema(MetaParser):
    """
    Schema for hw-module beacon [switch {switch_num}] slot {slot_num} port {port_num} status
    """

    schema = {
        'beacon_status': str
    }

class HwModuleBeaconSlotPortStatus(HwModuleBeaconSlotPortStatusSchema):
    """Parser for hw-module beacon [switch {switch_num}] slot {slot_num} port {port_num} status"""

    cli_command = [
        "hw-module beacon switch {switch_num} slot {slot_num} port {port_num} status",
        "hw-module beacon slot {slot_num} port {port_num} status"
    ]

    def cli(self, slot_num='', port_num='', switch_num=None, output=None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[0].format(switch_num=switch_num, slot_num=slot_num, port_num=port_num)
            else:
                cmd = self.cli_command[1].format(slot_num=slot_num, port_num=port_num)

            output = self.device.execute(cmd)

        # BEACON OFF
        p1 = re.compile(r'^BEACON\s+(?P<beacon_status>\w+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # BEACON OFF
            m = p1.match(line)
            if m:
                ret_dict['beacon_status'] = m.group('beacon_status')
                break

        return ret_dict
