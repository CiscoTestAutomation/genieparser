''' show_hw.py
IOSXE parsers for the following show commands:
    * show hw module subslot {subslot} transceiver {transceiver} status
    * show hw-module slot {slot} port-group mode
    * show hw-module usbflash1 security status
    * show hw-module {filesystem} security-lock status
    * show hardware led port {port} {mode}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

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
        Optional('led_ecomode'): str,
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
        p1 = re.compile('^SWITCH:\s+(?P<switch_num>\d+)$')

        # SYSTEM: GREEN
        p2 = re.compile('^SYSTEM:\s+(?P<system>\w+)$')

        # BEACON: OFF
        p3 = re.compile('^BEACON:\s+(?P<beacon>\w+)$')

        # PORT STATUS: (124) Hu1/0/1:GREEN Hu1/0/2:OFF Hu1/0/3:GREEN Hu1/0/4:OFF Hu1/0/5:OFF Hu1/0/6:GREEN Hu1/0/7:OFF Hu1/0/8:OFF Hu1/0/9:OFF Hu1/0/10:GREEN Hu1/0/11:GREEN Hu1/0/12:GREEN Hu1/0/13:GREEN Hu1/0/14:GREEN Fou1/0/15:GREEN Fou1/0/16:GREEN Fou1/0/17:GREEN Fou1/0/18:GREEN Fou1/0/19:GREEN Fou1/0/20:GREEN Fou1/0/21:GREEN Fou1/0/22:GREEN Hu1/0/23:GREEN Hu1/0/24:GREEN Hu1/0/25:OFF Hu1/0/26:GREEN Hu1/0/27:GREEN Hu1/0/28:GREEN Hu1/0/29:GREEN Hu1/0/30:GREEN Hu1/0/31:OFF Hu1/0/32:GREEN Hu1/0/33:GREEN Hu1/0/34:GREEN Hu1/0/35:GREEN Hu1/0/36:GREEN
        p4 = re.compile('^PORT STATUS:\s+\S+\s+(?P<led_ports>((\S+:\w+\s*))+)$')
        
        #STATUS: (28) Gi1/0/1:FLASH_GREEN Gi1/0/2:BLACK Gi1/0/3:BLACK Gi1/0/4:BLACK Gi1/0/5:FLASH_GREEN Gi1/0/6:FLASH_GREEN Gi1/0/7:FLASH_GREEN Gi1/0/8:FLASH_GREEN Gi1/0/9:BLACK Gi1/0/10:FLASH_GREEN Gi1/0/11:FLASH_GREEN Gi1/0/12:BLACK Gi1/0/13:BLACK Gi1/0/14:BLACK Gi1/0/15:BLACK Gi1/0/16:BLACK Gi1/0/17:BLACK Gi1/0/18:BLACK Gi1/0/19:BLACK Gi1/0/20:BLACK Gi1/0/21:BLACK Gi1/0/22:BLACK Gi1/0/23:FLASH_GREEN Gi1/0/24:FLASH_GREEN Gi1/0/25:BLACK Gi1/0/26:BLACK Gi1/0/27:BLACK Gi1/0/28:BLACK
        p4_1 = re.compile('^STATUS:\s+\((?P<port_nums_in_status>\d+)\)+\s+(?P<led_ports>((\S+:[\w-]+\s*))+)$')

        # RJ45 CONSOLE: GREEN
        p5 = re.compile('^RJ45 CONSOLE:\s+(?P<rj45_console>\w+)$')

        # FANTRAY 1 STATUS: GREEN
        p6 = re.compile('^FANTRAY\s+(?P<fantray_num>\d+)\s+STATUS:\s+(?P<fantray_status>\w+)$')

        # POWER-SUPPLY 1 BEACON: OFF
        p7 = re.compile('^POWER-SUPPLY\s+(?P<power_supply_num>\d+)\s+BEACON:\s+(?P<power_supply_status>\w+)$')
        
        #DC-A: GREEN
        p7_1 = re.compile('^DC-A:\s+(?P<dc_a>\w+)$')

        #DC-B: BLACK
        p7_2 = re.compile('^DC-B:\s+(?P<dc_b>\w+)$')

        # SYSTEM PSU: AMBER
        p8 = re.compile('^SYSTEM PSU:\s+(?P<system_psu>\w+)$')

        # SYSTEM FAN: GREEN
        p9 = re.compile('^SYSTEM FAN:\s+(?P<system_fan>\w+)$')

        #EXPRESS-SETUP: BLACK
        p10 = re.compile('^EXPRESS-SETUP:\s+(?P<express_setup>\w+)$')

        # ALARM-OUT: GREEN
        # ALARM-IN1: GREEN
        # ALARM-IN2: GREEN
        p11 = re.compile('^(?P<alarm>ALARM\-\w+):\s+(?P<alarm_color>\w+)$')

        # Current Mode: STATUS
        p12 = re.compile('^Current Mode:\s+(?P<status>\w+)$')

        # LED Ecomode: Enabled
        p12_1 = re.compile('^LED Ecomode:\s+(?P<ecomode>\w+)$')

        # MASTER: GREEN
        p13 = re.compile('^MASTER:\s+(?P<master>\w+)$')

        # DUPLEX: (65) Tw1/0/1:BLACK Tw1/0/2:BLACK Tw1/0/3:BLACK 
        # Tw1/0/4:GREEN Tw1/0/5:BLACK Tw1/0/6:BLACK Tw1/0/7:BLACK
        p14 = re.compile('^DUPLEX:\s+\S+\s+(?P<duplex>((\S+:\S+\s*))+)$')

        # SPEED: (65) Tw1/0/1:BLACK Tw1/0/2:BLACK Tw1/0/3:BLACK 
        # Tw1/0/4:BLINK_GREEN Tw1/0/5:BLACK Tw1/0/6:BLACK Tw1/0/7:BLACK
        p15 = re.compile('^SPEED:\s+\S+\s+(?P<speed>((\S+:\S+\s*))+)$')

        # STACK: (65) Tw1/0/1:FLASH_GREEN Tw1/0/2:BLACK Tw1/0/3:BLACK
        # Tw1/0/4:BLACK Tw1/0/5:BLACK Tw1/0/6:BLACK Tw1/0/7:BLACK Tw1/0/8:BLACK
        p16 = re.compile('^STACK:\s+\S+\s+(?P<stack_port>((\S+:\S+\s*))+)$')

        # POE: (65) Tw1/0/1:BLACK Tw1/0/2:BLACK Tw1/0/3:BLACK Tw1/0/4:BLACK
        # Tw1/0/5:BLACK Tw1/0/6:BLACK Tw1/0/7:BLACK Tw1/0/8:BLACK Tw1/0/9:BLACK
        p17 = re.compile('^POE:\s+\S+\s+(?P<poe>((\S+:\S+\s*))+)$')

        # STACK POWER: BLACK
        p18 = re.compile('^STACK POWER:\s+(?P<stack_power>\w+)$')

        # XPS: BLACK
        p19 = re.compile('^XPS:\s+(?P<xps>\w+)$')

        # USB CONSOLE: BLACK
        p20 = re.compile('^USB CONSOLE:\s+(?P<usb_console>\w+)$')

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

            # LED Ecomode: Enabled
            m = p12_1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'led_ecomode' : group['ecomode']})
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
        p1 = re.compile('^(?P<port_status>\w+)$')

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
        'current_mode': str,
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
