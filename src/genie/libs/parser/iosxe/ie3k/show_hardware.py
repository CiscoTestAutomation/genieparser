''' show_hardware.py
IOSXE parsers for the following show commands:
    * show hardware hardware-led-state
    * show hardware led
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

class ShowHardwareLedStateSchema(MetaParser):
    """
    Schema for show hardware hardware-led-state
    """
    schema = {
        'system': str,
        'express_setup': str,
        Optional('poe'): str,
        'dc_a': str,
        'dc_b': str,
        'alarm_out': str,
        'alarm_in1': str,
        'alarm_in2': str,
        'eip_net_led': str,
        Optional('interfaces'): {
            str: str  # Interface name as key and LED state as value
        }
    }

class ShowHardwareLedState(ShowHardwareLedStateSchema):
    """ Parser for show hardware hardware-led-state """

    cli_command = ['show hardware hardware-led-state']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        ret_dict = {}
        
        # SYSTEM: GREEN
        p1 = re.compile(r'^SYSTEM:\s+(?P<system>\w+)$')

        # EXPRESS-SETUP: BLACK
        p2 = re.compile(r'^EXPRESS-SETUP:\s+(?P<express_setup>\w+)$')

        # POE: BLACK
        p3 = re.compile(r'^POE:\s+(?P<poe>\w+)$')

        # DC-A: GREEN
        p4 = re.compile(r'^DC-A:\s+(?P<dc_a>\w+)$')

        # DC-B: BLACK
        p5 = re.compile(r'^DC-B:\s+(?P<dc_b>\w+)$')

        # ALARM-OUT: GREEN
        p6 = re.compile(r'^ALARM-OUT:\s+(?P<alarm_out>\w+)$')

        # ALARM-IN1: GREEN
        p7 = re.compile(r'^ALARM-IN1:\s+(?P<alarm_in1>\w+)$')

        # ALARM-IN2: GREEN
        p8 = re.compile(r'^ALARM-IN2:\s+(?P<alarm_in2>\w+)$')

        # EIP-NET-LED: BLACK
        p9 = re.compile(r'^EIP-NET-LED:\s+(?P<eip_net_led>\w+)$')

        # Gi1/1 BLACK
        p10 = re.compile(r'^(?P<interface>\S+)\s+(?P<led_state>\w+(?:\([^)]+\))?)$')

        for line in output.splitlines():
            line = line.strip()

            # SYSTEM: GREEN
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'system': group['system']})
                continue

            # EXPRESS-SETUP: BLACK
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'express_setup': group['express_setup']})
                continue

            # POE: BLACK
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'poe': group['poe']})
                continue

            # DC-A: GREEN
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'dc_a': group['dc_a']})
                continue

            # DC-B: BLACK
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'dc_b': group['dc_b']})
                continue

            # ALARM-OUT: GREEN
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'alarm_out': group['alarm_out']})
                continue

            # ALARM-IN1: GREEN
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'alarm_in1': group['alarm_in1']})
                continue

            # ALARM-IN2: GREEN
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'alarm_in2': group['alarm_in2']})
                continue

            # EIP-NET-LED: BLACK
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'eip_net_led': group['eip_net_led']})
                continue

            # Gi1/1 BLACK
            m = p10.match(line)
            if m:
                group = m.groupdict()
                interface_led_dict = ret_dict.setdefault('interfaces', {})
                interface_led_dict.update({Common.convert_intf_name(group['interface']): group['led_state']})
                continue 
               
        return ret_dict


# ==================================================================================
#  Schema for 'show hardware led'
# ==================================================================================

class ShowHardwareLedSchema(MetaParser):
    """
    Schema for show hardware led
    """
    schema = {
        Optional('current_mode'): str,        
        Optional('system'):str,
        'status':{
            str: str
        },
        'number_of_ports_in_status':str,
        'express_setup':str,
        Optional('dc_a'):str,
        Optional('dc_b'):str,
        'alarm-out':str,
        Optional('alarm-in1'):str,
        Optional('alarm-in2'):str,
        Optional('alarm-in3'):str,
        Optional('alarm-in4'):str,
        Optional('alarm-in'):str,
        Optional('poe'): str,
        Optional('switch'): str,
        Optional('sd_card'): str,
        Optional('mode_speed'): str,
        Optional('mode_duplex'): str,
        Optional('mode_redundancy'): str,
        Optional('mode_stack'): str,
        Optional('usb_type_host'): str,
        Optional('stack_active'): str,
        Optional('stack_a'): str,
        Optional('stack_b'): str,
        Optional('rj45_console'): str,
        Optional('usb_console'): str,
        Optional('console'): str,
        Optional('eip_mod'): str,
        Optional('eip_net'): str,
    }     
                       
class ShowHardwareLed(ShowHardwareLedSchema):
    """ Parser for show hardware led"""

    cli_command = ['show hardware led']
    
    def cli(self, output=None): 
        if output is None:
            cmd = self.cli_command[0]
            output = self.device.execute(cmd)
            
        # initial variables
        ret_dict = {}
        
        # Current Mode: STATUS
        p1 = re.compile(r'^Current Mode:\s+(?P<status>\w+)$')

        # SYSTEM: GREEN
        p2 = re.compile(r'^SYSTEM:\s+(?P<system>\w+)$')

        # EXPRESS-SETUP: BLACK
        p3 = re.compile(r'^EXPRESS-SETUP:\s+(?P<express_setup>\w+)$')

        # DC-A: BLACK
        p4 = re.compile(r'^DC-A:\s+(?P<dc_a>\w+)$')

        # DC-B: GREEN
        p5 = re.compile(r'^DC-B:\s+(?P<dc_b>\w+)$')

        # ALARM-OUT: GREEN
        # ALARM-IN1: GREEN
        # ALARM-IN2: GREEN
        # ALARM-IN3: GREEN
        # ALARM-IN4: GREEN
        # ALARM-IN: GREEN
        p6 = re.compile(r'^(?P<alarm>ALARM\-\w+):\s+(?P<alarm_color>\w+)$')

        # POE: BLACK
        p7 = re.compile(r'^POE:\s+(?P<poe>\w+)$')

        # STATUS: (26) Te1/1: Te1/2: Gi1/3:BLACK-BLACK Gi1/4:BLACK-BLACK Gi1/5:BLACK-BLACK Gi1/6:BLACK-BLACK Gi1/7:BLACK Gi1/8:BLACK Gi1/9:BLACK Gi1/10:BLACK Gi2/1:BLACK-BLACK Gi2/2:BLACK-BLACK Gi2/3:BLACK-BLACK Gi2/4:BLACK-BLACK Gi2/5:BLACK Gi2/6:BLACK Gi2/7:BLACK Gi2/8:BLACK Gi2/9:BLACK Gi2/10:BLACK Gi2/11:BLACK Gi2/12:BLACK Gi2/13:
        # STATUS: (28) Gi1/1:FLASH_GREEN Gi1/2:FLASH_GREEN Gi1/3:FLASH_GREEN Gi1/4:ACT_GREEN Gi1/5:BLACK Gi1/6:ACT_GREEN Gi1/7:BLACK Gi1/8:BLACK Gi1/9:ACT_GREEN Gi1/10:ACT_GREEN Gi1/11:ACT_GREEN Gi2/1:ACT_GREEN Gi2/2:BLACK Gi2/3:BLACK Gi2/4:BLACK Gi2/5:ACT_GREEN Gi2/6:BLACK Gi2/7:BLACK Gi2/8:ACT_AMBER Gi2/9:ACT_GREEN Gi2/10:BLACK Gi2/11:BLACK Gi2/12:BLACK Gi2/13:ACT_GREEN Gi2/14:BLACK Gi2/15:BLACK Gi2/16:ACT_GREEN
        p8 = re.compile(r'^STATUS:\s+\((?P<port_nums_in_status>\d+)\)\s+(?P<led_ports>(?:\S+:[\w-]*\s*)+)$')

        # SWITCH: 1
        p9 = re.compile(r'^SWITCH:\s+(?P<switch>\d+)$')

        # SD-CARD: GREEN
        p10 = re.compile(r'^SD-CARD:\s+(?P<sd_card>\w+)$')

        # MODE-SPEED: BLACK
        # MODE-DUPLEX: BLACK
        # MODE-REDUNDANCY: BLACK
        # MODE-STACK: BLACK
        p11 = re.compile(r'^MODE-(?P<mode>\w+):\s+(?P<mode_color>\w+)$')

        # USB-TYPE-A-HOST: BLACK
        p12 = re.compile(r'^USB-TYPE-A-HOST:\s+(?P<usb_type_host>\w+)$')

        # STACK-ACTIVE: BLACK
        # STACK-A: BLACK
        # STACK-B: BLACK
        p13 = re.compile(r'^STACK-(?P<name>ACTIVE|A|B):\s+(?P<stack_color>\w+)$')

        # RJ45 CONSOLE: GREEN
        p14 = re.compile(r'^RJ45\s+CONSOLE:\s+(?P<rj45_console>\w+)$')

        # USB CONSOLE: BLACK
        p15 = re.compile(r'^USB\s+CONSOLE:\s+(?P<usb_console>\w+)$')

        # CONSOLE: BLACK
        p16 = re.compile(r'^CONSOLE:\s+(?P<console>\w+)$')

        # EIP-MOD: GREEN
        p17 = re.compile(r'^EIP-MOD:\s+(?P<eip_mod>\w+)$')

        # EIP-NET: BLACK
        p18 = re.compile(r'^EIP-NET:\s+(?P<eip_net>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # Current Mode: STATUS
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'current_mode' : group['status']})
                continue

            # SYSTEM: GREEN
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'system' : group['system']})
                continue

            # EXPRESS-SETUP: BLACK
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'express_setup' : group['express_setup']})
                continue

            # DC-A: BLACK
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if group['dc_a']:
                    ret_dict.update({'dc_a': group['dc_a']})
                    continue

            # DC-B: GREEN
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if group['dc_b']:
                    ret_dict.update({'dc_b': group['dc_b']})
                    continue

            # ALARM-OUT: GREEN
            # ALARM-IN1: GREEN
            # ALARM-IN2: GREEN
            # ALARM-IN: GREEN
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({group['alarm'].lower() : group['alarm_color']})
                continue

            # POE: BLACK
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'poe': group['poe']})
                continue

            # STATUS: (28) Gi1/1:FLASH_GREEN Gi1/2:FLASH_GREEN Gi1/3:FLASH_GREEN Gi1/4:ACT_GREEN Gi1/5:BLACK Gi1/6:ACT_GREEN Gi1/7:BLACK Gi1/8:BLACK Gi1/9:ACT_GREEN Gi1/10:ACT_GREEN Gi1/11:ACT_GREEN Gi2/1:ACT_GREEN Gi2/2:BLACK Gi2/3:BLACK Gi2/4:BLACK Gi2/5:ACT_GREEN Gi2/6:BLACK Gi2/7:BLACK Gi2/8:ACT_AMBER Gi2/9:ACT_GREEN Gi2/10:BLACK Gi2/11:BLACK Gi2/12:BLACK Gi2/13:ACT_GREEN Gi2/14:BLACK Gi2/15:BLACK Gi2/16:ACT_GREEN
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'number_of_ports_in_status' : group['port_nums_in_status']})
                for port in group['led_ports'].split():
                    port = (port.split(':'))
                    port_led_dict = ret_dict.setdefault('status',{})
                    port_led_dict.update({Common.convert_intf_name(port[0]): port[1]})
                continue

            # SWITCH: 1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'switch' : group['switch']})
                continue

            # SD-CARD: GREEN
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'sd_card' : group['sd_card']})
                continue

            # MODE-SPEED: BLACK
            # MODE-DUPLEX: BLACK
            # MODE-REDUNDANCY: BLACK    
            # MODE-STACK: BLACK
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict[f"mode_{group['mode'].lower()}"] = group['mode_color']
                continue

            # USB-TYPE-A-HOST: BLACK
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'usb_type_host' : group['usb_type_host']})
                continue

            # STACK-ACTIVE: BLACK
            # STACK-A: BLACK        
            # STACK-B: BLACK
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict[f"stack_{group['name'].lower()}"] = group['stack_color']
                continue

            # RJ45 CONSOLE: GREEN
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'rj45_console' : group['rj45_console']})
                continue

            # USB CONSOLE: BLACK
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'usb_console' : group['usb_console']})
                continue

            # CONSOLE: BLACK
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'console' : group['console']})
                continue

            # EIP-MOD: GREEN
            m = p17.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'eip_mod' : group['eip_mod']})
                continue

            # EIP-NET: BLACK
            m = p18.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'eip_net' : group['eip_net']})
                continue

        return ret_dict
