"""show_platform_software.py
    * show platform software status control-processor brief
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or, ListOf

class ShowPlatformSoftwareStatusControlProcessorSchema(MetaParser):
    """Schema for show platform software control-processor brief"""

    schema = {
        "rp_status": {
            "status": str,
            "statistics_updated": str,
        },
        "load_average": {
            "status": str,
            "1_min": {
                "value": float,
                "status": str,
                "threshold": float,
            },
            "5_min": {
                "value": float,
                "status": str,
                "threshold": float,
            },
            "15_min": {
                "value": float,
                "status": str,
                "threshold": float,
            },
        },
        "memory": {
            "status": str,
            "total_kb": int,
            "used_kb": int,
            "used_percentage": int,
            "used_status": str,
            "free_kb": int,
            "free_percentage": int,
            "committed_kb": int,
            "committed_percentage": int,
            "committed_threshold": int,
        },
        "cpu": {
            Any(): {
                "user": float,
                "system": float,
                "nice": float,
                "idle": float,
                "irq": float,
                "sirq": float,
                "iowait": float,
            }
        },
    }

class ShowPlatformSoftwareStatusControlProcessor(ShowPlatformSoftwareStatusControlProcessorSchema):
    """Parser for show platform software control-processor"""

    cli_command = "show platform software control-processor"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # RP0: online, statistics updated 2 seconds ago
        p1 = re.compile(
            r"^RP\d+: +(?P<status>\w+), +statistics +updated +(?P<statistics_updated>.+)$"
        )

        # Load Average: healthy
        p2 = re.compile(r"^Load +Average: +(?P<status>\w+)$")

        # 1-Min: 0.81, status: healthy, under 32.00
        p3 = re.compile(
            r"^(?P<interval>\d+)-Min: +(?P<value>[\d\.]+), +status: +(?P<status>\w+), +under +(?P<threshold>[\d\.]+)$"
        )

        # Memory (kb): healthy
        p4 = re.compile(r"^Memory +\(kb\): +(?P<status>\w+)$")

        # Total: 32586296
        p5 = re.compile(r"^Total: +(?P<total>\d+)$")

        # Used: 3321760 (10%), status: healthy
        p6 = re.compile(
            r"^Used: +(?P<used>\d+) +\((?P<used_percentage>\d+)%\), +status: +(?P<used_status>\w+)$"
        )

        # Free: 29264536 (90%)
        p7 = re.compile(r"^Free: +(?P<free>\d+) +\((?P<free_percentage>\d+)%\)$")

        # Committed: 9506744 (29%), under 95%
        p8 = re.compile(
            r"^Committed: +(?P<committed>\d+) +\((?P<committed_percentage>\d+)%\), +under +(?P<committed_threshold>\d+)%$"
        )

        # CPU0: CPU Utilization (percentage of time spent)
        p9 = re.compile(r"^(?P<cpu>CPU\d+): +CPU +Utilization +\(percentage +of +time +spent\)$")

        # User:  0.79, System:  1.29, Nice:  0.00, Idle: 97.90
        p10 = re.compile(
            r"^User: +(?P<user>[\d\.]+), +System: +(?P<system>[\d\.]+), +Nice: +(?P<nice>[\d\.]+), +Idle: *(?P<idle>[\d\.]+)$"
        )

        # IRQ:  0.00, SIRQ:  0.00, IOwait:  0.00
        p11 = re.compile(
            r"^IRQ: +(?P<irq>[\d\.]+), +SIRQ: +(?P<sirq>[\d\.]+), +IOwait: +(?P<iowait>[\d\.]+)$"
        )

        current_cpu = None

        for line in output.splitlines():
            line = line.strip()

            # RP0: online, statistics updated 2 seconds ago
            m = p1.match(line)
            if m:
                rp_dict = ret_dict.setdefault("rp_status", {})
                rp_dict["status"] = m.groupdict()["status"]
                rp_dict["statistics_updated"] = m.groupdict()["statistics_updated"]
                continue

            # Load Average: healthy
            m = p2.match(line)
            if m:
                load_dict = ret_dict.setdefault("load_average", {})
                load_dict["status"] = m.groupdict()["status"]
                continue

            # 1-Min: 0.81, status: healthy, under 32.00
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interval = group["interval"] + "_min"
                load_dict = ret_dict.setdefault("load_average", {})
                interval_dict = load_dict.setdefault(interval, {})
                interval_dict["value"] = float(group["value"])
                interval_dict["status"] = group["status"]
                interval_dict["threshold"] = float(group["threshold"])
                continue

            # Memory (kb): healthy
            m = p4.match(line)
            if m:
                memory_dict = ret_dict.setdefault("memory", {})
                memory_dict["status"] = m.groupdict()["status"]
                continue

            # Total: 32586296
            m = p5.match(line)
            if m:
                memory_dict = ret_dict.setdefault("memory", {})
                memory_dict["total_kb"] = int(m.groupdict()["total"])
                continue

            # Used: 3321760 (10%), status: healthy
            m = p6.match(line)
            if m:
                group = m.groupdict()
                memory_dict = ret_dict.setdefault("memory", {})
                memory_dict["used_kb"] = int(group["used"])
                memory_dict["used_percentage"] = int(group["used_percentage"])
                memory_dict["used_status"] = group["used_status"]
                continue

            # Free: 29264536 (90%)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                memory_dict = ret_dict.setdefault("memory", {})
                memory_dict["free_kb"] = int(group["free"])
                memory_dict["free_percentage"] = int(group["free_percentage"])
                continue

            # Committed: 9506744 (29%), under 95%
            m = p8.match(line)
            if m:
                group = m.groupdict()
                memory_dict = ret_dict.setdefault("memory", {})
                memory_dict["committed_kb"] = int(group["committed"])
                memory_dict["committed_percentage"] = int(group["committed_percentage"])
                memory_dict["committed_threshold"] = int(group["committed_threshold"])
                continue

            # CPU0: CPU Utilization (percentage of time spent)
            m = p9.match(line)
            if m:
                current_cpu = m.groupdict()["cpu"]
                cpu_dict = ret_dict.setdefault("cpu", {})
                cpu_dict.setdefault(current_cpu, {})
                continue

            # User:  0.79, System:  1.29, Nice:  0.00, Idle: 97.90
            m = p10.match(line)
            if m and current_cpu:
                group = m.groupdict()
                cpu_dict = ret_dict.setdefault("cpu", {})
                current_cpu_dict = cpu_dict.setdefault(current_cpu, {})
                current_cpu_dict["user"] = float(group["user"])
                current_cpu_dict["system"] = float(group["system"])
                current_cpu_dict["nice"] = float(group["nice"])
                current_cpu_dict["idle"] = float(group["idle"])
                continue

            # IRQ:  0.00, SIRQ:  0.00, IOwait:  0.00
            m = p11.match(line)
            if m and current_cpu:
                group = m.groupdict()
                cpu_dict = ret_dict.setdefault("cpu", {})
                current_cpu_dict = cpu_dict.setdefault(current_cpu, {})
                current_cpu_dict["irq"] = float(group["irq"])
                current_cpu_dict["sirq"] = float(group["sirq"])
                current_cpu_dict["iowait"] = float(group["iowait"])
                continue

        return ret_dict
