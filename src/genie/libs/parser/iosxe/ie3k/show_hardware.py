''' show_hardware.py
IOSXE parsers for the following show commands:
    * show hardware hardware-led-state
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
        'poe': str,
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
        p10 = re.compile(r'^(?P<interface>\S+)\s+(?P<led_state>\w+)$')

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
