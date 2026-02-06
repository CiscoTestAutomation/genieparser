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
    * 'show platform software object-manager FP standby statistics'
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
    * 'show platform software memory database forwarding-manager {slot} active brief | include {options}'
    * 'show platform soft infra bipc | inc buffer'
    * 'show platform software infractructure inject'
    * 'show platform software process list fp active'
    * 'show platform software process list F0 name {process}'
    * 'show platform software process list FP active name {process} '
    * 'show platform software l2vpn fp active atom'
    * 'show platform software adjacency RP active'
    * 'show platform software nat fp active qfp-stats'
    * 'show platform software nat fp active cpp-stats'
    * 'show platform software mpls fp active eos'
    * 'show platform software multicast stats'
    * 'show platform software interface fp active name Port-channel32'
    * 'show platform software nat fp active interface'
    * 'show platform software access-list fp active statistics'
    * 'show platform software nat fp active pool'
    * 'show platform software nat fp active mapping dynamic'
    * 'show platform software memory forwarding-manager F0 brief | include {option}'
    * 'show platform software firewall FP active pairs'
    * show platform software firewall RP active vrf-pmap-binding
    * show platform software firewall FP active vrf-pmap-binding
    * 'show platform software nat ipalias'
    * 'show platform software trace level ios rp active | in pki'
    * 'show platform software firewall RP active zones'
    * 'show platform software firewall FP active zones'
    * 'show platform software nat fp active mapping static'
    * 'show platform software firewall RP active parameter-maps'
    * 'show platform software subslot {subslot} module firmware'
    * 'show platform software bp crimson content oper'
    * 'show platform software audit monitor status'
    * 'show platform software audit ruleset'
    * show platform software firewall qfp active runtime
    * show platform software ip FP active cef summary
    * show platform software adjacency nexthop-ipfrr
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
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, ListOf, Use, And
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
            r"(?P<free>\d+) *free, +(?P<used>\d+) *used, +"
            r"(?P<buff_cache>\d+) *buff\/cache$"
        )

        p2 = re.compile(
            r"^KiB +Swap *: +(?P<total>\d+) *total, +"
            r"(?P<free>\d+) *free, +(?P<used>\d+) *used. +"
            r"(?P<available_memory>\d+) *avail +Mem$"
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
            r"(?P<min1>[\d\.]+) +(?P<min5>[\d\.]+) +(?P<min15>[\d\.]+)$"
        )

        p2 = re.compile(
            r"^(?P<slot>\S+) +(?P<status>\w+) +"
            r"(?P<total>\d+) +(?P<used>\d+) +\((?P<used_percentage>[\d\s]+)\%\) +"
            r"(?P<free>\d+) +\((?P<free_percentage>[\d\s]+)\%\) +"
            r"(?P<committed>\d+) +\((?P<committed_percentage>[\d\s]+)\%\)$"
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
        # *Sep 30 15:56:15.001: %SYS-5-CONFIG_I: Configured from console by consoleConfd Status: Started
        p1 = re.compile(r".*Confd +Status: +(?P<status>.+)$")

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
            r" +(?P<sc_idx>\d+) +\|"
            r" +(?P<pre_cur_an>\d+\/\d+) +\|"
            r" +(?P<sci>\S+) +\|"
            r" +(?P<idx>\d+\/ \d+\/ \d+) +\|"
            r" +(?P<cipher>\S+) +\|"
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
        p3 = re.compile(r"Prev AN\: (?P<prev_an>\d+)\, Cur AN\: (?P<cur_an>\d+)")

        # SA index: 50331759, vport index: 2, rule index: 1
        p4 = re.compile(
            r"SA index\: (?P<sa_index>\d+)\, +"
            r"vport index\: (?P<vport_index>\d+)\, +"
            r"rule index\: (?P<rule_index>\d+)"
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
#  * 'show platform software object-manager FP active pending-ack-update'
# =======================================================================================
class ShowPlatformSoftwareObjectManagerF0PendingAckUpdateSchema(MetaParser):
    """Schema for 'show platform software object-manager {switch} {switch_type} F0 pending-ack-update'
    'show platform software object-manager F0 pending-ack-update'
    'show platform software object-manager FP active pending-ack-update'
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
#  * 'show platform software object-manager FP active pending-ack-update'
# =======================================================================================


class ShowPlatformSoftwareObjectManagerF0PendingAckUpdate(
    ShowPlatformSoftwareObjectManagerF0PendingAckUpdateSchema
):
    """
    Parser for :
        * 'show platform software object-manager {switch} {switch_type} F0 pending-ack-update'
        * 'show platform software object-manager F0 pending-ack-update'
        * 'show platform software object-manager FP active pending-ack-update'
    """

    cli_command = [
        "show platform software object-manager {switch} {switch_type} F0 pending-ack-update",
	"show platform software object-manager F0 pending-ack-update",
        "show platform software object-manager {processor} {type} pending-ack-update",
    ]

    def cli(self, switch_type="", switch="", processor="", type="", output=None):
        if output is None:
            if switch and switch_type:
                output = self.device.execute(
                    self.cli_command[0].format(switch=switch, switch_type=switch_type)
                )
            elif processor and type:
                output = self.device.execute(
                    self.cli_command[2].format(processor=processor, type=type)
                )
            else:
                output = self.device.execute(
                    self.cli_command[1]
                )
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
        p1 = re.compile(r"^(?P<name>\S+)\s+(?P<id>\d+)\s+(?P<qfp_id>\d+)$")

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

    cli_command = ["show platform software cpm switch {mode} BP {mode2} counters drop",
                   "show platform software cpm switch {mode} B0 counters drop"]

    def cli(self, mode,  mode2=None, output=None):

        if output is None:
            if  mode2:
                output = self.device.execute(self.cli_command[0].format(mode=mode, mode2=mode2))
            else:
                output = self.device.execute(self.cli_command[1].format(mode=mode))

        # initial variables
        ret_dict = {}

        # RX unexpected packet count                    311
        p1 = re.compile(r"^(?P<drop_counters>[\w ]+)\s+(?P<drop_count>\d+)$")

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

    cli_command = ['show platform software cpm switch {mode} BP {mode2} counters punt-inject',
                  'show platform software cpm switch {mode} B0 counters punt-inject']

    def cli(self, mode, mode2=None, output=None):

        if output is None:
            if  mode2:
                output = self.device.execute(self.cli_command[0].format(mode=mode, mode2=mode2))
            else:
                output = self.device.execute(self.cli_command[1].format(mode=mode))

        # initial variables
        ret_dict = {}
        temp_dict = {}

        # SVL CTRL           12673           12641                0                15
        p1 = re.compile(
            r"^(?P<traffic_type>\w+\s+\w+)\s+(?P<packets_inject>\d+)\s+(?P<packets_punt>\d+)\s+(?P<drop_inject>\d+)\s+(?P<drop_punt>\d+)$"
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
        p1 = re.compile(r"^cpm-cm\s+(?P<cpm_cm>\w+)$")

        # cpm-fed    connected
        p2 = re.compile(r"^cpm-fed\s+(?P<cpm_fed>\w+)$")

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
        p1 = re.compile(r"^Service:\s+(?P<service>\S+)$")

        # Peer Location: -1
        p2 = re.compile(r"^Peer Location:\s+(?P<peer_location>\S+)$")

        # Peer State: 2
        p3 = re.compile(r"^Peer State:\s+(?P<peer_state>\d+)$")

        # Connection Drops: 0
        p4 = re.compile(r"^Connection Drops:\s+(?P<connection_drops>\d+)$")

        # Flow Control: 0
        p5 = re.compile(r"^Flow Control:\s+(?P<flow_control>\d+)$")

        # Transition Count: 0
        p6 = re.compile(r"^Transition Count:\s+(?P<transition_count>\d+)$")

        # Received Msgs: 1
        p7 = re.compile(r"^Received Msgs:\s+(?P<received_msgs>\d+)$")

        # TDL hdl failure: 0
        p8 = re.compile(r"^TDL hdl failure:\s+(?P<tdl_hdl_failure>\d+)$")

        # Dispatch failures: 1
        p9 = re.compile(r"^Dispatch failures:\s+(?P<dispatch_failures>\d+)$")

        # Rx Other Drops: 0
        p10 = re.compile(r"^Rx Other Drops:\s+(?P<rx_other_drops>\d+)$")

        # Sent msgs: 1
        p11 = re.compile(r"^Sent msgs:\s+(?P<sent_msgs>\d+)$")

        # Tx No Mem failures: 0
        p12 = re.compile(r"^Tx No Mem failures:\s+(?P<tx_no_mem_failures>\d+)$")

        # Tx Other Drops: 0
        p13 = re.compile(r"^Tx Other Drops:\s+(?P<tx_other_drops>\d+)$")

        # Tx No Space failures: 0
        p14 = re.compile(r"^Tx No Space failures:\s+(?P<tx_no_space_failures>\d+)$")

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
                    Optional("preffered_link"): str
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
        p1 = re.compile(r"^System port: (?P<system_port>\d+)$")

        # SVL Control Interface: HundredGigE1/0/2
        p2 = re.compile(r"^SVL Control Interface: (?P<svl_control_interface>\S+)$")

        # 27                  FiftyGigE1/0/56
        p1_2 = re.compile(r"^(?P<system_port>\s*\d+)\s+(?P<svl_control_interface>\S+)$")

        # 0x2c       0x2c     28       etherchannel
        # If Id         Ec If Id           System Port     If Type      Preferred Link
        p3 = re.compile(
            r"^(?P<if_id>\S+)\s+(?P<ec_if_id>\S+)\s+(?P<system_port>\d+)\s+(?P<if_type>\S+)(\s+(?P<preffered_link>\S+))?$"
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
                if group["preffered_link"]:
                    root_dict["preffered_link"] = group["preffered_link"]
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
        p1 = re.compile(r"^oobnd1\s+(?P<oobnd1>UP|DOWN)$")

        # leaba0_3        UP
        p2 = re.compile(r"^leaba0_3\s+(?P<leaba0_3>UP|DOWN)$")

        # leaba0_5        UP
        p3 = re.compile(r"^leaba0_5\s+(?P<leaba0_5>UP|DOWN)$")

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
    * show platform software object-manager FP standby statistics
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
    show platform software object-manager FP standby statisics
    """

    cli_command = [
        "show platform software object-manager switch {switchstate} {serviceprocessor} active statistics",
        "show platform software object-manager FP {processor} statistics",
    ]

    def cli(self, switchstate="", serviceprocessor="", processor="", output=None):
        if output is None:
            if switchstate:
                cmd = self.cli_command[0].format(
                    switchstate=switchstate, serviceprocessor=serviceprocessor
                )
            else:
                cmd = self.cli_command[1].format(processor=processor)

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
            r"^(?P<node>\d+)\s+(?P<domain>\d+)\s+(?P<mode>\w+)(\s+(?P<router_id>\w+))?$"
        )

        # Node    Priority
        # 1       1
        p2 = re.compile(r"^(?P<node>\d+)\s+(?P<priority>\d+)$")

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
        p1 = re.compile(r"^(?P<bp_crimson_statistics>BP Crimson Statistics)$")

        # Regexp  for  all the  lines  which fals in the below  pattern
        # Initialized            : Yes
        p2 = re.compile(r"^(?P<description>[\w'\s]+)\:\s+(?P<value>\w+)$")

        # BP SVL Crimson Statistics
        p3 = re.compile(r"^(?P<bp_svl_crimson_statistics>BP SVL Crimson Statistics)$")

        # BP Remote DB Statistics
        p4 = re.compile(r"^(?P<bp_remote_db_statistics>BP Remote DB Statistics)$")

        # GET Requests:
        p5 = re.compile(r"^(?P<get_requests>GET Requests\:)$")

        # SET Requests:
        p6 = re.compile(r"^(?P<set_requests>SET Requests\:)$")

        # In Progress Requests:
        p7 = re.compile(r"^(?P<in_progress_requests>In Progress Requests\:)$")

        # DBAL Response Time:
        p8 = re.compile(r"^(?P<dbal_response_time>DBAL Response Time\:)$")

        # Record Free Failures:
        p9 = re.compile(r"^(?P<record_free_failures>Record Free Failures\:)$")

        #  MAX (ms)         : 49
        p10 = re.compile(r"^\s*MAX +\(ms\) +\:\s*(?P<max>\d+)$")

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
        # p1 = re.compile(r'^(?P<node_description>[\w\s]+)\: (?P<status>.*)$')
        # Local Node Number: 1
        p1 = re.compile(r"^Local +Node +Number\: +(?P<local_node_number>\d+)$")

        # Node status is: NODE_STATUS_UP
        p2 = re.compile(r"^Node +status +is\: +(?P<node_status_is>.*)$")

        # Tunnel status is: NODE_TUNNEL_UP
        p3 = re.compile(r"^Tunnel +status +is\: +(?P<tunnel_status_is>.*)$")

        # Node role is: CLUSTER_NODE_ROLE_LEADER
        p4 = re.compile(r"^Node +role +is\: +(?P<node_role_is>.*)$")

        # MAC address is : 64 181 193 255 238 0
        p5 = re.compile(r"^MAC +address +is +\: +(?P<mac_address_is>.*)$")

        # Slot number is : 0
        p6 = re.compile(r"^Slot +number +is +\: +(?P<slot_number_is>\d+)$")

        # priority set to: 1
        p7 = re.compile(r"^priority +set +to\: +(?P<priority_set_to>\d+)$")

        # Leader node num is: 1
        p8 = re.compile(r"^Leader +node +num is\: +(?P<leader_node_num_is>\d+)$")

        # Follower node is: 2
        p9 = re.compile(r"^Follower +node +is\: +(?P<follower_node_is>\d+)$")

        # Total node present in cluster: 2
        p10 = re.compile(
            r"^Total +node +present +in +cluster\: +(?P<total_node_present_in_cluster>\d+)$"
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
        p1 = re.compile(r"^(?P<bp_crimson_statistics>BP Crimson Statistics)$")

        # Regexp  for  all the  lines  which fals in the below  pattern
        # Initialized            : Yes
        p2 = re.compile(r"^(?P<description>[\w'\s]+)\:\s+(?P<value>\w+)$")

        # BP SVL Crimson Statistics
        p3 = re.compile(r"^(?P<bp_svl_crimson_statistics>BP SVL Crimson Statistics)$")

        # BP Remote DB Statistics
        p4 = re.compile(r"^(?P<bp_remote_db_statistics>BP Remote DB Statistics)$")

        # GET Requests:
        p5 = re.compile(r"^(?P<get_requests>GET Requests\:)$")

        # SET Requests:
        p6 = re.compile(r"^(?P<set_requests>SET Requests\:)$")

        # In Progress Requests:
        p7 = re.compile(r"^(?P<in_progress_requests>In Progress Requests\:)$")

        # DBAL Response Time:
        p8 = re.compile(r"^(?P<dbal_response_time>DBAL Response Time\:)$")

        # Record Free Failures:
        p9 = re.compile(r"^(?P<record_free_failures>Record Free Failures\:)$")

        #  MAX (ms)         : 49
        p10 = re.compile(r"^\s*MAX +\(ms\) +\:\s*(?P<max>\d+)$")

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
        # p1 = re.compile(r'^(?P<node_description>[\w\s]+)\: (?P<status>.*)$')
        # Local Node Number: 1
        p1 = re.compile(r"^Local +Node +Number\: +(?P<local_node_number>\d+)$")

        # Node status is: NODE_STATUS_UP
        p2 = re.compile(r"^Node +status +is\: +(?P<node_status_is>.*)$")

        # Tunnel status is: NODE_TUNNEL_UP
        p3 = re.compile(r"^Tunnel +status +is\: +(?P<tunnel_status_is>.*)$")

        # Node role is: CLUSTER_NODE_ROLE_LEADER
        p4 = re.compile(r"^Node +role +is\: +(?P<node_role_is>.*)$")

        # MAC address is : 64 181 193 255 238 0
        p5 = re.compile(r"^MAC +address +is +\: +(?P<mac_address_is>.*)$")

        # Slot number is : 0
        p6 = re.compile(r"^Slot +number +is +\: +(?P<slot_number_is>\d+)$")

        # priority set to: 1
        p7 = re.compile(r"^priority +set +to\: +(?P<priority_set_to>\d+)$")

        # Leader node num is: 1
        p8 = re.compile(r"^Leader +node +num is\: +(?P<leader_node_num_is>\d+)$")

        # Follower node is: 2
        p9 = re.compile(r"^Follower +node +is\: +(?P<follower_node_is>\d+)$")

        # Total node present in cluster: 2
        p10 = re.compile(
            r"^Total +node +present +in +cluster\: +(?P<total_node_present_in_cluster>\d+)$"
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

    cli_command = ["show platform software access-list F0 summary", 
                   "show platform software access-list {switch} {mode} F0 summary"]

    def cli(self, switch=None, mode='active', output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

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


# ======================================================
# Parser for 'show platform software access-list fp active summary'
# ======================================================


class ShowPlatformSoftwareAccessListFpActiveSummarySchema(MetaParser):
    """Schema for show platform software access-list fp active summary"""

    schema = {
        "access_list": {
            Any(): {
                "index": int,
                "num_ref": int,
                "num_aces": int,
            }
        }
    }


class ShowPlatformSoftwareAccessListFpActiveSummary(
    ShowPlatformSoftwareAccessListFpActiveSummarySchema
):
    """Parser for show platform software access-list {fp} {active} summary"""

    cli_command = "show platform software access-list {fp} {active} summary"

    def cli(self, fp="fp", active="active", output=None):
        if output is None:
            cmd = self.cli_command.format(fp=fp, active=active)
            output = self.device.execute(cmd)

        # implicit_deny_v6                     5            0            1  
        p1 = re.compile(r"^(?P<access_list_name>\S+)\s+(?P<index>\d+)\s+(?P<num_ref>\d+)\s+(?P<num_aces>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            
            # preauth_v4                           2            0            6            
            m = p1.match(line)
            if m:
                group = m.groupdict()
                access_list_name = group["access_list_name"]
                
                access_list_dict = ret_dict.setdefault("access_list", {}).setdefault(access_list_name, {})
                access_list_dict["index"] = int(group["index"])
                access_list_dict["num_ref"] = int(group["num_ref"])
                access_list_dict["num_aces"] = int(group["num_aces"])
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
    """Schema for show platform software cpm switch active B0 counters interface lacp"""

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

    cli_command = ['show platform software cpm switch {mode} BP {mode2} counters interface lacp',
                   'show platform software cpm switch {mode} B0 counters interface lacp']

    def cli(self, mode, mode2=None, output=None):

        if output is None:
            if mode2:
                output = self.device.execute(self.cli_command[0].format(mode=mode,mode2=mode2))
            else:
                output = self.device.execute(self.cli_command[1].format(mode=mode))

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

    cli_command = ['show platform software cpm switch {mode} BP {mode2} counters interface isis',
                   'show platform software cpm switch {mode} B0 counters interface isis']

    def cli(self, mode,  mode2=None, output=None):

        if output is None:
            if  mode2:
                output = self.device.execute(self.cli_command[0].format(mode=mode, mode2=mode2))
            else:
                output = self.device.execute(self.cli_command[1].format(mode=mode))

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

class ShowPlatformSoftwareInterfaceF0NameSchema(MetaParser):
    """
    Schema for show platform software interface f0 name {intf}
    """

    schema = {
            "name": str,
            "id": int,
            "qfp_id": int,
            Optional("schedules"): int,
            Optional("type"): str,
            Optional("state"): str,
            Optional("snmp_id"): int,
            Optional("mtu"): int,
            "tx_channel_id": int,
            "rx_channel_id": int,
            "aom_state": str,
            "flow_control_id": int,
            "bandwidth": int,
            "encap": str,
            "ip_address": str,
            "ipv6_address": str,
            Optional("icmp_flags"): list,
            Optional("icmp6_flags"): list,
            Optional("smi_protocols"): list,
            "auth_user": str,
            "frr_linkdown_id": int,
            "vnet_name": str,
            "vnet_tag": int,
            "vnet_extra_info": int,
            "dirty_status": str,
            "aom_sanity_check": str,
            "aom_obj_id": int,
            "qos_trust_type": str,
            Optional("flags"): str
          }

class ShowPlatformSoftwareInterfaceF0Name(ShowPlatformSoftwareInterfaceF0NameSchema):
    """Parser for show platform software interface f0 name {intf}"""

    cli_command = "show platform software interface f0 name {intf}"

    def cli(self, intf=None, output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command.format(intf=intf))

        # initial variables
        ret_dict = {}
        # Name: HundredGigE2/0/22, ID: 1275, QFP ID: 1275, Schedules: 4096
        p0 = re.compile(r"^Name: +(?P<name>\S+),\s+ID: +(?P<id>\d+),\s+QFP ID: +(?P<qfp_id>\d+),\s+Schedules: +(?P<schedules>\d+)$")

        # Type: PORT, State: enabled, SNMP ID: 98, MTU: 1500
        p1 = re.compile(r"^Type: +(?P<type>\w+),\s+State: +(?P<state>\w+),\s+SNMP ID: +(?P<snmp_id>\d+),\s+MTU: +(?P<mtu>\d+)$")

        # TX channel ID: 0, RX channel ID: 0, AOM state: created
        p2 = re.compile(r"^TX channel ID: +(?P<tx_channel_id>\d+),\s+RX channel ID: +(?P<rx_channel_id>\d+),\s+AOM state: +(?P<aom_state>\w+)$")

        # Flow control ID: 49175
        p3 = re.compile(r"^Flow control ID: +(?P<flow_control_id>\d+)$")

        # bandwidth: 100000000, encap: ARPA
        p4 = re.compile(r"^bandwidth: +(?P<bandwidth>\d+),\s+encap: +(?P<encap>\w+)$")

        # IP Address: 10.10.10.96
        p5 = re.compile(r"^IP Address: +(?P<ip_address>(\d{1,3}\.){3}\d{1,3})$")

        # IPV6 Address: ::
        p6 = re.compile(r"^IPV6 Address: +(?P<ipv6_address>[\da-fA-F:]+)$")

        # Flags: ipv4
        p7 = re.compile(r"^Flags: +(?P<flags>[\w\s]+)$")

        # ICMP Flags: unreachables, redirects, no-info-reply, no-mask-reply
        p8 = re.compile(r"^ICMP Flags: +(?P<icmp_flags>[\w\s,-]+)$")

        # ICMP6 Flags: unreachables, redirects
        p9 = re.compile(r"^ICMP6 Flags: +(?P<icmp6_flags>[\w\s,-]+)$")

        # SMI enabled on protocol(s): UNKNOWN
        p10 = re.compile(r"^SMI enabled on protocol\(s\): +(?P<smi_protocols>[\w\s,-]+)$")

        # Authenticated-user:
        p11 = re.compile(r"^Authenticated-user: *(?P<auth_user>.*)$")

        # FRR linkdown ID: 65535
        p12 = re.compile(r"^FRR linkdown ID: +(?P<frr_linkdown_id>\d+)$")

        # vNet Name: , vNet Tag: 0, vNet Extra Information: 0
        p13 = re.compile(r"^vNet Name: *(?P<vnet_name>.*),\s+vNet Tag: +(?P<vnet_tag>\d+),\s+vNet Extra Information: +(?P<vnet_extra_info>\d+)$")

        # Dirty: unknown
        p14 = re.compile(r"^Dirty: +(?P<dirty_status>\w+)$")

        # AOM dependency sanity check: PASS
        p15 = re.compile(r"^AOM dependency sanity check: +(?P<aom_sanity_check>\w+)$")

        # AOM Obj ID: 2071
        p16 = re.compile(r"^AOM Obj ID: +(?P<aom_obj_id>\d+)$")

        # QOS trust type: Trust DSCP
        p17 = re.compile(r"^QOS trust type: +(?P<qos_trust_type>[\w\s]+)$")

        for line in output.splitlines():
            line = line.strip()

            # Name: HundredGigE2/0/22, ID: 1275, QFP ID: 1275, Schedules: 4096
            m = p0.match(line)
            if m:
                group = m.groupdict()
                ret_dict["name"] = group["name"]
                ret_dict["id"] = int(group["id"])
                ret_dict["qfp_id"] = int(group["qfp_id"])
                ret_dict["schedules"] = int(group["schedules"])
                continue

            # Type: PORT, State: enabled, SNMP ID: 98, MTU: 1500
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["type"] = group["type"]
                ret_dict["state"] = group["state"]
                ret_dict["snmp_id"] = int(group["snmp_id"])
                ret_dict["mtu"] = int(group["mtu"])
                continue

            # TX channel ID: 0, RX channel ID: 0, AOM state: created
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["tx_channel_id"] = int(group["tx_channel_id"])
                ret_dict["rx_channel_id"] = int(group["rx_channel_id"])
                ret_dict["aom_state"] = group["aom_state"]
                continue

            # Flow control ID: 49175
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict["flow_control_id"] = int(group["flow_control_id"])
                continue

            # bandwidth: 100000000, encap: ARPA
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["bandwidth"] = int(group["bandwidth"])
                ret_dict["encap"] = group["encap"]
                continue

            # IP Address: 10.10.10.96
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict["ip_address"] = group["ip_address"]
                continue

            # IPV6 Address: ::
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict["ipv6_address"] = group["ipv6_address"]
                continue

            # Flags: ipv4
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict["flags"] = group["flags"]
                continue

            # ICMP Flags: unreachables, redirects, no-info-reply, no-mask-reply
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict["icmp_flags"] = group["icmp_flags"].split(", ")
                continue

            # ICMP6 Flags: unreachables, redirects
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict["icmp6_flags"] = group["icmp6_flags"].split(", ")
                continue

            # SMI enabled on protocol(s): UNKNOWN
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict["smi_protocols"] = group["smi_protocols"].split(", ")
                continue

            # Authenticated-user:
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict["auth_user"] = group["auth_user"]
                continue

            # FRR linkdown ID: 65535
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict["frr_linkdown_id"] = int(group["frr_linkdown_id"])
                continue

            # vNet Name: , vNet Tag: 0, vNet Extra Information: 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict["vnet_name"] = group["vnet_name"]
                ret_dict["vnet_tag"] = int(group["vnet_tag"])
                ret_dict["vnet_extra_info"] = int(group["vnet_extra_info"])
                continue

            # Dirty: unknown
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict["dirty_status"] = group["dirty_status"]
                continue

            # AOM dependency sanity check: PASS
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ret_dict["aom_sanity_check"] = group["aom_sanity_check"]
                continue

            # AOM Obj ID: 2071
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ret_dict["aom_obj_id"] = int(group["aom_obj_id"])
                continue
            # QOS trust type: Trust DSCP
            m = p17.match(line)
            if m:
                group = m.groupdict()
                ret_dict["qos_trust_type"] = group["qos_trust_type"]
                continue

        return ret_dict

class ShowPlatformSoftwareObjectManagerF0ObjectIdentifierSchema(MetaParser):
    """Schema for show platform software object-manager f0 object {object} {object_identifier}"""

    schema = {
        "object_identifier": {
            Any(): {
                Optional("object_identifier"): int,
                Optional("status"): str,
                Optional("description"): str,
            }
        },
    }

class ShowPlatformSoftwareObjectManagerF0ObjectIdentifier(
    ShowPlatformSoftwareObjectManagerF0ObjectIdentifierSchema
):
    """Parser for show platform software object-manager f0 object {object} {object_identifier}"""

    cli_command = "show platform software object-manager f0 object {object} {object_identifier}"

    def cli(self, object=None, object_identifier=None, output=None):
        if output is None:
            if object and object_identifier:
                # excute command to get output
                output = self.device.execute(self.cli_command.format(object=object,object_identifier=object_identifier))

        # Init vars
        ret_dict = {}

        # Object identifier: 2072
        p0 = re.compile(r"^Object identifier\:\s+(?P<object_identifier>\d+)$")

        # Description: Tx Channel HundredGigE2/0/22, handle 1275, hw handle 1275, flag 0x0, dirty hw: NONE dirty aom NONE
        p1 = re.compile(r"^Description\:\s+(?P<description>.+)$")

        # Status: Done
        p2 = re.compile(r"Status\:\s+(?P<status>\w+)$")

        for line in output.splitlines():
            line = line.strip()

            # Object identifier: 2072
            m = p0.match(line)
            if m:
                group = m.groupdict()
                object_identifier = group.pop("object_identifier")
                identifier_dict = ret_dict.setdefault("object_identifier", {})
                obj_identifier_dict = identifier_dict.setdefault(int(object_identifier), {})
                obj_identifier_dict.update(
                    {
                        "object_identifier": int(object_identifier),
                    }
                )
                continue

            # Description: Tx Channel HundredGigE2/0/22, handle 1275, hw handle 1275, flag 0x0, dirty hw: NONE dirty aom NONE
            m = p1.match(line)
            if m:
                group = m.groupdict()
                obj_identifier_dict.update({"description": group["description"]})
                continue

            # Status: Done
            m = p2.match(line)
            if m:
                group = m.groupdict()
                obj_identifier_dict.update({"status": group["status"]})
                continue

        return ret_dict


class ShowPlatsoftwaremcuversionSchema(MetaParser):
    """show platform software mcu  switch  1 R0 version  0"""

    schema = {
        'switch_number': int,
        'software_version': str,
        'system_type': int,
        'device_id': int,
        'device_revision': int,
        'hardware_version': int,
        'bootloader_version': int,
        }

class ShowPlatsoftwaremcuversion(ShowPlatsoftwaremcuversionSchema):
    """
    show platform software mcu  switch  1 R0 version  0
    """

    cli_command = 'show platform software mcu switch {switch_num} {route_processor} version 0'


    def cli(self, switch_num, route_processor, output=None):

        if output is None:

                output = self.device.execute(self.cli_command.format(switch_num=switch_num,route_processor=route_processor))

        ret_dict = {}

        # Switch 1 MCU
        p1 = re.compile(r'^Switch +(?P<switch_number>\d+) +MCU\:$')

        # Software Version   0.0
        p2 =  re.compile(r'^Software +Version +(?P<software_version>.*)$')

        # System Type        0
        p3 = re.compile(r'^System +Type +(?P<system_type>.*)$')

        # Device Id          0
        p4 = re.compile(r'^Device +Id +(?P<device_id>.*)$')

        # Device Revision    0
        p5 = re.compile(r'^Device +Revision +(?P<device_revision>.*)$')

        # Hardware Version   0
        p6 = re.compile(r'^Hardware +Version +(?P<hardware_version>.*)$')

        # Bootloader Version 0
        p7 = re.compile(r'^Bootloader +Version +(?P<bootloader_version>.*)$')

        for line in output.splitlines():
            line = line.strip()

            # Switch 1 MCU
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['switch_number'] = int(group['switch_number'])
                continue

            # Software Version   0.0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['software_version'] = group['software_version']
                continue

            # System Type        0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['system_type'] = int(group['system_type'])
                continue

            # Device Id          0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['device_id'] = int(group['device_id'])
                continue

            # Device Revision    0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict['device_revision'] = int(group['device_revision'])
                continue

            # Hardware Version   0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict['hardware_version'] = int(group['hardware_version'])
                continue

            # Bootloader Version 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict['bootloader_version'] = int(group['bootloader_version'])
                continue

        return ret_dict


class ShowPlatsoftwaremcusubordinateSchema(MetaParser):
    """show platform software mcu  switch  1 R0 version  0"""

    schema = {
        'showing_sub_info': int,
        'state': str,
        'last_reset_reason': str,
        'uart_fe_error': int,
        'uart_pe_error': int,
        'uart_dor_error': int,
        'rx_buf_overflow': int,
        'rx_buf_underflow': int,
        'tx_buf_full': int,
        'rx_bad_endbyte': int,
        'ple_invalid_app': int,
        'ple_disabled_app': int,
        'ple_invalid_data': int,
        'ple_invalid_flags': int,
        'ple_app_error': int,
        'ple_lost_ctxt': int,
        'ple_invalid_reg': int,
        'ple_invalid_reg_len': int,
        'ple_invalid_msg_len': int,
        'sle_poe_no_port': int,
        'sle_invalid_reg_len': int,
        'sle_msg_underrun': int,
        }

class ShowPlatsoftwaremcusubordinate(
    ShowPlatsoftwaremcusubordinateSchema):
    """
    show platform software mcu  switch  1 R0 version  0
    """

    cli_command = 'show platform software mcu switch {switch_num} {route_processor} subordinate 0'

    def cli(self, switch_num, route_processor, output=None):

        if output is None:

                output = self.device.execute(self.cli_command.format(switch_num=switch_num,route_processor=route_processor))

        ret_dict = {}

        # showing sub info:    1
        p1 = re.compile(r'^showing +sub +info\: +(?P<showing_sub_info>.*)$')

        # State                OK
        p2 =  re.compile(r'^State +(?P<state>.*)$')

        # Last Reset Reason    UNKNOWN REASON
        p3 = re.compile(r'^Last +Reset +Reason +(?P<last_reset_reason>.*)$')

        # UART FE Error        0
        p4 = re.compile(r'^UART +FE +Error +(?P<uart_fe_error>\d+)$')

        # UART PE Error        0
        p5 = re.compile(r'^UART +PE +Error +(?P<uart_pe_error>\d+)$')

        # UART DOR Error       0
        p6 = re.compile(r'^UART +DOR +Error +(?P<uart_dor_error>\d+)$')

        # Rx Buf Overflow      0
        p7 = re.compile(r'^Rx +Buf +Overflow +(?P<rx_buf_overflow>\d+)$')

        # Rx Buf Underflow      0
        p8 = re.compile(r'^Rx +Buf +Underflow +(?P<rx_buf_underflow>\d+)$')

        # Tx Buf Full          0
        p9 = re.compile(r'^Tx +Buf +Full +(?P<tx_buf_full>\d+)$')

        # Rx Bad Endbyte       0
        p10 = re.compile(r'^Rx +Bad +Endbyte +(?P<rx_bad_endbyte>\d+)$')

        # PLE Invalid App      0
        p11 = re.compile(r'^PLE +Invalid +App +(?P<ple_invalid_app>\d+)$')

        # PLE Disabled App     0
        p12 = re.compile(r'^PLE +Disabled +App +(?P<ple_disabled_app>\d+)$')

        # PLE Invalid Data     0
        p13 = re.compile(r'^PLE +Invalid +Data +(?P<ple_invalid_data>\d+)$')

        # PLE Invalid Flags    0
        p14 = re.compile(r'^PLE +Invalid +Flags +(?P<ple_invalid_flags>\d+)$')

        # PLE App Error        0
        p15 = re.compile(r'^PLE +App +Error +(?P<ple_app_error>\d+)$')

        # PLE Lost Ctxt        0
        p16 = re.compile(r'^PLE +Lost +Ctxt +(?P<ple_lost_ctxt>\d+)$')

        # PLE Invalid Reg      0
        p17 = re.compile(r'^PLE +Invalid +Reg +(?P<ple_invalid_reg>\d+)$')

        # PLE Invalid Reg Len  0
        p18 = re.compile(r'^PLE +Invalid +Reg +Len +(?P<ple_invalid_reg_len>\d+)$')

        # PLE Invalid Msg Len  0
        p19 = re.compile(r'^PLE +Invalid +Msg +Len +(?P<ple_invalid_msg_len>\d+)$')

        # SLE Poe No Port      0
        p20 = re.compile(r'^SLE +Poe +No +Port +(?P<sle_poe_no_port>\d+)$')

        # SLE Invalid Reg Len  0
        p21 = re.compile(r'^SLE +Invalid +Reg +Len +(?P<sle_invalid_reg_len>\d+)$')

        # SLE Msg Underrun     0
        p22 = re.compile(r'^SLE +Msg +Underrun +(?P<sle_msg_underrun>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # showing sub info:    1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['showing_sub_info'] = int(group['showing_sub_info'])
                continue

            # State                OK
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['state'] = group['state']
                continue

            # Last Reset Reason    UNKNOWN REASON
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['last_reset_reason'] = group['last_reset_reason']
                continue

            # UART FE Error        0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['uart_fe_error'] = int(group['uart_fe_error'])
                continue

            # UART PE Error        0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict['uart_pe_error'] = int(group['uart_pe_error'])
                continue

            # UART DOR Error       0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict['uart_dor_error'] = int(group['uart_dor_error'])
                continue

            # Rx Buf Overflow      0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_buf_overflow'] = int(group['rx_buf_overflow'])
                continue

            # Rx Buf Underflow      0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_buf_underflow'] = int(group['rx_buf_underflow'])
                continue

            # Tx Buf Full          0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_buf_full'] = int(group['tx_buf_full'])
                continue

            # Rx Bad Endbyte       0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_bad_endbyte'] = int(group['rx_bad_endbyte'])
                continue

            # PLE Invalid App      0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict['ple_invalid_app'] = int(group['ple_invalid_app'])
                continue

            # PLE Disabled App     0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict['ple_disabled_app'] = int(group['ple_disabled_app'])
                continue

            # PLE Invalid Data     0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict['ple_invalid_data'] = int(group['ple_invalid_data'])
                continue

            # PLE Invalid Flags    0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict['ple_invalid_flags'] = int(group['ple_invalid_flags'])
                continue

            # PLE App Error        0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ret_dict['ple_app_error'] = int(group['ple_app_error'])
                continue

            # PLE Lost Ctxt        0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ret_dict['ple_lost_ctxt'] = int(group['ple_lost_ctxt'])
                continue

            # PLE Invalid Reg      0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                ret_dict['ple_invalid_reg'] = int(group['ple_invalid_reg'])
                continue

            # PLE Invalid Reg Len  0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                ret_dict['ple_invalid_reg_len'] = int(group['ple_invalid_reg_len'])
                continue

            # PLE Invalid Msg Len  0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                ret_dict['ple_invalid_msg_len'] = int(group['ple_invalid_msg_len'])
                continue

            # SLE Poe No Port      0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                ret_dict['sle_poe_no_port'] = int(group['sle_poe_no_port'])
                continue

            # SLE Invalid Reg Len  0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                ret_dict['sle_invalid_reg_len'] = int(group['sle_invalid_reg_len'])
                continue

            # SLE Msg Underrun     0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                ret_dict['sle_msg_underrun'] = int(group['sle_msg_underrun'])
                continue

        return ret_dict


class ShowPlatformSoftwareInfrastructureInjectSchema(MetaParser):
    schema = {
        'l3_injected_packets': {
            Optional('total_inject'): int,
            Optional('failed_inject'): int,
            Optional('sent'): int,
            Optional('prerouted'): int,
            Optional('non_cef_capable'): int,
            Optional('non_unicast'): int,
            Optional('ip'): int,
            Optional('ipv6'): int,
            Optional('mpls'): int,
            Optional('non_ip_tunnel'): int,
            Optional('udlr_tunnel'): int,
            Optional('p2mp_replicated_mcast'): int,
            Optional('non_ip_fastswitched_over_tunnel'): int,
            Optional('legacy_pak_path'): int,
            Optional('other_packet'): int,
            Optional('ip_fragmented'): int,
            Optional('normal'): int,
            Optional('nexthop'): int,
            Optional('adjacency'): int,
            Optional('feature'): int,
            Optional('undefined'): int,
            Optional('pak_find_no_adj'): int,
            Optional('no_adj_id'): int,
            Optional('sb_alloc'): int,
            Optional('sb_local'): int,
            Optional('p2mcast_failed_count_0_p2mcast_enqueue_fail'): int,
            Optional('unicast_dhc'): int,
            Optional('mobile_ip'): int,
            Optional('ipv6_na'): int,
            Optional('ipv6_ns'): int,
            Optional('transport_failed_cases'): int,
            Optional('grow_packet_buffer'): int,
            Optional('cant_l3_inject_pkts'): int,
        },
        'per_feature_packet_inject_statistics': {
            Optional('feature_multicast'): int,
            Optional('feature_edge_switching_service'): int,
            Optional('feature_session_border_controller'): int,
            Optional('feature_interrupt_level'): int,
            Optional('feature_use_outbound_interface'): int,
            Optional('feature_interrupt_level_with_oce'): int,
            Optional('feature_icmpv6_error_message'): int,
            Optional('feature_session_border_controller_media_packet_injection'): int,
            Optional('feature_tunnel_ethernet_over_gre'): int,
            Optional('feature_secure_socket_layer_virtual_private_network'): int,
            Optional('feature_epc_wireshark_injecting_packets'): int,
            Optional('feature_multicast_overlay_replication'): int,
        },
        'l2_injected_packets': {
            Optional('total_l2_inject'): int,
            Optional('total_bd__inject'): int,
            Optional('total_bd_local__inject'): int,
            Optional('total_efp_inject'): int,
            Optional('total_vlan_inject'): int,
            Optional('failed_l2_inject'): int,
            Optional('failed_bd_local__inject'): int,
            Optional('failed_bd__inject'): int,
            Optional('failed_vlan_inject'): int,
            Optional('failed_efp_inject'): int,
        }
    }

class ShowPlatformSoftwareInfrastructureInject(ShowPlatformSoftwareInfrastructureInjectSchema):
    cli_command = 'show platform software infrastructure inject'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the result dictionary as empty
        parsed_dict = {}

        # 3524142 total inject pak, 0 failed
        p1 = re.compile(r'^(?P<total>\d+) total (?P<type>[\w\s\-]+) pak, (?P<failed>\d+) failed$')

        #  0 Feature multicast overlay replication
        p2 = re.compile(r'^(?P<value>\d+) (?P<key>[\w\s\-]+)$')

        #  0 MPLS, 0 Non-IP Tunnel
        p3 = re.compile(r'^(?P<value1>\d+) (?P<key1>[\w\s\-]+), (?P<value2>\d+) (?P<key2>[\w\s\-]+)$')

        # Statistics for L2 injected packets:
        p4 = re.compile(r'^(?P<key>[\w\s\-]+):$')

        # Track sections
        current_section = None

        for line in output.splitlines():
            line = line.strip()

            # Statistics for L2 injected packets:
            if 'Statistics for L3 injected packets' in line:
                current_section = 'l3_injected_packets'
                parsed_dict[current_section] = {}
                continue
            elif 'per feature packet inject statistics' in line:
                current_section = 'per_feature_packet_inject_statistics'
                parsed_dict[current_section] = {}
                continue
            elif 'Statistics for L2 injected packets' in line:
                current_section = 'l2_injected_packets'
                parsed_dict[current_section] = {}
                continue

            if current_section is None:
                continue

            # 28324 total L2 inject pak, 0 failed
            m = p1.match(line)
            if m:
                group = m.groupdict()
                key = group['type'].strip().lower().replace(' ', '_').replace('-', '_')
                parsed_dict[current_section][f'total_{key}'] = int(group['total'])
                parsed_dict[current_section][f'failed_{key}'] = int(group['failed'])
                continue

            # 0 Feature multicast overlay replication
            m = p2.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].strip().lower().replace(' ', '_').replace('-', '_')
                value = int(group['value'])
                parsed_dict[current_section][key] = value
                continue

            #  1023352 sb alloc, 135 sb local
            m = p3.match(line)
            if m:
                group = m.groupdict()
                key1 = group['key1'].strip().lower().replace(' ', '_').replace('-', '_')
                key2 = group['key2'].strip().lower().replace(' ', '_').replace('-', '_')
                value1 = int(group['value1'])
                value2 = int(group['value2'])
                parsed_dict[current_section][key1] = value1
                parsed_dict[current_section][key2] = value2
                continue

        return parsed_dict



class ShowPlatsoftwaremcumanagerSchema(MetaParser):
    """show platform software mcu  switch  1 R0 version  0"""

    schema = {
        'showing_manager_info': int,
        'tx_cmd_cnt_sys_app_1': int,
        'rx_cmd_cnt_sys_app_1': int,
        'tx_cmd_ignore_sys_app_1': int,
        'tx_cmd_q_full_sys_app_1': int,
        Optional('tx_cmd_cnt_sys_app_2'): int,
        Optional('rx_cmd_cnt_sys_app_2'): int,
        Optional('tx_cmd_ignore_sys_app_2'): int,
        Optional('tx_cmd_q_full_sys_app_2'): int,
        Optional('tx_cmd_cnt_sys_app_3'): int,
        Optional('rx_cmd_cnt_sys_app_3'): int,
        Optional('tx_cmd_ignore_sys_app_3'): int,
        Optional('tx_cmd_q_full_sys_app_3'): int,
        'tx_cmd_cnt_therm_app': int,
        'rx_cmd_cnt_therm_app': int,
        'tx_cmd_ignore_therm_app': int,
        'tx_cmd_q_full_therm_app': int,
        'tx_cmd_cnt_gpio_app':int,
        'rx_cmd_cnt_gpio_app':int,
        'tx_cmd_ignore_gpio_app':int,
        'tx_cmd_q_full_gpio_app':int,
        'tx_cmd_cnt_poe_app': int,
        'rx_cmd_cnt_poe_app': int,
        'tx_cmd_ignore_poe_app': int,
        'tx_cmd_q_full_poe_app': int,
        'tx_cmd_cnt_image_app': int,
        'rx_cmd_cnt_image_app': int,
        'tx_cmd_ignore_image_app': int,
        'tx_cmd_q_full_image_app': int,
        'tx_cmd_cnt_stackpower_app': int,
        'rx_cmd_cnt_stackpower_app': int,
        'tx_cmd_ignore_stackpower_app': int,
        'tx_cmd_q_full_stackpower_app': int,
        'tx_cmd_cnt_frufep_app': int,
        'rx_cmd_cnt_frufep_app': int,
        'tx_cmd_ignore_frufep_app': int,
        'tx_cmd_q_full_frufep_app': int,
        'tx_cmd_cnt_poe_ext_app': int,
        'rx_cmd_cnt_poe_ext_app': int,
        'tx_cmd_ignore_poe_ext_app': int,
        'tx_cmd_q_full_poe_ext_app': int,
        'tx_cmd_cnt_j2a_app': int,
        'rx_cmd_cnt_j2a_app': int,
        'tx_cmd_ignore_j2a_app': int,
        'tx_cmd_q_full_j2a_app': int,
        'tx_cmd_cnt_dsmg_app': int,
        'rx_cmd_cnt_dsmg_app': int,
        'tx_cmd_ignore_dsmg_app': int,
        'tx_cmd_q_full_dsmg_app': int,
        Optional('tx_cmd_cnt_sys_app_4'): int,
        Optional('rx_cmd_cnt_sys_app_4'): int,
        Optional('tx_cmd_ignore_sys_app_4'): int,
        Optional('tx_cmd_q_full_sys_app_4'): int,
        'tx_reg_cnt': int,
        'rx_reg_cnt': int,
        'tx_reg_ignore': int,
        'tx_reg_q_full': int,
        'rx_invalid_frame': int,
        'rx_invalid_app': int,
        'rx_invalid_seq': int ,
        'rx_invalid_checksum': int,
        'nack_cnt': int,
        'send_break_count': int,
        'early_send_break_count': int,
        'retransmission_cnt': int,
        }

class ShowPlatsoftwaremcumanager(ShowPlatsoftwaremcumanagerSchema):
    """
    show platform software mcu switch 1 R0 manager 0
    """

    cli_command = 'show platform software mcu switch {switch_num} R0 manager 0'

    def cli(self, switch_num, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_num=switch_num))

        ret_dict = {}

        #showing manager info: 1
        p1 = re.compile(r'^showing +manager +info\: +(?P<showing_manager_info>.*)$')

        #Tx cmd cnt   SYS App              0
        p2 =  re.compile(r'^Tx +cmd +cnt +SYS +App +(?P<tx_cmd_cnt_sys_app>.*)$')

        #Rx cmd cnt   SYS App              0
        p3 = re.compile(r'^Rx +cmd +cnt +SYS +App +(?P<rx_cmd_cnt_sys_app>.*)$')

        #Tx cmd ignore   SYS App           0
        p4 = re.compile(r'^Tx +cmd +ignore +SYS +App +(?P<tx_cmd_ignore_sys_app>.*)$')

        #Tx cmd Q full   SYS App           0
        p5 = re.compile(r'^Tx +cmd +Q +full +SYS +App +(?P<tx_cmd_q_full_sys_app>.*)$')

        #Tx cmd cnt   POE App              0
        p6 = re.compile(r'^Tx +cmd +cnt +POE +App +(?P<tx_cmd_cnt_poe_app>.*)$')

        #Rx cmd cnt   POE App              0
        p7 = re.compile(r'^Rx +cmd +cnt +POE +App +(?P<rx_cmd_cnt_poe_app>.*)$')

        #Tx cmd ignore   POE App           0
        p8 = re.compile(r'^Tx +cmd +ignore +POE +App+(?P<tx_cmd_ignore_poe_app>.*)$')

        #Tx cmd Q full   POE App           0
        p9 = re.compile(r'^Tx +cmd +Q +full +POE +App +(?P<tx_cmd_q_full_poe_app>.*)$')

        #Tx cmd cnt FRUFEP App              0
        p10 = re.compile(r'^Tx +cmd +cnt +FRUFEP +App +(?P<tx_cmd_cnt_frufep_app>.*)$')

        #Rx cmd cnt FRUFEP App              0
        p11 = re.compile(r'^Rx +cmd +cnt +FRUFEP +App +(?P<rx_cmd_cnt_frufep_app>.*)$')

        #Tx cmd ignore FRUFEP App           0
        p12 = re.compile(r'^Tx +cmd +ignore +FRUFEP +App +(?P<tx_cmd_ignore_frufep_app>.*)$')

        #Tx cmd Q full FRUFEP App           0
        p13 = re.compile(r'^Tx +cmd +Q +full +FRUFEP +App +(?P<tx_cmd_q_full_frufep_app>.*)$')

        #Tx cmd cnt IMAGE App              0
        p14 = re.compile(r'^Tx +cmd +cnt +IMAGE +App +(?P<tx_cmd_cnt_image_app>.*)$')

        #Rx cmd cnt IMAGE App              0
        p15 = re.compile(r'^Rx +cmd +cnt +IMAGE +App +(?P<rx_cmd_cnt_image_app>.*)$')

        #Tx cmd ignore IMAGE App           0
        p16 = re.compile(r'^Tx +cmd +ignore +IMAGE +App +(?P<tx_cmd_ignore_image_app>.*)$')

        #Tx cmd Q full IMAGE App           0
        p17 = re.compile(r'^Tx +cmd +Q +full +IMAGE +App +(?P<tx_cmd_q_full_image_app>.*)$')

        #Tx cmd cnt STACKPOWER App              0
        p18 = re.compile(r'^Tx +cmd +cnt +STACKPOWER +App +(?P<tx_cmd_cnt_stackpower_app>.*)$')

        #Rx cmd cnt STACKPOWER App              0
        p19 = re.compile(r'^Rx +cmd +cnt +STACKPOWER +App +(?P<rx_cmd_cnt_stackpower_app>.*)$')

        #Tx cmd ignore STACKPOWER App           0
        p20 = re.compile(r'^Tx +cmd +ignore +STACKPOWER +App +(?P<tx_cmd_ignore_stackpower_app>.*)$')

        #Tx cmd Q full STACKPOWER App           0
        p21 = re.compile(r'^Tx +cmd +Q +full +STACKPOWER +App +(?P<tx_cmd_q_full_stackpower_app>.*)$')

        #Tx cmd cnt   J2A App              0
        p22 = re.compile(r'^Tx +cmd +cnt +J2A +App +(?P<tx_cmd_cnt_j2a_app>.*)$')

        #Rx cmd cnt   J2A App              0
        p23 = re.compile(r'^Rx +cmd +cnt +J2A +App +(?P<rx_cmd_cnt_j2a_app>.*)$')

        #Tx cmd ignore   J2A App           0
        p24 = re.compile(r'^Tx +cmd +ignore +J2A +App +(?P<tx_cmd_ignore_j2a_app>.*)$')

        #Tx cmd Q full   J2A App           0
        p25 = re.compile(r'^Tx +cmd +Q +full +J2A +App +(?P<tx_cmd_q_full_j2a_app>.*)$')

        #Tx cmd cnt THERM App              0
        p26 = re.compile(r'^Tx +cmd +cnt +THERM +App +(?P<tx_cmd_cnt_therm_app>.*)$')

        #Rx cmd cnt THERM App              0
        p27 = re.compile(r'^Rx +cmd +cnt +THERM +App +(?P<rx_cmd_cnt_therm_app>.*)$')

        #Tx cmd ignore THERM App           0
        p28 = re.compile(r'^Tx +cmd +ignore +THERM +App +(?P<tx_cmd_ignore_therm_app>.*)$')

        #Tx cmd Q full THERM App           0
        p29 = re.compile(r'^Tx +cmd +Q +full +THERM +App +(?P<tx_cmd_q_full_therm_app>.*)$')

        #Tx reg cnt                        2
        p30 = re.compile(r'^Tx +reg +cnt +(?P<tx_reg_cnt>.*)$')

        #Rx reg cnt                        0
        p31 = re.compile(r'^Rx +reg +cnt +(?P<rx_reg_cnt>.*)$')

        #Tx reg ignore                     2
        p32 = re.compile(r'^Tx +reg +ignore +(?P<tx_reg_ignore>\d+)$')

        #Tx reg Q full                     0
        p33 = re.compile(r'^Tx +reg +Q full +(?P<tx_reg_q_full>\d+)$')

        #Rx invalid frame                  2
        p34 = re.compile(r'^Rx +invalid +frame +(?P<rx_invalid_frame>\d+)$')

        #Rx invalid App                    0
        p35 = re.compile(r'^Rx +invalid +App +(?P<rx_invalid_app>\d+)$')

        #Rx invalid Seq                    0
        p36 = re.compile(r'^Rx +invalid +Seq +(?P<rx_invalid_seq>\d+)$')

        #Rx invalid checksum               0
        p37 = re.compile(r'^Rx +invalid +checksum +(?P<rx_invalid_checksum>\d+)$')

        #Nack cnt                          0
        p38 = re.compile(r'^Nack +cnt +(?P<nack_cnt>\d+)$')

        #Send Break count                  0
        p39 = re.compile(r'^Send +Break +count +(?P<send_break_count>\d+)$')

        #Early Send Break count            0
        p40 = re.compile(r'^Early +Send +Break +count +(?P<early_send_break_count>\d+)$')

        #Retransmission cnt                0
        p41 = re.compile(r'^Retransmission +cnt +(?P<retransmission_cnt>\d+)$')

        #Tx cmd cnt  GPIO App              0
        p42 = re.compile(r'^Tx +cmd +cnt +GPIO +App +(?P<tx_cmd_cnt_gpio_app>.*)$')

        #Rx cmd cnt  GPIO App              0
        p43 = re.compile(r'^Rx +cmd +cnt +GPIO +App +(?P<rx_cmd_cnt_gpio_app>.*)$')

        #Tx cmd ignore  GPIO App           0
        p44 = re.compile(r'^Tx +cmd +ignore +GPIO +App +(?P<tx_cmd_ignore_gpio_app>.*)$')

        #Tx cmd Q full  GPIO App           0
        p45 = re.compile(r'^Tx +cmd +Q +full +GPIO +App +(?P<tx_cmd_q_full_gpio_app>.*)$')

        #Tx cmd cnt POE_EXT App              0
        p46 = re.compile(r'^Tx +cmd +cnt +POE_EXT +App +(?P<tx_cmd_cnt_poe_ext_app>.*)$')

        #Rx cmd cnt POE_EXT App              0
        p47 = re.compile(r'^Rx +cmd +cnt +POE_EXT +App +(?P<rx_cmd_cnt_poe_ext_app>.*)$')

        #Tx cmd ignore POE_EXT App           0
        p48 = re.compile(r'^Tx +cmd +ignore +POE_EXT +App +(?P<tx_cmd_ignore_poe_ext_app>.*)$')

        #Tx cmd Q full POE_EXT App           0
        p49 = re.compile(r'^Tx +cmd +Q +full +POE_EXT +App +(?P<tx_cmd_q_full_poe_ext_app>.*)$')

        #Tx cmd cnt DMSG App              0
        p50 = re.compile(r'^Tx +cmd +cnt +DMSG +App +(?P<tx_cmd_cnt_dsmg_app>.*)$')

        #Rx cmd cnt DMSG App              0
        p51 = re.compile(r'^Rx +cmd +cnt +DMSG +App +(?P<rx_cmd_cnt_dsmg_app>.*)$')

        #Tx cmd ignore DMSG App           0
        p52 = re.compile(r'^Tx +cmd +ignore +DMSG +App +(?P<tx_cmd_ignore_dsmg_app>.*)$')

        #Tx cmd Q full DMSG App           0
        p53 = re.compile(r'^Tx +cmd +Q +full +DMSG +App +(?P<tx_cmd_q_full_dsmg_app>.*)$')

        i = j = k = l = 0

        for line in output.splitlines():
            line = line.strip()

            # showing manager info: 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['showing_manager_info'] = int(group['showing_manager_info'])
                continue

            # Tx cmd cnt   SYS App              0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                i = i + 1
                temp_val = 'tx_cmd_cnt_sys_app_'+str(i)
                ret_dict[temp_val] = int(group['tx_cmd_cnt_sys_app'])
                continue

            # Rx cmd cnt   SYS App              0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                j = j + 1
                temp_val = 'rx_cmd_cnt_sys_app_'+str(j)
                ret_dict[temp_val] = int(group['rx_cmd_cnt_sys_app'])
                continue

            # Tx cmd ignore   SYS App           0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                k = k + 1
                temp_val = 'tx_cmd_ignore_sys_app_'+str(k)
                ret_dict[temp_val] = int(group['tx_cmd_ignore_sys_app'])
                continue

            # Tx cmd Q full   SYS App           0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                l = l + 1
                temp_val = 'tx_cmd_q_full_sys_app_'+str(l)
                ret_dict[temp_val] = int(group['tx_cmd_q_full_sys_app'])
                continue

            # Tx cmd cnt   POE App              0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_cnt_poe_app'] = int(group['tx_cmd_cnt_poe_app'])
                continue

            # Rx cmd cnt   POE App              0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_cmd_cnt_poe_app'] = int(group['rx_cmd_cnt_poe_app'])
                continue

            # Tx cmd ignore   POE App           0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_ignore_poe_app'] = int(group['tx_cmd_ignore_poe_app'])
                continue

            # Tx cmd Q full   POE App           0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_q_full_poe_app'] = int(group['tx_cmd_q_full_poe_app'])
                continue

            # Tx cmd cnt FRUFEP App              0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_cnt_frufep_app'] = int(group['tx_cmd_cnt_frufep_app'])
                continue

            # Rx cmd cnt FRUFEP App              0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_cmd_cnt_frufep_app'] = int(group['rx_cmd_cnt_frufep_app'])
                continue

            # Tx cmd ignore FRUFEP App           0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_ignore_frufep_app'] = int(group['tx_cmd_ignore_frufep_app'])
                continue

            # Tx cmd Q full FRUFEP App           0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_q_full_frufep_app'] = int(group['tx_cmd_q_full_frufep_app'])
                continue

            # Tx cmd cnt IMAGE App              0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_cnt_image_app'] = int(group['tx_cmd_cnt_image_app'])
                continue

            # Rx cmd cnt IMAGE App              0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_cmd_cnt_image_app'] = int(group['rx_cmd_cnt_image_app'])
                continue

            # Tx cmd ignore IMAGE App           0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_ignore_image_app'] = int(group['tx_cmd_ignore_image_app'])
                continue

            # Tx cmd Q full IMAGE App           0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_q_full_image_app'] = int(group['tx_cmd_q_full_image_app'])
                continue

            # Tx cmd cnt STACKPOWER App              0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_cnt_stackpower_app'] = int(group['tx_cmd_cnt_stackpower_app'])
                continue

            # Rx cmd cnt STACKPOWER App              0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_cmd_cnt_stackpower_app'] = int(group['rx_cmd_cnt_stackpower_app'])
                continue

            # Tx cmd ignore STACKPOWER App           0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_ignore_stackpower_app'] = int(group['tx_cmd_ignore_stackpower_app'])
                continue

            # Tx cmd Q full STACKPOWER App           0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_q_full_stackpower_app'] = int(group['tx_cmd_q_full_stackpower_app'])
                continue

            # Tx cmd cnt   J2A App              0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_cnt_j2a_app'] = int(group['tx_cmd_cnt_j2a_app'])
                continue

            # Rx cmd cnt   J2A App              0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_cmd_cnt_j2a_app'] = int(group['rx_cmd_cnt_j2a_app'])
                continue

            # Tx cmd ignore   J2A App           0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_ignore_j2a_app'] = int(group['tx_cmd_ignore_j2a_app'])
                continue

            # Tx cmd Q full   J2A App           0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_q_full_j2a_app'] = int(group['tx_cmd_q_full_j2a_app'])
                continue

            # Tx cmd cnt THERM App              0
            m = p26.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_cnt_therm_app'] = int(group['tx_cmd_cnt_therm_app'])
                continue

            # Rx cmd cnt THERM App              0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_cmd_cnt_therm_app'] = int(group['rx_cmd_cnt_therm_app'])
                continue

            # Tx cmd ignore THERM App           0
            m = p28.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_ignore_therm_app'] = int(group['tx_cmd_ignore_therm_app'])
                continue

            # Tx cmd Q full THERM App           0
            m = p29.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_q_full_therm_app'] = int(group['tx_cmd_q_full_therm_app'])
                continue

            # Tx reg cnt                        2
            m = p30.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_reg_cnt'] = int(group['tx_reg_cnt'])
                continue

            # Rx reg cnt                        0
            m = p31.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_reg_cnt'] = int(group['rx_reg_cnt'])
                continue

            # Tx reg ignore                     2
            m = p32.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_reg_ignore'] = int(group['tx_reg_ignore'])
                continue

            # Tx reg Q full                     0
            m = p33.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_reg_q_full'] = int(group['tx_reg_q_full'])
                continue

            # Rx invalid frame                  2
            m = p34.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_invalid_frame'] = int(group['rx_invalid_frame'])
                continue

            # Rx invalid App                    0
            m = p35.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_invalid_app'] = int(group['rx_invalid_app'])
                continue

            # Rx invalid Seq                    0
            m = p36.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_invalid_seq'] = int(group['rx_invalid_seq'])
                continue

            # Rx invalid checksum               0
            m = p37.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_invalid_checksum'] = int(group['rx_invalid_checksum'])
                continue

            # Nack cnt                          0
            m = p38.match(line)
            if m:
                group = m.groupdict()
                ret_dict['nack_cnt'] = int(group['nack_cnt'])
                continue

            # Send Break count                  0
            m = p39.match(line)
            if m:
                group = m.groupdict()
                ret_dict['send_break_count'] = int(group['send_break_count'])
                continue

            # Early Send Break count            0
            m = p40.match(line)
            if m:
                group = m.groupdict()
                ret_dict['early_send_break_count'] = int(group['early_send_break_count'])
                continue

            # Retransmission cnt                0
            m = p41.match(line)
            if m:
                group = m.groupdict()
                ret_dict['retransmission_cnt'] = int(group['retransmission_cnt'])
                continue

            # Tx cmd cnt  GPIO App              0
            m = p42.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_cnt_gpio_app'] = int(group['tx_cmd_cnt_gpio_app'])
                continue

            # Rx cmd cnt  GPIO App              0
            m = p43.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_cmd_cnt_gpio_app'] = int(group['rx_cmd_cnt_gpio_app'])
                continue

            # Tx cmd ignore  GPIO App           0
            m = p44.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_ignore_gpio_app'] = int(group['tx_cmd_ignore_gpio_app'])
                continue

            # Tx cmd Q full  GPIO App           0
            m = p45.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_q_full_gpio_app'] = int(group['tx_cmd_q_full_gpio_app'])
                continue

            # Tx cmd cnt POE_EXT App              0
            m = p46.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_cnt_poe_ext_app'] = int(group['tx_cmd_cnt_poe_ext_app'])
                continue

            # Rx cmd cnt POE_EXT App              0
            m = p47.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_cmd_cnt_poe_ext_app'] = int(group['rx_cmd_cnt_poe_ext_app'])
                continue

            # Tx cmd ignore POE_EXT App           0
            m = p48.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_ignore_poe_ext_app'] = int(group['tx_cmd_ignore_poe_ext_app'])
                continue

            # Tx cmd Q full POE_EXT App           0
            m = p49.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_q_full_poe_ext_app'] = int(group['tx_cmd_q_full_poe_ext_app'])
                continue

            # Tx cmd cnt DMSG App              0
            m = p50.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_cnt_dsmg_app'] = int(group['tx_cmd_cnt_dsmg_app'])
                continue

            # Rx cmd cnt DMSG App              0
            m = p51.match(line)
            if m:
                group = m.groupdict()
                ret_dict['rx_cmd_cnt_dsmg_app'] = int(group['rx_cmd_cnt_dsmg_app'])
                continue

            # Tx cmd ignore DMSG App           0
            m = p52.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_ignore_dsmg_app'] = int(group['tx_cmd_ignore_dsmg_app'])
                continue

            # Tx cmd Q full DMSG App           0
            m = p53.match(line)
            if m:
                group = m.groupdict()
                ret_dict['tx_cmd_q_full_dsmg_app'] = int(group['tx_cmd_q_full_dsmg_app'])
                continue

        return ret_dict


class ShowPlatformSoftwareWiredClientIDSchema(MetaParser):
    """Schema for show platform software wired-client {client_id}"""
    schema = {
        'wired_client': {
            Any(): {
                'id': str,
                'mac': str,
                'fwd': str,
                'open_access': str
            }
        }
    }

class ShowPlatformSoftwareWiredClientID(ShowPlatformSoftwareWiredClientIDSchema):
    """Parser for show platform software wired-client {client_id}"""

    cli_command = "show platform software wired-client {client_id}"

    def cli(self, client_id, output=None):
        if output is None:
            cmd = self.cli_command.format(client_id=client_id)
            output = self.device.execute(cmd)

        # Final dict to return
        parsed_output = {}

        # Regular expression pattern
        # ID  MAC Address     Fwd    Open Access
        # 0x15be62c3  00a3.d1f3.d9eb  Yes    No
        p1 = re.compile(r'^(?P<id>0x[a-fA-F0-9]+)\s+(?P<mac_address>[0-9a-fA-F\.]+)\s+(?P<fwd>\w+)\s+(?P<open_access>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # ID  MAC Address     Fwd    Open Access
            # 0x15be62c3  00a3.d1f3.d9eb  Yes    No
            m = p1.match(line)
            if m:
                group = m.groupdict()
                client_id = group['id']
                clients = parsed_output.setdefault('wired_client', {})
                clients[client_id] = {
                    'id': client_id,
                    'mac': group['mac_address'],
                    'fwd': group['fwd'],
                    'open_access': group['open_access']
                }

        return parsed_output
        
        
class ShowPlatsoftwaremcusnapshotSchema(MetaParser):
    """show platform software mcu  switch  1 R0 version  0"""

    schema = {
        'fast_poe_power_budget': int,
        'load_shed_info': {
            'top': int,
            'wrap_around': int,
            'invalid_load_shed_info': str,
        },
        'mcu_snapshot_data': {
            'manufacturing_config': {
                Any(): Or(int,str),
            },
            'user_config': {
                Any(): Or(int,str)
            },
            'red_earth_data': {
                Any(): Or(int,str),
            },
            'i2c_data': {
                Any(): int,
            },
            'load_shed_registers': {
                Any() : Or(int,str),
            },
        },    
        'register_value': {
            Any() : Or(int,str),
            },    
        } 
        
class ShowPlatsoftwaremcusnapshot(ShowPlatsoftwaremcusnapshotSchema):
    """
    show platform software mcu switch {switch_num} {route-processor} snapshot_detail display
    """
    
    cli_command = 'show platform software MCU switch {switch_num} {routeprocessor} snapshot_detail display' 
                    

    def cli(self, switch_num, routeprocessor, output=None): 

        if output is None:            
           
            output = self.device.execute(self.cli_command.format(switch_num=switch_num, routeprocessor=routeprocessor))  
                
        ret_dict = {}
                
        # Fast PoE power budget: 0
        p1 = re.compile(r'^Fast +PoE +power +budget\: +(?P<fast_poe_power_budget>\d+)$')
        
        # Load Shed info:
        p2 =  re.compile(r'^Load +Shed +info\:$')        
                
        # TOP: 1, wrap around : 0 
        p3 = re.compile(r'^TOP\: +(?P<top>\d+)\, +wrap +around +\: +(?P<wrap_around>\d+)$')  

        # Got invalid load shed info
        # 0x00
        p4 = re.compile(r'^(?P<invalid_load_shed_info>(0x\w+){1})$')
         
        # Manufacturing Config
        p5 = re.compile(r'^Manufacturing +Config$')
        
        # User Config                           
        p6 = re.compile(r'^User +Config$') 
        
        # Red Earth data
        p7 = re.compile(r'^Red +Earth +data$')

        # I2C data         
        p8 = re.compile(r'^I2C +data$')  
        
        # Load Shed Registers      
        p9 = re.compile(r'^Load +Shed +Registers$')  
        
        # acmy_cfg0                   : 0xc0          
        # Lo POE load shed priority   : 0
        # Power stack mode            : STK_PWR_POWER_SHARING_MODE_STRICT 
        # mac address                 : aa:bb:cc:dd:ee:ff 
        p10 = re.compile(r'^(?P<key>[\w\s]+):\s+(?P<value>0x[\w\d]+|\d{1,3}|\w[\w:\-]+)') 
        
        # 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00
        p11 = re.compile(r'^(?P<registers>(?:0x[0-9A-Fa-f]{2}\s*){3,})$')    
        
        count  = regflag = 0    
        
        for line in output.splitlines():
            line = line.strip()
            
            # Fast PoE power budget: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['fast_poe_power_budget'] = int(group['fast_poe_power_budget'])               
                continue  
            
            # Load Shed info:
            m = p2.match(line)
            if m:                
                curr_dict  = ret_dict.setdefault('load_shed_info',{}) 
                continue 
                
            # TOP: 1, wrap around : 0     
            m = p3.match(line)
            if m:                
                group = m.groupdict()
                curr_dict['top'] = int(group['top'])
                curr_dict['wrap_around'] = int(group['wrap_around'])
                continue 
            
            # Got invalid load shed info
            # 0x00 
            m = p4.match(line)
            if m:
                group = m.groupdict()
                curr_dict['invalid_load_shed_info'] = group['invalid_load_shed_info']         
                continue     
            
            # Manufacturing Config
            m = p5.match(line)
            if m:
                group = m.groupdict()
                curr_dict =  ret_dict.setdefault('mcu_snapshot_data', {}).setdefault('manufacturing_config', {})
                continue
                
            # User Config          
            m = p6.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('mcu_snapshot_data', {}).setdefault('user_config', {})               
                continue
                
            # Red Earth data
            m = p7.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('mcu_snapshot_data', {}).setdefault('red_earth_data', {})              
                continue
                
            # I2C data    
            m = p8.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('mcu_snapshot_data', {}).setdefault('i2c_data', {})                
                continue 
                
            # Load Shed Registers  
            m = p9.match(line)
            if m:
                group = m.groupdict()
                curr_dict = ret_dict.setdefault('mcu_snapshot_data', {}).setdefault('load_shed_registers', {})                
                continue
                    
            # acmy_cfg0                   : 0xc0          
            # Lo POE load shed priority   : 0
            # Power stack mode            : STK_PWR_POWER_SHARING_MODE_STRICT 
            # mac address                 : aa:bb:cc:dd:ee:ff 
            m = p10.match(line)
            if m:
                group = m.groupdict()                
                key = m.group('key').strip().replace(' ', '_').lower()
                value = m.group('value')
                try:
                    value = int(value)
                except ValueError:
                    pass
                curr_dict[key] = value    
                continue
                
            # 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    
            m = p11.match(line)
            if m: 
                #ForkedPdb().set_trace()
                group = m.groupdict()
                count = count  + 1
                if regflag == 0:
                    curr_dict = ret_dict.setdefault('register_value', {})
                curr_dict[count] = group['registers']  
                regflag = 1
                continue                
           
        return ret_dict                        

class ShowPlatformSoftwareRouteMapSchema(MetaParser):
    """Schema for show platform software route-map R0 map"""
    schema = {
        'route_map': {
            Any(): {
                'permit': bool,
                'sequence': int,
                'match_clauses': {
                    'ip_address': str
                },
                'set_clauses': {
                    'ipv4_nexthop': str,
                    'table_id': int,
                    'set_force': bool
                }
            }
        }
    }

class ShowPlatformSoftwareRouteMap(ShowPlatformSoftwareRouteMapSchema):
    """Parser for show platform software route-map R0 map"""

    cli_command = 'show platform software route-map R0 map'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # route-map AAA, permit, sequence 100
        p1 = re.compile(r'^route-map +(?P<route_map>\S+), +(?P<permit>\S+), +sequence +(?P<sequence>\d+)$')

        # ip address (access-lists): 101
        p2 = re.compile(r'^ip address \(access-lists\): +(?P<ip_address>\S+)$')

        # ipv4 nexthop: 10.0.0.1, table_id 0
        p3 = re.compile(r'^ipv4 nexthop: +(?P<ipv4_nexthop>\S+), +table_id +(?P<table_id>\d+)$')

        # set force: False
        p4 = re.compile(r'^set force: +(?P<set_force>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # route-map AAA, permit, sequence 100
            m = p1.match(line)
            if m:
                group = m.groupdict()
                route_map = group['route_map']
                permit = group['permit'] == 'permit'
                sequence = int(group['sequence'])
                route_map_dict = ret_dict.setdefault('route_map', {}).setdefault(route_map, {})
                route_map_dict.update({
                    'permit': permit,
                    'sequence': sequence
                })
                continue

            # ip address (access-lists): 101
            m = p2.match(line)
            if m:
                group = m.groupdict()
                route_map_dict.setdefault('match_clauses', {}).update({
                    'ip_address': group['ip_address']
                })
                continue

            # ipv4 nexthop: 10.0.0.1, table_id 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                route_map_dict.setdefault('set_clauses', {}).update({
                    'ipv4_nexthop': group['ipv4_nexthop'],
                    'table_id': int(group['table_id'])
                })
                continue

            # set force: False
            m = p4.match(line)
            if m:
                group = m.groupdict()
                route_map_dict.setdefault('set_clauses', {}).update({
                    'set_force': group['set_force'] == 'True'
                })
                continue

        return ret_dict

"""
Schema for show platform software process list fp active
"""
class ShowPlatformSoftwareProcessListFpActiveSchema(MetaParser):
    """Schema for show platform software process list fp active"""
    schema = {
        'processes': {
            Any(): {
                'pids' : {
                    Any() : {
                        'ppid': int,
                        'group_id': int,
                        'status': str,
                        'priority': str,
                        'size': int,
                    }
                }
            }
        }
    }
 
"""
Schema for show platform software process list fp active
"""
class ShowPlatformSoftwareProcessListFpActive(ShowPlatformSoftwareProcessListFpActiveSchema):
    """Parser for show platform software process list fp active"""

    cli_command = 'show platform software process list fp active'

    def cli(self, output=None):
        if output is None:
            # Execute the command on the device
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        #Name                     Pid    PPid  Group Id  Status    Priority  Size
        #------------------------------------------------------------------------------
        #systemd                    1       0         1  S               20  13636
        p1 = re.compile(
            r'^(?P<name>\S+)\s+(?P<pid>\d+)\s+(?P<ppid>\d+)\s+(?P<group_id>\d+)\s+(?P<status>\S+)\s+(?P<priority>\S+)\s+(?P<size>\d+)'
        )

        lines = output.splitlines()
        # Skip the header lines
        lines = lines[2:]

        for line in lines:

            line = line.strip()

            # Extract the process details
            #systemd                    1       0         1  S               20  13636
            m = p1.match(line)
            if not m:
                continue  # Skip lines that don't match

            process_info = m.groupdict()
            name = process_info['name']
            pid = int(process_info['pid'])
            ppid = int(process_info['ppid'])
            group_id = int(process_info['group_id'])
            status = process_info['status']
            priority = process_info['priority']
            size = int(process_info['size'])

            # Add the process details to the parsed dictionary
            #systemd                    1       0         1  S               20  13636
            processes_dict = parsed_dict.setdefault('processes',{})
            name_dict = processes_dict.setdefault(name,{})
            pid_dict = name_dict.setdefault('pids',{})
            sub_pid_dict = pid_dict.setdefault(pid,{})
            sub_pid_dict.update({  
                'ppid': ppid,
                'group_id': group_id,
                'status': status,
                'priority': priority,
                'size': size,
            })

        return parsed_dict


"""
Schema for show platform software process list F0 name {process}
"""
class ShowPlatformSoftwareProcessListF0NameSchema(MetaParser):
    """Schema for show platform software process list F0 name {process}"""
    schema = {
        'processes': {
            Any(): {  # Process name
                'process_id': int,
                'parent_process_id': int,
                'group_id': int,
                'status': str,
                'session_id': int,
                'user_time': int,
                'kernel_time': int,
                'priority': int,
                'virtual_bytes': int,
                'resident_pages': int,
                'resident_limit': int,
                'minor_page_faults': int,
                'major_page_faults': int,
            }
        }
    }

"""
Schema for show platform software process list F0 name {process}
"""
class ShowPlatformSoftwareProcessListF0Name(ShowPlatformSoftwareProcessListF0NameSchema):
    """Parser for show platform software process list F0 name {process}"""

    cli_command = 'show platform software process list F0 name {process}'

    def cli(self, process, output=None):
        if output is None:
            cmd = self.cli_command.format(process=process)
            output = self.device.execute(cmd)

        # Initialize the parsed dictionary
        parsed_dict ={}

        # Regular expressions for parsing the output
        #Name: fman_rp
        p1 = re.compile(r'^Name:\s+(?P<name>\S+)$')

        #Process id       : 5116
        p2 = re.compile(r'^\s*Process id\s+:\s+(?P<process_id>\d+)$')

        #Parent process id: 5049
        p3 = re.compile(r'^\s*Parent process id\s*:\s+(?P<parent_process_id>\d+)$')

        #Group id         : 5116
        p4 = re.compile(r'^\s*Group id\s+:\s+(?P<group_id>\d+)$')

        #Status           : S
        p5 = re.compile(r'^\s*Status\s+:\s+(?P<status>\S+)$')

        #Session id       : 2811
        p6 = re.compile(r'^\s*Session id\s+:\s+(?P<session_id>\d+)$')

        #User time        : 780
        p7 = re.compile(r'^\s*User time\s+:\s+(?P<user_time>\d+)$')

        #Kernel time      : 588
        p8 = re.compile(r'^\s*Kernel time\s+:\s+(?P<kernel_time>\d+)$')

        #Priority         : 20
        p9 = re.compile(r'^\s*Priority\s+:\s+(?P<priority>\d+)$')

        #Virtual bytes    : 316301312
        p10 = re.compile(r'^\s*Virtual bytes\s+:\s+(?P<virtual_bytes>\d+)$')

        #Resident pages   : 22976
        p11 = re.compile(r'^\s*Resident pages\s+:\s+(?P<resident_pages>\d+)$')

        #Resident limit   : 18446744073709551615
        p12 = re.compile(r'^\s*Resident limit\s+:\s+(?P<resident_limit>\d+)$')

        #Minor page faults: 24680
        p13 = re.compile(r'^\s*Minor page faults\s*:\s+(?P<minor_page_faults>\d+)$')

        #Major page faults: 914
        p14 = re.compile(r'^\s*Major page faults\s*:\s+(?P<major_page_faults>\d+)$')

        current_process = None

        for line in output.splitlines():
            line = line.strip()

            # Match each line with the appropriate regex
            #Name: fman_rp
            m = p1.match(line)
            if m:
                parsed_dict.setdefault('processes', {})
                current_process = m.group('name')
                parsed_dict['processes'][current_process] = {}
                continue

            #Process id       : 5116
            m = p2.match(line)
            if m:
                parsed_dict['processes'][current_process]['process_id'] = int(m.group('process_id'))
                continue

            #Parent process id: 5049
            m = p3.match(line)
            if m:
                parsed_dict['processes'][current_process]['parent_process_id'] = int(m.group('parent_process_id'))
                continue
            
            #Group id         : 5116
            m = p4.match(line)
            if m:
                parsed_dict['processes'][current_process]['group_id'] = int(m.group('group_id'))
                continue

            #Status           : S
            m = p5.match(line)
            if m:
                parsed_dict['processes'][current_process]['status'] = m.group('status')
                continue

            #Session id       : 2811
            m = p6.match(line)
            if m:
                parsed_dict['processes'][current_process]['session_id'] = int(m.group('session_id'))
                continue

            #User time        : 780
            m = p7.match(line)
            if m:
                parsed_dict['processes'][current_process]['user_time'] = int(m.group('user_time'))
                continue

            #Kernel time      : 588
            m = p8.match(line)
            if m:
                parsed_dict['processes'][current_process]['kernel_time'] = int(m.group('kernel_time'))
                continue

            #Priority         : 20
            m = p9.match(line)
            if m:
                parsed_dict['processes'][current_process]['priority'] = int(m.group('priority'))
                continue

            #Virtual bytes    : 316301312
            m = p10.match(line)
            if m:
                parsed_dict['processes'][current_process]['virtual_bytes'] = int(m.group('virtual_bytes'))
                continue

            #Resident pages   : 22976
            m = p11.match(line)
            if m:
                parsed_dict['processes'][current_process]['resident_pages'] = int(m.group('resident_pages'))
                continue

            #Resident limit   : 18446744073709551615
            m = p12.match(line)
            if m:
                parsed_dict['processes'][current_process]['resident_limit'] = int(m.group('resident_limit'))
                continue

            #Minor page faults: 24680
            m = p13.match(line)
            if m:
                parsed_dict['processes'][current_process]['minor_page_faults'] = int(m.group('minor_page_faults'))
                continue

            #Major page faults: 914
            m = p14.match(line)
            if m:
                parsed_dict['processes'][current_process]['major_page_faults'] = int(m.group('major_page_faults'))
                continue

        return parsed_dict

# =====================================
# Parser for 'show platform software process list FP active name {process}'
# =====================================
class ShowPlatformSoftwareProcessListFPActiveName(ShowPlatformSoftwareProcessListF0Name):

    """ Parser for "show platform software process list FP active name {process}" """
    cli_command = 'show platform software process list FP active name {process}'

    def cli(self, process, output = None):
        if output is None:
            cmd = self.cli_command.format(process=process)
            show_output = self.device.execute(cmd)
        else:
            show_output = output
        return super().cli(process=process, output = show_output)

class ShowPlatformSoftwareL2vpnFpActiveAtomSchema(MetaParser):
    """Schema for show platform software l2vpn fp active atom"""
    schema = {
        'num_of_entries': int,
        'entries': {
            Any(): {
                'xid': str,
                'ifnumber': str,
                'ac_type': str,
                'imp': str,
                'hw_info': str,
                'interface_name': str,
                Optional('vlan_info'): {
                    'out_vlan_id': int,
                    'in_vlan_id': int,
                    'out_ether': str,
                    'peer_vlan_id': int,
                    'dot1q_any': int,
                }
            }
        }
    }

class ShowPlatformSoftwareL2vpnFpActiveAtom(ShowPlatformSoftwareL2vpnFpActiveAtomSchema):
    """Parser for show platform software l2vpn fp active atom"""

    cli_command = 'show platform software l2vpn fp active atom'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # ATOM/Local Cross-connect table, Number of entries: 1
        p1 = re.compile(r'^ATOM/Local Cross-connect table, Number of entries:\s(?P<num_of_entries>\d+)$')
        
        # AToM Cross-Connect xid 0x1c, ifnumber 0x1c
        p2 = re.compile(r'^AToM Cross-Connect xid (?P<xid>0x[0-9a-f]+), ifnumber (?P<ifnumber>0x[0-9a-f]+)$')
        
        # AC VLAN(IW:VLAN) -> Imp 0xb4(ATOM_IMP), HW info: 1c (om_id 314 created)
        p3 = re.compile(r'^AC (?P<ac_type>\S+)\(IW:\S+\) -> Imp (?P<imp>0x[0-9a-f]+)\(ATOM_IMP\), HW info: (?P<hw_info>\S+)')
        
        # Interface Name: GigabitEthernet0/0/8.100
        p4 = re.compile(r'^Interface Name: (?P<interface_name>\S+)$')
        
        # VLAN Info: outVlan id: 100, inVlan id: 100, outEther: 0x8100, peerVlan id: 100, dot1qAny: 0
        p5 = re.compile(r'^VLAN Info: outVlan id: (?P<out_vlan_id>\d+), inVlan id: (?P<in_vlan_id>\d+), outEther: (?P<out_ether>0x[0-9a-f]+), peerVlan id: (?P<peer_vlan_id>\d+), dot1qAny: (?P<dot1q_any>\d+)$')

        # Parse each line of the output
        for line in output.splitlines():
            line = line.strip()

            # ATOM/Local Cross-connect table, Number of entries: 1
            m = p1.match(line)
            if m:
                parsed_dict['num_of_entries'] = int(m.group('num_of_entries'))
                continue
            
            # AToM Cross-Connect xid 0x1c, ifnumber 0x1c
            m = p2.match(line)
            if m:
                entry = m.groupdict()
                xid = entry['xid']
                entry_dict = parsed_dict.setdefault('entries', {}).setdefault(xid, {})
                entry_dict.update(entry)
                continue

            # AC VLAN(IW:VLAN) -> Imp 0xb4(ATOM_IMP), HW info: 1c (om_id 314 created)
            m = p3.match(line)
            if m:
                entry_dict.update(m.groupdict())
                continue

            # Interface Name: GigabitEthernet0/0/8.100
            m = p4.match(line)
            if m:
                entry_dict['interface_name'] = m.group('interface_name')
                continue

            # VLAN Info: outVlan id: 100, inVlan id: 100, outEther: 0x8100, peerVlan id: 100, dot1qAny: 0
            m = p5.match(line)
            if m:
                vlan_info = m.groupdict()
                # Convert numeric fields to integers
                for key in ['out_vlan_id', 'in_vlan_id', 'peer_vlan_id', 'dot1q_any']:
                    vlan_info[key] = int(vlan_info[key])
                entry_dict['vlan_info'] = vlan_info
                continue

        return parsed_dict

class ShowPlatformSoftwareAdjacencyRpActiveSchema(MetaParser):
    """Schema for show platform software adjacency RP active"""
    schema = {
        'number_of_adjacency_objects': int,
        'adjacencies': {
            int: {
                'adjacency_id': str,
                'interface': str,
                'if_index': int,
                'link_type': str,
                'encap': str,
                'encap_length': int,
                'encap_type': str,
                'mtu': int,
                'flags': str,
                'incomplete_behavior_type': str,
                'fixup': str,
                'fixup_flags_2': str,
                'nexthop_addr': str,
                'ip_frr': str,
                'om_handle': str,
            }
        }
    }

class ShowPlatformSoftwareAdjacencyRpActive(ShowPlatformSoftwareAdjacencyRpActiveSchema):
    """Parser for show platform software adjacency RP active"""

    cli_command = 'show platform software adjacency RP active'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Number of adjacency objects: 5
        p1 = re.compile(r'^Number of adjacency objects: +(?P<number>\d+)$')
        
        # Adjacency id: 0x35 (53)
        p2 = re.compile(r'^Adjacency id: +(?P<adjacency_id>0x[\da-f]+) +\((?P<adjacency_num>\d+)\)$')
        
        # Interface: TenGigabitEthernet0/0/13, IF index: 21, Link Type: MCP_LINK_TAG
        p3 = re.compile(r'^Interface: +(?P<interface>[\w\/]+), +IF index: +(?P<if_index>\d+), +Link Type: +(?P<link_type>[\w_]+)$')
        
        # Encap: 0:0:0:35
        p4 = re.compile(r'^Encap: +(?P<encap>[\w:]+)$')
        
        # Encap Length: 4, Encap Type: MCP_ET_ARPA, MTU: 1500
        p5 = re.compile(r'^Encap Length: +(?P<encap_length>\d+), +Encap Type: +(?P<encap_type>[\w_]+), +MTU: +(?P<mtu>\d+)$')
        
        # Flags: incomplete
        p6 = re.compile(r'^Flags: +(?P<flags>[\w-]+)$')
        
        # Incomplete behavior type: Punt
        p7 = re.compile(r'^Incomplete behavior type: +(?P<incomplete_behavior_type>[\w]+)$')
        
        # Fixup: unknown
        p8 = re.compile(r'^Fixup: +(?P<fixup>[\w]+)$')
        
        #  Fixup_Flags_2: unknown
        p9 = re.compile(r'^Fixup_Flags_2: +(?P<fixup_flags_2>[\w]+)$')
        
        # Nexthop addr: 227.0.0.0
        p10 = re.compile(r'^Nexthop addr: +(?P<nexthop_addr>[\d\.]+)$')
        
        # IP FRR MCP_ADJ_IPFRR_NONE 0
        p11 = re.compile(r'^IP FRR +(?P<ip_frr>[\w_]+) +\d+$')
        
        # OM handle: 0x3480212828
        p12 = re.compile(r'^OM handle: +(?P<om_handle>0x[\da-f]+)$')

        adjacency_id = None

        for line in output.splitlines():
            line = line.strip()

            # Number of adjacency objects: 5
            m = p1.match(line)
            if m:
                parsed_dict['number_of_adjacency_objects'] = int(m.group('number'))
                continue

            # Adjacency id: 0x35 (53)
            m = p2.match(line)
            if m:
                adjacency_id = int(m.group('adjacency_num'))
                adjacency_dict = parsed_dict.setdefault('adjacencies', {}).setdefault(adjacency_id, {})
                adjacency_dict['adjacency_id'] = m.group('adjacency_id')
                continue

            # Interface: TenGigabitEthernet0/0/13, IF index: 21, Link Type: MCP_LINK_TAG
            m = p3.match(line)
            if m:
                adjacency_dict['interface'] = m.group('interface')
                adjacency_dict['if_index'] = int(m.group('if_index'))
                adjacency_dict['link_type'] = m.group('link_type')
                continue

            # Encap: 0:0:0:35
            m = p4.match(line)
            if m:
                adjacency_dict['encap'] = m.group('encap')
                continue

            # Encap Length: 4, Encap Type: MCP_ET_ARPA, MTU: 1500
            m = p5.match(line)
            if m:
                adjacency_dict['encap_length'] = int(m.group('encap_length'))
                adjacency_dict['encap_type'] = m.group('encap_type')
                adjacency_dict['mtu'] = int(m.group('mtu'))
                continue

            # Flags: incomplete
            m = p6.match(line)
            if m:
                adjacency_dict['flags'] = m.group('flags')
                continue

            #  Incomplete behavior type: Punt
            m = p7.match(line)
            if m:
                adjacency_dict['incomplete_behavior_type'] = m.group('incomplete_behavior_type')
                continue

            # Fixup: unknown
            m = p8.match(line)
            if m:
                adjacency_dict['fixup'] = m.group('fixup')
                continue

            # Fixup_Flags_2: unknown
            m = p9.match(line)
            if m:
                adjacency_dict['fixup_flags_2'] = m.group('fixup_flags_2')
                continue

            # Nexthop addr: 227.0.0.0
            m = p10.match(line)
            if m:
                adjacency_dict['nexthop_addr'] = m.group('nexthop_addr')
                continue

            # IP FRR MCP_ADJ_IPFRR_NONE 0
            m = p11.match(line)
            if m:
                adjacency_dict['ip_frr'] = m.group('ip_frr')
                continue

            # OM handle: 0x3480212828
            m = p12.match(line)
            if m:
                adjacency_dict['om_handle'] = m.group('om_handle')
                continue

        return parsed_dict

class ShowPlatformSoftwareNatFpActiveQfpStatsSchema(MetaParser):
    schema = {
        'interface': {
            'add': int,
            'upd': int,
            'del': int,
            'ack': int,
            'err': int,
        },
        'timeout': {
            'set': int,
            'ack': int,
            'err': int,
        },
        'service': {
            'set': int,
            'ack': int,
            'err': int,
        },
    }

class ShowPlatformSoftwareNatFpActiveQfpStats(ShowPlatformSoftwareNatFpActiveQfpStatsSchema):
    """Parser for 'show platform software nat fp active qfp-stats'"""

    cli_command = 'show platform software nat fp active qfp-stats'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}
        # Interface add: 10, upd: 20, del: 5, ack: 30, err: 0
        p1 = re.compile(
            r'^interface add: (?P<add>\d+), upd: (?P<upd>\d+), del: (?P<del>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # Timeout set: 100, ack: 98, err: 2
        p2 = re.compile(
            r'^timeout set: (?P<set>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # Service set: 50, ack: 50, err: 0
        p3 = re.compile(
            r'^service set: (?P<set>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )

        for line in output.splitlines():
            line = line.strip()

            # Interface add: 10, upd: 20, del: 5, ack: 30, err: 0
            m = p1.match(line)
            if m:
                parsed_dict.setdefault('interface', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # Timeout set: 100, ack: 98, err: 2
            m = p2.match(line)
            if m:
                parsed_dict.setdefault('timeout', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # Service set: 50, ack: 50, err: 0
            m = p3.match(line)
            if m:
                parsed_dict.setdefault('service', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

        return parsed_dict

class ShowPlatformSoftwareInterfaceFpActiveSchema(MetaParser):
    schema = {
        'name': str,
        'id': int,
        'qfp_id': int,
        'schedules': int,
        'type': str,
        'state': str,
        'snmp_id': int,
        'mtu': int,
        Optional('ip_address'): str,
        Optional('ipv6_address'): str,
        Optional('vfr_egress'): {
            'vfr_enabled': int,
            'max_reassemblies': int,
            'max_fragments': int,
            'vfr_timeout': int,
            'drop_fragments': int,
            'dscp_bitmap': str,
            'percentage': int
        },
        Optional('ipv6_vfr_egress'): {
            'vfr_enabled': int,
            'max_reassemblies': int,
            'max_fragments': int,
            'vfr_timeout': int,
            'drop_fragments': int,
            'dscp_bitmap': str,
            'percentage': int
        },
        'flags': ListOf(str),
        'icmp_flags': ListOf(str),
        'icmp6_flags': ListOf(str),
        'smi_protocols': ListOf(str),
        Optional('authenticated_user'): str,
        'frr_linkdown_id': int,
        Optional('vnet_name'): str,
        'vnet_tag': int,
        'vnet_extra_info': int,
        'dirty': str,
        'aom_dependency_sanity_check': str,
        'aom_obj_id': int,
        Optional('ether_channel_id'): int,
        Optional('load_balancing_method'): str,
        Optional('number_of_member_links'): int,
        Optional('members'): ListOf(str),
        Optional('number_of_buckets'): int,
        Optional('buckets'): ListOf({
            'id': int,
            'link': str
        })
    }
class ShowPlatformSoftwareInterfaceFpActive(ShowPlatformSoftwareInterfaceFpActiveSchema):
    cli_command = 'show platform software interface fp active name {name}'

    def cli(self, name=" ", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(name=name))

        # Initialize the parsed dictionary
        parsed_dict = {}
        # Name: Te0/0/0, ID: 5, QFP ID: 1, Schedules: 2
        p1 = re.compile(r'^Name: +(?P<name>\S+), +ID: +(?P<id>\d+), +QFP ID: +(?P<qfp_id>\d+), +Schedules: +(?P<schedules>\d+)$')

        # Type: Ethernet, State: UP, SNMP ID: 101, MTU: 1500
        p2 = re.compile(r'^Type: +(?P<type>\S+), +State: +(?P<state>\S+), +SNMP ID: +(?P<snmp_id>\d+), +MTU: +(?P<mtu>\d+)$')

        # IP Address: 192.168.1.1
        p3 = re.compile(r'^IP Address: +(?P<ip_address>\S+)$')

        # IPV6 Address: 2001:0db8:85a3::8a2e:0370:7334
        p4 = re.compile(r'^IPV6 Address: +(?P<ipv6_address>\S+)$')

        # Flags: Up Broadcast Running
        p5 = re.compile(r'^Flags: +(?P<flags>[\S\s]+)$')

        # ICMP Flags: Enabled
        p6 = re.compile(r'^ICMP Flags: +(?P<icmp_flags>[\S\s]+)$')

        # ICMP6 Flags: Disabled
        p7 = re.compile(r'^ICMP6 Flags: +(?P<icmp6_flags>[\S\s]+)$')

        # VFR EGRESS:
        p20 = re.compile(r'^VFR EGRESS:$')

        # IPv6 VFR EGRESS:
        p21 = re.compile(r'^IPv6 VFR EGRESS:$')

        # VFR enabled: 1, Max reassemblies: 1024, Max fragments: 32
        p22 = re.compile(r'^VFR enabled: +(?P<vfr_enabled>\d+), +Max reassemblies: +(?P<max_reassemblies>\d+), +Max fragments: +(?P<max_fragments>\d+)$')

        # VFR timeout: 3, Drop Fragments: 0
        p23 = re.compile(r'^VFR timeout: +(?P<vfr_timeout>\d+), +Drop Fragments: +(?P<drop_fragments>\d+)$')

        # Dscp bitmap: 0x0000000000000000, Percentage: 0
        p24 = re.compile(r'^Dscp bitmap: +(?P<dscp_bitmap>0x[0-9a-fA-F]+), +Percentage: +(?P<percentage>\d+)$')

        # SMI enabled on protocol(s): ARP, IP, MPLS
        p8 = re.compile(r'^SMI enabled on protocol\(s\): +(?P<smi_protocols>[\S\s]+)$')

        # Authenticated-user: admin
        p9 = re.compile(r'^Authenticated-user: *(?P<authenticated_user>.*)$')

        # FRR linkdown ID: 300
        p10 = re.compile(r'^FRR linkdown ID: +(?P<frr_linkdown_id>\d+)$')

        # vNet Name: RED, vNet Tag: 10, vNet Extra Information: 5
        p11 = re.compile(r'^vNet Name: +(?P<vnet_name>.*), +vNet Tag: +(?P<vnet_tag>\d+), +vNet Extra Information: +(?P<vnet_extra_info>\d+)$')

        # Dirty: No
        p12 = re.compile(r'^Dirty: +(?P<dirty>\S+)$')

        # AOM dependency sanity check: Passed
        p13 = re.compile(r'^AOM dependency sanity check: +(?P<aom_dependency_sanity_check>\S+)$')

        # AOM Obj ID: 456
        p14 = re.compile(r'^AOM Obj ID: +(?P<aom_obj_id>\d+)$')

        # Ether-Channel ID: 3, Load-balancing method: src-dst-ip
        p15 = re.compile(r'^Ether-Channel ID: +(?P<ether_channel_id>\d+), +Load-balancing method: +(?P<load_balancing_method>[\S\s]+)$')

        # Number of member links: 2
        p16 = re.compile(r'^Number of member links: +(?P<number_of_member_links>\d+)$')

        # Members: Te0/0/0, Te0/0/1
        p17 = re.compile(r'^Members: +(?P<members>[\S\s]+)$')

        # Number of buckets: 256
        p18 = re.compile(r'^Number of buckets: +(?P<number_of_buckets>\d+)$')

        # ID: 1, link: Up
        p19 = re.compile(r'^ID: +(?P<id>\d+), +link: +(?P<link>\S+)$')


        # Parse each line of the output
        current_vfr_section = None  # Track which VFR section we're in
        
        for line in output.splitlines():
            line = line.strip()

            # Check for VFR section headers
            m = p20.match(line)
            if m:
                current_vfr_section = 'vfr_egress'
                continue

            m = p21.match(line)
            if m:
                current_vfr_section = 'ipv6_vfr_egress'
                continue

            # Name: Te0/0/0, ID: 5, QFP ID: 1, Schedules: 2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['name'] = group['name']
                parsed_dict['id'] = int(group['id'])
                parsed_dict['qfp_id'] = int(group['qfp_id'])
                parsed_dict['schedules'] = int(group['schedules'])
                continue

            # Type: Ethernet, State: UP, SNMP ID: 101, MTU: 1500
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['type'] = group['type']
                parsed_dict['state'] = group['state']
                parsed_dict['snmp_id'] = int(group['snmp_id'])
                parsed_dict['mtu'] = int(group['mtu'])
                continue

            # IP Address: 192.168.1.1
            m = p3.match(line)
            if m:
                parsed_dict['ip_address'] = m.group('ip_address')
                continue

            # IPV6 Address: 2001:0db8:85a3::8a2e:0370:7334
            m = p4.match(line)
            if m:
                parsed_dict['ipv6_address'] = m.group('ipv6_address')
                continue

            # VFR enabled: 1, Max reassemblies: 1024, Max fragments: 32
            m = p22.match(line)
            if m and current_vfr_section:
                group = m.groupdict()
                parsed_dict.setdefault(current_vfr_section, {})
                parsed_dict[current_vfr_section]['vfr_enabled'] = int(group['vfr_enabled'])
                parsed_dict[current_vfr_section]['max_reassemblies'] = int(group['max_reassemblies'])
                parsed_dict[current_vfr_section]['max_fragments'] = int(group['max_fragments'])
                continue

            # VFR timeout: 3, Drop Fragments: 0
            m = p23.match(line)
            if m and current_vfr_section:
                group = m.groupdict()
                parsed_dict[current_vfr_section]['vfr_timeout'] = int(group['vfr_timeout'])
                parsed_dict[current_vfr_section]['drop_fragments'] = int(group['drop_fragments'])
                continue

            # Dscp bitmap: 0x0000000000000000, Percentage: 0
            m = p24.match(line)
            if m and current_vfr_section:
                group = m.groupdict()
                parsed_dict[current_vfr_section]['dscp_bitmap'] = group['dscp_bitmap']
                parsed_dict[current_vfr_section]['percentage'] = int(group['percentage'])
                current_vfr_section = None  # Reset after completing a VFR section
                continue

            # Flags: Up Broadcast Runnings
            m = p5.match(line)
            if m:
                flags_text = m.group('flags').strip()
                if ', ' in flags_text:
                    parsed_dict['flags'] = flags_text.split(', ')
                else:
                    parsed_dict['flags'] = flags_text.split()
                continue

            # ICMP Flags: Enabled
            m = p6.match(line)
            if m:
                icmp_flags_text = m.group('icmp_flags').strip()
                if ', ' in icmp_flags_text:
                    parsed_dict['icmp_flags'] = icmp_flags_text.split(', ')
                else:
                    parsed_dict['icmp_flags'] = icmp_flags_text.split()
                continue

            # ICMP6 Flags: Disabled
            m = p7.match(line)
            if m:
                icmp6_flags_text = m.group('icmp6_flags').strip()
                if ', ' in icmp6_flags_text:
                    parsed_dict['icmp6_flags'] = icmp6_flags_text.split(', ')
                else:
                    parsed_dict['icmp6_flags'] = icmp6_flags_text.split()
                continue

            # SMI enabled on protocol(s): ARP, IP, MPLS
            m = p8.match(line)
            if m:
                smi_protocols_text = m.group('smi_protocols').strip()
                if ', ' in smi_protocols_text:
                    parsed_dict['smi_protocols'] = smi_protocols_text.split(', ')
                else:
                    parsed_dict['smi_protocols'] = smi_protocols_text.split()
                continue

            # Authenticated-user: admin
            m = p9.match(line)
            if m:
                auth_user = m.group('authenticated_user').strip()
                if auth_user:  # Only include if not empty
                    parsed_dict['authenticated_user'] = auth_user
                continue

            # FRR linkdown ID: 300
            m = p10.match(line)
            if m:
                parsed_dict['frr_linkdown_id'] = int(m.group('frr_linkdown_id'))
                continue

            # vNet Name: RED, vNet Tag: 10, vNet Extra Information: 5
            m = p11.match(line)
            if m:
                group = m.groupdict()
                vnet_name = group['vnet_name'].strip()
                if vnet_name:  # Only include if not empty
                    parsed_dict['vnet_name'] = vnet_name
                parsed_dict['vnet_tag'] = int(group['vnet_tag'])
                parsed_dict['vnet_extra_info'] = int(group['vnet_extra_info'])
                continue

            # Dirty: No
            m = p12.match(line)
            if m:
                parsed_dict['dirty'] = m.group('dirty')
                continue

            # AOM dependency sanity check: Passed
            m = p13.match(line)
            if m:
                parsed_dict['aom_dependency_sanity_check'] = m.group('aom_dependency_sanity_check')
                continue

            # AOM Obj ID: 456
            m = p14.match(line)
            if m:
                parsed_dict['aom_obj_id'] = int(m.group('aom_obj_id'))
                continue

            # Ether-Channel ID: 3, Load-balancing method: src-dst-ip
            m = p15.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['ether_channel_id'] = int(group['ether_channel_id'])
                parsed_dict['load_balancing_method'] = group['load_balancing_method']
                continue

            # Number of member links: 2
            m = p16.match(line)
            if m:
                parsed_dict['number_of_member_links'] = int(m.group('number_of_member_links'))
                continue

            # Members: Te0/0/0, Te0/0/1
            m = p17.match(line)
            if m:
                members_text = m.group('members').strip()
                if ', ' in members_text:
                    parsed_dict['members'] = members_text.split(', ')
                else:
                    parsed_dict['members'] = members_text.split()
                continue

            # Number of buckets: 256
            m = p18.match(line)
            if m:
                parsed_dict['number_of_buckets'] = int(m.group('number_of_buckets'))
                continue

            # ID: 1, link: Up
            m = p19.match(line)
            if m:
                bucket = {'id': int(m.group('id')), 'link': m.group('link')}
                parsed_dict.setdefault('buckets', []).append(bucket)
                continue

        return parsed_dict

class ShowPlatformSoftwareMulticastStatsSchema(MetaParser):
    """Schema for show platform software multicast stats"""
    schema = {
        'bad_fman_stats': int,
        'access_without_platform_markings': int,
        'punts_without_subblocks': int,
        'v4_mfib_entry_add_messages': int,
        'v4_mfib_entry_modify_messages': int,
        'v4_mfib_entry_delete_messages': int,
        'duplicate_v4_entry_deletes': int,
        'v4_mfib_outgoing_interface_add_messages': int,
        'v4_mfib_outgoing_interface_modify_messages': int,
        'v4_mfib_outgoing_interface_delete_messages': int,
        'v4_interface_enable_messages': int,
        'v4_interface_disable_messages': int,
        'oif_v4_adds_missing_adjacency': int,
        'oif_v4_missing_adjs_added': int,
        'oif_v4_adj_creation_skipped': int,
        'oif_v4_adj_creation_failure': int,
        'oif_v4_id_creation_failure': int,
        'oif_v4_deletes_missing_adj_using_cached_id': int,
        'oif_v4_deletes_missing_id_cache': int,
        'oif_v4_add_modify_ic_flag_update_failure': int,
        'oif_v4_deletes_ic_flag_update_failure': int,
        'mgre_non_autorp_packets_for_autorp_groups': int,
        'mgre_autorp_packets_injected_to_p2mp_interface': int,
        'v6_mfib_entry_add_messages': int,
        'v6_mfib_entry_modify_messages': int,
        'v6_mfib_entry_delete_messages': int,
        'duplicate_v6_entry_deletes': int,
        'v6_mfib_outgoing_interface_add_messages': int,
        'v6_mfib_outgoing_interface_modify_messages': int,
        'v6_mfib_outgoing_interface_delete_messages': int,
        'v6_interface_enable_messages': int,
        'v6_interface_disable_messages': int,
        'oif_v6_adds_missing_adjacency': int,
        'oif_v6_missing_adjs_added': int,
        'oif_v6_adj_creation_skipped': int,
        'oif_v6_adj_creation_failure': int,
        'oif_v6_id_creation_failure': int,
        'oif_v6_deletes_missing_adj_using_cached_id': int,
        'oif_v6_deletes_missing_id_cache': int,
        'oif_v6_add_modify_ic_flag_update_failure': int,
        'oif_v6_delete_ic_flag_update_failure': int,
        'downloads_with_unknown_af': int,
        'oif_ic_count_add_modify_failure': int,
        'oif_ic_count_deletes_failure': int,
        'oif_a_count_add_modify_failure': int,
        'oif_a_count_deletes_failure': int,
    }

class ShowPlatformSoftwareMulticastStats(ShowPlatformSoftwareMulticastStatsSchema):
    """Parser for show platform software multicast stats"""

    cli_command = 'show platform software multicast stats'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Define regex patterns using re.compile
        # 12 Number of bad fman stats
        p1 = re.compile(r'(?P<value>\d+) Number of bad fman stats')

        # 25 Number of access to entries without platform markings
        p2 = re.compile(r'(?P<value>\d+) Number of access to entries without platform markings')

        # 3 Number of punts without subblocks
        p3 = re.compile(r'(?P<value>\d+) Number of punts without subblocks')

        # 100 v4-mfib-entry add messages
        p4 = re.compile(r'(?P<value>\d+) v4-mfib-entry add messages')

        # 200 v4-mfib-entry modify messages
        p5 = re.compile(r'(?P<value>\d+) v4-mfib-entry modify messages')

        # 150 v4-mfib-entry delete messages
        p6 = re.compile(r'(?P<value>\d+) v4-mfib-entry delete messages')

        # 5 Number of duplicate v4 entry deletes
        p7 = re.compile(r'(?P<value>\d+) Number of duplicate v4 entry deletes')

        # 10 v4-mfib-outgoing-interface add messages
        p8 = re.compile(r'(?P<value>\d+) v4-mfib-outgoing-interface add messages')

        # 8 v4-mfib-outgoing-interface modify messages
        p9 = re.compile(r'(?P<value>\d+) v4-mfib-outgoing-interface modify messages')

        # 6 v4-mfib-outgoing-interface delete messages
        p10 = re.compile(r'(?P<value>\d+) v4-mfib-outgoing-interface delete messages')

        # 300 v4-interface enable messages
        p11 = re.compile(r'(?P<value>\d+) v4-interface enable messages')

        # 120 v4-interface disable messages
        p12 = re.compile(r'(?P<value>\d+) v4-interface disable messages')

        # 50 Oif v4 adds, missing adjacency
        p13 = re.compile(r'(?P<value>\d+) Oif v4 adds, missing adjacency')

        # 30 Oif v4 missing adj's added
        p14 = re.compile(r'(?P<value>\d+) Oif v4 missing adj\'s added')

        # 12 Oif v4 adj creation skipped
        p15 = re.compile(r'(?P<value>\d+) Oif v4 adj creation skipped')

        # 3 Oif v4 adj creation failure
        p16 = re.compile(r'(?P<value>\d+) Oif v4 adj creation failure')

        # 2 Oif v4 ID creation failure
        p17 = re.compile(r'(?P<value>\d+) Oif v4 ID creation failure')

        # 18 Oif v4 deletes, missing adj using cached ID
        p18 = re.compile(r'(?P<value>\d+) Oif v4 deletes, missing adj using cached ID')

        # 5 Oif v4 deletes, missing ID cache
        p19 = re.compile(r'(?P<value>\d+) Oif v4 deletes, missing ID cache')

        # 7 Oif v4 add/modify, IC flag update failure
        p20 = re.compile(r'(?P<value>\d+) Oif v4 add/modify, IC flag update failure')

        # 4 Oif v4 deletes, IC flag update failure
        p21 = re.compile(r'(?P<value>\d+) Oif v4 deletes, IC flag update failure')

        # 8 mGRE, non-AutoRP Packets for AutoRP groups
        p22 = re.compile(r'(?P<value>\d+) mGRE, non-AutoRP Packets for AutoRP groups')

        # 2 mGRE, AutoRP Packets injected to p2MP interface
        p23 = re.compile(r'(?P<value>\d+) mGRE, AutoRP Packets injected to p2MP interface')

        # 14 v6-mfib-entry add messages
        p24 = re.compile(r'(?P<value>\d+) v6-mfib-entry add messages')

        # 9 v6-mfib-entry modify messages
        p25 = re.compile(r'(?P<value>\d+) v6-mfib-entry modify messages')

        # 11 v6-mfib-entry delete messages
        p26 = re.compile(r'(?P<value>\d+) v6-mfib-entry delete messages')

        # 6 Number of duplicate v6 entry deletes
        p27 = re.compile(r'(?P<value>\d+) Number of duplicate v6 entry deletes')

        # 20 v6-mfib-outgoing-interface add messages
        p28 = re.compile(r'(?P<value>\d+) v6-mfib-outgoing-interface add messages')

        # 15 v6-mfib-outgoing-interface modify messages
        p29 = re.compile(r'(?P<value>\d+) v6-mfib-outgoing-interface modify messages')

        # 25 v6-mfib-outgoing-interface delete messages
        p30 = re.compile(r'(?P<value>\d+) v6-mfib-outgoing-interface delete messages')

        # 50 v6-interface enable messages
        p31 = re.compile(r'(?P<value>\d+) v6-interface enable messages')

        # 45 v6-interface disable messages
        p32 = re.compile(r'(?P<value>\d+) v6-interface disable messages')

        # 23 Oif v6 adds, missing adjacency
        p33 = re.compile(r'(?P<value>\d+) Oif v6 adds, missing adjacency')

        # 19 Oif v6 missing adj's added
        p34 = re.compile(r'(?P<value>\d+) Oif v6 missing adj\'s added')

        # 7 Oif v6 adj creation skipped
        p35 = re.compile(r'(?P<value>\d+) Oif v6 adj creation skipped')

        # 4 Oif v6 adj creation failure
        p36 = re.compile(r'(?P<value>\d+) Oif v6 adj creation failure')

        # 3 Oif v6 ID creation failure
        p37 = re.compile(r'(?P<value>\d+) Oif v6 ID creation failure')

        # 17 Oif v6 deletes, missing adj using cached ID
        p38 = re.compile(r'(?P<value>\d+) Oif v6 deletes, missing adj using cached ID')

        # 9 Oif v6 deletes, missing ID cache
        p39 = re.compile(r'(?P<value>\d+) Oif v6 deletes, missing ID cache')

        # 6 Oif v6 add/modify, IC flag update failure
        p40 = re.compile(r'(?P<value>\d+) Oif v6 add/modify, IC flag update failure')

        # 3 Oif v6 delete, IC flag update failure
        p41 = re.compile(r'(?P<value>\d+) Oif v6 delete, IC flag update failure')

        # 2 Number of downloads with unknown AF
        p42 = re.compile(r'(?P<value>\d+) Number of downloads with unknown AF')

        # 5 Oif IC count add/modify failure
        p43 = re.compile(r'(?P<value>\d+) Oif IC count add/modify failure')

        # 3 Oif IC count deletes failure
        p44 = re.compile(r'(?P<value>\d+) Oif IC count deletes failure')

        # 2 Oif A count add/modify failure
        p45 = re.compile(r'(?P<value>\d+) Oif A count add/modify failure')

        # 1 Oif A count deletes failure
        p46 = re.compile(r'(?P<value>\d+) Oif A count deletes failure')

        # Iterate over each line in the output
        for line in output.splitlines():
            line = line.strip()

            # 12 Number of bad fman stats
            match = p1.match(line)
            if match:
                parsed_dict['bad_fman_stats'] = int(match.group('value'))
                continue

            # 25 Number of access to entries without platform markings
            match = p2.match(line)
            if match:
                parsed_dict['access_without_platform_markings'] = int(match.group('value'))
                continue

            # 3 Number of punts without subblocks
            match = p3.match(line)
            if match:
                parsed_dict['punts_without_subblocks'] = int(match.group('value'))
                continue

            # 100 v4-mfib-entry add messages
            match = p4.match(line)
            if match:
                parsed_dict['v4_mfib_entry_add_messages'] = int(match.group('value'))
                continue

            # 200 v4-mfib-entry modify messages
            match = p5.match(line)
            if match:
                parsed_dict['v4_mfib_entry_modify_messages'] = int(match.group('value'))
                continue

            # 150 v4-mfib-entry delete messages
            match = p6.match(line)
            if match:
                parsed_dict['v4_mfib_entry_delete_messages'] = int(match.group('value'))
                continue

            # 5 Number of duplicate v4 entry deletes
            match = p7.match(line)
            if match:
                parsed_dict['duplicate_v4_entry_deletes'] = int(match.group('value'))
                continue

            # 10 v4-mfib-outgoing-interface add messages
            match = p8.match(line)
            if match:
                parsed_dict['v4_mfib_outgoing_interface_add_messages'] = int(match.group('value'))
                continue

            # 8 v4-mfib-outgoing-interface modify messages
            match = p9.match(line)
            if match:
                parsed_dict['v4_mfib_outgoing_interface_modify_messages'] = int(match.group('value'))
                continue

            # 6 v4-mfib-outgoing-interface delete messages
            match = p10.match(line)
            if match:
                parsed_dict['v4_mfib_outgoing_interface_delete_messages'] = int(match.group('value'))
                continue

            # 300 v4-interface enable messages
            match = p11.match(line)
            if match:
                parsed_dict['v4_interface_enable_messages'] = int(match.group('value'))
                continue

            # 120 v4-interface disable messages
            match = p12.match(line)
            if match:
                parsed_dict['v4_interface_disable_messages'] = int(match.group('value'))
                continue

            # 50 Oif v4 adds, missing adjacency
            match = p13.match(line)
            if match:
                parsed_dict['oif_v4_adds_missing_adjacency'] = int(match.group('value'))
                continue

            # 30 Oif v4 missing adj's added
            match = p14.match(line)
            if match:
                parsed_dict['oif_v4_missing_adjs_added'] = int(match.group('value'))
                continue

            # 12 Oif v4 adj creation skipped
            match = p15.match(line)
            if match:
                parsed_dict['oif_v4_adj_creation_skipped'] = int(match.group('value'))
                continue

            # 3 Oif v4 adj creation failure
            match = p16.match(line)
            if match:
                parsed_dict['oif_v4_adj_creation_failure'] = int(match.group('value'))
                continue

            # 2 Oif v4 ID creation failure
            match = p17.match(line)
            if match:
                parsed_dict['oif_v4_id_creation_failure'] = int(match.group('value'))
                continue

            # 18 Oif v4 deletes, missing adj using cached ID
            match = p18.match(line)
            if match:
                parsed_dict['oif_v4_deletes_missing_adj_using_cached_id'] = int(match.group('value'))
                continue

            # 5 Oif v4 deletes, missing ID cache
            match = p19.match(line)
            if match:
                parsed_dict['oif_v4_deletes_missing_id_cache'] = int(match.group('value'))
                continue

            # 7 Oif v4 add/modify, IC flag update failure
            match = p20.match(line)
            if match:
                parsed_dict['oif_v4_add_modify_ic_flag_update_failure'] = int(match.group('value'))
                continue

            # 4 Oif v4 deletes, IC flag update failure
            match = p21.match(line)
            if match:
                parsed_dict['oif_v4_deletes_ic_flag_update_failure'] = int(match.group('value'))
                continue

            # 8 mGRE, non-AutoRP Packets for AutoRP groups
            match = p22.match(line)
            if match:
                parsed_dict['mgre_non_autorp_packets_for_autorp_groups'] = int(match.group('value'))
                continue

            # 2 mGRE, AutoRP Packets injected to p2MP interface
            match = p23.match(line)
            if match:
                parsed_dict['mgre_autorp_packets_injected_to_p2mp_interface'] = int(match.group('value'))
                continue

            # 14 v6-mfib-entry add messages
            match = p24.match(line)
            if match:
                parsed_dict['v6_mfib_entry_add_messages'] = int(match.group('value'))
                continue

            # 9 v6-mfib-entry modify messages
            match = p25.match(line)
            if match:
                parsed_dict['v6_mfib_entry_modify_messages'] = int(match.group('value'))
                continue

            # 11 v6-mfib-entry delete messages
            match = p26.match(line)
            if match:
                parsed_dict['v6_mfib_entry_delete_messages'] = int(match.group('value'))
                continue

            # 6 Number of duplicate v6 entry deletes
            match = p27.match(line)
            if match:
                parsed_dict['duplicate_v6_entry_deletes'] = int(match.group('value'))
                continue

            # 20 v6-mfib-outgoing-interface add messages
            match = p28.match(line)
            if match:
                parsed_dict['v6_mfib_outgoing_interface_add_messages'] = int(match.group('value'))
                continue

            # 15 v6-mfib-outgoing-interface modify messages
            match = p29.match(line)
            if match:
                parsed_dict['v6_mfib_outgoing_interface_modify_messages'] = int(match.group('value'))
                continue

            # 25 v6-mfib-outgoing-interface delete messages
            match = p30.match(line)
            if match:
                parsed_dict['v6_mfib_outgoing_interface_delete_messages'] = int(match.group('value'))
                continue

            # 50 v6-interface enable messages
            match = p31.match(line)
            if match:
                parsed_dict['v6_interface_enable_messages'] = int(match.group('value'))
                continue

            # 45 v6-interface disable messages
            match = p32.match(line)
            if match:
                parsed_dict['v6_interface_disable_messages'] = int(match.group('value'))
                continue

            # 23 Oif v6 adds, missing adjacency
            match = p33.match(line)
            if match:
                parsed_dict['oif_v6_adds_missing_adjacency'] = int(match.group('value'))
                continue

            # 19 Oif v6 missing adj's added
            match = p34.match(line)
            if match:
                parsed_dict['oif_v6_missing_adjs_added'] = int(match.group('value'))
                continue

            # 7 Oif v6 adj creation skipped
            match = p35.match(line)
            if match:
                parsed_dict['oif_v6_adj_creation_skipped'] = int(match.group('value'))
                continue

            # 4 Oif v6 adj creation failure
            match = p36.match(line)
            if match:
                parsed_dict['oif_v6_adj_creation_failure'] = int(match.group('value'))
                continue

            # 3 Oif v6 ID creation failure
            match = p37.match(line)
            if match:
                parsed_dict['oif_v6_id_creation_failure'] = int(match.group('value'))
                continue

            # 17 Oif v6 deletes, missing adj using cached ID
            match = p38.match(line)
            if match:
                parsed_dict['oif_v6_deletes_missing_adj_using_cached_id'] = int(match.group('value'))
                continue

            # 9 Oif v6 deletes, missing ID cache
            match = p39.match(line)
            if match:
                parsed_dict['oif_v6_deletes_missing_id_cache'] = int(match.group('value'))
                continue

            # 6 Oif v6 add/modify, IC flag update failure
            match = p40.match(line)
            if match:
                parsed_dict['oif_v6_add_modify_ic_flag_update_failure'] = int(match.group('value'))
                continue

            # 3 Oif v6 delete, IC flag update failure
            match = p41.match(line)
            if match:
                parsed_dict['oif_v6_delete_ic_flag_update_failure'] = int(match.group('value'))
                continue

            # 2 Number of downloads with unknown AF
            match = p42.match(line)
            if match:
                parsed_dict['downloads_with_unknown_af'] = int(match.group('value'))
                continue

            # 5 Oif IC count add/modify failure
            match = p43.match(line)
            if match:
                parsed_dict['oif_ic_count_add_modify_failure'] = int(match.group('value'))
                continue

            # 3 Oif IC count deletes failure
            match = p44.match(line)
            if match:
                parsed_dict['oif_ic_count_deletes_failure'] = int(match.group('value'))
                continue

            # 2 Oif A count add/modify failure
            match = p45.match(line)
            if match:
                parsed_dict['oif_a_count_add_modify_failure'] = int(match.group('value'))
                continue

            # 1 Oif A count deletes failure
            match = p46.match(line)
            if match:
                parsed_dict['oif_a_count_deletes_failure'] = int(match.group('value'))
                continue

        return parsed_dict

class ShowPlatformSoftwareMplsFpActiveEosSchema(MetaParser):
    """Schema for show platform software mpls fp active eos"""
    schema = {
        'number_of_eos_choice_entries': int,
        'eos_choices': {
            int: {
                'number_of_paths': int,
                'next_object_type': ListOf(str),  # Use ListOf for type validation
                'next_object_index': ListOf(str),  # Use ListOf for type validation
                Optional('aom_id'): int,
                Optional('cpp_handle'): str,
                Optional('flags'): int
            }
        }
    }

class ShowPlatformSoftwareMplsFpActiveEos(ShowPlatformSoftwareMplsFpActiveEosSchema):
    """Parser for show platform software mpls fp active eos"""
    cli_command = 'show platform software mpls fp active eos'
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        parsed_dict = {}
        eos_choice = None
        # Define regex patterns

        # Number of EOS Choice entries: 12
        p1 = re.compile(r'^Number of EOS Choice entries:\s+(?P<entry_count>\d+)$')

        # EOS Choice 142, Number of paths: 2
        p2 = re.compile(r'^EOS Choice\s+(?P<eos_choice>0x[0-9a-fA-F]+|\d+),\s+Number of paths:\s+(?P<number_of_paths>\d+)$')

        # Next Object Type: OBJ_LABEL, OBJ_LABEL
        p3 = re.compile(r'^Next Object Type:\s+(?P<next_object_type>.+)$')

        # Next Object Index: 0x1d, 0x1e
        p4 = re.compile(r'^Next Object Index:\s+(?P<next_object_index>.+)$')

        # aom id: 5, CPP handle: 0x7, flags: 0
        p5 = re.compile(r'^aom id:\s+(?P<aom_id>\d+),\s+CPP handle:\s+(?P<cpp_handle>\S+),\s+flags:\s+(?P<flags>\d+)$')

        # Process each line of the output
        for line in output.splitlines():
            line = line.strip()
            # Number of EOS Choice entries: 12
            m = p1.match(line)
            if m:
                parsed_dict['number_of_eos_choice_entries'] = int(m.group('entry_count'))
                continue

            # EOS Choice 142, Number of paths: 2
            m = p2.match(line)
            if m:
                eos_choice_raw = m.group('eos_choice')
                eos_choice = int(eos_choice_raw, 16) if eos_choice_raw.startswith('0x') else int(eos_choice_raw)
                parsed_dict.setdefault('eos_choices', {}).setdefault(eos_choice, {})
                parsed_dict['eos_choices'][eos_choice]['number_of_paths'] = int(m.group('number_of_paths'))
                continue

            # Next Object Type: OBJ_LABEL, OBJ_LABEL
            m = p3.match(line)
            if m and eos_choice is not None:
                types = [t.strip() for t in m.group('next_object_type').split(',')]
                parsed_dict['eos_choices'][eos_choice]['next_object_type'] = types
                continue

            # Next Object Index: 0x1d, 0x1e
            m = p4.match(line)
            if m and eos_choice is not None:
                indexes = [i.strip() for i in m.group('next_object_index').split(',')]
                parsed_dict['eos_choices'][eos_choice]['next_object_index'] = indexes
                continue

            # aom id: 5, CPP handle: 0x7, flags: 0
            m = p5.match(line)
            if m and eos_choice is not None:
                parsed_dict['eos_choices'][eos_choice]['aom_id'] = int(m.group('aom_id'))
                parsed_dict['eos_choices'][eos_choice]['cpp_handle'] = m.group('cpp_handle')
                parsed_dict['eos_choices'][eos_choice]['flags'] = int(m.group('flags'))
                continue
        return parsed_dict

class ShowPlatformSoftwareMemoryDatabaseForwardingManagerSchema(MetaParser):
    """Schema for 'show platform software memory database forwarding-manager {slot} active brief | include {options}'"""
    schema = {
        'entries': {
            str: {  # This will be the table/type name
                'count': int,
                'database': str,
            }
        }
    }

class ShowPlatformSoftwareMemoryDatabaseForwardingManager(ShowPlatformSoftwareMemoryDatabaseForwardingManagerSchema):
    """Parser for 'show platform software memory database forwarding-manager {slot} active brief | include {options}'"""

    cli_command = 'show platform software memory database forwarding-manager {slot} active brief | include {options}'

    def cli(self, slot='', options='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(slot=slot, options=options))

        # Initialize the parsed dictionary
        parsed_dict = {}

        # 1 entries [nat_db] table nat_addr_range/0
        p0 = re.compile(r'(\d+) entries \[(\w+)\] \w+ (\S+)/\d+')

        # Process each line of the output
        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # 1 entries [nat_db] table nat_addr_range/0
            m = p0.match(line)
            if m:
                count, database, name = m.groups()
                # Use setdefault to avoid key errors
                entry_dict = parsed_dict.setdefault('entries', {}).setdefault(name, {})
                entry_dict['count'] = int(count)
                entry_dict['database'] = database

        return parsed_dict

class ShowPlatformSoftwareNatFpActiveInterfaceSchema(MetaParser):
    """Schema for show platform software nat fp active interface"""
    schema = {
        'interfaces': {
            str: {
                'interface_handle': int,
                'domain': str,
                'static_host_allowed': str,
                'qfp_handle': int,
            }
        }
    }

class ShowPlatformSoftwareNatFpActiveInterface(ShowPlatformSoftwareNatFpActiveInterfaceSchema):
    """Parser for show platform software nat fp active interface"""

    cli_command = 'show platform software nat fp active interface'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

    # Regular expressions for parsing the output
		#Name: GigabitEthernet0/0/2, Inteface handle: 10
        p1 = re.compile(r'^Name: +(?P<name>\S+), +Inteface +handle: +(?P<interface_handle>\d+)$')
		
		#Domain: OUTSIDE, Static-host allowed: No
        p2 = re.compile(r'^Domain: +(?P<domain>\S+), +Static-host +allowed: +(?P<static_host_allowed>\S+)$')
		
		#QFP handle: 9
        p3 = re.compile(r'^QFP +handle: +(?P<qfp_handle>\d+)$')

        # Iterate over each line in the output
        for line in output.splitlines():
            line = line.strip()

            # Match the first line of each interface block
			#Name: GigabitEthernet0/0/2, Inteface handle: 10
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_name = group['name']
                interface_handle = int(group['interface_handle'])

                # Use setdefault to avoid KeyError
                interface_dict = parsed_dict.setdefault('interfaces', {}).setdefault(interface_name, {})
                interface_dict['interface_handle'] = interface_handle
                continue

            # Match the second line of each interface block
			#Domain: OUTSIDE, Static-host allowed: No
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface_dict['domain'] = group['domain']
                interface_dict['static_host_allowed'] = group['static_host_allowed']
                continue

            # Match the third line of each interface block
			#QFP handle: 9
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface_dict['qfp_handle'] = int(group['qfp_handle'])
                continue

        return parsed_dict

class ShowPlatformSoftwareAccessListFpActiveStatisticsSchema(MetaParser):
    """Schema for show platform software access-list fp active statistics"""
    schema = {
        'set_log_threshold': {
            'threshold': int,
            'interval': int,
        },
        'ipv4_access_list': {
            'entry_add': int,
            'entry_delete': int,
            'bind': int,
            'unbind': int,
            'resequence': int,
            'delete': int,
        },
        'ipv6_access_list': {
            'entry_add': int,
            'entry_delete': int,
            'bind': int,
            'unbind': int,
            'resequence': int,
            'delete': int,
        },
        'mac_access_list': {
            'entry_add': int,
            'entry_delete': int,
            'bind': int,
            'unbind': int,
            'delete': int,
        },
        'access_list_sync': {
            'start': int,
            'end': int,
        },
        'qfp_match_add': {
            'add': int,
            'replace': int,
            'ack_success': int,
            'ack_error': int,
        },
        'qfp_match_delete': {
            'delete': int,
            'ack_success': int,
            'ack_error': int,
        },
        'qfp_action_edit': {
            'edit': int,
            'ack_success': int,
            'ack_error': int,
        },
        'qfp_action_replace': {
            'replace': int,
            'ack_success': int,
            'ack_error': int,
        },
        'qfp_bind': {
            'bind': int,
            'ack_success': int,
            'ack_error': int,
        },
        'qfp_unbind': {
            'unbind': int,
            'ack_success': int,
            'ack_error': int,
        },
    }

class ShowPlatformSoftwareAccessListFpActiveStatistics(ShowPlatformSoftwareAccessListFpActiveStatisticsSchema):
    """Parser for show platform software access-list fp active statistics"""

    cli_command = 'show platform software access-list fp active statistics'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing the output
        # Set Log Threshold: 0, Interval: 0
        p1 = re.compile(r'^Set Log Threshold: (?P<threshold>\d+), Interval: (?P<interval>\d+)$')

        # IPv4 Access-list Entry Add: 1, Delete: 0
        p2 = re.compile(r'^IPv4 Access-list Entry Add: (?P<entry_add>\d+), Delete: (?P<entry_delete>\d+)$')

        # IPv4 Access-list Bind: 0, Unbind: 0
        p3 = re.compile(r'^IPv4 Access-list Bind: (?P<bind>\d+), Unbind: (?P<unbind>\d+)$')

        # IPv4 Access-list Resequence: 0, Delete: 1
        p4 = re.compile(r'^IPv4 Access-list Resequence: (?P<resequence>\d+), Delete: (?P<delete>\d+)$')

        # IPv6 Access-list Entry Add: 0, Delete: 0
        p5 = re.compile(r'^IPv6 Access-list Entry Add: (?P<entry_add>\d+), Delete: (?P<entry_delete>\d+)$')

        # IPv6 Access-list Bind: 0, Unbind: 0
        p6 = re.compile(r'^IPv6 Access-list Bind: (?P<bind>\d+), Unbind: (?P<unbind>\d+)$')

        # IPv6 Access-list Resequence: 0, Delete: 0
        p7 = re.compile(r'^IPv6 Access-list Resequence: (?P<resequence>\d+), Delete: (?P<delete>\d+)$')

        # MAC Access-list Entry Add: 0, Delete: 0
        p8 = re.compile(r'^MAC Access-list Entry Add: (?P<entry_add>\d+), Delete: (?P<entry_delete>\d+)$')

        # MAC Access-list Bind: 0, Unbind: 0
        p9 = re.compile(r'^MAC Access-list Bind: (?P<bind>\d+), Unbind: (?P<unbind>\d+)$')

        # MAC Access-list Delete: 0
        p10 = re.compile(r'^MAC Access-list Delete: (?P<delete>\d+)$')

        # Access-list Sync Start: 0, End: 0
        p11 = re.compile(r'^Access-list Sync Start: (?P<start>\d+), End: (?P<end>\d+)$')

        # QFP Match Add: 0, Replace: 0, ACK Success: 0, ACK Error: 0
        p12 = re.compile(r'^QFP Match Add: (?P<add>\d+), Replace: (?P<replace>\d+), ACK Success: (?P<ack_success>\d+), ACK Error: (?P<ack_error>\d+)$')

        # QFP Match Delete: 0, ACK Success: 0, ACK Error: 0
        p13 = re.compile(r'^QFP Match Delete: (?P<delete>\d+), ACK Success: (?P<ack_success>\d+), ACK Error: (?P<ack_error>\d+)$')

        # QFP Action Edit: 0, ACK Success: 0, ACK Error: 0
        p14 = re.compile(r'^QFP Action Edit: (?P<edit>\d+), ACK Success: (?P<ack_success>\d+), ACK Error: (?P<ack_error>\d+)$')

        # QFP Action Replace: 0, ACK Success: 0, ACK Error: 0
        p15 = re.compile(r'^QFP Action Replace: (?P<replace>\d+), ACK Success: (?P<ack_success>\d+), ACK Error: (?P<ack_error>\d+)$')

        # QFP Bind: 0, ACK Success: 0, ACK Error: 0
        p16 = re.compile(r'^QFP Bind: (?P<bind>\d+), ACK Success: (?P<ack_success>\d+), ACK Error: (?P<ack_error>\d+)$')

        # QFP Unbind: 0, ACK Success: 0, ACK Error: 0
        p17 = re.compile(r'^QFP Unbind: (?P<unbind>\d+), ACK Success: (?P<ack_success>\d+), ACK Error: (?P<ack_error>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Match and parse each line
            # Set Log Threshold: 0, Interval: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('set_log_threshold', {}).update({
                    'threshold': int(group['threshold']),
                    'interval': int(group['interval']),
                })
                continue

            # IPv4 Access-list Entry Add: 1, Delete: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('ipv4_access_list', {}).update({
                    'entry_add': int(group['entry_add']),
                    'entry_delete': int(group['entry_delete']),
                })
                continue

            # IPv4 Access-list Bind: 0, Unbind: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('ipv4_access_list', {}).update({
                    'bind': int(group['bind']),
                    'unbind': int(group['unbind']),
                })
                continue

            # IPv4 Access-list Resequence: 0, Delete: 1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('ipv4_access_list', {}).update({
                    'resequence': int(group['resequence']),
                    'delete': int(group['delete']),
                })
                continue

            # IPv6 Access-list Entry Add: 0, Delete: 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('ipv6_access_list', {}).update({
                    'entry_add': int(group['entry_add']),
                    'entry_delete': int(group['entry_delete']),
                })
                continue

            # IPv6 Access-list Bind: 0, Unbind: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('ipv6_access_list', {}).update({
                    'bind': int(group['bind']),
                    'unbind': int(group['unbind']),
                })
                continue

            # IPv6 Access-list Resequence: 0, Delete: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('ipv6_access_list', {}).update({
                    'resequence': int(group['resequence']),
                    'delete': int(group['delete']),
                })
                continue

            # MAC Access-list Entry Add: 0, Delete: 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('mac_access_list', {}).update({
                    'entry_add': int(group['entry_add']),
                    'entry_delete': int(group['entry_delete']),
                })
                continue

            # MAC Access-list Bind: 0, Unbind: 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('mac_access_list', {}).update({
                    'bind': int(group['bind']),
                    'unbind': int(group['unbind']),
                })
                continue

            # MAC Access-list Delete: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('mac_access_list', {}).update({
                    'delete': int(group['delete']),
                })
                continue

            # Access-list Sync Start: 0, End: 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('access_list_sync', {}).update({
                    'start': int(group['start']),
                    'end': int(group['end']),
                })
                continue

            # QFP Match Add: 0, Replace: 0, ACK Success: 0, ACK Error: 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('qfp_match_add', {}).update({
                    'add': int(group['add']),
                    'replace': int(group['replace']),
                    'ack_success': int(group['ack_success']),
                    'ack_error': int(group['ack_error']),
                })
                continue

            # QFP Match Delete: 0, ACK Success: 0, ACK Error: 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('qfp_match_delete', {}).update({
                    'delete': int(group['delete']),
                    'ack_success': int(group['ack_success']),
                    'ack_error': int(group['ack_error']),
                })
                continue

            # QFP Action Edit: 0, ACK Success: 0, ACK Error: 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('qfp_action_edit', {}).update({
                    'edit': int(group['edit']),
                    'ack_success': int(group['ack_success']),
                    'ack_error': int(group['ack_error']),
                })
                continue

            # QFP Action Replace: 0, ACK Success: 0, ACK Error: 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('qfp_action_replace', {}).update({
                    'replace': int(group['replace']),
                    'ack_success': int(group['ack_success']),
                    'ack_error': int(group['ack_error']),
                })
                continue

            # QFP Bind: 0, ACK Success: 0, ACK Error: 0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('qfp_bind', {}).update({
                    'bind': int(group['bind']),
                    'ack_success': int(group['ack_success']),
                    'ack_error': int(group['ack_error']),
                })
                continue

            # QFP Unbind: 0, ACK Success: 0, ACK Error: 0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('qfp_unbind', {}).update({
                    'unbind': int(group['unbind']),
                    'ack_success': int(group['ack_success']),
                    'ack_error': int(group['ack_error']),
                })
                continue

        return parsed_dict

class ShowPlatformSoftwareNatFpActivePoolSchema(MetaParser):
    """Schema for show platform software nat fp active pool"""
    schema = {
        'nat_pools': {
            int: {  # ID is an integer
                'name': str,
                'type': str,
                'mask': str,
                'flags': str,
                Optional('acct_name'): str,
                'address_range_blocks': int,
                'start': str,
                'end': str,
                'last_stats_update': str,
                'last_refcount_value': int,
            }
        }
    }

class ShowPlatformSoftwareNatFpActivePool(ShowPlatformSoftwareNatFpActivePoolSchema):
    """Parser for show platform software nat fp active pool"""

    cli_command = 'show platform software nat fp active pool'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing the output

        #ID: 3, Name: abc, Type: Generic, Mask: 255.255.255.0
        p1 = re.compile(r'^ID: +(?P<id>\d+), +Name: +(?P<name>\S+), +Type: +(?P<type>\S+), +Mask: +(?P<mask>\S+)$')

        #Flags: Unknown, Acct name:
        p2 = re.compile(r'^Flags: +(?P<flags>\S+), +Acct name: *(?P<acct_name>\S+)?$')
		
        #Address range blocks: 1
        p3 = re.compile(r'^Address range blocks: +(?P<address_range_blocks>\d+)$')

        #Start: 42.0.0.3, End: 42.0.0.3
        p4 = re.compile(r'^Start: +(?P<start>\S+), +End: +(?P<end>\S+)$')

        #Last stats update: 02/20 03:57:22.711119081
        p5 = re.compile(r'^Last stats update: +(?P<last_stats_update>.+)$')

        #Last refcount value: 1
        p6 = re.compile(r'^Last refcount value: +(?P<last_refcount_value>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            #ID: 3, Name: abc, Type: Generic, Mask: 255.255.255.0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                pool_id = int(group['id'])
                pool_dict = parsed_dict.setdefault('nat_pools', {}).setdefault(pool_id, {})
                pool_dict.update({
                    'name': group['name'],
                    'type': group['type'],
                    'mask': group['mask']
                })
                continue

            #Flags: Unknown, Acct name:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group['acct_name']:
                    pool_dict.update({
                        'flags': group['flags'],
                        'acct_name': group['acct_name']
                    })
                else:
                    pool_dict.update({
                        'flags': group['flags']
                    })
                continue

            #Address range blocks: 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                pool_dict.update({
                    'address_range_blocks': int(group['address_range_blocks'])
                })
                continue

            #Start: 42.0.0.3, End: 42.0.0.3
            m = p4.match(line)
            if m:
                group = m.groupdict()
                pool_dict.update({
                    'start': group['start'],
                    'end': group['end']
                })
                continue

            #Last stats update: 02/20 03:57:22.711119081
            m = p5.match(line)
            if m:
                group = m.groupdict()
                pool_dict.update({
                    'last_stats_update': group['last_stats_update']
                })
                continue

            #Last refcount value: 1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                pool_dict.update({
                    'last_refcount_value': int(group['last_refcount_value'])
                })
                continue

        return parsed_dict

class ShowPlatformSoftwareNatFpActiveMappingDynamicSchema(MetaParser):
    """Schema for show platform software nat fp active mapping dynamic"""

    schema = {
        'mapping_id': {
            int: {
                'domain': str,
                'lookup': str,
                'flags': ListOf(str),
                'pool_name': str,
                'pool_id': int,
                'route_map_name': str,
                'cgm_class_group': str,
                'cgm_class_id': int,
                'dynamic_pat': str,
                'last_stats_update': str,
                'last_refcount_value': int,
        }
    }
}

class ShowPlatformSoftwareNatFpActiveMappingDynamic(ShowPlatformSoftwareNatFpActiveMappingDynamicSchema):
    """Parser for show platform software nat fp active mapping dynamic"""

    cli_command = 'show platform software nat fp active mapping dynamic'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing the output
        # Define regex patterns for each line of interest

        #Mapping id: 2
        p1 = re.compile(r'^Mapping +id: +(?P<mapping_id>\d+)$')

        #Domain: INSIDE, Lookup: LOOKUP_LOCAL
        p2 = re.compile(r'^Domain: +(?P<domain>\S+), +Lookup: +(?P<lookup>\S+)$')

        #Flags: routemap
        p3 = re.compile(r'^Flags: +(?P<flags>\S+)$')

        #Pool name: xyz, Pool id: 2
        p4 = re.compile(r'^Pool +name: +(?P<pool_name>\S+), +Pool +id: +(?P<pool_id>\d+)$')

        #Route-map name: NAT-MAP
        p5 = re.compile(r'^Route-map +name: +(?P<route_map_name>\S+)$')

        #CGM class group: INSIDE_SRC_CG, CGM class id: 268435458
        p6 = re.compile(r'^CGM +class +group: +(?P<cgm_class_group>\S+), +CGM +class +id: +(?P<cgm_class_id>\d+)$')

        #Dynamic PAT: No
        p7 = re.compile(r'^Dynamic +PAT: +(?P<dynamic_pat>\S+)$')

        #Last stats update: 02/20 03:56:32.711040681
        p8 = re.compile(r'^Last +stats +update: +(?P<last_stats_update>.+)$')

        #Last refcount value: 5 
        p9 = re.compile(r'^Last +refcount +value: +(?P<last_refcount_value>\d+)$')

        # Iterate over each line in the output
        for line in output.splitlines():
            line = line.strip()

            #Mapping id: 2
            m = p1.match(line)
            if m:
                mapping_id = int(m.group('mapping_id'))
                mapping_dict = parsed_dict.setdefault('mapping_id', {}).setdefault(mapping_id, {})
                continue

            #Domain: INSIDE, Lookup: LOOKUP_LOCAL
            m = p2.match(line)
            if m:
                mapping_dict['domain'] = m.group('domain')
                mapping_dict['lookup'] = m.group('lookup')
                continue

            #Flags: routemap
            m = p3.match(line)
            if m:
                mapping_dict['flags'] = m.group('flags').split(',')
                continue

            #Pool name: xyz, Pool id: 2
            m = p4.match(line)
            if m:
                mapping_dict['pool_name'] = m.group('pool_name')
                mapping_dict['pool_id'] = int(m.group('pool_id'))
                continue

            #Route-map name: NAT-MAP
            m = p5.match(line)
            if m:
                mapping_dict['route_map_name'] = m.group('route_map_name')
                continue

            #CGM class group: INSIDE_SRC_CG, CGM class id: 268435458
            m = p6.match(line)
            if m:
                mapping_dict['cgm_class_group'] = m.group('cgm_class_group')
                mapping_dict['cgm_class_id'] = int(m.group('cgm_class_id'))
                continue

            #Dynamic PAT: No
            m = p7.match(line)
            if m:
                mapping_dict['dynamic_pat'] = m.group('dynamic_pat')
                continue

            #Last stats update: 02/20 03:56:32.711040681
            m = p8.match(line)
            if m:
                mapping_dict['last_stats_update'] = m.group('last_stats_update')
                continue

            #Last refcount value: 5
            m = p9.match(line)
            if m:
                mapping_dict['last_refcount_value'] = int(m.group('last_refcount_value'))
                continue

        return parsed_dict

class ShowPlatformSoftwareMemoryForwardingManagerSchema(MetaParser):
    """Schema for show platform software memory forwarding-manager F0 brief | include {option}"""
    schema = {
        'module': {
            str: {
                'allocated': int,
                'requested': int,
                'allocs': int,
                'frees': int,
            }
        }
    }
class ShowPlatformSoftwareMemoryForwardingManager(ShowPlatformSoftwareMemoryForwardingManagerSchema):
    """Parser for show platform software memory forwarding-manager F0 brief | include {option}"""

    cli_command = 'show platform software memory forwarding-manager F0 brief | include {option}'

    def cli(self, output=None):
        if output is None:
            # Execute the command to get the output
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expression to match each line of the output
        #nat-pap-settings        168           152           1             0
        p1 = re.compile(r'^(?P<module>[\w\s-]+)\s+(?P<allocated>\d+)\s+(?P<requested>\d+)\s+(?P<allocs>\d+)\s+(?P<frees>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Match the line with the regular expression
            #nat-pap-settings        168           152           1             0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                module = group['module'].strip()
                module_dict = parsed_dict.setdefault('module', {}).setdefault(module, {})
                module_dict['allocated'] = int(group['allocated'])
                module_dict['requested'] = int(group['requested'])
                module_dict['allocs'] = int(group['allocs'])
                module_dict['frees'] = int(group['frees'])

        return parsed_dict

class ShowPlatformSoftwareFirewallFPActivePairsSchema(MetaParser):
    '''Schema for show platform software firewall FP active pairs'''
    schema = {
        'zone_pair': {
            Any(): {
                'source_zone': str,
                'destination_zone': str,
                'obj_id': str,
            }
        }
    }

class ShowPlatformSoftwareFirewallFPActivePairs(ShowPlatformSoftwareFirewallFPActivePairsSchema):
    '''Parser for show platform software firewall FP active pairs'''
    
    cli_command = 'show platform software firewall FP active pairs'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed = {}

        #Zone-Pair Name          Source Zone             Destination Zone        Obj-id
        #------------------------------------------------------------------------------
        #z1-z2                   z1                      z2                      1
        #z2-z1                   z2                      z1                      2
        p1 = re.compile(r'^(?P<zone_pair_name>\S+)\s+(?P<source_zone>\S+)\s+(?P<destination_zone>\S+)\s+(?P<obj_id>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            #Zone-Pair Name          Source Zone             Destination Zone        Obj-id
            #------------------------------------------------------------------------------
            #z1-z2                   z1                      z2                      1
            #z2-z1                   z2                      z1                      2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                zone_pairs_dict = parsed.setdefault('zone_pair', {})
                zone_pairs_dict[group['zone_pair_name']] = {
                    'source_zone': group['source_zone'],
                    'destination_zone': group['destination_zone'],
                    'obj_id': group['obj_id'],
                }

        return parsed

class ShowPlatformSoftwareFirewallRPActiveVrfPmapBindingSchema(MetaParser):
    '''Schema for show platform software firewall RP active vrf-pmap-binding'''
    schema = {
        'vrf': {
            Any(): {
                'vrf_name': str,
                'vrf_id': int,
                'parameter_map': str,
		}
	    }
	}

class ShowPlatformSoftwareFirewallRPActiveVrfPmapBinding(ShowPlatformSoftwareFirewallRPActiveVrfPmapBindingSchema):
    '''Parser for show platform software firewall RP active vrf-pmap-binding
                  show platform software firewall FP active vrf-pmap-binding'''

    cli_command = 'show platform software firewall {processor} active vrf-pmap-binding'

    def cli(self, processor="", output=None):

        if output is None:
            if processor:
                cmd = self.cli_command.format(processor=processor)
                output = self.device.execute(cmd)

            else:
                out = output

        # Init return dictionary
        parsed = {}

        # Regex patterns
        #  VRF Name: default, VRF ID: 0, Parameter-Map: vrf-default
        p1 = re.compile(r'^VRF Name: +(?P<vrf_name>\S+), +VRF ID: +(?P<vrf_id>\d+), +Parameter-Map: +(?P<parameter_map>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Match VRF information
            #VRF Name: default, VRF ID: 0, Parameter-Map: vrf-default
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf_dict = parsed.setdefault('vrf', {}).setdefault(group['vrf_name'], {})
                vrf_dict['vrf_name'] = group['vrf_name']
                vrf_dict['vrf_id'] = int(group['vrf_id'])
                vrf_dict['parameter_map'] = group['parameter_map']

        return parsed

class ShowPlatformSoftwareNatIpaliasSchema(MetaParser):
    schema = {
        'ip_address': {
            Any(): {  # IP address as key
                 'table_id': int
        }
    }
}

class ShowPlatformSoftwareNatIpalias(ShowPlatformSoftwareNatIpaliasSchema):
    """Parser for show platform software nat ipalias"""

    cli_command = 'show platform software nat ipalias'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        parsed = {}

        # IP Address          Table ID
        # 80.0.0.11           0
        p1 = re.compile(r'^(?P<ip_address>\S+)\s+(?P<table_id>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Skip header line
            if 'IP Address' in line and 'Table ID' in line:
                continue

            # Match IP address and table ID
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ip_address_dict = parsed.setdefault('ip_address', {})
                ip_address_dict[group['ip_address']] ={
                     'table_id': int(group['table_id']),
                }

        return parsed

# =================================================
#  Schema for 'show platform software trace level ios rp active | in pki'
# =================================================
class ShowPlatformSoftwareTraceLevelIosRpActiveInPkiSchema(MetaParser):
    """Schema for 'show platform software trace level ios rp active | in pki'"""
    schema = {
        str: str  # module name : level
    }

# =================================================
#  Parser for 'show platform software trace level ios rp active | in pki'
# =================================================
class ShowPlatformSoftwareTraceLevelIosRpActiveInPki(ShowPlatformSoftwareTraceLevelIosRpActiveInPkiSchema):
    """Parser for 'show platform software trace level ios rp active | in pki'"""

    cli_command = 'show platform software trace level ios rp active | in pki'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

            parsed_dict = {}


        # Example line: "pki    Noise"
        p1 = re.compile(r'^(?P<module>\S+)\s+(?P<level>\S+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue
            # Match lines with a module name followed by a log level, e.g., "pki    Noise"
            m = p1.match(line)
            if m:
                module = m.group('module')
                level = m.group('level')
                parsed_dict[module] = level

        return parsed_dict

class ShowPlatformSoftwareFirewallRPActiveZonesSchema(MetaParser):
    '''Schema for show platform software firewall RP active zones
	          show platform software firewall FP active zones'''
schema = {
        'zones': {
            Any(): {
                'zone_name': str,
                'parameter_map': str,
                Optional('obj_id'): int,
            }
        }
    }
class ShowPlatformSoftwareFirewallRPActiveZones(ShowPlatformSoftwareFirewallRPActiveZonesSchema):
    '''Parser for show platform software firewall RP active zones
                  show platform software firewall FP active zones'''

    cli_command = 'show platform software firewall {processor} active zones'

    def cli(self, processor="", output=None):

        if output is None:
            if processor:
                cmd = self.cli_command.format(processor=processor)
                output = self.device.execute(cmd)
            else:
                out = output

        # Init return dictionary
        parsed = {}

        # Regex patterns
        #  Zone Name: in, parameter-map:
        p1_RP = re.compile(r'^Zone +Name: +(?P<zone_name>\S+), +parameter-map: *(?P<parameter_map>.*)$')

        #  Zone Name: in, parameter-map: (null), Obj-id 116
        p1_FP = re.compile(r'^Zone +Name: +(?P<zone_name>\S+), +parameter-map: +(?P<parameter_map>\S+), +Obj-id +(?P<obj_id>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            # Zone Name: in, parameter-map:
            m = p1_RP.match(line)
            if m:
                group = m.groupdict()
                zones_dict = parsed.setdefault('zones', {})
                if group['parameter_map']: # This checks if the string is not empty
                    zones_dict[group['zone_name']] = {
                        'zone_name': group['zone_name'],
                        'parameter_map': group['parameter_map']
                    }
                else: # If parameter_map is empty, only include 'zone_name'
                    zones_dict[group['zone_name']] = {
                        'zone_name': group['zone_name']
                    }

            #  Zone Name: in, parameter-map: (null), Obj-id 116
            m = p1_FP.match(line)
            if m:
                group = m.groupdict()
                zones_dict = parsed.setdefault('zones', {})
                zones_dict[group['zone_name']] = {
                    'zone_name': group['zone_name'],
                    'parameter_map': group['parameter_map'],
                    'obj_id': int(group['obj_id']),
                }
        return parsed

class ShowPlatformSoftwareNatFpActiveMappingStaticSchema(MetaParser):
    """Schema for:
        show platform software nat fp active mapping static
    """

    schema = {
        "mappings": {
            Any(): {
                "vrf_name": str,
                "vrf_id": int,
                "table_id": int,
                "domain": str,
                "lookup": str,
                "proto": str,
                "flags": str,
                "local_addr": str,
                "local_port": int,
                "global_addr": str,
                "global_port": int,
                "network_mask": str,
                "pool_id": int,
                "ig_interface_address": str,
                "route_map_name": str,
                "last_stats_update": str,
                "last_refcount_value": int,
            }
        }
    }


class ShowPlatformSoftwareNatFpActiveMappingStatic(ShowPlatformSoftwareNatFpActiveMappingStaticSchema):
    """Parser for:
        show platform software nat fp active mapping static
    """

    cli_command = "show platform software nat fp active mapping static"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Check for empty output
        if not output.strip():
            return {}

        # Init return dict
        parsed = {}

        # Regex patterns
        # Mapping id
        p1 = re.compile(r"^Mapping +id:\s+(?P<id>\d+)$")
        # VRF line
        p2 = re.compile(
            r"^VRF +name:\s+(?P<vrf_name>\S+), +VRF +id:\s+(?P<vrf_id>\d+), +Table +id:\s+(?P<table_id>\d+)$"
        )
        # Domain / Lookup / Proto
        p3 = re.compile(
            r"^Domain:\s+(?P<domain>\S+), +Lookup:\s+(?P<lookup>\S+), +Proto:\s+(?P<proto>\S+)$"
        )
        # Flags
        p4 = re.compile(r"^Flags:\s+(?P<flags>.+)$")
        # Local addr / port
        p5 = re.compile(
            r"^Local +addr:\s+(?P<local_addr>[\d\.]+), +Local +port:\s+(?P<local_port>\d+)$"
        )
        # Global addr / port
        p6 = re.compile(
            r"^Global +addr:\s+(?P<global_addr>[\d\.]+), +Global +port:\s+(?P<global_port>\d+)$"
        )
        # Network mask
        p7 = re.compile(r"^Network +mask:\s+(?P<network_mask>[\d\.]+)$")
        # Pool ID
        p8 = re.compile(r"^Pool +ID:\s+(?P<pool_id>\d+)$")
        # IG interface address
        p9 = re.compile(r"^IG +is +interface +address:\s+(?P<ig_interface_address>\S+)$")
        # Route-map name
        p10 = re.compile(r"^Route-map +name:\s*(?P<route_map_name>.*)$")
        # Last stats update
        p11 = re.compile(r"^Last +stats +update:\s+(?P<last_stats_update>.*)$")
        # Last refcount value
        p12 = re.compile(r"^Last +refcount +value:\s+(?P<last_refcount_value>\d+)$")

        cur_id = None

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Mapping id
            m = p1.match(line)
            if m:
                cur_id = int(m.group("id"))
                mapping_dict = parsed.setdefault("mappings", {}).setdefault(cur_id, {})
                continue

            # VRF line
            m = p2.match(line)
            if m and cur_id is not None:
                mapping_dict.update(
                    {
                        "vrf_name": m.group("vrf_name"),
                        "vrf_id": int(m.group("vrf_id")),
                        "table_id": int(m.group("table_id")),
                    }
                )
                continue

            # Domain / Lookup / Proto
            m = p3.match(line)
            if m and cur_id is not None:
                mapping_dict.update(
                    {
                        "domain": m.group("domain"),
                        "lookup": m.group("lookup"),
                        "proto": m.group("proto"),
                    }
                )
                continue

            # Flags
            m = p4.match(line)
            if m and cur_id is not None:
                mapping_dict["flags"] = m.group("flags")
                continue

            # Local addr / port
            m = p5.match(line)
            if m and cur_id is not None:
                mapping_dict.update(
                    {
                        "local_addr": m.group("local_addr"),
                        "local_port": int(m.group("local_port")),
                    }
                )
                continue

            # Global addr / port
            m = p6.match(line)
            if m and cur_id is not None:
                mapping_dict.update(
                    {
                        "global_addr": m.group("global_addr"),
                        "global_port": int(m.group("global_port")),
                    }
                )
                continue

            # Network mask
            m = p7.match(line)
            if m and cur_id is not None:
                mapping_dict["network_mask"] = m.group("network_mask")
                continue

            # Pool ID
            m = p8.match(line)
            if m and cur_id is not None:
                mapping_dict["pool_id"] = int(m.group("pool_id"))
                continue

            # IG interface address
            m = p9.match(line)
            if m and cur_id is not None:
                mapping_dict["ig_interface_address"] = m.group("ig_interface_address")
                continue

            # Route-map name
            m = p10.match(line)
            if m and cur_id is not None:
                mapping_dict["route_map_name"] = m.group("route_map_name")
                continue

            # Last stats update
            m = p11.match(line)
            if m and cur_id is not None:
                mapping_dict["last_stats_update"] = m.group("last_stats_update")
                continue

            # Last refcount value
            m = p12.match(line)
            if m and cur_id is not None:
                mapping_dict["last_refcount_value"] = int(m.group("last_refcount_value"))
                continue

        return parsed

# =======================================================
# Schema for 'show platform software nat fp active cpp-stats'
# =======================================================
class ShowPlatformSoftwareNatFpActiveCppStatsSchema(MetaParser):
    """Schema for show platform software nat fp active cpp-stats"""
    schema = {
        Optional('interface'): {
            'add': int,
            'upd': int,
            'del': int,
            'ack': int,
            'err': int,
        },
        Optional('timeout'): {
            'set': int,
            'ack': int,
            'err': int,
        },
        Optional('service'): {
            'set': int,
            'ack': int,
            'err': int,
        },
        Optional('modify_in_progress'): {
            'set': int,
            'ack': int,
            'err': int,
        },
        Optional('esp'): {
            'set': int,
            'ack': int,
            'err': int,
        },
        Optional('dnsv6'): {
            'set': int,
            'ack': int,
            'err': int,
        },
        Optional('settings'): {
            'set': int,
            'ack': int,
            'err': int,
        },
        Optional('pap_settings'): {
            'set': int,
            'ack': int,
            'err': int,
        },
        Optional('flow_entries'): {
            'set': int,
            'ack': int,
            'err': int,
        },
        Optional('pool'): {
            'add': int,
            'del': int,
            'ack': int,
            'err': int,
        },
        Optional('addr_range'): {
            'add': int,
            'upd': int,
            'del': int,
            'ack': int,
            'err': int,
        },
        Optional('static_mapping'): {
            'add': int,
            'upd': int,
            'del': int,
            'ack': int,
            'err': int,
        },
        Optional('dyn_mapping'): {
            'add': int,
            'upd': int,
            'del': int,
            'ack': int,
            'err': int,
        },
        Optional('dyn_pat_mapping'): {
            'add': int,
            'del': int,
            'ack': int,
            'err': int,
        },
        Optional('porlist'): {
            'add': int,
            'del': int,
            'ack': int,
            'err': int,
        },
        Optional('logging'): {
            'add': int,
            'upd': int,
            'del': int,
            'ack': int,
            'err': int,
        },
        Optional('per_vrf_logging'): {
            'add': int,
            'upd': int,
            'del': int,
            'ack': int,
            'err': int,
        },
        Optional('sess_replicate'): {
            'add': int,
            'upd': int,
            'del': int,
            'ack': int,
            'err': int,
        },
        Optional('max_entry'): {
            'set': int,
            'clr': int,
            'ack': int,
            'err': int,
        },
        Optional('ifaddr_change'): {
            'notify': int,
            'ack': int,
            'err': int,
        },
        Optional('debug'): {
            'set': int,
            'clr': int,
            'ack': int,
            'err': int,
        },
        Optional('dp_static_rt'): {
            'add': int,
            'del': int,
            'err': int,
        },
        Optional('dp_ipalias'): {
            'add': int,
            'del': int,
            'err': int,
        },
        Optional('dp_portlist'): {
            'req': int,
            'ret': int,
            'err': int,
        },
        Optional('dp_wlan_sess'): {
            'est': int,
            'term': int,
            'err': int,
        },
        Optional('mib_setup'): {
            'enable': int,
            'disable': int,
            'ack': int,
            'err': int,
        },
        Optional('mib_addr_bind'): {
            'query': int,
            'reply': int,
            'err': int,
        },
        Optional('misc_settings'): {
            'set': int,
            'ack': int,
            'err': int,
        },
        Optional('gatekeeper_settings'): {
            'set': int,
            'ack': int,
            'err': int,
        },
    }

class ShowPlatformSoftwareNatFpActiveCppStats(ShowPlatformSoftwareNatFpActiveCppStatsSchema):
    """Parser for 'show platform software nat fp active cpp-stats'"""

    cli_command = 'show platform software nat fp active cpp-stats'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # interface add: 10, upd: 0, del: 5, ack: 6, err: 0
        p1 = re.compile(
            r'^interface add: (?P<add>\d+), upd: (?P<upd>\d+), del: (?P<del>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # timeout set: 24, ack: 24, err: 0
        p2 = re.compile(
            r'^timeout set: (?P<set>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # service set: 54, ack: 54, err: 0
        p3 = re.compile(
            r'^service set: (?P<set>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # modify-in-progress set: 0, ack: 0, err: 0
        p4 = re.compile(
            r'^modify-in-progress set: (?P<set>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # esp set: 0, ack: 0, err: 0
        p5 = re.compile(
            r'^esp set: (?P<set>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # dnsv6 set: 1, ack: 1, err: 0
        p6 = re.compile(
            r'^dnsv6 set: (?P<set>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # settings set: 0, ack: 0, err: 0
        p7 = re.compile(
            r'^settings set: (?P<set>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # PAP settings set: 0, ack: 0, err: 0
        p8 = re.compile(
            r'^PAP settings set: (?P<set>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # Flow entries set: 1, ack: 1, err: 0
        p9 = re.compile(
            r'^Flow entries set: (?P<set>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # pool add: 1, del: 0, ack: 1, err: 0
        p10 = re.compile(
            r'^pool add: (?P<add>\d+), del: (?P<del>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # addr range add: 1, upd: 0, del: 0, ack: 1, err: 0
        p11 = re.compile(
            r'^addr range add: (?P<add>\d+), upd: (?P<upd>\d+), del: (?P<del>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # static mapping add: 2, upd: 0, del: 2, ack: 0, err: 0
        p12 = re.compile(
            r'^static mapping add: (?P<add>\d+), upd: (?P<upd>\d+), del: (?P<del>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # dyn mapping add: 1, upd: 0, del: 0, ack: 1, err: 0
        p13 = re.compile(
            r'^dyn mapping add: (?P<add>\d+), upd: (?P<upd>\d+), del: (?P<del>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # dyn pat mapping add: 0, del: 0, ack: 0, err: 0
        p14 = re.compile(
            r'^dyn pat mapping add: (?P<add>\d+), del: (?P<del>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # porlist add: 0, del: 0, ack: 0, err: 0
        p15 = re.compile(
            r'^porlist add: (?P<add>\d+), del: (?P<del>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # Logging add: 0, upd: 0, del: 0, ack: 0, err: 0
        p16 = re.compile(
            r'^Logging add: (?P<add>\d+), upd: (?P<upd>\d+), del: (?P<del>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # Per-VRF logging add: 0, upd: 0, del: 0, ack: 0, err: 0
        p17 = re.compile(
            r'^Per-VRF logging add: (?P<add>\d+), upd: (?P<upd>\d+), del: (?P<del>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # Sess replicate add: 1, upd: 0, del: 1, ack: 2, err: 0
        p18 = re.compile(
            r'^Sess replicate add: (?P<add>\d+), upd: (?P<upd>\d+), del: (?P<del>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # max entry set: 1, clr: 0, ack: 1, err: 0
        p19 = re.compile(
            r'^max entry set: (?P<set>\d+), clr: (?P<clr>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # ifaddr change notify: 0, ack: 0, err: 0
        p20 = re.compile(
            r'^ifaddr change notify: (?P<notify>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # debug set: 0, clr: 0, ack: 0, err: 0
        p21 = re.compile(
            r'^debug set: (?P<set>\d+), clr: (?P<clr>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # dp static-rt add: 0, del: 0, err: 0
        p22 = re.compile(
            r'^dp static-rt add: (?P<add>\d+), del: (?P<del>\d+), err: (?P<err>\d+)$'
        )
        # dp ipalias add: 4, del: 2, err: 0
        p23 = re.compile(
            r'^dp ipalias add: (?P<add>\d+), del: (?P<del>\d+), err: (?P<err>\d+)$'
        )
        # dp portlist req: 0, ret: 0, err: 0
        p24 = re.compile(
            r'^dp portlist req: (?P<req>\d+), ret: (?P<ret>\d+), err: (?P<err>\d+)$'
        )
        # dp wlan sess est: 0, term: 0, err: 0
        p25 = re.compile(
            r'^dp wlan sess est: (?P<est>\d+), term: (?P<term>\d+), err: (?P<err>\d+)$'
        )
        # mib setup enable: 0, disable: 0, ack: 0, err: 0
        p26 = re.compile(
            r'^mib setup enable: (?P<enable>\d+), disable: (?P<disable>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # mib addr-bind query: 0, reply: 0, err: 0
        p27 = re.compile(
            r'^mib addr-bind query: (?P<query>\d+), reply: (?P<reply>\d+), err: (?P<err>\d+)$'
        )
        # MISC settings set: 0, ack: 0, err: 0
        p28 = re.compile(
            r'^MISC settings set: (?P<set>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )
        # Gatekeeper settings set: 0, ack: 0, err: 0
        p29 = re.compile(
            r'^Gatekeeper settings set: (?P<set>\d+), ack: (?P<ack>\d+), err: (?P<err>\d+)$'
        )

        for line in output.splitlines():
            line = line.strip()

            # interface add: 10, upd: 0, del: 5, ack: 6, err: 0
            m = p1.match(line)
            if m:
                parsed_dict.setdefault('interface', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # timeout set: 24, ack: 24, err: 0
            m = p2.match(line)
            if m:
                parsed_dict.setdefault('timeout', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # service set: 54, ack: 54, err: 0
            m = p3.match(line)
            if m:
                parsed_dict.setdefault('service', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # modify-in-progress set: 0, ack: 0, err: 0
            m = p4.match(line)
            if m:
                parsed_dict.setdefault('modify_in_progress', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # esp set: 0, ack: 0, err: 0
            m = p5.match(line)
            if m:
                parsed_dict.setdefault('esp', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # dnsv6 set: 1, ack: 1, err: 0
            m = p6.match(line)
            if m:
                parsed_dict.setdefault('dnsv6', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # settings set: 0, ack: 0, err: 0
            m = p7.match(line)
            if m:
                parsed_dict.setdefault('settings', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # PAP settings set: 0, ack: 0, err: 0
            m = p8.match(line)
            if m:
                parsed_dict.setdefault('pap_settings', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # Flow entries set: 1, ack: 1, err: 0
            m = p9.match(line)
            if m:
                parsed_dict.setdefault('flow_entries', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # pool add: 1, del: 0, ack: 1, err: 0
            m = p10.match(line)
            if m:
                parsed_dict.setdefault('pool', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # addr range add: 1, upd: 0, del: 0, ack: 1, err: 0
            m = p11.match(line)
            if m:
                parsed_dict.setdefault('addr_range', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # static mapping add: 2, upd: 0, del: 2, ack: 0, err: 0
            m = p12.match(line)
            if m:
                parsed_dict.setdefault('static_mapping', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # dyn mapping add: 1, upd: 0, del: 0, ack: 1, err: 0
            m = p13.match(line)
            if m:
                parsed_dict.setdefault('dyn_mapping', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # dyn pat mapping add: 0, del: 0, ack: 0, err: 0
            m = p14.match(line)
            if m:
                parsed_dict.setdefault('dyn_pat_mapping', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # porlist add: 0, del: 0, ack: 0, err: 0
            m = p15.match(line)
            if m:
                parsed_dict.setdefault('porlist', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # Logging add: 0, upd: 0, del: 0, ack: 0, err: 0
            m = p16.match(line)
            if m:
                parsed_dict.setdefault('logging', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # Per-VRF logging add: 0, upd: 0, del: 0, ack: 0, err: 0
            m = p17.match(line)
            if m:
                parsed_dict.setdefault('per_vrf_logging', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # Sess replicate add: 1, upd: 0, del: 1, ack: 2, err: 0
            m = p18.match(line)
            if m:
                parsed_dict.setdefault('sess_replicate', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # max entry set: 1, clr: 0, ack: 1, err: 0
            m = p19.match(line)
            if m:
                parsed_dict.setdefault('max_entry', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # ifaddr change notify: 0, ack: 0, err: 0
            m = p20.match(line)
            if m:
                parsed_dict.setdefault('ifaddr_change', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # debug set: 0, clr: 0, ack: 0, err: 0
            m = p21.match(line)
            if m:
                parsed_dict.setdefault('debug', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # dp static-rt add: 0, del: 0, err: 0
            m = p22.match(line)
            if m:
                parsed_dict.setdefault('dp_static_rt', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # dp ipalias add: 4, del: 2, err: 0
            m = p23.match(line)
            if m:
                parsed_dict.setdefault('dp_ipalias', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # dp portlist req: 0, ret: 0, err: 0
            m = p24.match(line)
            if m:
                parsed_dict.setdefault('dp_portlist', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # dp wlan sess est: 0, term: 0, err: 0
            m = p25.match(line)
            if m:
                parsed_dict.setdefault('dp_wlan_sess', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # mib setup enable: 0, disable: 0, ack: 0, err: 0
            m = p26.match(line)
            if m:
                parsed_dict.setdefault('mib_setup', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # mib addr-bind query: 0, reply: 0, err: 0
            m = p27.match(line)
            if m:
                parsed_dict.setdefault('mib_addr_bind', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # MISC settings set: 0, ack: 0, err: 0
            m = p28.match(line)
            if m:
                parsed_dict.setdefault('misc_settings', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # Gatekeeper settings set: 0, ack: 0, err: 0
            m = p29.match(line)
            if m:
                parsed_dict.setdefault('gatekeeper_settings', {}).update({k: int(v) for k, v in m.groupdict().items()})
                continue

        return parsed_dict

# =======================================================
# Schema for 'show platform software nat fp active translation'
# =======================================================
class ShowPlatformSoftwareNatFpActiveTranslationSchema(MetaParser):
    """Schema for show platform software nat fp active translation"""
    schema = {
        Optional('translations'): {
            Any(): {  # protocol (udp, tcp, icmp)
                'inside_global': str,
                'inside_local': str,
                'outside_local': str,
                'outside_global': str,
            }
        },
        'total_number_of_translations': int,
    }

# =======================================================
# Parser for 'show platform software nat fp active translation'
# =======================================================
class ShowPlatformSoftwareNatFpActiveTranslation(ShowPlatformSoftwareNatFpActiveTranslationSchema):
    """Parser for show platform software nat fp active translation"""

    cli_command = 'show platform software nat fp active translation'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initial return dictionary
        ret_dict = {}

        # Pro  Inside global         Inside local          Outside local         Outside global
        # udp  110.100.1.1:49186     5.0.0.2:49186         110.1.1.1:33438       110.1.1.1:33438
        # tcp  120.100.1.1:60371     5.0.0.2:60371         120.1.1.1:23          120.1.1.1:23
        # icmp 120.100.1.1:8         5.0.0.2:8             120.1.1.1:8           120.1.1.8
        p1 = re.compile(r'^(?P<protocol>\w+)\s+(?P<inside_global>\S+)\s+(?P<inside_local>\S+)\s+(?P<outside_local>\S+)\s+(?P<outside_global>\S+)$')

        # Total number of translations: 8
        p2 = re.compile(r'^Total\s+number\s+of\s+translations:\s+(?P<total>\d+)$')

        translation_count = 1

        for line in output.splitlines():
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Pro  Inside global         Inside local          Outside local         Outside global
            if line.startswith('Pro') and 'Inside global' in line:
                continue

            # Total number of translations: 8
            match = p2.match(line)
            if match:
                total_translations = int(match.group('total'))
                ret_dict['total_number_of_translations'] = total_translations
                continue

            # udp  110.100.1.1:49186     5.0.0.2:49186         110.1.1.1:33438       110.1.1.1:33438
            # tcp  120.100.1.1:60371     5.0.0.2:60371         120.1.1.1:23          120.1.1.1:23
            # icmp 120.100.1.1:8         5.0.0.2:8             120.1.1.1:8           120.1.1.8
            # Only match lines that don't start with "Total"
            if not line.startswith('Total'):
                match = p1.match(line)
                if match:
                    protocol = match.group('protocol')
                    inside_global = match.group('inside_global')
                    inside_local = match.group('inside_local')
                    outside_local = match.group('outside_local')
                    outside_global = match.group('outside_global')

                    # Create a unique key for each translation entry
                    translation_key = f"{protocol}_{translation_count}"
                    
                    translation_dict = ret_dict.setdefault('translations', {})
                    translation_dict[translation_key] = {
                        'inside_global': inside_global,
                        'inside_local': inside_local,
                        'outside_local': outside_local,
                        'outside_global': outside_global,
                    }
                    
                    translation_count += 1
                    continue

        return ret_dict

# =======================================================
# Schema for 'show platform software firewall RP active parameter-maps'
# =======================================================
class ShowPlatformSoftwareFirewallRPActiveParameterMapsSchema(MetaParser):
    """Schema for show platform software firewall RP active parameter-maps"""
    schema = {
        'parameter_maps': {
            Any(): {
                'parameter_map_type': str,
                Optional('global_parameter_map'): bool,
                Optional('alerts'): str,
                Optional('audits'): str,
                Optional('drop_log'): str,
                Optional('log_flow'): str,
                Optional('hsl_mode'): str,
                Optional('host'): str,
                Optional('port'): int,
                Optional('template'): str,
                Optional('zone_mismatch_drop'): str,
                Optional('multi_tenancy'): str,
                Optional('icmp_ureachable_allowed'): str,
                Optional('session_rate'): {
                    'high': int,
                    'low': int,
                    'time_duration': str,
                },
                Optional('half_open'): {
                    'high': int,
                    'low': int,
                    'host': int,
                    'host_block_time': int,
                },
                Optional('inactivity_times'): {
                    'dns': int,
                    'icmp': int,
                    'tcp': int,
                    'udp': int,
                },
                Optional('inactivity_age_out_times'): {
                    'icmp': int,
                    'tcp': int,
                    'udp': int,
                },
                Optional('tcp_timeouts'): {
                    'syn_wait_time': int,
                    'fin_wait_time': int,
                },
                Optional('tcp_ageout_timeouts'): {
                    'syn_wait_time': int,
                    'fin_wait_time': int,
                },
                Optional('tcp_rst_pkt_control'): {
                    'half_open': str,
                    'half_close': str,
                    'idle': str,
                },
                Optional('udp_timeout'): {
                    'udp_half_open_time': int,
                },
                Optional('udp_ageout_timeout'): {
                    'udp_half_open_time': int,
                },
                Optional('max_sessions'): str,
                Optional('number_of_simultaneous_packet_per_sessions'): int,
                Optional('syn_cookie_and_resource_management'): {
                    'global_syn_flood_limit': int,
                    'global_total_session': int,
                    Optional('global_number_of_simultaneous_packet_per_session'): str,
                },
                Optional('global_total_session_aggressive_aging'): str,
                Optional('global_alert'): str,
                Optional('global_max_incomplete'): int,
                Optional('global_max_incomplete_tcp'): int,
                Optional('global_max_incomplete_udp'): int,
                Optional('global_max_incomplete_icmp'): int,
                Optional('global_max_incomplete_aggressive_aging'): str,
                Optional('per_box_configuration'): {
                    'syn_flood_limit': int,
                    'total_session_aggressive_aging': str,
                    'max_incomplete': int,
                    'max_incomplete_tcp': int,
                    'max_incomplete_udp': int,
                    'max_incomplete_icmp': int,
                    'max_incomplete_aggressive_aging': str,
                },
                Optional('application_protocol_control'): {
                    Any(): {
                        'protocol': str,
                        'status': str,
                    }
                },
                Optional('vrf_pmap_syn_flood_limit'): int,
                Optional('vrf_pmap_total_session'): int,
                Optional('vrf_pmap_total_session_aggressive_aging'): str,
                Optional('vrf_pmap_alert'): str,
                Optional('vrf_pmap_max_incomplete'): int,
                Optional('vrf_pmap_max_incomplete_tcp'): int,
                Optional('vrf_pmap_max_incomplete_udp'): int,
                Optional('vrf_pmap_max_incomplete_icmp'): int,
                Optional('vrf_pmap_max_incomplete_aggressive_aging'): str,
            }
        }
    }


# =======================================================
# Parser for 'show platform software firewall RP active parameter-maps'
# =======================================================
class ShowPlatformSoftwareFirewallRPActiveParameterMaps(ShowPlatformSoftwareFirewallRPActiveParameterMapsSchema):
    """Parser for show platform software firewall RP active parameter-maps"""

    cli_command = 'show platform software firewall RP active parameter-maps'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize return dictionary
        ret_dict = {}

        # Regex patterns
        # Inspect Parameter Map: global
        p1 = re.compile(r'^\s*Inspect Parameter Map:\s+(?P<param_map_name>\S+)$')

        # Parameter Map Type: Parameter-Map
        p2 = re.compile(r'^\s*Parameter Map Type:\s+(?P<param_map_type>.+)$')

        # Global Parameter-Map
        p3 = re.compile(r'^\s*Global Parameter-Map$')

        # Alerts: On, Audits: Off, Drop-Log: On, Log flow: Off
        p4 = re.compile(r'^\s*Alerts:\s+(?P<alerts>\S+),\s+Audits:\s+(?P<audits>\S+),\s+Drop-Log:\s+(?P<drop_log>\S+),\s+Log flow:\s+(?P<log_flow>\S+)$')

        # HSL Mode: Disabled, Host: :0, Port: 0, Template: 300 sec
        p5 = re.compile(r'^\s*HSL Mode:\s+(?P<hsl_mode>\S+),\s+Host:\s+(?P<host>\S+),\s+Port:\s+(?P<port>\d+),\s+Template:\s+(?P<template>.+)$')

        # Zone mismatch drop: Off
        p6 = re.compile(r'^\s*Zone mismatch drop:\s+(?P<zone_mismatch_drop>\S+)$')

        # Multi tenancy: Off
        p7 = re.compile(r'^\s*Multi tenancy:\s+(?P<multi_tenancy>\S+)$')

        # ICMP ureachable allowed: No
        p8 = re.compile(r'^\s*ICMP ureachable allowed:\s+(?P<icmp_ureachable_allowed>\S+)$')

        # Session Rate High: 2147483647, Session Rate Low: 2147483647, Time Duration: 60 sec
        p9 = re.compile(r'^\s*Session Rate High:\s+(?P<high>\d+),\s+Session Rate Low:\s+(?P<low>\d+),\s+Time Duration:\s+(?P<time_duration>.+)$')

        # High: 2147483647, Low: 2147483647, Host: 4294967295, Host Block Time: 0
        p10 = re.compile(r'^\s*High:\s+(?P<high>\d+),\s+Low:\s+(?P<low>\d+),\s+Host:\s+(?P<host>\d+),\s+Host Block Time:\s+(?P<host_block_time>\d+)$')

        # DNS: 5, ICMP: 10, TCP: 3600, UDP: 30
        p11 = re.compile(r'^\s*DNS:\s+(?P<dns>\d+),\s+ICMP:\s+(?P<icmp>\d+),\s+TCP:\s+(?P<tcp>\d+),\s+UDP:\s+(?P<udp>\d+)$')

        # ICMP: 10, TCP: 3600, UDP: 30
        p12 = re.compile(r'^\s*ICMP:\s+(?P<icmp>\d+),\s+TCP:\s+(?P<tcp>\d+),\s+UDP:\s+(?P<udp>\d+)$')

        # SYN wait time: 30, FIN wait time: 1
        p13 = re.compile(r'^\s*SYN wait time:\s+(?P<syn_wait_time>\d+),\s+FIN wait time:\s+(?P<fin_wait_time>\d+)$')

        # half-open: On, half-close: On, idle: On
        p14 = re.compile(r'^\s*half-open:\s+(?P<half_open>\S+),\s+half-close:\s+(?P<half_close>\S+),\s+idle:\s+(?P<idle>\S+)$')

        # UDP Half-open time: 30000
        p15 = re.compile(r'^\s*UDP Half-open time:\s+(?P<udp_half_open_time>\d+)$')

        # Max Sessions: Unlimited
        p16 = re.compile(r'^\s*Max Sessions:\s+(?P<max_sessions>.+)$')

        # Number of Simultaneous Packet per Sessions: 0
        p17 = re.compile(r'^\s*Number of Simultaneous Packet per Sessions:\s+(?P<simultaneous_packets>\d+)$')

        # Global Syn Flood Limit: 4294967295
        p18 = re.compile(r'^\s*Global Syn Flood Limit:\s+(?P<global_syn_flood_limit>\d+)$')

        # Global Total Session : 4294967295
        p19 = re.compile(r'^\s*Global Total Session\s+:\s+(?P<global_total_session>\d+)$')

        # Global Number of Simultaneous Packet per Session :
        p20 = re.compile(r'^\s*Global Number of Simultaneous Packet per Session\s+:\s*(?P<global_simultaneous>.*)$')

        # Global Total Session Aggressive Aging Disabled
        p21 = re.compile(r'^\s*Global Total Session Aggressive Aging\s+(?P<aggressive_aging>\S+)$')

        # Global alert : Off
        p22 = re.compile(r'^\s*Global alert\s+:\s+(?P<global_alert>\S+)$')

        # Global max incomplete : 4294967295
        p23 = re.compile(r'^\s*Global max incomplete\s+:\s+(?P<global_max_incomplete>\d+)$')

        # Global max incomplete TCP: 4294967295
        p24 = re.compile(r'^\s*Global max incomplete TCP:\s+(?P<global_max_incomplete_tcp>\d+)$')

        # Global max incomplete UDP: 4294967295
        p25 = re.compile(r'^\s*Global max incomplete UDP:\s+(?P<global_max_incomplete_udp>\d+)$')

        # Global max incomplete ICMP: 4294967295
        p26 = re.compile(r'^\s*Global max incomplete ICMP:\s+(?P<global_max_incomplete_icmp>\d+)$')

        # Global max incomplete Aggressive Aging Disabled
        p27 = re.compile(r'^\s*Global max incomplete Aggressive Aging\s+(?P<global_max_incomplete_aging>\S+)$')

        # syn flood limit : 4294967295
        p28 = re.compile(r'^\s*syn flood limit\s+:\s+(?P<syn_flood_limit>\d+)$')

        # Total Session Aggressive Aging Disabled
        p29 = re.compile(r'^\s*Total Session Aggressive Aging\s+(?P<total_session_aging>\S+)$')

        # max incomplete : 4294967295
        p30 = re.compile(r'^\s*max incomplete\s+:\s+(?P<max_incomplete>\d+)$')

        # max incomplete TCP: 4294967295
        p31 = re.compile(r'^\s*max incomplete TCP:\s+(?P<max_incomplete_tcp>\d+)$')

        # max incomplete UDP: 4294967295
        p32 = re.compile(r'^\s*max incomplete UDP:\s+(?P<max_incomplete_udp>\d+)$')

        # max incomplete ICMP: 4294967295
        p33 = re.compile(r'^\s*max incomplete ICMP:\s+(?P<max_incomplete_icmp>\d+)$')

        # max incomplete Aggressive Aging Disabled
        p34 = re.compile(r'^\s*max incomplete Aggressive Aging\s+(?P<max_incomplete_aging>\S+)$')

        #         Protocol         Status
        #        dns              on
        
        p35 = re.compile(r'^\s*(?P<protocol>\S+)\s+(?P<status>\S+)$')

        # VRF PMAP lines
        # VRF PMAP syn flood limit : 4294967295
        p36 = re.compile(r'^\s*VRF PMAP syn flood limit\s+:\s+(?P<vrf_syn_flood_limit>\d+)$')

        # VRF PMAP total session : 4294967295
        p37 = re.compile(r'^\s*VRF PMAP total session\s+:\s+(?P<vrf_total_session>\d+)$')

        # VRF PMAP total session Aggressive Aging Disabled
        p38 = re.compile(r'^\s*VRF PMAP total session Aggressive Aging\s+(?P<vrf_total_session_aging>\S+)$')

        # VRF PMAP alert : Off
        p39 = re.compile(r'^\s*VRF PMAP alert\s+:\s+(?P<vrf_alert>\S+)$')

        # VRF PMAP max incomplete : 4294967295
        p40 = re.compile(r'^\s*VRF PMAP max incomplete\s+:\s+(?P<vrf_max_incomplete>\d+)$')

        # VRF PMAP max incomplete TCP: 4294967295
        p41 = re.compile(r'^\s*VRF PMAP max incomplete TCP:\s+(?P<vrf_max_incomplete_tcp>\d+)$')

        # VRF PMAP max incomplete UDP: 4294967295
        p42 = re.compile(r'^\s*VRF PMAP max incomplete UDP:\s+(?P<vrf_max_incomplete_udp>\d+)$')

        # VRF PMAP max incomplete ICMP: 4294967295
        p43 = re.compile(r'^\s*VRF PMAP max incomplete ICMP:\s+(?P<vrf_max_incomplete_icmp>\d+)$')

        # VRF PMAP max incomplete Aggressive Aging Disabled
        p44 = re.compile(r'^\s*VRF PMAP max incomplete Aggressive Aging\s+(?P<vrf_max_incomplete_aging>\S+)$')

        # Section headers to track context
        # Half-Open:
        p45 = re.compile(r'^\s*Half-Open:$')

        # Inactivity Times [sec]:
        p46 = re.compile(r'^\s*Inactivity Times \[sec\]:$')

        # Inactivity Age-out Times [sec]:
        p47 = re.compile(r'^\s*Inactivity Age-out Times \[sec\]:$')

        # TCP Timeouts [sec]:
        p48 = re.compile(r'^\s*TCP Timeouts \[sec\]:$')

        # TCP Ageout Timeouts [sec]:
        p49 = re.compile(r'^\s*TCP Ageout Timeouts \[sec\]:$')

        # TCP RST pkt control:
        p50 = re.compile(r'^\s*TCP RST pkt control:$')

        # UDP Timeout [msec]:
        p51 = re.compile(r'^\s*UDP Timeout \[msec\]:$')

        # UDP Ageout Timeout [msec]:
        p52 = re.compile(r'^\s*UDP Ageout Timeout \[msec\]:$')

        # Syn Cookie and Resource Management:
        p53 = re.compile(r'^\s*Syn Cookie and Resource Management:$')

        # Per Box Configuration
        p54 = re.compile(r'^\s*Per Box Configuration$')

        # Application protocol control:
        p55 = re.compile(r'^\s*Application protocol control:$')

        # Protocol         Status
        p56 = re.compile(r'^\s*Protocol\s+Status$')

        # --------------------------------
        p57 = re.compile(r'^\s*-+$')

        current_param_map = None
        current_section = None
        protocol_counter = 0

        for line in output.splitlines():
            line = line.strip()

            # Skip empty lines and separators
            if not line or p57.match(line) or p56.match(line):
                continue

            # Parse parameter map name
            # Inspect Parameter Map: global
            m = p1.match(line)
            if m:
                param_map_name = m.group('param_map_name')
                current_param_map = param_map_name
                param_maps_dict = ret_dict.setdefault('parameter_maps', {})
                param_maps_dict[param_map_name] = {}
                current_section = None
                protocol_counter = 0
                continue

            if not current_param_map:
                continue

            param_dict = ret_dict['parameter_maps'][current_param_map]

            # Parse parameter map type
            # Parameter Map Type: Parameter-Map
            m = p2.match(line)
            if m:
                param_dict['parameter_map_type'] = m.group('param_map_type')
                continue

            # Parse global parameter map
            # Global Parameter-Map
            m = p3.match(line)
            if m:
                param_dict['global_parameter_map'] = True
                continue

            # Parse alerts and audits
            # Alerts: On, Audits: Off, Drop-Log: On, Log flow: Off
            m = p4.match(line)
            if m:
                param_dict['alerts'] = m.group('alerts')
                param_dict['audits'] = m.group('audits')
                param_dict['drop_log'] = m.group('drop_log')
                param_dict['log_flow'] = m.group('log_flow')
                continue

            # Parse HSL mode
            # HSL Mode: Disabled, Host: :0, Port: 0, Template: 300 sec
            m = p5.match(line)
            if m:
                param_dict['hsl_mode'] = m.group('hsl_mode')
                param_dict['host'] = m.group('host')
                param_dict['port'] = int(m.group('port'))
                param_dict['template'] = m.group('template')
                continue

            # Parse zone mismatch drop
            # Zone mismatch drop: Off
            m = p6.match(line)
            if m:
                param_dict['zone_mismatch_drop'] = m.group('zone_mismatch_drop')
                continue

            # Parse multi tenancy
            # Multi tenancy: Off
            m = p7.match(line)
            if m:
                param_dict['multi_tenancy'] = m.group('multi_tenancy')
                continue

            # Parse ICMP ureachable
            # ICMP ureachable allowed: No
            m = p8.match(line)
            if m:
                param_dict['icmp_ureachable_allowed'] = m.group('icmp_ureachable_allowed')
                continue

            # Parse session rate
            # Session Rate High: 2147483647, Session Rate Low: 2147483647, Time Duration: 60 sec
            m = p9.match(line)
            if m:
                session_rate_dict = param_dict.setdefault('session_rate', {})
                session_rate_dict['high'] = int(m.group('high'))
                session_rate_dict['low'] = int(m.group('low'))
                session_rate_dict['time_duration'] = m.group('time_duration')
                continue

            # Parse section headers
            # Half-Open:
            if p45.match(line):
                current_section = 'half_open'
                continue

            # Inactivity Times [sec]:
            elif p46.match(line):
                current_section = 'inactivity_times'
                continue

            # Inactivity Age-out Times [sec]:
            elif p47.match(line):
                current_section = 'inactivity_age_out'
                continue

            # TCP Timeouts [sec]:
            elif p48.match(line):
                current_section = 'tcp_timeouts'
                continue

            # TCP Ageout Timeouts [sec]:
            elif p49.match(line):
                current_section = 'tcp_ageout'
                continue

            # TCP RST pkt control:
            elif p50.match(line):
                current_section = 'tcp_rst'
                continue

            # UDP Timeout [msec]:
            elif p51.match(line):
                current_section = 'udp_timeout'
                continue

            # UDP Ageout Timeout [msec]:
            elif p52.match(line):
                current_section = 'udp_ageout'
                continue

            # Syn Cookie and Resource Management:
            elif p53.match(line):
                current_section = 'syn_cookie'
                continue

            # Per Box Configuration
            elif p54.match(line):
                current_section = 'per_box'
                continue

            # Application protocol control:
            elif p55.match(line):
                current_section = 'app_protocol'
                continue

            # Parse based on current section
            if current_section == 'half_open':
                # High: 2147483647, Low: 2147483647, Host: 4294967295, Host Block Time: 0
                m = p10.match(line)
                if m:
                    half_open_dict = param_dict.setdefault('half_open', {})
                    half_open_dict['high'] = int(m.group('high'))
                    half_open_dict['low'] = int(m.group('low'))
                    half_open_dict['host'] = int(m.group('host'))
                    half_open_dict['host_block_time'] = int(m.group('host_block_time'))
                    continue

            elif current_section == 'inactivity_times':
                # DNS: 5, ICMP: 10, TCP: 3600, UDP: 30
                m = p11.match(line)
                if m:
                    inactivity_dict = param_dict.setdefault('inactivity_times', {})
                    inactivity_dict['dns'] = int(m.group('dns'))
                    inactivity_dict['icmp'] = int(m.group('icmp'))
                    inactivity_dict['tcp'] = int(m.group('tcp'))
                    inactivity_dict['udp'] = int(m.group('udp'))
                    continue

            elif current_section == 'inactivity_age_out':
                # ICMP: 10, TCP: 3600, UDP: 30
                m = p12.match(line)
                if m:
                    age_out_dict = param_dict.setdefault('inactivity_age_out_times', {})
                    age_out_dict['icmp'] = int(m.group('icmp'))
                    age_out_dict['tcp'] = int(m.group('tcp'))
                    age_out_dict['udp'] = int(m.group('udp'))
                    continue

            elif current_section in ['tcp_timeouts', 'tcp_ageout']:
                # SYN wait time: 30, FIN wait time: 1
                m = p13.match(line)
                if m:
                    if current_section == 'tcp_timeouts':
                        tcp_dict = param_dict.setdefault('tcp_timeouts', {})
                    else:
                        tcp_dict = param_dict.setdefault('tcp_ageout_timeouts', {})
                    tcp_dict['syn_wait_time'] = int(m.group('syn_wait_time'))
                    tcp_dict['fin_wait_time'] = int(m.group('fin_wait_time'))
                    continue

            elif current_section == 'tcp_rst':
                # half-open: On, half-close: On, idle: On
                m = p14.match(line)
                if m:
                    tcp_rst_dict = param_dict.setdefault('tcp_rst_pkt_control', {})
                    tcp_rst_dict['half_open'] = m.group('half_open')
                    tcp_rst_dict['half_close'] = m.group('half_close')
                    tcp_rst_dict['idle'] = m.group('idle')
                    continue

            elif current_section in ['udp_timeout', 'udp_ageout']:
                # UDP Half-open time: 30000
                m = p15.match(line)
                if m:
                    if current_section == 'udp_timeout':
                        udp_dict = param_dict.setdefault('udp_timeout', {})
                    else:
                        udp_dict = param_dict.setdefault('udp_ageout_timeout', {})
                    udp_dict['udp_half_open_time'] = int(m.group('udp_half_open_time'))
                    continue

            elif current_section == 'app_protocol':
                #         Protocol         Status
                #        dns              on
                m = p35.match(line)
                if m:
                    protocol_counter += 1
                    protocol_key = f"protocol_{protocol_counter}"
                    app_protocol_dict = param_dict.setdefault('application_protocol_control', {})
                    app_protocol_dict[protocol_key] = {
                        'protocol': m.group('protocol'),
                        'status': m.group('status')
                    }
                    continue

            # Parse max sessions
            # Max Sessions: Unlimited
            m = p16.match(line)
            if m:
                param_dict['max_sessions'] = m.group('max_sessions')
                continue

            # Parse simultaneous packets
            # Number of Simultaneous Packet per Sessions: 0
            m = p17.match(line)
            if m:
                param_dict['number_of_simultaneous_packet_per_sessions'] = int(m.group('simultaneous_packets'))
                continue

            # Parse syn cookie and resource management
            if current_section == 'syn_cookie':
                # Global Syn Flood Limit: 4294967295
                m = p18.match(line)
                if m:
                    syn_cookie_dict = param_dict.setdefault('syn_cookie_and_resource_management', {})
                    syn_cookie_dict['global_syn_flood_limit'] = int(m.group('global_syn_flood_limit'))
                    continue

                # Global Total Session : 4294967295
                m = p19.match(line)
                if m:
                    syn_cookie_dict = param_dict.setdefault('syn_cookie_and_resource_management', {})
                    syn_cookie_dict['global_total_session'] = int(m.group('global_total_session'))
                    continue

                # Global Number of Simultaneous Packet per Session :
                m = p20.match(line)
                if m:
                    syn_cookie_dict = param_dict.setdefault('syn_cookie_and_resource_management', {})
                    global_sim = m.group('global_simultaneous').strip()
                    if global_sim:
                        syn_cookie_dict['global_number_of_simultaneous_packet_per_session'] = global_sim
                    continue

            # Parse per box configuration
            if current_section == 'per_box':
                # syn flood limit : 4294967295
                m = p28.match(line)
                if m:
                    per_box_dict = param_dict.setdefault('per_box_configuration', {})
                    per_box_dict['syn_flood_limit'] = int(m.group('syn_flood_limit'))
                    continue

                # Total Session Aggressive Aging Disabled
                m = p29.match(line)
                if m:
                    per_box_dict = param_dict.setdefault('per_box_configuration', {})
                    per_box_dict['total_session_aggressive_aging'] = m.group('total_session_aging')
                    continue

                # max incomplete : 4294967295
                m = p30.match(line)
                if m:
                    per_box_dict = param_dict.setdefault('per_box_configuration', {})
                    per_box_dict['max_incomplete'] = int(m.group('max_incomplete'))
                    continue

                # max incomplete TCP: 4294967295
                m = p31.match(line)
                if m:
                    per_box_dict = param_dict.setdefault('per_box_configuration', {})
                    per_box_dict['max_incomplete_tcp'] = int(m.group('max_incomplete_tcp'))
                    continue

                # max incomplete UDP: 4294967295
                m = p32.match(line)
                if m:
                    per_box_dict = param_dict.setdefault('per_box_configuration', {})
                    per_box_dict['max_incomplete_udp'] = int(m.group('max_incomplete_udp'))
                    continue

                # max incomplete ICMP: 4294967295
                m = p33.match(line)
                if m:
                    per_box_dict = param_dict.setdefault('per_box_configuration', {})
                    per_box_dict['max_incomplete_icmp'] = int(m.group('max_incomplete_icmp'))
                    continue

                # max incomplete Aggressive Aging Disabled
                m = p34.match(line)
                if m:
                    per_box_dict = param_dict.setdefault('per_box_configuration', {})
                    per_box_dict['max_incomplete_aggressive_aging'] = m.group('max_incomplete_aging')
                    continue

            # Parse global settings outside of sections
            # Global Total Session Aggressive Aging Disabled
            m = p21.match(line)
            if m:
                param_dict['global_total_session_aggressive_aging'] = m.group('aggressive_aging')
                continue

            # Global alert : Off
            m = p22.match(line)
            if m:
                param_dict['global_alert'] = m.group('global_alert')
                continue

            # Global max incomplete : 4294967295
            m = p23.match(line)
            if m:
                param_dict['global_max_incomplete'] = int(m.group('global_max_incomplete'))
                continue

            # Global max incomplete TCP: 4294967295
            m = p24.match(line)
            if m:
                param_dict['global_max_incomplete_tcp'] = int(m.group('global_max_incomplete_tcp'))
                continue

            # Global max incomplete UDP: 4294967295
            m = p25.match(line)
            if m:
                param_dict['global_max_incomplete_udp'] = int(m.group('global_max_incomplete_udp'))
                continue

            # Global max incomplete ICMP: 4294967295
            m = p26.match(line)
            if m:
                param_dict['global_max_incomplete_icmp'] = int(m.group('global_max_incomplete_icmp'))
                continue

            # Global max incomplete Aggressive Aging Disabled
            m = p27.match(line)
            if m:
                param_dict['global_max_incomplete_aggressive_aging'] = m.group('global_max_incomplete_aging')
                continue

            # Parse VRF PMAP settings
            # VRF PMAP syn flood limit : 4294967295
            m = p36.match(line)
            if m:
                param_dict['vrf_pmap_syn_flood_limit'] = int(m.group('vrf_syn_flood_limit'))
                continue

            # VRF PMAP total session : 4294967295
            m = p37.match(line)
            if m:
                param_dict['vrf_pmap_total_session'] = int(m.group('vrf_total_session'))
                continue

            # VRF PMAP total session Aggressive Aging Disabled
            m = p38.match(line)
            if m:
                param_dict['vrf_pmap_total_session_aggressive_aging'] = m.group('vrf_total_session_aging')
                continue

            # VRF PMAP alert : Off
            m = p39.match(line)
            if m:
                param_dict['vrf_pmap_alert'] = m.group('vrf_alert')
                continue

            # VRF PMAP max incomplete : 4294967295
            m = p40.match(line)
            if m:
                param_dict['vrf_pmap_max_incomplete'] = int(m.group('vrf_max_incomplete'))
                continue

            # VRF PMAP max incomplete TCP: 4294967295
            m = p41.match(line)
            if m:
                param_dict['vrf_pmap_max_incomplete_tcp'] = int(m.group('vrf_max_incomplete_tcp'))
                continue

            # VRF PMAP max incomplete UDP: 4294967295
            m = p42.match(line)
            if m:
                param_dict['vrf_pmap_max_incomplete_udp'] = int(m.group('vrf_max_incomplete_udp'))
                continue

            # VRF PMAP max incomplete ICMP: 4294967295
            m = p43.match(line)
            if m:
                param_dict['vrf_pmap_max_incomplete_icmp'] = int(m.group('vrf_max_incomplete_icmp'))
                continue

            # VRF PMAP max incomplete Aggressive Aging Disabled
            m = p44.match(line)
            if m:
                param_dict['vrf_pmap_max_incomplete_aggressive_aging'] = m.group('vrf_max_incomplete_aging')
                continue

        return ret_dict


# ==========================================================================================
# Schema for 'show platform software subslot {subslot} module status'  
# ==========================================================================================
class ShowPlatformSoftwareSubslotModuleStatusSchema(MetaParser):
    """Schema for show platform software subslot {subslot} module status"""

    schema = {
        "process_and_memory": {
            "memory_stats": {
                "mem_used_kb": int,
                "mem_free_kb": int,
                "mem_shrd_kb": int,
                "mem_buff_kb": int,
                "mem_cached_kb": int,
            },
            "cpu_stats": {
                "cpu_usr_percent": int,
                "cpu_sys_percent": int,
                "cpu_nic_percent": int,
                "cpu_idle_percent": int,
                "cpu_io_percent": int,
                "cpu_irq_percent": int,
                "cpu_sirq_percent": int,
            },
            "load_average": str,
            "processes": {
                Any(): {
                    "pid": int,
                    "ppid": int,
                    "user": str,
                    "stat": str,
                    "vsz": str,
                    "mem_percent": str,
                    "cpu_percent": str,
                    "command": str,
                }
            },
        },
        "interrupts": {
            Any(): {
                "cpu0": int,
                "controller": str,
                "description": str,
            },
            "err": int,
        },
        "system_status": {
            "cpu": str,
            "intr": str,
            "ctxt": int,
            "btime": int,
            "processes": int,
            "procs_running": int,
            "procs_blocked": int,
        },
        "klm_module_status": {
            "modules": {
                Any(): {
                    "size": int,
                    "used": int,
                    "flags": str,
                    "address": str,
                    Optional("state"): str,
                }
            },
            "wddi_memory": int,
            "qnode_status": int,
        },
    }


class ShowPlatformSoftwareSubslotModuleStatus(ShowPlatformSoftwareSubslotModuleStatusSchema):
    """Parser for show platform software subslot {subslot} module status"""

    cli_command = "show platform software subslot {subslot} module status"

    def cli(self, subslot="0/2", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(subslot=subslot))

        ret_dict = {}

        # Process and Memory
        p1 = re.compile(r"^Process and Memory$")

        # Mem: 46468K used, 14468K free, 0K shrd, 0K buff, 32764K cached
        p2 = re.compile(
            r"^Mem: +(?P<used>\d+)K +used, +(?P<free>\d+)K +free, +"
            r"(?P<shrd>\d+)K +shrd, +(?P<buff>\d+)K +buff, +(?P<cached>\d+)K +cached$"
        )

        # CPU:   0% usr   0% sys   0% nic 100% idle   0% io   0% irq   0% sirq
        p3 = re.compile(
            r"^CPU: +(?P<usr>\d+)% +usr +(?P<sys>\d+)% +sys +(?P<nic>\d+)% +nic +"
            r"(?P<idle>\d+)% +idle +(?P<io>\d+)% +io +(?P<irq>\d+)% +irq +(?P<sirq>\d+)% +sirq$"
        )

        # Load average: 0.06 0.03 0.00 3/20 10258
        p4 = re.compile(r"^Load average: (?P<load_average>.*)$")

        # PID  PPID USER     STAT   VSZ %MEM %CPU COMMAND
        p4_1 = re.compile(r"^PID +PPID +USER +STAT +VSZ +%MEM +%CPU +COMMAND$")

        # Process entries:
        #   158   157 0        R     146m 246%   0% [cisco_fortitude]
        p5 = re.compile(
            r"^(?P<pid>\d+) +(?P<ppid>\d+) +(?P<user>\S+) +(?P<stat>\S+) +"
            r"(?P<vsz>\S+) +(?P<mem_percent>\S+) +(?P<cpu_percent>\S+) +(?P<command>.*)$"
        )

        # Interrupts
        p6 = re.compile(r"^Interrupts$")

        #            CPU0
        p6_1 = re.compile(r"^CPU0$")

        # Interrupt entries like:
        #   2:          0            MIPS  WinPath interrupt controller
        p7 = re.compile(
            r"^(?P<interrupt>\d+): +(?P<cpu0>\d+) +(?P<controller>\S+) +(?P<description>.*)$"
        )

        # ERR:          0
        p8 = re.compile(r"^ERR: +(?P<err>\d+)$")

        # System status
        p9 = re.compile(r"^System status$")

        # cpu  115 0 611 21404 0 0 0 0 0
        p10 = re.compile(r"^cpu +(?P<cpu>.*)$")

        # intr 86063 0 0 0 0 0 0 0 55326 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 544 0 0 0 0 0 0 0 0 0 0 0 0 30193 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
        p11 = re.compile(r"^intr +(?P<intr>.*)$")

        # ctxt 205235
        p12 = re.compile(r"^ctxt +(?P<ctxt>\d+)$")

        # btime 0
        p13 = re.compile(r"^btime +(?P<btime>\d+)$")

        # processes 10236
        p14 = re.compile(r"^processes +(?P<processes>\d+)$")

        # procs_running 2
        p15 = re.compile(r"^procs_running +(?P<procs_running>\d+)$")

        # procs_blocked 0
        p16 = re.compile(r"^procs_blocked +(?P<procs_blocked>\d+)$")

        # KLM Module status
        p17 = re.compile(r"^KLM Module status$")

        # klm_mmap 5917008 4 - Live 0xc05ff000
        p18 = re.compile(
            r"^(?P<module>\S+) +(?P<size>\d+) +(?P<used>\d+) +(?P<flags>\S+) +"
            r"(?P<state>\S+) +(?P<address>\S+)$"
        )

        # klm_ds0dump 2848 0 - Live 0xc0bb2000
        # dmesg 544 0 - Live 0xc0bbb000 (P)
        p19 = re.compile(
            r"^(?P<module>\S+) +(?P<size>\d+) +(?P<used>\d+) +(?P<flags>\S+) +"
            r"(?P<state>\S+) +(?P<address>\S+)(?:\s+\((?P<extra>.*)\))?$"
        )

        # WDDI Memory:          8732064
        p20 = re.compile(r"^WDDI Memory: +(?P<wddi_memory>\d+)$")

        # Qnode Status:        65276
        p21 = re.compile(r"^Qnode Status: +(?P<qnode_status>\d+)$")

        current_section = None

        for line in output.splitlines():
            line = line.strip()

            # Process and Memory
            m = p1.match(line)
            if m:
                current_section = "process_and_memory"
                ret_dict.setdefault(current_section, {"processes": {}})
                continue

            # Mem: 46468K used, 14468K free, 0K shrd, 0K buff, 32764K cached
            m = p2.match(line)
            if m and current_section == "process_and_memory":
                group = m.groupdict()
                mem_stats = ret_dict[current_section].setdefault("memory_stats", {})
                mem_stats["mem_used_kb"] = int(group["used"])
                mem_stats["mem_free_kb"] = int(group["free"])
                mem_stats["mem_shrd_kb"] = int(group["shrd"])
                mem_stats["mem_buff_kb"] = int(group["buff"])
                mem_stats["mem_cached_kb"] = int(group["cached"])
                continue

            # CPU:   0% usr   0% sys   0% nic 100% idle   0% io   0% irq   0% sirq
            m = p3.match(line)
            if m and current_section == "process_and_memory":
                group = m.groupdict()
                cpu_stats = ret_dict[current_section].setdefault("cpu_stats", {})
                cpu_stats["cpu_usr_percent"] = int(group["usr"])
                cpu_stats["cpu_sys_percent"] = int(group["sys"])
                cpu_stats["cpu_nic_percent"] = int(group["nic"])
                cpu_stats["cpu_idle_percent"] = int(group["idle"])
                cpu_stats["cpu_io_percent"] = int(group["io"])
                cpu_stats["cpu_irq_percent"] = int(group["irq"])
                cpu_stats["cpu_sirq_percent"] = int(group["sirq"])
                continue

            # Load average: 0.06 0.03 0.00 3/20 10258
            m = p4.match(line)
            if m and current_section == "process_and_memory":
                group = m.groupdict()
                ret_dict[current_section]["load_average"] = group["load_average"]
                continue

            # PID  PPID USER     STAT   VSZ %MEM %CPU COMMAND
            m = p4_1.match(line)
            if m and current_section == "process_and_memory":
                # Skip header line
                continue

            # Process entries like:   158   157 0        R     146m 246%   0% [cisco_fortitude]
            m = p5.match(line)
            if m and current_section == "process_and_memory":
                group = m.groupdict()
                processes = ret_dict[current_section].setdefault("processes", {})
                pid = int(group["pid"])
                processes[pid] = {
                    "pid": pid,
                    "ppid": int(group["ppid"]),
                    "user": group["user"],
                    "stat": group["stat"],
                    "vsz": group["vsz"],
                    "mem_percent": group["mem_percent"],
                    "cpu_percent": group["cpu_percent"],
                    "command": group["command"],
                }
                continue

            # Interrupts
            m = p6.match(line)
            if m:
                current_section = "interrupts"
                ret_dict.setdefault(current_section, {})
                continue

            #            CPU0
            m = p6_1.match(line)
            if m and current_section == "interrupts":
                # Skip header line
                continue

            # Interrupt entries like:   2:          0            MIPS  WinPath interrupt controller
            m = p7.match(line)
            if m and current_section == "interrupts":
                group = m.groupdict()
                interrupt = int(group["interrupt"])
                ret_dict[current_section][interrupt] = {
                    "cpu0": int(group["cpu0"]),
                    "controller": group["controller"],
                    "description": group["description"],
                }
                continue

            # ERR:          0
            m = p8.match(line)
            if m and current_section == "interrupts":
                group = m.groupdict()
                ret_dict[current_section]["err"] = int(group["err"])
                continue

            # System status
            m = p9.match(line)
            if m:
                current_section = "system_status"
                ret_dict.setdefault(current_section, {})
                continue

            # cpu  115 0 611 21404 0 0 0 0 0
            m = p10.match(line)
            if m and current_section == "system_status":
                group = m.groupdict()
                ret_dict[current_section]["cpu"] = group["cpu"]
                continue

            # intr 86063 0 0 0 0 0 0 0 55326 ...
            m = p11.match(line)
            if m and current_section == "system_status":
                group = m.groupdict()
                ret_dict[current_section]["intr"] = group["intr"]
                continue

            # ctxt 205235
            m = p12.match(line)
            if m and current_section == "system_status":
                group = m.groupdict()
                ret_dict[current_section]["ctxt"] = int(group["ctxt"])
                continue

            # btime 0
            m = p13.match(line)
            if m and current_section == "system_status":
                group = m.groupdict()
                ret_dict[current_section]["btime"] = int(group["btime"])
                continue

            # processes 10236
            m = p14.match(line)
            if m and current_section == "system_status":
                group = m.groupdict()
                ret_dict[current_section]["processes"] = int(group["processes"])
                continue

            # procs_running 2
            m = p15.match(line)
            if m and current_section == "system_status":
                group = m.groupdict()
                ret_dict[current_section]["procs_running"] = int(group["procs_running"])
                continue

            # procs_blocked 0
            m = p16.match(line)
            if m and current_section == "system_status":
                group = m.groupdict()
                ret_dict[current_section]["procs_blocked"] = int(group["procs_blocked"])
                continue

            # KLM Module status
            m = p17.match(line)
            if m:
                current_section = "klm_module_status"
                ret_dict.setdefault(current_section, {"modules": {}})
                continue

            # klm_mmap 5917008 4 - Live 0xc05ff000
            # dmesg 544 0 - Live 0xc0bbb000 (P)
            m = p19.match(line)
            if m and current_section == "klm_module_status":
                group = m.groupdict()
                modules = ret_dict[current_section]["modules"]
                module_name = group["module"]
                modules[module_name] = {
                    "size": int(group["size"]),
                    "used": int(group["used"]),
                    "flags": group["flags"],
                    "address": group["address"],
                }
                if group["state"] != "-":
                    modules[module_name]["state"] = group["state"]
                continue

            # WDDI Memory:          8732064
            m = p20.match(line)
            if m and current_section == "klm_module_status":
                group = m.groupdict()
                ret_dict[current_section]["wddi_memory"] = int(group["wddi_memory"])
                continue

            # Qnode Status:        65276
            m = p21.match(line)
            if m and current_section == "klm_module_status":
                group = m.groupdict()
                ret_dict[current_section]["qnode_status"] = int(group["qnode_status"])
                continue

        return ret_dict


class ShowPlatformSoftwareBPCrimsonContentOperSchema(MetaParser):
    """Schema for show platform software bp crimson content oper"""

    schema = {
        "node": {
            Any(): {
                "node_details": {
                    "node_number": int,
                    "priority": int,
                    "negotiation_state": str,
                },
                "domain_details": {
                    "node": int,
                    "domain": int,
                    "mode": str,
                },
                Optional("svl_ports"): {
                    Any(): {
                        "interface": str,
                        "link": int,
                        "if_id": int,
                        "status": str,
                        "prot": str,
                        "speed": str,
                        "sync": str,
                        "svl_state": str,
                        "slot": str,
                        "type": str,
                    }
                },
                Optional("dad_ports"): {
                    Any(): {
                        "interface": str,
                        "link": int,
                        "if_id": int,
                        "status": str,
                        "prot": str,
                        "speed": str,
                        "sync": str,
                        "svl_state": str,
                        "slot": str,
                        "type": str,
                    }
                },
            },
        }
    }


class ShowPlatformSoftwareBPCrimsonContentOper(
    ShowPlatformSoftwareBPCrimsonContentOperSchema
):
    """Parser for
    show platform software bp crimson content oper
    """

    cli_command = "show platform software bp crimson content oper"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        current_node = None
        current_section = None
        expect_domain_details = False

        # Header line: Node    Domain    Mode
        p0 = re.compile(r"^Node\s+Domain\s+Mode$")

        # Node    Priority   Negotiation State data
        # 1       1          Done
        p1 = re.compile(
            r"^(?P<node>\d+)\s+(?P<priority>\d+)\s+(?P<negotiation_state>\S+)$"
        )

        # Node    Domain    Mode data
        # 1       1         Aggregation
        p2 = re.compile(
            r"^(?P<node>\d+)\s+(?P<domain>\d+)\s+(?P<mode>\S+)$"
        )

        # Oper SVL Ports:
        p3 = re.compile(r"^Oper SVL Ports:")

        # Oper DAD Ports:
        p4 = re.compile(r"^Oper DAD Ports:")

        # Interface                     Link   if_id   Status   Prot   Speed    Sync            SVLState   Slot:Bay:Port   Type
        # FiftyGigE1/0/1                1      3       Up       P      10gbps   BP-Owns         Created    1:0:1           SFP-10GBase-CU1M
        p5 = re.compile(
            r"^(?P<interface>\S+)\s+(?P<link>\d+)\s+(?P<if_id>\d+)\s+(?P<status>\S+)\s+(?P<prot>\S+)\s+(?P<speed>\S+)\s+(?P<sync>\S+)\s+(?P<svl_state>\S+)\s+(?P<slot>\S+)\s+(?P<type>\S+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Check for Node Domain Mode header
            m = p0.match(line)
            if m:
                expect_domain_details = True
                continue

            # Node Priority Negotiation State data (appears first, no header check needed)
            # 1       1          Done
            m = p1.match(line)
            if m and not expect_domain_details:
                group = m.groupdict()
                current_node = group["node"]
                node_wrapper = ret_dict.setdefault("node", {})
                node_dict = node_wrapper.setdefault(current_node, {})
                node_details = node_dict.setdefault("node_details", {})
                node_details["node_number"] = int(group["node"])
                node_details["priority"] = int(group["priority"])
                node_details["negotiation_state"] = group["negotiation_state"]
                continue

            # Node Domain Mode data (only after seeing the header)
            # 1       1         Aggregation
            m = p2.match(line)
            if m and expect_domain_details:
                group = m.groupdict()
                if current_node:
                    node_wrapper = ret_dict["node"]
                    node_dict = node_wrapper[current_node]
                    domain_details = node_dict.setdefault("domain_details", {})
                    domain_details["node"] = int(group["node"])
                    domain_details["domain"] = int(group["domain"])
                    domain_details["mode"] = group["mode"]
                expect_domain_details = False
                continue

            # Oper SVL Ports:
            m = p3.match(line)
            if m:
                current_section = "svl_ports"
                continue

            # Oper DAD Ports:
            m = p4.match(line)
            if m:
                current_section = "dad_ports"
                continue

            # Interface details
            m = p5.match(line)
            if m:
                group = m.groupdict()
                node_wrapper = ret_dict["node"]
                node_dict = node_wrapper[current_node]
                ports_dict = node_dict.setdefault(current_section, {})
                interface_dict = ports_dict.setdefault(group["interface"], {})
                interface_dict["interface"] = group["interface"]
                interface_dict["link"] = int(group["link"])
                interface_dict["if_id"] = int(group["if_id"])
                interface_dict["status"] = group["status"]
                interface_dict["prot"] = group["prot"]
                interface_dict["speed"] = group["speed"]
                interface_dict["sync"] = group["sync"]
                interface_dict["svl_state"] = group["svl_state"]
                interface_dict["slot"] = group["slot"]
                interface_dict["type"] = group["type"]
                continue

        return ret_dict


class ShowPlatformSoftwareFirewallFPActiveParameterMapsSchema(MetaParser):
    """Schema for show platform software firewall FP active parameter-maps"""
    schema = {
        'parameter_maps': {
            Any(): {
                'name': str,
                'index': int,
                'type': str,
                'global_parameter_map': bool,
                'alerts': str,
                'audits': str,
                'drop_log': str,
                'hsl_mode': str,
                'host': str,
                'port': int,
                'template': str,
                'session_rate_high': int,
                'session_rate_low': int,
                'time_duration': str,
                'half_open': {
                    'high': int,
                    'low': int,
                    'host': int,
                    'host_block_time': int,
                },
                'inactivity_times': {
                    'dns': int,
                    'icmp': int,
                    'tcp': int,
                    'udp': int,
                },
                'tcp_timeouts': {
                    'syn_wait_time': int,
                    'fin_wait_time': int,
                },
                'tcp_rst_pkt_control': {
                    'half_open': str,
                    'half_close': str,
                    'idle': str,
                },
                'udp_timeout': {
                    'udp_half_open_time': int,
                },
                'max_sessions': str,
                'number_of_simultaneous_packet_per_sessions': int,
                'syn_cookie_and_resource_management': {
                    'global_syn_flood_limit': int,
                    'global_total_session': int,
                },
            }
        }
    }


class ShowPlatformSoftwareFirewallFPActiveParameterMaps(ShowPlatformSoftwareFirewallFPActiveParameterMapsSchema):
    """Parser for show platform software firewall FP active parameter-maps"""

    cli_command = 'show platform software firewall FP active parameter-maps'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize return dictionary
        ret_dict = {}

        # Inspect Parameter Map: global, Index 1
        p1 = re.compile(r'^Inspect Parameter Map: (?P<name>\S+), Index (?P<index>\d+)$')

        # Parameter Map Type: Parameter-Map
        p2 = re.compile(r'^Parameter Map Type: (?P<type>[\S\s]+)$')

        # Global Parameter-Map
        p3 = re.compile(r'^Global Parameter-Map$')

        # Alerts: On, Audits: Off, Drop-Log: Off
        p4 = re.compile(r'^Alerts: (?P<alerts>\S+), Audits: (?P<audits>\S+), Drop-Log: (?P<drop_log>\S+)$')

        # HSL Mode: V9, Host: 10.1.1.1:9000, Port: 54174, Template: 300 sec
        p5 = re.compile(r'^HSL Mode: (?P<hsl_mode>\S+), Host: (?P<host>\S+), Port: (?P<port>\d+), Template: (?P<template>[\d\s\w]+)$')

        # Session Rate High: 2147483647, Session Rate Low: 2147483647, Time Duration: 60 sec
        p6 = re.compile(r'^Session Rate High: (?P<session_rate_high>\d+), Session Rate Low: (?P<session_rate_low>\d+), Time Duration: (?P<time_duration>[\d\s\w]+)$')

        # High: 2147483647, Low: 2147483647, Host: 4294967295, Host Block Time: 0
        p7 = re.compile(r'^High: (?P<high>\d+), Low: (?P<low>\d+), Host: (?P<host_val>\d+), Host Block Time: (?P<host_block_time>\d+)$')

        # DNS: 5, ICMP: 10, TCP: 3600, UDP: 30
        p8 = re.compile(r'^DNS: (?P<dns>\d+), ICMP: (?P<icmp>\d+), TCP: (?P<tcp>\d+), UDP: (?P<udp>\d+)$')

        # SYN wait time: 30, FIN wait time: 1
        p9 = re.compile(r'^SYN wait time: (?P<syn_wait_time>\d+), FIN wait time: (?P<fin_wait_time>\d+)$')

        # half-open: On, half-close: On, idle: On
        p10 = re.compile(r'^half-open: (?P<half_open>\S+), half-close: (?P<half_close>\S+), idle: (?P<idle>\S+)$')

        # UDP Half-open time: 30000
        p11 = re.compile(r'^UDP Half-open time: (?P<udp_half_open_time>\d+)$')

        # Max Sessions: Unlimited
        p12 = re.compile(r'^Max Sessions: (?P<max_sessions>\S+)$')

        # Number of Simultaneous Packet per Sessions: 0
        p13 = re.compile(r'^Number of Simultaneous Packet per Sessions: (?P<number_of_simultaneous_packet_per_sessions>\d+)$')

        # Global Syn Flood Limit: 4294967295
        p14 = re.compile(r'^Global Syn Flood Limit: (?P<global_syn_flood_limit>\d+)$')

        # Global Total Session : 4294967295
        p15 = re.compile(r'^Global Total Session\s*:\s*(?P<global_total_session>\d+)$')

        current_param_map = None

        for line in output.splitlines():
            line = line.strip()

            # Inspect Parameter Map: global, Index 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group['name']
                current_param_map = ret_dict.setdefault('parameter_maps', {}).setdefault(name, {})
                current_param_map['name'] = name
                current_param_map['index'] = int(group['index'])
                continue

            # Parameter Map Type: Parameter-Map
            m = p2.match(line)
            if m:
                group = m.groupdict()
                current_param_map['type'] = group['type']
                continue

            # Global Parameter-Map
            m = p3.match(line)
            if m:
                current_param_map['global_parameter_map'] = True
                continue

            # Alerts: On, Audits: Off, Drop-Log: Off
            m = p4.match(line)
            if m:
                group = m.groupdict()
                current_param_map['alerts'] = group['alerts']
                current_param_map['audits'] = group['audits']
                current_param_map['drop_log'] = group['drop_log']
                continue

            # HSL Mode: V9, Host: 10.1.1.1:9000, Port: 54174, Template: 300 sec
            m = p5.match(line)
            if m:
                group = m.groupdict()
                current_param_map['hsl_mode'] = group['hsl_mode']
                current_param_map['host'] = group['host']
                current_param_map['port'] = int(group['port'])
                current_param_map['template'] = group['template']
                continue

            # Session Rate High: 2147483647, Session Rate Low: 2147483647, Time Duration: 60 sec
            m = p6.match(line)
            if m:
                group = m.groupdict()
                current_param_map['session_rate_high'] = int(group['session_rate_high'])
                current_param_map['session_rate_low'] = int(group['session_rate_low'])
                current_param_map['time_duration'] = group['time_duration']
                continue

            # High: 2147483647, Low: 2147483647, Host: 4294967295, Host Block Time: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                half_open_dict = current_param_map.setdefault('half_open', {})
                half_open_dict['high'] = int(group['high'])
                half_open_dict['low'] = int(group['low'])
                half_open_dict['host'] = int(group['host_val'])
                half_open_dict['host_block_time'] = int(group['host_block_time'])
                continue

            # DNS: 5, ICMP: 10, TCP: 3600, UDP: 30
            m = p8.match(line)
            if m:
                group = m.groupdict()
                inactivity_dict = current_param_map.setdefault('inactivity_times', {})
                inactivity_dict['dns'] = int(group['dns'])
                inactivity_dict['icmp'] = int(group['icmp'])
                inactivity_dict['tcp'] = int(group['tcp'])
                inactivity_dict['udp'] = int(group['udp'])
                continue

            # SYN wait time: 30, FIN wait time: 1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                tcp_timeouts_dict = current_param_map.setdefault('tcp_timeouts', {})
                tcp_timeouts_dict['syn_wait_time'] = int(group['syn_wait_time'])
                tcp_timeouts_dict['fin_wait_time'] = int(group['fin_wait_time'])
                continue

            # half-open: On, half-close: On, idle: On
            m = p10.match(line)
            if m:
                group = m.groupdict()
                tcp_rst_dict = current_param_map.setdefault('tcp_rst_pkt_control', {})
                tcp_rst_dict['half_open'] = group['half_open']
                tcp_rst_dict['half_close'] = group['half_close']
                tcp_rst_dict['idle'] = group['idle']
                continue

            # UDP Half-open time: 30000
            m = p11.match(line)
            if m:
                group = m.groupdict()
                udp_timeout_dict = current_param_map.setdefault('udp_timeout', {})
                udp_timeout_dict['udp_half_open_time'] = int(group['udp_half_open_time'])
                continue

            # Max Sessions: Unlimited
            m = p12.match(line)
            if m:
                group = m.groupdict()
                current_param_map['max_sessions'] = group['max_sessions']
                continue

            # Number of Simultaneous Packet per Sessions: 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                current_param_map['number_of_simultaneous_packet_per_sessions'] = int(group['number_of_simultaneous_packet_per_sessions'])
                continue

            # Global Syn Flood Limit: 4294967295
            m = p14.match(line)
            if m:
                group = m.groupdict()
                syn_cookie_dict = current_param_map.setdefault('syn_cookie_and_resource_management', {})
                syn_cookie_dict['global_syn_flood_limit'] = int(group['global_syn_flood_limit'])
                continue

            # Global Total Session : 4294967295
            m = p15.match(line)
            if m:
                group = m.groupdict()
                syn_cookie_dict = current_param_map.setdefault('syn_cookie_and_resource_management', {})
                syn_cookie_dict['global_total_session'] = int(group['global_total_session'])
                continue

        return ret_dict

# ==========================================================================
# Schema for 'show platform software subslot {subslot} module firmware'
# ==========================================================================

class ShowPlatformSoftwareSubslotModuleFirmwareSchema(MetaParser):
    """Schema for show platform software subslot {subslot} module firmware"""

    schema = {
        'chip_revision': str,
        'wddi_build': int,
        'winfarm_dps_builds': {
            'winfarm_0': int,
            'winfarm_1': int,
        },
        'wf_features_sets': {
            'wf_0': str,
            'wf_1': str,
        },
        'nim_firmware': {
            'linux_version': str,
            'gcc_version': str,
            'compile_time': str,
        },
        'boot_loader_info': {
            'current_secure_boot_loader': str,
            'golden_boot_loader_version': str,
            'upgrade_boot_loader_version': str,
            'bundled_boot_image_version': str,
            'upgrade_boot_loader_valid': str,
        },
        'fpga_versions': {
            'active': str,
            'upgraded': str,
            'golden': str,
        },
    }


class ShowPlatformSoftwareSubslotModuleFirmware(ShowPlatformSoftwareSubslotModuleFirmwareSchema):
    """Parser for show platform software subslot {subslot} module firmware"""

    cli_command = 'show platform software subslot {subslot} module firmware'

    def cli(self, subslot, output=None):

        if output is None:
            cmd = self.cli_command.format(subslot=subslot)
            out = self.device.execute(cmd)
        else:
            out = output

        # Initialize return dictionary to store parsed results
        ret_dict = {}

        # Chip Revision: unknown
        p1 = re.compile(r'^Chip\s+Revision:\s+(?P<chip_revision>\S+)$')

        # WDDI Build: 1908
        p2 = re.compile(r'^WDDI\s+Build:\s+(?P<wddi_build>\d+)$')

        # WinFarm-0:DPS Build: 2392
        p3 = re.compile(r'^WinFarm-(?P<wf_num>\d+):DPS\s+Build:\s+(?P<dps_build>\d+)$')

        # WF-0 features set:
        p4 = re.compile(r'^WF-(?P<wf_num>\d+)\s+features\s+set:$')

        # 70d43f57 7987fffe 30f80386 46809a62 016d100e
        p5 = re.compile(r'^[0-9a-f\s]+$')

        # Linux version 2.6.28.10.mips-malta (paulhu@sjc-marsbu-131) (gcc version 4.3.3 (MontaVista Linux Sourcery G++ 4.3-302) ) #2 PREEMPT Thu Nov 24 22:10:30 PST 2022
        p6 = re.compile(r'^Linux\s+version\s+(?P<linux_version>\S+)\s+.*\(gcc\s+version\s+(?P<gcc_version>[\d\.]+).*\)\s+#\d+\s+PREEMPT\s+(?P<compile_time>.+)$')

        # Current Secure Boot Loader : Upgrade
        p7 = re.compile(r'^Current\s+Secure\s+Boot\s+Loader\s+:\s+(?P<current_boot_loader>\S+)$')

        # Golden Boot Loader Version : 0x5
        p8 = re.compile(r'^Golden\s+Boot\s+Loader\s+Version\s+:\s+(?P<golden_version>\S+)$')

        # Upgrade Boot Loader Version: 0x7
        p9 = re.compile(r'^Upgrade\s+Boot\s+Loader\s+Version:\s+(?P<upgrade_version>\S+)$')

        # Bundled Boot Image Version : 0x7
        p10 = re.compile(r'^Bundled\s+Boot\s+Image\s+Version\s+:\s+(?P<bundled_version>\S+)$')

        # Upgrade Boot Loader Valid  : 0x1
        p11 = re.compile(r'^Upgrade\s+Boot\s+Loader\s+Valid\s+:\s+(?P<upgrade_valid>\S+)$')

        # FPGA (Active) version: 14050215
        p12 = re.compile(r'^FPGA\s+\(Active\)\s+version:\s+(?P<fpga_active>\S+)$')

        # FPGA (Upgraded) version: 19062002
        p13 = re.compile(r'^FPGA\s+\(Upgraded\)\s+version:\s+(?P<fpga_upgraded>\S+)$')

        # FPGA (Golden) version: Unknownge: 1
        p14 = re.compile(r'^FPGA\s+\(Golden\)\s+version:\s+(?P<fpga_golden>.+)$')

        # State variables for multi-line parsing
        # current_wf: Tracks which WF section we're currently parsing (0 or 1)
        # features_data_buffer: Accumulates hex feature data lines for current WF
        # in_nim_firmware: Flag indicating we're in the NIM Firmware section
        current_wf = None
        features_data_buffer = []
        in_nim_firmware = False

        # Parse each line of the command output
        for line in out.splitlines():
            line = line.strip()

            if not line:  # Skip empty lines
                continue

            # Check for NIM Firmware section header
            # This marks the transition from WF features to NIM firmware info
            if line == "NIM Firmware:":
                # End of features data for current WF if any
                if current_wf is not None and features_data_buffer:
                    wf_features_dict = ret_dict.setdefault('wf_features_sets', {})
                    wf_key = f"wf_{current_wf}"
                    wf_features_dict[wf_key] = '\n'.join(features_data_buffer).strip()
                    features_data_buffer = []
                    current_wf = None
                in_nim_firmware = True
                continue

            # Chip Revision: unknown
            m = p1.match(line)
            if m:
                ret_dict['chip_revision'] = m.groupdict()['chip_revision']
                continue

            # WDDI Build: 1908
            m = p2.match(line)
            if m:
                ret_dict['wddi_build'] = int(m.groupdict()['wddi_build'])
                continue

            # WinFarm-0:DPS Build: 2392
            m = p3.match(line)
            if m:
                group = m.groupdict()
                winfarm_dict = ret_dict.setdefault('winfarm_dps_builds', {})
                wf_key = f"winfarm_{group['wf_num']}"
                winfarm_dict[wf_key] = int(group['dps_build'])
                continue

            # WF-0 features set:
            m = p4.match(line)
            if m:
                # End of previous WF if any
                if current_wf is not None and features_data_buffer:
                    wf_features_dict = ret_dict.setdefault('wf_features_sets', {})
                    wf_key = f"wf_{current_wf}"
                    wf_features_dict[wf_key] = '\n'.join(features_data_buffer).strip()

                current_wf = m.groupdict()['wf_num']
                features_data_buffer = []
                continue

            # 70d43f57 7987fffe 30f80386 46809a62 016d100e
            if current_wf is not None and not in_nim_firmware:
                m = p5.match(line)
                if m:
                    features_data_buffer.append(line)
                    continue

            # Linux version 2.6.28.10.mips-malta (paulhu@sjc-marsbu-131) (gcc version 4.3.3 (MontaVista Linux Sourcery G++ 4.3-302) ) #2 PREEMPT Thu Nov 24 22:10:30 PST 2022
            m = p6.match(line)
            if m:
                group = m.groupdict()
                nim_dict = ret_dict.setdefault('nim_firmware', {})
                nim_dict['linux_version'] = group['linux_version']
                nim_dict['gcc_version'] = group['gcc_version']
                nim_dict['compile_time'] = group['compile_time']
                continue

            # Current Secure Boot Loader : Upgrade
            m = p7.match(line)
            if m:
                boot_dict = ret_dict.setdefault('boot_loader_info', {})
                boot_dict['current_secure_boot_loader'] = m.groupdict()['current_boot_loader']
                continue

            # Golden Boot Loader Version : 0x5
            m = p8.match(line)
            if m:
                boot_dict = ret_dict.setdefault('boot_loader_info', {})
                boot_dict['golden_boot_loader_version'] = m.groupdict()['golden_version']
                continue

            # Upgrade Boot Loader Version: 0x7
            m = p9.match(line)
            if m:
                boot_dict = ret_dict.setdefault('boot_loader_info', {})
                boot_dict['upgrade_boot_loader_version'] = m.groupdict()['upgrade_version']
                continue

            # Bundled Boot Image Version : 0x7
            m = p10.match(line)
            if m:
                boot_dict = ret_dict.setdefault('boot_loader_info', {})
                boot_dict['bundled_boot_image_version'] = m.groupdict()['bundled_version']
                continue

            # Upgrade Boot Loader Valid  : 0x1
            m = p11.match(line)
            if m:
                boot_dict = ret_dict.setdefault('boot_loader_info', {})
                boot_dict['upgrade_boot_loader_valid'] = m.groupdict()['upgrade_valid']
                continue

            # FPGA (Active) version: 14050215
            m = p12.match(line)
            if m:
                fpga_dict = ret_dict.setdefault('fpga_versions', {})
                fpga_dict['active'] = m.groupdict()['fpga_active']
                continue

            # FPGA (Upgraded) version: 19062002
            m = p13.match(line)
            if m:
                fpga_dict = ret_dict.setdefault('fpga_versions', {})
                fpga_dict['upgraded'] = m.groupdict()['fpga_upgraded']
                continue

            # FPGA (Golden) version: Unknownge: 1
            m = p14.match(line)
            if m:
                fpga_dict = ret_dict.setdefault('fpga_versions', {})
                fpga_dict['golden'] = m.groupdict()['fpga_golden']
                continue

        # Handle any remaining WF features data that wasn't closed by another section
        # This ensures we don't lose the last WF section if it's at the end of output
        if current_wf is not None and features_data_buffer:
            wf_features_dict = ret_dict.setdefault('wf_features_sets', {})
            wf_key = f"wf_{current_wf}"
            wf_features_dict[wf_key] = '\n'.join(features_data_buffer).strip()

        return ret_dict

class ShowPlatformSoftwareAuditMonitorStatusSchema(MetaParser):
    """
    Schema for 'show platform software audit monitor status'
    """
    schema = {
        "rules": ListOf({
            "name": str,
            "status": str
        })
    }

class ShowPlatformSoftwareAuditMonitorStatus(ShowPlatformSoftwareAuditMonitorStatusSchema, MetaParser):
    """Parser for 'show platform software audit monitor status'"""

    cli_command = 'show platform software audit monitor status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        # Compile regex pattern for rule lines with named groups before the loop
        rule_pattern = re.compile(
            r'(?P<name>[A-Z_]+)\s*:\s*(?P<status>enable|disable)', re.IGNORECASE
        )

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue
            m = rule_pattern.match(line)
            if m:
                rules = ret_dict.setdefault('rules', [])
                rules.append({
                    "name": m.group("name").upper(),
                    "status": m.group("status").lower()
                })
        return ret_dict

class ShowPlatformSoftwareAuditRulesetSchema(MetaParser):
    """
    Schema for 'show platform software audit ruleset'
    """
    schema = {
        "rulesets": ListOf({
            "name": str,
            "rules": ListOf(str)
        })
    }

class ShowPlatformSoftwareAuditRuleset(ShowPlatformSoftwareAuditRulesetSchema, MetaParser):
    """Parser for 'show platform software audit ruleset'"""

    cli_command = 'show platform software audit ruleset'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        # Compile regex patterns before the loop for efficiency
        ruleset_pattern = re.compile(r'^(?P<name>[a-zA-Z0-9_]+)\s*:\s*$')
        rule_pattern = re.compile(r'^:\s+(?P<rule>.+)$')
        section_end_pattern = re.compile(r'^_{5,}$')

        current_ruleset = None
        current_rules = []

        for line in output.splitlines():
            line = line.strip()
            m = ruleset_pattern.match(line)
            if m:
                if current_ruleset:
                    rulesets = ret_dict.setdefault('rulesets', [])
                    rulesets.append({
                        "name": current_ruleset,
                        "rules": current_rules
                    })
                current_ruleset = m.group("name")
                current_rules = []
                continue
            m = rule_pattern.match(line)
            if m and current_ruleset:
                current_rules.append(m.group("rule").strip())
                continue
            if section_end_pattern.match(line):
                continue

        if current_ruleset:
            rulesets = ret_dict.setdefault('rulesets', [])
            rulesets.append({
                "name": current_ruleset,
                "rules": current_rules
            })

        return ret_dict


class ShowPlatformSoftwareFirewallQfpActiveRuntimeSchema(MetaParser):
    """Schema for show platform software firewall qfp active runtime"""
    schema = {
        "global": {
            "address": str,
            "ha_state": str,
            "fw_configured": str,
            "init_done": str,
            "init_requested": str,
            "syslog_deployed": str
        },
        "global2": {
            "address": str,
            "salt": int,
            "global_num_simul_pkt_per_sess_allowed": int,
            "default_num_simul_pkt_per_sess_allowed": int
        },
        "global3": {
            "address": str,
            "same_zone_policy": str,
            "vpn_zone_security": str,
            "teardowns": int,
            "pam_cce": str,
            "num_zp_with_policy": int,
            "high_priority_recycle_queue_addr": str,
            "low_priority_recycle_queue_addr": str,
            "lock_upgrades": int,
            "half_open_aggressive_aging": int,
            "num_ack_exceeds_limit": int,
            "num_rst_exceeds_limit": int,
            "unknown_vrf_limit_exceeds": int,
            "syncookie_over_rate_cnt": int,
            "fw_tcp_session_termination_rst_segment_control": {
                "halfopen": {
                    "rst_sent": int,
                    "blocked": int
                },
                "idle": {
                    "rst_sent": int,
                    "blocked": int
                },
                "halfclose": {
                    "rst_sent": int,
                    "blocked": int
                }
            },
            "nat_caching": {
                "nat_registration": int,
                "nat_unregistration": int,
                "too_many_nat_sessions": int,
                "cant_register_with_nat": int,
                "invalid_nat_session": int,
                "no_nat_session_caching": int,
                "nat_cached_session": int
            },
            "l2_firewall": {
                "l2_unknown_encap": int,
                "l2_skip_tcp_pkt": int,
                "timer_stop_failed": int
            },
            "vrf_global_action_block": {
                "l7_inspection_disable_flags": str
            },
            "total_sessions": {
                "max_limit": int,
                "current_count": int,
                "exceed": int,
                "aggr_age_high_watermark": int,
                "aggr_age_low_watermark": int,
                "num_times_enter_aggr_age": int,
                "aggr_age_period": str
            },
            "tcp_syn_cookie": {
                "max_limit": int,
                "current_count": int,
                "exceed": int
            },
            "total_half_open_sessions": {
                "max_limit": int,
                "current_count": int,
                "exceed": int,
                "aggr_age_high_watermark": int,
                "aggr_age_low_watermark": int,
                "num_times_enter_aggr_age": int,
                "aggr_age_period": str
            },
            "tcp_half_open_sessions": {
                "max_limit": int,
                "current_count": int,
                "exceed": int
            },
            "udp_half_open_sessions": {
                "max_limit": int,
                "current_count": int,
                "exceed": int
            },
            "icmp_half_open_sessions": {
                "max_limit": int,
                "current_count": int,
                "exceed": int
            },
            "domain_flags": str,
            "box_action_block": {
                "l7_inspection_disable_flags": str
            },
            "current_count": {
                "total_sessions": int,
                "aggr_age_high_watermark": int,
                "aggr_age_low_watermark": int,
                "num_times_enter_aggr_age": int,
                "aggr_age_period": str,
                "tcp_syn_cookie": {
                    "max_limit": int,
                    "current_count": int,
                    "exceed": int
                },
                "total_half_open_sessions": {
                    "max_limit": int,
                    "current_count": int,
                    "exceed": int,
                    "aggr_age_high_watermark": int,
                    "aggr_age_low_watermark": int,
                    "num_times_enter_aggr_age": int,
                    "aggr_age_period": str
                },
                "tcp_half_open_sessions": {
                    "max_limit": int,
                    "current_count": int,
                    "exceed": int
                },
                "udp_half_open_sessions": {
                    "max_limit": int,
                    "current_count": int,
                    "exceed": int
                },
                "icmp_half_open_sessions": {
                    "max_limit": int,
                    "current_count": int,
                    "exceed": int
                },
                "domain_flags": str
            },
            "fw_persona_alert_rlimit": int,
            "backpressure": str,
            "invalid_rg_exceeds_max_rg": int,
            "invalid_ha_message_version": int,
            "rii_hash_table": {
                "address": str,
                "size": int
            },
            "vrf_action_table": {
                "address": str,
                "size": int
            },
            "avc_stats_table_index_out_of_range": int
        },
        "vrf_id_name_table": ListOf(
            {
                "id": int,
                "name": str,
                "vrf_namehash": str,
                "ipv4": int,
                "ipv6": int
            }
        ),
        "w_persona": str,
        "vpn_zone_table": {
            "address": str,
            "size": int
        },
        "vpn_to_zone_mappings": ListOf(
            {
                "vpn": int,
                "zone": int
            }
        )
    }


class ShowPlatformSoftwareFirewallQfpActiveRuntime(ShowPlatformSoftwareFirewallQfpActiveRuntimeSchema):
    """Parser for show platform software firewall qfp active runtime"""
    cli_command = "show platform software firewall qfp active runtime"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        current_section = None
        current_fw_rst = None
        current_nat_caching = None
        current_l2_firewall = None
        current_vrf_block = None
        current_box_block = None
        inside_current_count = False
        current_current_count = None
        current_session_block = None
        current_session_block_name = None
        vrf_id_name_list = []
        vpn_to_zone_list = []

        # global 0x020001a1:
        p1 = re.compile(r'^global\s+(?P<addr>0x[0-9a-fA-F]+):$')
        # HA state Allow-New-Sess
        p2 = re.compile(r'^HA state\s+(?P<ha_state>.+)$')
        # FW Configured (0x00000020)
        p3 = re.compile(r'^FW Configured\s+\((?P<fw_conf>0x[0-9a-fA-F]+)\)$')
        # Init Done (0x00000080)
        p4 = re.compile(r'^Init Done\s+\((?P<init_done>0x[0-9a-fA-F]+)\)$')
        # Init Requested (0x00000100)
        p5 = re.compile(r'^Init Requested\s+\((?P<init_req>0x[0-9a-fA-F]+)\)$')
        # Syslog Deployed (0x02000000)
        p6 = re.compile(r'^Syslog Deployed\s+\((?P<syslog_deployed>0x[0-9a-fA-F]+)\)$')
        # global2 0x190000b7:
        p7 = re.compile(r'^global2\s+(?P<addr>0x[0-9a-fA-F]+):$')
        # Salt 183
        p8 = re.compile(r'^Salt\s+(?P<salt>\d+)$')
        # Global number of simultaneous packet per session allowed 0
        p9 = re.compile(r'^Global number of simultaneous packet per session allowed\s+(?P<val>\d+)$')
        # Default number of simultaneous packet per session allowed 25
        p10 = re.compile(r'^Default number of simultaneous packet per session allowed\s+(?P<val>\d+)$')
        # global3 0x00000009:
        p11 = re.compile(r'^global3\s+(?P<addr>0x[0-9a-fA-F]+):$')
        # Same Zone Policy (0x00000001)
        p12 = re.compile(r'^Same Zone Policy\s+\((?P<val>0x[0-9a-fA-F]+)\)$')
        # vpn zone security (0x00000008)
        p13 = re.compile(r'^vpn zone security\s+\((?P<val>0x[0-9a-fA-F]+)\)$')
        # teardowns 0, pam_cce 0x0 00000000
        p14 = re.compile(r'^teardowns\s+(?P<teardowns>\d+), pam_cce\s+(?P<pam>0x[0-9a-fA-F]+ [0-9a-fA-F]+)$')
        # num zp with policy 1
        p15 = re.compile(r'^num zp with policy\s+(?P<val>\d+)$')
        # High priority recycle queue address 0x84969ea0
        p16 = re.compile(r'^High priority recycle queue address\s+(?P<addr>0x[0-9a-fA-F]+)$')
        # Low priority recycle queue address 0x84969eb0
        p17 = re.compile(r'^Low priority recycle queue address\s+(?P<addr>0x[0-9a-fA-F]+)$')
        # Lock upgrades 0
        p18 = re.compile(r'^Lock upgrades\s+(?P<val>\d+)$')
        # Half open aggressive aging: 0
        p19 = re.compile(r'^Half open aggressive aging:\s+(?P<val>\d+)$')
        # Num of ACK exceeds limit(5): 0
        p20 = re.compile(r'^Num of ACK exceeds limit\(5\):\s+(?P<val>\d+)$')
        # Num of RST exceeds limit(5) 0
        p21 = re.compile(r'^Num of RST exceeds limit\(5\)\s+(?P<val>\d+)$')
        # Unknown VRF limit exceeds 0
        p22 = re.compile(r'^Unknown VRF limit exceeds\s+(?P<val>\d+)$')
        # syncookie over rate cnt 0
        p23 = re.compile(r'^syncookie over rate cnt\s+(?P<val>\d+)$')
        # fw tcp session termination RST segment control:
        p24 = re.compile(r'^fw tcp session termination RST segment control:$')
        # halfopen: RST sent 0, blocked 0
        p25 = re.compile(r'^(?P<state>halfopen|idle|halfclose): RST sent (?P<rst>\d+), blocked (?P<blocked>\d+)$')
        # NAT caching:
        p26 = re.compile(r'^NAT caching:$')
        # NAT registration 1
        p27 = re.compile(r'^NAT registration\s+(?P<val>\d+)$')
        # NAT unregistration 1
        p28 = re.compile(r'^NAT unregistration\s+(?P<val>\d+)$')
        # Too many nat sessions 0
        p29 = re.compile(r'^Too many nat sessions\s+(?P<val>\d+)$')
        # Can't register with NAT 0
        p30 = re.compile(r"^Can't register with NAT\s+(?P<val>\d+)$")
        # Invalid nat session 0
        p31 = re.compile(r'^Invalid nat session\s+(?P<val>\d+)$')
        # No NAT session caching 0
        p32 = re.compile(r'^No NAT session caching\s+(?P<val>\d+)$')
        # NAT cached session 0
        p33 = re.compile(r'^NAT cached session\s+(?P<val>\d+)$')
        # L2 Firewall:
        p34 = re.compile(r'^L2 Firewall:$')
        # L2 unknown encap 0
        p35 = re.compile(r'^L2 unknown encap\s+(?P<val>\d+)$')
        # L2 skip tcp pkt 0
        p36 = re.compile(r'^L2 skip tcp pkt\s+(?P<val>\d+)$')
        # Timer stop failed 0
        p37 = re.compile(r'^Timer stop failed\s+(?P<val>\d+)$')
        # VRF Global Action Block:
        p38 = re.compile(r'^VRF Global Action Block:$')
        # L7 Inspection disable flags: 0x0
        p39 = re.compile(r'^L7 Inspection disable flags:\s+(?P<flags>0x[0-9a-fA-F]+)$')
        # Total Sessions:
        p40 = re.compile(r'^Total Sessions:$')
        # max limit: 4294967295, current count: 0, exceed: 0
        p41 = re.compile(r'^max limit:\s+(?P<max>\d+), current count:\s+(?P<count>\d+), exceed:\s+(?P<exceed>\d+)$')
        # aggr-age high watermark: 4294967295, low watermark: 0
        p42 = re.compile(r'^aggr-age high watermark:\s+(?P<high>\d+), low watermark:\s+(?P<low>\d+)$')
        # num of times enter aggr-age: 0, aggr-age period: off
        p43 = re.compile(r'^num of times enter aggr-age:\s+(?P<num>\d+), aggr-age period:\s+(?P<period>\S+)$')
        # TCP SYN Cookie:
        p44 = re.compile(r'^TCP SYN Cookie:$')
        # Total Half Open Sessions:
        p45 = re.compile(r'^Total Half Open Sessions:$')
        # TCP Half Open Sessions:
        p46 = re.compile(r'^TCP Half Open Sessions:$')
        # UDP Half Open Sessions:
        p47 = re.compile(r'^UDP Half Open Sessions:$')
        # ICMP Half Open Sessions:
        p48 = re.compile(r'^ICMP Half Open Sessions:$')
        # Domain flags: 0x0
        p49 = re.compile(r'^Domain flags: (?P<flags>0x[0-9a-fA-F]+)$')
        # Box Action Block:
        p50 = re.compile(r'^Box Action Block:$')
        # Current count::
        p51 = re.compile(r'^Current count::$')
        # Total Sessions 0
        p52 = re.compile(r'^Total Sessions\s+(?P<val>\d+)$')
        # FW persona alert_rlimit: 0, backpressure: 0x0
        p53 = re.compile(r'^FW persona alert_rlimit: (?P<rlimit>\d+), backpressure: (?P<bp>0x[0-9a-fA-F]+)$')
        # Invalid RG (exceeds max RG): 0
        p54 = re.compile(r'^Invalid RG \(exceeds max RG\): (?P<val>\d+)$')
        # Invalid HA message version: 0
        p55 = re.compile(r'^Invalid HA message version: (?P<val>\d+)$')
        # RII Hash Table: address 0x093c9c10 size 128
        p56 = re.compile(r'^RII Hash Table: address (?P<addr>0x[0-9a-fA-F]+) size (?P<size>\d+)$')
        # VRF Action Table Addr 0x0x1237c000, Size 4096
        p57 = re.compile(r'^VRF Action Table Addr (?P<addr>0x[0-9a-fA-Fx]+), Size (?P<size>\d+)$')
        # AVC stats table index out-of-range 0
        p58 = re.compile(r'^AVC stats table index out-of-range (?P<val>\d+)$')
        # VRF ID-Name Table:
        p59 = re.compile(r'^VRF ID-Name Table:$')
        # VRF:(id=4106:name=__Platform_iVRF:ID00)
        p60 = re.compile(r'^VRF:\(id=(?P<id>\d+):name=(?P<name>[^)]+)\)$')
        # vrf_namehash 9f30f5f1fd89b0f0 ipv4 4106, ipv6 65535
        p61 = re.compile(r'^vrf_namehash (?P<hash>[0-9a-fA-F]+) ipv4 (?P<ipv4>\d+), ipv6 (?P<ipv6>\d+)$')
        # w_persona: 0x84969ec0 vpn zone table address: 0x13b00400, size 65536
        p62 = re.compile(r'^w_persona: (?P<wpersona>0x[0-9a-fA-F]+) vpn zone table address: (?P<addr>0x[0-9a-fA-F]+), size (?P<size>\d+)$')
        # VPN to Zone mappings
        p63 = re.compile(r'^VPN to Zone mappings$')
        # vpn: 1 zone: 1
        p64 = re.compile(r'^vpn: (?P<vpn>\d+) zone: (?P<zone>\d+)$')

        # State for vrf_id_name_list
        current_vrf_entry = None
        inside_vrf_id_name_table = False
        inside_vpn_to_zone = False

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # global 0x020001a1:
            m = p1.match(line)
            if m:
                current_section = ret_dict.setdefault("global", {})
                current_section["address"] = m.group("addr")
                continue

            # HA state Allow-New-Sess
            m = p2.match(line)
            if m and current_section is ret_dict.get("global"):
                current_section["ha_state"] = m.group("ha_state")
                continue

            # FW Configured (0x00000020)
            m = p3.match(line)
            if m and current_section is ret_dict.get("global"):
                current_section["fw_configured"] = m.group("fw_conf")
                continue

            # Init Done (0x00000080)
            m = p4.match(line)
            if m and current_section is ret_dict.get("global"):
                current_section["init_done"] = m.group("init_done")
                continue

            # Init Requested (0x00000100)
            m = p5.match(line)
            if m and current_section is ret_dict.get("global"):
                current_section["init_requested"] = m.group("init_req")
                continue

            # Syslog Deployed (0x02000000)
            m = p6.match(line)
            if m and current_section is ret_dict.get("global"):
                current_section["syslog_deployed"] = m.group("syslog_deployed")
                continue

            # global2 0x190000b7:
            m = p7.match(line)
            if m:
                current_section = ret_dict.setdefault("global2", {})
                current_section["address"] = m.group("addr")
                continue

            # Salt 183
            m = p8.match(line)
            if m and current_section is ret_dict.get("global2"):
                current_section["salt"] = int(m.group("salt"))
                continue

            # Global number of simultaneous packet per session allowed 0
            m = p9.match(line)
            if m and current_section is ret_dict.get("global2"):
                current_section["global_num_simul_pkt_per_sess_allowed"] = int(m.group("val"))
                continue

            # Default number of simultaneous packet per session allowed 25
            m = p10.match(line)
            if m and current_section is ret_dict.get("global2"):
                current_section["default_num_simul_pkt_per_sess_allowed"] = int(m.group("val"))
                continue

            # global3 0x00000009:
            m = p11.match(line)
            if m:
                current_section = ret_dict.setdefault("global3", {})
                current_section["address"] = m.group("addr")
                continue

            # Same Zone Policy (0x00000001)
            m = p12.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["same_zone_policy"] = m.group("val")
                continue

            # vpn zone security (0x00000008)
            m = p13.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["vpn_zone_security"] = m.group("val")
                continue

            # teardowns 0, pam_cce 0x0 00000000
            m = p14.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["teardowns"] = int(m.group("teardowns"))
                current_section["pam_cce"] = m.group("pam")
                continue

            # num zp with policy 1
            m = p15.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["num_zp_with_policy"] = int(m.group("val"))
                continue

            # High priority recycle queue address 0x84969ea0
            m = p16.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["high_priority_recycle_queue_addr"] = m.group("addr")
                continue

            # Low priority recycle queue address 0x84969eb0
            m = p17.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["low_priority_recycle_queue_addr"] = m.group("addr")
                continue

            # Lock upgrades 0
            m = p18.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["lock_upgrades"] = int(m.group("val"))
                continue

            # Half open aggressive aging: 0
            m = p19.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["half_open_aggressive_aging"] = int(m.group("val"))
                continue

            # Num of ACK exceeds limit(5): 0
            m = p20.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["num_ack_exceeds_limit"] = int(m.group("val"))
                continue

            # Num of RST exceeds limit(5) 0
            m = p21.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["num_rst_exceeds_limit"] = int(m.group("val"))
                continue

            # Unknown VRF limit exceeds 0
            m = p22.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["unknown_vrf_limit_exceeds"] = int(m.group("val"))
                continue

            # syncookie over rate cnt 0
            m = p23.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["syncookie_over_rate_cnt"] = int(m.group("val"))
                continue

            # fw tcp session termination RST segment control:
            m = p24.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_fw_rst = current_section.setdefault("fw_tcp_session_termination_rst_segment_control", {})
                continue

            # halfopen: RST sent 0, blocked 0
            m = p25.match(line)
            if m and current_fw_rst is not None:
                state = m.group("state")
                current_fw_rst[state] = {
                    "rst_sent": int(m.group("rst")),
                    "blocked": int(m.group("blocked"))
                }
                continue

            # NAT caching:
            m = p26.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_nat_caching = current_section.setdefault("nat_caching", {})
                continue

            # NAT registration 1
            m = p27.match(line)
            if m and current_nat_caching is not None:
                current_nat_caching["nat_registration"] = int(m.group("val"))
                continue

            # NAT unregistration 1
            m = p28.match(line)
            if m and current_nat_caching is not None:
                current_nat_caching["nat_unregistration"] = int(m.group("val"))
                continue

            # Too many nat sessions 0
            m = p29.match(line)
            if m and current_nat_caching is not None:
                current_nat_caching["too_many_nat_sessions"] = int(m.group("val"))
                continue

            # Can't register with NAT 0
            m = p30.match(line)
            if m and current_nat_caching is not None:
                current_nat_caching["cant_register_with_nat"] = int(m.group("val"))
                continue

            # Invalid nat session 0
            m = p31.match(line)
            if m and current_nat_caching is not None:
                current_nat_caching["invalid_nat_session"] = int(m.group("val"))
                continue

            # No NAT session caching 0
            m = p32.match(line)
            if m and current_nat_caching is not None:
                current_nat_caching["no_nat_session_caching"] = int(m.group("val"))
                continue

            # NAT cached session 0
            m = p33.match(line)
            if m and current_nat_caching is not None:
                current_nat_caching["nat_cached_session"] = int(m.group("val"))
                continue

            # L2 Firewall:
            m = p34.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_l2_firewall = current_section.setdefault("l2_firewall", {})
                continue

            # L2 unknown encap 0
            m = p35.match(line)
            if m and current_l2_firewall is not None:
                current_l2_firewall["l2_unknown_encap"] = int(m.group("val"))
                continue

            # L2 skip tcp pkt 0
            m = p36.match(line)
            if m and current_l2_firewall is not None:
                current_l2_firewall["l2_skip_tcp_pkt"] = int(m.group("val"))
                continue

            # Timer stop failed 0
            m = p37.match(line)
            if m and current_l2_firewall is not None:
                current_l2_firewall["timer_stop_failed"] = int(m.group("val"))
                continue

            # VRF Global Action Block:
            m = p38.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_vrf_block = current_section.setdefault("vrf_global_action_block", {})
                continue

            # L7 Inspection disable flags: 0x0
            m = p39.match(line)
            if m:
                if current_vrf_block is not None:
                    current_vrf_block["l7_inspection_disable_flags"] = m.group("flags")
                elif current_box_block is not None:
                    current_box_block["l7_inspection_disable_flags"] = m.group("flags")
                continue

            # Total Sessions:
            m = p40.match(line)
            if m and current_section is ret_dict.get("global3") and not inside_current_count:
                current_session_block = current_section.setdefault("total_sessions", {})
                current_session_block_name = "total_sessions"
                continue
            if m and inside_current_count and current_section is ret_dict.get("global3"):
                current_session_block = current_current_count.setdefault("total_sessions", None)
                current_session_block_name = "total_sessions"
                continue

            # max limit: 4294967295, current count: 0, exceed: 0
            m = p41.match(line)
            if m and current_session_block_name:
                d = {
                    "max_limit": int(m.group("max")),
                    "current_count": int(m.group("count")),
                    "exceed": int(m.group("exceed"))
                }
                if inside_current_count and current_current_count is not None and current_session_block_name:
                    if current_session_block_name == "total_sessions":
                        current_current_count["total_sessions"] = d["current_count"]
                    elif current_session_block_name == "tcp_syn_cookie":
                        current_current_count.setdefault("tcp_syn_cookie", {}).update(d)
                    elif current_session_block_name == "total_half_open_sessions":
                        current_current_count.setdefault("total_half_open_sessions", {}).update(d)
                    elif current_session_block_name == "tcp_half_open_sessions":
                        current_current_count.setdefault("tcp_half_open_sessions", {}).update(d)
                    elif current_session_block_name == "udp_half_open_sessions":
                        current_current_count.setdefault("udp_half_open_sessions", {}).update(d)
                    elif current_session_block_name == "icmp_half_open_sessions":
                        current_current_count.setdefault("icmp_half_open_sessions", {}).update(d)
                elif current_section is ret_dict.get("global3"):
                    if current_session_block_name == "total_sessions":
                        current_section.setdefault("total_sessions", {}).update(d)
                    elif current_session_block_name == "tcp_syn_cookie":
                        current_section.setdefault("tcp_syn_cookie", {}).update(d)
                    elif current_session_block_name == "total_half_open_sessions":
                        current_section.setdefault("total_half_open_sessions", {}).update(d)
                    elif current_session_block_name == "tcp_half_open_sessions":
                        current_section.setdefault("tcp_half_open_sessions", {}).update(d)
                    elif current_session_block_name == "udp_half_open_sessions":
                        current_section.setdefault("udp_half_open_sessions", {}).update(d)
                    elif current_session_block_name == "icmp_half_open_sessions":
                        current_section.setdefault("icmp_half_open_sessions", {}).update(d)
                continue

            # aggr-age high watermark: 4294967295, low watermark: 0
            m = p42.match(line)
            if m and current_session_block_name:
                d = {
                    "aggr_age_high_watermark": int(m.group("high")),
                    "aggr_age_low_watermark": int(m.group("low"))
                }
                if inside_current_count and current_current_count is not None and current_session_block_name:
                    if current_session_block_name == "total_sessions":
                        current_current_count["aggr_age_high_watermark"] = d["aggr_age_high_watermark"]
                        current_current_count["aggr_age_low_watermark"] = d["aggr_age_low_watermark"]
                    elif current_session_block_name == "total_half_open_sessions":
                        current_current_count.setdefault("total_half_open_sessions", {}).update(d)
                elif current_section is ret_dict.get("global3"):
                    if current_session_block_name == "total_sessions":
                        current_section.setdefault("total_sessions", {}).update(d)
                    elif current_session_block_name == "total_half_open_sessions":
                        current_section.setdefault("total_half_open_sessions", {}).update(d)
                continue

            # num of times enter aggr-age: 0, aggr-age period: off
            m = p43.match(line)
            if m and current_session_block_name:
                d = {
                    "num_times_enter_aggr_age": int(m.group("num")),
                    "aggr_age_period": m.group("period")
                }
                if inside_current_count and current_current_count is not None and current_session_block_name:
                    if current_session_block_name == "total_sessions":
                        current_current_count["num_times_enter_aggr_age"] = d["num_times_enter_aggr_age"]
                        current_current_count["aggr_age_period"] = d["aggr_age_period"]
                    elif current_session_block_name == "total_half_open_sessions":
                        current_current_count.setdefault("total_half_open_sessions", {}).update(d)
                elif current_section is ret_dict.get("global3"):
                    if current_session_block_name == "total_sessions":
                        current_section.setdefault("total_sessions", {}).update(d)
                    elif current_session_block_name == "total_half_open_sessions":
                        current_section.setdefault("total_half_open_sessions", {}).update(d)
                continue

            # TCP SYN Cookie:
            m = p44.match(line)
            if m and current_section is ret_dict.get("global3") and not inside_current_count:
                current_session_block = current_section.setdefault("tcp_syn_cookie", {})
                current_session_block_name = "tcp_syn_cookie"
                continue
            if m and inside_current_count and current_section is ret_dict.get("global3"):
                current_session_block = current_current_count.setdefault("tcp_syn_cookie", {})
                current_session_block_name = "tcp_syn_cookie"
                continue

            # Total Half Open Sessions:
            m = p45.match(line)
            if m and current_section is ret_dict.get("global3") and not inside_current_count:
                current_session_block = current_section.setdefault("total_half_open_sessions", {})
                current_session_block_name = "total_half_open_sessions"
                continue
            if m and inside_current_count and current_section is ret_dict.get("global3"):
                current_session_block = current_current_count.setdefault("total_half_open_sessions", {})
                current_session_block_name = "total_half_open_sessions"
                continue

            # TCP Half Open Sessions:
            m = p46.match(line)
            if m and current_section is ret_dict.get("global3") and not inside_current_count:
                current_session_block = current_section.setdefault("tcp_half_open_sessions", {})
                current_session_block_name = "tcp_half_open_sessions"
                continue
            if m and inside_current_count and current_section is ret_dict.get("global3"):
                current_session_block = current_current_count.setdefault("tcp_half_open_sessions", {})
                current_session_block_name = "tcp_half_open_sessions"
                continue

            # UDP Half Open Sessions:
            m = p47.match(line)
            if m and current_section is ret_dict.get("global3") and not inside_current_count:
                current_session_block = current_section.setdefault("udp_half_open_sessions", {})
                current_session_block_name = "udp_half_open_sessions"
                continue
            if m and inside_current_count and current_section is ret_dict.get("global3"):
                current_session_block = current_current_count.setdefault("udp_half_open_sessions", {})
                current_session_block_name = "udp_half_open_sessions"
                continue

            # ICMP Half Open Sessions:
            m = p48.match(line)
            if m and current_section is ret_dict.get("global3") and not inside_current_count:
                current_session_block = current_section.setdefault("icmp_half_open_sessions", {})
                current_session_block_name = "icmp_half_open_sessions"
                continue
            if m and inside_current_count and current_section is ret_dict.get("global3"):
                current_session_block = current_current_count.setdefault("icmp_half_open_sessions", {})
                current_session_block_name = "icmp_half_open_sessions"
                continue

            # Domain flags: 0x0
            m = p49.match(line)
            if m:
                if inside_current_count and current_current_count is not None:
                    current_current_count["domain_flags"] = m.group("flags")
                elif current_section is ret_dict.get("global3"):
                    current_section["domain_flags"] = m.group("flags")
                continue

            # Box Action Block:
            m = p50.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_box_block = current_section.setdefault("box_action_block", {})
                current_vrf_block = None
                continue

            # Current count::
            m = p51.match(line)
            if m and current_section is ret_dict.get("global3"):
                inside_current_count = True
                current_current_count = current_section.setdefault("current_count", {})
                current_session_block = None
                current_session_block_name = None
                continue

            # Total Sessions 0
            m = p52.match(line)
            if m and inside_current_count and current_current_count is not None:
                current_current_count["total_sessions"] = int(m.group("val"))
                continue

            # aggr-age high watermark: 4294967295, low watermark: 0 (inside current_count)
            m = p42.match(line)
            if m and inside_current_count and current_current_count is not None and not current_session_block_name:
                current_current_count["aggr_age_high_watermark"] = int(m.group("high"))
                current_current_count["aggr_age_low_watermark"] = int(m.group("low"))
                continue

            # num of times enter aggr-age: 0, aggr-age period: off (inside current_count)
            m = p43.match(line)
            if m and inside_current_count and current_current_count is not None and not current_session_block_name:
                current_current_count["num_times_enter_aggr_age"] = int(m.group("num"))
                current_current_count["aggr_age_period"] = m.group("period")
                continue

            # FW persona alert_rlimit: 0, backpressure: 0x0
            m = p53.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["fw_persona_alert_rlimit"] = int(m.group("rlimit"))
                current_section["backpressure"] = m.group("bp")
                continue

            # Invalid RG (exceeds max RG): 0
            m = p54.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["invalid_rg_exceeds_max_rg"] = int(m.group("val"))
                continue

            # Invalid HA message version: 0
            m = p55.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["invalid_ha_message_version"] = int(m.group("val"))
                continue

            # RII Hash Table: address 0x093c9c10 size 128
            m = p56.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["rii_hash_table"] = {
                    "address": m.group("addr"),
                    "size": int(m.group("size"))
                }
                continue

            # VRF Action Table Addr 0x0x1237c000, Size 4096
            m = p57.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["vrf_action_table"] = {
                    "address": m.group("addr"),
                    "size": int(m.group("size"))
                }
                continue

            # AVC stats table index out-of-range 0
            m = p58.match(line)
            if m and current_section is ret_dict.get("global3"):
                current_section["avc_stats_table_index_out_of_range"] = int(m.group("val"))
                continue

            # VRF ID-Name Table:
            m = p59.match(line)
            if m:
                inside_vrf_id_name_table = True
                continue

            # VRF:(id=4106:name=__Platform_iVRF:ID00)
            m = p60.match(line)
            if m and inside_vrf_id_name_table:
                current_vrf_entry = {
                    "id": int(m.group("id")),
                    "name": m.group("name")
                }
                continue

            # vrf_namehash 9f30f5f1fd89b0f0 ipv4 4106, ipv6 65535
            m = p61.match(line)
            if m and inside_vrf_id_name_table and current_vrf_entry:
                current_vrf_entry["vrf_namehash"] = m.group("hash")
                current_vrf_entry["ipv4"] = int(m.group("ipv4"))
                current_vrf_entry["ipv6"] = int(m.group("ipv6"))
                vrf_id_name_list.append(current_vrf_entry)
                current_vrf_entry = None
                continue

            # w_persona: 0x84969ec0 vpn zone table address: 0x13b00400, size 65536
            m = p62.match(line)
            if m:
                ret_dict["w_persona"] = m.group("wpersona")
                ret_dict["vpn_zone_table"] = {
                    "address": m.group("addr"),
                    "size": int(m.group("size"))
                }
                continue

            # VPN to Zone mappings
            m = p63.match(line)
            if m:
                inside_vpn_to_zone = True
                continue

            # vpn: 1 zone: 1
            m = p64.match(line)
            if m and inside_vpn_to_zone:
                vpn_to_zone_list.append({
                    "vpn": int(m.group("vpn")),
                    "zone": int(m.group("zone"))
                })
                continue

            # End of current_count section (when a blank line or a section header is hit)
            if inside_current_count and (line.startswith("VRF ID-Name Table:") or line.startswith("w_persona:") or line.startswith("VPN to Zone mappings") or not line):
                inside_current_count = False
                current_current_count = None
                current_session_block = None
                current_session_block_name = None
                continue

        if vrf_id_name_list:
            ret_dict["vrf_id_name_table"] = vrf_id_name_list
        if vpn_to_zone_list:
            ret_dict["vpn_to_zone_mappings"] = vpn_to_zone_list

        return ret_dict


class ShowPlatformSoftwareIpFpActiveCefSummarySchema(MetaParser):
    """Schema for show platform software ip FP active cef summary"""

    schema = {
        "forwarding_table_summary": {
            "entries": ListOf(
                {
                    "name": str,
                    "vrf_id": int,
                    "table_id": int,
                    "protocol": str,
                    "prefixes": int,
                    "state": str,
                }
            )
        }
    }


class ShowPlatformSoftwareIpFpActiveCefSummary(ShowPlatformSoftwareIpFpActiveCefSummarySchema):
    """Parser for show platform software ip FP active cef summary"""

    cli_command = "show platform software ip FP active cef summary"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        if not output:
            return ret_dict

        entries = []
        # Name             VRF id  Table id    Protocol         Prefixes    State
        p1 = re.compile(
            r"^(?P<name>\S+)\s+(?P<vrf_id>\d+)\s+(?P<table_id>\d+)\s+(?P<protocol>\S+)\s+(?P<prefixes>\d+)\s+(?P<state>.+)$"
        )

        parsing_entries = False

        for line in output.splitlines():
            line = line.rstrip()
            if not line:
                continue

            # Default          0       0           IPv4             2528        hw: 0x55d505991190 (created)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                entry = {
                    "name": group["name"],
                    "vrf_id": int(group["vrf_id"]),
                    "table_id": int(group["table_id"]),
                    "protocol": group["protocol"],
                    "prefixes": int(group["prefixes"]),
                    "state": group["state"].strip(),
                }
                entries.append(entry)
                continue

        if entries:
            ret_dict.setdefault("forwarding_table_summary", {})["entries"] = entries

        return ret_dict


class ShowPlatformSoftwareAdjacencyNexthopIpfrrSchema(MetaParser):
    """Schema for show platform software adjacency nexthop-ipfrr"""
    schema = {
        "static_nexthop_ip_fastreroute": {
            "flags": {
                "primary": str,
                "no_adjacency": str,
                "incomplete_adjacency": str,
                "adjacency": str,
                "adjacency_downloaded": str,
                "adjacency_resolution": str,
                "ipfrr_adjacency_index": str,
            },
            "nexthops": ListOf(
                {
                    "protocol": str,
                    "primary": bool,
                    "adj_id": Or(int, str),
                    "ifnum": int,
                    "address": str,
                    "idx": int,
                    "dl": int,
                    "res": int,
                    "interface": str,
                }
            ),
            "static_nexthop_resolution_timer_sec": int,
            "total_nexthop_adjacency_triggered": int,
        }
    }


class ShowPlatformSoftwareAdjacencyNexthopIpfrr(ShowPlatformSoftwareAdjacencyNexthopIpfrrSchema):
    """Parser for show platform software adjacency nexthop-ipfrr"""

    cli_command = "show platform software adjacency nexthop-ipfrr"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        static_section_found = False

        #  Static Nexthop IP Fast ReRoute:
        p1 = re.compile(r"^\s*Static Nexthop IP Fast ReRoute:$")

        #  Flags: * Primary, - No Adjacency, = Incomplete Adjacency
        p2 = re.compile(
            r"^\s*Flags:\s*(?P<primary>[\*\-=\+A-Za-z]+)\s+Primary,\s*(?P<no_adjacency>[\*\-=\+A-Za-z]+)\s+No Adjacency,\s*(?P<incomplete_adjacency>[\*\-=\+A-Za-z]+)\s+Incomplete Adjacency$"
        )

        #         + Adjacency, DL: Adjacency Downloaded
        p3 = re.compile(
            r"^\s*(?P<adjacency>[\*\-=\+A-Za-z]+)\s+Adjacency,\s*DL:\s+Adjacency Downloaded$"
        )

        #         Res: Adjacency Resolution, Idx: IPFRR Adjacency Index
        p4 = re.compile(
            r"^\s*Res:\s+Adjacency Resolution,\s*Idx:\s+IPFRR Adjacency Index$"
        )

        # Protocol   Adj-ID  Ifnum               Address  Idx    DL  Res  Interface
        p5 = re.compile(
            r"^\s*Protocol\s+Adj-ID\s+Ifnum\s+Address\s+Idx\s+DL\s+Res\s+Interface$"
        )

        # *IP           23     20             100.5.0.2+   1     3    0  Gi0/0/6
        #  IP           85     21             100.6.0.2+   1     3    2  Gi0/0/7
        # *IPv6         56     20 2FF:100::2+   2     3    0  Gi0/0/6
        #  IPv6         82     21 3FF:100::2+   2     3    2  Gi0/0/7
        p6 = re.compile(
            r"^\s*(?P<primary>\*?)\s*(?P<protocol>IP|IPv6)\s+"
            r"(?P<adj_id>[0-9A-Fa-f]+)\s+"
            r"(?P<ifnum>\d+)\s+"
            r"(?P<address>(?:[0-9\.]+|[0-9A-Fa-f:]+)\+)\s+"
            r"(?P<idx>\d+)\s+"
            r"(?P<dl>\d+)\s+"
            r"(?P<res>\d+)\s+"
            r"(?P<interface>\S+)$"
        )

        #  Static nexthop resolution will be triggered in 255 sec
        p7 = re.compile(
            r"^\s*Static nexthop resolution will be triggered in\s+(?P<timer>\d+)\s+sec$"
        )

        #  Total nexthop adjacency triggered 8
        p8 = re.compile(
            r"^\s*Total nexthop adjacency triggered\s+(?P<total>\d+)$"
        )

        for line in out.splitlines():
            #  Static Nexthop IP Fast ReRoute:
            m = p1.match(line)
            if m:
                static_section_found = True
                static_dict = ret_dict.setdefault("static_nexthop_ip_fastreroute", {})
                continue

            if not static_section_found:
                continue

            #  Flags: * Primary, - No Adjacency, = Incomplete Adjacency
            m = p2.match(line)
            if m:
                flags_dict = static_dict.setdefault("flags", {})
                flags_dict["primary"] = m.group("primary")
                flags_dict["no_adjacency"] = m.group("no_adjacency")
                flags_dict["incomplete_adjacency"] = m.group("incomplete_adjacency")
                continue

            #         + Adjacency, DL: Adjacency Downloaded
            m = p3.match(line)
            if m:
                flags_dict = static_dict.setdefault("flags", {})
                flags_dict["adjacency"] = m.group("adjacency")
                flags_dict["adjacency_downloaded"] = "DL"
                continue

            #         Res: Adjacency Resolution, Idx: IPFRR Adjacency Index
            m = p4.match(line)
            if m:
                flags_dict = static_dict.setdefault("flags", {})
                flags_dict["adjacency_resolution"] = "Res"
                flags_dict["ipfrr_adjacency_index"] = "Idx"
                continue

            # Protocol   Adj-ID  Ifnum               Address  Idx    DL  Res  Interface
            m = p5.match(line)
            if m:
                continue  # header, skip

            # *IP           23     20             100.5.0.2+   1     3    0  Gi0/0/6
            #  IP           85     21             100.6.0.2+   1     3    2  Gi0/0/7
            # *IPv6         56     20 2FF:100::2+   2     3    0  Gi0/0/6
            #  IPv6         82     21 3FF:100::2+   2     3    2  Gi0/0/7
            m = p6.match(line)
            if m:
                nexthop = {
                    "protocol": m.group("protocol"),
                    "primary": True if m.group("primary") == "*" else False,
                    "adj_id": int(m.group("adj_id")) if m.group("adj_id").isnumeric() else m.group("adj_id"),
                    "ifnum": int(m.group("ifnum")),
                    "address": m.group("address"),
                    "idx": int(m.group("idx")),
                    "dl": int(m.group("dl")),
                    "res": int(m.group("res")),
                    "interface": m.group("interface"),
                }
                static_dict.setdefault("nexthops", []).append(nexthop)
                continue

            #  Static nexthop resolution will be triggered in 255 sec
            m = p7.match(line)
            if m:
                static_dict["static_nexthop_resolution_timer_sec"] = int(m.group("timer"))
                continue

            #  Total nexthop adjacency triggered 8
            m = p8.match(line)
            if m:
                static_dict["total_nexthop_adjacency_triggered"] = int(m.group("total"))
                continue

        return ret_dict
