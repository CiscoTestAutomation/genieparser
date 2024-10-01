''' show_hardware.py
IOSXE parsers for the following show commands:
    * show hardware led
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common


class ShowHardwareLedSchema(MetaParser):
    """
    Schema for show hardware led
    """
    schema = {
        Optional('switch'): {
            Any():{
                'line_card': {
                    Any():{
                        'number_of_ports_in_status':int,
                        'port_led_status':{
                            str: str
                        },
                        'beacon': str,
                        'status': str
                    }
                },
                'supervisor': {
                    Any():{
                        Optional('port_led_status'):{
                            str: str
                        },
                        'slot': int,
                        'beacon': str,
                        'status': str,
                        'system': str,
                        'active': str
                    }
                },
                'fantray_status': str,
                'fantray_beacon': str,
                'model': str,
                'system': str
            }
        },
        Optional('line_card'): {
            Any():{
                'number_of_ports_in_status':int,
                'port_led_status':{
                    str: str
                },
                'beacon': str,
                'status': str
            }
        },
        Optional('supervisor'): {
            Any():{
                Optional('port_led_status'):{
                    str: str
                },
                'slot': int,
                'beacon': str,
                Optional('status'): str,
                Optional('system'): str,
                Optional('active'): str
            }
        },
        Optional('fantray_status'): str,
        Optional('fantray_beacon'): str,
        Optional('model'): str,
        Optional('system'): str
    }
                  
class ShowHardwareLed(ShowHardwareLedSchema):
    """ Parser for show hardware led"""

    cli_command = 'show hardware led'
    
    def cli(self, output=None): 
        if output is None:
            output = self.device.execute(self.cli_command)

        # Switch 1:
        p0 = re.compile(r'^Switch\s+(?P<switch_num>\d+):$')

        # SWITCH: C9606R
        p1 = re.compile(r'^SWITCH:\s+(?P<model>\S+)$')

        # SYSTEM: GREEN
        p2 = re.compile(r'^SYSTEM:\s+(?P<system>\w+)$')

        # Line Card : 1
        p3 = re.compile(r'^Line\sCard\s*:\s+(?P<line_card>\d+)$')

        # PORT STATUS: (124) Hu1/0/1:GREEN Hu1/0/2:OFF Hu1/0/3:GREEN Hu1/0/4:OFF Hu1/0/5:OFF Hu1/0/6:GREEN Hu1/0/7:OFF Hu1/0/8:OFF Hu1/0/9:OFF Hu1/0/10:GREEN Hu1/0/11:GREEN Hu1/0/12:GREEN Hu1/0/13:GREEN Hu1/0/14:GREEN Fou1/0/15:GREEN Fou1/0/16:GREEN Fou1/0/17:GREEN Fou1/0/18:GREEN Fou1/0/19:GREEN Fou1/0/20:GREEN Fou1/0/21:GREEN Fou1/0/22:GREEN Hu1/0/23:GREEN Hu1/0/24:GREEN Hu1/0/25:OFF Hu1/0/26:GREEN Hu1/0/27:GREEN Hu1/0/28:GREEN Hu1/0/29:GREEN Hu1/0/30:GREEN Hu1/0/31:OFF Hu1/0/32:GREEN Hu1/0/33:GREEN Hu1/0/34:GREEN Hu1/0/35:GREEN Hu1/0/36:GREEN
        p4 = re.compile(r'^PORT\sSTATUS:\s+\((?P<number_of_ports_in_status>\d+)\)\s+(?P<led_ports>((\S+:\w+\s*))+)$')
        
        # BEACON: OFF
        p5 = re.compile(r'^BEACON:\s+(?P<beacon>.+)$')

        # STATUS: GREEN
        p6 = re.compile(r'^STATUS:\s+(?P<status>\w+)$')

        # MODULE: slot 3
        p7 = re.compile(r'^MODULE:\s*slot\s*(?P<supervisor>\d+)$')

        # SUPERVISOR: ACTIVE
        p8 = re.compile(r'^SUPERVISOR:\s*(?P<status>\w+)$')

        # ACTIVE: GREEN
        p9 = re.compile(r'^ACTIVE:\s+(?P<active>\w+)$')

        # FANTRAY STATUS: GREEN
        p10 = re.compile('^FANTRAY STATUS:\s+(?P<fantray_status>\w+)$')

        # FANTRAY BEACON: OFF
        p11 = re.compile('^FANTRAY BEACON:\s+(?P<fantray_beacon>\w+)$')

        ret_dict = {}
        root_dict = {}
        system_flag = False
        for line in output.splitlines():
            line = line.strip()
            
            # Switch 1:
            m = p0.match(line)
            if m:
                system_flag = False
                root_dict = ret_dict.setdefault('switch', {}).setdefault(int(m.groupdict()['switch_num']), {})
                continue

            # SWITCH: C9606R
            m = p1.match(line)
            if m:
                if not ret_dict:
                    root_dict = ret_dict
                root_dict['model'] = m.groupdict()['model']
                continue
            
            # SYSTEM: GREEN
            m = p2.match(line)
            if m:
                if system_flag:
                    card_dict['system'] = m.groupdict()['system']
                    continue
                root_dict['system'] = m.groupdict()['system']
                continue
            
            # Line Card : 1
            m = p3.match(line)
            if m:
                card_dict = root_dict.setdefault('line_card', {}).setdefault(int(m.groupdict()['line_card']), {})
                continue

            # PORT STATUS: (124) Hu1/0/1:GREEN Hu1/0/2:OFF Hu1/0/3:GREEN Hu1/0/4:OFF Hu1/0/5:OFF Hu1/0/6:GREEN Hu1/0/7:OFF Hu1/0/8:OFF Hu1/0/9:OFF Hu1/0/10:GREEN Hu1/0/11:GREEN Hu1/0/12:GREEN Hu1/0/13:GREEN Hu1/0/14:GREEN Fou1/0/15:GREEN Fou1/0/16:GREEN Fou1/0/17:GREEN Fou1/0/18:GREEN Fou1/0/19:GREEN Fou1/0/20:GREEN Fou1/0/21:GREEN Fou1/0/22:GREEN Hu1/0/23:GREEN Hu1/0/24:GREEN Hu1/0/25:OFF Hu1/0/26:GREEN Hu1/0/27:GREEN Hu1/0/28:GREEN Hu1/0/29:GREEN Hu1/0/30:GREEN Hu1/0/31:OFF Hu1/0/32:GREEN Hu1/0/33:GREEN Hu1/0/34:GREEN Hu1/0/35:GREEN Hu1/0/36:GREEN       
            m = p4.match(line)
            if m:
                group = m.groupdict()
                for port in group['led_ports'].split():
                    port = (port.split(':'))
                    port_led_dict = card_dict.setdefault('port_led_status',{})
                    port_led_dict.update({Common.convert_intf_name(port[0]): port[1]})
                card_dict['number_of_ports_in_status'] = int(group['number_of_ports_in_status'])
                continue

            # BEACON: OFF
            m = p5.match(line)
            if m:
                card_dict['beacon'] = m.groupdict()['beacon']
                continue

            # STATUS: GREEN
            m = p6.match(line)
            if m:
                card_dict['status'] = m.groupdict()['status']
                continue

            # MODULE: slot 3
            m = p7.match(line)
            if m:
                supervisor = m.groupdict()['supervisor']
                continue

            # SUPERVISOR: ACTIVE
            m = p8.match(line)
            if m:
                system_flag = True
                card_dict = root_dict.setdefault('supervisor', {}).setdefault(m.groupdict()['status'].lower(), {})
                card_dict['slot'] = int(supervisor)
                continue

            # ACTIVE: GREEN
            m = p9.match(line)
            if m:
                card_dict['active'] = m.groupdict()['active']
                continue

            # FANTRAY STATUS: GREEN
            m = p10.match(line)
            if m:
                root_dict['fantray_status'] = m.groupdict()['fantray_status']
                continue

            # FANTRAY BEACON: OFF
            m = p11.match(line)
            if m:
                root_dict['fantray_beacon'] = m.groupdict()['fantray_beacon']
                continue

        return ret_dict
