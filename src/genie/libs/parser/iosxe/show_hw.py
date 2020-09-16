''' show_hw.py
IOSXE parsers for the following show commands:
    * show hw module subslot {subslot} transceiver {transceiver} status
'''

import re

from genie.metaparser import MetaParser
# from genie.metaparser.util.schemaengine import Any, Optional

# parser utils
# from genie.libs.parser.utils.common import Common


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
