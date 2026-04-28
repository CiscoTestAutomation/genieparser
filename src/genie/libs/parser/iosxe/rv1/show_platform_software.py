""" show_platform_software.py

IOSXE parsers for the following show commands:
    * 'show platform software access-list fp active statistics'
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

class ShowPlatformSoftwareAccessListFpActiveStatisticsSchema(MetaParser):
    """Schema for show platform software access-list fp active statistics"""

    schema = {
        "forwarding_manager_access_list_messaging_statistics": {
            "set_log_threshold": int,
            "interval": int,
            "ipv4": {
                "access_list": {
                    "entry": {"add": int, "delete": int},
                    "binding": {"bind": int, "unbind": int},
                    "resequence": {"resequence": int, "delete": int},
                }
            },
            "ipv6": {
                "access_list": {
                    "entry": {"add": int, "delete": int},
                    "binding": {"bind": int, "unbind": int},
                    "resequence": {"resequence": int, "delete": int},
                }
            },
            "mac": {
                "access_list": {
                    "entry": {"add": int, "delete": int},
                    "binding": {"bind": int, "unbind": int},
                    "delete": int,
                }
            },
            "access_list_sync": {"start": int, "end": int},
            "qfp": {
                "match_add_replace": {
                    "add": int,
                    "replace": int,
                    "ack_success": int,
                    "ack_error": int,
                },
                "match_delete": {
                    "delete": int,
                    "ack_success": int,
                    "ack_error": int,
                },
                "action_edit": {"count": int, "ack_success": int, "ack_error": int},
                "action_replace": {"count": int, "ack_success": int, "ack_error": int},
                "bind": {"count": int, "ack_success": int, "ack_error": int},
                "unbind": {"count": int, "ack_success": int, "ack_error": int},
            },
        }
    }


class ShowPlatformSoftwareAccessListFpActiveStatistics(
    ShowPlatformSoftwareAccessListFpActiveStatisticsSchema
):
    """Parser for show platform software access-list fp active statistics"""

    cli_command = "show platform software access-list fp active statistics"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        if not out:
            return ret_dict

        fm_stats = ret_dict.setdefault(
            "forwarding_manager_access_list_messaging_statistics", {}
        )

        # Set Log Threshold: 0, Interval: 0
        p1 = re.compile(
            r"^Set\s+Log\s+Threshold\s*:\s*(?P<set_log_threshold>\d+)\s*,\s*Interval\s*:\s*(?P<interval>\d+)\s*$"
        )
        # IPv4 Access-list Entry Add: 0, Delete: 0
        p2 = re.compile(
            r"^(?P<family>IPv4|IPv6)\s+Access-list\s+Entry\s+Add\s*:\s*(?P<add>\d+)\s*,\s*Delete\s*:\s*(?P<delete>\d+)\s*$"
        )
        # IPv4 Access-list Bind: 0, Unbind: 0
        p3 = re.compile(
            r"^(?P<family>IPv4|IPv6)\s+Access-list\s+Bind\s*:\s*(?P<bind>\d+)\s*,\s*Unbind\s*:\s*(?P<unbind>\d+)\s*$"
        )
        # IPv4 Access-list Resequence: 0, Delete: 0
        p4 = re.compile(
            r"^(?P<family>IPv4|IPv6)\s+Access-list\s+Resequence\s*:\s*(?P<resequence>\d+)\s*,\s*Delete\s*:\s*(?P<delete>\d+)\s*$"
        )
        # MAC Access-list Entry Add: 0, Delete: 0
        p5 = re.compile(
            r"^MAC\s+Access-list\s+Entry\s+Add\s*:\s*(?P<add>\d+)\s*,\s*Delete\s*:\s*(?P<delete>\d+)\s*$"
        )
        # MAC Access-list Bind: 0, Unbind: 0
        p6 = re.compile(
            r"^MAC\s+Access-list\s+Bind\s*:\s*(?P<bind>\d+)\s*,\s*Unbind\s*:\s*(?P<unbind>\d+)\s*$"
        )
        # MAC Access-list Delete: 0
        p7 = re.compile(r"^MAC\s+Access-list\s+Delete\s*:\s*(?P<delete>\d+)\s*$")
        # Access-list Sync Start: 0, End: 0
        p8 = re.compile(
            r"^Access-list\s+Sync\s+Start\s*:\s*(?P<start>\d+)\s*,\s*End\s*:\s*(?P<end>\d+)\s*$"
        )
        # QFP Match Add: 0, Replace: 0, ACK Success: 0, ACK Error: 0
        p9 = re.compile(
            r"^QFP\s+Match\s+Add\s*:\s*(?P<add>\d+)\s*,\s*Replace\s*:\s*(?P<replace>\d+)\s*,\s*ACK\s+Success\s*:\s*(?P<ack_success>\d+)\s*,\s*ACK\s+Error\s*:\s*(?P<ack_error>\d+)\s*$"
        )
        # QFP Match Delete: 0, ACK Success: 0, ACK Error: 0
        p10 = re.compile(
            r"^QFP\s+Match\s+Delete\s*:\s*(?P<delete>\d+)\s*,\s*ACK\s+Success\s*:\s*(?P<ack_success>\d+)\s*,\s*ACK\s+Error\s*:\s*(?P<ack_error>\d+)\s*$"
        )
        # QFP Action Edit: 0, ACK Success: 0, ACK Error: 0
        p11 = re.compile(
            r"^QFP\s+Action\s+Edit\s*:\s*(?P<count>\d+)\s*,\s*ACK\s+Success\s*:\s*(?P<ack_success>\d+)\s*,\s*ACK\s+Error\s*:\s*(?P<ack_error>\d+)\s*$"
        )
        # QFP Action Replace: 0, ACK Success: 0, ACK Error: 0
        p12 = re.compile(
            r"^QFP\s+Action\s+Replace\s*:\s*(?P<count>\d+)\s*,\s*ACK\s+Success\s*:\s*(?P<ack_success>\d+)\s*,\s*ACK\s+Error\s*:\s*(?P<ack_error>\d+)\s*$"
        )
        # QFP Bind: 0, ACK Success: 0, ACK Error: 0
        p13 = re.compile(
            r"^QFP\s+Bind\s*:\s*(?P<count>\d+)\s*,\s*ACK\s+Success\s*:\s*(?P<ack_success>\d+)\s*,\s*ACK\s+Error\s*:\s*(?P<ack_error>\d+)\s*$"
        )
        # QFP Unbind: 0, ACK Success: 0, ACK Error: 0
        p14 = re.compile(
            r"^QFP\s+Unbind\s*:\s*(?P<count>\d+)\s*,\s*ACK\s+Success\s*:\s*(?P<ack_success>\d+)\s*,\s*ACK\s+Error\s*:\s*(?P<ack_error>\d+)\s*$"
        )

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # Set Log Threshold: 0, Interval: 0
            m = p1.match(line)
            if m:
                gd = m.groupdict()
                fm_stats["set_log_threshold"] = int(gd["set_log_threshold"])
                fm_stats["interval"] = int(gd["interval"])
                continue

            # IPv4 Access-list Entry Add: 0, Delete: 0
            m = p2.match(line)
            if m:
                gd = m.groupdict()
                family = gd["family"].lower()
                access_list = fm_stats.setdefault(family, {}).setdefault(
                    "access_list", {}
                )
                entry = access_list.setdefault("entry", {})
                entry["add"] = int(gd["add"])
                entry["delete"] = int(gd["delete"])
                continue

            # IPv4 Access-list Bind: 0, Unbind: 0
            m = p3.match(line)
            if m:
                gd = m.groupdict()
                family = gd["family"].lower()
                access_list = fm_stats.setdefault(family, {}).setdefault(
                    "access_list", {}
                )
                binding = access_list.setdefault("binding", {})
                binding["bind"] = int(gd["bind"])
                binding["unbind"] = int(gd["unbind"])
                continue

            # IPv4 Access-list Resequence: 0, Delete: 0
            m = p4.match(line)
            if m:
                gd = m.groupdict()
                family = gd["family"].lower()
                access_list = fm_stats.setdefault(family, {}).setdefault(
                    "access_list", {}
                )
                resequence = access_list.setdefault("resequence", {})
                resequence["resequence"] = int(gd["resequence"])
                resequence["delete"] = int(gd["delete"])
                continue

            # MAC Access-list Entry Add: 0, Delete: 0
            m = p5.match(line)
            if m:
                gd = m.groupdict()
                access_list = fm_stats.setdefault("mac", {}).setdefault(
                    "access_list", {}
                )
                entry = access_list.setdefault("entry", {})
                entry["add"] = int(gd["add"])
                entry["delete"] = int(gd["delete"])
                continue

            # MAC Access-list Bind: 0, Unbind: 0
            m = p6.match(line)
            if m:
                gd = m.groupdict()
                access_list = fm_stats.setdefault("mac", {}).setdefault(
                    "access_list", {}
                )
                binding = access_list.setdefault("binding", {})
                binding["bind"] = int(gd["bind"])
                binding["unbind"] = int(gd["unbind"])
                continue

            # MAC Access-list Delete: 0
            m = p7.match(line)
            if m:
                gd = m.groupdict()
                access_list = fm_stats.setdefault("mac", {}).setdefault(
                    "access_list", {}
                )
                access_list["delete"] = int(gd["delete"])
                continue

            # Access-list Sync Start: 0, End: 0
            m = p8.match(line)
            if m:
                gd = m.groupdict()
                sync = fm_stats.setdefault("access_list_sync", {})
                sync["start"] = int(gd["start"])
                sync["end"] = int(gd["end"])
                continue

            # QFP Match Add: 0, Replace: 0, ACK Success: 0, ACK Error: 0
            m = p9.match(line)
            if m:
                gd = m.groupdict()
                qfp = fm_stats.setdefault("qfp", {})
                mar = qfp.setdefault("match_add_replace", {})
                mar["add"] = int(gd["add"])
                mar["replace"] = int(gd["replace"])
                mar["ack_success"] = int(gd["ack_success"])
                mar["ack_error"] = int(gd["ack_error"])
                continue

            # QFP Match Delete: 0, ACK Success: 0, ACK Error: 0
            m = p10.match(line)
            if m:
                gd = m.groupdict()
                qfp = fm_stats.setdefault("qfp", {})
                md = qfp.setdefault("match_delete", {})
                md["delete"] = int(gd["delete"])
                md["ack_success"] = int(gd["ack_success"])
                md["ack_error"] = int(gd["ack_error"])
                continue

            # QFP Action Edit: 0, ACK Success: 0, ACK Error: 0
            m = p11.match(line)
            if m:
                gd = m.groupdict()
                qfp = fm_stats.setdefault("qfp", {})
                ae = qfp.setdefault("action_edit", {})
                ae["count"] = int(gd["count"])
                ae["ack_success"] = int(gd["ack_success"])
                ae["ack_error"] = int(gd["ack_error"])
                continue

            # QFP Action Replace: 0, ACK Success: 0, ACK Error: 0
            m = p12.match(line)
            if m:
                gd = m.groupdict()
                qfp = fm_stats.setdefault("qfp", {})
                ar = qfp.setdefault("action_replace", {})
                ar["count"] = int(gd["count"])
                ar["ack_success"] = int(gd["ack_success"])
                ar["ack_error"] = int(gd["ack_error"])
                continue

            # QFP Bind: 0, ACK Success: 0, ACK Error: 0
            m = p13.match(line)
            if m:
                gd = m.groupdict()
                qfp = fm_stats.setdefault("qfp", {})
                bind = qfp.setdefault("bind", {})
                bind["count"] = int(gd["count"])
                bind["ack_success"] = int(gd["ack_success"])
                bind["ack_error"] = int(gd["ack_error"])
                continue

            # QFP Unbind: 0, ACK Success: 0, ACK Error: 0
            m = p14.match(line)
            if m:
                gd = m.groupdict()
                qfp = fm_stats.setdefault("qfp", {})
                unbind = qfp.setdefault("unbind", {})
                unbind["count"] = int(gd["count"])
                unbind["ack_success"] = int(gd["ack_success"])
                unbind["ack_error"] = int(gd["ack_error"])
                continue

        return ret_dict
