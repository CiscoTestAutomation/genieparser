""" show_hw.py

IOSXE parsers for the following show commands:
    * 'show hw-module subslot {subslot} transceiver {transceiver} status'
"""

# Python
import re
import xmltodict
import collections
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use, ListOf

# import parser utils
from genie.libs.parser.utils.common import Common

class ShowHwModuleSubslotSubslotTransceiverTransceiverStatusSchema(MetaParser):
    schema = {
        "subslot": {
            Any(): {
                "transceiver": {
                    Any(): {
                        "status": str,
                        "disabled_reasons": ListOf(str),
                        "module_temperature_c": float,
                        "tx_supply_voltage_mV": float,
                        "tx_bias_current_uA": Or(float, None),
                        "tx_power_dbm": float,
                        "tx_power_mW": Or(float, None),
                        "rx_optical_power_dbm": float,
                        "rx_optical_power_dbm_is_less_than": bool,
                        "rx_optical_power_mW": Or(float, None),
                        "lanes": {
                            "tx_power_dbm": {Optional(Any()): float},
                            "tx_power_mW": {Optional(Any()): float},
                            "rx_power_dbm": {Optional(Any()): float},
                            "rx_power_mW": {Optional(Any()): float},
                            "bias_current_mA": {Optional(Any()): float},
                        },
                    }
                }
            }
        }
    }


class ShowHwModuleSubslotSubslotTransceiverTransceiverStatus(ShowHwModuleSubslotSubslotTransceiverTransceiverStatusSchema):
    cli_command = "show hw-module subslot {subslot} transceiver {transceiver} status"

    def cli(self, subslot=None, transceiver=None, output=None):
        if output is None:
            cmd = self.cli_command.format(subslot=subslot, transceiver=transceiver)
            output = self.device.execute(cmd)

        ret_dict = {}
        if not output:
            return ret_dict

        # ==========================
        # Regex Section
        # ==========================

        # Example:
        # "show hw-module subslot 0/0 transceiver 0 status"
        p_cmd = re.compile(
            r"subslot\s+(?P<subslot>\S+).*transceiver\s+(?P<transceiver>\S+)"
        )

        # Example:
        # "The Transceiver in slot 0 subslot 0 port 0 is enabled."
        p1 = re.compile(
            r"is\s+(?P<status>enabled|disabled)\.", re.I
        )

        # Example:
        # "Transceiver has been disabled because:"
        p3 = re.compile(
            r"has\s+been\s+disabled\s+because:", re.I
        )

        # Example:
        # "  Some failure reason text"
        p4 = re.compile(
            r"^\s+(?P<reason>.+)$"
        )

        # Example:
        # "Module temperature = +28.945 C"
        p5 = re.compile(
            r"Module\s+temperature\s*=\s*(?P<temp>[+\-]?\d+\.\d+)"
        )

        # Example:
        # "Transceiver Tx supply voltage = 3284.2 mVolts"
        p6 = re.compile(
            r"Tx\s+supply\s+voltage\s*=\s*(?P<val>[+\-]?\d+\.\d+)\s+(?P<unit>mVolts|Volts)"
        )

        # Example:
        # "Transceiver Tx bias current = 5296 uAmps"
        p7 = re.compile(
            r"Tx\s+bias\s+current\s*=\s*(?P<val>\d+)"
        )

        # Example:
        # "Transceiver Tx power = -2.3 dBm"
        p8 = re.compile(
            r"Tx\s+power\s*=\s*(?P<dbm>[+\-]?\d+\.\d+)\s+dBm(?:.*?(?P<mw>\d+\.\d+)\s+mW)?"
        )

        # Example:
        # "Transceiver Rx optical power = -2.4 dBm"
        p9 = re.compile(
            r"Rx\s+optical\s+power\s*=\s*(?P<dbm>[+\-]?\d+\.\d+)\s+dBm(?:.*?(?P<mw>\d+\.\d+)\s+mW)?"
        )

        # Example:
        # "Rx optical power = <-40 dBm"
        p10 = re.compile(
            r"Rx\s+optical\s+power\s*=\s*<(?P<ldb>[+\-]?\d+(?:\.\d+)?)\s+dBm"
        )

        # Example:
        # "Tx power Network Lane[00] = -1.2 dBm 0.75 mW"
        p11 = re.compile(
            r"Tx\s+power\s+Network\s+Lane\[(?P<idx>\d{2})\].*?=\s*(?P<dbm>[+\-]?\d+\.\d+).*?(?P<mw>\d+\.\d+)"
        )

        # Example:
        # "Rx power Network Lane[00] = -1.5 dBm 0.70 mW"
        p12 = re.compile(
            r"Rx\s+power\s+Network\s+Lane\[(?P<idx>\d{2})\].*?=\s*(?P<dbm>[+\-]?\d+\.\d+).*?(?P<mw>\d+\.\d+)"
        )

        # Example:
        # "Bias Current Network Lane[00] = 5.2 mA"
        p13 = re.compile(
            r"Bias\s+Current\s+Network\s+Lane\[(?P<idx>\d{2})\].*?=\s*(?P<ma>\d+\.\d+)"
        )

        # ==========================
        # Parsing Logic
        # ==========================

        first_line = output.splitlines()[0]
        m_cmd = p_cmd.search(first_line)

        if m_cmd:
            subslot_key = m_cmd.group("subslot")
            transceiver_key = m_cmd.group("transceiver")
        else:
            subslot_key = subslot if subslot else "unknown"
            transceiver_key = transceiver if transceiver else "unknown"

        subslot_dict = ret_dict.setdefault("subslot", {})
        subslot_entry = subslot_dict.setdefault(subslot_key, {})
        transceiver_dict = subslot_entry.setdefault("transceiver", {})
        entry = transceiver_dict.setdefault(transceiver_key, {})

        # Defaults
        entry.setdefault("module_temperature_c", None)
        entry.setdefault("tx_supply_voltage_mV", None)
        entry.setdefault("tx_bias_current_uA", None)
        entry.setdefault("tx_power_dbm", None)
        entry.setdefault("tx_power_mW", None)
        entry.setdefault("rx_optical_power_dbm", None)
        entry.setdefault("rx_optical_power_dbm_is_less_than", False)
        entry.setdefault("rx_optical_power_mW", None)
        entry.setdefault("disabled_reasons", [])
        entry["lanes"] = {
            "tx_power_dbm": {},
            "tx_power_mW": {},
            "rx_power_dbm": {},
            "rx_power_mW": {},
            "bias_current_mA": {},
        }

        for raw_line in output.splitlines():
            line = raw_line.strip()
            if not line:
                continue

            m = p4.match(line)
            if m and "=" not in line:
                reason = m.group("reason").strip()
                if reason:
                    entry["disabled_reasons"].append(reason)
                continue

            m = p1.search(line)
            if m:
                entry["status"] = m.group("status").lower()
                continue

            if p3.search(line):
                entry["status"] = "disabled"
                continue

            m = p5.search(line)
            if m:
                entry["module_temperature_c"] = float(m.group("temp"))
                continue

            m = p6.search(line)
            if m:
                val = float(m.group("val"))
                entry["tx_supply_voltage_mV"] = val * 1000 if m.group("unit") == "Volts" else val
                continue

            m = p7.search(line)
            if m:
                entry["tx_bias_current_uA"] = float(m.group("val"))
                continue

            m = p8.search(line)
            if m:
                entry["tx_power_dbm"] = float(m.group("dbm"))
                if m.group("mw"):
                    entry["tx_power_mW"] = float(m.group("mw"))
                continue

            m = p9.search(line)
            if m:
                entry["rx_optical_power_dbm"] = float(m.group("dbm"))
                if m.group("mw"):
                    entry["rx_optical_power_mW"] = float(m.group("mw"))
                entry["rx_optical_power_dbm_is_less_than"] = False
                continue

            m = p10.search(line)
            if m:
                val = float(m.group("ldb"))
                entry["rx_optical_power_dbm"] = -abs(val)
                entry["rx_optical_power_dbm_is_less_than"] = True
                entry["rx_optical_power_mW"] = None
                continue

            m = p11.search(line)
            if m:
                idx = m.group("idx")
                entry["lanes"]["tx_power_dbm"][idx] = float(m.group("dbm"))
                entry["lanes"]["tx_power_mW"][idx] = float(m.group("mw"))
                continue

            m = p12.search(line)
            if m:
                idx = m.group("idx")
                entry["lanes"]["rx_power_dbm"][idx] = float(m.group("dbm"))
                entry["lanes"]["rx_power_mW"][idx] = float(m.group("mw"))
                continue

            m = p13.search(line)
            if m:
                idx = m.group("idx")
                entry["lanes"]["bias_current_mA"][idx] = float(m.group("ma"))
                continue


        return ret_dict
