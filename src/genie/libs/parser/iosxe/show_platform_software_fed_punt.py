"""show_platform_software_fed_punt.py

    * 'show platform software fed switch active punt cpuq {cpu_q_id}'
    * 'show platform software fed {switch} {mode} punt entries'
    * 'show platform software fed {mode} punt entries'
    * 'show platform software fed switch {switch} punt cpuq brief'
    * 'show platform software fed active punt cpuq brief'
    * 'show platform software fed active punt ios-cause brief'
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


# ==========================================================================
# Schema for 'show platform software fed switch active punt cpuq {cpu_q_id}'
# ==========================================================================
class ShowPlatformSoftwareFedSwitchActivePuntCpuqSchema(MetaParser):
    """Schema for show platform software fed switch active punt cpuq {cpu_q_id}"""

    schema = {
        "punt_cpu_q_statistics": {
            "cpu_q_id": int,
            "cpu_q_name": str,
            "packets_received_from_asic": int,
            "send_to_iosd_total_attempts": int,
            "send_to_iosd_failed_count": int,
            "rx_suspend_count": int,
            "rx_unsuspend_count": int,
            "rx_unsuspend_send_count": int,
            "rx_unsuspend_send_failed_count": int,
            "rx_consumed_count": int,
            "rx_dropped_count": int,
            "rx_non_active_dropped_count": int,
            "rx_conversion_failure_dropped": int,
            "rx_intack_count": int,
            "rx_packets_dq_d_after_intack": int,
            "active_rxq_event": int,
            "rx_spurious_interrupt": int,
            "rx_phy_idb_fetch_failed": int,
            "rx_table_id_fetch_failed": int,
            "rx_invalid_punt_cause": int,
        },
        "replenish_stats_for_all_rxq": {
            "number_of_replenish": int,
            "number_of_replenish_suspend": int,
            "number_of_replenish_unsuspend": int,
        },
    }


# =========================================================================
#  Parser for show platform software fed switch active punt cpuq {cpu_q_id}
# =========================================================================
class ShowPlatformSoftwareFedSwitchActivePuntCpuq(
    ShowPlatformSoftwareFedSwitchActivePuntCpuqSchema
):
    """
    show platform software fed switch active punt cpuq {cpu_q_id}
    """

    cli_command = [
        "show platform software fed {switch} {switch_type} punt cpuq {cpu_q_id}",
        "show platform software fed active punt cpuq {cpu_q_id}",
    ]

    def cli(self, cpu_q_id, switch="", switch_type="active", output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(
                    switch=switch, cpu_q_id=cpu_q_id, switch_type=switch_type
                )
            else:
                cmd = self.cli_command[1].format(cpu_q_id=cpu_q_id)

            output = self.device.execute(cmd)

        ret_dict = {}

        # Punt CPU Q Statistics
        p0 = re.compile(r"Punt CPU Q Statistics$")

        # CPU Q Id                       : 18
        p1 = re.compile(r"CPU Q Id +: +(?P<cpu_q_id>\d+)$")

        # CPU Q Name                     : CPU_Q_TRANSIT_TRAFFIC
        p2 = re.compile(r"^CPU Q Name +: +(?P<cpu_q_name>\S+)$")

        # Packets received from ASIC     : 64564
        p3 = re.compile(
            r"^Packets received from ASIC +: +(?P<packets_received_from_asic>\d+)$"
        )

        # Send to IOSd total attempts    : 64564
        p4 = re.compile(
            r"^Send to IOSd total attempts +: +(?P<send_to_iosd_total_attempts>\d+)$"
        )

        # Send to IOSd failed count      : 0
        p5 = re.compile(
            r"^Send to IOSd failed count +: +(?P<send_to_iosd_failed_count>\d+)$"
        )

        # RX suspend count               : 0
        p6 = re.compile(r"^RX suspend count +: +(?P<rx_suspend_count>\d+)$")

        # RX unsuspend count             : 0
        p7 = re.compile(r"^RX unsuspend count +: +(?P<rx_unsuspend_count>\d+)$")

        # RX unsuspend send count        : 0
        p8 = re.compile(
            r"^RX unsuspend send count +: +(?P<rx_unsuspend_send_count>\d+)$"
        )

        # RX unsuspend send failed count : 0
        p9 = re.compile(
            r"^RX unsuspend send failed count +: +(?P<rx_unsuspend_send_failed_count>\d+)$"
        )

        # RX consumed count              : 0
        p10 = re.compile(r"^RX consumed count +: +(?P<rx_consumed_count>\d+)$")

        # RX dropped count               : 0
        p11 = re.compile(r"^RX dropped count +: +(?P<rx_dropped_count>\d+)$")

        # RX non-active dropped count    : 0
        p12 = re.compile(
            r"^RX non-active dropped count +: +(?P<rx_non_active_dropped_count>\d+)$"
        )

        # RX conversion failure dropped  : 0
        p13 = re.compile(
            r"^RX conversion failure dropped +: +(?P<rx_conversion_failure_dropped>\d+)$"
        )

        # RX INTACK count                : 15377
        p14 = re.compile(r"^RX INTACK count +: +(?P<rx_intack_count>\d+)$")

        # RX packets dq'd after intack   : 0
        p15 = re.compile(
            r"^RX packets dq\'d after intack +: +(?P<rx_packets_dq_d_after_intack>\d+)$"
        )

        # Active RxQ event               : 16723
        p16 = re.compile(r"^Active RxQ event +: +(?P<active_rxq_event>\d+)$")

        # RX spurious interrupt          : 1831
        p17 = re.compile(r"^RX spurious interrupt +: +(?P<rx_spurious_interrupt>\d+)$")

        # RX phy_idb fetch failed: 0
        p18 = re.compile(
            r"^RX phy_idb fetch failed+: +(?P<rx_phy_idb_fetch_failed>\d+)$"
        )

        # RX table_id fetch failed: 0
        p19 = re.compile(
            r"^RX table_id fetch failed+: +(?P<rx_table_id_fetch_failed>\d+)$"
        )

        # RX invalid punt cause: 0
        p20 = re.compile(r"^RX invalid punt cause+: +(?P<rx_invalid_punt_cause>\d+)$")

        # Replenish Stats for all rxq:
        p21 = re.compile(r"Replenish Stats for all rxq:$")

        # Number of replenish            : 20055
        p22 = re.compile(r"^Number of replenish +: +(?P<number_of_replenish>\d+)$")

        # Number of replenish suspend    : 0
        p23 = re.compile(
            r"^Number of replenish suspend +: +(?P<number_of_replenish_suspend>\d+)$"
        )

        # Number of replenish un-suspend : 0
        p24 = re.compile(
            r"^Number of replenish un-suspend +: +(?P<number_of_replenish_unsuspend>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Punt CPU Q Statistics
            m = p0.match(line)
            if m:
                punt_cpu_q_statistics = ret_dict.setdefault("punt_cpu_q_statistics", {})

            # CPU Q Id                       : 18
            m = p1.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["cpu_q_id"] = int(group["cpu_q_id"])

            # CPU Q Name                     : CPU_Q_TRANSIT_TRAFFIC
            m = p2.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["cpu_q_name"] = group["cpu_q_name"]

            # Packets received from ASIC     : 64564
            m = p3.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["packets_received_from_asic"] = int(
                    group["packets_received_from_asic"]
                )

            # Send to IOSd total attempts    : 64564
            m = p4.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["send_to_iosd_total_attempts"] = int(
                    group["send_to_iosd_total_attempts"]
                )

            # Send to IOSd failed count      : 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["send_to_iosd_failed_count"] = int(
                    group["send_to_iosd_failed_count"]
                )

            # RX suspend count               : 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_suspend_count"] = int(
                    group["rx_suspend_count"]
                )

            # RX unsuspend count             : 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_unsuspend_count"] = int(
                    group["rx_unsuspend_count"]
                )

            # RX unsuspend send count        : 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_unsuspend_send_count"] = int(
                    group["rx_unsuspend_send_count"]
                )

            # RX unsuspend send failed count : 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_unsuspend_send_failed_count"] = int(
                    group["rx_unsuspend_send_failed_count"]
                )

            # RX consumed count              : 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_consumed_count"] = int(
                    group["rx_consumed_count"]
                )

            # RX dropped count               : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_dropped_count"] = int(
                    group["rx_dropped_count"]
                )

            # RX non-active dropped count    : 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_non_active_dropped_count"] = int(
                    group["rx_non_active_dropped_count"]
                )

            # RX conversion failure dropped  : 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_conversion_failure_dropped"] = int(
                    group["rx_conversion_failure_dropped"]
                )

            # RX INTACK count                : 15377
            m = p14.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_intack_count"] = int(group["rx_intack_count"])

            # RX packets dq'd after intack   : 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_packets_dq_d_after_intack"] = int(
                    group["rx_packets_dq_d_after_intack"]
                )

            # Active RxQ event               : 16723
            m = p16.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["active_rxq_event"] = int(
                    group["active_rxq_event"]
                )

            # RX spurious interrupt          : 1831
            m = p17.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_spurious_interrupt"] = int(
                    group["rx_spurious_interrupt"]
                )

            # RX phy_idb fetch failed: 0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_phy_idb_fetch_failed"] = int(
                    group["rx_phy_idb_fetch_failed"]
                )

            # RX table_id fetch failed: 0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_table_id_fetch_failed"] = int(
                    group["rx_table_id_fetch_failed"]
                )

            # RX invalid punt cause: 0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                punt_cpu_q_statistics["rx_invalid_punt_cause"] = int(
                    group["rx_invalid_punt_cause"]
                )

            # Replenish Stats for all rxq:
            m = p21.match(line)
            if m:
                replenish_stats_for_all_rxq = ret_dict.setdefault(
                    "replenish_stats_for_all_rxq", {}
                )

            # Number of replenish            : 20055
            m = p22.match(line)
            if m:
                group = m.groupdict()
                replenish_stats_for_all_rxq["number_of_replenish"] = int(
                    group["number_of_replenish"]
                )

            # Number of replenish suspend    : 0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                replenish_stats_for_all_rxq["number_of_replenish_suspend"] = int(
                    group["number_of_replenish_suspend"]
                )

            # Number of replenish un-suspend : 0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                replenish_stats_for_all_rxq["number_of_replenish_unsuspend"] = int(
                    group["number_of_replenish_unsuspend"]
                )

        return ret_dict


class ShowPlatformSoftwareFedPuntEntriesSchema(MetaParser):
    """Schema for show platform software fed {switch} {mode} punt entries"""

    schema = {
        "name": {
            Any(): {
                "source": str,
                "priority": int,
                "tc": int,
                "policy": str,
                "cir_sw": int,
                "cir_hw": int,
                "packets_a": int,
                "bytes_a": int,
                "packets_d": int,
                "bytes_d": int,
            }
        }
    }


class ShowPlatformSoftwareFedPuntEntries(ShowPlatformSoftwareFedPuntEntriesSchema):
    """Parser for show platform software fed {switch} {mode} punt entries"""

    cli_command = [
        "show platform software fed {switch} {mode} punt entries",
        "show platform software fed {mode} punt entries",
    ]

    def cli(self, mode, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        ret_dict = {}

        punt_dict = oper_fill_tabular(
            header_fields=[
                "Source",
                "Name",
                "Pri",
                "TC",
                "Policy",
                "CIR-SW",
                "CIR-HW",
                "Pkts\(A\)",
                "Bytes\(A\)",
                "Pkts\(D\)",
                "Bytes\(D\)",
            ],
            label_fields=[
                "source",
                "name",
                "priority",
                "tc",
                "policy",
                "cir_sw",
                "cir_hw",
                "packets_a",
                "bytes_a",
                "packets_d",
                "bytes_d",
            ],
            device_output=output,
            device_os="iosxe",
            index=[1],
        ).entries

        ret_dict.update({"name": punt_dict})
        for key1 in ret_dict["name"]:
            del ret_dict["name"][key1]["name"]
            for key2 in ret_dict["name"][key1]:
                if key2 != "source" and key2 != "policy":
                    ret_dict["name"][key1][key2] = int(ret_dict["name"][key1][key2])
        return ret_dict


class ShowPlatformSoftwareFedSwitchActivePuntCpuqBriefSchema(MetaParser):
    """Schema for show platform software fed switch active punt cpuq brief schema"""

    schema = {
        "queue_number": {
            Any(): {
                "queue_name": {
                    Any(): {
                        "rx_prev": int,
                        "rx_cur": int,
                        "rx_delta": int,
                        "drop_prev": int,
                        "drop_cur": int,
                        "drop_delta": int,
                    }
                }
            }
        }
    }


class ShowPlatformSoftwareFedSwitchActivePuntCpuqBrief(
    ShowPlatformSoftwareFedSwitchActivePuntCpuqBriefSchema
):
    """Parser for show platform software fed switch active punt cpuq brief
    show platform software fed active punt cpuq brief"""

    cli_command = [
        "show platform software fed {switch} active punt cpuq brief",
        "show platform software fed active punt cpuq brief",
    ]

    def cli(self, switch="", output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch)
            else:
                cmd = self.cli_command[1]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Punt CPU Q Statistics
        p0 = re.compile(r"Punt CPU Q Statistics$")

        # 2  CPU_Q_FORUS_TRAFFIC             44325    44328    3        0        0        0
        p1 = re.compile(
            r"^(?P<queue_number>\d+) +(?P<queue_name>\w+) +(?P<rx_prev>\d+) +(?P<rx_cur>\d+) +(?P<rx_delta>\d+) +(?P<drop_prev>\d+) +(?P<drop_cur>\d+) +(?P<drop_delta>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                queue_number_ = group.pop("queue_number")
                queue_name_ = group.pop("queue_name")
                dir_dict = (
                    ret_dict.setdefault("queue_number", {})
                    .setdefault(queue_number_, {})
                    .setdefault("queue_name", {})
                    .setdefault(queue_name_, {})
                )
                dir_dict.update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchActivePuntBriefSchema(MetaParser):
    """
    Schema for show platform software fed switch active punt ios-cause brief
    """

    schema = {
        "cause_dict": {
            Any(): {
                "cause": int,
                "rcvd": int,
                "dropped": int,
            },
        },
    }


class ShowPlatformSoftwareFedSwitchActivePuntBrief(
    ShowPlatformSoftwareFedSwitchActivePuntBriefSchema
):
    """
    show platform software fed switch active punt ios-cause brief
    """

    cli_command = [
        "show platform software fed {switch} {mode} punt ios-cause brief",
        "show platform software fed active punt ios-cause brief",
    ]

    def cli(self, switch=None, mode=None, output=None):
        if output is None:
            if switch and mode:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        ret_dict = {}
        cause_dict = {}

        # Cause  Cause Info                      Rcvd                 Dropped
        # 0      Reserved                        0                    1
        # 7      ARP request or response         201                  0
        # 55     For-us control                  685                  0
        # 96     Layer2 control protocols        930                  0
        p0 = re.compile(
            r"^(?P<cause>\d+)\s+(?P<cause_info>[\w -]+)\s+(?P<rcvd>\d+)\s+(?P<dropped>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Cause  Cause Info                      Rcvd                 Dropped
            # 0      Reserved                        0                    1
            # 7      ARP request or response         201                  0
            # 55     For-us control                  685                  0
            # 96     Layer2 control protocols        930                  0
            m = p0.match(line)
            if m:
                group = m.groupdict()
                cause_info = group["cause_info"].strip()
                cause_dict = ret_dict.setdefault("cause_dict", {}).setdefault(
                    cause_info, {}
                )
                cause_dict["cause"] = int(group["cause"])
                cause_dict["rcvd"] = int(group["rcvd"])
                cause_dict["dropped"] = int(group["dropped"])
                continue

        return ret_dict