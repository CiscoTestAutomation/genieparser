"""show_platform_software.py

    * 'show platform software yang-management process'
    * 'show platform software yang-management process monitor'
    * 'show platform software yang-management process state'
    * 'show platform software object-manager {switch} {switch_type} F0 error-object'
    * 'show platform software object-manager {switch} {switch_type} F0 statistics'
    * 'show platform software object-manager {switch} {switch_type} F0 pending-ack-update'
    * 'show platform software dpidb index'
    * 'show platform software interface switch {mode} F0 brief'
    * 'show platform software dns-umbrella statistics'
    * 'show platform software cpm switch {mode} B0 counters drop'
    * 'show platform software cpm switch {mode} B0 counters punt-inject'
    * 'show platform software cpm switch {mode} B0 ipc brief'
    * 'show platform software cpm switch {mode} B0 ipc detail'
    * 'show platform software install-manager RP active operation history summary'
    * 'show platform software install-manager switch active r0 operation history summary'
    * 'show platform software object-manager switch {switchstate} {serviceprocessor} active statistics'
    * 'show platform software object-manager FP active statistics'
    * 'show platform software bp crimson content config'
    * 'show platform software node cluster-manager switch {mode} B0 node {node}'
    * 'show platform software factory-reset secure log'
    * 'show platform software wired-client switch {switch_state} r0'
    * 'show platform software monitor session {session}'
    * 'show platform software install-manager chassis active r0 operation history summary'
    * 'show platform software audit summary'
    * 'show platform software steering-policy forwarding-manager switch {switch} F0 policy-aom-info'
    * 'show platform software steering-policy forwarding-manager F0 policy-aom-info'
    * 'show platform software object-manager switch {switch} F0 object {object}'
    * 'show platform software memory database fed {switch} {switch_var} callsite'
    * 'show platform software memory database fed {switch_var} callsite'
    * 'show platform soft infra bipc | inc buffer'
"""

# Python
import re
import logging
from collections import OrderedDict
from sys import int_info
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And
from genie.libs.parser.utils.common import Common
from genie.parsergen import oper_fill_tabular

# genie.parsergen
try:
    import genie.parsergen
except (ImportError, OSError):
    pass

# pyATS
from pyats.utils.exceptions import SchemaTypeError

log = logging.getLogger(__name__)


class ShowPlatformSoftwareSlotActiveMonitorMemSchema(MetaParser):
    """Schema for show platform software process slot switch active R0 monitor | inc Mem :|Swap:"""

    schema = {
        "memory": {"total": int, "free": int, "used": int, "buff_cache": int},
        "swap": {"total": int, "free": int, "used": int, "available_memory": int},
    }


class ShowPlatformSoftwareSlotActiveMonitorMem(
    ShowPlatformSoftwareSlotActiveMonitorMemSchema
):
    """Parser for show platform software process slot switch active R0 monitor | inc Mem :|Swap:"""

    cli_command = (
        "show platform software process slot switch active R0 monitor | inc Mem :|Swap:"
    )

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(
            r"^KiB +Mem *: +(?P<total>\d+) *total, +"
            "(?P<free>\d+) *free, +(?P<used>\d+) *used, +"
            "(?P<buff_cache>\d+) *buff\/cache$"
        )

        p2 = re.compile(
            r"^KiB +Swap *: +(?P<total>\d+) *total, +"
            "(?P<free>\d+) *free, +(?P<used>\d+) *used. +"
            "(?P<available_memory>\d+) *avail +Mem$"
        )

        for line in out.splitlines():
            line = line.strip()

            # KiB Mem :  4010000 total,    16756 free,  1531160 used,  2462084 buff/cache
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name_dict = ret_dict.setdefault("memory", {})
                name_dict.update({k: int(v) for k, v in group.items()})
                continue

            # KiB Swap:        0 total,        0 free,        0 used.  1778776 avail Mem
            m = p2.match(line)
            if m:
                group = m.groupdict()
                name_dict = ret_dict.setdefault("swap", {})
                name_dict.update({k: int(v) for k, v in group.items()})
                continue
        return ret_dict


class ShowPlatformSoftwareStatusControlSchema(MetaParser):
    """Schema for show platform software status control-processor brief"""

    schema = {
        "slot": {
            Any(): {
                "load_average": {
                    "status": str,
                    "1_min": float,
                    "5_min": float,
                    "15_min": float,
                },
                "memory": {
                    "status": str,
                    "total": int,
                    "used": int,
                    "used_percentage": int,
                    "free": int,
                    "free_percentage": int,
                    "committed": int,
                    "committed_percentage": int,
                },
                "cpu": {
                    Any(): {
                        "user": float,
                        "system": float,
                        "nice_process": float,
                        "idle": float,
                        "irq": float,
                        "sirq": float,
                        "waiting": float,
                    }
                },
            }
        }
    }


class ShowPlatformSoftwareStatusControl(ShowPlatformSoftwareStatusControlSchema):
    """Parser for show platform software status control-processor brief"""

    cli_command = "show platform software status control-processor brief"
    exclude = [
        "idle",
        "system",
        "user",
        "1_min",
        "5_min",
        "15_min",
        "free",
        "used",
        "sirq",
        "waiting",
        "committed",
    ]

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(
            r"^(?P<slot>\S+) +(?P<status>\w+) +"
            "(?P<min1>[\d\.]+) +(?P<min5>[\d\.]+) +(?P<min15>[\d\.]+)$"
        )

        p2 = re.compile(
            r"^(?P<slot>\S+) +(?P<status>\w+) +"
            "(?P<total>\d+) +(?P<used>\d+) +\((?P<used_percentage>[\d\s]+)\%\) +"
            "(?P<free>\d+) +\((?P<free_percentage>[\d\s]+)\%\) +"
            "(?P<committed>\d+) +\((?P<committed_percentage>[\d\s]+)\%\)$"
        )

        p3 = re.compile(
            r"^((?P<slot>\S+) +)?(?P<cpu>\d+) +(?P<user>[\d\.]+) +(?P<system>[\d\.]+) +(?P<nice_process>[\d\.]+) +(?P<idle>[\d\.]+) +(?P<irq>[\d\.]+) +(?P<sirq>[\d\.]+) +(?P<waiting>[\d\.]+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # Slot  Status  1-Min  5-Min 15-Min
            # 1-RP0 Healthy   0.26   0.35   0.33
            m = p1.match(line)
            if m:
                group = m.groupdict()
                slot = group.pop("slot").lower()
                load_dict = (
                    ret_dict.setdefault("slot", {})
                    .setdefault(slot, {})
                    .setdefault("load_average", {})
                )
                load_dict["status"] = group["status"].lower()
                load_dict["1_min"] = float(group["min1"])
                load_dict["5_min"] = float(group["min5"])
                load_dict["15_min"] = float(group["min15"])
                continue

            # Slot  Status    Total     Used (Pct)     Free (Pct) Committed (Pct)
            # 1-RP0 Healthy  4010000  2553084 (64%)  1456916 (36%)   3536536 (88%)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                slot = group.pop("slot").lower()
                mem_dict = (
                    ret_dict.setdefault("slot", {})
                    .setdefault(slot, {})
                    .setdefault("memory", {})
                )
                mem_dict["status"] = group.pop("status").lower()
                mem_dict.update({k: int(v) for k, v in group.items()})
                continue

            #  Slot  CPU   User System   Nice   Idle    IRQ   SIRQ IOwait
            # 1-RP0    0   3.89   2.09   0.00  93.80   0.00   0.19   0.00
            #          1   5.70   1.00   0.00  93.20   0.00   0.10   0.00
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if group["slot"]:
                    slot = group.pop("slot").lower()
                else:
                    group.pop("slot")
                cpu = group.pop("cpu")
                cpu_dict = (
                    ret_dict.setdefault("slot", {})
                    .setdefault(slot, {})
                    .setdefault("cpu", {})
                    .setdefault(cpu, {})
                )
                cpu_dict.update({k: float(v) for k, v in group.items()})
                continue
        return ret_dict


class ShowPlatformSoftwareMemoryCallsiteSchema(MetaParser):
    """Schema for show platform software memory <process> switch active <R0> alloc callsite brief"""

    schema = {
        "tracekey": str,
        "callsites": {Any(): {"thread": int, "diff_byte": int, "diff_call": int}},
    }


class ShowPlatformSoftwareMemoryCallsite(ShowPlatformSoftwareMemoryCallsiteSchema):
    """Parser for show platform software memory <process> <hw> active <R0> alloc callsite brief"""

    cli_command = [
        "show platform software memory {process} {hw} active {slot} alloc callsite brief",
        "show platform software memory {process} {hw} active alloc callsite brief",
    ]

    def cli(self, process, slot=None, hw="switch", output=None):
        if output is None:
            if slot is not None:
                out = self.device.execute(
                    self.cli_command[0].format(process=process, hw=hw, slot=slot)
                )
            else:
                out = self.device.execute(
                    self.cli_command[1].format(process=process, hw=hw)
                )

        # Init vars
        parsed_dict = {}
        if out:
            callsite_dict = parsed_dict.setdefault("callsites", {})

        # The current tracekey is   : 1#2315ece11e07bc883d89421df58e37b6
        p1 = re.compile(r"The +current +tracekey +is\s*: +(?P<tracekey>[#\d\w]*)")

        # callsite      thread    diff_byte               diff_call
        # ----------------------------------------------------------
        # 1617611779    31884     57424                   2
        # 16A761F779    31884     37424                   21
        p2 = re.compile(
            r"(?P<callsite>([0-9a-fA-F]+))\s+(?P<thread>(\d+))\s+(?P<diffbyte>(\d+))\s+(?P<diffcall>(\d+))"
        )

        for line in out.splitlines():
            line = line.strip()

            # The current tracekey is   : 1#2315ece11e07bc883d89421df58e37b6
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict["tracekey"] = str(group["tracekey"])
                continue

            # callsite      thread    diff_byte               diff_call
            # ----------------------------------------------------------
            # 1617611779    31884     57424                   2
            # 16A761C7F9    31884     27454                   19
            m = p2.match(line)
            if m:
                group = m.groupdict()
                callsite = group["callsite"]
                one_callsite_dict = callsite_dict.setdefault(callsite, {})
                one_callsite_dict["thread"] = int(group["thread"])
                one_callsite_dict["diff_byte"] = int(group["diffbyte"])
                one_callsite_dict["diff_call"] = int(group["diffcall"])
                continue

        return parsed_dict


class ShowPlatformSoftwareMemoryBacktraceSchema(MetaParser):
    """Schema for show platform software memory <process> switch active <R0> alloc backtrace"""

    schema = {
        "backtraces": {
            Any(): {
                "allocs": int,
                "frees": int,
                "call_diff": int,
                "callsite": str,
                "thread_id": int,
            }
        }
    }


class ShowPlatformSoftwareMemoryBacktrace(ShowPlatformSoftwareMemoryBacktraceSchema):
    """Parser for show platform software memory <process> switch active <R0> alloc backtrace"""

    cli_command = (
        "show platform software memory {process} switch active {slot} alloc backtrace"
    )

    def cli(self, process, slot, output=None):
        if output is None:
            out = self.device.execute(
                self.cli_command.format(process=process, slot=slot)
            )
        else:
            out = output

        # Init vars
        parsed_dict = {}
        if out:
            backtraces_dict = parsed_dict.setdefault("backtraces", {})

        # backtrace: 1#2315ece11e07bc883d89421df58e37b6   maroon:7F740DEDC000+61F6 tdllib:7F7474D05000+B2B46 ui:7F74770E4000+4639A ui:7F74770E4000+4718C cdlcore:7F7466A6B000+37C95 cdlcore:7F7466A6B000+37957 uipeer:7F747A7A8000+24F2A evutil:7F747864E000+7966 evutil:7F747864E000+7745
        p1 = re.compile(r"backtrace: (?P<backtrace>[\w#\d\s:+]+)$")

        #   callsite: 2150603778, thread_id: 31884
        p2 = re.compile(
            r"callsite: +(?P<callsite>\d+), +thread_id: +(?P<thread_id>\d+)"
        )

        #   allocs: 1, frees: 0, call_diff: 1
        p3 = re.compile(
            r"allocs: +(?P<allocs>(\d+)), +frees: +(?P<frees>(\d+)), +call_diff: +(?P<call_diff>(\d+))"
        )

        for line in out.splitlines():
            line = line.strip()

            # backtrace: 1#2315ece11e07bc883d89421df58e37b6   maroon:7F740DEDC000+61F6 tdllib:7F7474D05000+B2B46 ui:7F74770E4000+4639A ui:7F74770E4000+4718C cdlcore:7F7466A6B000+37C95 cdlcore:7F7466A6B000+37957 uipeer:7F747A7A8000+24F2A evutil:7F747864E000+7966 evutil:7F747864E000+7745
            m = p1.match(line)
            if m:
                group = m.groupdict()
                backtrace = str(group["backtrace"])
                one_backtrace_dict = backtraces_dict.setdefault(backtrace, {})
                continue

            #   callsite: 2150603778, thread_id: 31884
            m = p2.match(line)
            if m:
                group = m.groupdict()
                one_backtrace_dict["callsite"] = group["callsite"]
                one_backtrace_dict["thread_id"] = int(group["thread_id"])
                continue

            #   allocs: 1, frees: 0, call_diff: 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                one_backtrace_dict["allocs"] = int(group["allocs"])
                one_backtrace_dict["frees"] = int(group["frees"])
                one_backtrace_dict["call_diff"] = int(group["call_diff"])
                continue

        return parsed_dict


class ShowPlatformSoftwareYangManagementProcessSchema(MetaParser):
    """schema for
    * show platform software yang-management process
    """

    schema = {str: str}


class ShowPlatformSoftwareYangManagementProcess(
    ShowPlatformSoftwareYangManagementProcessSchema
):
    """parser for
    * show platform software yang-management process
    """

    cli_command = "show platform software yang-management process"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # confd            : Running
        # pubd             : Running
        # gnmib            : Not Running
        p1 = re.compile(r"^(?P<key>\S+) *: +(?P<data>(Running|Not +Running))$")

        ret_dict = dict()

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({group["key"]: group["data"]})
                continue

        return ret_dict


class ShowPlatformSoftwareYangManagementProcessMonitorSchema(MetaParser):
    """schema for
    * show platform software yang-management process monitor
    """

    schema = {
        "pid": {
            int: {
                "command": str,
                "state": str,
                "vsz": int,
                "rss": int,
                "cpu": float,
                "mem": float,
                "elapsed": str,
            }
        }
    }


class ShowPlatformSoftwareYangManagementProcessMonitor(
    ShowPlatformSoftwareYangManagementProcessMonitorSchema
):
    """parser for
    * show platform software yang-management process monitor
    """

    cli_command = "show platform software yang-management process monitor"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # dmiauthd          551 S 376940 49600  0.0  0.6    21:44:33
        # ncsshd           1503 S 301344 17592  0.0  0.2    21:44:32
        p1 = re.compile(
            r"^(?P<command>\S+) +(?P<pid>\d+) +(?P<s>\S+) +(?P<vsz>\d+) +"
            r"(?P<rss>\d+) +(?P<cpu>\S+) +(?P<mem>\S+) +(?P<elapsed>\S+)$"
        )

        ret_dict = dict()

        for line in out.splitlines():
            line = line.strip()

            # dmiauthd          551 S 376940 49600  0.0  0.6    21:44:33
            # ncsshd           1503 S 301344 17592  0.0  0.2    21:44:32
            m = p1.match(line)
            if m:
                group = m.groupdict()
                commands = ret_dict.setdefault("pid", {})
                command = commands.setdefault(int(group["pid"]), {})
                command.update(
                    {
                        "command": group["command"],
                        "state": group["s"],
                        "vsz": int(group["vsz"]),
                        "rss": int(group["rss"]),
                        "cpu": float(group["cpu"]),
                        "mem": float(group["mem"]),
                        "elapsed": group["elapsed"],
                    }
                )
                continue

        return ret_dict


class ShowPlatformSoftwareYangManagementProcessStateSchema(MetaParser):
    """schema for
    * show platform software yang-management process state
    """

    schema = {
        "confd-status": str,
        "processes": {
            str: {
                "status": str,
                "state": str,
            },
        },
    }


class ShowPlatformSoftwareYangManagementProcessState(
    ShowPlatformSoftwareYangManagementProcessStateSchema
):
    """parser for
    * show platform software yang-management process state
    """

    cli_command = "show platform software yang-management process state"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Confd Status: Started
        # Confd Status: Not Running
        p1 = re.compile(r"^Confd +Status: +(?P<status>.+)$")

        # pubd                 Running             Active
        # gnmib                Not Running         Not Applicable
        # ndbmand              Not Running         Down
        # pubd                 Running             Reset
        p2 = re.compile(
            r"^(?P<process>\S+) +(?P<status>(Running|Not +Running)) +"
            r"(?P<state>(Active|Not +Active|Not +Applicable|Down|Reset|Init|Failed|Invalid))$"
        )

        ret_dict = dict()

        for line in out.splitlines():
            line = line.strip()

            # Confd Status: Started
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["confd-status"] = group["status"]
                continue

            # pubd                 Running             Active
            # gnmib                Not Running         Not Applicable
            # ndbmand              Not Running         Down
            m = p2.match(line)
            if m:
                group = m.groupdict()
                commands = ret_dict.setdefault("processes", {})
                command = commands.setdefault(group["process"], {})
                command.update(
                    {
                        "status": group["status"],
                        "state": group["state"],
                    }
                )
                continue

        return ret_dict


class ShowPlatformSoftwareMemoryRpActiveSchema(MetaParser):
    """Schema for
    * show platform software memory mdt-pubd RP active
    """

    schema = {
        "module": {
            Any(): {
                "allocated": int,
                "requested": int,
                "overhead": int,
                Optional("allocations"): int,
                Optional("failed"): int,
                Optional("frees"): int,
            }
        }
    }


class ShowPlatformSoftwareMemoryRpActive(ShowPlatformSoftwareMemoryRpActiveSchema):
    """Parser for
    * show platform software memory mdt-pubd RP active
    """

    cli_command = "show platform software memory {process} RP active"

    def cli(self, process, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(process=process))
        else:
            out = output

        ret_dict = {}

        # Module: process
        p1 = re.compile(r"Module: +(?P<module>[\S\s]+)$")

        # allocated: 16695, requested: 16647, overhead: 48
        p2 = re.compile(
            r"allocated: +(?P<allocated>\d+), +requested: +"
            r"(?P<requested>\d+), +overhead: +(?P<overhead>\d+)$"
        )

        # Allocations: 3, failed: 0, frees: 0
        p3 = re.compile(
            r"Allocations: +(?P<allocations>\d+), +failed: +"
            r"(?P<failed>\d+), +frees: +(?P<frees>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # Module: process
            m = p1.match(line)
            if m:
                group = m.groupdict()
                module = group.get("module")
                module_dict = ret_dict.setdefault("module", {}).setdefault(module, {})
                continue

            # allocated: 16695, requested: 16647, overhead: 48
            m = p2.match(line)
            if m:
                group = m.groupdict()
                module_dict.update(
                    {k: int(v) for k, v in group.items() if v is not None}
                )
                continue

            # Allocations: 3, failed: 0, frees: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                module_dict.update(
                    {k: int(v) for k, v in group.items() if v is not None}
                )
                continue

        return ret_dict


class ShowPlatformSoftwareMemorySwitchActive(ShowPlatformSoftwareMemoryRpActive):
    """Parser for
    * show platform software memory mdt-pubd switch active <R0>
    """

    cli_command = "show platform software memory {process} switch active {slot}"

    def cli(self, process, slot, output=None):
        if output is None:
            out = self.device.execute(
                self.cli_command.format(process=process, slot=slot)
            )
        else:
            out = output

        return super().cli(process=process, output=out)


class ShowPlatformSoftwareMemoryChassisActive(ShowPlatformSoftwareMemoryRpActive):
    """Parser for
    * show platform software memory mdt-pubd chassis active <R0>
    """

    cli_command = "show platform software memory {process} chassis active {slot}"

    def cli(self, process, slot, output=None):
        if output is None:
            out = self.device.execute(
                self.cli_command.format(process=process, slot=slot)
            )
        else:
            out = output

        return super().cli(process=process, output=out)


class ShowPlatformSoftwareMemoryRpActiveBriefSchema(MetaParser):
    """Schema for
    * show platform software memory mdt-pubd RP active brief
    """

    schema = {
        "module": {
            Any(): {
                "allocated": int,
                "requested": int,
                "allocs": int,
                "frees": int,
            }
        }
    }


class ShowPlatformSoftwareMemoryRpActiveBrief(
    ShowPlatformSoftwareMemoryRpActiveBriefSchema
):
    """Parser for
    * show platform software memory mdt-pubd RP active brief
    """

    cli_command = "show platform software memory {process} RP active brief"

    def cli(self, process, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(process=process))
        else:
            out = output

        ret_dict = {}

        # Summary                 420136        364136        3706          206
        p1 = re.compile(
            r"^(?P<module>\S+) +(?P<allocated>\d+) +"
            r"(?P<requested>\d+) +(?P<allocs>\d+) +(?P<frees>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # Summary                 420136        364136        3706          206
            m = p1.match(line)
            if m:
                group = m.groupdict()
                module = group.pop("module")
                module_dict = ret_dict.setdefault("module", {}).setdefault(module, {})
                module_dict.update(
                    {k: int(v) for k, v in group.items() if v is not None}
                )
                continue

        return ret_dict


class ShowPlatformSoftwareMemorySwitchActiveBrief(
    ShowPlatformSoftwareMemoryRpActiveBrief
):
    """Parser for
    * show platform software memory mdt-pubd switch active R0 brief
    """

    cli_command = "show platform software memory {process} switch active {slot} brief"

    def cli(self, process, slot, output=None):
        if output is None:
            out = self.device.execute(
                self.cli_command.format(process=process, slot=slot)
            )
        else:
            out = output

        return super().cli(process=process, output=out)


class ShowPlatformSoftwareMemoryChassisActiveBrief(
    ShowPlatformSoftwareMemoryRpActiveBrief
):
    """Parser for
    * show platform software memory mdt-pubd chassis active R0 brief
    """

    cli_command = "show platform software memory {process} chassis active {slot} brief"

    def cli(self, process, slot, output=None):
        if output is None:
            out = self.device.execute(
                self.cli_command.format(process=process, slot=slot)
            )
        else:
            out = output

        return super().cli(process=process, output=out)


class ShowPlatformSoftwareMemoryRpActiveAllocCallsiteSchema(MetaParser):
    """Schema for
    * show platform software memory mdt-pubd RP active alloc callsite
    """

    schema = {
        "callsite": {
            Any(): {
                "thread_id": int,
                "allocs": int,
                "frees": int,
                "alloc_bytes": int,
                "free_bytes": int,
                "call_diff": int,
                "byte_diff": int,
            }
        }
    }


class ShowPlatformSoftwareMemoryRpActiveAllocCallsite(
    ShowPlatformSoftwareMemoryRpActiveAllocCallsiteSchema
):
    """Parser for
    * show platform software memory mdt-pubd RP active alloc callsite
    """

    cli_command = "show platform software memory {process} RP active alloc callsite"

    def cli(self, process, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(process=process))
        else:
            out = output

        ret_dict = {}

        # callsite: 1355696130, thread_id: 24813
        p1 = re.compile(
            r"^callsite: +(?P<callsite>\d+), +thread_id: +(?P<thread_id>\d+)$"
        )

        # allocs: 138151, frees: 138141, alloc_bytes: 15466123, free_bytes: 15464846, call_diff: 10, byte_diff: 1277
        p2 = re.compile(
            r"^allocs: +(?P<allocs>\d+), +frees: +(?P<frees>\d+), +"
            r"alloc_bytes: +(?P<alloc_bytes>\d+), +free_bytes: +(?P<free_bytes>\d+), +"
            r"call_diff: +(?P<call_diff>\d+), +byte_diff: +(?P<byte_diff>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # callsite: 1355696130, thread_id: 24813
            m = p1.match(line)
            if m:
                group = m.groupdict()
                callsite = group.get("callsite")
                thread_id = group.get("thread_id")
                thread_dict = ret_dict.setdefault("callsite", {}).setdefault(
                    callsite, {}
                )
                thread_dict.update({"thread_id": int(thread_id)})
                continue

            # allocs: 138151, frees: 138141, alloc_bytes: 15466123, free_bytes: 15464846, call_diff: 10, byte_diff: 1277
            m = p2.match(line)
            if m:
                group = m.groupdict()
                thread_dict.update(
                    {k: int(v) for k, v in group.items() if v is not None}
                )
                continue

        return ret_dict


class ShowPlatformSoftwareMemorySwitchActiveAllocCallsite(
    ShowPlatformSoftwareMemoryRpActiveAllocCallsite
):
    """Parser for
    * show platform software memory mdt-pubd switch active <R0> alloc callsite
    """

    cli_command = (
        "show platform software memory {process} switch active {slot} alloc callsite"
    )

    def cli(self, process, slot, output=None):
        if output is None:
            out = self.device.execute(
                self.cli_command.format(process=process, slot=slot)
            )
        else:
            out = output

        return super().cli(process=process, output=out)


class ShowPlatformSoftwareMemoryRpActiveAllocCallsiteBriefSchema(MetaParser):
    """Schema for
    * show platform software memory mdt-pubd RP active alloc callsite
    """

    schema = {
        "tracekey": str,
        "callsite": {
            Any(): {
                "thread_id": int,
                "diff_byte": int,
                "diff_call": int,
            }
        },
    }


class ShowPlatformSoftwareMemoryRpActiveAllocCallsiteBrief(
    ShowPlatformSoftwareMemoryRpActiveAllocCallsiteBriefSchema
):
    """Parser for
    * show platform software memory mdt-pubd RP active alloc callsite brief
    """

    cli_command = (
        "show platform software memory {process} RP active alloc callsite brief"
    )

    def cli(self, process, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(process=process))
        else:
            out = output

        ret_dict = {}

        # callsite: 1355696130, thread_id: 24813
        p1 = re.compile(r"^The +current +tracekey +is +: +(?P<tracekey>\S+)$")

        # allocs: 138151, frees: 138141, alloc_bytes: 15466123, free_bytes: 15464846, call_diff: 10, byte_diff: 1277
        p2 = re.compile(
            r"^(?P<callsite>\d+) +(?P<thread_id>\d+) +(?P<diff_byte>\d+) +(?P<diff_call>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({"tracekey": group["tracekey"]})
                continue

            # callsite: 1355696130, thread_id: 24813
            m = p2.match(line)
            if m:
                group = m.groupdict()
                callsite = group.pop("callsite")
                thread_id = group.pop("thread_id")
                thread_dict = ret_dict.setdefault("callsite", {}).setdefault(
                    callsite, {}
                )
                thread_dict.update({"thread_id": int(thread_id)})
                thread_dict.update(
                    {k: int(v) for k, v in group.items() if v is not None}
                )
                continue

        return ret_dict


class ShowPlatformSoftwareMemoryRpActiveAllocTypeSchema(MetaParser):
    """Schema for
    * show platform software memory mdt-pubd RP active alloc type component
    """

    schema = {
        Optional("module"): {
            Any(): {
                "allocated": int,
                "requested": int,
                "overhead": int,
                "allocations": int,
                "null_allocations": int,
                "frees": int,
            }
        },
        Optional("type"): {
            Any(): {
                "allocated": int,
                "requested": int,
                "overhead": int,
                "allocations": int,
                "null_allocations": int,
                "frees": int,
            }
        },
    }


class ShowPlatformSoftwareMemoryRpActiveAllocType(
    ShowPlatformSoftwareMemoryRpActiveAllocTypeSchema
):
    """Parser for
    * show platform software memory mdt-pubd RP active alloc type component
    * show platform software memory mdt-pubd RP active alloc type data
    """

    cli_command = (
        "show platform software memory {process} RP active alloc type {alloc_type}"
    )

    def cli(self, process, alloc_type, output=None):
        if output is None:
            out = self.device.execute(
                self.cli_command.format(process=process, alloc_type=alloc_type)
            )
        else:
            out = output

        ret_dict = {}

        # Module: process
        p1 = re.compile(r"Module: +(?P<module>[\S\s]+)$")

        # Type: process
        p1_1 = re.compile(r"Type: +(?P<type>[\S\s]+)$")

        # allocated: 16695, requested: 16647, overhead: 48
        p2 = re.compile(
            r"Allocated: +(?P<allocated>\d+), +"
            r"Requested: +(?P<requested>\d+), +Overhead: +(?P<overhead>\d+)$"
        )

        # Allocations: 3, failed: 0, frees: 0
        p3 = re.compile(
            r"Allocations: +(?P<allocations>\d+), +Null +Allocations: +"
            r"(?P<null_allocations>\d+), +Frees: +(?P<frees>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # Module: process
            m = p1.match(line)
            if m:
                group = m.groupdict()
                module = group.get("module")
                module_dict = ret_dict.setdefault("module", {}).setdefault(module, {})
                continue

            # type: process
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                module = group.get("type")
                module_dict = ret_dict.setdefault("type", {}).setdefault(module, {})
                continue

            # allocated: 16695, requested: 16647, overhead: 48
            m = p2.match(line)
            if m:
                group = m.groupdict()
                module_dict.update(
                    {k: int(v) for k, v in group.items() if v is not None}
                )
                continue

            # Allocations: 3, failed: 0, frees: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                module_dict.update(
                    {k: int(v) for k, v in group.items() if v is not None}
                )
                continue

        return ret_dict


class ShowPlatformSoftwareMemorySwitchActiveAllocType(
    ShowPlatformSoftwareMemoryRpActiveAllocType
):
    """Parser for
    * show platform software memory mdt-pubd switch active <R0> alloc type component
    """

    cli_command = "show platform software memory {process} switch active {slot} alloc type {alloc_type}"

    def cli(self, process, slot, alloc_type, output=None):
        if output is None:
            out = self.device.execute(
                self.cli_command.format(
                    process=process, slot=slot, alloc_type=alloc_type
                )
            )
        else:
            out = output

        return super().cli(process=process, output=out, alloc_type=alloc_type)


class ShowPlatformSoftwareMemoryRpActiveAllocTypeBriefSchema(MetaParser):
    """Schema for
    * show platform software memory mdt-pubd RP active alloc type component brief
    """

    schema = {
        "type": {
            Any(): {
                "allocated": int,
                "requested": int,
                "allocations": int,
                "frees": int,
            }
        }
    }


class ShowPlatformSoftwareMemoryRpActiveAllocTypeBrief(
    ShowPlatformSoftwareMemoryRpActiveAllocTypeBriefSchema
):
    """Parser for
    * show platform software memory mdt-pubd RP active alloc type component brief
    """

    cli_command = "show platform software memory {process} RP active alloc type {alloc_type} brief"

    def cli(self, process, alloc_type, output=None):
        if output is None:
            out = self.device.execute(
                self.cli_command.format(process=process, alloc_type=alloc_type)
            )
        else:
            out = output

        ret_dict = {}

        # Summary                 4989412       4501988       150851        142147
        p1 = re.compile(
            r"(?P<type>\S+) +(?P<allocated>\d+) +"
            r"(?P<requested>\d+) +(?P<allocations>\d+) +(?P<frees>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # Summary                 4989412       4501988       150851        142147
            m = p1.match(line)
            if m:
                group = m.groupdict()
                module = group.pop("type")
                module_dict = ret_dict.setdefault("type", {}).setdefault(module, {})
                module_dict.update(
                    {k: int(v) for k, v in group.items() if v is not None}
                )
                continue

        return ret_dict


class ShowPlatformSoftwareMemorySwitchActiveAllocTypeBrief(
    ShowPlatformSoftwareMemoryRpActiveAllocTypeBrief
):
    """Parser for
    * show platform software memory mdt-pubd switch active <R0> alloc type component brief
    """

    cli_command = "show platform software memory {process} switch active {slot} alloc type {alloc_type} brief"

    def cli(self, process, slot, alloc_type, output=None):
        if output is None:
            out = self.device.execute(
                self.cli_command.format(
                    process=process, slot=slot, alloc_type=alloc_type
                )
            )
        else:
            out = output

        return super().cli(process=process, alloc_type=alloc_type, output=out)


class ShowPlatformSoftwareIomdMacsecInterfaceBriefSchema(MetaParser):
    """Schema for
    * show platform software iomd 1/0 macsec interface {interface} brief
    """

    schema = {
        Optional("tx-sc"): {
            Any(): {
                "sub-interface": str,
                "sc-idx": str,
                "pre-cur-an": str,
                "sci": str,
                "sa-vp-rule-idx": str,
                "cipher": str,
            }
        },
        Optional("rx-sc"): {
            Any(): {
                "sub-interface": str,
                "sc-idx": str,
                "pre-cur-an": str,
                "sci": str,
                "sa-vp-rule-idx": str,
                "cipher": str,
            }
        },
    }


class ShowPlatformSoftwareIomdMacsecInterfaceBrief(
    ShowPlatformSoftwareIomdMacsecInterfaceBriefSchema
):
    """Parser for
    * show platform software iomd 1/0 macsec interface {interface} brief
    """

    cli_command = "show platform software iomd 1/0 macsec interface {interface} brief"

    def cli(self, interface, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        ret_dict = {}
        # Tx SC
        p1 = re.compile(r"(.*)Tx SC")

        # Rx SC
        p2 = re.compile(r"(.*)Rx SC")

        # 3/11  |   0    |     3/0    | f87a41252702008b | 50331759/ 2/ 1  |     GCM_AES_128 |
        p3 = re.compile(
            r"(?P<if>\d+\/\d+) +\|"
            " +(?P<sc_idx>\d+) +\|"
            " +(?P<pre_cur_an>\d+\/\d+) +\|"
            " +(?P<sci>\S+) +\|"
            " +(?P<idx>\d+\/ \d+\/ \d+) +\|"
            " +(?P<cipher>\S+) +\|"
        )

        sess_tx = 0
        sess_rx = 0
        for line in out.splitlines():
            line = line.strip()
            m1 = p1.match(line)
            if m1:
                sc = "tx"
                tx_sc = ret_dict.setdefault("tx-sc", {})
            m2 = p2.match(line)
            if m2:
                sc = "rx"
                rx_sc = ret_dict.setdefault("rx-sc", {})
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                if sc == "tx":
                    sess_tx += 1
                    sc_tx_dict = tx_sc.setdefault(sess_tx, {})
                    sc_tx_dict["sub-interface"] = group["if"]
                    sc_tx_dict["sc-idx"] = group["sc_idx"]
                    sc_tx_dict["pre-cur-an"] = group["pre_cur_an"]
                    sc_tx_dict["sci"] = group["sci"]
                    sc_tx_dict["sa-vp-rule-idx"] = group["idx"]
                    sc_tx_dict["cipher"] = group["cipher"]
                elif sc == "rx":
                    sess_rx += 1
                    sc_rx_dict = rx_sc.setdefault(sess_rx, {})
                    sc_rx_dict["sub-interface"] = group["if"]
                    sc_rx_dict["sc-idx"] = group["sc_idx"]
                    sc_rx_dict["pre-cur-an"] = group["pre_cur_an"]
                    sc_rx_dict["sci"] = group["sci"]
                    sc_rx_dict["sa-vp-rule-idx"] = group["idx"]
                    sc_rx_dict["cipher"] = group["cipher"]
        return ret_dict


class ShowPlatformSoftwareIomdMacsecInterfaceDetailSchema(MetaParser):
    """Schema for
    * show platform software iomd 1/0 macsec interface {interface} detail
    """

    schema = {
        Optional("subport-11-tx"): {
            "bypass": str,
            "cipher": str,
            "conf-offset": str,
            "cur-an": str,
            "delay-protection": str,
            "encrypt": str,
            "end-station": str,
            "hashkey-len": str,
            "key-len": str,
            "next-pn": str,
            "prev-an": str,
            "rule-index": str,
            "sa-index": str,
            "scb": str,
            "sci": str,
            "vlan": str,
            "vport-index": str,
        },
        Optional("subport-12-tx"): {
            "bypass": str,
            "cipher": str,
            "conf-offset": str,
            "cur-an": str,
            "delay-protection": str,
            "encrypt": str,
            "end-station": str,
            "hashkey-len": str,
            "key-len": str,
            "next-pn": str,
            "prev-an": str,
            "rule-index": str,
            "sa-index": str,
            "scb": str,
            "sci": str,
            "vlan": str,
            "vport-index": str,
        },
        Optional("subport-11-rx"): {
            "bypass": str,
            "cipher": str,
            "conf-offset": str,
            "cur-an": str,
            "decrypt-frames": str,
            "hashkey-len": str,
            "key-len": str,
            "next-pn": str,
            "prev-an": str,
            "replay-protect": str,
            "replay-window-size": str,
            "rule-index": str,
            "sa-index": str,
            "sci": str,
            "validate-frames": str,
            "vport-index": str,
        },
        Optional("subport-12-rx"): {
            "bypass": str,
            "cipher": str,
            "conf-offset": str,
            "cur-an": str,
            "decrypt-frames": str,
            "hashkey-len": str,
            "key-len": str,
            "next-pn": str,
            "prev-an": str,
            "replay-protect": str,
            "replay-window-size": str,
            "rule-index": str,
            "sa-index": str,
            "sci": str,
            "validate-frames": str,
            "vport-index": str,
        },
    }


class ShowPlatformSoftwareIomdMacsecInterfaceDetail(
    ShowPlatformSoftwareIomdMacsecInterfaceDetailSchema
):
    """Parser for
    * show platform software iomd 1/0 macsec interface {interface} detail
    """

    cli_command = "show platform software iomd 1/0 macsec interface {interface} detail"

    def cli(self, interface, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        ret_dict = {}

        # Port:3, Subport:11, Tx SC index:0
        p1 = re.compile(r"Port\:\d+\, Subport\:(.*)\, Tx SC index")

        # Port:3, Subport:11, Rx SC index:0
        p2 = re.compile(r"Port\:\d+\, Subport\:(.*)\, Rx SC index")

        # Prev AN: 3, Cur AN: 0
        p3 = re.compile(r"Prev AN\: (?P<prev_an>\d+)\, +" "Cur AN\: (?P<cur_an>\d+)")

        # SA index: 50331759, vport index: 2, rule index: 1
        p4 = re.compile(
            r"SA index\: (?P<sa_index>\d+)\, +"
            "vport index\: (?P<vport_index>\d+)\, +"
            "rule index\: (?P<rule_index>\d+)"
        )

        # key_len: 16
        p5 = re.compile(r"^key_len\: (?P<key_len>\d+)$")

        # hashkey_len: 16
        p6 = re.compile(r"^hashkey_len\: (?P<hashkey_len>\d+)$")

        # bypass: 0
        p7 = re.compile(r"^bypass\: (?P<bypass>\d+)$")

        # nextPn: 1
        p8 = re.compile(r"^nextPn\: (?P<nextPn>\d+)$")

        # conf_offset: 0
        p9 = re.compile(r"^conf_offset\: (?P<conf_offset>\d+)$")

        # encrypt: 1
        p10 = re.compile(r"^encrypt\: (?P<encrypt>\d+)$")

        # vlan: 1
        p11 = re.compile(r"^vlan\: (?P<vlan>\d+)$")

        # end_station: 0
        p12 = re.compile(r"^end_station\: (?P<end_station>\d+)$")

        # scb: 0
        p13 = re.compile(r"^scb\: (?P<scb>\d+)$")

        # cipher: GCM_AES_128
        p14 = re.compile(r"^cipher\: (?P<cipher>\S+)$")

        # Delay protection: 0
        p15 = re.compile(r"^Delay protection\: (?P<delay_protection>\d+)$")

        # replay_protect: 1
        p16 = re.compile(r"^replay_protect\: (?P<replay_protect>\d+)$")

        # replay_window_size: 0
        p17 = re.compile(r"^replay_window_size\: (?P<replay_window_size>\d+)$")

        # decrypt_frames: 1
        p18 = re.compile(r"^decrypt_frames\: (?P<decrypt_frames>\d+)$")

        # validate_frames: 1
        p19 = re.compile(r"^validate_frames\: (?P<validate_frames>\d+)$")

        # sci:ecce1346f902008c
        p20 = re.compile(r"^sci\:(?P<sci>\S+)$")

        for line in out.splitlines():
            line = line.strip()
            m1 = p1.match(line)
            if m1:
                sc = "tx"
                subport_tx = m1.group(1)
                subport_tx_dict = ret_dict.setdefault(
                    "subport-{}-tx".format(subport_tx), {}
                )
            m2 = p2.match(line)
            if m2:
                sc = "rx"
                subport_rx = m2.group(1)
                subport_rx_dict = ret_dict.setdefault(
                    "subport-{}-rx".format(subport_rx), {}
                )
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                if sc == "tx":
                    subport_tx_dict["prev-an"] = group["prev_an"]
                    subport_tx_dict["cur-an"] = group["cur_an"]
                elif sc == "rx":
                    subport_rx_dict["prev-an"] = group["prev_an"]
                    subport_rx_dict["cur-an"] = group["cur_an"]
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                if sc == "tx":
                    subport_tx_dict["sa-index"] = group["sa_index"]
                    subport_tx_dict["vport-index"] = group["vport_index"]
                    subport_tx_dict["rule-index"] = group["rule_index"]
                elif sc == "rx":
                    subport_rx_dict["sa-index"] = group["sa_index"]
                    subport_rx_dict["vport-index"] = group["vport_index"]
                    subport_rx_dict["rule-index"] = group["rule_index"]
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                if sc == "tx":
                    subport_tx_dict["key-len"] = group["key_len"]
                elif sc == "rx":
                    subport_rx_dict["key-len"] = group["key_len"]
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                if sc == "tx":
                    subport_tx_dict["hashkey-len"] = group["hashkey_len"]
                elif sc == "rx":
                    subport_rx_dict["hashkey-len"] = group["hashkey_len"]
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                if sc == "tx":
                    subport_tx_dict["bypass"] = group["bypass"]
                elif sc == "rx":
                    subport_rx_dict["bypass"] = group["bypass"]
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                if sc == "tx":
                    subport_tx_dict["next-pn"] = group["nextPn"]
                elif sc == "rx":
                    subport_rx_dict["next-pn"] = group["nextPn"]
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                if sc == "tx":
                    subport_tx_dict["conf-offset"] = group["conf_offset"]
                elif sc == "rx":
                    subport_rx_dict["conf-offset"] = group["conf_offset"]
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                if sc == "tx":
                    subport_tx_dict["encrypt"] = group["encrypt"]
                elif sc == "rx":
                    subport_rx_dict["encrypt"] = group["encrypt"]
            m11 = p11.match(line)
            if m11:
                group = m11.groupdict()
                if sc == "tx":
                    subport_tx_dict["vlan"] = group["vlan"]
                elif sc == "rx":
                    subport_rx_dict["vlan"] = group["vlan"]
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                if sc == "tx":
                    subport_tx_dict["end-station"] = group["end_station"]
                elif sc == "rx":
                    subport_rx_dict["end-station"] = group["end_station"]
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                if sc == "tx":
                    subport_tx_dict["scb"] = group["scb"]
                elif sc == "rx":
                    subport_rx_dict["scb"] = group["scb"]
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                if sc == "tx":
                    subport_tx_dict["cipher"] = group["cipher"]
                elif sc == "rx":
                    subport_rx_dict["cipher"] = group["cipher"]
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                if sc == "tx":
                    subport_tx_dict["delay-protection"] = group["delay_protection"]
                elif sc == "rx":
                    subport_rx_dict["delay-protection"] = group["delay_protection"]
            m16 = p16.match(line)
            if m16:
                group = m16.groupdict()
                if sc == "tx":
                    subport_tx_dict["replay-protect"] = group["replay_protect"]
                elif sc == "rx":
                    subport_rx_dict["replay-protect"] = group["replay_protect"]
            m17 = p17.match(line)
            if m17:
                group = m17.groupdict()
                if sc == "tx":
                    subport_tx_dict["replay-window-size"] = group["replay_window_size"]
                elif sc == "rx":
                    subport_rx_dict["replay-window-size"] = group["replay_window_size"]
            m18 = p18.match(line)
            if m18:
                group = m18.groupdict()
                if sc == "tx":
                    subport_tx_dict["decrypt-frames"] = group["decrypt_frames"]
                elif sc == "rx":
                    subport_rx_dict["decrypt-frames"] = group["decrypt_frames"]
            m19 = p19.match(line)
            if m19:
                group = m19.groupdict()
                if sc == "tx":
                    subport_tx_dict["validate-frames"] = group["validate_frames"]
                elif sc == "rx":
                    subport_rx_dict["validate-frames"] = group["validate_frames"]
            m20 = p20.match(line)
            if m20:
                group = m20.groupdict()
                if sc == "tx":
                    subport_tx_dict["sci"] = group["sci"]
                elif sc == "rx":
                    subport_rx_dict["sci"] = group["sci"]

        return ret_dict


# ======================================================================================
#  Schema for
#  * 'show platform software object-manager {switch} {switch_type} F0 pending-ack-update'
#  * 'show platform software object-manager F0 pending-ack-update'
# =======================================================================================
class ShowPlatformSoftwareObjectManagerF0PendingAckUpdateSchema(MetaParser):
    """Schema for 'show platform software object-manager {switch} {switch_type} F0 pending-ack-update'
    'show platform software object-manager F0 pending-ack-update'
    """

    schema = {
        "object_id": {
            Any(): {
                "update_id": int,
                "description": str,
                "action": str,
                "pending_sec": int,
                "num_retries": int,
                "number_batch_begin_retries": int,
                "number_nacked_download_retries": int,
            },
        }
    }


# =======================================================================================
#  Parser for
#  * 'show platform software object-manager {switch} {switch_type} F0 pending-ack-update'
#  * 'show platform software object-manager F0 pending-ack-update'
# =======================================================================================


class ShowPlatformSoftwareObjectManagerF0PendingAckUpdate(
    ShowPlatformSoftwareObjectManagerF0PendingAckUpdateSchema
):
    """
    Parser for :
        * 'show platform software object-manager {switch} {switch_type} F0 pending-ack-update'
        * 'show platform software object-manager F0 pending-ack-update'
    """

    cli_command = [
        "show platform software object-manager {switch} {switch_type} F0 pending-ack-update",
        "show platform software object-manager F0 pending-ack-update",
    ]

    def cli(self, switch_type="", switch="", output=None):
        if output is None:
            if switch and switch_type:
                output = self.device.execute(
                    self.cli_command[0].format(switch=switch, switch_type=switch_type)
                )
            else:
                output = self.device.execute(self.cli_command[1])
        else:
            output = output

        # initial return dictionary
        ret_dict = {}
        sub_dict = {}

        # Update identifier: 305, Object identifier: 305
        p1 = re.compile(
            r"^Update identifier:\s+(?P<update_id>\d*)(?:,\s*)Object identifier:\s+(?P<object_id>\d*)$"
        )

        # Description: [aom_mlist_show_cb] mlist 2046
        p2 = re.compile(r"^Description:\s*(?P<description>.*)$")

        # Action: Create, Pending seconds: 3930
        p3 = re.compile(
            r"^Action:\s*(?P<action>\w*)(?:,\s*)Pending seconds:\s*(?P<pending_sec>\d*)$"
        )

        # Number of retries: 0, Number of batch begin retries: 0, Number of nacked download retries: 0
        p4 = re.compile(
            r"^Number of retries:\s*(?P<num_retries>\d*)(?:,\s*)"
            r"Number of batch begin retries:\s*(?P<number_batch_begin_retries>\d*)(?:,\s*)"
            r"Number of nacked download retries:\s*(?P<number_nacked_download_retries>\d*)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Update identifier: 305, Object identifier: 305
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                object_id = groups["object_id"]
                sub_dict = ret_dict.setdefault("object_id", {}).setdefault(
                    object_id, {}
                )

                update_id = groups["update_id"]
                sub_dict["update_id"] = int(update_id)
                continue

            # Description: [aom_mlist_show_cb] mlist 2046
            m = p2.match(line)
            if m:
                group = m.groupdict()
                description = group["description"]
                sub_dict["description"] = str(description)
                continue

            # Action: Create, Pending seconds: 3930
            m = p3.match(line)
            if m:
                group = m.groupdict()
                action = group["action"]
                sub_dict["action"] = str(action)

                pending_sec = group["pending_sec"]
                sub_dict["pending_sec"] = int(pending_sec)
                continue

            # Number of retries: 0, Number of batch begin retries: 0, Number of nacked download retries: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                num_retries = group["num_retries"]
                sub_dict["num_retries"] = int(num_retries)

                number_batch_begin_retries = group["number_batch_begin_retries"]
                sub_dict["number_batch_begin_retries"] = int(number_batch_begin_retries)

                number_nacked_download_retries = group["number_nacked_download_retries"]
                sub_dict["number_nacked_download_retries"] = int(
                    number_nacked_download_retries
                )
                continue

        return ret_dict


# ===============================================================================
# Schema for 'show platform software dpidb index'
# ===============================================================================
class ShowPlatformSoftwareDpidIndexSchema(MetaParser):
    """Schema for :
    show platform software dpidb index"""

    schema = {
        Any(): {
            "index": int,
        },
    }


# ===============================================================================
# Parser for 'show platform software dpidb index'
# ===============================================================================
class ShowPlatformSoftwareDpidIndex(ShowPlatformSoftwareDpidIndexSchema):
    """parser for :
    show platform software dpidb index"""

    cli_command = "show platform software dpidb index"

    def cli(
        self,
        output=None,
    ):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        result_dict = {}
        # Index 1030 -- swidb Hu1/0/1
        p1 = re.compile(r"^Index\s+(?P<index>\d+)\s+--\s+swidb\s+(?P<interface>\S+)$")

        for line in out.splitlines():
            line = line.strip()
            # Index 1030 -- swidb Hu1/0/1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group.pop("interface")
                interface_dict = result_dict.setdefault(interface, {})
                interface_dict.update(
                    {
                        "index": int(group["index"]),
                    }
                )
                continue

        return result_dict


class ShowPlatformSoftwareDbalR0DataAllSchema(MetaParser):
    schema = {
        "db_name": {
            Any(): {
                "db_mode": str,
                "batches_waiting": int,
                "batches_in_progress": int,
                "batches_done": int,
                "tunnels_active": int,
                "tunnels_closed": int,
            }
        }
    }


class ShowPlatformSoftwareDbalR0DataAll(ShowPlatformSoftwareDbalR0DataAllSchema):
    cli_command = "show platform software dbal smd R0 database all"

    def cli(self, output=None):
        out = self.device.execute(self.cli_command) if output is None else output

        ret_dict = {}

        # SMD_CONF                  Local                       0                     0                30                 0                 0

        pr = re.compile(
            r"^(?P<db_name>\S+) +"
            r"(?P<db_mode>\S+) +"
            r"(?P<batches_waiting>\d+) +"
            r"(?P<batches_in_progress>\d+) +"
            r"(?P<batches_done>\d+) +"
            r"(?P<tunnels_active>\d+) +"
            r"(?P<tunnels_closed>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            m = pr.match(line)
            if m:
                group = m.groupdict()

                dbnames_dict = ret_dict.setdefault("db_name", {})
                dbname_dict = dbnames_dict.setdefault(group["db_name"], {})

                dbname_dict.update(
                    {
                        "db_mode": group["db_mode"],
                        "batches_waiting": int(group["batches_waiting"]),
                        "batches_in_progress": int(group["batches_in_progress"]),
                        "batches_done": int(group["batches_done"]),
                        "tunnels_active": int(group["tunnels_active"]),
                        "tunnels_closed": int(group["tunnels_closed"]),
                    }
                )

                continue

        return ret_dict


class ShowPlatformSoftwareInterfaceSwitchF0BriefSchema(MetaParser):
    """
    Schema for show platform software interface switch {mode} F0 brief
    """

    schema = {
        "forwarding_manager_interface_information": {
            Any(): {
                "id": int,
                "qfp_id": int,
            },
        }
    }


class ShowPlatformSoftwareInterfaceSwitchF0Brief(
    ShowPlatformSoftwareInterfaceSwitchF0BriefSchema
):
    """Parser for show platform software interface switch {mode} F0 brief"""

    cli_command = "show platform software interface switch {mode} F0 brief"

    def cli(self, mode, output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}
        # HundredGigE2/0/35/4                1285              1285
        p1 = re.compile("^(?P<name>\S+)\s+(?P<id>\d+)\s+(?P<qfp_id>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # HundredGigE2/0/35/4                1285              1285
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault(
                    "forwarding_manager_interface_information", {}
                ).setdefault(group["name"], {})
                root_dict["id"] = int(group["id"])
                root_dict["qfp_id"] = int(group["qfp_id"])
                continue

        return ret_dict


# ==============================================================
# Parser for 'show platform software dns-umbrella statistics'
# ==============================================================
class ShowPlatformSoftwareDnsUmbrellaStatisticsSchema(MetaParser):
    """Schema for show platform software dns-umbrella statistics"""

    schema = {
        "umbrella_statistics": {
            "total_packets": int,
            "dns_crypt_queries": int,
            "dns_crypt_responses": int,
            "dns_queries": int,
            "dns_bypass_queries": int,
            "dns_umbrella_responses": int,
            "dns_other_responses": int,
            "aged_queries": int,
            "dropped_packets": int,
        },
    }


class ShowPlatformSoftwareDnsUmbrellaStatistics(
    ShowPlatformSoftwareDnsUmbrellaStatisticsSchema
):
    """Parser for show platform software dns-umbrella statistics"""

    cli_command = "show platform software dns-umbrella statistics"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Umbrella Statistics
        p0 = re.compile(r"^Umbrella\s+Statistics$")

        # Total Packets               : 57057
        p1 = re.compile(r"^Total\s+Packets\s+:\s+(?P<TotalPacket>\d+)$")

        # DNSCrypt queries            : 0
        p2 = re.compile(r"^DNSCrypt\s+queries\s+:\s+(?P<DnsCryptQueri>\d+)$")

        # DNSCrypt responses          : 0
        p3 = re.compile(r"^DNSCrypt\s+responses\s+:\s+(?P<DnsCryptResp>\d+)$")

        # DNS queries                 : 32321
        p4 = re.compile(r"^DNS\s+queries\s+:\s+(?P<DnsQueri>\d+)$")

        # DNS bypassed queries(Regex) : 0
        p5 = re.compile(
            r"^DNS\s+bypassed\s+queries\(Regex\)\s+:\s+(?P<DnsBypassQueri>\d+)$"
        )

        # DNS responses(Umbrella)     : 24693
        p6 = re.compile(r"^DNS\s+responses\(Umbrella\)\s+:\s+(?P<DnsUmbrellaResp>\d+)$")

        # DNS responses(Other)        : 37
        p7 = re.compile(r"^DNS\s+responses\(Other\)\s+:\s+(?P<DnsOtherResp>\d+)$")

        # Aged queries                : 7628
        p8 = re.compile(r"^Aged\s+queries\s+:\s+(?P<AgedQueri>\d+)$")

        # Dropped pkts                : 0
        p9 = re.compile(r"^Dropped\s+pkts\s+:\s+(?P<DroppedPkts>\d+)$")

        for line in out.splitlines():
            line = line.strip()

            # Umbrella Statistics
            m = p0.match(line)
            if m:
                ret_dict["umbrella_statistics"] = {}
                continue

            # Total Packets               : 57057
            m = p1.match(line)
            if m:
                ret_dict["umbrella_statistics"]["total_packets"] = int(
                    m.groupdict()["TotalPacket"]
                )
                continue

            # DNSCrypt queries            : 0
            m = p2.match(line)
            if m:
                ret_dict["umbrella_statistics"]["dns_crypt_queries"] = int(
                    m.groupdict()["DnsCryptQueri"]
                )
                continue

            # DNSCrypt responses          : 0
            m = p3.match(line)
            if m:
                ret_dict["umbrella_statistics"]["dns_crypt_responses"] = int(
                    m.groupdict()["DnsCryptResp"]
                )
                continue

            # DNS queries                 : 32321
            m = p4.match(line)
            if m:
                ret_dict["umbrella_statistics"]["dns_queries"] = int(
                    m.groupdict()["DnsQueri"]
                )
                continue

            # DNS bypassed queries(Regex) : 0
            m = p5.match(line)
            if m:
                ret_dict["umbrella_statistics"]["dns_bypass_queries"] = int(
                    m.groupdict()["DnsBypassQueri"]
                )
                continue

            # DNS responses(Umbrella)     : 24693
            m = p6.match(line)
            if m:
                ret_dict["umbrella_statistics"]["dns_umbrella_responses"] = int(
                    m.groupdict()["DnsUmbrellaResp"]
                )
                continue

            # DNS responses(Other)        : 37
            m = p7.match(line)
            if m:
                ret_dict["umbrella_statistics"]["dns_other_responses"] = int(
                    m.groupdict()["DnsOtherResp"]
                )
                continue

            # Aged queries                : 7628
            m = p8.match(line)
            if m:
                ret_dict["umbrella_statistics"]["aged_queries"] = int(
                    m.groupdict()["AgedQueri"]
                )
                continue

            # Dropped pkts                : 0
            m = p9.match(line)
            if m:
                ret_dict["umbrella_statistics"]["dropped_packets"] = int(
                    m.groupdict()["DroppedPkts"]
                )
                continue

        return ret_dict


class ShowPlatformSoftwareCpmSwitchB0CountersDropSchema(MetaParser):
    """
    Schema for show platform software cpm switch {mode} B0 counters drop
    """

    schema = {
        Any(): int,
    }


class ShowPlatformSoftwareCpmSwitchB0CountersDrop(
    ShowPlatformSoftwareCpmSwitchB0CountersDropSchema
):
    """Parser for show platform software cpm switch {mode} B0 counters drop"""

    cli_command = "show platform software cpm switch {mode} B0 counters drop"

    def cli(self, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}

        # RX unexpected packet count                    311
        p1 = re.compile("^(?P<drop_counters>[\w ]+)\s+(?P<drop_count>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict[group["drop_counters"].strip()] = int(group["drop_count"])
                continue

        return ret_dict


class ShowPlatformSoftwareCpmSwitchB0CountersPuntInjectSchema(MetaParser):
    """
    Schema for show platform software cpm switch {mode} B0 counters punt-inject
    """

    schema = {
        "traffic_type": {
            Any(): {
                "packets_inject": int,
                "packets_punt": int,
                "drop_inject": int,
                "drop_punt": int,
            },
        },
        Optional("timestamp_now"): str,
        Optional("ctrl_rx_timestamp"): {
            "timestamp": dict,
            Optional("ctrl_rx_max_time_gap_sec"): str,
            Optional("ctrl_rx_max_timestamp"): str,
        },
        Optional("ctrl_tx_timestamp"): {
            "timestamp": dict,
            Optional("ctrl_tx_max_time_gap_sec"): str,
            Optional("ctrl_tx_max_timestamp"): str,
        },
        Optional("ipc_rx_timestamp"): {
            "timestamp": dict,
            Optional("ipc_rx_max_time_gap_sec"): str,
            Optional("ipc_rx_max_timestamp"): str,
        },
        Optional("ipc_tx_timestamp"): {
            "timestamp": dict,
            Optional("ipc_tx_max_time_gap_sec"): str,
            Optional("ipc_tx_max_timestamp"): str,
        },
    }


class ShowPlatformSoftwareCpmSwitchB0CountersPuntInject(
    ShowPlatformSoftwareCpmSwitchB0CountersPuntInjectSchema
):
    """Parser for show platform software cpm switch {mode} B0 counters punt-inject"""

    cli_command = "show platform software cpm switch {mode} B0 counters punt-inject"

    def cli(self, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}
        temp_dict = {}

        # SVL CTRL           12673           12641                0                15
        p1 = re.compile(
            "^(?P<traffic_type>\w+\s+\w+)\s+(?P<packets_inject>\d+)\s+(?P<packets_punt>\d+)\s+(?P<drop_inject>\d+)\s+(?P<drop_punt>\d+)$"
        )

        # Timestamp Now: May 07 11:58:31.969
        p2 = re.compile(r"^Timestamp +Now\: +(?P<timestamp_now>.*)$")

        # CTRL RX Timestamp: May 07 11:58:21.515 [1]
        p3 = re.compile(r"^CTRL +RX +Timestamp\: +(?P<time>.*) +\[(?P<count>\d+)\]$")

        # CTRL RX Maximum Time Gap:                4 sec,          941197usec
        p4 = re.compile(
            r"^CTRL +RX +Maximum +Time +Gap\: +(?P<ctrl_rx_max_time_gap_sec>.*)$"
        )

        # CTRL RX Maximum Gap Timestamp: May 07 06:13:36.003
        p5 = re.compile(
            r"^CTRL +RX +Maximum +Gap +Timestamp\: +(?P<ctrl_rx_max_timestamp>.*)$"
        )

        # CTRL TX Timestamp: May 07 11:58:20.859 [3]
        p6 = re.compile(r"^CTRL +TX +Timestamp\: +(?P<time>.*) +\[(?P<count>\d+)\]$")

        # CTRL TX Maximum Time Gap:                4 sec,          991449usec
        p7 = re.compile(
            r"^CTRL +TX +Maximum +Time +Gap\: +(?P<ctrl_tx_max_time_gap_sec>.*)$"
        )

        # CTRL TX Maximum Gap Timestamp: May 07 05:25:53.959
        p8 = re.compile(
            r"^CTRL +TX +Maximum +Gap +Timestamp\: +(?P<ctrl_tx_max_timestamp>.*)$"
        )

        # IPC RX Timestamp: May 07 11:58:31.882 [2]
        p9 = re.compile(r"^IPC +RX +Timestamp\: +(?P<time>.*) +\[(?P<count>\d+)\]$")

        # IPC RX Maximum Time Gap:                4 sec,          350695usec
        p10 = re.compile(
            r"^IPC +RX +Maximum +Time +Gap\: +(?P<ipc_rx_max_time_gap_sec>.*)$"
        )

        # IPC RX Maximum Gap Timestamp: May 07 05:29:06.825
        p11 = re.compile(
            r"^IPC +RX +Maximum +Gap +Timestamp\: +(?P<ipc_rx_max_timestamp>.*)$"
        )

        # IPC TX Timestamp: May 07 11:58:31.869 [2]
        p12 = re.compile(r"^IPC +TX +Timestamp\: +(?P<time>.*) +\[(?P<count>\d+)\]$")

        # IPC TX Maximum Time Gap:                1 sec,          953783usec
        p13 = re.compile(
            r"^IPC +TX +Maximum +Time +Gap\: +(?P<ipc_tx_max_time_gap_sec>.*)$"
        )

        # IPC TX Maximum Gap Timestamp: May 07 05:21:16.021
        p14 = re.compile(
            r"^IPC +TX +Maximum +Gap +Timestamp\: +(?P<ipc_tx_max_timestamp>.*)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # SVL CTRL           12673           12641                0                15
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("traffic_type", {}).setdefault(
                    group["traffic_type"].strip(), {}
                )
                root_dict["packets_inject"] = int(group["packets_inject"])
                root_dict["packets_punt"] = int(group["packets_punt"])
                root_dict["drop_inject"] = int(group["drop_inject"])
                root_dict["drop_punt"] = int(group["drop_punt"])
                continue

            # Timestamp Now: May 07 11:58:31.969
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["timestamp_now"] = group["timestamp_now"]
                continue

            # CTRL RX Timestamp: May 07 11:58:21.515 [1]
            m = p3.match(line)
            if m:
                group = m.groupdict()
                count = int(group["count"])
                temp_dict.update({count: group["time"]})
                continue

            # CTRL RX Maximum Time Gap:                4 sec,          941197usec
            m = p4.match(line)
            if m:
                root_dict = ret_dict.setdefault("ctrl_rx_timestamp", {})
                root_dict["timestamp"] = temp_dict
                temp_dict = {}
                group = m.groupdict()
                root_dict["ctrl_rx_max_time_gap_sec"] = group[
                    "ctrl_rx_max_time_gap_sec"
                ]
                continue

            # CTRL RX Maximum Gap Timestamp: May 07 06:13:36.003
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict["ctrl_rx_max_timestamp"] = group["ctrl_rx_max_timestamp"]
                continue

            # CTRL TX Timestamp: May 07 11:58:20.859 [3]
            m = p6.match(line)
            if m:
                group = m.groupdict()
                count = int(group["count"])
                temp_dict.update({count: group["time"]})
                continue

            # CTRL TX Maximum Time Gap:                4 sec,          991449usec
            m = p7.match(line)
            if m:
                root_dict = ret_dict.setdefault("ctrl_tx_timestamp", {})
                root_dict["timestamp"] = temp_dict
                temp_dict = {}
                group = m.groupdict()
                root_dict["ctrl_tx_max_time_gap_sec"] = group[
                    "ctrl_tx_max_time_gap_sec"
                ]
                continue

            # CTRL TX Maximum Gap Timestamp: May 07 05:25:53.959
            m = p8.match(line)
            if m:
                group = m.groupdict()
                root_dict["ctrl_tx_max_timestamp"] = group["ctrl_tx_max_timestamp"]
                continue

            # IPC RX Timestamp: May 07 11:58:31.882 [2]
            m = p9.match(line)
            if m:
                group = m.groupdict()
                count = int(group["count"])
                temp_dict.update({count: group["time"]})
                continue

            # IPC RX Maximum Time Gap:                4 sec,          350695usec
            m = p10.match(line)
            if m:
                root_dict = ret_dict.setdefault("ipc_rx_timestamp", {})
                root_dict["timestamp"] = temp_dict
                temp_dict = {}
                group = m.groupdict()
                root_dict["ipc_rx_max_time_gap_sec"] = group["ipc_rx_max_time_gap_sec"]
                continue

            # IPC RX Maximum Gap Timestamp: May 07 05:29:06.825
            m = p11.match(line)
            if m:
                group = m.groupdict()
                root_dict["ipc_rx_max_timestamp"] = group["ipc_rx_max_timestamp"]
                continue

            # IPC TX Timestamp: May 07 11:58:31.869 [2]
            m = p12.match(line)
            if m:
                group = m.groupdict()
                count = int(group["count"])
                temp_dict.update({count: group["time"]})
                continue

            # IPC TX Maximum Time Gap:                1 sec,          953783usec
            m = p13.match(line)
            if m:
                root_dict = ret_dict.setdefault("ipc_tx_timestamp", {})
                root_dict["timestamp"] = temp_dict
                temp_dict = {}
                group = m.groupdict()
                root_dict["ipc_tx_max_time_gap_sec"] = group["ipc_tx_max_time_gap_sec"]
                continue

            # IPC TX Maximum Gap Timestamp: May 07 05:21:16.021
            m = p14.match(line)
            if m:
                group = m.groupdict()
                root_dict["ipc_tx_max_timestamp"] = group["ipc_tx_max_timestamp"]
                continue

        return ret_dict


class ShowPlatformSoftwareCpmSwitchB0IpcBriefSchema(MetaParser):
    """
    Schema for show platform software cpm switch {mode} B0 ipc brief
    """

    schema = {
        "ipc_status": {
            "cpm_cm": str,
            "cpm_fed": str,
        },
    }


class ShowPlatformSoftwareCpmSwitchB0IpcBrief(
    ShowPlatformSoftwareCpmSwitchB0IpcBriefSchema
):
    """Parser for show platform software cpm switch {mode} B0 ipc brief"""

    cli_command = "show platform software cpm switch {mode} B0 ipc brief"

    def cli(self, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}

        # cpm-cm     connected
        p1 = re.compile("^cpm-cm\s+(?P<cpm_cm>\w+)$")

        # cpm-fed    connected
        p2 = re.compile("^cpm-fed\s+(?P<cpm_fed>\w+)$")

        for line in output.splitlines():
            line = line.strip()

            # cpm-cm     connected
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("ipc_status", {})
                root_dict["cpm_cm"] = group["cpm_cm"]
                continue

            # cpm-fed    connected
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict["cpm_fed"] = group["cpm_fed"]
                continue

        return ret_dict


class ShowPlatformSoftwareCpmSwitchB0IpcDetailSchema(MetaParser):
    """
    Schema for show platform software cpm switch {mode} B0 ipc detail
    """

    schema = {
        "bipc_connection_status": {
            Optional("service"): str,
            Optional("peer_location"): int,
            Optional("peer_state"): int,
            Optional("connection_drops"): int,
            Optional("flow_control"): int,
            Optional("transition_count"): int,
            Optional("received_msgs"): int,
            Optional("tdl_hdl_failure"): int,
            Optional("dispatch_failures"): int,
            Optional("rx_other_drops"): int,
            Optional("sent_msgs"): int,
            Optional("tx_no_mem_failures"): int,
            Optional("tx_other_drops"): int,
            Optional("tx_no_space_failures"): int,
        },
    }


class ShowPlatformSoftwareCpmSwitchB0IpcDetail(
    ShowPlatformSoftwareCpmSwitchB0IpcDetailSchema
):
    """Parser for show platform software cpm switch {mode} B0 ipc detail"""

    cli_command = "show platform software cpm switch {mode} B0 ipc detail"

    def cli(self, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}

        # Service: cpm-cm
        p1 = re.compile("^Service:\s+(?P<service>\S+)$")

        # Peer Location: -1
        p2 = re.compile("^Peer Location:\s+(?P<peer_location>\S+)$")

        # Peer State: 2
        p3 = re.compile("^Peer State:\s+(?P<peer_state>\d+)$")

        # Connection Drops: 0
        p4 = re.compile("^Connection Drops:\s+(?P<connection_drops>\d+)$")

        # Flow Control: 0
        p5 = re.compile("^Flow Control:\s+(?P<flow_control>\d+)$")

        # Transition Count: 0
        p6 = re.compile("^Transition Count:\s+(?P<transition_count>\d+)$")

        # Received Msgs: 1
        p7 = re.compile("^Received Msgs:\s+(?P<received_msgs>\d+)$")

        # TDL hdl failure: 0
        p8 = re.compile("^TDL hdl failure:\s+(?P<tdl_hdl_failure>\d+)$")

        # Dispatch failures: 1
        p9 = re.compile("^Dispatch failures:\s+(?P<dispatch_failures>\d+)$")

        # Rx Other Drops: 0
        p10 = re.compile("^Rx Other Drops:\s+(?P<rx_other_drops>\d+)$")

        # Sent msgs: 1
        p11 = re.compile("^Sent msgs:\s+(?P<sent_msgs>\d+)$")

        # Tx No Mem failures: 0
        p12 = re.compile("^Tx No Mem failures:\s+(?P<tx_no_mem_failures>\d+)$")

        # Tx Other Drops: 0
        p13 = re.compile("^Tx Other Drops:\s+(?P<tx_other_drops>\d+)$")

        # Tx No Space failures: 0
        p14 = re.compile("^Tx No Space failures:\s+(?P<tx_no_space_failures>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # Service: cpm-cm
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("bipc_connection_status", {})
                root_dict["service"] = group["service"]
                continue

            # Peer Location: -1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict["peer_location"] = int(group["peer_location"])
                continue

            # Peer State: 2
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict["peer_state"] = int(group["peer_state"])
                continue

            # Connection Drops: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict["connection_drops"] = int(group["connection_drops"])
                continue

            # Flow Control: 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict["flow_control"] = int(group["flow_control"])
                continue

            # Transition Count: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                root_dict["transition_count"] = int(group["transition_count"])
                continue

            # Received Msgs: 1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                root_dict["received_msgs"] = int(group["received_msgs"])
                continue

            # TDL hdl failure: 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                root_dict["tdl_hdl_failure"] = int(group["tdl_hdl_failure"])
                continue

            # Dispatch failures: 1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                root_dict["dispatch_failures"] = int(group["dispatch_failures"])
                continue

            # Rx Other Drops: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                root_dict["rx_other_drops"] = int(group["rx_other_drops"])
                continue

            # Sent msgs: 1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                root_dict["sent_msgs"] = int(group["sent_msgs"])
                continue

            # Tx No Mem failures: 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                root_dict["tx_no_mem_failures"] = int(group["tx_no_mem_failures"])
                continue

            # Tx Other Drops: 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                root_dict["tx_other_drops"] = int(group["tx_other_drops"])
                continue

            # Tx No Space failures: 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                root_dict["tx_no_space_failures"] = int(group["tx_no_space_failures"])
                continue

        return ret_dict


class ShowPlatformSoftwareCpmSwitchB0ControlInfoSchema(MetaParser):
    """
    Schema for show platform software cpm switch {mode} B0 control-info
    """

    schema = {
        "system_port": int,
        "svl_control_interface": {
            Any(): {
                Any(): {
                    "ec_if_id": str,
                    "system_port": int,
                    "if_type": str,
                },
            },
        },
    }


class ShowPlatformSoftwareCpmSwitchB0ControlInfo(
    ShowPlatformSoftwareCpmSwitchB0ControlInfoSchema
):
    """Parser for show platform software cpm switch {mode} B0 control-info"""

    cli_command = "show platform software cpm switch {mode} B0 control-info"

    def cli(self, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}

        # System port: 98
        p1 = re.compile("^System port: (?P<system_port>\d+)$")

        # SVL Control Interface: HundredGigE1/0/2
        p2 = re.compile("^SVL Control Interface: (?P<svl_control_interface>\S+)$")

        # 27                  FiftyGigE1/0/56
        p1_2 = re.compile("^(?P<system_port>\s*\d+)\s+(?P<svl_control_interface>\S+)$")

        # 0x2c       0x2c     28       etherchannel
        p3 = re.compile(
            "^(?P<if_id>\S+)\s+(?P<ec_if_id>\S+)\s+(?P<system_port>\d+)\s+(?P<if_type>\S+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # System port: 98
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["system_port"] = int(group["system_port"])
                continue

            # SVL Control Interface: HundredGigE1/0/2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("svl_control_interface", {})
                root_dict1 = root_dict.setdefault(group["svl_control_interface"], {})
                continue

            # 27                     FiftyGigE1/0/56
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["system_port"] = int(group["system_port"])
                root_dict = ret_dict.setdefault("svl_control_interface", {})
                root_dict1 = root_dict.setdefault(group["svl_control_interface"], {})
                continue

            # 0x2c       0x2c     28       etherchannel
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict = root_dict1.setdefault(group["if_id"], {})
                root_dict["ec_if_id"] = group["ec_if_id"]
                root_dict["system_port"] = int(group["system_port"])
                root_dict["if_type"] = group["if_type"]
                continue

        return ret_dict


class ShowPlatformSoftwareCpmSwitchB0ResourceSchema(MetaParser):
    """
    Schema for show platform software cpm switch {mode} B0 resource
    """

    schema = {
        "device_status": {"oobnd1": str, "leaba0_3": str, "leaba0_5": str},
    }


class ShowPlatformSoftwareCpmSwitchB0Resource(
    ShowPlatformSoftwareCpmSwitchB0ResourceSchema
):
    """Parser for show platform software cpm switch {mode} B0 resource"""

    cli_command = "show platform software cpm switch {mode} B0 resource"

    def cli(self, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}

        # oobnd1          UP
        p1 = re.compile("^oobnd1\s+(?P<oobnd1>UP|DOWN)$")

        # leaba0_3        UP
        p2 = re.compile("^leaba0_3\s+(?P<leaba0_3>UP|DOWN)$")

        # leaba0_5        UP
        p3 = re.compile("^leaba0_5\s+(?P<leaba0_5>UP|DOWN)$")

        for line in output.splitlines():
            line = line.strip()

            # oobnd1          UP
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("device_status", {})
                root_dict["oobnd1"] = group["oobnd1"]
                continue

            # leaba0_3        UP
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict["leaba0_3"] = group["leaba0_3"]
                continue

            # leaba0_5        UP
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict["leaba0_5"] = group["leaba0_5"]
                continue

        return ret_dict


# =====================================================================================
# Schema for 'show platform software object-manager switch active FP active statistics'
# =====================================================================================
class ShowPlatformSoftwareObjectManagerFpActiveStatisticsSchema(MetaParser):
    """Schema for the commands:
    * show platform software object-manager switch {switchstate} {serviceprocessor} active statistics
    * show platform software object-manager FP active statistics
    """

    schema = {
        "object_update": {"pending_issue": int, "pending_acknowledgement": int},
        "batch_begin": {"pending_issue": int, "pending_acknowledgement": int},
        "batch_end": {"pending_issue": int, "pending_acknowledgement": int},
        "command": {"pending_acknowledgement": int},
        "total_objects": int,
        "stale_objects": int,
        "resolve_objects": int,
        "childless_delete_objects": int,
        "backplane_objects": int,
        "error_objects": int,
        "number_of_bundles": int,
        "paused_types": int,
    }


# ====================================================================================
#  Parser for show platform software object-manager switch active FP active statistics
# ====================================================================================
class ShowPlatformSoftwareObjectManagerFpActiveStatistics(
    ShowPlatformSoftwareObjectManagerFpActiveStatisticsSchema
):
    """
    show platform software object-manager switch {switchstate} {serviceprocessor} active statistics
    show platform software object-manager FP active statistics
    """

    cli_command = [
        "show platform software object-manager switch {switchstate} {serviceprocessor} active statistics",
        "show platform software object-manager FP active statistics",
    ]

    def cli(self, switchstate="", serviceprocessor="", output=None):
        if output is None:
            if switchstate:
                cmd = self.cli_command[0].format(
                    switchstate=switchstate, serviceprocessor=serviceprocessor
                )
            else:
                cmd = self.cli_command[1]

            output = self.device.execute(cmd)

        # initial variables
        ret_dict = {}

        # Object update: Pending-issue: 7083, Pending-acknowledgement: 14101
        p0 = re.compile(
            r"^Object update: +Pending-issue: +(?P<pending_issue>\d+), +Pending-acknowledgement: +(?P<pending_acknowledgement>\d+)$"
        )

        # Batch begin:   Pending-issue: 0, Pending-acknowledgement: 0
        p1 = re.compile(
            r"^Batch begin: + Pending-issue: +(?P<pending_issue>\d)+, +Pending-acknowledgement: +(?P<pending_acknowledgement>\d+)$"
        )

        # Batch end:     Pending-issue: 0, Pending-acknowledgement: 0
        p2 = re.compile(
            r"^Batch end: + Pending-issue: +(?P<pending_issue>\d)+, +Pending-acknowledgement: +(?P<pending_acknowledgement>\d+)$"
        )

        # Command:       Pending-acknowledgement: 54
        p3 = re.compile(
            r"^Command: + Pending-acknowledgement: +(?P<pending_acknowledgement>\d+)$"
        )

        # Total-objects: 30105
        p4 = re.compile(r"^Total-objects: +(?P<total_objects>\d+)$")

        # Stale-objects: 0
        p5 = re.compile(r"^Stale-objects: +(?P<stale_objects>\d+)$")

        # Resolve-objects: 0
        p6 = re.compile(r"^Resolve-objects: +(?P<resolve_objects>\d+)$")

        # Childless-delete-objects: 0
        p7 = re.compile(
            r"^Childless-delete-objects: +(?P<childless_delete_objects>\d+)$"
        )

        # Backplane-objects: 0
        p8 = re.compile(r"^Backplane-objects: +(?P<backplane_objects>\d+)$")

        # Error-objects: 0
        p9 = re.compile(r"^Error-objects: +(?P<error_objects>\d+)$")

        # Number of bundles: 0
        p10 = re.compile(r"^Number of bundles: +(?P<number_of_bundles>\d+)$")

        # Paused-types: 0
        p11 = re.compile(r"^Paused-types: +(?P<paused_types>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # Object update: Pending-issue: 7083, Pending-acknowledgement: 14101
            m = p0.match(line)
            if m:
                group = m.groupdict()
                object_update = ret_dict.setdefault("object_update", {})
                object_update["pending_issue"] = int(group["pending_issue"])
                object_update["pending_acknowledgement"] = int(
                    group["pending_acknowledgement"]
                )

            # Batch begin:   Pending-issue: 0, Pending-acknowledgement: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                batch_begin = ret_dict.setdefault("batch_begin", {})
                batch_begin["pending_issue"] = int(group["pending_issue"])
                batch_begin["pending_acknowledgement"] = int(
                    group["pending_acknowledgement"]
                )

            # Batch end:     Pending-issue: 0, Pending-acknowledgement: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                batch_end = ret_dict.setdefault("batch_end", {})
                batch_end["pending_issue"] = int(group["pending_issue"])
                batch_end["pending_acknowledgement"] = int(
                    group["pending_acknowledgement"]
                )

            # Command:       Pending-acknowledgement: 54
            m = p3.match(line)
            if m:
                group = m.groupdict()
                command = ret_dict.setdefault("command", {})
                command["pending_acknowledgement"] = int(
                    group["pending_acknowledgement"]
                )

            # Total-objects: 30105
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["total_objects"] = int(group["total_objects"])

            # Stale-objects: 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict["stale_objects"] = int(group["stale_objects"])

            # Resolve-objects: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict["resolve_objects"] = int(group["resolve_objects"])

            # Childless-delete-objects: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict["childless_delete_objects"] = int(
                    group["childless_delete_objects"]
                )

            # Backplane-objects: 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict["backplane_objects"] = int(group["backplane_objects"])

            # Error-objects: 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict["error_objects"] = int(group["error_objects"])

            # Number of bundles: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict["number_of_bundles"] = int(group["number_of_bundles"])

            # Paused-types: 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict["paused_types"] = int(group["paused_types"])

        return ret_dict


class ShowPlatformSoftwareInstallManagerRpActiveOperationHistorySummarySchema(
    MetaParser
):
    """
    Schema for show platform software install-manager RP active operation history summary
    """

    schema = {
        "operation_summary": {
            Any(): {
                "uuid": str,
                "op_id": int,
                "command": str,
                "status": str,
                "duration": str,
                "start_date": str,
                "start_time": str,
                "end_date": str,
                "end_time": str,
            }
        },
    }


class ShowPlatformSoftwareInstallManagerRpActiveOperationHistorySummary(
    ShowPlatformSoftwareInstallManagerRpActiveOperationHistorySummarySchema
):
    """
    Parser for show platform software install-manager RP active operation history summary
    """

    cli_command = (
        "show platform software install-manager RP active operation history summary"
    )

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}
        index = 0
        # 2021_11_02_06_50_44_op_rollback  1        rollback     Fail    00:00:04   [2021-11-02 06:50:44 - 2021-11-02 06:50:48]
        p1 = re.compile(
            r"(?P<uuid>\S*)\s*(?P<op_id>\d+)\s*(?P<command>\S*)\s*(?P<status>\w+)\s*(?P<duration>\d+:\d+:\d+)\s*"
            r"\[(?P<start_date>\d+-\d+-\d+)\s*(?P<start_time>\d+:\d+:\d+)\s*-\s*(?P<end_date>\d+-\d+-\d+)\s*"
            r"(?P<end_time>\d+:\d+:\d+)\]"
        )

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                index += 1
                uuid_dict = ret_dict.setdefault("operation_summary", {}).setdefault(
                    index, {}
                )
                uuid_dict.update({"uuid": group["uuid"]})
                uuid_dict.update({"op_id": int(group["op_id"])})
                uuid_dict.update({"command": group["command"]})
                uuid_dict.update({"status": group["status"]})
                uuid_dict.update({"duration": group["duration"]})
                uuid_dict.update({"start_date": group["start_date"]})
                uuid_dict.update({"start_time": group["start_time"]})
                uuid_dict.update({"end_date": group["end_date"]})
                uuid_dict.update({"end_time": group["end_time"]})

        return ret_dict


class ShowPlatformSoftwareInstallManagerSwitchActiveR0OperationHistorySummarySchema(
    MetaParser
):
    """
    Schema for show platform software install-manager switch active r0 operation history summary
    """

    schema = {
        "operation_summary": {
            Any(): {
                "uuid": str,
                "op_id": int,
                "command": str,
                "status": str,
                "duration": str,
                "start_date": str,
                "start_time": str,
                "end_date": str,
                "end_time": str,
            }
        },
    }


class ShowPlatformSoftwareInstallManagerSwitchActiveR0OperationHistorySummary(
    ShowPlatformSoftwareInstallManagerSwitchActiveR0OperationHistorySummarySchema
):
    """
    Parser for show platform software install-manager switch active r0 operation history summary
    """

    cli_command = "show platform software install-manager switch active r0 operation history summary"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}
        index = 0
        # 2021_11_02_06_50_44_op_rollback  1        rollback     Fail    00:00:04   [2021-11-02 06:50:44 - 2021-11-02 06:50:48]
        p1 = re.compile(
            r"(?P<uuid>\S*)\s*(?P<op_id>\d+)\s*(?P<command>\S*)\s*(?P<status>\w+)\s*(?P<duration>\d+:\d+:\d+)\s*"
            r"\[(?P<start_date>\d+-\d+-\d+)\s*(?P<start_time>\d+:\d+:\d+)\s*-\s*(?P<end_date>\d+-\d+-\d+)\s*"
            r"(?P<end_time>\d+:\d+:\d+)\]"
        )

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                index += 1
                uuid_dict = ret_dict.setdefault("operation_summary", {}).setdefault(
                    index, {}
                )
                uuid_dict.update({"uuid": group["uuid"]})
                uuid_dict.update({"op_id": int(group["op_id"])})
                uuid_dict.update({"command": group["command"]})
                uuid_dict.update({"status": group["status"]})
                uuid_dict.update({"duration": group["duration"]})
                uuid_dict.update({"start_date": group["start_date"]})
                uuid_dict.update({"start_time": group["start_time"]})
                uuid_dict.update({"end_date": group["end_date"]})
                uuid_dict.update({"end_time": group["end_time"]})

        return ret_dict


class ShowPlatformSoftwareSteeringCellInfoSchema(MetaParser):

    """Schema for "show platform software steering-policy forwarding-manager switch {switch} F0 cell-info" """

    schema = {
        "sgt": {
            Any(): {
                "sgt": int,
                "dgt": int,
                "template_name": str,
                "number_of_policies": int,
                "policy_id": int,
            },
        }
    }


class ShowPlatformSoftwareSteeringCellInfo(ShowPlatformSoftwareSteeringCellInfoSchema):
    """Schema for show platform software steering-policy forwarding-manager F0 cell-info"""

    cli_command = [
        "show platform software steering-policy forwarding-manager switch {switch} F0 cell-info",
        "show platform software steering-policy forwarding-manager F0 cell-info",
    ]

    def cli(self, switch=None, output=None):
        if output is None:
            if not switch:
                cmd = self.cli_command[1]
            else:
                cmd = self.cli_command[0].format(switch=switch)
            output = self.device.execute(cmd)

        parsed_dict = {}

        # SGT: 2057, DGT: 3003
        # Template name: V4GRPPLC9;00, No.of Policies: 1
        #   Policy IDs
        #   -----------
        #   3861840057

        # SGT: 2057, DGT: 3003
        p1 = re.compile(r"^SGT\s*:\s*(?P<sgt>\d+)\s*,\s*DGT\s*:\s*(?P<dgt>\d+)$")

        # Template name: V4GRPPLC9;00, No.of Policies: 1
        p2 = re.compile(
            r"^Template name\s*:\s*(?P<template_name>.+)\s*,\s*No.of Policies\s*:\s*(?P<number_of_policies>\d+)$"
        )

        #   3861840057
        p3 = re.compile(r"^(?P<policy_id>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # SGT: 2057, DGT: 3003
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                sgt = int(groups["sgt"])
                dgt = int(groups["dgt"])
                sgt_dict = parsed_dict.setdefault("sgt", {})
                sgt_detailed_dict = sgt_dict.setdefault(sgt, {})
                sgt_detailed_dict.update({"sgt": sgt, "dgt": dgt})
                continue

            # Template name: V4GRPPLC9;00, No.of Policies: 1
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                template_name = groups["template_name"]
                number_of_policies = int(groups["number_of_policies"])
                sgt_detailed_dict.update(
                    {
                        "template_name": template_name,
                        "number_of_policies": number_of_policies,
                    }
                )
                continue

            #   3861840057
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                policy_id = int(groups["policy_id"])
                sgt_detailed_dict.update({"policy_id": policy_id})
                continue

        return parsed_dict


class ShowPlatformSoftwareSteeringPolicyPermissionsSchema(MetaParser):

    """Schema for "show platform software steering-policy forwarding-manager {switch} R0 permissions ipV4 {sgt} {dgt}" """

    schema = {
        "policy_permissions": {
            "sgt": {
                Any(): {
                    "source_sgt": int,
                    "destination_sgt": int,
                    "policy_id": int,
                },
            }
        }
    }


class ShowPlatformSoftwareSteeringPolicyPermissions(
    ShowPlatformSoftwareSteeringPolicyPermissionsSchema
):
    """Schema for show platform software steering-policy forwarding-manager {switch} R0 permissions ipV4 {sgt} {dgt}"""

    cli_command = [
        "show platform software steering-policy forwarding-manager switch {switch} R0 permissions ipv4 {sgt} {dgt}",
        "show platform software steering-policy forwarding-manager R0 permissions ipv4 {sgt} {dgt}",
    ]

    def cli(self, sgt, dgt, switch=None, output=None):
        if output is None:
            if not switch:
                cmd = self.cli_command[1].format(sgt=sgt, dgt=dgt)
            else:
                cmd = self.cli_command[0].format(sgt=sgt, dgt=dgt, switch=switch)
            output = self.device.execute(cmd)
        parsed_dict = {}

        sgt_dict = parsed_dict.setdefault("policy_permissions", {})
        policy_permissions_dict = oper_fill_tabular(
            header_fields=["sgt", "dgt", "Policy ID"],
            label_fields=["source_sgt", "destination_sgt", "policy_id"],
            device_output=output,
            device_os="iosxe",
            index=[0],
        ).entries

        sgt_dict.update({"sgt": policy_permissions_dict})

        for key1 in parsed_dict["policy_permissions"]["sgt"]:
            for key2 in parsed_dict["policy_permissions"]["sgt"][key1]:
                parsed_dict["policy_permissions"]["sgt"][key1][key2] = int(
                    parsed_dict["policy_permissions"]["sgt"][key1][key2]
                )

        return parsed_dict


class ShowPlatformSoftwareSteeringPolicyServiceSchema(MetaParser):

    """Schema for "show platform software steering-policy forwarding-manager switch {switch} r0 service-id {service_id}" """

    schema = {
        "policy_service": {
            "vnid": {
                Any(): {
                    "priority": int,
                    "weightage": int,
                    "vnid": int,
                    "rloc_ip": str,
                }
            }
        }
    }


class ShowPlatformSoftwareSteeringPolicyService(
    ShowPlatformSoftwareSteeringPolicyServiceSchema
):
    """Schema for show platform software steering-policy forwarding-manager switch {switch} r0 service-id {service_id}"""

    cli_command = [
        "show platform software steering-policy forwarding-manager switch {switch} r0 service-id {service_id}",
        "show platform software steering-policy forwarding-manager r0 service-id {service_id}",
    ]

    def cli(self, service_id, switch="", output=None):
        if output is None:
            if not switch:
                cmd = self.cli_command[1].format(service_id=service_id)
            else:
                cmd = self.cli_command[0].format(switch=switch, service_id=service_id)
            output = self.device.execute(cmd)

        parsed_dict = {}
        vnid_dict = parsed_dict.setdefault("policy_service", {})
        policy_service_dict = oper_fill_tabular(
            header_fields=["Priority", "Weightage", "VNID", "RLOC IP address"],
            label_fields=["priority", "weightage", "vnid", "rloc_ip"],
            device_output=output,
            device_os="iosxe",
            index=[2],
        ).entries

        vnid_dict.update({"vnid": policy_service_dict})

        for key1 in parsed_dict["policy_service"]["vnid"]:
            for key2 in parsed_dict["policy_service"]["vnid"][key1]:
                if key2 != "rloc_ip":
                    parsed_dict["policy_service"]["vnid"][key1][key2] = int(
                        parsed_dict["policy_service"]["vnid"][key1][key2]
                    )

        return parsed_dict


class ShowPlatformSoftwareSteeringPolicyServiceAllSchema(MetaParser):

    """Schema for "show platform software steering-policy forwarding-manager switch {switch} F0 service-all" """

    schema = {
        "services_ip": {
            Any(): {
                "service_id": int,
                "service_vrf": int,
                "firewall_mode": str,
                "service_selector": int,
                "service_ip": str,
                "number_of_rlocs": int,
            }
        }
    }


class ShowPlatformSoftwareSteeringPolicyServiceAll(
    ShowPlatformSoftwareSteeringPolicyServiceAllSchema
):
    """Schema for show platform software steering-policy forwarding-manager switch {switch} F0 service-all"""

    cli_command = [
        "show platform software steering-policy forwarding-manager switch {switch} F0 service-all",
        "show platform software steering-policy forwarding-manager F0 service-all",
    ]

    def cli(self, switch="", output=None):
        if output is None:
            if not switch:
                cmd = self.cli_command[1]
            else:
                cmd = self.cli_command[0].format(switch=switch)
            output = self.device.execute(cmd)

        parsed_dict = {}
        services_dict = oper_fill_tabular(
            header_fields=[
                "Service ID",
                "Service VRF",
                "Firewall mode",
                "Service Selector",
                "Service IP",
                "No. Of RLOCs",
            ],
            label_fields=[
                "service_id",
                "service_vrf",
                "firewall_mode",
                "service_selector",
                "service_ip",
                "number_of_rlocs",
            ],
            device_output=output,
            device_os="iosxe",
            index=[4],
        ).entries

        parsed_dict.update({"services_ip": services_dict})

        for key1 in parsed_dict["services_ip"]:
            for key2 in parsed_dict["services_ip"][key1]:
                if key2 != "firewall_mode" and key2 != "service_ip":
                    parsed_dict["services_ip"][key1][key2] = int(
                        parsed_dict["services_ip"][key1][key2]
                    )

        return parsed_dict


class ShowPlatformSoftwareSteeringPolicySummarySchema(MetaParser):

    """Schema for "show platform software steering-policy forwarding-manager switch {switch} F0 policy-summary" """

    schema = {
        "policy_index": {
            Any(): {
                "policy": str,
                "index": int,
                "num_ref": int,
                "num_entries": int,
            },
        }
    }


class ShowPlatformSoftwareSteeringPolicySummary(
    ShowPlatformSoftwareSteeringPolicySummarySchema
):
    """Schema for show platform software steering-policy forwarding-manager switch {switch} F0 policy-summary"""

    cli_command = [
        "show platform software steering-policy forwarding-manager switch {switch} F0 policy-summary",
        "show platform software steering-policy forwarding-manager F0 policy-summary",
    ]

    def cli(self, switch=None, output=None):
        if output is None:
            if not switch:
                cmd = self.cli_command[1]
            else:
                cmd = self.cli_command[0].format(switch=switch)
            output = self.device.execute(cmd)

        parsed_dict = {}
        policy_index_dict = oper_fill_tabular(
            header_fields=["Policy", "Index", "Num Ref", "Num Entries"],
            label_fields=["policy", "index", "num_ref", "num_entries"],
            device_output=output,
            device_os="iosxe",
            index=[1],
        ).entries

        parsed_dict.update({"policy_index": policy_index_dict})

        for key1 in parsed_dict["policy_index"]:
            for key2 in parsed_dict["policy_index"][key1]:
                if key2 != "policy":
                    parsed_dict["policy_index"][key1][key2] = int(
                        parsed_dict["policy_index"][key1][key2]
                    )
        return parsed_dict


class ShowPlatformSoftwareBPCrimsonContentConfigSchema(MetaParser):
    """Schema for show platform software bp crimson content config"""

    schema = {
        Any(): {
            "fipskey": str,
            "interface_details": {
                Any(): {
                    "link": int,
                    "slot": str,
                }
            },
            "node_details": {
                "node_number": int,
                "priority": int,
            },
            "svl_link": {
                "link": int,
            },
            "svl_ports": {
                "domain": int,
                "mode": str,
                "node": int,
                "router_id": str,
            },
        },
    }


class ShowPlatformSoftwareBPCrimsonContentConfig(
    ShowPlatformSoftwareBPCrimsonContentConfigSchema
):
    """Parser for
    show platform software bp crimson content config
    """

    cli_command = "show platform software bp crimson content config"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Node    Domain    Mode          Router-ID
        # 1       1         Aggregation   0.0.0.0
        p1 = re.compile(
            r"(?P<node>(\d)) +(?P<domain>(\d)) + (?P<mode>(\w+)) +(?P<router_id>(\S+))"
        )

        # FIPSKEY
        # 4D56F017FFC920A5FA0EF11397788E917931D1D1AE48F9C0
        p2 = re.compile(r"^(?P<fipskey>(\w+)$)")

        # Node    Priority
        # 1       1
        p3 = re.compile(r"^(?P<node_number>(\d)) +(?P<priority>(\d))")

        # Configured SVL Links:
        # Link ID: 1
        p4 = re.compile(r"^Link +ID+\: +(?P<link>\d+)")

        # Interface                     Link    Slot:Bay:Port
        # HundredGigE1/0/13             1       1:0:13
        # HundredGigE1/0/14             1       1:0:14
        p5 = re.compile(r"^(?P<interface>(\S+)) +(?P<link>(\d+)) +(?P<slot>(\S+))$")

        for line in output.splitlines():
            line = line.strip()

            # Node    Domain    Mode          Router-ID
            # 1       1         Aggregation   0.0.0.0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                domain_dict = node_dict.setdefault("svl_ports", {})
                domain_dict["node"] = int(group["node"])
                domain_dict["domain"] = int(group["domain"])
                domain_dict["mode"] = group["mode"]
                domain_dict["router_id"] = group["router_id"]
                continue

            # FIPSKEY
            # 4D56F017FFC920A5FA0EF11397788E917931D1D1AE48F9C0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                node_dict["fipskey"] = group["fipskey"]
                continue

            # Node    Priority
            # 1       1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                node_number = group["node_number"]
                node_dict = ret_dict.setdefault(node_number, {})
                priority_dict = node_dict.setdefault("node_details", {})
                priority_dict["node_number"] = int(group["node_number"])
                priority_dict["priority"] = int(group["priority"])
                continue

            # Configured SVL Links:
            # Link ID: 1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                link_dict = node_dict.setdefault("svl_link", {})
                link_dict["link"] = int(group["link"])
                continue

            # Interface                     Link    Slot:Bay:Port
            # HundredGigE1/0/13             1       1:0:13
            # HundredGigE1/0/14             1       1:0:14
            m = p5.match(line)
            if m:
                group = m.groupdict()
                stack_ports = node_dict.setdefault("interface_details", {})
                each_ports = stack_ports.setdefault(group["interface"], {})
                each_ports["link"] = int(group["link"])
                each_ports["slot"] = group["slot"]
                continue

        return ret_dict


class ShowPlatformSoftwareNodeClusterManagerSwitchB0NodeSchema(MetaParser):
    """
    Schema for show platform software node cluster-manager switch {mode} B0 node {node}
    """

    schema = {
        Any(): str,
    }


class ShowPlatformSoftwareNodeClusterManagerSwitchB0Node(
    ShowPlatformSoftwareNodeClusterManagerSwitchB0NodeSchema
):
    """Parser for show platform software node cluster-manager switch {mode} B0 node {node}"""

    cli_command = (
        "show platform software node cluster-manager switch {mode} B0 node {node}"
    )

    def cli(self, mode, node, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode, node=node))

        # initial variables
        ret_dict = {}
        # Node status is : NODE_STATUS_UP
        p1 = re.compile(r"^(?P<node_description>[\w\s]+)\: (?P<status>.*)$")

        for line in output.splitlines():
            line = line.strip()
            # Node status is : NODE_STATUS_UP
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict[group["node_description"]] = group["status"]
                continue
        return ret_dict


# ======================================================================================
# Parser Schema for 'show platform software punt-policer'
# ======================================================================================


class ShowPlatformSoftwarePuntPolicerSchema(MetaParser):
    """Schema for "show platform software punt-policer" """

    schema = {
        "punt_policer": {
            Any(): {
                "description": str,
                "config_rate_normal_pps": int,
                "config_rate_high_pps": int,
                "conform_pkts_normal": int,
                "conform_pkts_high": int,
                "dropped_pkts_normal": int,
                "dropped_pkts_high": int,
                "config_burst_normal_pkts": int,
                "config_burst_high_pkts": int,
                "config_alert_normal": str,
                "config_alert_high": str,
            }
        }
    }


# ================================================================================
# Parser for 'show platform software punt-policer'
# ================================================================================


class ShowPlatformSoftwarePuntPolicer(ShowPlatformSoftwarePuntPolicerSchema):
    """parser for "show platform software punt-policer" """

    cli_command = "show platform software punt-policer"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        #   2    IPv4 Options   4000     3000     0        0         0         0           4000     3000     Off      Off
        p1 = re.compile(
            r"^(?P<punt_cause>\d+)\s+(?P<description>(([A-Za-z0-9_-]+ ?){5}).*\s+|([A-Za-z0-9_-]+ ?))"
            r"\s+(?P<config_rate_normal_pps>\d+)\s+(?P<config_rate_high_pps>\d+)\s+(?P<conform_pkts_normal>\d+)"
            r"\s+(?P<conform_pkts_high>\d+)\s+(?P<dropped_pkts_normal>\d+)\s+(?P<dropped_pkts_high>\d+)"
            r"\s+(?P<config_burst_normal_pkts>\d+)\s+(?P<config_burst_high_pkts>\d+)\s+(?P<config_alert_normal>\w+)"
            r"\s+(?P<config_alert_high>\w+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            #   2    IPv4 Options  4000     3000     0       0      0       0        4000     3000     Off      Off
            m = p1.match(line)
            if m:
                group = m.groupdict()
                punt_cause = int(group.pop("punt_cause"))
                description = group.pop("description")
                config_alert_normal = group.pop("config_alert_normal")
                config_alert_high = group.pop("config_alert_high")
                punt_policer_dict = parsed_dict.setdefault(
                    "punt_policer", {}
                ).setdefault(punt_cause, {})
                punt_policer_dict["description"] = description.rstrip()
                punt_policer_dict.update(
                    {
                        k: int(v.rstrip().replace(" ", "_").lower())
                        for k, v in group.items()
                    }
                )
                punt_policer_dict.update(
                    [
                        ("config_alert_normal", config_alert_normal),
                        ("config_alert_high", config_alert_high),
                    ]
                )

                continue

        return parsed_dict


# =================================================================
# Parser Schema for show platform software factory-reset secure log
# =================================================================


class ShowPlatformSoftwareFactoryResetSecureLogSchema(MetaParser):

    """Schema for show platform software factory-reset secure log"""

    schema = {
        "start_time": str,
        "end_time": str,
        Any(): {
            Optional("mid"): str,
            Optional("nist"): str,
            Optional("pnm"): str,
            Optional("prv"): str,
            Optional("sn"): str,
            Optional("mnm"): str,
            Optional("status"): str,
        },
    }


# ===========================================================
#  parser for show platform software factory-reset secure log
# ===========================================================


class ShowPlatformSoftwareFactoryResetSecureLog(
    ShowPlatformSoftwareFactoryResetSecureLogSchema
):

    """Parser for  show platform software factory-reset secure log"""

    cli_command = "show platform software factory-reset secure log"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # START : 13-07-2022, 06:27:18
        p0 = re.compile(r".*START\s+:\s+(?P<start_time>.*)")

        #   END : 13-07-2022, 06:30:01
        p1 = re.compile(r".*END\s+:\s+(?P<end_time>.*)")

        #  -eMMC-
        p2 = re.compile(r"-(?P<partition>\S+)-$")

        #  PNM : nor
        #  NIST : PURGE
        p3 = re.compile(r"^(?P<partition_key>\S+)\s+:\s+(?P<partition_value>\S+)")

        for line in output.splitlines():
            line = line.strip()
            m = p0.match(line)

            if m:
                group = m.groupdict()
                ret_dict["start_time"] = group["start_time"]
                continue

            #   END : 13-07-2022, 06:30:01
            m1 = p1.match(line)

            if m1:
                group = m1.groupdict()
                ret_dict["end_time"] = group["end_time"]
                continue

            # -eMMC-
            m2 = p2.match(line)

            if m2:
                group = m2.groupdict()
                partition_dict = ret_dict.setdefault(group["partition"], {})
                continue

            #  NIST : PURGE
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                partition_dict.update(
                    {group["partition_key"].lower(): group["partition_value"]}
                )
                continue

        return ret_dict


# ==========================================================================================
# Parser Schema for 'show platform soft infra bipc | inc buffer'
# ==========================================================================================


class ShowPlatformSoftInfraBipcSchema(MetaParser):
    """Schema for "show platform soft infra bipc | inc buffer" """

    schema = {
        "platform_soft_infra_bipc": {
            "total_buffers_allocated": int,
            "total_buffers_freed": int,
            "total_buffer_alloc_failure": int,
        },
        "buffers": {
            "rx_buffers_allocated": int,
            "rx_buffer_freed": int,
            "tx_buffer_allocated": int,
            "tx_buffer_freed": int,
        },
        "failure": {"rx_buffer_alloc_failure": int, "tx_buffer_alloc_failure": int},
    }


# ================================================================================
# Parser for 'show platform soft infra bipc | inc buffer'
# ================================================================================


class ShowPlatformSoftInfraBipc(ShowPlatformSoftInfraBipcSchema):
    """parser for "show platform soft infra bipc | inc buffer" """

    cli_command = "show platform soft infra bipc | inc buffer"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # 338036 total buffers allocated
        p1 = re.compile(r"^(?P<total>\d+)\s+total\s+buffers\s+allocated$")

        # 338036 total buffers freed
        p2 = re.compile(r"^(?P<total>\d+)\s+total\s+buffers\s+freed$")

        # 307831 rx buffer allocated
        p3 = re.compile(r"^(?P<total>\d+)\s+rx\s+buffer\s+allocated$")

        # 307831 rx buffer freed
        p4 = re.compile(r"^(?P<total>\d+)\s+rx\s+buffer\s+freed$")

        # 30205 tx buffer allocated
        p5 = re.compile(r"^(?P<total>\d+)\s+tx\s+buffer\s+allocated$")

        # 30205 tx buffer freed
        p6 = re.compile(r"^(?P<total>\d+)\s+tx\s+buffer\s+freed$")

        # 0 total buffer alloc failure
        p7 = re.compile(r"^(?P<total>\d+)\s+total\s+buffer\s+alloc\s+failure$")

        # 0 rx buffer alloc failure
        p8 = re.compile(r"^(?P<total>\d+)\s+rx\s+buffer\s+alloc\s+failure$")

        # 0 tx buffer alloc failure
        p9 = re.compile(r"^(?P<total>\d+)\s+tx\s+buffer\s+alloc\s+failure$")

        for line in output.splitlines():
            line = line.strip()

            # 338036 total buffers allocated
            m = p1.match(line)
            if m:
                group = m.groupdict()
                buffer_info_dict = parsed_dict.setdefault(
                    "platform_soft_infra_bipc", {}
                )
                buffer_info_dict["total_buffers_allocated"] = int(group["total"])
                continue

            #  338036 total buffers freed
            m = p2.match(line)
            if m:
                group = m.groupdict()
                buffer_info_dict["total_buffers_freed"] = int(group["total"])
                continue

            # 307831 rx buffer allocated
            m = p3.match(line)
            if m:
                group = m.groupdict()
                buffer_dict = parsed_dict.setdefault("buffers", {})
                buffer_dict["rx_buffers_allocated"] = int(group["total"])
                continue

            # 307831 rx buffer freed
            m = p4.match(line)
            if m:
                group = m.groupdict()
                buffer_dict["rx_buffer_freed"] = int(group["total"])
                continue

            # 30205 tx buffer allocated
            m = p5.match(line)
            if m:
                group = m.groupdict()
                buffer_dict["tx_buffer_allocated"] = int(group["total"])
                continue

            # 30205 tx buffer freed
            m = p6.match(line)
            if m:
                group = m.groupdict()
                buffer_dict["tx_buffer_freed"] = int(group["total"])
                continue

            # 0 total buffer alloc failure
            m = p7.match(line)
            if m:
                group = m.groupdict()
                buffer_info_dict["total_buffer_alloc_failure"] = int(group["total"])
                continue

            # 0 rx buffer alloc failure
            m = p8.match(line)
            if m:
                group = m.groupdict()
                failure_dict = parsed_dict.setdefault("failure", {})
                failure_dict["rx_buffer_alloc_failure"] = int(group["total"])
                continue

            # 0 tx buffer alloc failure
            m = p9.match(line)
            if m:
                group = m.groupdict()
                failure_dict["tx_buffer_alloc_failure"] = int(group["total"])
                continue

        return parsed_dict


# ======================================================
# Parser for 'show platform software wired-client switch <active/standby> f0 '
# ======================================================


class ShowPlatformSoftwareWiredClientSwitchActiveF0Schema(MetaParser):
    """Schema for show platform software wired-client switch <active/standby>} f0"""

    schema = {
        "mac_address": {
            Any(): {
                "id": str,
                "fwd": str,
                "open_access": str,
                "status": str,
            },
        },
    }


class ShowPlatformSoftwareWiredClientSwitchActiveF0(
    ShowPlatformSoftwareWiredClientSwitchActiveF0Schema
):
    """Parser for show platform software wired-client switch <active/standby> f0"""

    cli_command = "show platform software wired-client switch {switch} f0"

    def cli(self, switch=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch=switch))

        # 0x13151bdb  001b.0c18.918d  Yes      No            Done
        p1 = re.compile(
            r"^(?P<id>\S+)\s+(?P<mac_address>\S+)\s+(?P<fwd>\w+)\s+(?P<open_access>\w+)\s+(?P<status>\w+)\s+$"
        )

        ret_dict = {}

        for line in output.splitlines():
            # 0x13151bdb  001b.0c18.918d  Yes      No            Done
            match_obj = p1.match(line)
            if match_obj:
                dict_val = match_obj.groupdict()
                mac_address_var = dict_val["mac_address"]
                if "mac_address" not in ret_dict:
                    mac_address = ret_dict.setdefault("mac_address", {})
                if mac_address_var not in ret_dict["mac_address"]:
                    mac_address_dict = ret_dict["mac_address"].setdefault(
                        mac_address_var, {}
                    )
                mac_address_dict["id"] = dict_val["id"]
                mac_address_dict["fwd"] = dict_val["fwd"]
                mac_address_dict["open_access"] = dict_val["open_access"]
                mac_address_dict["status"] = dict_val["status"]
                continue

        return ret_dict


# ========================================================================
# Schema for 'show platform software wired-client switch {switch_state} r0 '
# ========================================================================


class ShowPlatformSoftwareWiredClientSwitchR0Schema(MetaParser):
    """Schema for show platform software wired-client switch {switch_state} r0"""

    schema = {
        "wired_client": {
            Any(): {
                "id": str,
                "mac": str,
                "fwd": str,
                "open_access": str,
            },
        },
    }


# ==========================================================================
# Parser for 'show platform software wired-client switch {switch_state} r0 '
# ==========================================================================


class ShowPlatformSoftwareWiredClientSwitchR0(
    ShowPlatformSoftwareWiredClientSwitchR0Schema
):
    """Parser for show platform software wired-client switch {switch_state} r0"""

    cli_command = "show platform software wired-client switch {switch_state} r0"

    def cli(self, switch_state, output=None):
        if output is None:
            output = self.device.execute(
                self.cli_command.format(switch_state=switch_state)
            )

        # 0x13151bdb  001b.0c18.918d  Yes    No
        p1 = re.compile(
            r"^(?P<id>\S+)\s+(?P<mac>\S+)\s+(?P<fwd>\w+)\s+(?P<open_access>\w+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # 0x13151bdb  001b.0c18.918d  Yes    No
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                id_var = dict_val["id"]
                if "wired_client" not in ret_dict:
                    wired_client = ret_dict.setdefault("wired_client", {})
                if id_var not in ret_dict["wired_client"]:
                    id_dict = ret_dict["wired_client"].setdefault(id_var, {})
                id_dict["id"] = dict_val["id"]
                id_dict["mac"] = dict_val["mac"]
                id_dict["fwd"] = dict_val["fwd"]
                id_dict["open_access"] = dict_val["open_access"]
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform software monitor session {session}'
# ======================================================


class ShowPlatformSoftwareMonitorSessionSchema(MetaParser):
    """Schema for show platform software monitor session {session}"""

    schema = {
        "span_session": str,
        "fed_session": str,
        "type": str,
        "prev_type": str,
        Optional("ingress_source_ports"): str,
        Optional("egress_source_ports"): str,
        Optional("ingress_local_source_ports"): str,
        Optional("egress_local_source_ports"): str,
        Optional("destination_ports"): list,
        Optional("ingress_source_vlans"): str,
        Optional("egress_source_vlans"): str,
        Optional("ingress_up_source_vlans"): str,
        Optional("egress_up_source_vlans"): str,
        Optional("source_trunk_filter_vlans"): str,
        "rspan": {"destination_vlan": int, "source_vlan": int, "source_vlan_sav": int},
        "destination_port_encap": str,
        "destination_port_ingress_encap": str,
        "destination_port_ingress_vlan": str,
        "source_session": str,
        "destination_session": str,
        "destination_port_cfgd": str,
        "rspn_destination_cfg": str,
        "rspn_source_vld": str,
        "dstination_cli_cfg": str,
        "dstination_prt_init": str,
        "pslclcfgd": str,
        "flags": list,
        "remote_destination_port": str,
        "destination_port_group": str,
        Optional("erspan"): {
            "id": str,
            Optional("org_ip"): str,
            Optional("destination_ip"): str,
            Optional("org_ipv6"): str,
            Optional("destination_ipv6"): str,
            Optional("ip_ttl"): int,
            Optional("dscp"): int,
            Optional("ipv6_flow_label"): int,
            Optional("vrfid"): int,
            Optional("state"): str,
            Optional("tun_id"): int,
        },
    }


class ShowPlatformSoftwareMonitorSession(ShowPlatformSoftwareMonitorSessionSchema):
    """Parser for show platform software monitor session {session}"""

    cli_command = "show platform software monitor session {session}"

    def cli(self, session="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(session=session))

        # Span Session 3 (FED Session 2):
        p1 = re.compile(
            r"^Span\s+Session\s+(?P<span_session>\d+)\s+\(FED\s+Session\s+(?P<fed_session>\w+)\):$"
        )

        # Type:      ERSPAN Source
        p2 = re.compile(r"^Type:\s+(?P<type>.+)$")

        # Prev type: Unknown
        p3 = re.compile(r"^Prev\s+type:\s+(?P<prev_type>[\w\s]+)$")

        # Ingress Src Ports: Fif2/0/2
        # Ingress Src Ports: Po23 Po25 Po27 Po29 Po31 Po33 Po35 Po37 Po39 Po41 Po42 Po43 Po44 Po45
        p4 = re.compile(r"^Ingress\s+Src\s+Ports:\s+(?P<ingress_source_ports>.+)$")

        # Egress Src Ports: Fif2/0/4
        p5 = re.compile(r"^Egress\s+Src\s+Ports:\s+(?P<egress_source_ports>\S+)$")

        # Ingress Local Src Ports: (null)
        p6 = re.compile(
            r"^Ingress\s+Local\s+Src\s+Ports:\s+\((?P<ingress_local_source_ports>(?!null)\S+)\)$"
        )

        # Egress Local Src Ports: (null)
        p7 = re.compile(
            r"^Egress\s+Local\s+Src\s+Ports:\s+\((?P<egress_local_source_ports>(?!null)\S+)\)$"
        )

        # Destination Ports: Fif2/0/10 2/0/5
        p8 = re.compile(r"^Destination\s+Ports:\s+(?P<destination_ports>.+)$")

        # Ingress Src Vlans: 3
        p9 = re.compile(r"^Ingress\s+Src\s+Vlans:\s+(?P<ingress_source_vlans>\d+)$")

        # Egress Src Vlans: 3
        p10 = re.compile(r"^Egress\s+Src\s+Vlans:\s+(?P<egress_source_vlans>\d+)$")

        # Ingress Up Src Vlans: (null)
        p11 = re.compile(
            r"^Ingress\s+Up\s+Src\s+Vlans:\s+\((?P<ingress_up_source_vlans>(?!null)\S+)\)$"
        )

        # Egress Up Src Vlans:  (null)
        p12 = re.compile(
            r"^Egress\s+Up\s+Src\s+Vlans:\s+\((?P<egress_up_source_vlans>(?!null)\S+)\)$"
        )

        # Src Trunk filter Vlans: 3
        p13 = re.compile(
            r"^Src\s+Trunk\s+filter\s+Vlans:\s+(?P<source_trunk_filter_vlans>\d+)$"
        )

        # RSPAN dst vlan: 0
        p14 = re.compile(r"^RSPAN\s+dst\s+vlan:\s+(?P<destination_vlan>\d+)$")

        # RSPAN src vlan: 0
        p15 = re.compile(r"^RSPAN\s+src\s+vlan:\s+(?P<source_vlan>\d+)$")

        # RSPAN src vlan sav: 0
        p16 = re.compile(r"^RSPAN\s+src\s+vlan\s+sav:\s+(?P<source_vlan_sav>\d+)$")

        # Dest port encap = 0x0000
        p17 = re.compile(r"^Dest\s+port\s+encap\s+=\s+(?P<destination_port_encap>\S+)$")

        # Dest port ingress encap = 0x0000
        p18 = re.compile(
            r"^Dest\s+port\s+ingress\s+encap\s+=\s+(?P<destination_port_ingress_encap>\S+)$"
        )

        # Dest port ingress vlan = 0x0
        p19 = re.compile(
            r"^Dest\s+port\s+ingress\s+vlan\s+=\s+(?P<destination_port_ingress_vlan>\S+)$"
        )

        # SrcSess: 1  DstSess: 0 DstPortCfgd: 0  RspnDstCfg: 0  RspnSrcVld: 0
        p20 = re.compile(
            r"^SrcSess:\s+(?P<source_session>\d+)\s+DstSess:\s+(?P<destination_session>\d+)\s+DstPortCfgd:\s+(?P<destination_port_cfgd>\d+)\s+RspnDstCfg:\s+(?P<rspn_destination_cfg>\d+)\s+RspnSrcVld:\s+(?P<rspn_source_vld>\d+)$"
        )

        # DstCliCfg: 0  DstPrtInit: 0  PsLclCfgd: 0
        p21 = re.compile(
            r"^DstCliCfg:\s+(?P<dstination_cli_cfg>\d+)\s+DstPrtInit:\s+(?P<dstination_prt_init>\d+)\s+PsLclCfgd:\s+(?P<pslclcfgd>\d+)$"
        )

        # Flags: 0x00000002 VSPAN
        p22 = re.compile(r"^Flags:\s+(?P<flags>.+)$")

        # Remote dest port: 0   Dest port group: 0
        p23 = re.compile(
            r"^Remote dest port:\s(?P<remote_destination_port>\w+)\s+Dest port group:\s(?P<destination_port_group>\w+)$"
        )

        # ERSPAN Id    : 11
        p24 = re.compile(r"^ERSPAN\sId\s+:\s+(?P<id>\d+)$")

        # ERSPAN Org Ip: 0.0.0.0
        p25 = re.compile(r"^ERSPAN\s+Org\s+Ip:\s+(?P<org_ip>[\d.]+)$")

        # ERSPAN Dst Ip: 0.0.0.0
        p26 = re.compile(r"^ERSPAN\s+Dst\s+Ip:\s+(?P<destination_ip>[\d.]+)$")

        #  ERSPAN Org Ipv6: 2002::1
        p27 = re.compile(r"^ERSPAN\s+Org\s+Ipv6:\s+(?P<org_ipv6>[\d:]+)$")

        # ERSPAN Dst Ipv6: 2001::1
        p28 = re.compile(r"^ERSPAN\s+Dst\s+Ipv6:\s+(?P<destination_ipv6>[\d:]+)$")

        # ERSPAN Ip Ttl: 255
        p29 = re.compile(r"^ERSPAN\s+Ip\s+Ttl:\s+(?P<ip_ttl>\d+)$")

        # ERSPAN DSCP  : 0
        p30 = re.compile(r"^ERSPAN DSCP\s+:\s+(?P<dscp>\d+)$")

        # ERSPAN Ipv6 flow label: 0
        p31 = re.compile(r"^ERSPAN Ipv6 flow label:\s+(?P<ipv6_flow_label>\d+)$")

        # ERSPAN VRFID   : 0
        p32 = re.compile(r"^ERSPAN VRFID\s+:\s+(?P<vrfid>\d+)$")

        # ERSPAN State : Enabled
        p33 = re.compile(r"^ERSPAN State :\s+(?P<state>\w+)$")

        # ERSPAN Tun id: 1251
        p34 = re.compile(r"^ERSPAN Tun id:\s+(?P<tun_id>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Span Session 3 (FED Session 2):
            m = p1.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Type:      ERSPAN Source
            m = p2.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Prev type: Unknown
            m = p3.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Ingress Src Ports: Fif2/0/2
            m = p4.match(line)
            if m:
                ret_dict["ingress_source_ports"] = Common.convert_intf_name(
                    m.groupdict()["ingress_source_ports"]
                )
                continue

            # Egress Src Ports: Fif2/0/4
            m = p5.match(line)
            if m:
                ret_dict["egress_source_ports"] = Common.convert_intf_name(
                    m.groupdict()["egress_source_ports"]
                )
                continue

            # Ingress Local Src Ports: (null)
            m = p6.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Egress Local Src Ports: (null)
            m = p7.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Destination Ports: Fif2/0/10 2/0/5
            m = p8.match(line)
            if m:
                dst_ports = [
                    Common.convert_intf_name(port)
                    for port in m.groupdict()["destination_ports"].split()
                ]
                ret_dict["destination_ports"] = dst_ports
                continue

            # Ingress Src Vlans: 3
            m = p9.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Egress Src Vlans: 3
            m = p10.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Ingress Up Src Vlans: 3
            m = p11.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Egress Up Src Vlans:  (null)
            m = p12.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Src Trunk filter Vlans: 3
            m = p13.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # RSPAN dst vlan: 0
            m = p14.match(line)
            if m:
                rspan_dict = ret_dict.setdefault("rspan", {})
                rspan_dict.setdefault(
                    "destination_vlan", int(m.groupdict()["destination_vlan"])
                )
                continue

            # RSPAN src vlan: 0
            m = p15.match(line)
            if m:
                rspan_dict.setdefault("source_vlan", int(m.groupdict()["source_vlan"]))
                continue

            # RSPAN src vlan sav: 0
            m = p16.match(line)
            if m:
                rspan_dict.setdefault(
                    "source_vlan_sav", int(m.groupdict()["source_vlan_sav"])
                )
                continue

            # Dest port encap = 0x0000
            m = p17.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Dest port ingress encap = 0x0000
            m = p18.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Dest port ingress vlan = 0x0
            m = p19.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # SrcSess: 1  DstSess: 0 DstPortCfgd: 0  RspnDstCfg: 0  RspnSrcVld: 0
            m = p20.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # DstCliCfg: 0  DstPrtInit: 0  PsLclCfgd: 0
            m = p21.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # Flags: 0x00000002 VSPAN
            m = p22.match(line)
            if m:
                ret_dict["flags"] = m.groupdict()["flags"].split(" ")
                continue

            # Remote dest port: 0   Dest port group: 0
            m = p23.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

            # ERSPAN Id    : 11
            m = p24.match(line)
            if m:
                erspan_dict = ret_dict.setdefault("erspan", {})
                erspan_dict.setdefault("id", m.groupdict()["id"])
                continue

            # ERSPAN Org Ip: 0.0.0.0
            m = p25.match(line)
            if m:
                erspan_dict.update(m.groupdict())
                continue

            # ERSPAN Dst Ip: 0.0.0.0
            m = p26.match(line)
            if m:
                erspan_dict.update(m.groupdict())
                continue

            # ERSPAN Org Ipv6: 2002::1
            m = p27.match(line)
            if m:
                erspan_dict.update(m.groupdict())
                continue

            # ERSPAN Dst Ipv6: 2001::1
            m = p28.match(line)
            if m:
                erspan_dict.update(m.groupdict())
                continue

            # ERSPAN Ip Ttl: 255
            m = p29.match(line)
            if m:
                erspan_dict.setdefault("ip_ttl", int(m.groupdict()["ip_ttl"]))
                continue

            # ERSPAN DSCP  : 0
            m = p30.match(line)
            if m:
                erspan_dict.setdefault("dscp", int(m.groupdict()["dscp"]))
                continue

            # ERSPAN Ipv6 flow label: 0
            m = p31.match(line)
            if m:
                erspan_dict.setdefault(
                    "ipv6_flow_label", int(m.groupdict()["ipv6_flow_label"])
                )
                continue

            # ERSPAN VRFID   : 0
            m = p32.match(line)
            if m:
                erspan_dict.setdefault("vrfid", int(m.groupdict()["vrfid"]))
                continue

            # ERSPAN State : Enabled
            m = p33.match(line)
            if m:
                erspan_dict.update(m.groupdict())
                continue

            # ERSPAN Tun id: 1251
            m = p34.match(line)
            if m:
                erspan_dict.setdefault("tun_id", int(m.groupdict()["tun_id"]))
                continue

        return ret_dict


class ShowPlatformSoftwareTdlContentBpConfigSchema(MetaParser):
    """
    Schema for 'show platform software tdl-database content bp config {mode}'
    """

    schema = {
        "node": {
            Any(): {
                "node": int,
                Optional("domain"): int,
                Optional("mode"): str,
                Optional("router_id"): str,
                Optional("priority"): int,
            },
        }
    }


class ShowPlatformSoftwareTdlContentBpConfig(
    ShowPlatformSoftwareTdlContentBpConfigSchema
):
    """
    Parser for 'show platform software tdl-database content bp config {mode}'
    """

    cli_command = "show platform software tdl-database content bp config {mode}"

    def cli(self, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}

        # Node    Domain    Mode          Router-ID
        # 1       2         Aggregation
        p1 = re.compile(
            "^(?P<node>\d+)\s+(?P<domain>\d+)\s+(?P<mode>\w+)(\s+(?P<router_id>\w+))?$"
        )

        # Node    Priority
        # 1       1
        p2 = re.compile("^(?P<node>\d+)\s+(?P<priority>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # Node    Domain    Mode          Router-ID
            # 1       2         Aggregation
            m = p1.match(line)
            if m:
                group = m.groupdict()
                node = group.pop("node")
                node_dict = ret_dict.setdefault("node", {})
                n_node_dict = node_dict.setdefault(int(node), {})

                n_node_dict.update(
                    {
                        "node": int(node),
                        "domain": int(group["domain"]),
                        "mode": group["mode"],
                    }
                )
                if group["router_id"]:
                    n_node_dict.update({"router_id": group["router_id"]})
                continue

            # Node    Priority
            # 1       1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                node = group.pop("node")
                node_dict = ret_dict.setdefault("node", {})
                n_node_dict = node_dict.setdefault(int(node), {})
                n_node_dict.update(
                    {"node": int(node), "priority": int(group["priority"])}
                )
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform software install-manager chassis active r0 operation history summary'
# ======================================================


class ShowPlatformSoftwareInstallManagerChassisActiveR0OperationHistorySummary(
    ShowPlatformSoftwareInstallManagerRpActiveOperationHistorySummary
):
    """
    Parser for 'show platform software install-manager chassis active r0 operation history summary'
    """

    cli_command = "show platform software install-manager chassis active r0 operation history summary"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        return super().cli(output=output)


class ShowPlatformSoftwareBpCrimsonStatisticsSchema(MetaParser):
    """
    Schema for show platform software bp crimson statistics
    """

    schema = {
        "bp_crimson_statistics": {
            "initialized": str,
            "config_database_init_d": str,
            "config_db_persist": str,
            "config_db_restorable": str,
            "config_lock_mgr_dbid": int,
            "oper_database_init_d": str,
            "oper_lock_mgr_dbid": int,
            "garbage_collections": int,
        },
        Optional("bp_svl_crimson_statistics"): {
            "config_notify_mgr_id": int,
            "config_dyn_tables_reg_d": int,
            "config_dyn_reg_failures": int,
            "config_dyn_tables_dereg_d": int,
            "config_dereg_deferred": int,
            "config_dereg_failures": int,
            "config_table_updates": int,
            "config_applied": int,
            "config_skipped": int,
            "oper_notify_mgr_dbid": int,
            "oper_dyn_tables_reg_d": int,
            "oper_dyn_reg_failures": int,
            "oper_dyn_tables_dereg_d": int,
            "oper_dereg_s_deferred": int,
            "oper_dereg_failures": int,
            "oper_table_updates": int,
            "dyn_table_failures": int,
            "dyn_table_dereg_failures": int,
            "pending_notifications": int,
            "notifications_highwater": int,
            "notifications_processed": int,
            "notification_failures": int,
        },
        Optional("bp_remote_db_statistics"): {
            "get_requests": {
                "total_requests": int,
                "pending_requests": int,
                "timed_out_requests": int,
                "failed_requests": int,
            },
            "set_requests": {
                "total_requests": int,
                "pending_requests": int,
                "timed_out_requests": int,
                "failed_requests": int,
            },
            "in_progress_requests": {
                "type": str,
                "db_id": int,
                "batch_id": int,
                "op_id": int,
                "task_pid": int,
            },
            Optional("dbal_response_time"): {
                "max": int,
            },
            Optional("record_free_failures"): {
                "total_failures": int,
            },
        },
    }


class ShowPlatformSoftwareBpCrimsonStatistics(
    ShowPlatformSoftwareBpCrimsonStatisticsSchema
):
    """Parser for show platform software bp crimson statistics"""

    cli_command = "show platform software bp crimson statistics"

    def cli(self, output=None):
        # excute command to get output
        output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}

        # BP Crimson Statistics
        p1 = re.compile("^(?P<bp_crimson_statistics>BP Crimson Statistics)$")

        # Regexp  for  all the  lines  which fals in the below  pattern
        # Initialized            : Yes
        p2 = re.compile("^(?P<description>[\w'\s]+)\:\s+(?P<value>\w+)$")

        # BP SVL Crimson Statistics
        p3 = re.compile("^(?P<bp_svl_crimson_statistics>BP SVL Crimson Statistics)$")

        # BP Remote DB Statistics
        p4 = re.compile("^(?P<bp_remote_db_statistics>BP Remote DB Statistics)$")

        # GET Requests:
        p5 = re.compile("^(?P<get_requests>GET Requests\:)$")

        # SET Requests:
        p6 = re.compile("^(?P<set_requests>SET Requests\:)$")

        # In Progress Requests:
        p7 = re.compile("^(?P<in_progress_requests>In Progress Requests\:)$")

        # DBAL Response Time:
        p8 = re.compile("^(?P<dbal_response_time>DBAL Response Time\:)$")

        # Record Free Failures:
        p9 = re.compile("^(?P<record_free_failures>Record Free Failures\:)$")

        #  MAX (ms)         : 49
        p10 = re.compile("^\s*MAX +\(ms\) +\:\s*(?P<max>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # BP Crimson Statistics
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("bp_crimson_statistics", {})
                continue

            # Initialized            : Yes
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group["value"].isdigit():
                    group["value"] = int(group["value"])
                root_dict[
                    group["description"]
                    .strip()
                    .lower()
                    .replace(" ", "_")
                    .replace('"', "")
                    .replace("'", "_")
                ] = group["value"]
                continue

            # BP SVL Crimson Statistics
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("bp_svl_crimson_statistics", {})
                continue

            # BP Remote DB Statistics
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("bp_remote_db_statistics", {})
                continue

            # GET Requests:
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault(
                    "bp_remote_db_statistics", {}
                ).setdefault("get_requests", {})
                continue

            # SET Requests:
            m = p6.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault(
                    "bp_remote_db_statistics", {}
                ).setdefault("set_requests", {})
                continue

            # In Progress Requests:
            m = p7.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault(
                    "bp_remote_db_statistics", {}
                ).setdefault("in_progress_requests", {})
                continue

            # DBAL Response Time:
            m = p8.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault(
                    "bp_remote_db_statistics", {}
                ).setdefault("dbal_response_time", {})
                continue

            # Record Free Failures:
            m = p9.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault(
                    "bp_remote_db_statistics", {}
                ).setdefault("record_free_failures", {})
                continue

            #  MAX (ms)         : 49
            m = p10.match(line)
            if m:
                group = m.groupdict()
                root_dict.update({"max": int(group["max"])})
                continue

        return ret_dict


class ShowPlatformSoftwareNodeClusterManagerSwitchB0LocalSchema(MetaParser):
    """
    Schema for show platform software node cluster-manager switch {mode} B0 local
    """

    schema = {
        "local_node_number": int,
        "node_status_is": str,
        "tunnel_status_is": str,
        "node_role_is": str,
        "mac_address_is": str,
        "slot_number_is": int,
        "priority_set_to": int,
        "leader_node_num_is": int,
        "follower_node_is": int,
        "total_node_present_in_cluster": int,
    }


class ShowPlatformSoftwareNodeClusterManagerSwitchB0Local(
    ShowPlatformSoftwareNodeClusterManagerSwitchB0LocalSchema
):
    """Parser for show platform software node cluster-manager switch {mode} B0 local"""

    cli_command = "show platform software node cluster-manager switch {mode} B0 local"

    def cli(self, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}
        # p1 = re.compile('^(?P<node_description>[\w\s]+)\: (?P<status>.*)$')
        # Local Node Number: 1
        p1 = re.compile("^Local +Node +Number\: +(?P<local_node_number>\d+)$")

        # Node status is: NODE_STATUS_UP
        p2 = re.compile("^Node +status +is\: +(?P<node_status_is>.*)$")

        # Tunnel status is: NODE_TUNNEL_UP
        p3 = re.compile("^Tunnel +status +is\: +(?P<tunnel_status_is>.*)$")

        # Node role is: CLUSTER_NODE_ROLE_LEADER
        p4 = re.compile("^Node +role +is\: +(?P<node_role_is>.*)$")

        # MAC address is : 64 181 193 255 238 0
        p5 = re.compile("^MAC +address +is +\: +(?P<mac_address_is>.*)$")

        # Slot number is : 0
        p6 = re.compile("^Slot +number +is +\: +(?P<slot_number_is>\d+)$")

        # priority set to: 1
        p7 = re.compile("^priority +set +to\: +(?P<priority_set_to>\d+)$")

        # Leader node num is: 1
        p8 = re.compile("^Leader +node +num is\: +(?P<leader_node_num_is>\d+)$")

        # Follower node is: 2
        p9 = re.compile("^Follower +node +is\: +(?P<follower_node_is>\d+)$")

        # Total node present in cluster: 2
        p10 = re.compile(
            "^Total +node +present +in +cluster\: +(?P<total_node_present_in_cluster>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Local Node Number: 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["local_node_number"] = int(group["local_node_number"])
                continue

            # Node status is: NODE_STATUS_UP
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["node_status_is"] = group["node_status_is"]
                continue

            # Tunnel status is: NODE_TUNNEL_UP
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tunnel_status_is"] = group["tunnel_status_is"]
                continue

            # Node role is: CLUSTER_NODE_ROLE_LEADER
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["node_role_is"] = group["node_role_is"]
                continue

            # MAC address is : 64 181 193 255 238 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict["mac_address_is"] = group["mac_address_is"]
                continue

            # Slot number is : 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot_number_is"] = int(group["slot_number_is"])
                continue

            # priority set to: 1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict["priority_set_to"] = int(group["priority_set_to"])
                continue

            # Leader node num is: 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict["leader_node_num_is"] = int(group["leader_node_num_is"])
                continue

            # Follower node is: 2
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict["follower_node_is"] = int(group["follower_node_is"])
                continue

            # Total node present in cluster: 2
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict["total_node_present_in_cluster"] = int(
                    group["total_node_present_in_cluster"]
                )
                continue

        return ret_dict


class ShowPlatformSoftwareBpCrimsonStatisticsSchema(MetaParser):
    """
    Schema for show platform software bp crimson statistics
    """

    schema = {
        "bp_crimson_statistics": {
            "initialized": str,
            "config_database_init_d": str,
            "config_db_persist": str,
            "config_db_restorable": str,
            "config_lock_mgr_dbid": int,
            "oper_database_init_d": str,
            "oper_lock_mgr_dbid": int,
            "garbage_collections": int,
        },
        Optional("bp_svl_crimson_statistics"): {
            "config_notify_mgr_id": int,
            "config_dyn_tables_reg_d": int,
            "config_dyn_reg_failures": int,
            "config_dyn_tables_dereg_d": int,
            "config_dereg_deferred": int,
            "config_dereg_failures": int,
            "config_table_updates": int,
            "config_applied": int,
            "config_skipped": int,
            "oper_notify_mgr_dbid": int,
            "oper_dyn_tables_reg_d": int,
            "oper_dyn_reg_failures": int,
            "oper_dyn_tables_dereg_d": int,
            "oper_dereg_s_deferred": int,
            "oper_dereg_failures": int,
            "oper_table_updates": int,
            "dyn_table_failures": int,
            "dyn_table_dereg_failures": int,
            "pending_notifications": int,
            "notifications_highwater": int,
            "notifications_processed": int,
            "notification_failures": int,
        },
        Optional("bp_remote_db_statistics"): {
            "get_requests": {
                "total_requests": int,
                "pending_requests": int,
                "timed_out_requests": int,
                "failed_requests": int,
            },
            "set_requests": {
                "total_requests": int,
                "pending_requests": int,
                "timed_out_requests": int,
                "failed_requests": int,
            },
            "in_progress_requests": {
                "type": str,
                "db_id": int,
                "batch_id": int,
                "op_id": int,
                "task_pid": int,
            },
            Optional("dbal_response_time"): {
                "max": int,
            },
            Optional("record_free_failures"): {
                "total_failures": int,
            },
        },
    }


class ShowPlatformSoftwareBpCrimsonStatistics(
    ShowPlatformSoftwareBpCrimsonStatisticsSchema
):
    """Parser for show platform software bp crimson statistics"""

    cli_command = "show platform software bp crimson statistics"

    def cli(self, output=None):
        # excute command to get output
        output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}

        # BP Crimson Statistics
        p1 = re.compile("^(?P<bp_crimson_statistics>BP Crimson Statistics)$")

        # Regexp  for  all the  lines  which fals in the below  pattern
        # Initialized            : Yes
        p2 = re.compile("^(?P<description>[\w'\s]+)\:\s+(?P<value>\w+)$")

        # BP SVL Crimson Statistics
        p3 = re.compile("^(?P<bp_svl_crimson_statistics>BP SVL Crimson Statistics)$")

        # BP Remote DB Statistics
        p4 = re.compile("^(?P<bp_remote_db_statistics>BP Remote DB Statistics)$")

        # GET Requests:
        p5 = re.compile("^(?P<get_requests>GET Requests\:)$")

        # SET Requests:
        p6 = re.compile("^(?P<set_requests>SET Requests\:)$")

        # In Progress Requests:
        p7 = re.compile("^(?P<in_progress_requests>In Progress Requests\:)$")

        # DBAL Response Time:
        p8 = re.compile("^(?P<dbal_response_time>DBAL Response Time\:)$")

        # Record Free Failures:
        p9 = re.compile("^(?P<record_free_failures>Record Free Failures\:)$")

        #  MAX (ms)         : 49
        p10 = re.compile("^\s*MAX +\(ms\) +\:\s*(?P<max>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # BP Crimson Statistics
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("bp_crimson_statistics", {})
                continue

            # Initialized            : Yes
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group["value"].isdigit():
                    group["value"] = int(group["value"])
                root_dict[
                    group["description"]
                    .strip()
                    .lower()
                    .replace(" ", "_")
                    .replace('"', "")
                    .replace("'", "_")
                ] = group["value"]
                continue

            # BP SVL Crimson Statistics
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("bp_svl_crimson_statistics", {})
                continue

            # BP Remote DB Statistics
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault("bp_remote_db_statistics", {})
                continue

            # GET Requests:
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault(
                    "bp_remote_db_statistics", {}
                ).setdefault("get_requests", {})
                continue

            # SET Requests:
            m = p6.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault(
                    "bp_remote_db_statistics", {}
                ).setdefault("set_requests", {})
                continue

            # In Progress Requests:
            m = p7.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault(
                    "bp_remote_db_statistics", {}
                ).setdefault("in_progress_requests", {})
                continue

            # DBAL Response Time:
            m = p8.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault(
                    "bp_remote_db_statistics", {}
                ).setdefault("dbal_response_time", {})
                continue

            # Record Free Failures:
            m = p9.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault(
                    "bp_remote_db_statistics", {}
                ).setdefault("record_free_failures", {})
                continue

            #  MAX (ms)         : 49
            m = p10.match(line)
            if m:
                group = m.groupdict()
                root_dict.update({"max": int(group["max"])})
                continue

        return ret_dict


class ShowPlatformSoftwareNodeClusterManagerSwitchB0LocalSchema(MetaParser):
    """
    Schema for show platform software node cluster-manager switch {mode} B0 local
    """

    schema = {
        "local_node_number": int,
        "node_status_is": str,
        "tunnel_status_is": str,
        "node_role_is": str,
        "mac_address_is": str,
        "slot_number_is": int,
        "priority_set_to": int,
        "leader_node_num_is": int,
        "follower_node_is": int,
        "total_node_present_in_cluster": int,
    }


class ShowPlatformSoftwareNodeClusterManagerSwitchB0Local(
    ShowPlatformSoftwareNodeClusterManagerSwitchB0LocalSchema
):
    """Parser for show platform software node cluster-manager switch {mode} B0 local"""

    cli_command = "show platform software node cluster-manager switch {mode} B0 local"

    def cli(self, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}
        # p1 = re.compile('^(?P<node_description>[\w\s]+)\: (?P<status>.*)$')
        # Local Node Number: 1
        p1 = re.compile("^Local +Node +Number\: +(?P<local_node_number>\d+)$")

        # Node status is: NODE_STATUS_UP
        p2 = re.compile("^Node +status +is\: +(?P<node_status_is>.*)$")

        # Tunnel status is: NODE_TUNNEL_UP
        p3 = re.compile("^Tunnel +status +is\: +(?P<tunnel_status_is>.*)$")

        # Node role is: CLUSTER_NODE_ROLE_LEADER
        p4 = re.compile("^Node +role +is\: +(?P<node_role_is>.*)$")

        # MAC address is : 64 181 193 255 238 0
        p5 = re.compile("^MAC +address +is +\: +(?P<mac_address_is>.*)$")

        # Slot number is : 0
        p6 = re.compile("^Slot +number +is +\: +(?P<slot_number_is>\d+)$")

        # priority set to: 1
        p7 = re.compile("^priority +set +to\: +(?P<priority_set_to>\d+)$")

        # Leader node num is: 1
        p8 = re.compile("^Leader +node +num is\: +(?P<leader_node_num_is>\d+)$")

        # Follower node is: 2
        p9 = re.compile("^Follower +node +is\: +(?P<follower_node_is>\d+)$")

        # Total node present in cluster: 2
        p10 = re.compile(
            "^Total +node +present +in +cluster\: +(?P<total_node_present_in_cluster>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Local Node Number: 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["local_node_number"] = int(group["local_node_number"])
                continue

            # Node status is: NODE_STATUS_UP
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["node_status_is"] = group["node_status_is"]
                continue

            # Tunnel status is: NODE_TUNNEL_UP
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tunnel_status_is"] = group["tunnel_status_is"]
                continue

            # Node role is: CLUSTER_NODE_ROLE_LEADER
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["node_role_is"] = group["node_role_is"]
                continue

            # MAC address is : 64 181 193 255 238 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict["mac_address_is"] = group["mac_address_is"]
                continue

            # Slot number is : 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict["slot_number_is"] = int(group["slot_number_is"])
                continue

            # priority set to: 1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict["priority_set_to"] = int(group["priority_set_to"])
                continue

            # Leader node num is: 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict["leader_node_num_is"] = int(group["leader_node_num_is"])
                continue

            # Follower node is: 2
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict["follower_node_is"] = int(group["follower_node_is"])
                continue

            # Total node present in cluster: 2
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict["total_node_present_in_cluster"] = int(
                    group["total_node_present_in_cluster"]
                )
                continue

        return ret_dict


class ShowPlatformSoftwareAuditSummarySchema(MetaParser):
    """Schema for show platform software audit summary"""

    schema = {
        "chassis": {Any(): {Optional("route_process"): int, "avc_denial_count": int}}
    }


class ShowPlatformSoftwareAuditSummary(ShowPlatformSoftwareAuditSummarySchema):
    """Parser for show platform software audit summary"""

    cli_command = "show platform software audit summary"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # AUDIT LOG ON chassis 1 route-processor 0
        p1 = re.compile(
            r"^AUDIT LOG ON chassis (?P<chassis>\d+) route-processor (?P<route_process>\d+)$"
        )

        # AUDIT LOG ON ACTIVE
        p2 = re.compile(r"^AUDIT LOG ON (?P<chassis>\w+)$")

        # AVC Denial count: 82
        p3 = re.compile(r"^AVC Denial count: (?P<avc_denial_count>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # AUDIT LOG ON chassis 1 route-processor 0
            m = p1.match(line)
            if m:
                chassis_dict = ret_dict.setdefault("chassis", {}).setdefault(
                    m.groupdict()["chassis"], {}
                )
                chassis_dict["route_process"] = int(m.groupdict()["route_process"])
                continue

            # AUDIT LOG ON ACTIVE
            m = p2.match(line)
            if m:
                chassis_dict = ret_dict.setdefault("chassis", {}).setdefault(
                    m.groupdict()["chassis"].lower(), {}
                )
                continue

            # AVC Denial count: 82
            m = p3.match(line)
            if m:
                chassis_dict["avc_denial_count"] = int(
                    m.groupdict()["avc_denial_count"]
                )
                continue
        return ret_dict


# ==========================================================================================
# Parser Schema for 'show platform software ilpower port " +intf_detail["uut1_int9"]'
# ==========================================================================================
class ShowPlatformSoftwareIlppowerPortSchema(MetaParser):
    """
    Schema for
        * 'show platform software ilpower port {interface}'
    """

    schema = {
        "interface": {
            Any(): {
                "initialization_done": str,
                "ilp_supported": str,
                "ilp_enabled": str,
                "post": str,
                "detect_on": str,
                "pd_detected": str,
                "pd_class_done": str,
                "cisco_pd": str,
                "power_is_on": str,
                "power_denied": str,
                "pd_type": str,
                "pd_class": str,
                "power_state": str,
                "current_state": str,
                "previous_state": str,
                "requested_power": int,
                "short": int,
                "short_cnt": int,
                "cisco_pd_detect_count": int,
                "spare_pair_mode": int,
                "spare_pair_arch": int,
                "signal_pair_pwr_alloc": int,
                "spare_pair_power_on": int,
                "pd_power_state": int,
                "timer": {
                    "bad_power": str,
                    "power_good": str,
                    "power_denied": str,
                    "cisco_pd_detect": str,
                    "ieee_detect": str,
                    "ieee_short": str,
                    "link_down": str,
                    "vsense": str,
                },
            },
        },
    }


# ==========================================================================================
# Parser for 'show platform software ilpower port " +intf_detail["uut1_int9"]'
# ==========================================================================================


class ShowPlatformSoftwareIlppowerPort(ShowPlatformSoftwareIlppowerPortSchema):
    """
    Parser for
        * 'show platform software ilpower port " +intf_detail["uut1_int9"]'
    """

    cli_command = "show platform software ilpower port {interface}"

    def cli(self, interface="", output=None):
        cmd = self.cli_command.format(interface=interface)

        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        ret_dict = {}

        # ILP Port Configuration for interface Gi1/0/14
        p1 = re.compile(
            r"^ILP +Port +Configuration +for +interface+\s(?P<interface>[\w\/]+)$"
        )

        # Initialization Done:   Yes
        p2 = re.compile(r"^Initialization Done:\s+(?P<initialization_done>[\w]+)$")

        # ILP Supported:         Yes
        p3 = re.compile(r"^ILP Supported:\s+(?P<ilp_supported>[\w]+)$")

        # ILP Enabled:           Yes
        p4 = re.compile(r"^ILP Enabled:\s+(?P<ilp_enabled>[\w]+)$")

        # POST:                  Yes
        p5 = re.compile(r"^POST:\s+(?P<post>[\w]+)$")

        # Detect On:             No
        p6 = re.compile(r"^Detect On:\s+(?P<detect_on>[\w]+)$")

        # PD Detected            Yes
        p7 = re.compile(r"^PD Detected\s+(?P<pd_detected>[\w]+)$")

        # PD Class Done          No
        p8 = re.compile(r"^PD Class Done\s+(?P<pd_class_done>[\w]+)$")

        # Cisco PD:              No
        p9 = re.compile(r"^Cisco PD:\s+(?P<cisco_pd>[\w]+)$")

        # Power is On:           Yes
        p10 = re.compile(r"^Power is On:\s+(?P<power_is_on>[\w]+)$")

        # Power Denied:          No
        p11 = re.compile(r"^Power Denied:\s+(?P<power_denied>([Yy]es|[Nn]o)+)$")

        # PD Type:               IEEE
        p12 = re.compile(r"^PD Type:\s+(?P<pd_type>[\w]+)$")

        # PD Class:              IEEE3
        p13 = re.compile(r"^PD Class:\s+(?P<pd_class>[\w]+)$")

        # Power State:           OK
        p14 = re.compile(r"^Power State:\s+(?P<power_state>[\w]+)$")

        # Current State:         NGWC_ILP_LINK_UP_S
        p15 = re.compile(r"^Current State:\s+(?P<current_state>[\w\_]+)$")

        # Previous State:        NGWC_ILP_LINK_UP_S
        p16 = re.compile(r"^Previous State:\s+(?P<previous_state>[\w\_]+)$")

        # Requested Power:       10250
        p17 = re.compile(r"^Requested Power:\s+(?P<requested_power>[\d]+)$")

        # Short:                 0
        p18 = re.compile(r"^Short:\s+(?P<short>[\d]+)$")

        # Short Cnt:             0
        p19 = re.compile(r"^Short Cnt:\s+(?P<short_cnt>[\d]+)$")

        # Cisco PD Detect Count: 0
        p20 = re.compile(r"^Cisco PD Detect Count:\s+(?P<cisco_pd_detect_count>[\d]+)$")

        # Spare Pair mode:       0
        p21 = re.compile(r"^Spare Pair mode:\s+(?P<spare_pair_mode>[\d]+)$")

        # Spare Pair Arch:       1
        p22 = re.compile(r"^Spare Pair Arch:\s+(?P<spare_pair_arch>[\d]+)$")

        # Signal Pair Pwr alloc: 0
        p23 = re.compile(r"^Signal Pair Pwr alloc:\s+(?P<signal_pair_pwr_alloc>[\d]+)$")

        # Spare Pair Power On:   0
        p24 = re.compile(r"^Spare Pair Power On:\s+(?P<spare_pair_power_on>[\d]+)$")

        # PD power state:        0
        p25 = re.compile(r"^PD power state:\s+(?P<pd_power_state>[\d]+)$")

        # Timer:
        p26 = re.compile(r"^Timer:$")

        # Bad Power:        Stopped
        p27 = re.compile(r"^Bad Power:\s+(?P<bad_power>[\w]+)$")

        # Power Good:        Stopped
        p28 = re.compile(r"^Power Good:\s+(?P<power_good>[\w]+)$")

        # Power Denied:      Stopped
        p29 = re.compile(r"^Power Denied:\s+(?P<power_denied>([Ss]topped|[Ss]tarted)+)")

        # Cisco PD Detect:   Stopped
        p30 = re.compile(r"^Cisco PD Detect:\s+(?P<cisco_pd_detect>[\w]+)$")

        # IEEE Detect:       Stopped
        p31 = re.compile(r"^IEEE Detect:\s+(?P<ieee_detect>[\w]+)$")

        # IEEE Short:        Stopped
        p32 = re.compile(r"^IEEE Short:\s+(?P<ieee_short>[\w]+)$")

        # Link Down:         Stopped
        p33 = re.compile(r"^Link Down:\s+(?P<link_down>[\w]+)$")

        # Vsense:            Stopped
        p34 = re.compile(r"^Vsense:\s+(?P<vsense>[\w]+)$")

        for line in output.splitlines():
            line = line.strip()

            # ILP Port Configuration for interface Gi1/0/14
            m = p1.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict.setdefault("interface", {}).setdefault(
                    Common.convert_intf_name(group["interface"]), {}
                )
                continue

            # Initialization Done:   Yes
            m = p2.match(line)
            if m:
                group = m.groupdict()
                int_dict["initialization_done"] = group["initialization_done"]
                continue

            # ILP Supported:         Yes
            m = p3.match(line)
            if m:
                group = m.groupdict()
                int_dict["ilp_supported"] = group["ilp_supported"]
                continue

            # ILP Enabled:           Yes
            m = p4.match(line)
            if m:
                group = m.groupdict()
                int_dict["ilp_enabled"] = group["ilp_enabled"]
                continue

            # POST:                  Yes
            m = p5.match(line)
            if m:
                group = m.groupdict()
                int_dict["post"] = group["post"]
                continue

            # Detect On:             No
            m = p6.match(line)
            if m:
                group = m.groupdict()
                int_dict["detect_on"] = group["detect_on"]
                continue

            # PD Detected            Yes
            m = p7.match(line)
            if m:
                group = m.groupdict()
                int_dict["pd_detected"] = group["pd_detected"]
                continue

            # PD Class Done          No
            m = p8.match(line)
            if m:
                group = m.groupdict()
                int_dict["pd_class_done"] = group["pd_class_done"]
                continue

            # Cisco PD:              No
            m = p9.match(line)
            if m:
                group = m.groupdict()
                int_dict["cisco_pd"] = group["cisco_pd"]
                continue

            # Power is On:           Yes
            m = p10.match(line)
            if m:
                group = m.groupdict()
                int_dict["power_is_on"] = group["power_is_on"]
                continue

            # Power Denied:          No
            m = p11.match(line)
            if m:
                group = m.groupdict()
                int_dict["power_denied"] = group["power_denied"]
                continue

            # PD Type:               IEEE
            m = p12.match(line)
            if m:
                group = m.groupdict()
                int_dict["pd_type"] = group["pd_type"]
                continue

            # PD Class:              IEEE3
            m = p13.match(line)
            if m:
                group = m.groupdict()
                int_dict["pd_class"] = group["pd_class"]
                continue

            # Power State:           OK
            m = p14.match(line)
            if m:
                group = m.groupdict()
                int_dict["power_state"] = group["power_state"]
                continue

            # Current State:         NGWC_ILP_LINK_UP_S
            m = p15.match(line)
            if m:
                group = m.groupdict()
                int_dict["current_state"] = group["current_state"]
                continue

            # Previous State:        NGWC_ILP_LINK_UP_S
            m = p16.match(line)
            if m:
                group = m.groupdict()
                int_dict["previous_state"] = group["previous_state"]
                continue

            # Requested Power:       10250
            m = p17.match(line)
            if m:
                group = m.groupdict()
                int_dict["requested_power"] = int(group["requested_power"])
                continue

            # Short:                 0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                int_dict["short"] = int(group["short"])
                continue

            # Short Cnt:             0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                int_dict["short_cnt"] = int(group["short_cnt"])
                continue

            # Cisco PD Detect Count: 0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                int_dict["cisco_pd_detect_count"] = int(group["cisco_pd_detect_count"])
                continue

            # Spare Pair mode:       0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                int_dict["spare_pair_mode"] = int(group["spare_pair_mode"])
                continue

            # Spare Pair Arch:       1
            m = p22.match(line)
            if m:
                group = m.groupdict()
                int_dict["spare_pair_arch"] = int(group["spare_pair_arch"])
                continue

            # Signal Pair Pwr alloc: 0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                int_dict["signal_pair_pwr_alloc"] = int(group["signal_pair_pwr_alloc"])
                continue

            # Spare Pair Power On:   0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                int_dict["spare_pair_power_on"] = int(group["spare_pair_power_on"])
                continue

            # PD power state:        0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                int_dict["pd_power_state"] = int(group["pd_power_state"])
                continue

            # Timer:
            m = p26.match(line)
            if m:
                time_dict = {}
                int_dict["timer"] = time_dict
                continue

            # Bad Power:        Stopped
            m = p27.match(line)
            if m:
                group = m.groupdict()
                time_dict["bad_power"] = group["bad_power"]
                continue

            # Power Good:        Stopped
            m = p28.match(line)
            if m:
                group = m.groupdict()
                time_dict["power_good"] = group["power_good"]
                continue

            # Power Denied:      Stopped
            m = p29.match(line)
            if m:
                group = m.groupdict()
                time_dict["power_denied"] = group["power_denied"]
                continue

            # Cisco PD Detect:   Stopped
            m = p30.match(line)
            if m:
                group = m.groupdict()
                time_dict["cisco_pd_detect"] = group["cisco_pd_detect"]
                continue

            # IEEE Detect:       Stopped
            m = p31.match(line)
            if m:
                group = m.groupdict()
                time_dict["ieee_detect"] = group["ieee_detect"]
                continue

            # IEEE Short:        Stopped
            m = p32.match(line)
            if m:
                group = m.groupdict()
                time_dict["ieee_short"] = group["ieee_short"]
                continue

            # Link Down:         Stopped
            m = p33.match(line)
            if m:
                group = m.groupdict()
                time_dict["link_down"] = group["link_down"]
                continue

            # Vsense:            Stopped
            m = p34.match(line)
            if m:
                group = m.groupdict()
                time_dict["vsense"] = group["vsense"]
                continue

        return ret_dict


# ==================================================================
# Parser for 'show platform software wired-client {process} active'
# ==================================================================


class ShowPlatformSoftwareWiredClientFpActiveSchema(MetaParser):
    """Schema for show platform software wired-client {process} active"""

    schema = {
        "fp_active": {
            Any(): {
                "mac_address": str,
                "fwd": str,
                "open_access": str,
                "status": str,
            },
        },
    }


class ShowPlatformSoftwareWiredClientFpActive(
    ShowPlatformSoftwareWiredClientFpActiveSchema
):
    """Parser for show platform software wired-client {process} active"""

    cli_command = "show platform software wired-client {process} active"

    def cli(self, process, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(process=process))

        #      ID         MAC Address    Fwd Open Access Status
        # ------------------------------------------------------------------
        #      0x105e6628 14a2.a0d4.0200 Yes Yes         Done
        #      0x10ab50b0 e8d3.225d.c380 Yes Yes         Done
        #      0x10e2badd 44b6.beb4.21d0 Yes Yes         Done
        #      0x1348fba0 44b6.bec6.fb00 Yes Yes         Done
        #      0x14597f9b 00a3.d144.49f6 Yes Yes         Done
        #      0x145aa536 000c.29e0.3ea6 Yes Yes         Done
        #      0x14a5b221 0cd0.f8e7.9b00 Yes Yes         Done
        p1 = re.compile(
            r"^(?P<id>\S+)\s+(?P<mac_address>\S+)\s+(?P<fwd>\w+)\s+(?P<open_access>\w+)\s+(?P<status>\w+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            #      ID         MAC Address    Fwd Open Access Status
            # ------------------------------------------------------------------
            #      0x105e6628 14a2.a0d4.0200 Yes Yes         Done
            #      0x10ab50b0 e8d3.225d.c380 Yes Yes         Done
            #      0x10e2badd 44b6.beb4.21d0 Yes Yes         Done
            #      0x1348fba0 44b6.bec6.fb00 Yes Yes         Done
            #      0x14597f9b 00a3.d144.49f6 Yes Yes         Done
            #      0x145aa536 000c.29e0.3ea6 Yes Yes         Done
            #      0x14a5b221 0cd0.f8e7.9b00 Yes Yes         Done
            m = p1.match(line)
            if m:
                group = m.groupdict()
                id_var = group["id"]
                id_dict = ret_dict.setdefault("fp_active", {}).setdefault(id_var, {})
                id_dict["mac_address"] = group["mac_address"]
                id_dict["fwd"] = group["fwd"]
                id_dict["open_access"] = group["open_access"]
                id_dict["status"] = group["status"]
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform software access-list switch active F0 summary '
# ======================================================


class ShowPlatformSoftwareAccessListSwitchActiveF0SummarySchema(MetaParser):
    """Schema for show platform software access-list switch active F0 summary"""

    schema = {
        "summary": {
            Any(): {
                "access_list": str,
                "num_ref": str,
                "dwnld_aces": str,
            }
        }
    }


class ShowPlatformSoftwareAccessListSwitchActiveF0Summary(
    ShowPlatformSoftwareAccessListSwitchActiveF0SummarySchema
):
    """Parser for show platform software access-list switch active F0 summary"""

    cli_command = "show platform software access-list switch active F0 summary"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Access-list                          Index        Num Ref      Dwnld ACEs
        # --------------------------------------------------------------------------
        # IP-Adm-V4-Int-ACL-global             2            0            2
        # IP-Adm-V6-Int-ACL-global             3            0            2
        # preauth_v4                           4            0            6
        # preauth_v6                           5            0            10
        # implicit_deny                        6            0            1
        # implicit_permit                      7            0            1
        # implicit_deny_v6                     8            0            1
        # implicit_permit_v6                   9            0            1
        # CISCO-CWA-URL-REDIRECT-ACL           10           0            6
        # v6-ogacl-1                           13           1            1

        p1 = re.compile(
            r"^(?P<Access_list>\S+)\s+(?P<Index>\d+)\s+(?P<Num_Ref>\d+)\s+(?P<Dwnld_ACEs>\d+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Access-list                          Index        Num Ref      Dwnld ACEs
            # --------------------------------------------------------------------------
            # IP-Adm-V4-Int-ACL-global             2            0            2
            # IP-Adm-V6-Int-ACL-global             3            0            2
            # preauth_v4                           4            0            6
            # preauth_v6                           5            0            10
            # implicit_deny                        6            0            1
            # implicit_permit                      7            0            1
            # implicit_deny_v6                     8            0            1
            # implicit_permit_v6                   9            0            1
            # CISCO-CWA-URL-REDIRECT-ACL           10           0            6
            # v6-ogacl-1                           13           1            1

            m = p1.match(line)
            if m:
                group = m.groupdict()
                index = int(group["Index"])
                int_dict = ret_dict.setdefault("summary", {}).setdefault(index, {})
                int_dict["access_list"] = group["Access_list"]
                int_dict["num_ref"] = group["Num_Ref"]
                int_dict["dwnld_aces"] = group["Dwnld_ACEs"]
                continue

        return ret_dict


class ShowPlatformSoftwareDistributedIpsecTunnelInfoSchema(MetaParser):
    """Schema for show platform software distributed-ipsec tunnel-info"""

    schema = {
        "asic_count": int,
        int: {
            "switch_number": int,
            "asic_value": int,
            "num_of_tunnel": int,
            "platform": str,
        },
        Optional("svti_tunnel"): {
            Any(): {
                "if_id": str,
                "sbad_info": int,
                "switch_number": int,
                "asic_id": int,
            }
        },
    }


class ShowPlatformSoftwareDistributedIpsecTunnelInfo(
    ShowPlatformSoftwareDistributedIpsecTunnelInfoSchema
):
    """Parser for show platform software distributed-ipsec tunnel-info"""

    cli_command = "show platform software distributed-ipsec tunnel-info"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        list_key_num = 1
        # IPSEC Total ASIC Count = 2
        p1 = re.compile(r"IPSEC\s+Total\s+ASIC\s+Count\s+=\s+(?P<asic_count>-?\d+)\s+$")
        #   SW_NUM   ASIC   # of TUNNELS     PLATFORM
        #  |  2   |   0    |       2     |    C9300X   |
        p2 = re.compile(
            r"\s+\|\s+(?P<switch_number>-?\d+)\s+\|\s+(?P<asic_value>-?\d+)\s+\|\s+(?P<num_of_tunnel>-?\d+)\s+\|\s+(?P<platform>\S+)\s+\|$"
        )

        # |       INTERFACE |      IF_ID | SADB_ID | SW_NUM | ASIC |
        # |       Tunnel201 | 0x00000216 |       1 |      1 |    0 |
        p3 = re.compile(
            r"^\s+\|\s+(?P<tunnel_int>Tunnel\d+)\s+\|\s+(?P<if_id>\w+)\s+\|\s+(?P<sbad_info>\d+)\s+\|\s+(?P<switch_number>\d+)\s+\|\s+(?P<asic_id>\d+)\s+\|"
        )

        for line in output.splitlines():
            m = p1.match(line)
            # IPSEC Total ASIC Count = 2
            if m:
                match_dict = m.groupdict()
                ret_dict["asic_count"] = int(match_dict["asic_count"])
                continue

            m = p2.match(line)
            #  SW_NUM   ASIC   # of TUNNELS     PLATFORM
            #  |  2   |   0    |       2     |    C9300X   |
            if m:
                match_dict = m.groupdict()
                list_index_dict = ret_dict.setdefault(list_key_num, {})
                list_index_dict["switch_number"] = int(match_dict["switch_number"])
                list_index_dict["asic_value"] = int(match_dict["asic_value"])
                list_index_dict["num_of_tunnel"] = int(match_dict["num_of_tunnel"])
                list_index_dict["platform"] = match_dict["platform"]
                list_key_num += 1
                continue

            # |       INTERFACE |      IF_ID | SADB_ID | SW_NUM | ASIC |
            # |       Tunnel201 | 0x00000216 |       1 |      1 |    0 |

            m = p3.match(line)
            if m:
                match_dict = m.groupdict()
                list_index_dict = ret_dict.setdefault("svti_tunnel", {}).setdefault(
                    match_dict["tunnel_int"], {}
                )
                list_index_dict["asic_id"] = int(match_dict["asic_id"])
                list_index_dict["switch_number"] = int(match_dict["switch_number"])
                list_index_dict["if_id"] = match_dict["if_id"]
                list_index_dict["sbad_info"] = int(match_dict["sbad_info"])

        return ret_dict


# ======================================================
# Parser for 'show platform software access-list {switch} {mode} FP {switch_var} og-lkup-ids'
# ======================================================


class ShowPlatformSoftwareAccessListSwitchActiveFPActiveOgLkupIdsSchema(MetaParser):
    """Schema for show platform software access-list {switch} {mode} FP {switch_var} og-lkup-ids"""

    schema = {
        "summary": {Any(): {"access_list": str, "src_lkup_id": str, "dst_lkup_id": str}}
    }


class ShowPlatformSoftwareAccessListSwitchActiveFPActiveOgLkupIds(
    ShowPlatformSoftwareAccessListSwitchActiveFPActiveOgLkupIdsSchema
):
    """Parser for show platform software access-list {switch} {mode} FP {switch_var} og-lkup-ids"""

    cli_command = [
        "show platform software access-list {switch} {mode} FP {switch_var} og-lkup-ids"
    ]

    def cli(self, switch=None, mode=None, switch_var=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # IP-Adm-V4-Int-ACL-global             4            0x0          0x0
        p1 = re.compile(
            r"^(?P<access_list>\S+)\s+(?P<index>\d+)\s+(?P<src_lkup_id>\w+)\s+(?P<dst_lkup_id>\w+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # IP-Adm-V4-Int-ACL-global             4            0x0          0x0

            m = p1.match(line)
            if m:
                group = m.groupdict()
                index = int(group["index"])
                int_dict = ret_dict.setdefault("summary", {}).setdefault(index, {})
                int_dict["access_list"] = group["access_list"]
                int_dict["src_lkup_id"] = group["src_lkup_id"]
                int_dict["dst_lkup_id"] = group["dst_lkup_id"]
                continue

        return ret_dict


class ShowPlatformSoftwareSteeringPolicyPolicyAomInfoSchema(MetaParser):

    """Schema for "show platform software steering-policy forwarding-manager switch {switch} F0 policy-aom-info" """

    schema = {
        "policy_index": {
            Any(): {
                "policy": str,
                "aom_id": int,
                "num_ref": int,
                "ref_aom_id": int,
            },
        }
    }


class ShowPlatformSoftwareSteeringPolicyAomInfo(
    ShowPlatformSoftwareSteeringPolicyPolicyAomInfoSchema
):
    """Schema for show platform software steering-policy forwarding-manager switch {switch} F0 policy-aom-info"""

    cli_command = [
        "show platform software steering-policy forwarding-manager switch {switch} F0 policy-aom-info",
        "show platform software steering-policy forwarding-manager F0 policy-summary",
    ]

    def cli(self, switch=None, output=None):
        if output is None:
            if not switch:
                cmd = self.cli_command[1]
            else:
                cmd = self.cli_command[0].format(switch=switch)
            output = self.device.execute(cmd)

        # Policy                            Index         aom-id      Num Ref  Ref aom-id
        # -------------------------------------------------------------------------------
        # contract_4_28eadb333777_v0        2090904497    1895        1        1900
        # contract_4(Mirror)_b4675385cca2_  2090904057    1903        1        1907
        p1 = re.compile(
            r"^(?P<Policy>\S+)\s+(?P<Index>\d+)\s+(?P<Aom_id>\d+)\s+(?P<Num_ref>\d+)\s+(?P<Ref_aom_id>\d+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Policy                            Index         aom-id      Num Ref  Ref aom-id
            # -------------------------------------------------------------------------------
            # contract_4_28eadb333777_v0        2090904497    1895        1        1900
            # contract_4(Mirror)_b4675385cca2_  2090904057    1903        1        1907

            m = p1.match(line)
            if m:
                group = m.groupdict()
                index = group["Index"]
                int_dict = ret_dict.setdefault("policy_index", {}).setdefault(index, {})
                int_dict["policy"] = group["Policy"]
                int_dict["aom_id"] = int(group["Aom_id"])
                int_dict["num_ref"] = int(group["Num_ref"])
                int_dict["ref_aom_id"] = int(group["Ref_aom_id"])
                continue

        return ret_dict


class ShowPlatformSoftwareObjectManagerF0ObjectSchema(MetaParser):
    """Schema for show platform software object-manager switch {switch} F0 object {object}"""

    schema = {
        "obj_identifier": {
            "description": {"contract": str, "idx": int},
            "obj_identifier": int,
            "obj_status": {"client_data": str, "epoch": int, "status": str},
            "obj_type_id": int,
            Optional("post_lock_count"): int,
            Optional("pre_lock_count"): int,
        }
    }


class ShowPlatformSoftwareObjectManagerF0Object(
    ShowPlatformSoftwareObjectManagerF0ObjectSchema
):
    """Parser for show platform software object-manager switch {switch} F0 object {object}"""

    cli_command = [
        "show platform software object-manager switch {switch} F0 object {object}"
    ]

    def cli(self, object, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, object=object)

            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}
        obj_dict = {}
        sts_dict = {}

        # Object identifier: 1895
        p1 = re.compile(r"Object identifier\: (?P<obj_identifier>(\d+))")

        # Description: PLC: contract_4_28eadb333777_v0 idx: 2090904497
        p2 = re.compile(
            r"Description\:\s+PLC\: (?P<contract>\S+)\s+idx\: (?P<idx>(\d+))"
        )

        # Obj type id: 765
        p3 = re.compile(r"[Oo]bj type id\: (?P<obj_type_id>(\d+))")

        # Obj type: Hawkeye policy-defn
        p4 = re.compile(r"[Oobj] type\: (?P<obj_type>\W+)")

        # Status: Pending-issue, Epoch: 0, Client data: 0x4f0875b8
        p5 = re.compile(
            r"Status\: (?P<status>\S+)\, Epoch\: (?P<epoch>(\d+))\, Client data\: (?P<client_data>\S+)"
        )

        # Pre-lock count: 1
        p6 = re.compile(r"Pre-lock count\: (?P<pre_lock_count>(\d+))")

        # Post-lock count: 2
        p7 = re.compile(r"Post-lock count\: (?P<post_lock_count>(\d+))")

        for line in output.splitlines():
            line = line.strip()

            # Object identifier: 1895
            m = p1.match(line)
            if m:
                group = m.groupdict()
                obj_identifier = group["obj_identifier"]
                obj_dict = ret_dict.setdefault("obj_identifier", {})
                obj_dict["obj_identifier"] = int(group["obj_identifier"])
                continue

            # Description: PLC: contract_4_28eadb333777_v0 idx: 2090904497
            m = p2.match(line)
            if m:
                group = m.groupdict()
                contract = group["contract"]
                idx = group["idx"]
                des_dict = obj_dict.setdefault("description", {})
                des_dict["contract"] = group["contract"]
                des_dict["idx"] = int(group["idx"])
                continue

            # Obj type id: 765
            m = p3.match(line)
            if m:
                group = m.groupdict()
                obj_type_id = group["obj_type_id"]
                obj_dict["obj_type_id"] = int(group["obj_type_id"])
                continue

            # Obj type: Hawkeye policy-defn
            m = p4.match(line)
            if m:
                group = m.groupdict()
                obj_type = group["obj_type"]
                obj_dict["obj_type"] = group["obj_type"]
                continue

            # Status: Pending-issue, Epoch: 0, Client data: 0x4f0875b8
            m = p5.match(line)
            if m:
                group = m.groupdict()
                status = group["status"]
                epoch = group["epoch"]
                client_data = group["client_data"]
                sts_dict = obj_dict.setdefault("obj_status", {})
                sts_dict["status"] = group["status"]
                sts_dict["epoch"] = int(group["epoch"])
                sts_dict["client_data"] = group["client_data"]
                continue

            # Pre-lock count: 1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                pre_lock_count = group["pre_lock_count"]
                obj_dict["pre_lock_count"] = int(group["pre_lock_count"])
                continue

            # Post-lock count: 2
            m = p7.match(line)
            if m:
                group = m.groupdict()
                post_lock_count = group["post_lock_count"]
                obj_dict["post_lock_count"] = int(group["post_lock_count"])
                continue
        return ret_dict


# ============================================================================
#  Schema for
#  * 'show platform software iomd {lc no} macsec interface {port no} detail'
# ============================================================================


class ShowPlatformSoftwareIomdMacsecInterfacePortDetailSchema(MetaParser):
    schema = {
        "tx": {
            "tx_port": int,
            "tx_sub_port": int,
            "tx_index": int,
            "tx_prev_an": int,
            "tx_cur_an": int,
            "tx_encrypt": int,
            "tx_vlan": int,
            "tx_end_station": int,
            "tx_scb": int,
            "tx_next_pn": int,
            "tx_key_len": int,
            "tx_hashkey_len": int,
            "tx_bypass": int,
            "tx_conf_offset": int,
            "tx_cipher": str,
        },
        "common": {
            "delay_protection": int,
            "install_rx_cnt": int,
            "install_tx_cnt": int,
            "del_rx_cnt": int,
            "instal_rx_fail_cnt": int,
            "install_tx_fail_cnt": int,
            "del_rx_fail_cnt": int,
            "rx_an_cnt": int,
            "common_port": int,
            "common_sub_port": int,
            "common_index": str,
        },
        "rx": {
            "rx_port": int,
            "rx_sub_port": int,
            "rx_index": int,
            "rx_prev_an": int,
            "rx_cur_an": int,
            "rx_replay_protect": int,
            "replay_window_size": int,
            "decrypt_frames": int,
            "validate_frames": int,
            "rx_next_pn": int,
            "rx_key_len": int,
            "rx_hashkey_len": int,
            "rx_bypass": int,
            "rx_conf_offset": int,
            "rx_cipher": str,
        },
        "device": {"id": list},
    }


class ShowPlatformSoftwareIomdMacsecInterfacePortDetail(
    ShowPlatformSoftwareIomdMacsecInterfacePortDetailSchema
):

    """
    Parser for
    * 'show platform software iomd {lc no} macsec interface {port no} detail'
    """

    cli_command = (
        "show platform software iomd {lc_no} macsec interface {port_no} detail"
    )

    def cli(self, lc_no, port_no, output=None):
        if output is None:
            cmd = self.cli_command.format(lc_no=lc_no, port_no=port_no)
            output = self.device.execute(cmd)

        ret_dict = {}
        tx_match = rx_match = False

        # Port:10, Subport:0, Tx SC index:0
        p1 = re.compile(
            r"Port:(?P<tx_port>-?\d+),\s+Subport:(?P<tx_sub_port>-?\d+),\s+Tx\s+SC\s+index:(?P<tx_index>-?\d+)$"
        )

        # Prev AN: 1, Cur AN: 2
        p1_1 = re.compile(
            r"Prev\s+AN:\s+(?P<tx_prev_an>-?\d+),\s+Cur\s+AN:\s+(?P<tx_cur_an>-?\d+)$"
        )

        # encrypt: 1
        p1_2 = re.compile(r"encrypt:\s+(?P<tx_encrypt>-?\d+)$")

        # vlan: 1
        p1_3 = re.compile(r"vlan:\s+(?P<tx_vlan>-?\d+)$")

        # end_station: 0
        p1_4 = re.compile(r"end_station:\s+(?P<tx_end_station>-?\d+)$")

        # scb: 0
        p1_5 = re.compile(r"scb:\s+(?P<tx_scb>-?\d+)$")

        # nextPn: 1
        p1_6 = re.compile(r"nextPn:\s+(?P<tx_next_pn>-?\d+)$")

        # key_len: 32
        p1_7 = re.compile(r"key_len:\s+(?P<tx_key_len>-?\d+)$")

        # hashkey_len: 16
        p1_8 = re.compile(r"hashkey_len:\s+(?P<tx_hashkey_len>-?\d+)$")

        # bypass: 0
        p1_9 = re.compile(r"bypass:\s+(?P<tx_bypass>-?\d+)$")

        # conf_offset: 0
        p1_10 = re.compile(r"conf_offset:\s+(?P<tx_conf_offset>-?\d+)$")

        # cipher: GCM_AES_256
        p1_11 = re.compile(r"cipher:\s+(?P<tx_cipher>\S+)$")

        # Macsec hash data: Port: 10, Subport: 0, sa_index: -2130706432
        p2 = re.compile(
            r"Macsec\s+hash\s+data:\s+Port:\s+(?P<common_port>-?\d+),\s+Subport:\s+(?P<common_sub_port>-?\d+),\s+sa_index:\s+(?P<common_index>\S+)$"
        )

        # Install Rx Count 715
        p2_1 = re.compile(r"Install\s+Rx\s+Count\s+(?P<install_rx_cnt>-?\d+)$")

        # Install Tx Count 715
        p2_2 = re.compile(r"Install\s+Tx\s+Count\s+(?P<install_tx_cnt>-?\d+)$")

        # Delete Rx Count 711
        p2_3 = re.compile(r"Delete\s+Rx\s+Count\s+(?P<del_rx_cnt>-?\d+)$")

        # Install Rx Fail Count 3
        p2_4 = re.compile(
            r"Install\s+Rx\s+Fail\s+Count\s+(?P<instal_rx_fail_cnt>-?\d+)$"
        )

        # Install Tx Fail Count 0
        p2_5 = re.compile(
            r"Install\s+Tx\s+Fail\s+Count\s+(?P<install_tx_fail_cnt>-?\d+)$"
        )

        # Delete Rx Fail Count 0
        p2_6 = re.compile(r"Delete\s+Rx\s+Fail\s+Count\s+(?P<del_rx_fail_cnt>-?\d+)$")

        # Rx SA Same AN Count 3
        p2_7 = re.compile(r"Rx\s+SA\s+Same\s+AN\s+Count\s+(?P<rx_an_cnt>-?\d+)$")

        # Delay protection: 0
        p2_8 = re.compile(r"Delay\s+protection:\s+(?P<delay_protection>-?\d+)$")

        # Port:10, Subport:0, Rx SC index:0
        p3 = re.compile(
            r"Port:(?P<rx_port>-?\d+),\s+Subport:(?P<rx_sub_port>-?\d+),\s+Rx\s+SC\s+index:(?P<rx_index>-?\d+)$"
        )

        # Prev AN: 1, Cur AN: 2
        p3_1 = re.compile(
            r"Prev\s+AN:\s+(?P<rx_prev_an>-?\d+),\s+Cur\s+AN:\s+(?P<rx_cur_an>-?\d+)$"
        )

        # replay_protect: 1
        p3_2 = re.compile(r"replay_protect:\s+(?P<rx_replay_protect>-?\d+)$")

        # replay_window_size: 0
        p3_3 = re.compile(r"replay_window_size:\s+(?P<replay_window_size>-?\d+)$")

        # decrypt_frames: 1
        p3_4 = re.compile(r"decrypt_frames:\s+(?P<decrypt_frames>-?\d+)$")

        # validate_frames: 1
        p3_5 = re.compile(r"validate_frames:\s+(?P<validate_frames>-?\d+)$")

        # nextPn: 0
        p3_6 = re.compile(r"nextPn:\s+(?P<rx_next_pn>-?\d+)$")

        # key_len: 32
        p3_7 = re.compile(r"key_len:\s+(?P<rx_key_len>-?\d+)$")

        # hashkey_len: 16
        p3_8 = re.compile(r"hashkey_len:\s+(?P<rx_hashkey_len>-?\d+)$")

        # bypass: 0
        p3_9 = re.compile(r"bypass:\s+(?P<rx_bypass>-?\d+)$")

        # conf_offset: 0
        p3_10 = re.compile(r"conf_offset:\s+(?P<rx_conf_offset>-?\d+)$")

        # cipher: GCM_AES_256
        p3_11 = re.compile(r"cipher:\s+(?P<rx_cipher>\S+)$")

        # DeviceID 0
        p4 = re.compile(r"DeviceID\s+(?P<id>-?\d+)$")

        for line in output.splitlines():
            # Port:10, Subport:0, Tx SC index:0
            m = p1.match(line)
            if m:
                match_dict = m.groupdict()
                TX_dict = ret_dict.setdefault("tx", {})
                TX_dict["tx_port"] = int(match_dict["tx_port"])
                TX_dict["tx_sub_port"] = int(match_dict["tx_sub_port"])
                TX_dict["tx_index"] = int(match_dict["tx_index"])
                tx_match = True
                continue

            if tx_match:
                # Prev AN: 1, Cur AN: 2
                m = p1_1.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_prev_an"] = int(match_dict["tx_prev_an"])
                    TX_dict["tx_cur_an"] = int(match_dict["tx_cur_an"])
                    continue

                # encrypt: 1
                m = p1_2.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_encrypt"] = int(match_dict["tx_encrypt"])
                    continue

                # vlan: 1
                m = p1_3.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_vlan"] = int(match_dict["tx_vlan"])
                    continue

                # end_station: 0
                m = p1_4.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_end_station"] = int(match_dict["tx_end_station"])
                    continue

                # scb: 0
                m = p1_5.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_scb"] = int(match_dict["tx_scb"])
                    continue

                # nextPn: 1
                m = p1_6.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_next_pn"] = int(match_dict["tx_next_pn"])
                    continue

                # key_len: 32
                m = p1_7.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_key_len"] = int(match_dict["tx_key_len"])
                    continue

                # hashkey_len: 16
                m = p1_8.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_hashkey_len"] = int(match_dict["tx_hashkey_len"])
                    continue

                # bypass: 0
                m = p1_9.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_bypass"] = int(match_dict["tx_bypass"])
                    continue

                # conf_offset: 0
                m = p1_10.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_conf_offset"] = int(match_dict["tx_conf_offset"])
                    continue

                # cipher: GCM_AES_256
                m = p1_11.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_cipher"] = str(match_dict["tx_cipher"])
                    tx_match = False
                    continue

            # Macsec hash data: Port: 10, Subport: 0, sa_index: -2130706432
            m = p2.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict = ret_dict.setdefault("common", {})
                COMMON_dict["common_port"] = int(match_dict["common_port"])
                COMMON_dict["common_sub_port"] = int(match_dict["common_sub_port"])
                COMMON_dict["common_index"] = str(match_dict["common_index"])
                continue

            # Install Rx Count 715
            m = p2_1.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["install_rx_cnt"] = int(match_dict["install_rx_cnt"])
                continue

            # Install Tx Count 715
            m = p2_2.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["install_tx_cnt"] = int(match_dict["install_tx_cnt"])
                continue

            # Delete Rx Count 711
            m = p2_3.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["del_rx_cnt"] = int(match_dict["del_rx_cnt"])
                continue

            # Install Rx Fail Count 3
            m = p2_4.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["instal_rx_fail_cnt"] = int(
                    match_dict["instal_rx_fail_cnt"]
                )
                continue

            # Install Tx Fail Count 0
            m = p2_5.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["install_tx_fail_cnt"] = int(
                    match_dict["install_tx_fail_cnt"]
                )
                continue

            # Delete Rx Fail Count 0
            m = p2_6.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["del_rx_fail_cnt"] = int(match_dict["del_rx_fail_cnt"])
                continue

            # Rx SA Same AN Count 3
            m = p2_7.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["rx_an_cnt"] = int(match_dict["rx_an_cnt"])
                continue

            # Delay protection: 0
            m = p2_8.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["delay_protection"] = int(match_dict["delay_protection"])
                continue

            # Port:10, Subport:0, Rx SC index:0
            m = p3.match(line)
            if m:
                match_dict = m.groupdict()
                RX_dict = ret_dict.setdefault("rx", {})
                RX_dict["rx_port"] = int(match_dict["rx_port"])
                RX_dict["rx_sub_port"] = int(match_dict["rx_sub_port"])
                RX_dict["rx_index"] = int(match_dict["rx_index"])
                rx_match = True
                continue

            if rx_match:
                # Prev AN: 1, Cur AN: 2
                m = p3_1.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_prev_an"] = int(match_dict["rx_prev_an"])
                    RX_dict["rx_cur_an"] = int(match_dict["rx_cur_an"])
                    continue

                # replay_protect: 1
                m = p3_2.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_replay_protect"] = int(match_dict["rx_replay_protect"])
                    continue

                # replay_window_size: 0
                m = p3_3.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["replay_window_size"] = int(
                        match_dict["replay_window_size"]
                    )
                    continue

                # decrypt_frames: 1
                m = p3_4.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["decrypt_frames"] = int(match_dict["decrypt_frames"])
                    continue

                # validate_frames: 1
                m = p3_5.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["validate_frames"] = int(match_dict["validate_frames"])
                    continue

                # nextPn: 0
                m = p3_6.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_next_pn"] = int(match_dict["rx_next_pn"])
                    continue

                # key_len: 32
                m = p3_7.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_key_len"] = int(match_dict["rx_key_len"])
                    continue

                # hashkey_len: 16
                m = p3_8.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_hashkey_len"] = int(match_dict["rx_hashkey_len"])
                    continue

                # bypass: 0
                m = p3_9.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_bypass"] = int(match_dict["rx_bypass"])
                    continue

                # conf_offset: 0
                m = p3_10.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_conf_offset"] = int(match_dict["rx_conf_offset"])
                    continue

                # cipher: GCM_AES_256
                m = p3_11.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_cipher"] = str(match_dict["rx_cipher"])
                    rx_match = False
                    continue

            # DeviceID 0
            m = p4.match(line)
            if m:
                match_dict = m.groupdict()
                id = int(match_dict["id"])
                if "device" not in ret_dict:
                    ret_dict["device"] = {"id": []}
                ret_dict["device"]["id"].append(id)
                continue

        return ret_dict


# ============================================================================
#  Schema for
#  * 'show platform software iomd {lc no} macsec interface {port no} detail'
# ============================================================================


class ShowPlatformSoftwareIomdMacsecInterfacePortDetailSchema(MetaParser):
    schema = {
        "tx": {
            "tx_port": int,
            "tx_sub_port": int,
            "tx_index": int,
            "tx_prev_an": int,
            "tx_cur_an": int,
            "tx_encrypt": int,
            "tx_vlan": int,
            "tx_end_station": int,
            "tx_scb": int,
            "tx_next_pn": int,
            "tx_key_len": int,
            "tx_hashkey_len": int,
            "tx_bypass": int,
            "tx_conf_offset": int,
            "tx_cipher": str,
        },
        "common": {
            "delay_protection": int,
            "install_rx_cnt": int,
            "install_tx_cnt": int,
            "del_rx_cnt": int,
            "instal_rx_fail_cnt": int,
            "install_tx_fail_cnt": int,
            "del_rx_fail_cnt": int,
            "rx_an_cnt": int,
            "common_port": int,
            "common_sub_port": int,
            "common_index": str,
        },
        "rx": {
            "rx_port": int,
            "rx_sub_port": int,
            "rx_index": int,
            "rx_prev_an": int,
            "rx_cur_an": int,
            "rx_replay_protect": int,
            "replay_window_size": int,
            "decrypt_frames": int,
            "validate_frames": int,
            "rx_next_pn": int,
            "rx_key_len": int,
            "rx_hashkey_len": int,
            "rx_bypass": int,
            "rx_conf_offset": int,
            "rx_cipher": str,
        },
        "device": {"id": list},
    }


class ShowPlatformSoftwareIomdMacsecInterfacePortDetail(
    ShowPlatformSoftwareIomdMacsecInterfacePortDetailSchema
):

    """
    Parser for
    * 'show platform software iomd {lc no} macsec interface {port no} detail'
    """

    cli_command = (
        "show platform software iomd {lc_no} macsec interface {port_no} detail"
    )

    def cli(self, lc_no, port_no, output=None):
        if output is None:
            cmd = self.cli_command.format(lc_no=lc_no, port_no=port_no)
            output = self.device.execute(cmd)

        ret_dict = {}
        tx_match = rx_match = False

        # Port:10, Subport:0, Tx SC index:0
        p1 = re.compile(
            r"Port:(?P<tx_port>-?\d+),\s+Subport:(?P<tx_sub_port>-?\d+),\s+Tx\s+SC\s+index:(?P<tx_index>-?\d+)$"
        )

        # Prev AN: 1, Cur AN: 2
        p1_1 = re.compile(
            r"Prev\s+AN:\s+(?P<tx_prev_an>-?\d+),\s+Cur\s+AN:\s+(?P<tx_cur_an>-?\d+)$"
        )

        # encrypt: 1
        p1_2 = re.compile(r"encrypt:\s+(?P<tx_encrypt>-?\d+)$")

        # vlan: 1
        p1_3 = re.compile(r"vlan:\s+(?P<tx_vlan>-?\d+)$")

        # end_station: 0
        p1_4 = re.compile(r"end_station:\s+(?P<tx_end_station>-?\d+)$")

        # scb: 0
        p1_5 = re.compile(r"scb:\s+(?P<tx_scb>-?\d+)$")

        # nextPn: 1
        p1_6 = re.compile(r"nextPn:\s+(?P<tx_next_pn>-?\d+)$")

        # key_len: 32
        p1_7 = re.compile(r"key_len:\s+(?P<tx_key_len>-?\d+)$")

        # hashkey_len: 16
        p1_8 = re.compile(r"hashkey_len:\s+(?P<tx_hashkey_len>-?\d+)$")

        # bypass: 0
        p1_9 = re.compile(r"bypass:\s+(?P<tx_bypass>-?\d+)$")

        # conf_offset: 0
        p1_10 = re.compile(r"conf_offset:\s+(?P<tx_conf_offset>-?\d+)$")

        # cipher: GCM_AES_256
        p1_11 = re.compile(r"cipher:\s+(?P<tx_cipher>\S+)$")

        # Macsec hash data: Port: 10, Subport: 0, sa_index: -2130706432
        p2 = re.compile(
            r"Macsec\s+hash\s+data:\s+Port:\s+(?P<common_port>-?\d+),\s+Subport:\s+(?P<common_sub_port>-?\d+),\s+sa_index:\s+(?P<common_index>\S+)$"
        )

        # Install Rx Count 715
        p2_1 = re.compile(r"Install\s+Rx\s+Count\s+(?P<install_rx_cnt>-?\d+)$")

        # Install Tx Count 715
        p2_2 = re.compile(r"Install\s+Tx\s+Count\s+(?P<install_tx_cnt>-?\d+)$")

        # Delete Rx Count 711
        p2_3 = re.compile(r"Delete\s+Rx\s+Count\s+(?P<del_rx_cnt>-?\d+)$")

        # Install Rx Fail Count 3
        p2_4 = re.compile(
            r"Install\s+Rx\s+Fail\s+Count\s+(?P<instal_rx_fail_cnt>-?\d+)$"
        )

        # Install Tx Fail Count 0
        p2_5 = re.compile(
            r"Install\s+Tx\s+Fail\s+Count\s+(?P<install_tx_fail_cnt>-?\d+)$"
        )

        # Delete Rx Fail Count 0
        p2_6 = re.compile(r"Delete\s+Rx\s+Fail\s+Count\s+(?P<del_rx_fail_cnt>-?\d+)$")

        # Rx SA Same AN Count 3
        p2_7 = re.compile(r"Rx\s+SA\s+Same\s+AN\s+Count\s+(?P<rx_an_cnt>-?\d+)$")

        # Delay protection: 0
        p2_8 = re.compile(r"Delay\s+protection:\s+(?P<delay_protection>-?\d+)$")

        # Port:10, Subport:0, Rx SC index:0
        p3 = re.compile(
            r"Port:(?P<rx_port>-?\d+),\s+Subport:(?P<rx_sub_port>-?\d+),\s+Rx\s+SC\s+index:(?P<rx_index>-?\d+)$"
        )

        # Prev AN: 1, Cur AN: 2
        p3_1 = re.compile(
            r"Prev\s+AN:\s+(?P<rx_prev_an>-?\d+),\s+Cur\s+AN:\s+(?P<rx_cur_an>-?\d+)$"
        )

        # replay_protect: 1
        p3_2 = re.compile(r"replay_protect:\s+(?P<rx_replay_protect>-?\d+)$")

        # replay_window_size: 0
        p3_3 = re.compile(r"replay_window_size:\s+(?P<replay_window_size>-?\d+)$")

        # decrypt_frames: 1
        p3_4 = re.compile(r"decrypt_frames:\s+(?P<decrypt_frames>-?\d+)$")

        # validate_frames: 1
        p3_5 = re.compile(r"validate_frames:\s+(?P<validate_frames>-?\d+)$")

        # nextPn: 0
        p3_6 = re.compile(r"nextPn:\s+(?P<rx_next_pn>-?\d+)$")

        # key_len: 32
        p3_7 = re.compile(r"key_len:\s+(?P<rx_key_len>-?\d+)$")

        # hashkey_len: 16
        p3_8 = re.compile(r"hashkey_len:\s+(?P<rx_hashkey_len>-?\d+)$")

        # bypass: 0
        p3_9 = re.compile(r"bypass:\s+(?P<rx_bypass>-?\d+)$")

        # conf_offset: 0
        p3_10 = re.compile(r"conf_offset:\s+(?P<rx_conf_offset>-?\d+)$")

        # cipher: GCM_AES_256
        p3_11 = re.compile(r"cipher:\s+(?P<rx_cipher>\S+)$")

        # DeviceID 0
        p4 = re.compile(r"DeviceID\s+(?P<id>-?\d+)$")

        for line in output.splitlines():
            # Port:10, Subport:0, Tx SC index:0
            m = p1.match(line)
            if m:
                match_dict = m.groupdict()
                TX_dict = ret_dict.setdefault("tx", {})
                TX_dict["tx_port"] = int(match_dict["tx_port"])
                TX_dict["tx_sub_port"] = int(match_dict["tx_sub_port"])
                TX_dict["tx_index"] = int(match_dict["tx_index"])
                tx_match = True
                continue

            if tx_match:
                # Prev AN: 1, Cur AN: 2
                m = p1_1.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_prev_an"] = int(match_dict["tx_prev_an"])
                    TX_dict["tx_cur_an"] = int(match_dict["tx_cur_an"])
                    continue

                # encrypt: 1
                m = p1_2.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_encrypt"] = int(match_dict["tx_encrypt"])
                    continue

                # vlan: 1
                m = p1_3.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_vlan"] = int(match_dict["tx_vlan"])
                    continue

                # end_station: 0
                m = p1_4.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_end_station"] = int(match_dict["tx_end_station"])
                    continue

                # scb: 0
                m = p1_5.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_scb"] = int(match_dict["tx_scb"])
                    continue

                # nextPn: 1
                m = p1_6.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_next_pn"] = int(match_dict["tx_next_pn"])
                    continue

                # key_len: 32
                m = p1_7.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_key_len"] = int(match_dict["tx_key_len"])
                    continue

                # hashkey_len: 16
                m = p1_8.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_hashkey_len"] = int(match_dict["tx_hashkey_len"])
                    continue

                # bypass: 0
                m = p1_9.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_bypass"] = int(match_dict["tx_bypass"])
                    continue

                # conf_offset: 0
                m = p1_10.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_conf_offset"] = int(match_dict["tx_conf_offset"])
                    continue

                # cipher: GCM_AES_256
                m = p1_11.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_cipher"] = str(match_dict["tx_cipher"])
                    tx_match = False
                    continue

            # Macsec hash data: Port: 10, Subport: 0, sa_index: -2130706432
            m = p2.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict = ret_dict.setdefault("common", {})
                COMMON_dict["common_port"] = int(match_dict["common_port"])
                COMMON_dict["common_sub_port"] = int(match_dict["common_sub_port"])
                COMMON_dict["common_index"] = str(match_dict["common_index"])
                continue

            # Install Rx Count 715
            m = p2_1.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["install_rx_cnt"] = int(match_dict["install_rx_cnt"])
                continue

            # Install Tx Count 715
            m = p2_2.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["install_tx_cnt"] = int(match_dict["install_tx_cnt"])
                continue

            # Delete Rx Count 711
            m = p2_3.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["del_rx_cnt"] = int(match_dict["del_rx_cnt"])
                continue

            # Install Rx Fail Count 3
            m = p2_4.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["instal_rx_fail_cnt"] = int(
                    match_dict["instal_rx_fail_cnt"]
                )
                continue

            # Install Tx Fail Count 0
            m = p2_5.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["install_tx_fail_cnt"] = int(
                    match_dict["install_tx_fail_cnt"]
                )
                continue

            # Delete Rx Fail Count 0
            m = p2_6.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["del_rx_fail_cnt"] = int(match_dict["del_rx_fail_cnt"])
                continue

            # Rx SA Same AN Count 3
            m = p2_7.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["rx_an_cnt"] = int(match_dict["rx_an_cnt"])
                continue

            # Delay protection: 0
            m = p2_8.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["delay_protection"] = int(match_dict["delay_protection"])
                continue

            # Port:10, Subport:0, Rx SC index:0
            m = p3.match(line)
            if m:
                match_dict = m.groupdict()
                RX_dict = ret_dict.setdefault("rx", {})
                RX_dict["rx_port"] = int(match_dict["rx_port"])
                RX_dict["rx_sub_port"] = int(match_dict["rx_sub_port"])
                RX_dict["rx_index"] = int(match_dict["rx_index"])
                rx_match = True
                continue

            if rx_match:
                # Prev AN: 1, Cur AN: 2
                m = p3_1.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_prev_an"] = int(match_dict["rx_prev_an"])
                    RX_dict["rx_cur_an"] = int(match_dict["rx_cur_an"])
                    continue

                # replay_protect: 1
                m = p3_2.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_replay_protect"] = int(match_dict["rx_replay_protect"])
                    continue

                # replay_window_size: 0
                m = p3_3.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["replay_window_size"] = int(
                        match_dict["replay_window_size"]
                    )
                    continue

                # decrypt_frames: 1
                m = p3_4.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["decrypt_frames"] = int(match_dict["decrypt_frames"])
                    continue

                # validate_frames: 1
                m = p3_5.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["validate_frames"] = int(match_dict["validate_frames"])
                    continue

                # nextPn: 0
                m = p3_6.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_next_pn"] = int(match_dict["rx_next_pn"])
                    continue

                # key_len: 32
                m = p3_7.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_key_len"] = int(match_dict["rx_key_len"])
                    continue

                # hashkey_len: 16
                m = p3_8.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_hashkey_len"] = int(match_dict["rx_hashkey_len"])
                    continue

                # bypass: 0
                m = p3_9.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_bypass"] = int(match_dict["rx_bypass"])
                    continue

                # conf_offset: 0
                m = p3_10.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_conf_offset"] = int(match_dict["rx_conf_offset"])
                    continue

                # cipher: GCM_AES_256
                m = p3_11.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_cipher"] = str(match_dict["rx_cipher"])
                    rx_match = False
                    continue

            # DeviceID 0
            m = p4.match(line)
            if m:
                match_dict = m.groupdict()
                id = int(match_dict["id"])
                if "device" not in ret_dict:
                    ret_dict["device"] = {"id": []}
                ret_dict["device"]["id"].append(id)
                continue

        return ret_dict


# ============================================================================
#  Schema for
#  * 'show platform software iomd {lc no} macsec interface {port no} detail'
# ============================================================================


class ShowPlatformSoftwareIomdMacsecInterfacePortDetailSchema(MetaParser):
    schema = {
        "tx": {
            "tx_port": int,
            "tx_sub_port": int,
            "tx_index": int,
            "tx_prev_an": int,
            "tx_cur_an": int,
            "tx_encrypt": int,
            "tx_vlan": int,
            "tx_end_station": int,
            "tx_scb": int,
            "tx_next_pn": int,
            "tx_key_len": int,
            "tx_hashkey_len": int,
            "tx_bypass": int,
            "tx_conf_offset": int,
            "tx_cipher": str,
        },
        "common": {
            "delay_protection": int,
            "install_rx_cnt": int,
            "install_tx_cnt": int,
            "del_rx_cnt": int,
            "instal_rx_fail_cnt": int,
            "install_tx_fail_cnt": int,
            "del_rx_fail_cnt": int,
            "rx_an_cnt": int,
            "common_port": int,
            "common_sub_port": int,
            "common_index": str,
        },
        "rx": {
            "rx_port": int,
            "rx_sub_port": int,
            "rx_index": int,
            "rx_prev_an": int,
            "rx_cur_an": int,
            "rx_replay_protect": int,
            "replay_window_size": int,
            "decrypt_frames": int,
            "validate_frames": int,
            "rx_next_pn": int,
            "rx_key_len": int,
            "rx_hashkey_len": int,
            "rx_bypass": int,
            "rx_conf_offset": int,
            "rx_cipher": str,
        },
        "device": {"id": list},
    }


class ShowPlatformSoftwareIomdMacsecInterfacePortDetail(
    ShowPlatformSoftwareIomdMacsecInterfacePortDetailSchema
):

    """
    Parser for
    * 'show platform software iomd {lc no} macsec interface {port no} detail'
    """

    cli_command = (
        "show platform software iomd {lc_no} macsec interface {port_no} detail"
    )

    def cli(self, lc_no, port_no, output=None):
        if output is None:
            cmd = self.cli_command.format(lc_no=lc_no, port_no=port_no)
            output = self.device.execute(cmd)

        ret_dict = {}
        tx_match = rx_match = False

        # Port:10, Subport:0, Tx SC index:0
        p1 = re.compile(
            r"Port:(?P<tx_port>-?\d+),\s+Subport:(?P<tx_sub_port>-?\d+),\s+Tx\s+SC\s+index:(?P<tx_index>-?\d+)$"
        )

        # Prev AN: 1, Cur AN: 2
        p1_1 = re.compile(
            r"Prev\s+AN:\s+(?P<tx_prev_an>-?\d+),\s+Cur\s+AN:\s+(?P<tx_cur_an>-?\d+)$"
        )

        # encrypt: 1
        p1_2 = re.compile(r"encrypt:\s+(?P<tx_encrypt>-?\d+)$")

        # vlan: 1
        p1_3 = re.compile(r"vlan:\s+(?P<tx_vlan>-?\d+)$")

        # end_station: 0
        p1_4 = re.compile(r"end_station:\s+(?P<tx_end_station>-?\d+)$")

        # scb: 0
        p1_5 = re.compile(r"scb:\s+(?P<tx_scb>-?\d+)$")

        # nextPn: 1
        p1_6 = re.compile(r"nextPn:\s+(?P<tx_next_pn>-?\d+)$")

        # key_len: 32
        p1_7 = re.compile(r"key_len:\s+(?P<tx_key_len>-?\d+)$")

        # hashkey_len: 16
        p1_8 = re.compile(r"hashkey_len:\s+(?P<tx_hashkey_len>-?\d+)$")

        # bypass: 0
        p1_9 = re.compile(r"bypass:\s+(?P<tx_bypass>-?\d+)$")

        # conf_offset: 0
        p1_10 = re.compile(r"conf_offset:\s+(?P<tx_conf_offset>-?\d+)$")

        # cipher: GCM_AES_256
        p1_11 = re.compile(r"cipher:\s+(?P<tx_cipher>\S+)$")

        # Macsec hash data: Port: 10, Subport: 0, sa_index: -2130706432
        p2 = re.compile(
            r"Macsec\s+hash\s+data:\s+Port:\s+(?P<common_port>-?\d+),\s+Subport:\s+(?P<common_sub_port>-?\d+),\s+sa_index:\s+(?P<common_index>\S+)$"
        )

        # Install Rx Count 715
        p2_1 = re.compile(r"Install\s+Rx\s+Count\s+(?P<install_rx_cnt>-?\d+)$")

        # Install Tx Count 715
        p2_2 = re.compile(r"Install\s+Tx\s+Count\s+(?P<install_tx_cnt>-?\d+)$")

        # Delete Rx Count 711
        p2_3 = re.compile(r"Delete\s+Rx\s+Count\s+(?P<del_rx_cnt>-?\d+)$")

        # Install Rx Fail Count 3
        p2_4 = re.compile(
            r"Install\s+Rx\s+Fail\s+Count\s+(?P<instal_rx_fail_cnt>-?\d+)$"
        )

        # Install Tx Fail Count 0
        p2_5 = re.compile(
            r"Install\s+Tx\s+Fail\s+Count\s+(?P<install_tx_fail_cnt>-?\d+)$"
        )

        # Delete Rx Fail Count 0
        p2_6 = re.compile(r"Delete\s+Rx\s+Fail\s+Count\s+(?P<del_rx_fail_cnt>-?\d+)$")

        # Rx SA Same AN Count 3
        p2_7 = re.compile(r"Rx\s+SA\s+Same\s+AN\s+Count\s+(?P<rx_an_cnt>-?\d+)$")

        # Delay protection: 0
        p2_8 = re.compile(r"Delay\s+protection:\s+(?P<delay_protection>-?\d+)$")

        # Port:10, Subport:0, Rx SC index:0
        p3 = re.compile(
            r"Port:(?P<rx_port>-?\d+),\s+Subport:(?P<rx_sub_port>-?\d+),\s+Rx\s+SC\s+index:(?P<rx_index>-?\d+)$"
        )

        # Prev AN: 1, Cur AN: 2
        p3_1 = re.compile(
            r"Prev\s+AN:\s+(?P<rx_prev_an>-?\d+),\s+Cur\s+AN:\s+(?P<rx_cur_an>-?\d+)$"
        )

        # replay_protect: 1
        p3_2 = re.compile(r"replay_protect:\s+(?P<rx_replay_protect>-?\d+)$")

        # replay_window_size: 0
        p3_3 = re.compile(r"replay_window_size:\s+(?P<replay_window_size>-?\d+)$")

        # decrypt_frames: 1
        p3_4 = re.compile(r"decrypt_frames:\s+(?P<decrypt_frames>-?\d+)$")

        # validate_frames: 1
        p3_5 = re.compile(r"validate_frames:\s+(?P<validate_frames>-?\d+)$")

        # nextPn: 0
        p3_6 = re.compile(r"nextPn:\s+(?P<rx_next_pn>-?\d+)$")

        # key_len: 32
        p3_7 = re.compile(r"key_len:\s+(?P<rx_key_len>-?\d+)$")

        # hashkey_len: 16
        p3_8 = re.compile(r"hashkey_len:\s+(?P<rx_hashkey_len>-?\d+)$")

        # bypass: 0
        p3_9 = re.compile(r"bypass:\s+(?P<rx_bypass>-?\d+)$")

        # conf_offset: 0
        p3_10 = re.compile(r"conf_offset:\s+(?P<rx_conf_offset>-?\d+)$")

        # cipher: GCM_AES_256
        p3_11 = re.compile(r"cipher:\s+(?P<rx_cipher>\S+)$")

        # DeviceID 0
        p4 = re.compile(r"DeviceID\s+(?P<id>-?\d+)$")

        for line in output.splitlines():
            # Port:10, Subport:0, Tx SC index:0
            m = p1.match(line)
            if m:
                match_dict = m.groupdict()
                TX_dict = ret_dict.setdefault("tx", {})
                TX_dict["tx_port"] = int(match_dict["tx_port"])
                TX_dict["tx_sub_port"] = int(match_dict["tx_sub_port"])
                TX_dict["tx_index"] = int(match_dict["tx_index"])
                tx_match = True
                continue

            if tx_match:
                # Prev AN: 1, Cur AN: 2
                m = p1_1.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_prev_an"] = int(match_dict["tx_prev_an"])
                    TX_dict["tx_cur_an"] = int(match_dict["tx_cur_an"])
                    continue

                # encrypt: 1
                m = p1_2.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_encrypt"] = int(match_dict["tx_encrypt"])
                    continue

                # vlan: 1
                m = p1_3.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_vlan"] = int(match_dict["tx_vlan"])
                    continue

                # end_station: 0
                m = p1_4.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_end_station"] = int(match_dict["tx_end_station"])
                    continue

                # scb: 0
                m = p1_5.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_scb"] = int(match_dict["tx_scb"])
                    continue

                # nextPn: 1
                m = p1_6.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_next_pn"] = int(match_dict["tx_next_pn"])
                    continue

                # key_len: 32
                m = p1_7.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_key_len"] = int(match_dict["tx_key_len"])
                    continue

                # hashkey_len: 16
                m = p1_8.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_hashkey_len"] = int(match_dict["tx_hashkey_len"])
                    continue

                # bypass: 0
                m = p1_9.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_bypass"] = int(match_dict["tx_bypass"])
                    continue

                # conf_offset: 0
                m = p1_10.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_conf_offset"] = int(match_dict["tx_conf_offset"])
                    continue

                # cipher: GCM_AES_256
                m = p1_11.match(line)
                if m:
                    match_dict = m.groupdict()
                    TX_dict["tx_cipher"] = str(match_dict["tx_cipher"])
                    tx_match = False
                    continue

            # Macsec hash data: Port: 10, Subport: 0, sa_index: -2130706432
            m = p2.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict = ret_dict.setdefault("common", {})
                COMMON_dict["common_port"] = int(match_dict["common_port"])
                COMMON_dict["common_sub_port"] = int(match_dict["common_sub_port"])
                COMMON_dict["common_index"] = str(match_dict["common_index"])
                continue

            # Install Rx Count 715
            m = p2_1.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["install_rx_cnt"] = int(match_dict["install_rx_cnt"])
                continue

            # Install Tx Count 715
            m = p2_2.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["install_tx_cnt"] = int(match_dict["install_tx_cnt"])
                continue

            # Delete Rx Count 711
            m = p2_3.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["del_rx_cnt"] = int(match_dict["del_rx_cnt"])
                continue

            # Install Rx Fail Count 3
            m = p2_4.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["instal_rx_fail_cnt"] = int(
                    match_dict["instal_rx_fail_cnt"]
                )
                continue

            # Install Tx Fail Count 0
            m = p2_5.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["install_tx_fail_cnt"] = int(
                    match_dict["install_tx_fail_cnt"]
                )
                continue

            # Delete Rx Fail Count 0
            m = p2_6.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["del_rx_fail_cnt"] = int(match_dict["del_rx_fail_cnt"])
                continue

            # Rx SA Same AN Count 3
            m = p2_7.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["rx_an_cnt"] = int(match_dict["rx_an_cnt"])
                continue

            # Delay protection: 0
            m = p2_8.match(line)
            if m:
                match_dict = m.groupdict()
                COMMON_dict["delay_protection"] = int(match_dict["delay_protection"])
                continue

            # Port:10, Subport:0, Rx SC index:0
            m = p3.match(line)
            if m:
                match_dict = m.groupdict()
                RX_dict = ret_dict.setdefault("rx", {})
                RX_dict["rx_port"] = int(match_dict["rx_port"])
                RX_dict["rx_sub_port"] = int(match_dict["rx_sub_port"])
                RX_dict["rx_index"] = int(match_dict["rx_index"])
                rx_match = True
                continue

            if rx_match:
                # Prev AN: 1, Cur AN: 2
                m = p3_1.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_prev_an"] = int(match_dict["rx_prev_an"])
                    RX_dict["rx_cur_an"] = int(match_dict["rx_cur_an"])
                    continue

                # replay_protect: 1
                m = p3_2.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_replay_protect"] = int(match_dict["rx_replay_protect"])
                    continue

                # replay_window_size: 0
                m = p3_3.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["replay_window_size"] = int(
                        match_dict["replay_window_size"]
                    )
                    continue

                # decrypt_frames: 1
                m = p3_4.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["decrypt_frames"] = int(match_dict["decrypt_frames"])
                    continue

                # validate_frames: 1
                m = p3_5.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["validate_frames"] = int(match_dict["validate_frames"])
                    continue

                # nextPn: 0
                m = p3_6.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_next_pn"] = int(match_dict["rx_next_pn"])
                    continue

                # key_len: 32
                m = p3_7.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_key_len"] = int(match_dict["rx_key_len"])
                    continue

                # hashkey_len: 16
                m = p3_8.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_hashkey_len"] = int(match_dict["rx_hashkey_len"])
                    continue

                # bypass: 0
                m = p3_9.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_bypass"] = int(match_dict["rx_bypass"])
                    continue

                # conf_offset: 0
                m = p3_10.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_conf_offset"] = int(match_dict["rx_conf_offset"])
                    continue

                # cipher: GCM_AES_256
                m = p3_11.match(line)
                if m:
                    match_dict = m.groupdict()
                    RX_dict["rx_cipher"] = str(match_dict["rx_cipher"])
                    rx_match = False
                    continue

            # DeviceID 0
            m = p4.match(line)
            if m:
                match_dict = m.groupdict()
                id = int(match_dict["id"])
                if "device" not in ret_dict:
                    ret_dict["device"] = {"id": []}
                ret_dict["device"]["id"].append(id)
                continue

        return ret_dict


# ======================================================
# Parser for 'show platform software memory database fed switch active callsite'
# ======================================================
class ShowPlatformSoftwareMemoryDatabaseFedSwitchActiveCallsiteSchema(MetaParser):
    """Schema for show platform software memory database fed switch active callsite"""

    schema = {
        "database": {
            Any(): {Optional("callsite"): {Any(): {"calls": int, "bytes": int}}}
        }
    }


class ShowPlatformSoftwareMemoryDatabaseFedSwitchActiveCallsite(
    ShowPlatformSoftwareMemoryDatabaseFedSwitchActiveCallsiteSchema
):
    """Parser for show platform software memory database fed switch active callsite"""

    cli_command = [
        "show platform software memory database fed {switch} {switch_var} callsite",
        "show platform software memory database fed {switch_var} callsite",
    ]

    def cli(self, switch_var, switch="", output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, switch_var=switch_var)
            else:
                cmd = self.cli_command[1].format(switch_var=switch_var)
            output = self.device.execute(cmd)

        # Database name: BP_OPER_DB
        p1 = re.compile(r"^Database name:\s+(?P<database>[\w\_]+)$")

        # 7E24C8967BBC800C    1             136
        # AEB80E49BA63C001    10            1176
        p2 = re.compile(r"^(?P<callsite>\w+)\s+(?P<calls>\d+)\s+(?P<bytes>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Database name: BP_OPER_DB
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                db_dict = ret_dict.setdefault("database", {}).setdefault(
                    dict_val["database"], {}
                )

            # 7E24C8967BBC800C    1             136
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                callsite_dict = db_dict.setdefault("callsite", {}).setdefault(
                    dict_val["callsite"], {}
                )
                callsite_dict["calls"] = int(dict_val["calls"])
                callsite_dict["bytes"] = int(dict_val["bytes"])
                continue

        return ret_dict


# ============================================================
# Parser for 'show diagnostics status'
# ============================================================


class ShowDiagnosticStatusSchema(MetaParser):
    """Schema for show diagnostics status"""

    schema = {
        "diagnostic_status": {"card": int, "description": str, "run_by": str},
        "current_running_test": {Any(): {"run_by": str}},
    }


class ShowDiagnosticStatus(ShowDiagnosticStatusSchema):
    """Schema for show diagnostics status"""

    cli_command = "show diagnostic status"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # 1      C9300-24UX                        DiagThermalTest                 <HM>
        p1 = re.compile(
            r"^(?P<card>\d)+\s+(?P<description>\S+)+\s+\S+\s+.(?P<run_by>\w+).*$"
        )

        # DiagFanTest                     <HM>
        p2 = re.compile(r"^(?P<current_running_test>\S+\s+)<HM>$")

        for line in output.splitlines():
            line = line.strip()

            # 1      C9300-24UX                        DiagThermalTest                 <HM>
            m = p1.match(line)
            if m:
                group = m.groupdict()
                card = int(group["card"])
                description = group["description"]
                run = group["run_by"]
                sub_dict = ret_dict.setdefault("diagnostic_status", {})
                sub_dict["card"] = card
                sub_dict["description"] = description
                sub_dict["run_by"] = run
                continue

            # DiagFanTest                     <HM>
            m = p2.match(line)
            if m:
                group = m.groupdict()
                current_running_test = group["current_running_test"].strip()
                tmp_dict = ret_dict.setdefault("current_running_test", {}).setdefault(
                    current_running_test, {}
                )
                tmp_dict["run_by"] = run
                continue

        return ret_dict


class ShowPlatformSoftwareCpmSwitchActiveB0CountersInterfaceLacpSchema(MetaParser):
    """Schema for show platform software cpm switch active B0 counters interface isis"""

    schema = {
        Any(): {
            "tx": int,
            "rx": int,
            "tx_drop": int,
            "rx_drop": int,
        },
    }


class ShowPlatformSoftwareCpmSwitchActiveB0CountersInterfaceLacp(
    ShowPlatformSoftwareCpmSwitchActiveB0CountersInterfaceLacpSchema
):
    """
    ShowPlatformSoftwareCpmSwitchActiveB0CountersInterfaceLacp
    """

    cli_command = "show platform software cpm switch {mode} B0 counters interface lacp"

    def cli(self, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode))

        ret_dict = {}

        # FiftyGigE1/0/25
        p0 = re.compile(r"^(?P<interface>\S+)$")

        #'114      329      0     0'
        p1 = re.compile(
            r"^(?P<tx>\d+) +(?P<rx>\d+) +(?P<tx_drop>\d+) +(?P<rx_drop>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # FiftyGigE1/0/25
            m = p0.match(line)
            if m:
                group = m.groupdict()
                interface_name = Common.convert_intf_name(group["interface"])
                int_dict = ret_dict.setdefault(interface_name, {})
                continue

            #'114      329      0     0'
            m = p1.match(line)
            if m:
                group = m.groupdict()
                int_dict["tx"] = int(group["tx"])
                int_dict["rx"] = int(group["rx"])
                int_dict["tx_drop"] = int(group["tx_drop"])
                int_dict["rx_drop"] = int(group["rx_drop"])
                continue

        return ret_dict


class ShowPlatformSoftwareCpmCountersInterfaceIsisSchema(MetaParser):
    """Schema for show platform software cpm switch active B0 counters interface isis"""

    schema = {
        "traffic_detail": {
            Any(): {
                "tx": int,
                "rx": int,
                "tx_drop": int,
                "rx_drop": int,
            },
        },
        "timestamp_now": str,
        "interface": {
            Any(): {
                "isis_rx_timestamp": {
                    "timestamp": dict,
                    Optional("rx_max_time_gap"): str,
                    Optional("rx_max_timestamp"): str,
                },
                "isis_tx_timestamp": {
                    "timestamp": dict,
                    Optional("tx_max_time_gap"): str,
                    Optional("tx_max_timestamp"): str,
                },
            },
        },
    }


class ShowPlatformSoftwareCpmCountersInterfaceIsis(
    ShowPlatformSoftwareCpmCountersInterfaceIsisSchema
):
    """
    ShowPlatformSoftwareCpmSwitchActiveB0CountersInterfaceIsis
    """

    cli_command = "show platform software cpm switch {mode} B0 counters interface isis"

    def cli(self, mode, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(mode=mode))

        ret_dict = {}
        temp_dict = {}

        # FiftyGigE1/0/25 [4]
        p0 = re.compile(r"^(?P<interface>\S+)\s+\[\d+\]$")

        #'114      329      0     0'
        p1 = re.compile(
            r"^(?P<tx>\d+) +(?P<rx>\d+) +(?P<tx_drop>\d+) +(?P<rx_drop>\d+)$"
        )

        # Timestamp Now: Mar 07 11:00:43.313
        p2 = re.compile(r"^Timestamp +Now\: +(?P<timestamp_now>.*)$")

        # ISIS RX Timestamp: Mar 11 10:42:45.594 [3]
        p3 = re.compile(r"^ISIS +RX +Timestamp\: +(?P<time>.*) +\[(?P<count>\d+)\]$")

        # ISIS RX Maximum Time Gap:                5 sec,             512 usec
        p4 = re.compile(r"^ISIS +RX +Maximum +Time +Gap\: +(?P<rx_max_time_gap>.*)$")

        # ISIS RX Maximum Gap Timestamp: Mar 11 08:36:12.697
        p5 = re.compile(
            r"^ISIS +RX +Maximum +Gap +Timestamp\: +(?P<rx_max_timestamp>.*)$"
        )

        # ISIS TX Timestamp: Mar 11 10:42:50.983 [1]
        p6 = re.compile(r"^ISIS +TX +Timestamp\: +(?P<time>.*) +\[(?P<count>\d+)\]$")

        # ISIS TX Maximum Time Gap:                9 sec,          492792 usec
        p7 = re.compile(r"^ISIS +TX +Maximum +Time +Gap\: +(?P<tx_max_time_gap>.*)$")

        # ISIS TX Maximum Gap Timestamp: Mar 11 07:31:20.299
        p8 = re.compile(
            r"^ISIS +TX +Maximum +Gap +Timestamp\: +(?P<tx_max_timestamp>.*)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # FiftyGigE1/0/25 [4]
            m = p0.match(line)
            if m:
                group = m.groupdict()
                interface_name = Common.convert_intf_name(group["interface"])
                if ret_dict.get("timestamp_now"):
                    int_dict = ret_dict.setdefault("interface", {}).setdefault(
                        interface_name, {}
                    )
                else:
                    int_dict = ret_dict.setdefault("traffic_detail", {}).setdefault(
                        interface_name, {}
                    )

            #'114      329      0     0'
            m = p1.match(line)
            if m:
                group = m.groupdict()
                int_dict["tx"] = int(group["tx"])
                int_dict["rx"] = int(group["rx"])
                int_dict["tx_drop"] = int(group["tx_drop"])
                int_dict["rx_drop"] = int(group["rx_drop"])
                continue

            # Timestamp Now: Mar 07 11:00:43.313
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["timestamp_now"] = group["timestamp_now"]
                continue

            # ISIS RX Timestamp: Mar 11 10:42:45.594 [3]
            count = 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                count = int(group["count"])
                temp_dict.update({count: group["time"]})
                continue

            # ISIS RX Maximum Time Gap:                5 sec,             512 usec
            m = p4.match(line)
            if m:
                int_dict = int_dict.setdefault("isis_rx_timestamp", {})
                int_dict["timestamp"] = temp_dict
                temp_dict = {}
                group = m.groupdict()
                int_dict["rx_max_time_gap"] = group["rx_max_time_gap"]
                continue

            # ISIS RX Maximum Gap Timestamp: Mar 11 08:36:12.697
            m = p5.match(line)
            if m:
                group = m.groupdict()
                int_dict["rx_max_timestamp"] = group["rx_max_timestamp"]
                continue

            # ISIS TX Timestamp: Mar 11 10:42:50.983 [1]
            count = 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                count = int(group["count"])
                temp_dict.update({count: group["time"]})
                continue

            # ISIS TX Maximum Time Gap:                9 sec,          492792 usec
            m = p7.match(line)
            if m:
                int_dict = (
                    ret_dict.setdefault("interface", {})
                    .setdefault(interface_name, {})
                    .setdefault("isis_tx_timestamp", {})
                )
                int_dict["timestamp"] = temp_dict
                temp_dict = {}
                group = m.groupdict()
                int_dict["tx_max_time_gap"] = group["tx_max_time_gap"]
                continue

            # ISIS TX Maximum Gap Timestamp: Mar 11 07:31:20.299
            m = p8.match(line)
            if m:
                group = m.groupdict()
                int_dict["tx_max_timestamp"] = group["tx_max_timestamp"]
                continue

        return ret_dict


class ShowPlatformSoftwareMountSwitchActiveRpTmpfsSchema(MetaParser):
    """
    Schema for show platform software mount switch active rp active | include tmpfs
    """

    schema = {
        "index": {
            Any(): {
                "file_system": str,
                "used": int,
                "available": int,
                "use_percent": str,
                "mounted_on": str,
            },
        },
    }


class ShowPlatformSoftwareMountSwitchActiveRpTmpfs(
    ShowPlatformSoftwareMountSwitchActiveRpTmpfsSchema
):
    """
    show platform software mount switch active rp active | include tmpfs
    """

    cli_command = [
        "show platform software mount {switch} {mode} rp active | include {file_system}",
        "show platform software mount rp active | include {file_system}",
    ]

    def cli(self, file_system, switch=None, mode=None, output=None):
        if output is None:
            if switch and mode and file_system:
                cmd = self.cli_command[0].format(
                    switch=switch, mode=mode, file_system=file_system
                )
            else:
                cmd = self.cli_command[1].format(file_system=file_system)
            output = self.device.execute(cmd)

        ret_dict = {}
        index = 1

        # Filesystem                 Used  Available Use % Mounted on
        # -------------------------------------------------------------------------------
        # tmpfs                    147996   25782148    1% /tmp/rp/tdldb
        p0 = re.compile(
            r"^(?P<file_system>\S+)\s+(?P<used>\d+)\s+(?P<available>\d+)\s+(?P<use_percent>\S+)\s+(?P<mounted_on>\S+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Filesystem                 Used  Available Use % Mounted on
            # -------------------------------------------------------------------------------
            # tmpfs                    147996   25782148    1% /tmp/rp/tdldb
            m = p0.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault("index", {}).setdefault(index, {})
                index_dict.update(
                    {
                        "file_system": group["file_system"],
                        "used": int(group["used"]),
                        "available": int(group["available"]),
                        "use_percent": group["use_percent"],
                        "mounted_on": group["mounted_on"],
                    }
                )
                index += 1
                continue

        return ret_dict


# =======================================================================
# Schema for 'show platform software object-manager {switch} {switch_type} F0 statistics'
# =======================================================================
class ShowPlatSwObjectManagerF0StatisticsSchema(MetaParser):
    """Schema for :
    show platform software object-manager {switch} {switch_type} F0 statistics"""

    schema = {
        "object_update": {
            "pending_issue": int,
            "pending_acknowledgement": int,
        },
        "batch_begin": {
            "pending_issue": int,
            "pending_acknowledgement": int,
        },
        "batch_end": {
            "pending_issue": int,
            "pending_acknowledgement": int,
        },
        "command": {
            "pending_acknowledgement": int,
        },
        "total_objects": int,
        "stale_objects": int,
        "resolve_objects": int,
        "childless_delete_objects": int,
        "backplane_objects": int,
        "error_objects": int,
        "number_of_bundles": int,
        "paused_types": int,
    }


# ================================================================
# Parser for 'show platform software object-manager {switch} {switch_type} F0 statistics'
# ================================================================
class ShowPlatSwObjectManagerF0Statistics(ShowPlatSwObjectManagerF0StatisticsSchema):
    """parser for :
    'show platform software object-manager {switch} {switch_type} F0 statistics'
    'show platform software object-manager F0 statistics'
    """

    cli_command = [
        "show platform software object-manager F0 statistics",
        "show platform software object-manager {switch} {switch_type} F0 statistics",
    ]

    def cli(self, switch=None, switch_type=None, output=None):
        if output is None:
            if switch and switch_type:
                cmd = self.cli_command[1].format(switch=switch, switch_type=switch_type)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        # Object update: Pending-issue: 180, Pending-acknowledgement: 89
        p1 = re.compile(
            r"^Object update:\s+Pending-issue:"
            r"\s+(?P<pending_issue>\d+)\,\s"
            r"Pending-acknowledgement: "
            r"(?P<pending_acknowledgement>\d+)$"
        )

        # Batch begin:   Pending-issue: 0, Pending-acknowledgement: 0
        p2 = re.compile(
            r"^Batch begin:\s+Pending-issue:"
            r"\s+(?P<pending_issue>\d+)\,\s"
            r"Pending-acknowledgement: "
            r"(?P<pending_acknowledgement>\d+)$"
        )

        # Batch end:     Pending-issue: 0, Pending-acknowledgement: 0
        p3 = re.compile(
            r"^Batch end:\s+Pending-issue:"
            r"\s+(?P<pending_issue>\d+)\,\s"
            r"Pending-acknowledgement: "
            r"(?P<pending_acknowledgement>\d+)$"
        )

        # Command:       Pending-acknowledgement: 0
        p4 = re.compile(
            r"^Command:+"
            r"\s+Pending-acknowledgement: "
            r"(?P<pending_acknowledgement>\d+)$"
        )

        # Total-objects: 1401
        p5 = re.compile(r"^Total-objects:" r"\s+(?P<total_objects>\d+)$")

        # Stale-objects: 0
        p6 = re.compile(r"^Stale-objects:" r"\s+(?P<stale_objects>\d+)$")

        # Resolve-objects: 0
        p7 = re.compile(r"^Resolve-objects:" r"\s+(?P<resolve_objects>\d+)$")

        # Childless-delete-objects: 0
        p8 = re.compile(
            r"^Childless-delete-objects:" r"\s+(?P<childless_delete_objects>\d+)$"
        )

        # Backplane-objects: 0
        p9 = re.compile(r"^Backplane-objects:" r"\s+(?P<backplane_objects>\d+)$")

        # Error-objects: 1
        p10 = re.compile(r"^Error-objects:" r"\s+(?P<error_objects>\d+)$")

        # Number of bundles: 136
        p11 = re.compile(r"^Number of bundles:" r"\s+(?P<number_of_bundles>\d+)$")

        # Paused-types: 0
        p12 = re.compile(r"^Paused-types:" r"\s+(?P<paused_types>\d+)$")

        for line in out.splitlines():
            line = line.strip()

            # Object update: Pending-issue: 180, Pending-acknowledgement: 89
            m = p1.match(line)
            if m:
                group = m.groupdict()
                object_update = result_dict.setdefault("object_update", {})
                object_update.update(
                    {
                        "pending_issue": int(group["pending_issue"]),
                        "pending_acknowledgement": int(
                            group["pending_acknowledgement"]
                        ),
                    }
                )
                continue

            # Batch begin:   Pending-issue: 0, Pending-acknowledgement: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                batch_begin = result_dict.setdefault("batch_begin", {})
                batch_begin.update(
                    {
                        "pending_issue": int(group["pending_issue"]),
                        "pending_acknowledgement": int(
                            group["pending_acknowledgement"]
                        ),
                    }
                )
                continue

            # Batch end:     Pending-issue: 0, Pending-acknowledgement: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                batch_end = result_dict.setdefault("batch_end", {})
                batch_end.update(
                    {
                        "pending_issue": int(group["pending_issue"]),
                        "pending_acknowledgement": int(
                            group["pending_acknowledgement"]
                        ),
                    }
                )
                continue

            # Command:       Pending-acknowledgement: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                command = result_dict.setdefault("command", {})
                command.update(
                    {"pending_acknowledgement": int(group["pending_acknowledgement"])}
                )
                continue

            # Total-objects: 1401
            m = p5.match(line)
            if m:
                group = m.groupdict()
                result_dict["total_objects"] = int(group["total_objects"])
                continue

            # Stale-objects: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                result_dict["stale_objects"] = int(group["stale_objects"])
                continue

            # Resolve-objects: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                result_dict["resolve_objects"] = int(group["resolve_objects"])
                continue

            # Childless-delete-objects: 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                result_dict["childless_delete_objects"] = int(
                    group["childless_delete_objects"]
                )
                continue

            # Backplane-objects: 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                result_dict["backplane_objects"] = int(group["backplane_objects"])
                continue

            # Error-objects: 1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                result_dict["error_objects"] = int(group["error_objects"])
                continue

            # Number of bundles: 136
            m = p11.match(line)
            if m:
                group = m.groupdict()
                result_dict["number_of_bundles"] = int(group["number_of_bundles"])
                continue

            # Paused-types: 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                result_dict["paused_types"] = int(group["paused_types"])
                continue

        return result_dict


# =======================================================================
# Schema for 'show platform software object-manager {switch} {switch_type} F0 error-object'
# =======================================================================
class ShowPlatSwObjectManagerF0ErrorObjectSchema(MetaParser):
    """Schema for :
    'show platform software object-manager {switch} {switch_type} F0 error-object'
    'show platform software object-manager F0 error-object'
    """

    schema = {
        "identifier": {
            Any(): {
                Optional("identifier"): int,
                Optional("status"): str,
                Optional("description"): str,
            }
        },
    }


class ShowPlatSwObjectManagerF0ErrorObject(ShowPlatSwObjectManagerF0ErrorObjectSchema):
    """parser for :
    show platform software object-manager {switch} {switch_type} F0 error-object
    show platform software object-manage F0 error-object
    """

    cli_command = [
        "show platform software object-manager F0 error-object",
        "show platform software object-manager {switch} {switch_type} F0 error-object",
    ]

    def cli(self, switch=None, switch_type=None, output=None):
        if output is None:
            if switch and switch_type:
                cmd = self.cli_command[1].format(switch=switch, switch_type=switch_type)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        # Description: PREFIX 2.2.2.2/32 (Table id 1)
        p0 = re.compile(r"^Description:\s+(?P<description>.*).*$")

        # Object identifier: 1515
        p1 = re.compile(r"^Object identifier:\s+(?P<identifier>\d+)$")

        # Status: Create-failed"
        p2 = re.compile(r"Status:\s+(?P<status>\S+)$")

        for line in out.splitlines():
            line = line.strip()

            # Object identifier: 1515
            m = p1.match(line)
            if m:
                group = m.groupdict()
                identifier = group.pop("identifier")

                identifier_dict = result_dict.setdefault("identifier", {})
                n_identifier_dict = identifier_dict.setdefault(int(identifier), {})

                n_identifier_dict.update(
                    {
                        "identifier": int(identifier),
                    }
                )

            # Description: PREFIX 2.2.2.2/32 (Table id 1)
            m = p0.match(line)
            if m:
                group = m.groupdict()
                n_identifier_dict.update({"description": group["description"]})

            # Status: Create-failed"
            m = p2.match(line)
            if m:
                group = m.groupdict()
                n_identifier_dict.update({"status": group["status"]})
        return result_dict


# ============================================================
#  Schema for 'show platform software wired-client switch <state> r0 id <iif_id>'
# ============================================================
class ShowPlatformFedSwitchActiveWiredClientR0IdIifidSchema(MetaParser):
    """Schema for show platform software wired-client switch <state> r0 id <iif_id>
    show platform software wired-client <state> r0 id <iif_id>"""

    schema = {
        "id": str,
        "mac_address": str,
        "physical_interface_dpidx": str,
        "authentication_state": str,
        "vlan_id": str,
        "open_access": str,
        "client_forward": str,
        Optional("dynamic_policy_template"): str,
    }


# ============================================================================
#  Parser for
#  * 'show platform software wired-client switch <state> r0 id <iif_id>'
#  * 'show platform software wired-client <state> r0 id <iif_id>'
# ============================================================================
class ShowPlatformFedSwitchActiveWiredClientR0IdIifid(
    ShowPlatformFedSwitchActiveWiredClientR0IdIifidSchema
):
    """
    Parser for
    * 'show platform software wired-client switch {state} r0 id {iif_id}'
    * 'show platform software wired-client {state} r0 id {iif_id}'
    """

    cli_command = [
        "show platform software wired-client {state} r0 id {iif_id}",
        "show platform software wired-client {switch} {state} r0 id {iif_id}",
    ]

    def cli(self, iif_id, state, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(
                    state=state, switch=switch, iif_id=iif_id
                )
            else:
                cmd = self.cli_command[0].format(state=state, iif_id=iif_id)
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r"^(?P<pattern>[\w\s]+):\s+(?P<value>[\w\s\.]+)$")

        for line in output.splitlines():
            line = line.strip()

            # MAC address                  : 0020.0000.0001
            # Physical interface dpidx     : 0x00000040
            # Authentication state         : L3 Auth
            # VLAN ID                      : 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                scrubbed = (group["pattern"].strip()).replace(" ", "_")
                ret_dict.update({scrubbed.lower(): group["value"]})
                continue

        return ret_dict