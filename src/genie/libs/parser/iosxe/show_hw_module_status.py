''' show_hw_module_status.py
IOSXE parsers for the following show commands:
    * show hw_module subslot {subslot} transceiver {transceiver} status
'''

import re

from genie.metaparser import MetaParser
# from genie.metaparser.util.schemaengine import Any, Optional

# parser utils
# from genie.libs.parser.utils.common import Common


# ==========================
# Schema for:
#  * 'show_hw_module_status'
# ==========================
class Show_Hw_Module_StatusSchema(MetaParser):
    """Schema for show_hw_module_status."""

    schema = {
        "transceiver_status": {
            "transceivers": {
                str: {
                    "status": str,
                    "module_temperature": str,
                    "supply_voltage_mVolts": str,
                    "bias_current_uAmps": int,
                    "tx_power_dBm": str,
                    "optical_power_dBm": str
                }
            }
        }
    }


# ==========================
# Parser for:
#  * 'show_hw_module_status'
# ==========================
class Show_Hw_Module_Status(Show_Hw_Module_StatusSchema):
    """Parser for show_hw_module_status"""

    cli_command = [
        'show hw_module subslot {subslot} transceiver {transceiver} status'
    ]

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        p1 = re.compile(
            r"The\s+Transceiver\s+in\s+slot\s(?P<slot_id>\d+)"
            r"\s+subslot\s+(?P<subslot_id>\d+)"
            r"\s+port\s+(?P<port_id>\d+)\s+is\s+"
            r"(?P<status>(enabled|disabled))",
            re.MULTILINE)
        p2 = re.compile(r"\s+(?P<module_temperature>\S+)\s+C", re.MULTILINE)
        p3 = re.compile(r"\s+(?P<supply_voltage_mVolts>\d+\.\d+)",
                        re.MULTILINE)
        p4 = re.compile(r"\s+(?P<bias_current_uAmps>\d+)\s+uAmps",
                        re.MULTILINE)
        p5 = re.compile(r"\s+(?P<tx_power_dBm>\S+)\s+dBm",
                        re.MULTILINE)
        p6 = re.compile(r"\s+(?P<optical_power_dBm>\S+)\s+dBm",
                        re.MULTILINE)

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
                    slot_id = groups['slot_id']
                    subslot = groups['subslot_id']
                    port_id = groups['port_id']
                    transceiver = f"{slot_id}/{subslot}/{port_id}"
                    if not transceiver_dict.get('transceiver_status'):
                        transceiver_dict.update(
                            {'transceiver_status': {
                                'transceivers': {}}})
                    if not transceiver_dict['transceiver_status']['transceivers'].get(transceiver):
                        transceiver_dict['transceiver_status']['transceivers'].update({transceiver: {}})
                    transceiver_dict['transceiver_status']['transceivers'][transceiver].update({'status': groups['status']})
                continue
            if regex:
                match = regex.match((value))
                groups = match.groupdict()
                for k, v in groups.items():
                    if v is None:
                        continue
                    if v.isdigit():
                        v = int(v)
                    transceiver_dict['transceiver_status']['transceivers'][transceiver].update({k: v})

        if transceiver_dict:
            return transceiver_dict
        else:
            return {}
