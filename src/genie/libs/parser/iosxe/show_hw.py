''' show_hw.py
IOSXE parsers for the following show commands:
    * show hw module subslot {subslot} transceiver {transceiver} status
    * show hw-module slot {slot} port-group mode
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


class ShowHardwareLedSchema(MetaParser):
    """
    Schema for show hardware led
    """
    schema = {
        'switch': {
            Any():{
                'system': str,
                'beacon': str,
                'port_led_status':{
                    str: str
                    },
                'rj45_console':str,
                'fantray_status':{
                    int : str
                    },
                'power_supply_beacon_status':{
                    int : str
                    },
                'system_psu':str,
                'system_fan':str,
                },
            },
        }     
                       
class ShowHardwareLed(ShowHardwareLedSchema):
    """ Parser for show hardware led"""

    cli_command = 'show hardware led'
    
    def cli(self, output=None): 
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}

        # SWITCH: 1
        p1 = re.compile('^SWITCH:\s+(?P<switch_num>\d+)$')

        # SYSTEM: GREEN
        p2 = re.compile('^SYSTEM:\s+(?P<system>\w+)$')

        # BEACON: OFF
        p3 = re.compile('^BEACON:\s+(?P<beacon>\w+)$')

        # PORT STATUS: (124) Hu1/0/1:GREEN Hu1/0/2:OFF Hu1/0/3:GREEN Hu1/0/4:OFF Hu1/0/5:OFF Hu1/0/6:GREEN Hu1/0/7:OFF Hu1/0/8:OFF Hu1/0/9:OFF Hu1/0/10:GREEN Hu1/0/11:GREEN Hu1/0/12:GREEN Hu1/0/13:GREEN Hu1/0/14:GREEN Fou1/0/15:GREEN Fou1/0/16:GREEN Fou1/0/17:GREEN Fou1/0/18:GREEN Fou1/0/19:GREEN Fou1/0/20:GREEN Fou1/0/21:GREEN Fou1/0/22:GREEN Hu1/0/23:GREEN Hu1/0/24:GREEN Hu1/0/25:OFF Hu1/0/26:GREEN Hu1/0/27:GREEN Hu1/0/28:GREEN Hu1/0/29:GREEN Hu1/0/30:GREEN Hu1/0/31:OFF Hu1/0/32:GREEN Hu1/0/33:GREEN Hu1/0/34:GREEN Hu1/0/35:GREEN Hu1/0/36:GREEN
        p4 = re.compile('^PORT STATUS:\s+\S+\s+(?P<led_ports>((\S+:\w+\s*))+)$')

        # RJ45 CONSOLE: GREEN
        p5 = re.compile('^RJ45 CONSOLE:\s+(?P<rj45_console>\w+)$')

        # FANTRAY 1 STATUS: GREEN
        p6 = re.compile('^FANTRAY\s+(?P<fantray_num>\d+)\s+STATUS:\s+(?P<fantray_status>\w+)$')

        # POWER-SUPPLY 1 BEACON: OFF
        p7 = re.compile('^POWER-SUPPLY\s+(?P<power_supply_num>\d+)\s+BEACON:\s+(?P<power_supply_status>\w+)$')

        # SYSTEM PSU: AMBER
        p8 = re.compile('^SYSTEM PSU:\s+(?P<system_psu>\w+)$')

        # SYSTEM FAN: GREEN
        p9 = re.compile('^SYSTEM FAN:\s+(?P<system_fan>\w+)$')


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
